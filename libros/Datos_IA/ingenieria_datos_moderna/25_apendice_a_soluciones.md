# Apéndice A: Soluciones a los Ejercicios

## Capítulo 1: Introducción al Data Engineering

**Ejercicio 3 — ¿Por qué Parquet es mejor que CSV para un data lake?**

1. **Tamaño**: Parquet comprime datos columnarmente (90% menos espacio)
2. **Velocidad**: solo lee las columnas necesarias
3. **Schema**: el schema está incrustado, no hay parsing de tipos
4. **Particionamiento**: soporte nativo Hive-style

## Capítulo 2: Python para Data Engineering

**Ejercicio 3 — Decorador @retry con backoff exponencial:**

```python
import time
from functools import wraps

def retry(max_attempts=5, base_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    delay = base_delay * (2 ** (attempt - 1))
                    print(f"Intento {attempt} falló. Reintentando en {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator
```

## Capítulo 3: Formatos de Datos

**Ejercicio 1 — Comparación CSV vs Parquet:**

```python
import pandas as pd, sqlite3, os

conn = sqlite3.connect("data/techstore.db")
df = pd.read_sql_query("SELECT * FROM orders", conn)
conn.close()

df.to_csv("orders.csv", index=False)
df.to_parquet("orders.parquet", index=False)

csv_size = os.path.getsize("orders.csv")
parquet_size = os.path.getsize("orders.parquet")
print(f"CSV: {csv_size / 1024:.0f} KB")
print(f"Parquet: {parquet_size / 1024:.0f} KB")
print(f"Parquet es {csv_size / parquet_size:.1f}x más pequeño")
```

## Capítulo 4: Data Lakes y MinIO

**Ejercicio 6 — Descargar archivo y verificar integridad:**

```python
import boto3, hashlib

s3 = boto3.client("s3", endpoint_url="http://localhost:9000",
                  aws_access_key_id="minioadmin",
                  aws_secret_access_key="minioadmin123")

# Descargar
s3.download_file("techstore-bronze", "orders/orders_latest.parquet", "download.parquet")

# Verificar checksum (opcional)
md5 = hashlib.md5()
with open("download.parquet", "rb") as f:
    md5.update(f.read())
print(f"MD5: {md5.hexdigest()}")
```

## Capítulo 5: Introducción a dbt

**Ejercicio 2 — Staging model de customers:**

```sql
-- models/staging/stg_customers.sql
{{ config(materialized='view') }}

SELECT
    customer_id,
    TRIM(name) AS customer_name,
    LOWER(TRIM(email)) AS email,
    TRIM(city) AS city,
    TRIM(country) AS country,
    CAST(registration_date AS DATE) AS registration_date
FROM {{ source('techstore', 'customers') }}
```

## Capítulo 6: Modelado en dbt

**Ejercicio 3 — Intermediate model int_product_sales:**

```sql
-- models/intermediate/int_product_sales.sql
{{ config(materialized='view') }}

SELECT
    oi.product_id,
    p.product_name,
    p.category,
    COUNT(DISTINCT oi.order_id) AS pedidos,
    SUM(oi.quantity) AS unidades_vendidas,
    SUM(oi.line_total) AS ingresos
FROM {{ ref('stg_order_items') }} oi
JOIN {{ ref('stg_products') }} p ON oi.product_id = p.product_id
GROUP BY oi.product_id, p.product_name, p.category
```

## Capítulo 7: Testing en dbt

**Ejercicio 3 — Data test para totales negativos:**

```sql
-- tests/assert_no_negative_totals.sql
SELECT order_id, total
FROM {{ ref('stg_orders') }}
WHERE total < 0
```

## Capítulo 8: dbt Avanzado

**Ejercicio 2 — Surrogate key con dbt_utils:**

```sql
-- models/marts/fact_orders.sql
SELECT
    {{ dbt_utils.generate_surrogate_key(['order_id']) }} AS order_sk,
    order_id,
    customer_id,
    order_date,
    total,
    status
FROM {{ ref('stg_orders') }}
```

## Capítulo 9: Introducción a Airflow

**Ejercicio 2 — DAG con 3 tasks:**

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("simple_pipeline", schedule="@daily",
         start_date=datetime(2024, 1, 1), catchup=False) as dag:

    start = BashOperator(task_id="start", bash_command="echo 'Inicio'")
    process = BashOperator(task_id="process", bash_command="echo 'Procesando...'")
    end = BashOperator(task_id="end", bash_command="echo 'Fin'")

    start >> process >> end
```

## Capítulo 10: Airflow Avanzado

**Ejercicio 2 — Sensor para Parquet en MinIO:**

```python
from airflow.sensors.base import BaseSensorOperator

class ParquetSensor(BaseSensorOperator):
    def __init__(self, bucket, prefix, **kwargs):
        super().__init__(**kwargs)
        self.bucket = bucket
        self.prefix = prefix

    def poke(self, context):
        import boto3
        s3 = boto3.client("s3", endpoint_url="http://minio:9000",
                          aws_access_key_id="minioadmin",
                          aws_secret_access_key="minioadmin123")
        resp = s3.list_objects_v2(Bucket=self.bucket, Prefix=self.prefix)
        files = [o for o in resp.get("Contents", []) if o["Key"].endswith(".parquet")]
        return len(files) > 0
```

## Capítulo 11: Airflow + dbt

**Ejercicio 4 — Notificación Slack en fallo:**

```python
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

def notify_slack_failure(context):
    SlackWebhookOperator(
        task_id="slack_alert",
        slack_webhook_conn_id="slack_default",
        message=f"❌ Pipeline falló: {context['dag'].dag_id}.{context['task'].task_id}",
    ).execute(context=context)
```

## Capítulo 12: Monitoreo

**Ejercicio 3 — SLA de 30 minutos para dbt_run:**

```python
dbt_run = BashOperator(
    task_id="dbt_run",
    bash_command="dbt run",
    sla=timedelta(minutes=30),
)
```

## Capítulo 13: Docker

**Ejercicio 1 — Dockerfile para pipeline:**

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY pipelines/ ./pipelines/
COPY config/ ./config/
COPY run_pipeline.py .
CMD ["python", "run_pipeline.py"]
```

## Capítulo 14: CI/CD

**Ejercicio 1 — Workflow dbt compile en PR:**

```yaml
name: dbt Compile
on:
  pull_request:
    paths: ['dbt/**']
jobs:
  compile:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install dbt-core dbt-duckdb
      - run: dbt deps && dbt compile
        working-directory: dbt/techstore_dbt
```

## Capítulo 15: Proyecto Final

**Ejercicio 6 — Plan de disaster recovery:**

1. **Backup diario** del warehouse DuckDB y configuración de Airflow
2. **docker compose down** + **docker compose up** para reinicio completo
3. **dbt snapshot** para datos que cambian (SCD2)
4. **Backfill** automático vía Airflow si se detecta data faltante
5. **Repositorio Git** como source of truth: todo es reproducible
