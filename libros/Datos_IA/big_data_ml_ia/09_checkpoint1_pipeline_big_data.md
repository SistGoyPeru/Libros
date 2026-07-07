# Checkpoint 1: Pipeline de Big Data con TechStore

## Objetivo

Construir un pipeline completo de big data que procese el dataset TechStore a escala, combinando procesamiento batch y streaming.

## Requisitos

- PySpark configurado (local o cluster)
- Dataset TechStore generado (mínimo 1M transacciones)
- Kafka (opcional, para versión streaming)
- 30-45 minutos de ejecución

## Dataset

| Archivo | Registros | Formato |
|---------|-----------|---------|
| `techstore_transactions.parquet` | 1,000,000+ | Parquet |
| `techstore_customers.parquet` | 100,000 | Parquet |
| `techstore_products.parquet` | 5,000 | Parquet |
| `techstore_events_streaming/` | ∞ (streaming) | JSON por línea |

## Pipeline

### Fase 1: Data Lake Organizado

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, when, year, month
import pyspark.sql.functions as F

spark = SparkSession.builder \
    .appName("Checkpoint1-BigData") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

# 1. Leer datos crudos
transacciones = spark.read.parquet("data/techstore_transactions/")
clientes = spark.read.parquet("data/techstore_customers/")
productos = spark.read.parquet("data/techstore_products/")

# 2. Organizar en zonas del data lake
# Bronze: datos crudos (ya están en raw/)
# Silver: datos limpios y enriquecidos
silver_ventas = transacciones \
    .filter(col("amount").isNotNull() & (col("amount") > 0)) \
    .join(broadcast(productos.select("product_id", "category", "product_name")), "product_id", "left") \
    .join(broadcast(clientes.select("customer_id", "segment", "region")), "customer_id", "left") \
    .withColumn("year", year("timestamp")) \
    .withColumn("month", month("timestamp"))

silver_ventas.write \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet("data/silver/ventas/")
```

### Fase 2: Capa Gold (Métricas de Negocio)

```python
# Gold: agregaciones listas para consumo
spark.sql("""
    CREATE OR REPLACE TEMP VIEW gold_ventas_diarias AS
    SELECT
        date_trunc('day', timestamp) as dia,
        category,
        region,
        segment,
        COUNT(DISTINCT customer_id) as clientes_activos,
        COUNT(*) as transacciones,
        ROUND(SUM(amount), 2) as ingresos,
        ROUND(AVG(amount), 2) as ticket_promedio
    FROM silver_ventas
    GROUP BY dia, category, region, segment
""")

# Métricas de rendimiento de producto
spark.sql("""
    CREATE OR REPLACE TEMP VIEW gold_top_productos AS
    SELECT
        product_id,
        product_name,
        category,
        COUNT(*) as veces_vendido,
        ROUND(SUM(amount), 2) as ingresos_totales,
        ROUND(AVG(amount), 2) as precio_promedio,
        RANK() OVER (PARTITION BY category ORDER BY SUM(amount) DESC) as rank_categoria
    FROM silver_ventas
    GROUP BY product_id, product_name, category
    HAVING COUNT(*) > 10
""")
```

### Fase 3: Pipeline Streaming

```python
# Leer streaming de eventos de navegación
eventos = spark \
    .readStream \
    .schema("event_id STRING, customer_id INT, product_id INT, event_type STRING, ts TIMESTAMP") \
    .option("maxFilesPerTrigger", 1) \
    .json("data/events_streaming/")

# Combinar con datos batch para enriquecer
productos_broadcast = broadcast(productos)

eventos_enriquecidos = eventos \
    .join(productos_broadcast, "product_id", "left") \
    .withWatermark("ts", "5 minutes")

# Métricas en tiempo real
metricas_stream = eventos_enriquecidos \
    .groupBy(
        F.window("ts", "5 minutes"),
        "category",
        "event_type"
    ) \
    .agg(
        count("*").alias("total_eventos"),
        countDistinct("customer_id").alias("usuarios_unicos")
    )

# ForeachBatch para escribir en gold
def escribir_gold(df, epoch_id):
    df.write \
        .mode("append") \
        .partitionBy("category") \
        .parquet(f"data/gold/streaming/")

query = metricas_stream \
    .writeStream \
    .foreachBatch(escribir_gold) \
    .option("checkpointLocation", "data/checkpoints/cp1/") \
    .trigger(processingTime="30 seconds") \
    .start()

query.awaitTermination(timeout=120)
```

## Validación

```python
# Verificar pipeline batch
print("=== Validación Silver ===")
print(f"Registros silver: {spark.read.parquet('data/silver/ventas/').count():,}")

print("\n=== Validación Gold ===")
print(spark.sql("SELECT * FROM gold_ventas_diarias ORDER BY ingresos DESC LIMIT 10").toPandas())

print("\n=== Top Productos por Categoría ===")
print(spark.sql("""
    SELECT category, product_name, ingresos_totales, rank_categoria
    FROM gold_top_productos
    WHERE rank_categoria <= 3
    ORDER BY category, rank_categoria
""").toPandas())
```

## Entregables

1. Código del pipeline completo (este script)
2. Data Lake en 3 capas: Bronze → Silver → Gold
3. Pipeline streaming funcional con checkpointing
4. Tablas Gold listas para BI y ML

## Bonus: Dashboard en Tiempo Real

```python
import streamlit as st
import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Dashboard-Streaming").getOrCreate()

st.title("TechStore - Dashboard Tiempo Real")

# Auto-refresh cada 5 segundos
while True:
    df_gold = spark.read.parquet("data/gold/streaming/")
    pdf = df_gold.groupBy("category").sum("total_eventos").toPandas()
    st.bar_chart(pdf.set_index("category"))
    time.sleep(5)
```

## Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Pipeline batch funcional | 25 |
| Capas Bronze/Silver/Gold correctas | 25 |
| Pipeline streaming con watermark | 25 |
| Checkpointing y recuperación | 15 |
| Dashboard en tiempo real (bonus) | 10 |

¡Felicidades! Has construido tu primer pipeline de big data completo con TechStore.
