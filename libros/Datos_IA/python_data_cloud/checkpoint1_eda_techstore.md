# Checkpoint 1: EDA Completo de TechStore

## Objetivo

Has completado los cinco capítulos del Proyecto 1: Python avanzado, pandas, limpieza de datos, visualización y EDA. Ahora es momento de aplicar todo en un **análisis exploratorio completo de TechStore**.

## Requisitos

- Tener `techstore.db` en la carpeta `codigos/`
- Tener instaladas las bibliotecas: pandas, numpy, matplotlib, seaborn, sqlite3
- Haber completado los capítulos 1 al 5

## Paso 1: Carga y preparación de datos

Crea un script `codigos/eda_completo_techstore.py`:

```python
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("../codigos/techstore.db")

# Cargar todas las tablas
orders = pd.read_sql_query("SELECT * FROM orders", conn)
customers = pd.read_sql_query("SELECT * FROM customers", conn)
products = pd.read_sql_query("SELECT * FROM products", conn)
order_items = pd.read_sql_query("SELECT * FROM order_items", conn)
employees = pd.read_sql_query("SELECT * FROM employees", conn)

print("=== VISTA GENERAL ===")
for name, df in [("orders", orders), ("customers", customers),
                 ("products", products), ("order_items", order_items),
                 ("employees", employees)]:
    print(f"{name}: {df.shape[0]} filas, {df.shape[1]} columnas")

conn.close()
```

## Paso 2: Análisis univariante

```python
# Ventas por mes
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["mes"] = orders["order_date"].dt.to_period("M")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Histograma de totales
orders["total"].hist(ax=axes[0, 0], bins=30, color="steelblue", edgecolor="white")
axes[0, 0].set_title("Distribución de Totales")

# Boxplot de totales
orders.boxplot(column="total", ax=axes[0, 1])
axes[0, 1].set_title("Boxplot de Totales")

# Pedidos por estado
orders["status"].value_counts().plot(ax=axes[0, 2], kind="bar", color="coral")
axes[0, 2].set_title("Pedidos por Estado")

# Clientes por ciudad
customers["city"].value_counts().head(10).plot(ax=axes[1, 0], kind="barh", color="teal")
axes[1, 0].set_title("Top 10 Ciudades")

# Productos por categoría
products["category"].value_counts().plot(ax=axes[1, 1], kind="pie", autopct="%1.1f%%")
axes[1, 1].set_title("Productos por Categoría")

# Empleados por cargo
employees["position"].value_counts().plot(ax=axes[1, 2], kind="bar", color="purple")
axes[1, 2].set_title("Empleados por Cargo")

plt.tight_layout()
plt.savefig("eda_univariante.png", dpi=150)
plt.show()
```

## Paso 3: Análisis bivariante

```python
# Merge orders + customers
df = orders.merge(customers, on="customer_id")

# Ticket promedio por ciudad
top_ciudades = df.groupby("city").agg(
    pedidos=("order_id", "count"),
    ingresos=("total", "sum"),
    ticket_promedio=("total", "mean")
).sort_values("ingresos", ascending=False).head(10)
print("\nTop 10 ciudades por ingresos:")
print(top_ciudades)

# Merge order_items + products
df_items = order_items.merge(products, on="product_id")

# Ingresos por categoría
ingresos_cat = df_items.groupby("category").apply(
    lambda x: (x["quantity"] * x["unit_price"]).sum()
).sort_values(ascending=False)
print("\nIngresos por categoría:")
print(ingresos_cat)

# Correlación entre precio unitario y cantidad
print(f"\nCorrelación precio-cantidad: {df_items['unit_price'].corr(df_items['quantity']):.3f}")
```

## Paso 4: Dashboard ejecutivo

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Evolución de ingresos mensuales
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders.set_index("order_date").resample("ME")["total"].sum().plot(
    ax=axes[0, 0], marker="o", title="Ingresos Mensuales", color="green")

# 2. Top 10 productos
top_productos = df_items.groupby("name").apply(
    lambda x: (x["quantity"] * x["unit_price"]).sum()
).sort_values(ascending=False).head(10)
top_productos.plot(ax=axes[0, 1], kind="barh", title="Top 10 Productos", color="navy")

# 3. Mapa de calor: pedidos por día y mes
orders["dia_semana"] = orders["order_date"].dt.dayofweek
orders["mes"] = orders["order_date"].dt.month
heatmap_data = orders.pivot_table(index="dia_semana", columns="mes",
                                   values="order_id", aggfunc="count")
sns.heatmap(heatmap_data, ax=axes[1, 0], cmap="YlOrRd", annot=True, fmt=".0f")
axes[1, 0].set_title("Pedidos por Día y Mes")

# 4. Clientes por cantidad de pedidos
frecuencia_cliente = orders.groupby("customer_id").size()
frecuencia_cliente.value_counts().sort_index().plot(
    ax=axes[1, 1], kind="bar", title="Frecuencia de Pedidos por Cliente",
    color="orange", width=0.8)
axes[1, 1].set_xlabel("Número de pedidos")
axes[1, 1].set_ylabel("Clientes")

plt.tight_layout()
plt.savefig("eda_dashboard.png", dpi=150)
plt.show()
```

## Paso 5: Conclusiones y recomendaciones

Basado en tu EDA, documenta:

1. **Métricas clave**: ingresos totales, ticket promedio, clientes únicos, pedidos totales
2. **Patrones**: estacionalidad, días pico, categorías estrella
3. **Problemas**: datos faltantes, outliers, anomalías
4. **Recomendaciones**: 3 acciones concretas basadas en datos
5. **Próximos pasos**: qué más te gustaría analizar

## Entregables del Checkpoint 1

- [ ] Script `eda_completo_techstore.py` funcionando
- [ ] Gráfico de análisis univariante (6 paneles)
- [ ] Análisis bivariante (top ciudades, categorías, correlaciones)
- [ ] Dashboard ejecutivo (4 gráficos)
- [ ] Documento con conclusiones y recomendaciones

¡Felicidades! Has completado el análisis exploratorio de TechStore. En el Proyecto 2 migrarás estos datos a la nube con BigQuery.
