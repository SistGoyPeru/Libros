# Capítulo 17: Proyecto Final — Sistema de Reporting Cloud

## El cuadro completo

A lo largo de este libro has aprendido:
1. **Python + pandas** para análisis de datos
2. **BigQuery** como data warehouse cloud
3. **Looker Studio** para dashboards interactivos
4. **Cloud Functions y automatización** para pipelines serverless

Ahora es momento de integrarlo todo en un **sistema de reporting cloud** completo y automatizado para TechStore.

## Arquitectura del sistema

```
                    ┌─────────────────────────────┐
                    │   SQLite / CSVs locales      │
                    │   (datos fuente)              │
                    └──────────┬──────────────────┘
                               │
                               ▼
                    ┌─────────────────────────────┐
                    │   Migración a BigQuery       │
                    │   (Python + pandas)          │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  BigQuery           │
                    │  ┌───────────────┐  │
                    │  │ Datos brutos  │  │
                    │  ├───────────────┤  │
                    │  │ Transformados │  │
                    │  ├───────────────┤  │
                    │  │ Agregados     │  │
                    │  └───────────────┘  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
     ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
     │  Looker      │ │  Cloud       │ │  Scheduled   │
     │  Studio      │ │  Functions   │ │  Queries     │
     │  Dashboard   │ │  (informes)  │ │  (resúmenes) │
     └──────────────┘ └──────┬───────┘ └──────────────┘
                             │
                             ▼
                    ┌─────────────────────────────┐
                    │  Cloud Storage              │
                    │  (informes diarios/semanales) │
                    └─────────────────────────────┘
```

## Componente 1: Base de datos en la nube

Tu dataset `techstore` en BigQuery ya tiene las 5 tablas migradas. Ahora añade tablas derivadas para optimizar el reporting:

```sql
-- Tabla de métricas diarias (para dashboard rápido)
CREATE OR REPLACE TABLE techstore.metricas_diarias AS
SELECT
  DATE(order_date) AS fecha,
  COUNT(*) AS pedidos,
  COUNT(DISTINCT customer_id) AS clientes_activos,
  ROUND(SUM(total), 2) AS ingresos,
  ROUND(AVG(total), 2) AS ticket_promedio,
  ROUND(SUM(total) / NULLIF(COUNT(DISTINCT customer_id), 0), 2) AS ingresos_por_cliente,
  COUNT(*) / NULLIF(COUNT(DISTINCT customer_id), 0) AS pedidos_por_cliente
FROM techstore.orders
GROUP BY fecha
ORDER BY fecha;

-- Tabla de cohortes (actualizada semanalmente)
CREATE OR REPLACE TABLE techstore.cohortes_semanales AS
WITH primera_compra AS (
  SELECT
    customer_id,
    DATE_TRUNC(MIN(order_date), WEEK(MONDAY)) AS cohorte
  FROM techstore.orders
  GROUP BY customer_id
),
semanas AS (
  SELECT
    pc.customer_id,
    pc.cohorte,
    DATE_TRUNC(o.order_date, WEEK(MONDAY)) AS semana,
    DATE_DIFF(DATE_TRUNC(o.order_date, WEEK(MONDAY)), pc.cohorte, WEEK) AS semana_numero
  FROM techstore.orders AS o
  JOIN primera_compra AS pc ON o.customer_id = pc.customer_id
)
SELECT
  cohorte,
  semana_numero,
  COUNT(DISTINCT customer_id) AS clientes
FROM semanas
GROUP BY cohorte, semana_numero;
```

## Componente 2: Pipeline de actualización

Crea un pipeline automático que se ejecute diariamente:

```python
"""
pipeline_completo.py
Pipeline completo de actualización de TechStore.

Ejecuta: transformaciones en BigQuery → exporta informes → notifica.
"""

from google.cloud import bigquery
from datetime import datetime
import logging

PROJECT = "techstore-analytics"
DATASET = "techstore"

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cliente = bigquery.Client(project=PROJECT)


def ejecutar_query(query, descripcion):
    """Ejecuta una consulta y registra el resultado."""
    logger.info(f"Ejecutando: {descripcion}")
    job = cliente.query(query)
    job.result()
    bytes_procesados = job.total_bytes_processed / 1e6
    logger.info(f"  Completado ({bytes_procesados:.2f} MB)")
    return bytes_procesados


def pipeline_diario():
    """Ejecuta todas las transformaciones del pipeline diario."""
    inicio = datetime.now()
    logger.info(f"Iniciando pipeline diario: {inicio.isoformat()}")

    total_bytes = 0

    # Paso 1: Actualizar métricas diarias
    total_bytes += ejecutar_query(f"""
        CREATE OR REPLACE TABLE {DATASET}.metricas_diarias AS
        SELECT
            DATE(order_date) AS fecha,
            COUNT(*) AS pedidos,
            COUNT(DISTINCT customer_id) AS clientes_activos,
            ROUND(SUM(total), 2) AS ingresos,
            ROUND(AVG(total), 2) AS ticket_promedio
        FROM {DATASET}.orders
        GROUP BY fecha
        ORDER BY fecha
    """, "Actualizar métricas diarias")

    # Paso 2: Actualizar top productos
    total_bytes += ejecutar_query(f"""
        CREATE OR REPLACE TABLE {DATASET}.top_productos AS
        SELECT
            p.category,
            p.name AS producto,
            SUM(oi.quantity) AS unidades_vendidas,
            ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos,
            COUNT(DISTINCT oi.order_id) AS pedidos_con_producto
        FROM {DATASET}.order_items AS oi
        JOIN {DATASET}.products AS p ON oi.product_id = p.product_id
        WHERE oi.order_id IN (
            SELECT order_id FROM {DATASET}.orders
            WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        )
        GROUP BY p.category, p.name
        ORDER BY ingresos DESC
    """, "Actualizar top productos")

    # Paso 3: Métricas de rendimiento por empleado
    total_bytes += ejecutar_query(f"""
        CREATE OR REPLACE TABLE {DATASET}.rendimiento_vendedores AS
        SELECT
            e.employee_id,
            e.name AS vendedor,
            e.position,
            COUNT(o.order_id) AS pedidos,
            ROUND(SUM(o.total), 2) AS ingresos,
            ROUND(AVG(o.total), 2) AS ticket_promedio,
            ROUND(COUNT(o.order_id) / NULLIF(COUNT(DISTINCT DATE(o.order_date)), 0), 1) AS pedidos_por_dia
        FROM {DATASET}.orders AS o
        JOIN {DATASET}.employees AS e ON o.employee_id = e.employee_id
        WHERE o.order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
        GROUP BY e.employee_id, e.name, e.position
        ORDER BY ingresos DESC
    """, "Actualizar rendimiento vendedores")

    duracion = (datetime.now() - inicio).total_seconds()
    logger.info(f"Pipeline completado en {duracion:.1f}s. Total procesado: {total_bytes:.2f} MB")
    return {"duracion_seg": duracion, "total_mb": total_bytes}


if __name__ == "__main__":
    resultado = pipeline_diario()
    print(f"Pipeline ejecutado: {resultado}")
```

## Componente 3: Dashboard ejecutivo

Crea un dashboard en Looker Studio con estas páginas:

### Página 1: Vista Ejecutiva
- KPIs: Ingresos, Pedidos, Clientes, Ticket promedio (vs mes anterior)
- Serie temporal 12 meses
- Top 10 productos
- Métricas diarias (últimos 30 días)

### Página 2: Análisis de Clientes
- Mapa geográfico
- Top 10 ciudades
- Análisis de cohortes (heatmap)
- Clientes nuevos vs recurrentes

### Página 3: Operaciones
- Rendimiento de vendedores
- Pedidos por hora/día
- Categorías más vendidas
- Tasa de conversión (pedidos vs clientes)

## Componente 4: Notificaciones automáticas

Configura alertas para eventos importantes:

```python
"""
alertas_techstore/main.py
Cloud Function: verifica métricas y envía alertas.
"""

from google.cloud import bigquery
import json
import os

PROJECT = "techstore-analytics"
DATASET = "techstore"

cliente = bigquery.Client(project=PROJECT)
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")


def verificar_alertas(request=None):
    """Verifica umbrales críticos y envía notificaciones."""
    alertas = []

    # Alerta 1: Ventas muy por debajo del promedio
    query = f"""
        SELECT AVG(ingresos) AS promedio, STDDEV(ingresos) AS desviacion
        FROM {DATASET}.metricas_diarias
        WHERE fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    """
    stats = cliente.query(query).to_dataframe()
    promedio = stats["promedio"].iloc[0]
    desviacion = stats["desviacion"].iloc[0]

    query_hoy = f"""
        SELECT ingresos FROM {DATASET}.metricas_diarias
        WHERE fecha = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
    """
    df_hoy = cliente.query(query_hoy).to_dataframe()

    if len(df_hoy) > 0:
        ingresos_hoy = df_hoy["ingresos"].iloc[0]
        if ingresos_hoy < promedio - 2 * desviacion:
            alertas.append({
                "tipo": "ventas_bajas",
                "mensaje": f"Ventas de ayer (${ingresos_hoy:.2f}) "
                           f"muy por debajo del promedio (${promedio:.2f})"
            })

    # Alerta 2: Sin pedidos en las últimas 24h
    query_pedidos = f"""
        SELECT COUNT(*) AS pedidos FROM {DATASET}.orders
        WHERE order_date >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR)
    """
    pedidos = cliente.query(query_pedidos).to_dataframe()
    if pedidos["pedidos"].iloc[0] == 0:
        alertas.append({
            "tipo": "sin_pedidos",
            "mensaje": "No se registraron pedidos en las últimas 24 horas"
        })

    # Enviar alertas
    for alerta in alertas:
        print(f"ALERTA: {alerta['mensaje']}")
        # Aquí iría la lógica para enviar a Slack/Email

    return json.dumps({"alertas": alertas, "total": len(alertas)})
```

## Documentación del sistema

Cada componente del sistema debe estar documentado:

```markdown
# Sistema de Reporting TechStore

## Componentes
1. BigQuery: techstore (dataset con tablas raw + derivadas)
2. Looker Studio: Dashboard Ejecutivo (enlace)
3. Pipeline Diario: Cloud Scheduler → Cloud Function → BigQuery
4. Alertas: Cloud Function (verifica métricas cada hora)

## Mantenimiento
- Pipeline diario se ejecuta a las 3:00 AM
- Dashboard se actualiza automáticamente
- Alertas se envían a Slack #techstore-analytics

## Costes estimados (mensuales)
- BigQuery storage: ~100 MB → ~$0.02
- BigQuery queries: ~50 GB procesados → ~$0.25
- Cloud Functions: 0 (free tier)
- Total estimado: < $1 USD/mes
```

## Ejercicios

1. Crea la tabla `metricas_diarias` en BigQuery con todos los KPIs diarios
2. Implementa el script `pipeline_completo.py` con 3 transformaciones
3. ¿Cuál es la ventaja de tener tablas derivadas precalculadas?
4. Crea la tabla `rendimiento_vendedores` con métricas de los últimos 90 días
5. Configura una alerta que se dispare si los ingresos de hoy son 0
6. Documenta cada componente de tu sistema de reporting
7. ¿Cómo estimarías el coste mensual de este sistema?
8. Añade una alerta que verifique si el número de pedidos supera un umbral máximo
9. Crea una tabla `top_productos` actualizada semanalmente
10. Diseña un plan de mantenimiento para este sistema (frecuencia, responsables, backups)
