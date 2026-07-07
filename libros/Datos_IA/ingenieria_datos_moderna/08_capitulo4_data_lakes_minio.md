# Capítulo 4: Data Lakes y Object Storage

## ¿Qué es un Data Lake?

Un **Data Lake** es un repositorio centralizado que almacena datos en su formato nativo (crudo), sin necesidad de schema previo.

```
Data Warehouse:
  Solo datos estructurados, schema-on-write, caro

Data Lake:
  Todos los formatos, schema-on-read, barato (object storage)
```

### Data Lake vs Data Warehouse

| Característica | Data Warehouse | Data Lake |
|---------------|----------------|-----------|
| Datos | Estructurados | Todos (estructurados, semi, no estructurados) |
| Schema | On-write | On-read |
| Formato | Tablas SQL | Archivos (Parquet, Avro, CSV, JSON) |
| Almacenamiento | Costoso ($/GB) | Barato (object storage) |
| Uso | BI, reportes | Data Science, ML, pipelines |
| Mutabilidad | UPDATE/DELETE | Inmutable (nuevas versiones) |

## Object Storage

El object storage es la base de los data lakes modernos:

```
AWS S3 ──► El estándar de la industria
GCS   ──► Google Cloud Storage
Azure ──► Azure Data Lake Storage (ADLS)
MinIO ──► S3-compatible, corre localmente (Docker)
```

### Conceptos clave

```
Bucket ──► Contenedor lógico (como un "disco")
  └── key (ruta del objeto): "bronze/orders/orders_2024-01-01.parquet"
  └── metadata: tipo de contenido, fecha, etiquetas
  └── versiones: cada cambio crea una nueva versión
```

## MinIO — S3 local con Docker

MinIO es un servidor de object storage compatible con la API de S3. Corre en Docker y es perfecto para desarrollo local.

### Levantar MinIO

```yaml
# docker-compose.yml
services:
  minio:
    image: minio/minio:latest
    ports:
      - "9000:9000"   # API S3
      - "9001:9001"   # Consola web
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"
    volumes:
      - minio_data:/data

volumes:
  minio_data:
```

```bash
docker compose up -d
# Consola: http://localhost:9001 (user: minioadmin / pass: minioadmin123)
```

### Python + MinIO (boto3/S3 API)

```python
import boto3
from botocore.config import Config

# Cliente S3 apuntando a MinIO local
s3_client = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin123",
    config=Config(signature_version="s3v4"),
    region_name="us-east-1",
)

# Crear bucket
s3_client.create_bucket(Bucket="techstore-bronze")

# Subir archivo
s3_client.upload_file(
    "data/bronze/orders/orders_2024-01-01.parquet",
    "techstore-bronze",
    "orders/year=2024/month=1/orders_2024-01-01.parquet"
)

# Listar objetos
response = s3_client.list_objects_v2(
    Bucket="techstore-bronze",
    Prefix="orders/year=2024/"
)
for obj in response.get("Contents", []):
    print(f"  {obj['Key']} ({obj['Size']} bytes)")

# Descargar archivo
s3_client.download_file(
    "techstore-bronze",
    "orders/year=2024/month=1/orders_2024-01-01.parquet",
    "data/temp/orders_backup.parquet"
)
```

## Estructura del Data Lake de TechStore

```
techstore-bronze/           # Datos crudos
├── orders/year=2024/month=1/orders_2024-01-01.parquet
├── orders/year=2024/month=1/orders_2024-01-02.parquet
├── customers/customers_full.parquet
└── products/products_full.parquet

techstore-silver/           # Datos limpios
├── orders/year=2024/month=1/
├── customers/
└── products/

techstore-gold/             # Datos listos para negocio
├── fact_orders/
├── dim_customers/
└── dim_products/
```

## Script de carga a MinIO

```python
# pipelines/load_to_minio.py
import boto3
from pathlib import Path
import logging
from config.loader import load_config

logger = logging.getLogger("load_to_minio")

def get_s3_client(config: dict):
    return boto3.client(
        "s3",
        endpoint_url=config["data_lake"]["endpoint"],
        aws_access_key_id=config["data_lake"]["access_key"],
        aws_secret_access_key=config["data_lake"]["secret_key"],
        config=Config(signature_version="s3v4"),
    )

def upload_parquet_to_bronze(local_path: Path, bucket: str, s3_key: str):
    client = get_s3_client(load_config())
    client.upload_file(str(local_path), bucket, s3_key)
    logger.info(f"Subido: {local_path} → s3://{bucket}/{s3_key}")

# Uso
upload_parquet_to_bronze(
    local_path=Path("data/bronze/orders/orders_2024-01-01.parquet"),
    bucket="techstore-bronze",
    s3_key="orders/year=2024/month=1/orders_2024-01-01.parquet"
)
```

## Schema-on-read

El data lake no impone schema al escribir. Lo defines al leer:

```python
import pyarrow.parquet as pq

# Schema implícito (desde el archivo)
table = pq.read_table("s3://techstore-bronze/orders/year=2024/month=1/")

# Schema explícito (forzar tipos)
from pyarrow import parquet as pq, Table
import pyarrow as pa

schema = pa.schema([
    ("order_id", pa.string()),
    ("total", pa.float64()),
    ("status", pa.string()),
])

table = pq.read_table(
    "s3://techstore-bronze/orders/year=2024/month=1/",
    schema=schema  # Solo lee estas columnas
)
```

## Ejercicios

1. Levanta MinIO con Docker y accede a la consola en `http://localhost:9001`
2. Crea los buckets `techstore-bronze`, `techstore-silver`, `techstore-gold`
3. Extrae `orders` de SQLite, conviértelo a Parquet y súbelo a MinIO (bronze)
4. Lista los objetos en `techstore-bronze/` desde Python
5. ¿Cuál es la diferencia entre un bucket y un directorio en MinIO?
6. Descarga un archivo de MinIO y verifica su integridad
7. ¿Qué ventaja tiene schema-on-read frente a schema-on-write?
8. Crea una función `list_bronze_tables()` que liste todas las tablas en bronze
9. Sube `customers` y `products` como Parquet a bronze con partición por fecha
10. ¿Por qué se usa `signature_version="s4v4"` en la configuración de boto3?
