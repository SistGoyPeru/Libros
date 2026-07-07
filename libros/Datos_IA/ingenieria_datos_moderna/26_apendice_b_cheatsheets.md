# Apéndice B: Cheatsheets de Data Engineering

## Python para Data Engineering

```python
# ===== Path =====
from pathlib import Path
BASE = Path(__file__).parent
Path("data/bronze").mkdir(parents=True, exist_ok=True)
for f in Path("data").rglob("*.parquet"):
    print(f.name)

# ===== Logging =====
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("techstore.pipeline")

# ===== Decoradores =====
from functools import wraps
def retry(max_tries=3, delay=2):
    def dec(f):
        @wraps(f)
        def wrapper(*a, **kw):
            for i in range(1, max_tries+1):
                try: return f(*a, **kw)
                except Exception as e:
                    if i == max_tries: raise
                    time.sleep(delay * i)
        return wrapper
    return dec

# ===== Config =====
import yaml
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)
```

## Parquet

```python
# ===== Escribir =====
import pandas as pd
df.to_parquet("data.parquet", index=False)

import pyarrow as pa
import pyarrow.parquet as pq
table = pa.Table.from_pandas(df)
pq.write_table(table, "data.parquet")

# ===== Particionado =====
df.to_parquet("data/orders/", partition_cols=["year", "month"])

# ===== Leer columnas específicas =====
df = pd.read_parquet("data.parquet", columns=["order_id", "total"])

# ===== Leer con DuckDB =====
import duckdb
df = duckdb.sql("SELECT * FROM 'data/*.parquet'").df()

# ===== Schema =====
schema = pa.schema([
    ("id", pa.int64()),
    ("name", pa.string()),
    ("price", pa.float64()),
])
```

## MinIO (boto3)

```python
import boto3
from botocore.config import Config

s3 = boto3.client("s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin123",
    config=Config(signature_version="s3v4"),
)

# Buckets
s3.create_bucket(Bucket="techstore-bronze")
s3.list_buckets()

# Upload / Download
s3.upload_file("local.parquet", "bucket", "path/remote.parquet")
s3.download_file("bucket", "path/remote.parquet", "local.parquet")

# List
resp = s3.list_objects_v2(Bucket="bucket", Prefix="orders/")
for obj in resp.get("Contents", []):
    print(obj["Key"], obj["Size"])

# Delete
s3.delete_object(Bucket="bucket", Key="path/file.parquet")
```

## dbt

```bash
# Comandos
dbt init project_name      # Crear proyecto
dbt run                    # Ejecutar modelos
dbt run --select model     # Modelo específico
dbt run --select staging+  # staging y dependientes
dbt test                   # Ejecutar tests
dbt test --select model    # Tests de un modelo
dbt deps                   # Instalar paquetes
dbt compile                # Compilar SQL sin ejecutar
dbt docs generate          # Generar docs
dbt docs serve             # Servir docs local
dbt snapshot               # Ejecutar snapshots
dbt debug                  # Verificar conexión
```

```sql
-- dbt SQL patterns
{{ config(materialized='table') }}
{{ config(materialized='incremental', unique_key='id') }}

FROM {{ source('schema', 'table') }}
JOIN {{ ref('other_model') }}

{% if is_incremental() %}
  WHERE date > (SELECT MAX(date) FROM {{ this }})
{% endif %}
```

```yml
# dbt_project.yml
models:
  project:
    staging:
      +materialized: view
      +schema: staging
    marts:
      +materialized: table
```

## Airflow

```python
# DAG básico
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG("dag_id", schedule="@daily",
         start_date=datetime(2024, 1, 1), catchup=False) as dag:
    task1 = PythonOperator(task_id="t1", python_callable=my_func)
    task2 = PythonOperator(task_id="t2", python_callable=my_func)
    task1 >> task2

# TaskFlow
from airflow.decorators import dag, task
@dag(...)
def my_dag():
    @task
    def my_task():
        return "data"
    my_task()

# Operators comunes
BashOperator(task_id="t", bash_command="echo hi")
PythonOperator(task_id="t", python_callable=fn)
FileSensor(task_id="wait", filepath="/path/to/file")
BranchPythonOperator(task_id="branch", python_callable=fn)
```

## Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
USER nobody
CMD ["python", "main.py"]
```

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./data:/app/data
    depends_on:
      - db
  db:
    image: postgres:15
```

## GitHub Actions

```yaml
name: CI
on:
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/
```

## Medallion Architecture

```text
Bronze ───► Silver ───► Gold
(crudo)     (limpio)    (analítico)

Bronze: datos tal cual de la fuente, Parquet
Silver: datos validados, deduplicados, tipados
Gold:   hechos + dimensiones, listos para BI
```

## Conceptos clave

| Concepto | Definición |
|----------|------------|
| DAG | Directed Acyclic Graph — flujo de tareas sin loops |
| Medallion | Arquitectura de datos en 3 capas (bronze/silver/gold) |
| Schema-on-read | Schema se define al leer, no al escribir |
| Columnar | Datos almacenados por columna (Parquet) vs por fila (CSV) |
| Object Storage | Almacenamiento de objetos (S3, GCS, MinIO) |
| ELT | Extract → Load → Transform (vs ETL) |
| Idempotencia | Ejecutar N veces produce el mismo resultado |
| Backfill | Reprocesar datos históricos |
| Freshness | Qué tan actualizados están los datos |
| Lineage | Mapa de dependencias entre datos y transformaciones |
