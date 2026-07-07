# Capítulo 12: Data Pipelines con Python y BigQuery

## ¿Qué es un data pipeline?

Un **data pipeline** es un proceso automatizado que mueve datos desde un origen hasta un destino, aplicando transformaciones en el camino. El esquema clásico:

```
Origen → Extraer → Transformar → Cargar → Destino
```

En nuestro contexto:
- **Origen**: SQLite local, APIs, CSVs
- **Transformación**: pandas, SQL en BigQuery
- **Destino**: BigQuery, Cloud Storage

## ETL vs ELT

| Enfoque | Proceso | Cuándo usarlo |
|---------|---------|---------------|
| **ETL** | Extract → Transform → Load | Datos sucios, necesitas limpiar antes de cargar |
| **ELT** | Extract → Load → Transform | Data warehouses modernos (BigQuery). Cargas todo y transformas con SQL |

Con BigQuery usaremos **ELT**: cargamos datos brutos y usamos SQL para transformarlos dentro del warehouse.

## Pipeline 1: Carga diaria desde CSV a BigQuery

```python
"""
pipeline_carga_csv.py
Carga archivos CSV desde una carpeta local a BigQuery.
"""

from google.cloud import bigquery
import pandas as pd
import glob
from datetime import datetime

PROJECT = "techstore-analytics"
DATASET = "techstore_raw"
CARPETA_CSV = "data/ventas_diarias/"

cliente = bigquery.Client(project=PROJECT)

# Asegurar que el dataset existe
dataset_ref = cliente.dataset(DATASET)
try:
    cliente.get_dataset(dataset_ref)
except Exception:
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "us-central1"
    cliente.create_dataset(dataset)
    print(f"Dataset {DATASET} creado")

# Procesar cada CSV
archivos = glob.glob(f"{CARPETA_CSV}*.csv")
print(f"Archivos encontrados: {len(archivos)}")

for archivo in archivos:
    nombre_tabla = f"ventas_{datetime.now().strftime('%Y%m%d')}"

    df = pd.read_csv(archivo)
    print(f"Cargando {archivo}: {len(df)} filas")

    tabla_id = f"{DATASET}.{nombre_tabla}"
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",
        autodetect=True,
    )

    job = cliente.load_table_from_dataframe(df, tabla_id, job_config=job_config)
    job.result()
    print(f"  Cargadas {job.output_rows} filas en {tabla_id}")

print("Pipeline completado.")
```

## Pipeline 2: Transformación con SQL en BigQuery

Una vez que los datos brutos están en BigQuery, creamos tablas transformadas:

```python
"""
pipeline_transformaciones.py
Ejecuta transformaciones SQL en BigQuery.
"""

from google.cloud import bigquery

PROJECT = "techstore-analytics"
DATASET_RAW = "techstore_raw"
DATASET_CURATED = "techstore"

cliente = bigquery.Client(project=PROJECT)

TRANSFORMACIONES = [
    # Ventas diarias consolidadas
    f"""
    CREATE OR REPLACE TABLE {DATASET_CURATED}.ventas_diarias AS
    SELECT
        order_date,
        COUNT(*) AS pedidos,
        COUNT(DISTINCT customer_id) AS clientes_unicos,
        ROUND(SUM(total), 2) AS ingresos,
        ROUND(AVG(total), 2) AS ticket_promedio
    FROM {DATASET_RAW}.orders
    GROUP BY order_date
    ORDER BY order_date
    """,

    # Resumen por categoría
    f"""
    CREATE OR REPLACE TABLE {DATASET_CURATED}.resumen_categorias AS
    SELECT
        p.category,
        COUNT(DISTINCT oi.order_id) AS pedidos,
        SUM(oi.quantity) AS unidades_vendidas,
        ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos,
        ROUND(AVG(oi.unit_price), 2) AS precio_promedio
    FROM {DATASET_RAW}.order_items AS oi
    JOIN {DATASET_RAW}.products AS p ON oi.product_id = p.product_id
    GROUP BY p.category
    ORDER BY ingresos DESC
    """,
]

for i, query in enumerate(TRANSFORMACIONES, 1):
    print(f"Ejecutando transformación {i}...")
    job = cliente.query(query)
    job.result()
    print(f"  Completada ({job.total_bytes_processed / 1e6:.2f} MB procesados)")

print("Todas las transformaciones completadas.")
```

## Pipeline 3: Incremental con checkpoint

Para procesar solo datos nuevos, necesitas un checkpoint (última fecha procesada):

```python
"""
pipeline_incremental.py
Carga incremental: solo procesa datos nuevos desde la última ejecución.
"""

from google.cloud import bigquery
import pandas as pd
from datetime import datetime, timedelta
import json
import os

PROJECT = "techstore-analytics"
DATASET = "techstore"
CHECKPOINT_FILE = "checkpoint.json"

cliente = bigquery.Client(project=PROJECT)


def leer_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE) as f:
            data = json.load(f)
            return datetime.fromisoformat(data["ultima_ejecucion"])
    return datetime.now() - timedelta(days=7)


def guardar_checkpoint(fecha):
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({"ultima_ejecucion": fecha.isoformat()}, f)


# Leer desde dónde continuar
ultima_ejecucion = leer_checkpoint()
fecha_inicio = ultima_ejecucion.strftime("%Y-%m-%d")
fecha_fin = datetime.now().strftime("%Y-%m-%d")

print(f"Procesando pedidos desde {fecha_inicio} hasta {fecha_fin}")

# Consultar solo datos nuevos
query = f"""
    SELECT *
    FROM {DATASET}.orders
    WHERE order_date > '{fecha_inicio}'
      AND order_date <= '{fecha_fin}'
"""

df = cliente.query(query).to_dataframe()
print(f"Nuevos pedidos encontrados: {len(df)}")

# Aquí iría la lógica de transformación/carga
# ...

# Guardar checkpoint
guardar_checkpoint(datetime.now())
print("Pipeline incremental completado.")
```

## Orchestración con Cloud Composer (Airflow)

Para pipelines en producción, necesitas un orquestador. Google Cloud ofrece **Cloud Composer** (Apache Airflow gestionado):

```python
"""
DAG de ejemplo para Cloud Composer.
Este archivo se sube al bucket de Composer.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from google.cloud import bigquery
from datetime import datetime, timedelta

default_args = {
    "owner": "techstore",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def ejecutar_transformaciones():
    cliente = bigquery.Client()
    queries = [
        "CREATE OR REPLACE TABLE techstore.ventas_diarias AS ...",
        "CREATE OR REPLACE TABLE techstore.resumen_categorias AS ...",
    ]
    for query in queries:
        cliente.query(query).result()


with DAG(
    "techstore_pipeline_diario",
    default_args=default_args,
    description="Pipeline diario de TechStore",
    schedule_interval="0 6 * * *",  # Todos los días a las 6 AM
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="ejecutar_transformaciones",
        python_callable=ejecutar_transformaciones,
    )

    t1
```

## Buenas prácticas para pipelines

1. **Idempotencia**: ejecutar el pipeline N veces debe dar el mismo resultado
2. **Monitoreo**: registra cuántas filas se procesaron y cuánto tomó
3. **Alertas**: notificaciones si el pipeline falla (email, Slack)
4. **Versionado**: las transformaciones SQL deben estar en control de versiones
5. **Tests**: prueba cada etapa del pipeline con datos pequeños
6. **Documentación**: cada tabla transformada debe tener definición y linaje

## Ejercicios

1. ¿Cuál es la diferencia entre ETL y ELT? ¿Cuál prefieres para BigQuery?
2. Crea un script Python que lea un CSV y lo cargue a BigQuery
3. ¿Qué es un checkpoint y por qué es importante en pipelines incrementales?
4. Diseña un pipeline ELT para TechStore que genere una tabla de ventas por vendedor
5. ¿Qué es la idempotencia? ¿Cómo la lograrías en una tabla BigQuery?
6. Escribe una transformación SQL que calcule el top 3 productos por mes
7. ¿Para qué sirve Cloud Composer? ¿Qué alternativa más simple existe?
8. Crea un script que verifique que dos tablas en BigQuery tienen el mismo número de filas
9. ¿Qué metadatos registrarías de cada ejecución de pipeline?
10. Implementa un pipeline que cargue datos solo del último mes usando checkpoint
