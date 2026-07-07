# Capítulo 2: pandas Avanzado — Merge, GroupBy, Pivot y Apply

## Merge: el equivalente a JOINs de SQL

Igual que en SQL combinas tablas con JOINs, en pandas usas `merge()`.

```python
import pandas as pd

ventas = pd.read_csv("codigos/datos_ventas.csv")
productos = pd.read_csv("codigos/datos_productos.csv")
clientes = pd.read_csv("codigos/datos_clientes.csv")

# INNER JOIN (solo registros que coinciden)
df = pd.merge(ventas, productos, left_on="customer_id", right_on="id")
```

Espera, eso no tiene sentido. Corrigiendo:

```python
# INNER JOIN: ventas + productos por product_id
# Primero necesitamos detalles de ventas
detalles = pd.read_csv("codigos/datos_detalles_ventas.csv")
productos = pd.read_csv("codigos/datos_productos.csv")

df = pd.merge(detalles, productos, left_on="product_id", right_on="id", how="inner")
print(df.head())
print(f"Filas: {len(df)}")
```

### Tipos de merge

```python
# INNER JOIN (por defecto)
df = pd.merge(tabla1, tabla2, on="columna_comun")

# LEFT JOIN
df = pd.merge(tabla1, tabla2, on="columna_comun", how="left")

# RIGHT JOIN
df = pd.merge(tabla1, tabla2, on="columna_comun", how="right")

# FULL OUTER JOIN
df = pd.merge(tabla1, tabla2, on="columna_comun", how="outer")
```

### Merge con múltiples columnas

```python
# Merge con nombres de columna diferentes
ventas_con_cliente = pd.merge(
    ventas,
    clientes,
    left_on="customer_id",
    right_on="id",
    how="left"
)
```

## GroupBy: agrupar y agregar

Equivalente a GROUP BY de SQL:

```python
# Agrupar por región y calcular métricas
resumen = ventas.groupby("region").agg(
    pedidos=("order_id", "count"),
    ingresos=("total", "sum"),
    ticket_promedio=("total", "mean"),
    pedido_maximo=("total", "max"),
    pedido_minimo=("total", "min")
).reset_index()

print(resumen)
```

### Múltiples niveles de agrupación

```python
# Por región y estado
resumen = ventas.groupby(["region", "status"]).agg(
    pedidos=("order_id", "count"),
    ingresos=("total", "sum")
).reset_index()
```

### Transformaciones con groupby

```python
# Añadir columna con el promedio de la región
ventas["promedio_region"] = ventas.groupby("region")["total"].transform("mean")

# Añadir columna con el ranking dentro de la región
ventas["ranking_region"] = ventas.groupby("region")["total"].rank(ascending=False)
```

## Pivot Table: tablas dinámicas

Equivalente a las tablas dinámicas de Excel:

```python
# Tabla dinámica básica
pivot = pd.pivot_table(
    ventas,
    values="total",
    index="region",
    columns="status",
    aggfunc="sum",
    fill_value=0
)
print(pivot)
```

### Pivot table avanzada

```python
pivot = pd.pivot_table(
    ventas,
    values="total",
    index=["region", "customer_name"],
    columns="status",
    aggfunc={"total": "sum"},
    fill_value=0,
    margins=True,        # Añadir totales
    margins_name="Total"
)
```

## Apply: aplicar funciones

`apply()` aplica una función a cada fila o columna:

```python
# Función para clasificar pedidos
def clasificar_pedido(total):
    if total > 1000:
        return "Alto valor"
    elif total > 200:
        return "Medio"
    else:
        return "Bajo"

ventas["clasificacion"] = ventas["total"].apply(clasificar_pedido)
print(ventas["clasificacion"].value_counts())
```

### Apply con lambda

```python
ventas["descuento_sugerido"] = ventas["total"].apply(
    lambda x: x * 0.1 if x > 1000 else x * 0.05
)
```

### Apply en filas completas

```python
def calcular_margen(fila):
    return fila["total"] - fila["total"] * 0.6  # Margen estimado 40%

ventas["margen_estimado"] = ventas.apply(calcular_margen, axis=1)
```

## Operaciones con fechas

```python
# Convertir a datetime
ventas["order_date"] = pd.to_datetime(ventas["order_date"])

# Extraer componentes
ventas["año"] = ventas["order_date"].dt.year
ventas["mes"] = ventas["order_date"].dt.month
ventas["día_semana"] = ventas["order_date"].dt.day_name()
ventas["semana"] = ventas["order_date"].dt.isocalendar().week

# Filtrar por fecha
ventas_2025 = ventas[ventas["order_date"].dt.year == 2025]

# Agrupar por mes
ventas["año_mes"] = ventas["order_date"].dt.to_period("M")
mensual = ventas.groupby("año_mes").agg(
    pedidos=("order_id", "count"),
    ingresos=("total", "sum")
)
```

## Ejercicios del Capítulo 2

1. Combina `datos_ventas.csv` con `datos_clientes.csv` usando merge para añadir región y ciudad a cada pedido.
2. Agrupa por región y calcula: total de pedidos, ingresos totales, ticket promedio.
3. Crea una tabla dinámica con región en filas, status en columnas y suma de total como valores.
4. Usa apply para crear una columna "tamaño_pedido": Pequeño (<100), Medio (100-500), Grande (>500).
5. Añade una columna con el ranking de cada pedido dentro de su región por total descendente.
6. Calcula las ventas totales por año-mes usando groupby y .dt.to_period.
7. Filtra los pedidos del año 2025 y calcula el top 5 de clientes por gasto.
8. Usa transform para añadir a cada fila el promedio de su región.
9. Crea una tabla dinámica que muestre el promedio de ventas por región y día de la semana.
10. Usa merge para combinar detalles_ventas con productos y calcula el ingreso total por categoría.

## Checklist de autoevaluación

- [ ] Sé combinar DataFrames con merge (INNER, LEFT, FULL)
- [ ] Sé agrupar datos con groupby y múltiples agregaciones
- [ ] Sé crear tablas dinámicas con pivot_table
- [ ] Sé usar apply y lambda para transformaciones
- [ ] Sé trabajar con fechas en pandas
- [ ] Sé usar transform para broadcasting de agregaciones
