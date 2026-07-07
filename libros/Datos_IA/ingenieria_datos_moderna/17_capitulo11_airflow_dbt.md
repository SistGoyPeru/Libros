# Capítulo 11: Integración Airflow + dbt

## El tándem perfecto

dbt transforma datos. Airflow orquesta cuándo y cómo. Juntos forman el corazón del stack moderno de data engineering:

```
Airflow
├── extract_from_sqlite ──► MinIO (bronze)
├── trigger_dbt_run ──────► dbt (bronze → silver → gold)
└── notify_slack ─────────► Alerta de éxito/fallo
```

## Opción 1: BashOperator + dbt CLI

```python
from airflow.operators.bash import BashOperator

run_dbt = BashOperator(
    task_id="dbt_run",
    bash_command="cd /opt/airflow/dbt/techstore_dbt && dbt run",
    env={
        "DBT_PROFILES_DIR": "/opt/airflow/dbt/techstore_dbt",
        "DBT_ENV": "dev",
    },
)
```

### DAG completo

```python
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["techstore", "dbt"],
)
def techstore_dbt_pipeline():

    # 1. Extraer datos a bronze
    @task
    def extract_to_bronze():
        import sqlite3, pandas as pd
        import boto3

        tables = ["orders", "customers", "products", "order_items"]
        s3 = boto3.client("s3", endpoint_url="http://minio:9000",
                          aws_access_key_id="minioadmin",
                          aws_secret_access_key="minioadmin123")

        conn = sqlite3.connect("/opt/airflow/data/techstore.db")
        for table in tables:
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
            local_path = f"/opt/airflow/data/bronze/{table}.parquet"
            df.to_parquet(local_path, index=False)
            s3.upload_file(local_path, "techstore-bronze", f"{table}/{table}_latest.parquet")
        conn.close()

    # 2. Ejecutar dbt
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt/techstore_dbt && dbt run --target dev",
    )

    # 3. Testear dbt
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/dbt/techstore_dbt && dbt test",
    )

    # 4. Generar documentación
    dbt_docs = BashOperator(
        task_id="dbt_docs",
        bash_command="cd /opt/airflow/dbt/techstore_dbt && dbt docs generate",
    )

    extract_to_bronze() >> dbt_run >> dbt_test >> dbt_docs

dag = techstore_dbt_pipeline()
```

## Opción 2: DockerOperator para aislar dbt

```python
from airflow.providers.docker.operators.docker import DockerOperator

dbt_run = DockerOperator(
    task_id="dbt_run",
    image="ghcr.io/dbt-labs/dbt-duckdb:latest",
    command="run",
    api_version="auto",
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(source="/opt/airflow/dbt/techstore_dbt",
              target="/usr/app", type="bind"),
        Mount(source="/opt/airflow/data",
              target="/data", type="bind"),
    ],
    environment={
        "DBT_PROFILES_DIR": "/usr/app",
    },
)
```

## Opción 3: dbt Cloud + Airflow

```python
from airflow.providers.http.operators.http import SimpleHttpOperator

trigger_dbt_cloud_job = SimpleHttpOperator(
    task_id="trigger_dbt_cloud_job",
    http_conn_id="dbt_cloud",
    endpoint="api/v2/accounts/{account_id}/runs/",
    method="POST",
    data=json.dumps({"job_definition_id": 12345}),
    headers={"Content-Type": "application/json", "Authorization": "Bearer YOUR_TOKEN"},
)

check_dbt_cloud_run = SimpleHttpOperator(
    task_id="check_dbt_cloud_run",
    http_conn_id="dbt_cloud",
    endpoint="api/v2/accounts/{account_id}/runs/{run_id}/",
    method="GET",
)
```

## Pipeline completo: Extract → dbt → Notify

```python
@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["techstore"],
)
def techstore_full_pipeline():

    @task
    def extract():
        # Extraer datos a bronze (Parquet en MinIO)
        return {"status": "ok", "tables": ["orders", "customers"]}

    @task
    def run_dbt():
        # Ejecutar dbt run + dbt test
        import subprocess
        result = subprocess.run(
            ["dbt", "run"],
            cwd="/opt/airflow/dbt/techstore_dbt",
            capture_output=True, text=True
        )
        if result.returncode != 0:
            raise Exception(f"dbt failed: {result.stderr}")
        return {"dbt_run": "success"}

    @task
    def notify_slack(status: dict):
        from slack_sdk import WebClient
        client = WebClient(token="xoxb-your-token")
        client.chat_postMessage(
            channel="#data-pipelines",
            text=f"Pipeline TechStore completado: {status}"
        )

    extract_status = extract()
    dbt_status = run_dbt()
    notify_slack(dbt_status)

dag = techstore_full_pipeline()
```

## Buenas prácticas Airflow + dbt

1. **Entornos separados**: dev, staging, prod (cada uno con su target dbt)
2. **Variables de entorno**: no hardcodees rutas ni credenciales
3. **Logging**: configura `dbt run --log-format JSON` para logs estructurados
4. **Alertas**: Slack/Email cuando dbt falle (con el log de error)
5. **Idempotencia**: dbt debe poder ejecutarse múltiples veces sin duplicar datos
6. **Backfills**: Airflow permite reprocesar fechas históricas fácilmente

## Ejercicios

1. Crea un DAG que ejecute `dbt run` usando BashOperator
2. Agrega un task `dbt_test` después de `dbt_run`
3. Usa `DockerOperator` para ejecutar dbt en un contenedor aislado
4. Integra una notificación Slack/email cuando dbt falle
5. ¿Qué ventaja tiene separar extract, dbt y notify en tasks distintos?
6. Crea un DAG con TaskFlow que ejecute dbt y capture el log
7. ¿Por qué es importante la idempotencia en pipelines de datos?
8. Configura un DAG que ejecute dbt solo si el extract fue exitoso
9. ¿Cómo manejarías un fallo en dbt test? ¿Detendrías el pipeline?
10. Diseña un DAG que ejecute 3 modelos dbt en paralelo
