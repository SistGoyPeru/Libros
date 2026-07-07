# Capítulo 9: Introducción a Apache Airflow

## ¿Qué es Apache Airflow?

**Airflow** es una plataforma open source para programar, orquestar y monitorear workflows (pipelines). Creada por Airbnb en 2014, ahora es el estándar de la industria.

```
Sin Airflow:
  - Scripts Python en cron jobs (difíciles de monitorear)
  - Fallos silentosos (nadie sabe que falló)
  - Dependencias manuales entre scripts

Con Airflow:
  - DAGs visuales con dependencias explícitas
  - Logs centralizados, alertas automáticas
  - Reintentos, backfills, scheduling flexible
```

## Conceptos clave

### DAG (Directed Acyclic Graph)

Un **DAG** es un conjunto de tareas con dependencias. "Acíclico" significa que no puede haber loops (tarea A → B → A).

```
extract ──► transform ──► load ──► done
```

### Task

Cada paso del pipeline es un **task** (operador individual en el DAG).

### Operator

Define QUÉ hace cada task:

| Operator | Propósito |
|----------|-----------|
| `PythonOperator` | Ejecuta una función Python |
| `BashOperator` | Ejecuta un comando bash |
| `PostgresOperator` | Ejecuta SQL en PostgreSQL |
| `DockerOperator` | Corre un contenedor Docker |
| `S3FileTransformOperator` | Transforma archivos en S3 |
| `EmailOperator` | Envía un email |
| `BranchPythonOperator` | Decide qué camino seguir condicionalmente |
| `Sensor` | Espera a que ocurra algo (archivo, API, SQL) |

## Arquitectura de Airflow

```
┌──────────────┐     ┌─────────────────┐
│   Scheduler  │────►│  Metadata DB    │
│  (planifica) │     │  (PostgreSQL)   │
└──────┬───────┘     └────────┬────────┘
       │                      │
       ▼                      ▼
┌──────────────────────────────────────┐
│          Executor                    │
│  (LocalExecutor, CeleryExecutor,     │
│   KubernetesExecutor)                │
└──────┬──────────────────────┬────────┘
       │                      │
       ▼                      ▼
┌──────────────┐     ┌─────────────────┐
│   Worker 1   │     │   Worker 2      │
│  (ejecuta)   │     │  (ejecuta)      │
└──────────────┘     └─────────────────┘
```

Para desarrollo local: `LocalExecutor` + `SQLite` (suficiente).

## Levantar Airflow con Docker

```yaml
# docker-compose-airflow.yml
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres_data:/var/lib/postgresql/data

  airflow-webserver:
    image: apache/airflow:2.10.0
    ports:
      - "8080:8080"
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
    depends_on:
      - postgres
    command: >
      bash -c "airflow db init && airflow users create
      --username admin --password admin --firstname Admin
      --lastname Admin --role Admin --email admin@techstore.com
      && airflow webserver"

  airflow-scheduler:
    image: apache/airflow:2.10.0
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
    depends_on:
      - postgres
    command: airflow scheduler

volumes:
  postgres_data:
```

## Tu primer DAG

```python
# dags/01_hello_techstore.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "techstore",
    "depends_on_past": False,
    "email_on_failure": True,
    "email": ["alerts@techstore.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="techstore_hello",
    description="Primer DAG de TechStore",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["techstore", "example"],
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo 'Iniciando pipeline TechStore'",
    )

    def extract_data():
        import sqlite3, pandas as pd
        conn = sqlite3.connect("/opt/airflow/data/techstore.db")
        df = pd.read_sql_query("SELECT COUNT(*) AS total FROM orders", conn)
        conn.close()
        print(f"Total orders: {df['total'].iloc[0]}")
        return int(df["total"].iloc[0])

    extract = PythonOperator(
        task_id="extract_orders_count",
        python_callable=extract_data,
    )

    end = BashOperator(
        task_id="end",
        bash_command="echo 'Pipeline completado'",
    )

    start >> extract >> end
```

## Schedule en Airflow

```python
# Opciones de schedule
schedule="@daily"           # Diario a medianoche
schedule="@hourly"          # Cada hora
schedule="@weekly"          # Domingo a medianoche
schedule="@monthly"         # 1 del mes a medianoche
schedule="0 6 * * *"       # Cron: 6:00 AM todos los días
schedule="0 8 * * 1-5"     # 8:00 AM lunes a viernes
schedule="0 0 1 * *"       # 1 de cada mes
schedule=None               # Manual (solo trigger)
```

## Variables de Airflow

```bash
# CLI
airflow variables set TECHSTORE_DB_PATH /opt/airflow/data/techstore.db
airflow variables set MINIO_ENDPOINT http://minio:9000
```

```python
from airflow.models import Variable

db_path = Variable.get("TECHSTORE_DB_PATH")
minio_url = Variable.get("MINIO_ENDPOINT")
```

## Conexiones

```bash
# CLI
airflow connections add 'techstore_db' \
    --conn-type 'sqlite' \
    --conn-host '/opt/airflow/data/techstore.db'

airflow connections add 'minio_s3' \
    --conn-type 'aws' \
    --conn-login 'minioadmin' \
    --conn-password 'minioadmin123' \
    --conn-extra '{"endpoint_url": "http://minio:9000"}'
```

## Monitoreo básico

Desde la UI de Airflow (`http://localhost:8080`):

```
DAGs: Lista de todos los DAGs
Graph View: Dependencias visuales
Tree View: Historial de ejecuciones
Gantt: Duración de cada task
Logs: Output de cada task
Code: Código fuente del DAG
```

## Ejercicios

1. Levanta Airflow con Docker (webserver + scheduler + postgres)
2. Crea un DAG simple con 3 tasks: `start → process_data → end`
3. Programa el DAG para ejecutarse diariamente a las 7:00 AM
4. Agrega reintentos: 3 intentos con 2 minutos de espera
5. Usa `Variable.get` para leer la ruta de la base de datos SQLite
6. ¿Qué diferencia hay entre un DAG y un Task en Airflow?
7. Crea un `PythonOperator` que cuente las filas de `customers`
8. ¿Para qué sirve `catchup=False` en un DAG?
9. Explora la UI de Airflow (Graph View, Tree View, Logs)
10. Crea un DAG que se ejecute solo manualmente (sin schedule)
