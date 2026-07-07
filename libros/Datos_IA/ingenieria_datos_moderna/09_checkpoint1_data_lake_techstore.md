# Checkpoint 1: Data Lake de TechStore

## Objetivo

Construir el data lake de TechStore con MinIO, aplicando los conceptos de Python para data engineering, formatos de datos (Parquet) y object storage.

## Requisitos

- Docker Desktop instalado
- Python 3.10+ con `boto3`, `pyarrow`, `pandas`, `pyyaml`, `sqlite3`
- Archivo SQLite de TechStore (`techstore.db`)

## Paso 1: Levantar MinIO

```bash
# docker-compose.yml del capítulo 4
docker compose up -d
# Verificar: http://localhost:9001
```

## Paso 2: Estructura del proyecto

```
techstore_data_lake/
├── pipelines/
│   ├── __init__.py
│   ├── extract.py
│   ├── load_to_minio.py
│   └── utils.py
├── config/
│   └── config.yaml
├── docker-compose.yml
├── requirements.txt
└── .env
```

## Paso 3: Configuración

```yaml
# config/config.yaml
database:
  path: data/techstore.db

data_lake:
  endpoint: http://localhost:9000
  bucket_bronze: techstore-bronze
  bucket_silver: techstore-silver
  bucket_gold: techstore-gold
  access_key: ${MINIO_ACCESS_KEY}
  secret_key: ${MINIO_SECRET_KEY}
```

```txt
# .env
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin123
```

## Paso 4: Script de extracción

```python
# pipelines/extract.py
import sqlite3
import pandas as pd
from pathlib import Path
from datetime import date
from config.loader import load_config

def extract_table(table: str, output_dir: Path, dt: date = None) -> Path:
    config = load_config()
    db_path = config["database"]["path"]

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    conn.close()

    if dt:
        path = output_dir / f"{table}_{dt.isoformat()}.parquet"
    else:
        path = output_dir / f"{table}_full.parquet"

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    return path
```

## Paso 5: Script de carga

```python
# pipelines/load_to_minio.py
import boto3
from botocore.config import Config
from pathlib import Path

def upload_file(local_path: Path, bucket: str, s3_key: str):
    client = boto3.client(
        "s3",
        endpoint_url="http://localhost:9000",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin123",
        config=Config(signature_version="s3v4"),
    )
    client.upload_file(str(local_path), bucket, s3_key)

def create_bucket(bucket: str):
    client = boto3.client(
        "s3",
        endpoint_url="http://localhost:9000",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin123",
        config=Config(signature_version="s3v4"),
    )
    client.create_bucket(Bucket=bucket)
```

## Paso 6: Pipeline completo

```python
# run_pipeline.py
from pipelines.extract import extract_table
from pipelines.load_to_minio import upload_file, create_bucket
from config.loader import load_config
from datetime import date
from pathlib import Path

def main():
    config = load_config()
    bronze = config["data_lake"]["bucket_bronze"]

    # Crear buckets si no existen
    for bucket in [bronze, "techstore-silver", "techstore-gold"]:
        create_bucket(bucket)

    # Extraer tablas principales
    today = date.today()
    for table in ["orders", "customers", "products", "order_items"]:
        local_path = extract_table(table, Path("data/extract"), today)
        s3_key = f"{table}/year={today.year}/month={today.month}/{local_path.name}"
        upload_file(local_path, bronze, s3_key)
        print(f"  ✓ {table} → s3://{bronze}/{s3_key}")

if __name__ == "__main__":
    main()
```

## Entregables del Checkpoint 1

- [ ] MinIO corriendo con Docker
- [ ] Buckets creados (bronze, silver, gold)
- [ ] Script de extracción de tablas SQLite a Parquet
- [ ] Script de carga a MinIO
- [ ] Pipeline completo que extrae y carga tablas a bronze
- [ ] Datos accesibles desde la consola MinIO
- [ ] Logging configurado en los scripts

## Preguntas de reflexión

1. ¿Por qué es mejor tener 3 buckets (bronze/silver/gold) que uno solo?
2. ¿Qué ventaja tiene particionar por año/mes en el data lake?
3. ¿Cómo cambiarías el pipeline para manejar tablas con millones de filas?
4. ¿Qué información incluirías en los logs para debugging?

¡Felicidades! Tienes tu primer data lake funcional. En el Proyecto 2 lo transformarás con dbt.
