# Capítulo 2: PySpark: Procesamiento Distribuido

## 2.1 RDDs: La Base de Spark

Los RDDs (Resilient Distributed Datasets) son la abstracción fundamental de Spark. Son colecciones inmutables y distribuidas de objetos que pueden procesarse en paralelo.

### 2.1.1 Creación de RDDs

```python
# Desde una colección local
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
print(rdd.getNumPartitions())  # 4 (por defecto)

# Desde archivo
rdd_text = spark.sparkContext.textFile("data/reviews.txt")
print(rdd_text.count())  # número de líneas

# Con particiones específicas
rdd_opt = spark.sparkContext.parallelize(datos, minPartitions=8)
```

### 2.1.2 Transformaciones en RDD

```python
rdd = spark.sparkContext.parallelize([
    ("electronics", 250.0),
    ("clothing", 45.0),
    ("electronics", 180.0),
    ("food", 15.0),
    ("electronics", 300.0)
])

# map: transforma cada elemento
rdd_map = rdd.map(lambda x: (x[0], x[1] * 1.21))  # +21% IVA

# filter: selecciona elementos
rdd_filter = rdd.filter(lambda x: x[1] > 100)

# flatMap: un elemento puede producir 0, 1 o múltiples
text_rdd = spark.sparkContext.parallelize(["hola mundo", "hola spark"])
words = text_rdd.flatMap(lambda line: line.split(" "))
# ["hola", "mundo", "hola", "spark"]

# reduceByKey: agrupa por clave y reduce
totales = rdd.reduceByKey(lambda a, b: a + b)
print(totales.collect())
# [("electronics", 730.0), ("clothing", 45.0), ("food", 15.0)]
```

## 2.2 DataFrames: La API Moderna

Los DataFrames son la evolución de los RDDs. Ofrecen optimización nativa mediante Catalyst Optimizer.

### 2.2.1 Creación y Lectura

```python
# Desde archivo Parquet (recomendado)
df = spark.read.parquet("data/techstore_transactions/")
df.printSchema()

# Desde CSV
df_csv = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("data/techstore_products.csv")

# Desde JSON
df_json = spark.read.json("data/events/")

# Desde una tabla
df_table = spark.sql("SELECT * FROM techstore.transactions")
```

### 2.2.2 Transformaciones Principales

```python
from pyspark.sql.functions import col, sum, avg, count, when, datediff, to_date
from pyspark.sql.window import Window
import pyspark.sql.functions as F

# Selección y filtrado
ventas = df.select("customer_id", "amount", "timestamp") \
    .filter(col("amount") > 0) \
    .filter(col("timestamp").isNotNull())

# Agregaciones
por_categoria = df.groupBy("category") \
    .agg(
        sum("amount").alias("total_ventas"),
        avg("amount").alias("ticket_promedio"),
        count("transaction_id").alias("num_transacciones")
    ) \
    .orderBy(col("total_ventas").desc())

# Columnas condicionales
df_con_segmento = df.withColumn(
    "segmento",
    when(col("amount") > 500, "Premium")
    .when(col("amount") > 100, "Regular")
    .otherwise("Básico")
)

# Window functions
ventana_cliente = Window.partitionBy("customer_id") \
    .orderBy("timestamp") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

df_con_acumulado = df.withColumn(
    "gasto_acumulado",
    sum("amount").over(ventana_cliente)
)
```

### 2.2.3 SQL Directo

```python
# Registrar DataFrame como vista temporal
df.createOrReplaceTempView("ventas")

# Consultas SQL nativas
resultado = spark.sql("""
    SELECT
        category,
        DATE_TRUNC('month', timestamp) as mes,
        ROUND(SUM(amount), 2) as ingresos,
        COUNT(DISTINCT customer_id) as clientes_unicos,
        ROUND(AVG(amount), 2) as ticket_promedio
    FROM ventas
    WHERE amount > 0
    GROUP BY category, DATE_TRUNC('month', timestamp)
    HAVING ingresos > 1000
    ORDER BY mes, ingresos DESC
""")
resultado.show(5)
```

## 2.3 Optimización de Consultas

### 2.3.1 Catalyst Optimizer

Spark optimiza automáticamente tu código:

```python
# Esto...
resultado = df.filter(col("amount") > 100) \
    .select("customer_id", "amount") \
    .groupBy("customer_id") \
    .agg(sum("amount"))

# ...Catalyst lo optimiza a:
# 1. Predicate pushdown: filtra amount > 100 antes de leer
# 2. Project pruning: solo lee las columnas necesarias
# 3. Optimización de agregación: combine filters and aggregates
```

### 2.3.2 Particionamiento

```python
# Ver particiones actuales
print(f"Particiones: {df.rdd.getNumPartitions()}")

# Reparticionar
df_repart = df.repartition(8, "category")

# Coalesce (reduce particiones sin shuffle)
df_coalesce = df.coalesce(2)

# Particionamiento al escribir
df.write \
    .partitionBy("category", "year") \
    .mode("overwrite") \
    .parquet("data/techstore_optimized/")
```

### 2.3.3 Caching y Persistencia

```python
from pyspark.storagelevel import StorageLevel

# Cache en memoria (para datos reutilizados)
df_cached = df.filter(col("amount") > 0).cache()
df_cached.count()  # materializa el cache

# Storage levels
niveles = {
    "MEMORY_ONLY": "Solo memoria (default)",
    "MEMORY_AND_DISK": "Memoria, luego disco",
    "DISK_ONLY": "Solo disco",
    "OFF_HEAP": "Fuera del heap de JVM"
}

# Persistir con nivel específico
df_large = df.persist(StorageLevel.MEMORY_AND_DISK)

# Liberar
df_cached.unpersist()
```

## 2.4 Spark UI: Diagnóstico y Tuning

```python
# Configuración para ver Spark UI
spark = SparkSession.builder \
    .appName("TechStore-Optimized") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.sql.adaptive.skewJoin.enabled", "true") \
    .config("spark.sql.autoBroadcastJoinThreshold", "100MB") \
    .getOrCreate()
```

**Métricas clave en Spark UI:**
- **Shuffle Read/Write**: Datos movidos entre nodos
- **Stage Duration**: Tiempo por etapa
- **GC Time**: Tiempo de garbage collection
- **Spill**: Datos escritos a disco por falta de memoria

## 2.5 Ejercicios

1. **RDD**: Crea un RDD con 1000 números aleatorios y calcula media, mediana y desviación.
2. **DataFrame**: Lee `techstore_transactions` y calcula el top 10 productos por ingresos totales.
3. **SQL**: Usa Spark SQL para encontrar los clientes con mayor gasto acumulado en 2025.
4. **Optimización**: Mide la diferencia de rendimiento entre `df.filter().groupBy().agg()` con y sin cache.
5. **Particionamiento**: Genera un dataset particionado por `category` y `year` y explica el beneficio.
