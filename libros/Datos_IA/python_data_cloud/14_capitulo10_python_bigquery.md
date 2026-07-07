# Capítulo 10: Python + BigQuery — Consultas y Automatización

## La biblioteca google-cloud-bigquery

Python se conecta a BigQuery mediante la biblioteca oficial `google-cloud-bigquery`.

```bash
pip install google-cloud-bigquery google-cloud-storage pandas db-dtypes
```

- `google-cloud-bigquery`: cliente para consultas y gestión
- `google-cloud-storage`: para interactuar con Cloud Storage
- `pandas`: para convertir resultados a DataFrames
- `db-dtypes`: tipos de datos adicionales para compatibilidad pandas

## Conectar y consultar

```python
from google.cloud import bigquery

# Cliente usando Application Default Credentials
cliente = bigquery.Client()

# Consulta simple
query = """
    SELECT
        DATE_TRUNC(order_date, MONTH) AS mes,
        COUNT(*) AS pedidos,
        ROUND(SUM(total), 2) AS ingresos
    FROM techstore.orders
    WHERE order_date >= '2024-01-01'
    GROUP BY mes
    ORDER BY mes
"""

# Ejecutar y obtener resultados como lista de filas
rows = cliente.query(query).result()
for row in rows:
    print(f"{row.mes}: {row.pedidos} pedidos, ${row.ingresos}")
```

## Resultados como DataFrame de pandas

```python
import pandas as pd

query = """
    SELECT c.name, c.city, COUNT(o.order_id) AS pedidos
    FROM techstore.orders AS o
    JOIN techstore.customers AS c USING (customer_id)
    GROUP BY c.name, c.city
    ORDER BY pedidos DESC
    LIMIT 20
"""

df = cliente.query(query).to_dataframe()
print(df.head())
print(f"Shape: {df.shape}")
```

## Parámetros en consultas (SQL injection safe)

```python
from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter

query = """
    SELECT order_date, customer_id, total
    FROM techstore.orders
    WHERE order_date BETWEEN @fecha_inicio AND @fecha_fin
    ORDER BY order_date
"""

job_config = QueryJobConfig(
    query_parameters=[
        ScalarQueryParameter("fecha_inicio", "DATE", "2024-01-01"),
        ScalarQueryParameter("fecha_fin", "DATE", "2024-06-30"),
    ]
)

df = cliente.query(query, job_config=job_config).to_dataframe()
```

## Dry run (estimar coste sin ejecutar)

```python
from google.cloud.bigquery import QueryJobConfig

job_config = QueryJobConfig(dry_run=True)

query = "SELECT * FROM techstore.orders"
job = cliente.query(query, job_config=job_config)

print(f"Bytes a escanear: {job.total_bytes_processed:,}")
print(f"Costo estimado: ${job.total_bytes_processed / 1e12 * 5:.4f} USD")
```

## Cargar datos desde pandas a BigQuery

```python
import pandas as pd

# Suponiendo que ya tienes un DataFrame con los datos
df = pd.read_csv("codigos/techstore_export/orders.csv")

# Configuración de carga
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE",  # Reemplaza la tabla si existe
    autodetect=True,  # Detecta esquema automáticamente
)

# Cargar DataFrame a BigQuery
tabla_id = "techstore.orders_from_pandas"
job = cliente.load_table_from_dataframe(df, tabla_id, job_config=job_config)
job.result()  # Espera a que termine

print(f"Cargadas {job.output_rows} filas en {tabla_id}")
```

## Exportar datos de BigQuery a local

```python
# Consultar y guardar como CSV local
df = cliente.query("""
    SELECT * FROM techstore.orders
    WHERE order_date >= '2024-01-01'
""").to_dataframe()

df.to_csv("codigos/orders_2024_export.csv", index=False)
print(f"Exportadas {len(df)} filas")

# También puedes exportar directamente a GCS
# Exportación directa desde SQL (más eficiente para datasets grandes)
```

## Gestión de tablas desde Python

```python
# Listar datasets
datasets = list(cliente.list_datasets())
for ds in datasets:
    print(f"Dataset: {ds.dataset_id}")

# Listar tablas de un dataset
dataset_ref = cliente.dataset("techstore")
tables = list(cliente.list_tables(dataset_ref))
for table in tables:
    print(f"Tabla: {table.table_id}")

# Obtener metadatos de una tabla
table = cliente.get_table("techstore.orders")
print(f"Filas: {table.num_rows}")
print(f"Tamaño: {table.num_bytes / 1e9:.2f} GB")
print(f"Esquema:")
for field in table.schema:
    print(f"  - {field.name}: {field.field_type}")

# Crear tabla desde Python
schema = [
    bigquery.SchemaField("log_id", "INT64", mode="REQUIRED"),
    bigquery.SchemaField("accion", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("fecha", "DATETIME", mode="REQUIRED"),
    bigquery.SchemaField("usuario", "STRING"),
]
table = bigquery.Table("techstore.audit_logs", schema=schema)
table = cliente.create_table(table)
print(f"Tabla creada: {table.table_id}")
```

## Script completo: migración de TechStore a BigQuery

```python
"""
migrar_techstore_a_bigquery.py
Migra la base de datos SQLite de TechStore a BigQuery.

Uso:
    python migrar_techstore_a_bigquery.py
"""

import sqlite3
import pandas as pd
from google.cloud import bigquery

# --- Configuración ---
SQLITE_PATH = "../codigos/techstore.db"
PROJECT = "techstore-analytics"  # Cambia por tu Project ID
DATASET = "techstore"

TABLAS = [
    "customers",
    "products",
    "orders",
    "order_items",
    "employees",
]

cliente = bigquery.Client(project=PROJECT)

# --- Crear dataset si no existe ---
dataset_ref = cliente.dataset(DATASET)
try:
    cliente.get_dataset(dataset_ref)
    print(f"Dataset {DATASET} ya existe")
except Exception:
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "us-central1"
    cliente.create_dataset(dataset)
    print(f"Dataset {DATASET} creado")

# --- Migrar cada tabla ---
conn = sqlite3.connect(SQLITE_PATH)

for tabla in TABLAS:
    print(f"Migrando {tabla}...")

    # Leer desde SQLite
    df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn)
    print(f"  Filas leídas: {len(df)}")

    # Cargar a BigQuery
    tabla_id = f"{DATASET}.{tabla}"
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    job = cliente.load_table_from_dataframe(df, tabla_id, job_config=job_config)
    job.result()

    # Verificar
    table = cliente.get_table(tabla_id)
    print(f"  Cargadas: {table.num_rows} filas, {table.num_bytes / 1e6:.2f} MB")

conn.close()
print("Migración completada.")
```

## Buenas prácticas con Python + BigQuery

1. **Usa DataFrame para análisis exploratorio**: convierte resultados a pandas, explora, y luego escribe la query optimizada
2. **Siempre usa dry_run** antes de consultas grandes
3. **Usa parámetros** en vez de f-strings para evitar SQL injection
4. **Configura timeout** en consultas largas: `result(timeout=30)`
5. **Agrupa cargas**: mejor cargas grandes y pocas que muchas pequeñas
6. **Usa WRITE_TRUNCATE con cuidado**: borra datos existentes; usa WRITE_APPEND para añadir

## Ejercicios

1. Instala google-cloud-bigquery y pandas en tu entorno
2. Conecta Python a BigQuery y lista los datasets disponibles
3. Ejecuta una consulta que devuelva las 5 categorías más vendidas como DataFrame
4. Usa dry_run para estimar cuánto costaría un SELECT * FROM orders
5. Carga el DataFrame de orders desde SQLite a BigQuery desde Python
6. Escribe una función que reciba una fecha y devuelva las ventas de ese mes
7. Exporta los resultados de una consulta a un archivo CSV local
8. ¿Qué hace `write_disposition="WRITE_APPEND"`? ¿Cuándo lo usarías?
9. Crea una nueva tabla desde Python llamada `daily_summary` con 3 columnas
10. Escribe un script que compare el número de filas de cada tabla entre SQLite y BigQuery
