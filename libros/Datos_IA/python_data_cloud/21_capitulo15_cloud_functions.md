# Capítulo 15: Automatización Serverless con Cloud Functions

## ¿Qué es serverless?

**Serverless** no significa "sin servidores", sino "sin que tú gestiones servidores". Escribes código, lo subes y el proveedor (Google Cloud) se encarga de ejecutarlo, escalarlo y mantenerlo.

Ventajas:
- **Sin aprovisionamiento**: no eliges máquinas ni capacidades
- **Escalado automático**: de 0 a miles de ejecuciones simultáneas
- **Pago por uso**: solo pagas mientras tu código se ejecuta
- **Alta disponibilidad**: Google replica tu función en múltiples zonas

## Cloud Functions

**Cloud Functions** es el servicio serverless de Google Cloud. Ejecutas código Python (o Node.js, Go, Java, .NET, Ruby) en respuesta a eventos.

### Tipos de Cloud Functions

| Tipo | Disparador | Uso típico |
|------|-----------|------------|
| HTTP | Petición HTTP | APIs, webhooks, endpoints |
| Cloud Storage | Evento en GCS | Procesar archivos al subirse |
| Pub/Sub | Mensaje en cola | Pipelines asíncronos, eventos |
| Firestore | Cambio en documento | Reaccionar a cambios en DB |
| Cloud Scheduler | Cron programado | Tareas periódicas |

## Tu primera función HTTP

### 1. Crear la función

```python
"""
funcion_http/main.py
Cloud Function HTTP: endpoint de saludo.
"""

def saludar(request):
    """Responde a peticiones HTTP."""
    nombre = request.args.get("nombre", "Mundo")
    return f"Hola, {nombre}! Bienvenido a TechStore Analytics."
```

### 2. requirements.txt

```txt
functions-framework==3.*
google-cloud-bigquery
pandas
```

### 3. Desplegar

```bash
# Desplegar con gcloud
gcloud functions deploy saludar \
    --runtime python311 \
    --trigger-http \
    --allow-unauthenticated \
    --region us-central1

# Probar
curl https://REGION-PROJECT_ID.cloudfunctions.net/saludar?nombre=Alex
```

## Función: Consultar ventas del día

```python
"""
funcion_ventas_diarias/main.py
Cloud Function: devuelve las ventas del día actual.
"""

from google.cloud import bigquery
from datetime import date

PROJECT = "techstore-analytics"
DATASET = "techstore"

cliente = bigquery.Client(project=PROJECT)


def ventas_hoy(request):
    """Devuelve resumen de ventas del día."""
    hoy = date.today().isoformat()

    query = f"""
        SELECT
            COUNT(*) AS pedidos,
            ROUND(SUM(total), 2) AS ingresos,
            COUNT(DISTINCT customer_id) AS clientes
        FROM {DATASET}.orders
        WHERE DATE(order_date) = '{hoy}'
    """

    df = cliente.query(query).to_dataframe()

    return {
        "fecha": hoy,
        "pedidos": int(df["pedidos"].iloc[0]),
        "ingresos": float(df["ingresos"].iloc[0]),
        "clientes": int(df["clientes"].iloc[0]),
    }
```

## Función disparada por Cloud Storage

```python
"""
funcion_procesar_csv/main.py
Cloud Function: cuando se sube un CSV a GCS, lo procesa y carga a BigQuery.
"""

from google.cloud import bigquery, storage
import pandas as pd
import os

PROJECT = "techstore-analytics"
DATASET = "techstore_raw"

cliente_bq = bigquery.Client(project=PROJECT)
cliente_storage = storage.Client()


def procesar_csv(event, context):
    """Disparada por evento en Cloud Storage."""
    archivo = event["name"]
    bucket = event["bucket"]

    print(f"Procesando: gs://{bucket}/{archivo}")

    # Descargar archivo a directorio temporal
    ruta_local = f"/tmp/{os.path.basename(archivo)}"
    blob = cliente_storage.bucket(bucket).blob(archivo)
    blob.download_to_filename(ruta_local)

    # Leer CSV
    df = pd.read_csv(ruta_local)
    print(f"Filas: {len(df)}")

    # Cargar a BigQuery
    nombre_tabla = os.path.splitext(os.path.basename(archivo))[0]
    tabla_id = f"{DATASET}.{nombre_tabla}"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",
        autodetect=True,
    )

    job = cliente_bq.load_table_from_dataframe(df, tabla_id, job_config=job_config)
    job.result()

    print(f"Cargadas {job.output_rows} filas en {tabla_id}")

    # Opcional: mover archivo procesado
    blob_copy = cliente_storage.bucket(bucket).blob(f"procesados/{archivo}")
    blob_copy.rewrite(blob)
    blob.delete()

    return f"OK: {len(df)} filas procesadas"
```

## Función con Pub/Sub

```python
"""
funcion_pubsub/main.py
Cloud Function disparada por mensaje Pub/Sub.
"""

import base64
import json
from google.cloud import bigquery

PROJECT = "techstore-analytics"
DATASET = "techstore"
cliente = bigquery.Client(project=PROJECT)


def procesar_evento(event, context):
    """Procesa un mensaje Pub/Sub con datos de venta."""

    # Decodificar mensaje
    datos = base64.b64decode(event["data"]).decode("utf-8")
    venta = json.loads(datos)

    print(f"Procesando venta: {venta}")

    # Insertar en BigQuery
    query = f"""
        INSERT INTO {DATASET}.ventas_streaming
        (order_id, customer_id, total, timestamp)
        VALUES
        (@order_id, @customer_id, @total, CURRENT_TIMESTAMP())
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("order_id", "INT64", venta["order_id"]),
            bigquery.ScalarQueryParameter("customer_id", "INT64", venta["customer_id"]),
            bigquery.ScalarQueryParameter("total", "FLOAT64", venta["total"]),
        ]
    )

    cliente.query(query, job_config=job_config).result()
    print("Venta registrada en BigQuery.")
```

## Despliegue y monitorización

### Comandos gcloud útiles

```bash
# Listar funciones
gcloud functions list

# Ver logs
gcloud functions logs read saludar

# Describir función
gcloud functions describe saludar

# Eliminar función
gcloud functions delete saludar
```

### Logs y errores

Cloud Functions se integra con **Cloud Logging** para registrar automáticamente:
- Salida de `print()`
- Excepciones no capturadas
- Métricas de ejecución (duración, memoria, invocaciones)

## Buenas prácticas

1. **Función atómica**: cada función hace UNA cosa bien
2. **Timeout**: por defecto 60s, máximo 540s (9 min). Funciones largas → Cloud Run
3. **Idempotencia**: procesar el mismo mensaje dos veces no debe causar duplicados
4. **Mínimas dependencias**: menos dependencias = menos frialdad (cold start)
5. **Variables de entorno**: para configuraciones sensibles (no hardcodear)
6. **Retry**: Pub/Sub reintenta automáticamente; HTTP no

### Cold starts

La primera invocación después de un periodo de inactividad puede tardar más (la plataforma inicia tu entorno). Para evitarlo:
- Mantén una o dos instancias en espera (`min_instances`)
- Usa funciones más ligeras
- Para cargas críticas, considera Cloud Run

## Ejercicios

1. Crea y despliega una Cloud Function HTTP que devuelva "Hola, TechStore"
2. ¿Qué es un cold start? ¿Cómo mitigarlo?
3. Crea una función que consulte el total de pedidos de hoy en BigQuery y los devuelva como JSON
4. ¿Cuál es la diferencia entre una función HTTP y una función disparada por Storage?
5. Despliega una función que procese un CSV cuando se suba a un bucket de GCS
6. ¿Para qué sirve Pub/Sub? Nombra 2 casos de uso en data analytics
7. Crea una función que reciba un mensaje Pub/Sub y registre la venta en BigQuery
8. ¿Cómo monitoreas errores en Cloud Functions?
9. Configura variables de entorno para las credenciales de BigQuery
10. ¿Cuándo usarías Cloud Run en lugar de Cloud Functions? (investiga)
