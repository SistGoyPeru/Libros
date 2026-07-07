# Checkpoint 3: Orquestación Completa TechStore

## Objetivo

Integrar Airflow y dbt en un pipeline completo: extraer datos desde SQLite a MinIO (bronze), transformarlos con dbt (silver → gold), y generar documentación automática.

## Requisitos

- Airflow funcionando (Docker)
- dbt-core + dbt-duckdb instalados en el contenedor Airflow
- Proyecto dbt de TechStore (Checkpoint 2)
- MinIO con datos en bronze (Checkpoint 1)

## Paso 1: Estructura del proyecto Airflow

```
airflow/
├── dags/
│   └── techstore_complete.py   # DAG principal
├── dbt/
│   └── techstore_dbt/          # Proyecto dbt del Checkpoint 2
├── data/
│   └── techstore.db            # Base de datos fuente
├── docker-compose.yml          # Airflow + Postgres + MinIO
└── requirements.txt            # dbt-core, dbt-duckdb, boto3, pandas
```

## Paso 2: DAG completo

```python
# dags/techstore_complete.py
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from datetime import datetime, timedelta
import os

DBT_DIR = "/opt/airflow/dbt/techstore_dbt"
DATA_DIR = "/opt/airflow/data"

default_args = {
    "owner": "techstore",
    "email": ["data-eng@techstore.com"],
    "email_on_failure": True,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["techstore", "production"],
)
def techstore_complete():

    # ── Step 1: Extract ──
    @task
    def extract_orders():
        import sqlite3, pandas as pd
        conn = sqlite3.connect(f"{DATA_DIR}/techstore.db")
        df = pd.read_sql_query("SELECT * FROM orders", conn)
        conn.close()
        path = f"{DATA_DIR}/bronze/orders.parquet"
        df.to_parquet(path, index=False)
        return {"table": "orders", "rows": len(df), "path": path}

    @task
    def extract_customers():
        import sqlite3, pandas as pd
        conn = sqlite3.connect(f"{DATA_DIR}/techstore.db")
        df = pd.read_sql_query("SELECT * FROM customers", conn)
        conn.close()
        path = f"{DATA_DIR}/bronze/customers.parquet"
        df.to_parquet(path, index=False)
        return {"table": "customers", "rows": len(df), "path": path}

    # ── Step 2: dbt ──
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_DIR} && dbt run --target dev",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_DIR} && dbt test",
    )

    dbt_docs = BashOperator(
        task_id="dbt_docs",
        bash_command=f"cd {DBT_DIR} && dbt docs generate",
    )

    # ── Step 3: Notify ──
    @task
    def notify_success(extract_result: dict):
        print(f"Pipeline completado: {extract_result['table']} - {extract_result['rows']} filas")
        # Opcional: enviar a Slack
        return {"status": "success", "rows": extract_result["rows"]}

    @task
    def notify_failure():
        print("Pipeline falló - revisar logs")

    # ── Dependencies ──
    orders = extract_orders()
    customers = extract_customers()

    [orders, customers] >> dbt_run >> dbt_test >> dbt_docs
    dbt_docs >> notify_success(orders)

dag = techstore_complete()
```

## Paso 3: Docker Compose integrado

```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres_data:/var/lib/postgresql/data

  minio:
    image: minio/minio:latest
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"

  airflow-webserver:
    build:
      context: .
      dockerfile: Dockerfile.airflow
    ports:
      - "8080:8080"
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    volumes:
      - ./dags:/opt/airflow/dags
      - ./dbt:/opt/airflow/dbt
      - ./data:/opt/airflow/data
    depends_on:
      - postgres
      - minio
    command: >
      bash -c "airflow db init && airflow users create
      --username admin --password admin --firstname Admin
      --lastname Admin --role Admin --email admin@techstore.com
      && airflow webserver"

  airflow-scheduler:
    build:
      context: .
      dockerfile: Dockerfile.airflow
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    volumes:
      - ./dags:/opt/airflow/dags
      - ./dbt:/opt/airflow/dbt
      - ./data:/opt/airflow/data
    depends_on:
      - postgres
    command: airflow scheduler

volumes:
  postgres_data:
```

```dockerfile
# Dockerfile.airflow
FROM apache/airflow:2.10.0
RUN pip install dbt-core dbt-duckdb boto3 pandas pyarrow
```

## Paso 4: Notificaciones

```python
# dags/techstore_complete.py (agregar al final del DAG)
    on_failure_callback = SlackWebhookOperator(
        task_id="slack_notify",
        slack_webhook_conn_id="slack_default",
        message="⚠️ Pipeline TechStore falló. Revisar Airflow.",
    )
```

## Entregables del Checkpoint 3

- [ ] Docker Compose con Airflow + Postgres + MinIO
- [ ] DAG `techstore_complete` con extract → dbt → notify
- [ ] dbt run, dbt test, dbt docs generate como tasks separados
- [ ] Extract paralelo de orders y customers
- [ ] Notificación de éxito/fallo
- [ ] Pipeline ejecutándose correctamente en Airflow
- [ ] Documentación dbt generada automáticamente

## Preguntas de reflexión

1. ¿Por qué separar extract, dbt run y dbt test en tasks distintos?
2. ¿Qué ventaja tiene el extract paralelo de orders y customers?
3. ¿Cómo modificarías el pipeline para manejar 50 tablas fuente?
4. ¿Qué métricas de performance monitorearías en este pipeline?
