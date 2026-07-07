# Capítulo 4: Datos en Streaming

## 4.1 Procesamiento en Tiempo Real

El big data no es solo volumen; también es velocidad. Los datos en streaming llegan continuamente y deben procesarse en ventanas de tiempo.

### 4.1.1 Batch vs Streaming

```python
# Batch: procesamiento periódico
df_batch = spark.read.parquet("data/dia_2025_01_15/")
resultado = df_batch.groupBy("category").sum("amount")

# Streaming: procesamiento continuo
df_stream = spark \
    .readStream \
    .format("rate") \
    .option("rowsPerSecond", "1000") \
    .load()
```

### 4.1.2 Structured Streaming

Spark Structured Streaming trata los streams como DataFrames infinitos:

```python
from pyspark.sql.functions import window, col, sum

# Definir el stream de entrada
eventos_stream = spark \
    .readStream \
    .schema("event_id STRING, customer_id INT, amount DOUBLE, event_ts TIMESTAMP") \
    .option("maxFilesPerTrigger", 1) \
    .parquet("data/events/streaming/")

# Transformaciones en streaming (igual que batch)
metricas_stream = eventos_stream \
    .withWatermark("event_ts", "10 minutes") \
    .groupBy(
        window("event_ts", "5 minutes"),
        "customer_id"
    ) \
    .agg(sum("amount").alias("gasto_5min"))

# Salida
query = metricas_stream \
    .writeStream \
    .queryName("ventas_tiempo_real") \
    .outputMode("append") \
    .format("console") \
    .trigger(processingTime="10 seconds") \
    .start()

query.awaitTermination(timeout=60)
```

## 4.2 Kafka: El Sistema Nervioso del Streaming

### 4.2.1 Conceptos de Kafka

```python
conceptos_kafka = {
    "Producer": "Publica mensajes en topics",
    "Consumer": "Lee mensajes de topics",
    "Topic": "Canal de mensajes categorizado",
    "Partition": "División de un topic para paralelismo",
    "Broker": "Servidor Kafka",
    "Offset": "Posición del mensaje en la partición",
    "Consumer Group": "Grupo de consumidores que balancean carga"
}
```

### 4.2.2 Consumir desde Kafka con Spark

```python
# Configuración del consumidor Spark-Kafka
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "techstore_events") \
    .option("startingOffsets", "latest") \
    .option("failOnDataLoss", "false") \
    .load()

# Parsear mensajes JSON
from pyspark.sql.functions import from_json, col

schema_stream = "event_id STRING, event_type STRING, product_id INT, ts TIMESTAMP"

eventos = kafka_df \
    .select(from_json(col("value").cast("string"), schema_stream).alias("event")) \
    .select("event.*")

# Eventos en tiempo real
eventos_tiempo_real = eventos \
    .withWatermark("ts", "1 minute") \
    .groupBy(
        window("ts", "1 minute"),
        "event_type"
    ) \
    .count() \
    .orderBy("window")
```

## 4.3 Ventanas de Tiempo y Watermarks

```python
from pyspark.sql.functions import window, current_timestamp, expr

# Tipos de ventanas
ventanas = {
    "Tumbling": "Ventanas fijas sin solapamiento [0-5, 5-10, 10-15]",
    "Sliding": "Ventanas con solapamiento [0-5, 2-7, 4-9]",
    "Session": "Ventanas basadas inactividad [gap=10min]"
}

# Tumbling window cada 5 minutos
ventas_5min = eventos_stream \
    .withWatermark("event_ts", "5 minutes") \
    .groupBy(
        window("event_ts", "5 minutes"),
        "product_id"
    ) \
    .agg(
        sum("amount").alias("ingresos"),
        count("*").alias("ventas")
    )

# Sliding window cada 2 minutos, con ventana de 10
ventas_sliding = eventos_stream \
    .groupBy(
        window("event_ts", "10 minutes", "2 minutes"),
        "category"
    ) \
    .agg(sum("amount").alias("total"))

# Session window con gap de 5 minutos
comportamiento = eventos_stream \
    .groupBy(
        session_window("event_ts", "5 minutes"),
        "customer_id"
    ) \
    .agg(count("*").alias("eventos_sesion"))

# Watermark: tolerancia a datos tardíos
# Si watermark = 10 minutos, datos con ts < max(ts) - 10min se descartan
```

## 4.4 Output Modes y Sinks

```python
# Output modes
modos = {
    "append": "Solo nuevas filas (agregaciones sin estado)",
    "complete": "Todo el resultado (agregaciones con estado)",
    "update": "Solo filas actualizadas (similar a complete pero más eficiente)"
}

# Sinks de salida
sinks = {
    "console": query.writeStream.format("console"),
    "memory": query.writeStream.format("memory").queryName("tabla_stream"),
    "parquet": query.writeStream.format("parquet")
        .option("path", "data/stream_output/")
        .option("checkpointLocation", "data/checkpoints/parquet/"),
    "kafka": query.writeStream.format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("topic", "techstore_metrics"),
    "foreach": query.writeStream.foreach(procesador_personalizado)
}

# Checkpointing para recuperación
query = metricas_stream \
    .writeStream \
    .option("checkpointLocation", "data/checkpoints/stream_ventas/") \
    .trigger(processingTime="30 seconds") \
    .foreachBatch(procesar_lote) \
    .start()

def procesar_lote(df, epoch_id):
    print(f"Procesando lote {epoch_id} con {df.count()} registros")
    df.write.mode("append").parquet(f"data/stream/{epoch_id}/")
```

## 4.5 Ejercicios

1. **Streaming Básico**: Lee un stream de eventos TechStore y cuenta eventos por tipo cada minuto.
2. **Kafka**: Configura un productor Kafka que publique eventos de navegación y un consumidor Spark que los procese.
3. **Watermark**: Implementa una ventana de 5 minutos con watermark de 2 minutos y explica el comportamiento con datos tardíos.
4. **Output Mode**: Compara los 3 output modes para una agregación `groupBy("product_id").count()`.
5. **Checkpointing**: Diseña un pipeline streaming con checkpointing que pueda recuperarse de una caída sin perder datos.
