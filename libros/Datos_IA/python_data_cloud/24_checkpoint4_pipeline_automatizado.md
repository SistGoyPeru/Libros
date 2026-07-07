# Checkpoint 4: Pipeline Cloud Automatizado

## Objetivo

Has llegado al final del libro. Este checkpoint integra todo lo aprendido: **implementar un pipeline cloud completamente automatizado** que actualice los datos de TechStore, ejecute transformaciones, genere informes y notifique al equipo — todo sin intervención manual.

## Requisitos

- Proyecto GCP con BigQuery y Looker Studio configurados
- Checkpoints 1, 2 y 3 completados
- gcloud CLI instalado y autenticado
- Python con google-cloud-bigquery

## Paso 1: Scheduled Query para resumen diario

Programa una consulta en BigQuery que se ejecute cada día a las 3:00 AM:

```sql
-- Configurar desde la consola de BigQuery
-- Nombre: resumen_diario_automatico
-- Frecuencia: diario, 03:00
-- Destino: techstore.resumen_diario
-- Opción de escritura: WRITE_APPEND

SELECT
  CURRENT_DATE() AS fecha_generacion,
  DATE(order_date) AS fecha_venta,
  COUNT(*) AS pedidos,
  COUNT(DISTINCT customer_id) AS clientes_unicos,
  ROUND(SUM(total), 2) AS ingresos,
  ROUND(AVG(total), 2) AS ticket_promedio
FROM techstore.orders
WHERE order_date >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY)
  AND order_date < TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), DAY)
GROUP BY fecha_venta;
```

## Paso 2: Cloud Function para procesamiento adicional

Crea y despliega una Cloud Function que ejecute transformaciones adicionales:

```python
"""
transformaciones_post/main.py
Ejecuta transformaciones después de la carga diaria.
"""

from google.cloud import bigquery

PROJECT = "techstore-analytics"
DATASET = "techstore"

cliente = bigquery.Client(project=PROJECT)


def ejecutar_transformaciones(request=None):
    """Ejecuta transformaciones post-carga."""
    queries = [
        f"""
        CREATE OR REPLACE TABLE {DATASET}.metricas_diarias AS
        SELECT
            DATE(order_date) AS fecha,
            COUNT(*) AS pedidos,
            COUNT(DISTINCT customer_id) AS clientes_activos,
            ROUND(SUM(total), 2) AS ingresos,
            ROUND(AVG(total), 2) AS ticket_promedio,
            ROUND(SUM(total) / NULLIF(COUNT(DISTINCT customer_id), 0), 2) AS ingresos_por_cliente
        FROM {DATASET}.orders
        GROUP BY fecha
        ORDER BY fecha
        """,
        f"""
        CREATE OR REPLACE TABLE {DATASET}.top_productos AS
        SELECT
            p.name,
            p.category,
            SUM(oi.quantity) AS unidades,
            ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
        FROM {DATASET}.order_items AS oi
        JOIN {DATASET}.products AS p ON oi.product_id = p.product_id
        WHERE oi.order_id IN (
            SELECT order_id FROM {DATASET}.orders
            WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        )
        GROUP BY p.name, p.category
        ORDER BY ingresos DESC
        LIMIT 50
        """,
    ]

    for i, query in enumerate(queries, 1):
        job = cliente.query(query)
        job.result()
        print(f"Transformación {i} completada: {job.total_bytes_processed / 1e6:.2f} MB")

    return "Transformaciones completadas"
```

Despliega:

```bash
gcloud functions deploy transformaciones-post \
    --runtime python311 \
    --trigger-http \
    --allow-unauthenticated \
    --region us-central1
```

## Paso 3: Cloud Scheduler para orquestar

Crea un job en Cloud Scheduler que ejecute la función después del scheduled query:

```bash
# Ejecutar transformaciones a las 4:00 AM (1 hora después del scheduled query)
gcloud scheduler jobs create http transformaciones-diarias \
    --schedule="0 4 * * *" \
    --uri="https://us-central1-PROJECT_ID.cloudfunctions.net/transformaciones-post" \
    --http-method=GET \
    --time-zone="America/Lima" \
    --location=us-central1
```

## Paso 4: Función de informe semanal

Crea una función que genere un informe semanal en Cloud Storage:

```python
"""
informe_semanal/main.py
Genera informe semanal en Excel y lo guarda en GCS.
"""

from google.cloud import bigquery, storage
from datetime import date, timedelta
import pandas as pd
import io

PROJECT = "techstore-analytics"
DATASET = "techstore"
BUCKET = "techstore-informes"

cliente_bq = bigquery.Client(project=PROJECT)
cliente_gcs = storage.Client()


def generar_informe_semanal(request=None):
    """Genera informe semanal de ventas."""
    hoy = date.today()
    semana_inicio = hoy - timedelta(days=7)

    # Consultas para el informe
    ventas = cliente_bq.query(f"""
        SELECT
          DATE_TRUNC(order_date, WEEK(MONDAY)) AS semana,
          DATE(order_date) AS fecha,
          COUNT(*) AS pedidos,
          ROUND(SUM(total), 2) AS ingresos,
          ROUND(AVG(total), 2) AS ticket_promedio
        FROM {DATASET}.orders
        WHERE order_date >= '{semana_inicio.isoformat()}'
        GROUP BY semana, fecha
        ORDER BY fecha
    """).to_dataframe()

    top_productos = cliente_bq.query(f"""
        SELECT p.category, p.name, SUM(oi.quantity) AS vendidos,
               ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
        FROM {DATASET}.order_items AS oi
        JOIN {DATASET}.products AS p ON oi.product_id = p.product_id
        WHERE oi.order_id IN (
            SELECT order_id FROM {DATASET}.orders
            WHERE order_date >= '{semana_inicio.isoformat()}'
        )
        GROUP BY p.category, p.name
        ORDER BY ingresos DESC
        LIMIT 20
    """).to_dataframe()

    # Crear Excel en memoria
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        ventas.to_excel(writer, sheet_name="Ventas Diarias", index=False)
        top_productos.to_excel(writer, sheet_name="Top Productos", index=False)
    output.seek(0)

    # Subir a GCS
    nombre_archivo = f"informe_semanal_{hoy.isoformat()}.xlsx"
    bucket = cliente_gcs.bucket(BUCKET)
    blob = bucket.blob(f"semanales/{nombre_archivo}")
    blob.upload_from_string(output.getvalue(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    return f"Informe generado: gs://{BUCKET}/semanales/{nombre_archivo}"
```

## Paso 5: Pipeline completo — Verificación

Crea un script que verifique el estado del pipeline completo:

```python
"""
verificar_pipeline.py
Verifica que el pipeline completo funcione correctamente.
"""

from google.cloud import bigquery
from datetime import datetime, timedelta

PROJECT = "techstore-analytics"
DATASET = "techstore"
cliente = bigquery.Client(project=PROJECT)

print("=== Verificación del Pipeline TechStore ===")
print(f"Fecha: {datetime.now().isoformat()}")
print()

# 1. Verificar métricas diarias
try:
    df = cliente.query(f"""
        SELECT COUNT(*) AS dias, SUM(pedidos) AS total_pedidos,
               ROUND(SUM(ingresos), 2) AS total_ingresos
        FROM {DATASET}.metricas_diarias
        WHERE fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    """).to_dataframe()
    print(f"✓ Métricas diarias: {df['dias'].iloc[0]} días, "
          f"{df['total_pedidos'].iloc[0]} pedidos, "
          f"${df['total_ingresos'].iloc[0]} ingresos (7 días)")
except Exception as e:
    print(f"✗ Métricas diarias: ERROR — {e}")

# 2. Verificar top productos
try:
    df = cliente.query(f"""
        SELECT COUNT(*) AS productos FROM {DATASET}.top_productos
    """).to_dataframe()
    print(f"✓ Top productos: {df['productos'].iloc[0]} productos registrados")
except Exception as e:
    print(f"✗ Top productos: ERROR — {e}")

# 3. Verificar última ejecución del pipeline
try:
    df = cliente.query(f"""
        SELECT COUNT(*) AS pedidos_hoy
        FROM {DATASET}.orders
        WHERE DATE(order_date) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
    """).to_dataframe()
    print(f"✓ Pedidos ayer: {df['pedidos_hoy'].iloc[0]}")
except Exception as e:
    print(f"✗ Pedidos: ERROR — {e}")

print()
print("Verificación completada.")
```

## Entregables del Checkpoint 4

Al completar este checkpoint deberías tener:

- [ ] Scheduled Query ejecutándose diariamente
- [ ] Cloud Function desplegada para transformaciones post-carga
- [ ] Cloud Scheduler orquestando la secuencia
- [ ] Función de informe semanal en Cloud Storage
- [ ] Dashboard en Looker Studio actualizado automáticamente
- [ ] Script de verificación del pipeline
- [ ] Documentación del sistema de reporting

## Próximos pasos tras el checkpoint

1. **Expansión**: añade fuentes de datos adicionales (inventario, devoluciones)
2. **Alertas**: configura notificaciones a Slack/Email para fallos del pipeline
3. **Costes**: monitorea el gasto mensual con la consola de billing
4. **Colaboración**: invita a tu equipo al dashboard de Looker Studio
5. **Mejora continua**: ajusta las transformaciones según feedback del negocio

¡Felicidades! Has construido un sistema de reporting cloud completo, automatizado y profesional. Lo que antes requería hojas de cálculo manuales ahora se actualiza solo, todos los días, sin intervención humana. Bienvenido al mundo del analytics engineering en la nube.
