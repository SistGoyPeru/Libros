# Capítulo 3: Formatos de Datos — Parquet, Avro y CSV

## El problema de CSV

CSV es el formato más común y el peor para data engineering:

| Problema | CSV | Parquet |
|----------|-----|---------|
| Tipo de datos | Todo string | Tipado explícito (int, float, date, etc.) |
| Compresión | Ninguna (texto plano) | Columnar con compresión (Snappy, Zstd) |
| Tamaño | 10× más grande | Compacto |
| Lectura | Carga completa | Solo columnas necesarias |
| Schema | No tiene | Incrustado en el archivo |
| Particionamiento | Manual | Nativo (Hive-style) |

```python
# Comparación de tamaño
import pandas as pd

df = pd.read_sql_query("SELECT * FROM orders", conn)

df.to_csv("orders.csv", index=False)       # ~2.5 MB
df.to_parquet("orders.parquet", index=False)  # ~350 KB

# ¡7× más pequeño!
print(f"CSV: {os.path.getsize('orders.csv') / 1024:.0f} KB")
print(f"Parquet: {os.path.getsize('orders.parquet') / 1024:.0f} KB")
```

## Parquet

**Parquet** es un formato columnar de código abierto, diseñado para análisis.

### Columnar vs row-oriented

```
Row-oriented (CSV, Avro):
order_1 | cust_1 | 2024-01-01 | 150.00 | completed
order_2 | cust_2 | 2024-01-01 | 89.99  | completed
order_3 | cust_1 | 2024-01-02 | 250.00 | pending

Column-oriented (Parquet):
order_id:   order_1,  order_2,  order_3
customer:   cust_1,   cust_2,   cust_1
date:       2024-01, 2024-01,  2024-01-02
total:      150.00,   89.99,    250.00
status:     completed,completed,pending
```

Ventaja: si solo necesitas `total`, solo lees esa columna. En CSV lees todo.

### Schema de Parquet

```python
import pyarrow as pa

schema = pa.schema([
    ("order_id", pa.string()),
    ("customer_id", pa.int64()),
    ("order_date", pa.date32()),
    ("total", pa.float64()),
    ("status", pa.string()),
])

# Escribir con schema explícito
table = pa.Table.from_pandas(df, schema=schema)
pa.parquet.write_table(table, "orders.parquet")
```

### Particionamiento Hive-style

Parquet soporta particionamiento al estilo Hive, donde cada partición es un directorio:

```python
# Escribir particionado por año/mes
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month

df.to_parquet(
    "data/bronze/orders/",
    partition_cols=["year", "month"],
    index=False
)

# Resultado:
# data/bronze/orders/year=2024/month=1/part-0.parquet
# data/bronze/orders/year=2024/month=2/part-1.parquet
# ...
```

### Leer particiones

```python
# Leer solo un mes específico
import pyarrow.parquet as pq

dataset = pq.ParquetDataset(
    "data/bronze/orders/",
    filters=[("year", "=", 2024), ("month", "=", 6)]
)
table = dataset.read()
df = table.to_pandas()
print(f"Pedidos de junio 2024: {len(df)}")
```

## Avro

**Avro** es un formato row-oriented, ideal para datos secuenciales y streaming.

```python
import fastavro

schema = {
    "type": "record",
    "name": "Order",
    "fields": [
        {"name": "order_id", "type": "string"},
        {"name": "customer_id", "type": "int"},
        {"name": "total", "type": "float"},
        {"name": "status", "type": "string"},
    ]
}

records = [
    {"order_id": "ORD-001", "customer_id": 1, "total": 150.0, "status": "completed"},
    {"order_id": "ORD-002", "customer_id": 2, "total": 89.99, "status": "completed"},
]

with open("orders.avro", "wb") as f:
    fastavro.writer(f, schema, records)
```

### ¿Cuándo usar cada uno?

| Formato | Úsalo cuando... |
|---------|----------------|
| **Parquet** | Almacenes analíticos, data lakes, BI |
| **Avro** | Streaming, Kafka, transferencia entre sistemas |
| **CSV** | Exportaciones rápidas, interoperabilidad legacy |
| **JSON** | APIs, logs, datos semiestructurados |

## DuckDB: el SQLite del data engineering

**DuckDB** es una base de datos SQL embebida, optimizada para analítica. Ideal para pipelines:

```python
import duckdb

# Consultar Parquet directamente
df = duckdb.sql("""
    SELECT
        strftime(order_date, '%Y-%m') AS mes,
        COUNT(*) AS pedidos,
        ROUND(SUM(total), 2) AS ingresos
    FROM 'data/bronze/orders/*.parquet'
    GROUP BY mes
    ORDER BY mes
""").df()

print(df)
```

## Ejercicios

1. Convierte `orders` de TechStore de CSV a Parquet. Compara tamaños
2. Lee un Parquet con `pyarrow` usando solo las columnas `order_id` y `total`
3. Crea un dataset Parquet particionado por año/mes desde SQLite
4. Escribe un archivo Avro con 10 registros de `customers`
5. ¿Cuánto más pequeño es Parquet vs CSV para los datos de TechStore?
6. ¿Por qué Parquet es mejor que CSV para consultas analíticas?
7. Usa DuckDB para consultar archivos Parquet directamente
8. ¿Qué es el particionamiento Hive-style y por qué es útil?
9. Lee un Parquet de `order_items` filtrando por `quantity > 5`
10. ¿En qué escenario elegirías Avro en lugar de Parquet?
