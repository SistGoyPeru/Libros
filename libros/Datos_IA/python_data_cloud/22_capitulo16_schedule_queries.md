# Capítulo 16: Schedule Queries y Pipelines Automáticos

## Automatización sin servidores

No todo necesita Cloud Functions. BigQuery ofrece herramientas de automatización integradas que no requieren código:

1. **Schedule Queries**: ejecuta consultas SQL automáticamente en un horario
2. **Cloud Scheduler**: programa cualquier tarea (incluyendo invocar Cloud Functions)
3. **Workflows**: orquesta servicios de GCP en secuencia

## Scheduled Queries en BigQuery

Las **Scheduled Queries** ejecutan automáticamente consultas SQL en un horario definido y guardan los resultados en una tabla.

### Crear una consulta programada

```sql
-- Consulta que se ejecutará diariamente
-- Guarda el resumen diario de ventas
CREATE OR REPLACE TABLE techstore.resumen_diario AS
SELECT
  CURRENT_DATE() AS fecha_ejecucion,
  DATE(order_date) AS fecha_venta,
  COUNT(*) AS pedidos,
  COUNT(DISTINCT customer_id) AS clientes_unicos,
  ROUND(SUM(total), 2) AS ingresos,
  ROUND(AVG(total), 2) AS ticket_promedio
FROM techstore.orders
WHERE DATE(order_date) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
GROUP BY fecha_venta;
```

Para programarla:
1. En la consola de BigQuery, ejecuta la consulta
2. Haz clic en "Programar" → "Nueva programación"
3. Configura:
   - **Nombre**: `resumen_diario_techstore`
   - **Frecuencia**: Diario
   - **Hora**: 03:00 (madrugada, menor coste)
   - **Destino**: `techstore.resumen_diario`
   - **Opción de escritura**: `WRITE_APPEND`
4. Guarda

### Consulta recurrente con partición por fecha

```sql
-- Resumen semanal
CREATE OR REPLACE TABLE techstore.resumen_semanal AS
SELECT
  DATE_TRUNC(order_date, WEEK(MONDAY)) AS semana_inicio,
  DATE_ADD(DATE_TRUNC(order_date, WEEK(MONDAY)), INTERVAL 6 DAY) AS semana_fin,
  COUNT(*) AS pedidos,
  ROUND(SUM(total), 2) AS ingresos,
  ROUND(AVG(total), 2) AS ticket_promedio,
  ROUND(SUM(total) / COUNT(DISTINCT customer_id), 2) AS ingresos_por_cliente
FROM techstore.orders
WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 12 WEEK)
GROUP BY semana_inicio
ORDER BY semana_inicio;
```

## Cloud Scheduler + Cloud Functions

Cloud Scheduler es un servicio de cron gestionado. Puede invocar una Cloud Function HTTP en un horario.

### Ejemplo: Informe diario por email

1. Crea una Cloud Function que genere un resumen y lo envíe por email (o lo guarde en GCS)

```python
"""
funcion_informe_diario/main.py
Cloud Function: genera informe diario y lo guarda en GCS.
"""

from google.cloud import bigquery, storage
from datetime import date, timedelta
import pandas as pd

PROJECT = "techstore-analytics"
DATASET = "techstore"
BUCKET_INFORMES = "techstore-informes"

cliente_bq = bigquery.Client(project=PROJECT)
cliente_gcs = storage.Client()


def generar_informe_diario(request=None):
    """Genera informe diario y lo guarda en Cloud Storage."""
    ayer = date.today() - timedelta(days=1)
    mes = ayer.strftime("%Y%m")
    dia = ayer.strftime("%Y%m%d")

    # Consultar ventas de ayer
    query = f"""
        SELECT
            DATE(order_date) AS fecha,
            COUNT(*) AS pedidos,
            ROUND(SUM(total), 2) AS ingresos,
            p.category,
            COUNT(DISTINCT o.customer_id) AS clientes
        FROM {DATASET}.orders AS o
        JOIN {DATASET}.order_items AS oi ON o.order_id = oi.order_id
        JOIN {DATASET}.products AS p ON oi.product_id = p.product_id
        WHERE DATE(order_date) = '{ayer.isoformat()}'
        GROUP BY fecha, p.category
        ORDER BY ingresos DESC
    """

    df = cliente_bq.query(query).to_dataframe()

    # Guardar como CSV en GCS
    ruta = f"diarios/{mes}/informe_{dia}.csv"
    bucket = cliente_gcs.bucket(BUCKET_INFORMES)
    blob = bucket.blob(ruta)
    blob.upload_from_string(df.to_csv(index=False), content_type="text/csv")

    # Guardar también como Excel (usando pandas ExcelWriter)
    ruta_excel = f"diarios/{mes}/informe_{dia}.xlsx"
    blob_excel = bucket.blob(ruta_excel)
    with blob_excel.open("wb") as f:
        df.to_excel(f, index=False, sheet_name="Ventas Diarias")

    return f"Informe {dia} generado: {len(df)} categorías"
```

2. Crea un trabajo en Cloud Scheduler:

```bash
# Crear trabajo que ejecute la función cada día a las 7 AM
gcloud scheduler jobs create http informe-diario \
    --schedule="0 7 * * *" \
    --uri="https://REGION-PROJECT.cloudfunctions.net/generar-informe-diario" \
    --http-method=GET \
    --time-zone="America/Lima" \
    --location=us-central1
```

## Workflows: orquestación visual

**Workflows** permite encadenar servicios de GCP en una secuencia definida como YAML:

```yaml
# workflow_informe_diario.yaml
main:
  steps:
    - step1_generar_datos:
        call: googleapis.bigquery.v2.jobs.query
        args:
          projectId: techstore-analytics
          body:
            query: |
              CREATE OR REPLACE TABLE techstore.resumen_diario AS
              SELECT DATE(order_date) AS fecha, COUNT(*) AS pedidos,
                     ROUND(SUM(total), 2) AS ingresos
              FROM techstore.orders
              WHERE DATE(order_date) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
              GROUP BY fecha

    - step2_exportar_csv:
        call: googleapis.bigquery.v2.jobs.query
        args:
          projectId: techstore-analytics
          body:
            query: |
              EXPORT DATA OPTIONS(
                uri='gs://techstore-informes/diario/*.csv',
                format='CSV',
                overwrite=true
              ) AS
              SELECT * FROM techstore.resumen_diario

    - step3_enviar_notificacion:
        call: googleapis.pubsub.v1.projects.topics.publish
        args:
          topic: projects/techstore-analytics/topics/informe-generado
          body:
            messages:
              - data: "Informe diario generado exitosamente"
```

```bash
# Desplegar workflow
gcloud workflows deploy techstore-informe-diario \
    --source=workflow_informe_diario.yaml \
    --location=us-central1
```

## Cloud Run: serverless para contenedores

Cloud Run ejecuta contenedores serverless. Es como Cloud Functions pero para aplicaciones completas (no solo una función):

```dockerfile
# Dockerfile para Cloud Run
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
CMD ["python", "app.py"]
```

```python
"""
app.py para Cloud Run
API REST con análisis de TechStore.
"""

from flask import Flask, jsonify
from google.cloud import bigquery

app = Flask(__name__)
cliente = bigquery.Client()

@app.route("/")
def home():
    return "TechStore Analytics API — Cloud Run"

@app.route("/kpi")
def kpi():
    query = """
        SELECT
            ROUND(SUM(total), 2) AS ingresos,
            COUNT(*) AS pedidos,
            COUNT(DISTINCT customer_id) AS clientes
        FROM techstore.orders
    """
    df = cliente.query(query).to_dataframe()
    return jsonify(df.to_dict(orient="records")[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

```bash
# Construir y desplegar
gcloud builds submit --tag gcr.io/PROJECT_ID/techstore-api
gcloud run deploy techstore-api \
    --image gcr.io/PROJECT_ID/techstore-api \
    --region us-central1 \
    --allow-unauthenticated
```

## Pipeline completamente automatizado

```
┌─────────────┐     ┌─────────────────┐     ┌──────────────┐
│ Cloud       │ ──► │ Cloud Function   │ ──► │ BigQuery     │
│ Scheduler   │     │ (procesar datos)  │     │ (transformar) │
│ (6 AM)      │     │                   │     │              │
└─────────────┘     └─────────────────┘     └──────┬───────┘
                                                   │
                                                   ▼
┌─────────────┐     ┌─────────────────┐     ┌──────────────┐
│ Looker      │ ◄── │ Cloud Storage   │ ◄── │ Scheduled    │
│ Studio      │     │ (informes CSV)   │     │ Query        │
│ (dashboard) │     │                  │     │ (resumir)    │
└─────────────┘     └─────────────────┘     └──────────────┘
```

## Buenas prácticas de automatización

1. **Empieza simple**: Scheduled Queries antes que Cloud Functions
2. **Logs centralizados**: todo pipeline debe registrar inicio, fin, errores
3. **Alertas**: configura notificaciones en fallos (Pub/Sub → Email/Slack)
4. **Costes**: programa tareas pesadas en horas de menor tarifa
5. **Versiones**: usa tags para las funciones (`gcloud functions deploy --entry-point`)
6. **Pruebas**: prueba cada etapa por separado antes de orquestar

## Ejercicios

1. Crea una Scheduled Query que genere el resumen diario de ventas
2. ¿Qué diferencia hay entre Cloud Scheduler y Scheduled Queries?
3. Programa un Cloud Scheduler que invoque una función HTTP cada hora
4. ¿Para qué sirve Workflows? Nombra un caso de uso
5. Crea un pipeline que: Schedule → Cloud Function → BigQuery → GCS
6. ¿Cuándo usarías Cloud Run en lugar de Cloud Functions?
7. Configura una alerta por email cuando falle una Scheduled Query
8. Crea una función que genere un informe semanal en Excel y lo guarde en GCS
9. ¿Cómo gestionarías errores en un pipeline de múltiples pasos?
10. Diseña en papel un pipeline completo para TechStore desde la carga hasta el dashboard
