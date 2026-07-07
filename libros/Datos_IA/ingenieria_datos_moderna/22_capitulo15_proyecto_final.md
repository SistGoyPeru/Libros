# Capítulo 15: Proyecto Final — Data Platform TechStore

## La visión completa

En los proyectos anteriores construiste:
1. **Data Lake** con MinIO y Parquet
2. **Transformaciones** con dbt (bronze → silver → gold)
3. **Orquestación** con Airflow
4. **Contenedores** con Docker
5. **CI/CD** con GitHub Actions

Ahora es momento de integrar todo en una **Data Platform completa** para TechStore.

## Arquitectura final

```
┌────────────────────────────────────────────────────────────────────┐
│                       GITHUB ACTIONS (CI/CD)                       │
│  push → test → build → deploy → trigger pipeline                  │
└────────────────────────────────────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────┐
│                          AIRFLOW                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────────┐ │
│  │ Extract     │  │ dbt Run     │  │ dbt Test    │  │ Notify   │ │
│  │ (Python)    │─►│ (BashOp)    │─►│ (BashOp)    │─►│ (Slack)  │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────────┘ │
└─────────┼────────────────┼────────────────┼───────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌────────────────────────────────────────────────────────────────────┐
│                       DATA LAKE (MinIO)                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐        │
│  │ Bronze       │  │ Silver       │  │ Gold             │        │
│  │ (Parquet     │─►│ (Parquet     │─►│ (DuckDB/Gold    │──► BI  │
│  │  crudo)      │  │  limpio)     │  │  tablas analíticas)      │
│  └──────────────┘  └──────────────┘  └──────────────────┘        │
└────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                        ┌─────────────────────┐
                        │  Power BI / Looker   │
                        │  (Dashboards)        │
                        └─────────────────────┘
```

## Paso 1: Repositorio completo

```
techstore-data-platform/
├── .github/
│   └── workflows/
│       ├── dbt_ci.yml
│       ├── pipeline_ci.yml
│       └── deploy.yml
├── airflow/
│   ├── dags/
│   │   ├── techstore_complete.py
│   │   ├── techstore_health.py
│   │   └── techstore_monitoring.py
│   ├── Dockerfile.airflow
│   └── requirements.txt
├── dbt/
│   └── techstore_dbt/
│       ├── models/
│       │   ├── staging/
│       │   ├── intermediate/
│       │   └── marts/
│       ├── tests/
│       ├── macros/
│       ├── snapshots/
│       ├── dbt_project.yml
│       └── profiles.yml
├── pipelines/
│   ├── extract.py
│   ├── load_to_minio.py
│   └── utils.py
├── config/
│   └── config.yaml
├── tests/
│   └── test_extract.py
├── docker-compose.yml
├── Dockerfile.pipeline
├── .env.example
├── .dockerignore
├── .gitignore
└── README.md
```

## Paso 2: Configuración de variables

```bash
# .env (no commiteado)
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin123
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx/yyy/zzz
DBT_PROFILES_DIR=./dbt/techstore_dbt
TECHSTORE_DB_PATH=./data/techstore.db
```

## Paso 3: DAG de producción final

```python
# airflow/dags/techstore_complete.py
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from datetime import datetime, timedelta
from airflow.models import Variable
import json

DBT_DIR = "/opt/airflow/dbt/techstore_dbt"
DATA_DIR = "/opt/airflow/data"
SLACK_CONN = "slack_default"

default_args = {
    "owner": "techstore",
    "email": ["data-eng@techstore.com"],
    "email_on_failure": True,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    schedule="0 6 * * *",       # 6:00 AM todos los días
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["techstore", "production"],
)
def techstore_production():

    # ── Extract ──
    @task
    def extract_all():
        import sqlite3, pandas as pd
        from pathlib import Path

        tables = ["orders", "customers", "products", "order_items"]
        bronze_dir = Path(f"{DATA_DIR}/bronze")
        bronze_dir.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(f"{DATA_DIR}/techstore.db")
        for table in tables:
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
            path = bronze_dir / f"{table}.parquet"
            df.to_parquet(path, index=False)
        conn.close()
        return {"status": "ok", "tables": tables}

    # ── Load to MinIO ──
    @task
    def load_to_bronze():
        import boto3
        from pathlib import Path

        s3 = boto3.client("s3",
            endpoint_url="http://minio:9000",
            aws_access_key_id="minioadmin",
            aws_secret_access_key="minioadmin123")

        bronze_dir = Path(f"{DATA_DIR}/bronze")
        for f in bronze_dir.glob("*.parquet"):
            s3.upload_file(str(f), "techstore-bronze", f.name)

    # ── dbt pipeline ──
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_DIR} && dbt run --target prod",
        sla=timedelta(hours=1),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_DIR} && dbt test",
    )

    dbt_docs = BashOperator(
        task_id="dbt_docs",
        bash_command=f"cd {DBT_DIR} && dbt docs generate",
    )

    # ── Notifications ──
    @task
    def notify_complete():
        print("✅ Pipeline TechStore completado exitosamente")

    @task
    def notify_failure():
        SlackWebhookOperator(
            task_id="slack_failure",
            slack_webhook_conn_id=SLACK_CONN,
            message="🚨 Pipeline TechStore FALLÓ. Revisar Airflow.",
        ).execute(context={})

    # ── Pipeline flow ──
    extract_result = extract_all()
    extract_result >> load_to_bronze() >> dbt_run >> dbt_test >> dbt_docs
    dbt_docs >> notify_complete()

dag = techstore_production()
```

## Paso 4: README del proyecto

```markdown
# TechStore Data Platform

## Stack
- **Data Lake**: MinIO (S3-compatible) — Parquet
- **Transform**: dbt (DuckDB)
- **Orchestration**: Apache Airflow
- **Container**: Docker
- **CI/CD**: GitHub Actions

## Quick Start
```bash
# 1. Clone
git clone https://github.com/techstore/data-platform.git

# 2. Environment
cp .env.example .env
# Edit .env with your values

# 3. Start services
docker compose up -d

# 4. Access
# Airflow: http://localhost:8080 (admin/admin)
# MinIO:  http://localhost:9001 (minioadmin/minioadmin123)

# 5. Trigger pipeline
# Airflow UI → DAGs → techstore_production → Trigger
```

## Pipeline
| Step | Tool | Description |
|------|------|-------------|
| Extract | Python | SQLite → Parquet |
| Load | Python | Parquet → MinIO (bronze) |
| Transform | dbt | Bronze → Silver → Gold |
| Test | dbt | Schema + data tests |
| Docs | dbt | Auto-generated documentation |
| Notify | Slack | Success/failure alerts |

## Project Structure
(see tree above)
```

## Paso 5: Runbook de operaciones

```markdown
## Runbook: TechStore Data Platform

### Pipeline falló
1. Revisar Airflow → Logs del task que falló
2. Si es error de datos: corregir fuente, rerun
3. Si es error de infraestructura: verificar Docker, MinIO
4. Reprocess: `airflow dags backfill techstore_production -s YYYY-MM-DD`

### dbt test falló
1. Revisar `dbt test --store-failures` para ver registros específicos
2. Corregir modelo o datos fuente
3. `dbt run --select model_name && dbt test --select model_name`

### MinIO caído
1. `docker compose restart minio`
2. Verificar health: `curl http://localhost:9000/minio/health/live`
3. Reprocess data lake: `airflow dags trigger techstore_production`

### Deploy nuevo modelo dbt
1. Crear rama → PR → CI tests automáticos
2. Merge a main → deploy automático
3. Verificar en Airflow que el nuevo modelo se ejecuta
```

## Ejercicios

1. Escribe el README completo de tu Data Platform
2. Crea el docker-compose.yml final con todos los servicios
3. Configura variables de entorno en un `.env` file
4. Crea un runbook con 3 escenarios de fallo comunes
5. ¿Qué métricas de salud monitorearías en producción?
6. Diseña un plan de disaster recovery para la plataforma
7. ¿Cómo escalarías el pipeline para 100 tablas fuente?
8. Prepara una presentación de 5 slides de la arquitectura
9. ¿Qué mejoras harías para el próximo release (v2.0)?
10. Documenta cómo un nuevo miembro del equipo empezaría a trabajar
