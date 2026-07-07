# Capítulo 3: Procesamiento de Datos a Escala

## 3.1 ETL con PySpark

El proceso ETL (Extract, Transform, Load) es el pan de cada día del ingeniero de datos. Con PySpark, escalamos ETL a volúmenes masivos.

### 3.1.1 Extract: Lectura desde Múltiples Fuentes

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name, col

spark = SparkSession.builder.appName("TechStore-ETL").getOrCreate()

# Múltiples archivos con glob pattern
df_csv = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("data/raw/techstore_*.csv")

# Múltiples fuentes
fuentes = {
    "parquet": spark.read.parquet("data/transactions/"),
    "json": spark.read.json("data/events/"),
    "jdbc": spark.read.format("jdbc") \
        .option("url", "jdbc:postgresql://localhost/techstore") \
        .option("dbtable", "customers") \
        .option("user", "admin") \
        .option("password", "****").load(),
    "bigquery": spark.read.format("bigquery") \
        .option("table", "techstore.users").load()
}
```

### 3.1.2 Transform: Limpieza y Enriquecimiento

```python
# Pipeline de transformación completo
def transformar_ventas(df):
    return df \
        .filter(col("amount").isNotNull() & (col("amount") > 0)) \
        .filter(col("customer_id").isNotNull()) \
        .withColumn("fecha", col("timestamp").cast("date")) \
        .withColumn("año", F.year("timestamp")) \
        .withColumn("mes", F.month("timestamp")) \
        .withColumn("trimestre", F.quarter("timestamp")) \
        .withColumn("iva", col("amount") * 0.21) \
        .withColumn("total_con_iva", col("amount") + col("iva")) \
        .withColumn("rango_precio",
            when(col("amount") < 50, "Económico")
            .when(col("amount") < 200, "Estándar")
            .otherwise("Premium")
        ) \
        .dropDuplicates(["transaction_id", "customer_id"])

ventas_limpias = transformar_ventas(df)
```

### 3.1.3 Load: Escritura Optimizada

```python
# Escritura con múltiples formatos
formatos = {
    "parquet": {
        "path": "data/warehouse/ventas/",
        "opciones": {"compression": "snappy"}
    },
    "delta": {
        "path": "data/lake/ventas/",
        "opciones": {"delta.autoOptimize": "true"}
    },
    "iceberg": {
        "path": "data/catalog/ventas/",
        "opciones": {"write.format": "parquet"}
    }
}

for fmt, conf in formatos.items():
    ventas_limpias.write \
        .mode("overwrite") \
        .partitionBy("año", "mes") \
        .option("compression", "snappy") \
        .format(fmt) \
        .save(conf["path"])
```

## 3.2 Manejo de Datos Semi-estructurados

### 3.2.1 Trabajando con JSON

```python
from pyspark.sql.functions import from_json, get_json_object, json_tuple, schema_of_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, ArrayType

# Eventos TechStore en formato JSON
eventos_json = spark.read.text("data/events/raw/")

# Schema inferido o definido manualmente
schema = StructType([
    StructField("event_id", StringType()),
    StructField("user_id", StringType()),
    StructField("event_type", StringType()),
    StructField("product_id", StringType()),
    StructField("timestamp", StringType()),
    StructField("metadata", StructType([
        StructField("source", StringType()),
        StructField("session_id", StringType()),
        StructField("device", StringType())
    ]))
])

eventos_estructurados = eventos_json \
    .select(from_json(col("value"), schema).alias("event")) \
    .select("event.*")

# Anidamiento
eventos_con_dispositivo = eventos_estructurados \
    .select(
        "event_id", "user_id", "event_type",
        "metadata.device",
        "metadata.session_id"
    )
```

## 3.3 Broadcast Joins y Optimización

### 3.3.1 Tipos de Join en Spark

```python
# Dimensiones pequeñas → Broadcast Join
productos = spark.read.parquet("data/dim_productos/")  # pequeño
df_broadcast = ventas.join(
    broadcast(productos),
    "product_id",
    "left"
)
# Spark transmite productos a todos los workers

# Tablas grandes → Sort-Merge Join
df_largo = df_ventas.join(
    df_clientes,  # también grande
    "customer_id",
    "inner"
)
# Spark: shuffle + sort + merge

# Bucket join (pre-particionado)
ventas_bucket = df_ventas.bucketBy(16, "customer_id") \
    .saveAsTable("ventas_bucket")
clientes_bucket = df_clientes.bucketBy(16, "customer_id") \
    .saveAsTable("clientes_bucket")
# No necesita shuffle
```

### 3.3.2 Skew Join Handling

```python
# Detectar skew
skew = df.groupBy("customer_id").count() \
    .select(max("count"), avg("count"), stddev("count"))
skew.show()
# Si hay clientes con muchísimas transacciones

# Solución 1: Saltar skew (Spark 3.x automático)
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

# Solución 2: Salting manual
from pyspark.sql.functions import rand, concat, lit

df_salted = df_ventas.withColumn(
    "salt",
    (rand() * 10).cast("int")
)
clientes_salted = df_clientes.withColumn(
    "salt_array",
    F.array([lit(i) for i in range(10)])
).select(
    "*",
    F.explode("salt_array").alias("salt")
)

join_salted = df_salted.join(
    clientes_salted,
    ["customer_id", "salt"]
)
```

## 3.4 Catálogo TechStore Optimizado

```python
# Crear una tabla optimizada con particionamiento y bucketing
spark.sql("""
    CREATE TABLE IF NOT EXISTS techstore.catalog (
        transaction_id STRING,
        customer_id INT,
        product_id INT,
        amount DECIMAL(10,2),
        quantity INT,
        timestamp TIMESTAMP,
        category STRING,
        year INT,
        month INT
    )
    USING parquet
    PARTITIONED BY (year, month)
    CLUSTERED BY (customer_id) INTO 32 BUCKETS
    LOCATION 'data/techstore_catalog/'
""")

# Insertar datos optimizados
ventas_limpias.write \
    .mode("overwrite") \
    .insertInto("techstore.catalog")

# Consultas ultra rápidas
spark.sql("""
    SELECT category, SUM(amount) as total
    FROM techstore.catalog
    WHERE year = 2025 AND customer_id = 42
    GROUP BY category
""").show()
```

## 3.5 Ejercicios

1. **ETL Pipeline**: Construye un ETL que lea 3 fuentes de TechStore, las limpie y las unifique en una tabla particionada.
2. **Broadcast Join**: Compara rendimiento de join normal vs broadcast join con una tabla de 10k productos.
3. **Skew**: Simula datos skewed donde el 10% de clientes generan el 90% de transacciones y optimiza el join.
4. **JSON**: Procesa eventos TechStore en JSON anidado y extrae métricas por sesión y dispositivo.
5. **Catálogo**: Diseña un catálogo particionado por fecha y bucketeado por customer_id para consultas rápidas.
