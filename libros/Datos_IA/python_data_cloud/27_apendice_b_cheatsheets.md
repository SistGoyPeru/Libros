# Apéndice B: Cheatsheets

## pandas

```python
import pandas as pd

# Lectura
df = pd.read_csv("archivo.csv")
df = pd.read_excel("archivo.xlsx")
df = pd.read_sql_query("SELECT * FROM tabla", conexion)

# Exploración
df.head(10)          # Primeras filas
df.info()            # Tipos y nulos
df.describe()        # Estadísticas
df.shape             # Dimensiones
df.columns           # Nombres columnas
df.dtypes            # Tipos
df.isnull().sum()    # Nulos por columna

# Selección
df["columna"]        # Una columna
df[["a", "b"]]       # Varias columnas
df.iloc[0:5]         # Por posición
df.loc[df["x"] > 5]  # Por condición

# Limpieza
df.drop_duplicates()
df.dropna()
df.fillna(valor)
df.rename(columns={"old": "new"})
df["col"] = df["col"].astype(float)

# Transformación
df.groupby("col").agg({"x": "sum", "y": "mean"})
df.pivot_table(index="a", columns="b", values="c", aggfunc="sum")
df.merge(df2, on="key", how="left")
df.sort_values("col", ascending=False)
df["nueva"] = df["a"].apply(lambda x: x * 2)

# Fechas
pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month
df["año"] = df["fecha"].dt.year
```

## BigQuery SQL

```sql
-- Particionamiento
CREATE TABLE dataset.tabla
PARTITION BY DATE_TRUNC(col_fecha, MONTH)
AS SELECT * FROM origen;

-- Clustering
CREATE TABLE dataset.tabla
PARTITION BY DATE_TRUNC(col_fecha, MONTH)
CLUSTER BY col1, col2
AS SELECT * FROM origen;

-- Nested fields
SELECT customer.name, customer.city
FROM dataset.orders_nested;

-- UNNEST arrays
SELECT * FROM dataset.tabla,
UNNEST(col_array) AS elemento;

-- BQML
CREATE MODEL dataset.modelo
OPTIONS(model_type='linear_reg',
        input_label_cols=['target'])
AS SELECT * FROM dataset.tabla;

-- Scheduled Query (desde consola)
-- Configurar: frecuencia, destino, WRITE_APPEND/TRUNCATE

-- Scripting
DECLARE var DATE DEFAULT '2024-01-01';
EXECUTE IMMEDIATE "SELECT @var";

-- INFORMATION_SCHEMA
SELECT * FROM region-us.INFORMATION_SCHEMA.JOBS;
SELECT * FROM dataset.INFORMATION_SCHEMA.TABLES;
```

## gcloud CLI

```bash
# Autenticación
gcloud auth login
gcloud auth application-default login
gcloud config set project PROYECTO_ID

# BigQuery
bq ls                      # Listar datasets
bq show dataset.tabla      # Info de tabla
bq query "SELECT 1"        # Ejecutar SQL
bq query --dry_run "SQL"   # Estimar coste
bq mk dataset              # Crear dataset
bq rm -r dataset           # Eliminar dataset

# Cloud Functions
gcloud functions deploy NOMBRE \
    --runtime python311 \
    --trigger-http \
    --allow-unauthenticated \
    --region us-central1

gcloud functions logs read NOMBRE
gcloud functions delete NOMBRE

# Cloud Scheduler
gcloud scheduler jobs create http NOMBRE \
    --schedule="0 6 * * *" \
    --uri="URL" \
    --http-method=GET

# Cloud Storage
gcloud storage cp archivo.csv gs://bucket/
gcloud storage ls gs://bucket/
```

## Looker Studio

```text
// Campos calculados
SUM(total) / COUNT(order_id)
CASE WHEN x > 10 THEN 'Alto' ELSE 'Bajo' END
FORMAT_DATETIME('%Y-%m', order_date)
DATE_DIFF(CURRENT_DATE(), fecha, YEAR)

// Parámetros
// Crear parámetro: nombre, tipo, valor default
// Usar: SUM(total) / parametro_objetivo * 100

// Blending
// Añadir datos → Combinar datos
// Seleccionar clave de unión
// Elegir dimensiones y métricas de cada fuente
```

## Cloud Functions

```python
# Función HTTP
def mi_funcion(request):
    nombre = request.args.get("nombre", "Mundo")
    return f"Hola, {nombre}"

# Función Storage
def procesar_archivo(event, context):
    archivo = event["name"]
    bucket = event["bucket"]
    print(f"Archivo: gs://{bucket}/{archivo}")

# Función Pub/Sub
def procesar_mensaje(event, context):
    import base64, json
    datos = base64.b64decode(event["data"]).decode("utf-8")
    mensaje = json.loads(datos)
    print(f"Mensaje: {mensaje}")
```

## Conceptos cloud

| Concepto | Definición |
|----------|------------|
| IaaS | Infraestructura como servicio (VMs, redes) |
| PaaS | Plataforma como servicio (BigQuery, App Engine) |
| SaaS | Software como servicio (Looker Studio, Gmail) |
| Serverless | Código sin gestión de servidores |
| Data Warehouse | Datos estructurados para análisis |
| Data Lake | Datos brutos en formato nativo |
| ETL | Extract → Transform → Load |
| ELT | Extract → Load → Transform |
| IAM | Gestión de identidades y accesos |
| SLA | Acuerdo de nivel de servicio |
| Cold start | Latencia inicial en funciones serverless |
