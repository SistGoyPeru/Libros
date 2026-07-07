# Capítulo 12: Monitoreo, Alertas y SLAs

## ¿Por qué monitorear?

Los pipelines fallan. Es cuestión de cuándo, no de si. Sin monitoreo:

```
Día 1: Pipeline falla a las 3 AM
Día 5: Alguien nota que el dashboard no se actualizó
Día 6: Se descubre el fallo
Día 7: Se repara
→ 7 días sin datos actualizados
```

Con monitoreo:

```
3:00 AM: Pipeline falla
3:01 AM: Alerta en Slack
3:15 AM: Ingeniero recibe alerta en el móvil
3:30 AM: Pipeline reparado y reprocesado
→ 30 minutos de retraso
```

## Alertas por email en Airflow

Configuración nativa de Airflow:

```python
default_args = {
    "owner": "techstore",
    "email": ["data-eng@techstore.com", "alerts@techstore.com"],
    "email_on_failure": True,      # Email cuando un task falla
    "email_on_retry": True,        # Email cuando reintenta
    "email_on_success": False,     # No enviar email en éxito
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}
```

```bash
# Configurar SMTP en airflow.cfg
[smtp]
smtp_host = smtp.gmail.com
smtp_starttls = True
smtp_ssl = False
smtp_user = data-eng@techstore.com
smtp_password = app-password-here
smtp_port = 587
smtp_mail_from = data-eng@techstore.com
```

## Alertas en Slack

```python
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

SLACK_CONN_ID = "slack_techstore"

def send_slack_alert(context):
    dag_id = context["dag"].dag_id
    task_id = context["task"].task_id
    execution_date = context["execution_date"]
    log_url = context["task_instance"].log_url

    message = f"""
⚠️ Pipeline Falló
• DAG: {dag_id}
• Task: {task_id}
• Fecha: {execution_date}
• Logs: {log_url}
    """

    SlackWebhookOperator(
        task_id="slack_alert",
        slack_webhook_conn_id=SLACK_CONN_ID,
        message=message,
    ).execute(context=context)
```

```python
# Usar en DAG
with DAG(
    dag_id="techstore_pipeline",
    default_args=default_args,
    on_failure_callback=send_slack_alert,  # Callback global
) as dag:
    ...
```

## SLA (Service Level Agreements)

Los **SLAs** definen el tiempo máximo que un task puede tardar:

```python
from airflow.operators.python import PythonOperator

extract = PythonOperator(
    task_id="extract_orders",
    python_callable=extract_orders,
    sla=timedelta(hours=2),  # Debe completar en ≤ 2 horas
)

# Si el SLA se incumple:
# 1. Se envía email de SLA miss
# 2. Aparece en la UI con icono de alerta
# 3. Se registra en task_instance.sla_miss
```

### Configurar SLA

```python
# airflow.cfg
[email]
email_backend = airflow.utils.email.send_email_smtp

[sla]
sla_miss_callback = techstore_monitoring.sla_callback
default_sla = timedelta(hours=4)
```

## Monitoreo con logs estructurados

```python
import json
import logging

# Logger estructurado (JSON)
logger = logging.getLogger("techstore.pipeline")

def log_event(event_type: str, **kwargs):
    log_entry = {
        "event": event_type,
        "pipeline": "techstore",
        **kwargs
    }
    logger.info(json.dumps(log_entry))

# Uso
log_event("extract_complete", table="orders", rows=5678, duration_sec=12.3)
log_event("dbt_run", model_count=15, test_count=30, tests_passed=30)
log_event("pipeline_failed", error="Connection timeout", duration_sec=120)
```

## Pool de recursos

Airflow permite limitar concurrencia con **Pools**:

```bash
# CLI
airflow pools set extract_pool 2 "Máximo 2 extract simultáneos"
airflow pools set dbt_pool 1 "Solo 1 dbt run a la vez"
```

```python
extract = PythonOperator(
    task_id="extract_orders",
    python_callable=extract_orders,
    pool="extract_pool",
    pool_slots=1,
)
```

## SLAs por DAG

```python
from airflow.models.dag import DAG
from datetime import timedelta

dag = DAG(
    dag_id="techstore_sla_example",
    schedule="@daily",
    default_args={
        "sla": timedelta(hours=3),  # SLA global
    },
    sla_miss_callback=slack_sla_miss,  # Callback específico
)
```

## Monitoreo externo

### Health checks

```python
# dags/health_check.py
from airflow.decorators import dag, task
from datetime import datetime

@dag(schedule="*/5 * * * *", start_date=datetime(2024, 1, 1), catchup=False)
def techstore_health_check():

    @task
    def check_minio():
        import boto3
        client = boto3.client("s3", endpoint_url="http://minio:9000",
                              aws_access_key_id="minioadmin",
                              aws_secret_access_key="minioadmin123")
        buckets = client.list_buckets()
        assert len(buckets["Buckets"]) > 0
        return {"minio": "ok"}

    @task
    def check_dbt():
        import subprocess
        result = subprocess.run(["dbt", "--version"], capture_output=True, text=True)
        assert result.returncode == 0
        return {"dbt": "ok"}

    @task
    def check_db():
        import sqlite3
        conn = sqlite3.connect("/opt/airflow/data/techstore.db")
        conn.execute("SELECT 1")
        conn.close()
        return {"sqlite": "ok"}

    [check_minio(), check_dbt(), check_db()]

dag = techstore_health_check()
```

## Dashboard de monitoreo

Crea un DAG que genere métricas de pipeline:

```python
@task
def collect_metrics():
    from airflow.models import DagRun, TaskInstance
    from airflow.utils.state import State

    # Estado de los últimos 30 DAG runs
    dag_runs = DagRun.find(dag_id="techstore_pipeline")
    successes = sum(1 for dr in dag_runs if dr.state == State.SUCCESS)
    failures = sum(1 for dr in dag_runs if dr.state == State.FAILED)

    return {
        "total_runs": len(dag_runs),
        "success_rate": successes / len(dag_runs) * 100,
        "failures": failures,
    }
```

## Ejercicios

1. Configura alertas por email cuando un DAG falle
2. Crea un callback `on_failure_callback` que envíe una alerta a Slack
3. Define un SLA de 30 minutos para el task `dbt_run`
4. Crea un health check DAG que verifique MinIO, dbt y SQLite cada 5 minutos
5. ¿Qué diferencia hay entre `retries` y `sla` en Airflow?
6. Implementa un logger estructurado (JSON) para el pipeline
7. Configura un Pool para limitar a 1 tarea de dbt simultánea
8. ¿Por qué es importante tener un DAG de health check separado?
9. Crea un task que coleccione métricas semanales del pipeline
10. Diseña un flujo de alertas: fallo → Slack → Email → Reprocesamiento automático
