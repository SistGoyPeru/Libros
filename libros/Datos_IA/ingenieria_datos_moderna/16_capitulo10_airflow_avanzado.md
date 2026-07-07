# Capítulo 10: Airflow Avanzado — TaskFlow, XComs y Sensores

## TaskFlow API (Airflow 2.0+)

La **TaskFlow API** simplifica la creación de DAGs usando decoradores Python:

```python
from airflow.decorators import dag, task
from datetime import datetime, timedelta

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["techstore"],
)
def techstore_pipeline():

    @task
    def extract_orders():
        import sqlite3, pandas as pd
        conn = sqlite3.connect("/opt/airflow/data/techstore.db")
        df = pd.read_sql_query("SELECT * FROM orders", conn)
        conn.close()
        return df.to_dict("records")  # JSON-serializable

    @task
    def transform_orders(orders: list):
        import pandas as pd
        df = pd.DataFrame(orders)
        df["total"] = df["total"].round(2)
        df["order_date"] = pd.to_datetime(df["order_date"]).dt.date
        return df.to_dict("records")

    @task
    def load_orders(orders: list):
        import pandas as pd
        df = pd.DataFrame(orders)
        df.to_parquet("/opt/airflow/data/silver/orders_clean.parquet", index=False)
        print(f"Cargados {len(df)} pedidos")
        return len(df)

    # Flujo implícito
    orders = extract_orders()
    clean = transform_orders(orders)
    count = load_orders(clean)

dag = techstore_pipeline()
```

## XComs — Compartir datos entre tasks

Los **XComs** permiten pasar mensajes entre tasks:

```python
@task
def extract():
    import sqlite3
    conn = sqlite3.connect("/opt/airflow/data/techstore.db")
    count = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    conn.close()
    return {"table": "orders", "rows": count}  # Se guarda automáticamente en XCom

@task
def process(metadata: dict):
    # metadata llega desde XCom automáticamente (TaskFlow)
    print(f"Procesando {metadata['table']}: {metadata['rows']} filas")
    return metadata["rows"]

@task
def notify(row_count: int):
    from airflow.utils.email import send_email
    # Enviar notificación
    print(f"Pipeline completado: {row_count} filas procesadas")
```

### XComs tradicional (sin TaskFlow)

```python
from airflow.operators.python import PythonOperator

def push_xcom(ti):
    ti.xcom_push(key="order_count", value=1234)

def pull_xcom(ti):
    count = ti.xcom_pull(key="order_count", task_ids="extract")
    print(f"Orders: {count}")

extract = PythonOperator(task_id="extract", python_callable=push_xcom)
process = PythonOperator(task_id="process", python_callable=pull_xcom)
extract >> process
```

## BranchPythonOperator — Condicionales

```python
from airflow.operators.python import BranchPythonOperator

def decide_branch(**kwargs):
    import sqlite3
    conn = sqlite3.connect("/opt/airflow/data/techstore.db")
    count = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    conn.close()

    if count == 0:
        return "skip_pipeline"
    return "run_pipeline"

with DAG(...) as dag:
    check = BranchPythonOperator(
        task_id="check_data",
        python_callable=decide_branch,
    )

    skip = BashOperator(task_id="skip_pipeline", bash_command="echo 'Sin datos'")
    run = BashOperator(task_id="run_pipeline", bash_command="echo 'Ejecutando...'")
    end = BashOperator(task_id="end", bash_command="echo 'Fin'", trigger_rule="none_failed_or_skipped")

    check >> [skip, run] >> end
```

## Sensores — Esperar condiciones

Los **sensores** son tasks que esperan hasta que se cumple una condición:

```python
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.sql import SqlSensor
from airflow.sensors.time_delta import TimeDeltaSensor
from airflow.sensors.external_task import ExternalTaskSensor

# Esperar a que llegue un archivo
wait_for_file = FileSensor(
    task_id="wait_for_orders_file",
    filepath="/opt/airflow/data/raw/orders_new.parquet",
    fs_conn_id="fs_default",
    poke_interval=30,  # Revisar cada 30 segundos
    timeout=3600,      # Timeout después de 1 hora
    mode="reschedule", # Libera el slot mientras espera
)

# Esperar a que una tabla tenga datos
wait_for_data = SqlSensor(
    task_id="wait_for_orders",
    conn_id="techstore_db",
    sql="SELECT COUNT(*) FROM orders WHERE order_date = CURRENT_DATE",
    success=lambda row: row[0] > 0,
    poke_interval=60,
    timeout=7200,
)
```

### Sensor personalizado

```python
from airflow.sensors.base import BaseSensorOperator

class MinIOSensor(BaseSensorOperator):
    def __init__(self, bucket: str, key: str, minio_conn_id: str, **kwargs):
        super().__init__(**kwargs)
        self.bucket = bucket
        self.key = key
        self.minio_conn_id = minio_conn_id

    def poke(self, context):
        import boto3
        client = boto3.client("s3",
            endpoint_url="http://minio:9000",
            aws_access_key_id="minioadmin",
            aws_secret_access_key="minioadmin123",
        )
        try:
            client.head_object(Bucket=self.bucket, Key=self.key)
            self.log.info(f"Archivo encontrado: s3://{self.bucket}/{self.key}")
            return True
        except:
            self.log.info(f"Esperando archivo: s3://{self.bucket}/{self.key}")
            return False

# Uso
wait_minio = MinIOSensor(
    task_id="wait_orders_bronze",
    bucket="techstore-bronze",
    key="orders/year=2024/month=1/orders_2024-01-01.parquet",
    poke_interval=30,
    timeout=3600,
)
```

## Task Groups — Organizar tareas

```python
from airflow.utils.task_group import TaskGroup

with DAG(...) as dag:
    start = BashOperator(task_id="start", bash_command="echo 'Inicio'")

    with TaskGroup(group_id="extract_all") as extract_group:
        extract_orders = BashOperator(task_id="orders", bash_command="echo 'Orders'")
        extract_customers = BashOperator(task_id="customers", bash_command="echo 'Customers'")
        extract_products = BashOperator(task_id="products", bash_command="echo 'Products'")

    with TaskGroup(group_id="load_all") as load_group:
        load_bronze = BashOperator(task_id="bronze", bash_command="echo 'Cargando bronze'")
        load_silver = BashOperator(task_id="silver", bash_command="echo 'Cargando silver'")

    end = BashOperator(task_id="end", bash_command="echo 'Fin'")

    start >> extract_group >> load_group >> end
```

## Trigger Rules

Controlan cuándo se ejecuta un task según el estado de sus dependencias:

```python
from airflow.utils.trigger_rule import TriggerRule

end = BashOperator(
    task_id="end",
    bash_command="echo 'Fin'",
    trigger_rule=TriggerRule.ALL_DONE,       # Corre incluso si falla
    # trigger_rule="all_success"             # Default: solo si todo OK
    # trigger_rule="one_success"             # Si al menos uno OK
    # trigger_rule="one_failed"              # Si al menos uno falló
    # trigger_rule="none_failed"             # Ninguno falló
    # trigger_rule="none_failed_or_skipped"  # Ninguno falló o fue skipeado
    # trigger_rule="dummy"                   # Siempre, sin dependencias
)
```

## Backfill — Reprocesar históricos

```python
# CLI
airflow dags backfill techstore_pipeline \
    --start-date 2024-01-01 \
    --end-date 2024-06-30

# O desde la UI: DAG → Trigger DAG w/ config → {"start_date": "2024-01-01", "end_date": "2024-06-30"}
```

## Ejercicios

1. Convierte tu DAG anterior a TaskFlow API con decoradores
2. Crea un sensor que espere a que exista un archivo Parquet en MinIO
3. Usa XComs para pasar el número de pedidos extraídos entre tasks
4. Implementa un BranchPythonOperator que decida si ejecutar la pipeline según la fecha
5. Crea un TaskGroup para "extract_all_tables" con 4 tasks paralelos
6. ¿Qué diferencia hay entre `mode="poke"` y `mode="reschedule"` en un sensor?
7. Usa `trigger_rule="all_done"` para un task de limpieza que siempre se ejecute
8. Ejecuta un backfill para reprocesar enero 2024
9. Crea un sensor personalizado que verifique un registro en SQL
10. ¿Por qué los XComs deben contener datos serializables (JSON)?
