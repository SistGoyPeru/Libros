# Checkpoint 2: Migrar TechStore a BigQuery

## Objetivo

Has aprendido los fundamentos de cloud computing, BigQuery, particionamiento, clustering y cómo conectar Python con BigQuery. Ahora es momento de aplicar todo: **migrar la base de datos TechStore desde SQLite a BigQuery** y validar que los datos sean correctos.

## Requisitos

- Cuenta de Google Cloud con proyecto creado
- BigQuery API habilitada
- gcloud CLI instalado y autenticado
- Python con google-cloud-bigquery instalado
- Archivo `techstore.db` en `codigos/`

## Paso 1: Preparar el dataset en BigQuery

Crea el dataset `techstore` en tu proyecto de GCP:

```bash
bq mk --dataset --location=us-central1 PROJECT_ID:techstore
```

## Paso 2: Ejecutar el script de migración

Crea el archivo `codigos/migrar_techstore_a_bigquery.py` con el siguiente contenido:

```python
"""
migrar_techstore_a_bigquery.py
Migra la base de datos SQLite de TechStore a BigQuery.
"""

import sqlite3
import pandas as pd
from google.cloud import bigquery

# --- Configuración ---
SQLITE_PATH = "techstore.db"
PROJECT = "techstore-analytics"  # CAMBIA por tu Project ID
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

Ejecútalo:

```bash
python codigos/migrar_techstore_a_bigquery.py
```

## Paso 3: Validar la migración

Ejecuta estas consultas en la consola de BigQuery o desde Python para verificar que los datos sean correctos:

```sql
-- Verificar número de filas por tabla
SELECT 'customers' AS tabla, COUNT(*) AS filas FROM techstore.customers
UNION ALL
SELECT 'products', COUNT(*) FROM techstore.products
UNION ALL
SELECT 'orders', COUNT(*) FROM techstore.orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM techstore.order_items
UNION ALL
SELECT 'employees', COUNT(*) FROM techstore.employees;
```

```sql
-- Comparar ingresos totales con el EDA del Libro 1
SELECT
  ROUND(SUM(total), 2) AS ingresos_totales,
  COUNT(*) AS total_pedidos,
  ROUND(AVG(total), 2) AS ticket_promedio
FROM techstore.orders;
```

```sql
-- Top 10 clientes por gasto
SELECT
  c.name,
  c.city,
  COUNT(o.order_id) AS pedidos,
  ROUND(SUM(o.total), 2) AS gasto_total
FROM techstore.orders AS o
JOIN techstore.customers AS c ON o.customer_id = c.customer_id
GROUP BY c.name, c.city
ORDER BY gasto_total DESC
LIMIT 10;
```

```sql
-- Ventas por mes
SELECT
  DATE_TRUNC(order_date, MONTH) AS mes,
  COUNT(*) AS pedidos,
  ROUND(SUM(total), 2) AS ingresos
FROM techstore.orders
GROUP BY mes
ORDER BY mes;
```

## Paso 4: Crear tabla particionada

A partir de los datos migrados, crea una versión optimizada:

```sql
CREATE TABLE techstore.orders_partitioned
PARTITION BY DATE_TRUNC(order_date, MONTH)
CLUSTER BY customer_id
AS
SELECT * FROM techstore.orders;
```

Verifica la reducción de coste:

```sql
-- En la tabla original (sin particionar)
SELECT COUNT(*) FROM techstore.orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';

-- En la tabla particionada
SELECT COUNT(*) FROM techstore.orders_partitioned
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';
```

Compara los "Bytes que se leerán" en la consola antes de ejecutar.

## Paso 5: Automatizar desde Python

Crea `codigos/verificar_migracion.py`:

```python
"""
verificar_migracion.py
Verifica que la migración a BigQuery sea correcta.
Compara totales entre SQLite y BigQuery.
"""

import sqlite3
from google.cloud import bigquery

SQLITE_PATH = "techstore.db"
PROJECT = "techstore-analytics"  # CAMBIA
DATASET = "techstore"

conexion_bq = bigquery.Client(project=PROJECT)
conexion_sqlite = sqlite3.connect(SQLITE_PATH)

TABLAS = ["customers", "products", "orders", "order_items", "employees"]

print("Comparación de filas por tabla:")
print(f"{'Tabla':<15} {'SQLite':<10} {'BigQuery':<10} {'Coinciden':<10}")
print("-" * 50)

for tabla in TABLAS:
    # SQLite
    cursor = conexion_sqlite.execute(f"SELECT COUNT(*) FROM {tabla}")
    count_sqlite = cursor.fetchone()[0]

    # BigQuery
    query = f"SELECT COUNT(*) AS cnt FROM {DATASET}.{tabla}"
    rows = conexion_bq.query(query).result()
    count_bq = list(rows)[0].cnt

    coincide = "✓" if count_sqlite == count_bq else "✗"
    print(f"{tabla:<15} {count_sqlite:<10} {count_bq:<10} {coincide:<10}")

conexion_sqlite.close()
print("\nVerificación completada.")
```

## Entregables del Checkpoint 2

Al completar este checkpoint deberías tener:

- [ ] Dataset `techstore` creado en BigQuery
- [ ] 5 tablas migradas desde SQLite (customers, products, orders, order_items, employees)
- [ ] Script de migración funcionando (`migrar_techstore_a_bigquery.py`)
- [ ] Script de verificación funcionando (`verificar_migracion.py`)
- [ ] Tabla particionada `orders_partitioned` creada
- [ ] Todas las consultas de validación ejecutadas y resultados documentados

## Preguntas de reflexión

1. ¿Cuánto tiempo tomó la migración? ¿Fue más rápido de lo que esperabas?
2. ¿Qué diferencia de coste encontraste entre consultar la tabla original vs la particionada?
3. ¿Qué ventajas ves de tener TechStore en BigQuery vs SQLite para un equipo de 5 analistas?
4. Si tuvieras 50 millones de pedidos en lugar de 6000, ¿cómo cambiaría tu enfoque?

¡Felicidades! TechStore ya está en la nube. En el próximo proyecto conectarás estos datos a Looker Studio para crear dashboards profesionales.
