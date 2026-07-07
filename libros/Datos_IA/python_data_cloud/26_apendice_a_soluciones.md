# Apéndice A: Soluciones a los Ejercicios

Este apéndice contiene las soluciones a los ejercicios propuestos al final de cada capítulo. Las soluciones también están disponibles como archivos Python independientes en `codigos/soluciones/`.

## Capítulo 1: Repaso de Python y pandas

**Ejercicio 10 — EDA básico:**
```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("../codigos/techstore.db")

# Ventas totales por categoría
df = pd.read_sql_query("""
    SELECT p.category, ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
    FROM order_items AS oi
    JOIN products AS p ON oi.product_id = p.product_id
    GROUP BY p.category
    ORDER BY ingresos DESC
""", conn)
print(df)

# Ticket promedio por cliente
df2 = pd.read_sql_query("""
    SELECT c.name, COUNT(o.order_id) AS pedidos, ROUND(AVG(o.total), 2) AS ticket_promedio
    FROM orders AS o
    JOIN customers AS c ON o.customer_id = c.customer_id
    GROUP BY c.name
    HAVING pedidos > 1
    ORDER BY ticket_promedio DESC
    LIMIT 10
""", conn)
print(df2)
conn.close()
```

## Capítulo 2: pandas Avanzado

**Ejercicio 8 — Merge orders + order_items + products:**
```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("../codigos/techstore.db")

orders = pd.read_sql_query("SELECT * FROM orders", conn)
items = pd.read_sql_query("SELECT * FROM order_items", conn)
products = pd.read_sql_query("SELECT * FROM products", conn)

# Merge completo
df = orders.merge(items, on="order_id").merge(products, on="product_id")

# Top 10 productos por ingresos
top = (df.groupby(["product_id", "name"])
       .agg(ingresos=("unit_price", lambda x: (x * df.loc[x.index, "quantity"]).sum()),
            unidades=("quantity", "sum"))
       .sort_values("ingresos", ascending=False)
       .head(10))
print(top)
conn.close()
```

## Capítulo 3: Limpieza de Datos

**Ejercicio 7 — Pipeline de limpieza:**
```python
import pandas as pd

df = pd.read_csv("datos_ventas.csv")

# 1. Eliminar duplicados
df = df.drop_duplicates()

# 2. Manejar nulos
df["email"] = df["email"].fillna("sin_email@techstore.com")
df["phone"] = df["phone"].fillna("000-000-0000")

# 3. Estandarizar formatos
df["email"] = df["email"].str.lower().str.strip()
df["name"] = df["name"].str.title()

# 4. Eliminar outliers en precio (Z-score)
from scipy import stats
z_scores = stats.zscore(df["total"].dropna())
df = df[(abs(z_scores) < 3)]

print(f"Datos limpios: {len(df)} filas")
```

## Capítulo 4: Visualización

**Ejercicio 9 — Dashboard 2×2:**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3

conn = sqlite3.connect("../codigos/techstore.db")

orders = pd.read_sql_query("""
    SELECT DATE(order_date) AS fecha, total, status
    FROM orders
""", conn)
orders["fecha"] = pd.to_datetime(orders["fecha"])
orders["mes"] = orders["fecha"].dt.to_period("M").astype(str)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Ventas por mes
ventas_mes = orders.groupby("mes")["total"].sum().sort_index()
ventas_mes.plot(ax=axes[0, 0], kind="line", marker="o", title="Ingresos Mensuales")

# 2. Distribución de totales
orders["total"].plot(ax=axes[0, 1], kind="hist", bins=30, title="Distribución de Totales")

# 3. Status de pedidos
orders["status"].value_counts().plot(ax=axes[1, 0], kind="bar", title="Estado de Pedidos")

# 4. Boxplot mensual
sns.boxplot(ax=axes[1, 1], data=orders, x="mes", y="total")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
conn.close()
```

## Capítulo 5: EDA Completo

**Ejercicio 10 — Insights de negocio:**
```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("../codigos/techstore.db")

orders = pd.read_sql_query("SELECT * FROM orders", conn)
customers = pd.read_sql_query("SELECT * FROM customers", conn)
items = pd.read_sql_query("SELECT * FROM order_items", conn)
products = pd.read_sql_query("SELECT * FROM products", conn)

# Ticket promedio por ciudad
df = orders.merge(customers, on="customer_id")
top_ciudades = df.groupby("city").agg(
    pedidos=("order_id", "count"),
    ingresos=("total", "sum"),
    ticket_promedio=("total", "mean")
).sort_values("ingresos", ascending=False).head(10)
print("Top 10 ciudades por ingresos:")
print(top_ciudades)

# Productos más rentables
df2 = items.merge(products, on="product_id")
top_productos = df2.groupby("name").agg(
    unidades=("quantity", "sum"),
    ingresos=("unit_price", lambda x: (x * df2.loc[x.index, "quantity"]).sum())
).sort_values("ingresos", ascending=False).head(10)
print("\nTop 10 productos por ingresos:")
print(top_productos)

# Clientes con mayor recurrencia
df3 = df.groupby("customer_id").agg(
    nombre=("name", "first"),
    pedidos=("order_id", "count"),
    total=("total", "sum"),
    primera_compra=("order_date", "min"),
    ultima_compra=("order_date", "max")
)
df3["dias_entre"] = (pd.to_datetime(df3["ultima_compra"]) - pd.to_datetime(df3["primera_compra"])).dt.days
print("\nClientes más recurrentes:")
print(df3.sort_values("pedidos", ascending=False).head(10))
conn.close()
```

## Capítulo 6: Cloud Computing

**Ejercicio 2 — Costes BigQuery:**
- Almacenamiento BigQuery (región US): $0.02 por GB/mes (datos activos), $0.01 por GB/mes (datos de larga duración)
- Consultas (on-demand): $5 por TB procesado
- Free tier: 10 GB de almacenamiento y 1 TB de consultas por mes

## Capítulo 7: GCP Configuración

**Ejercicio 10 — gcloud query:**
```bash
bq query "SELECT CURRENT_DATE() AS hoy"
```
Resultado: `+------------+ | hoy | +------------+ | 2025-01-15 | +------------+`

## Capítulo 8: BigQuery

**Ejercicio 6 — INSERT en tabla test:**
```sql
CREATE TABLE techstore.test (
  id INT64 NOT NULL,
  nombre STRING(100),
  fecha DATE
);

INSERT INTO techstore.test (id, nombre, fecha) VALUES
  (1, 'Cliente A', '2024-01-15'),
  (2, 'Cliente B', '2024-02-20'),
  (3, 'Cliente C', '2024-03-10');

SELECT * FROM techstore.test;

DROP TABLE techstore.test;
```

## Capítulo 9: BigQuery Avanzado

**Ejercicio 5 — Comparar escaneo (con/sin partición):**
```sql
-- Sin partición: escanea toda la tabla
SELECT COUNT(*) FROM techstore.orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';

-- Con partición: escanea solo 3 meses
SELECT COUNT(*) FROM techstore.orders_partitioned
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';
```

## Capítulo 10: Python + BigQuery

**Ejercicio 6 — Función con parámetro fecha:**
```python
from google.cloud import bigquery

def ventas_del_mes(anio, mes):
    cliente = bigquery.Client()
    query = f"""
        SELECT DATE_TRUNC(order_date, MONTH) AS mes,
               COUNT(*) AS pedidos,
               ROUND(SUM(total), 2) AS ingresos
        FROM techstore.orders
        WHERE EXTRACT(YEAR FROM order_date) = {anio}
          AND EXTRACT(MONTH FROM order_date) = {mes}
        GROUP BY mes
    """
    df = cliente.query(query).to_dataframe()
    return df

print(ventas_del_mes(2024, 6))
```

## Capítulo 11: SQL Analítico y Nested Fields

**Ejercicio 3 — Percentiles:**
```sql
SELECT
  APPROX_QUANTILES(total, 100)[OFFSET(10)] AS p10,
  APPROX_QUANTILES(total, 100)[OFFSET(50)] AS p50_mediana,
  APPROX_QUANTILES(total, 100)[OFFSET(90)] AS p90,
  MAX(total) AS maximo
FROM techstore.orders;
```

## Capítulo 12: Data Pipelines

**Ejercicio 3 — Checkpoint:**
Un checkpoint registra la última posición procesada (ej: última fecha, último ID). En pipelines incrementales evita reprocesar datos ya cargados, ahorrando tiempo y costes.

## Capítulo 13: Looker Studio

**Ejercicio 7 — Consulta personalizada en Looker Studio:**
```sql
SELECT
  DATE_TRUNC(order_date, MONTH) AS mes,
  COUNT(DISTINCT customer_id) AS clientes_activos,
  ROUND(SUM(total), 2) AS ingresos,
  COUNT(*) AS pedidos
FROM techstore.orders
WHERE order_date >= '2024-01-01'
GROUP BY mes
ORDER BY mes;
```

## Capítulo 14: Looker Studio Avanzado

**Ejercicio 1 — Campo calculado de categorización:**
```text
CASE
  WHEN total < 200 THEN 'Pequeño'
  WHEN total < 500 THEN 'Mediano'
  WHEN total < 1000 THEN 'Grande'
  ELSE 'Premium'
END
```

## Capítulo 15: Cloud Functions

**Ejercicio 3 — Función que consulta BigQuery:**
```python
from google.cloud import bigquery
from datetime import date

def pedidos_hoy(request):
    cliente = bigquery.Client()
    hoy = date.today().isoformat()
    query = f"""
        SELECT COUNT(*) AS pedidos, ROUND(SUM(total), 2) AS ingresos
        FROM techstore.orders
        WHERE DATE(order_date) = '{hoy}'
    """
    df = cliente.query(query).to_dataframe()
    return {"fecha": hoy, "pedidos": int(df["pedidos"].iloc[0]),
            "ingresos": float(df["ingresos"].iloc[0])}
```

## Capítulo 16: Schedule Queries

**Ejercicio 2 — Diferencia Cloud Scheduler vs Scheduled Queries:**
- Scheduled Queries: solo ejecutan SQL en BigQuery, no requieren código
- Cloud Scheduler: dispara cualquier servicio (HTTP, Pub/Sub, App Engine), más flexible

## Capítulo 17: Proyecto Final

**Ejercicio 5 — Alerta de ingresos cero:**
```python
def verificar_ingresos_cero():
    cliente = bigquery.Client()
    df = cliente.query("""
        SELECT COUNT(*) AS pedidos FROM techstore.orders
        WHERE DATE(order_date) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
    """).to_dataframe()
    if df["pedidos"].iloc[0] == 0:
        print("ALERTA: No se registraron pedidos ayer")
        # Enviar notificación...
```
