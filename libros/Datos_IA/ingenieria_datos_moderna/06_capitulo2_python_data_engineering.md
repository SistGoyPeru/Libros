# Capítulo 2: Python para Data Engineering

## Python es el lenguaje del data engineer

No por moda, sino por pragmatismo: Python tiene bibliotecas para todo lo que un data engineer necesita —conexión a bases de datos, procesamiento de archivos, APIs, cloud, orquestación.

En este capítulo repasamos el Python que realmente usas como data engineer.

## Estructura de un proyecto

```
techstore_pipeline/
├── pipelines/          # Código de pipelines
│   ├── __init__.py
│   ├── extract.py      # Extracción de fuentes
│   ├── load.py         # Carga a data lake
│   └── utils.py        # Utilidades compartidas
├── config/
│   └── config.yaml     # Configuración centralizada
├── tests/
│   └── test_pipeline.py
├── requirements.txt
├── Dockerfile
└── .env                 # Variables de entorno
```

## Configuración centralizada

Nunca hardcodees credenciales o rutas. Usa configs y variables de entorno:

```python
# config/config.yaml
database:
  host: localhost
  port: 5432
  name: techstore
  user: ${DB_USER}
  password: ${DB_PASSWORD}

data_lake:
  endpoint: http://localhost:9000
  bucket: techstore-bronze
  access_key: ${MINIO_ACCESS_KEY}
  secret_key: ${MINIO_SECRET_KEY}
```

```python
# config/loader.py
import yaml
import os
from pathlib import Path

def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return _resolve_env_vars(config)

def _resolve_env_vars(obj):
    if isinstance(obj, dict):
        return {k: _resolve_env_vars(v) for k, v in obj.items()}
    if isinstance(obj, str) and obj.startswith("${") and obj.endswith("}"):
        env_var = obj[2:-1]
        return os.environ.get(env_var, "")
    return obj
```

## Logging profesional

`print()` no escala. Usa logging:

```python
import logging
import sys

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# Uso
logger = setup_logger("techstore.pipeline")
logger.info("Iniciando extracción de datos...")
logger.warning("No se encontraron datos para la fecha 2024-06-01")
logger.error("Error de conexión a la base de datos: timeout")
```

## Manejo de errores robusto

Los pipelines fallan. Diseña para que fallen bien:

```python
import time
from functools import wraps

def retry(max_attempts: int = 3, delay: int = 2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(f"Intento {attempt}/{max_attempts} falló: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay * attempt)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def extract_orders(date: str) -> list[dict]:
    # Simula extracción con posible fallo
    pass
```

## Trabajo con archivos y rutas

```python
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
BRONZE_DIR = DATA_DIR / "bronze" / "orders"
SILVER_DIR = DATA_DIR / "silver"

# Crear estructura
BRONZE_DIR.mkdir(parents=True, exist_ok=True)

# Listar archivos por fecha
for parquet_file in BRONZE_DIR.glob("orders_*.parquet"):
    print(f"Procesando: {parquet_file.name}")
```

## Fechas y particionamiento

Los pipelines casi siempre particionan por fecha:

```python
from datetime import datetime, timedelta, date

def get_partition_path(base_path: Path, dt: date) -> Path:
    return base_path / f"year={dt.year}" / f"month={dt.month:02d}" / f"day={dt.day:02d}"

def date_range(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

# Particionar por fecha
start = date(2024, 1, 1)
end = date(2024, 12, 31)
for dt in date_range(start, end):
    path = get_partition_path(BRONZE_DIR, dt)
    print(f"{dt}: {path}")
```

## Pipeline extract simple

```python
import sqlite3
import pandas as pd
from pathlib import Path

def extract_from_sqlite(db_path: str, table: str, output_path: Path) -> Path:
    logger = setup_logger("extract")
    logger.info(f"Extrayendo {table} de {db_path}")

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    conn.close()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)

    logger.info(f"Extraídas {len(df)} filas → {output_path}")
    return output_path

# Uso
extract_from_sqlite(
    db_path="data/techstore.db",
    table="orders",
    output_path=BRONZE_DIR / "orders_2024-01-01.parquet"
)
```

## Ejercicios

1. Crea un logger con formato `[fecha] [nivel] [módulo] mensaje`
2. Escribe una función `load_config` que lea un YAML y resuelva variables de entorno
3. Crea un decorador `@retry` que reintente 5 veces con backoff exponencial
4. Escribe una función que liste los archivos Parquet de un directorio particionado
5. ¿Por qué es importante usar `Path` en lugar de strings para rutas?
6. Crea un script que extraiga `customers` de SQLite y lo guarde como Parquet
7. ¿Qué ventaja tiene la configuración centralizada frente a variables sueltas?
8. Implementa un pipeline que extraiga `order_items` y lo guarde particionado por fecha
9. Escribe una función `safe_execute` que maneje excepciones y loguee el error
10. ¿Por qué usar `functools.wraps` en un decorador?
