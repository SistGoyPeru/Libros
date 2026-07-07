# Capítulo 5: Análisis Exploratorio de Datos (EDA) Completo

## ¿Qué es el EDA?

El Análisis Exploratorio de Datos (EDA) es el proceso de investigar un dataset para descubrir patrones, anomalías, relaciones y tendencias. No es un paso único: es un ciclo iterativo de:

1. **Preguntar** — ¿Qué quiero saber?
2. **Visualizar** — ¿Qué muestran los datos?
3. **Transformar** — ¿Necesito limpiar o crear nuevas variables?
4. **Concluir** — ¿Qué aprendí?

## EDA completo de TechStore

Vamos a realizar un EDA profesional sobre los datos de ventas de TechStore.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams.update({"figure.dpi": 150})

# Cargar datos
ventas = pd.read_csv("codigos/datos_ventas.csv")
clientes = pd.read_csv("codigos/datos_clientes.csv")
detalles = pd.read_csv("codigos/datos_detalles_ventas.csv")
productos = pd.read_csv("codigos/datos_productos.csv")

print("=" * 60)
print("EDA COMPLETO — TECHSTORE")
print("=" * 60)
```

## 1. Visión general del dataset

```python
def overview(df, name):
    print(f"\n--- {name} ---")
    print(f"Dimensiones: {df.shape}")
    print(f"\nColumnas: {df.columns.tolist()}")
    print(f"\nTipos:\n{df.dtypes}")
    print(f"\nPrimeras filas:")
    print(df.head(3))
    print(f"\nNulos:\n{df.isnull().sum()}")
    print(f"\nEstadísticas:\n{df.describe(include='all')}")

overview(ventas, "VENTAS")
overview(clientes, "CLIENTES")
overview(productos, "PRODUCTOS")
```

## 2. Análisis univariante

```python
# Configurar dashboard de distribuciones
fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# 1. Distribución del total de pedidos
axes[0, 0].hist(ventas["total"], bins=50, color="#2E75B6", edgecolor="white")
axes[0, 0].set_title("Distribución del Total de Pedidos")
axes[0, 0].set_xlabel("Total (€)")
axes[0, 0].axvline(ventas["total"].mean(), color="red", ls="--", label=f"Media: {ventas['total'].mean():.0f}€")
axes[0, 0].legend()

# 2. Distribución de pedidos por estado
status_counts = ventas["status"].value_counts()
axes[0, 1].bar(status_counts.index, status_counts.values, color=["#2E75B6", "#4BACC6", "#F4B183", "#A9D18E"])
axes[0, 1].set_title("Pedidos por Estado")
axes[0, 1].tick_params(axis="x", rotation=30)

# 3. Top 10 regiones por pedidos
region_counts = ventas["region"].value_counts().head(10)
axes[0, 2].barh(region_counts.index[::-1], region_counts.values[::-1], color="#2E75B6")
axes[0, 2].set_title("Top 10 Regiones por Pedidos")

# 4. Distribución de ventas por año
ventas["order_date"] = pd.to_datetime(ventas["order_date"])
ventas["año"] = ventas["order_date"].dt.year
año_ventas = ventas.groupby("año")["total"].sum()
axes[1, 0].bar(año_ventas.index, año_ventas.values, color="#4BACC6")
axes[1, 0].set_title("Ventas por Año")
axes[1, 0].set_xlabel("Año")
axes[1, 0].set_ylabel("Ingresos (€)")

# 5. Top 10 clientes por gasto
top_clientes = ventas.groupby("customer_name")["total"].sum().sort_values(ascending=False).head(10)
axes[1, 1].barh(top_clientes.index[::-1], top_clientes.values[::-1], color="#F4B183")
axes[1, 1].set_title("Top 10 Clientes por Gasto")

# 6. Distribución de pedidos por mes
ventas["mes"] = ventas["order_date"].dt.month
mes_ventas = ventas.groupby("mes")["total"].sum()
axes[1, 2].plot(mes_ventas.index, mes_ventas.values, marker="o", color="#2E75B6", linewidth=2)
axes[1, 2].set_title("Ventas por Mes (estacionalidad)")
axes[1, 2].set_xlabel("Mes")
axes[1, 2].set_xticks(range(1, 13))

plt.tight_layout()
plt.show()
```

## 3. Análisis bivariante

```python
# Relaciones entre variables

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Ventas por región y estado
pivot = pd.pivot_table(ventas, values="total", index="region", columns="status", aggfunc="sum", fill_value=0)
pivot.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Ventas por Región y Estado")
axes[0, 0].legend(loc="upper right")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Ticket promedio por región
ticket_region = ventas.groupby("region")["total"].mean().sort_values()
axes[0, 1].barh(ticket_region.index, ticket_region.values, color="#4BACC6")
axes[0, 1].set_title("Ticket Promedio por Región")
axes[0, 1].set_xlabel("Ticket promedio (€)")

# 3. Boxplot: distribución por región
sns.boxplot(data=ventas, x="region", y="total", ax=axes[1, 0], palette="Set2")
axes[1, 0].set_title("Distribución de Ventas por Región")
axes[1, 0].tick_params(axis="x", rotation=45)

# 4. Ventas por día de la semana
ventas["día_semana"] = ventas["order_date"].dt.day_name()
orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dias_ventas = ventas.groupby("día_semana")["total"].sum().reindex(orden_dias)
axes[1, 1].plot(dias_ventas.index, dias_ventas.values, marker="s", color="#F4B183", linewidth=2)
axes[1, 1].set_title("Ventas por Día de la Semana")
axes[1, 1].tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.show()
```

## 4. Análisis de correlaciones

```python
# Para análisis de correlación, combinamos tablas
detalles_con_productos = pd.merge(detalles, productos, left_on="product_id", right_on="id")
detalles_con_productos["line_total"] = detalles_con_productos["quantity"] * detalles_con_productos["unit_price"]

# Seleccionar columnas numéricas
num_cols = detalles_con_productos.select_dtypes(include=np.number).columns

# Matriz de correlación
corr = detalles_con_productos[num_cols].corr()

plt.figure(figsize=(12, 10))
mask = np.triu(corr)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0,
            square=True, mask=mask, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title("Matriz de Correlaciones — Detalles de Ventas", fontsize=16, pad=20)
plt.tight_layout()
plt.show()
```

## 5. Segmentación de clientes (RFM básico)

```python
# RFM: Recencia, Frecuencia, Valor Monetario
from datetime import datetime

fecha_referencia = datetime(2026, 7, 1)

rfm = ventas.groupby("customer_id").agg(
    recencia=("order_date", lambda x: (fecha_referencia - pd.to_datetime(x).max()).days),
    frecuencia=("order_id", "count"),
    monetario=("total", "sum")
).reset_index()

# Segmentar
rfm["segmento_recencia"] = pd.qcut(rfm["recencia"], q=4, labels=["Alta", "Media-Alta", "Media-Baja", "Baja"])
rfm["segmento_frecuencia"] = pd.qcut(rfm["frecuencia"], q=4, labels=["Baja", "Media-Baja", "Media-Alta", "Alta"])
rfm["segmento_valor"] = pd.qcut(rfm["monetario"], q=4, labels=["Bajo", "Medio-Bajo", "Medio-Alto", "Alto"])

# Puntaje combinado
rfm["puntaje_rfm"] = (
    rfm["segmento_recencia"].astype(str) + " | " +
    rfm["segmento_frecuencia"].astype(str) + " | " +
    rfm["segmento_valor"].astype(str)
)

print("Top 10 clientes por valor:")
print(rfm.sort_values("monetario", ascending=False).head(10))
```

## 6. Informe ejecutivo

```python
print("\n" + "=" * 60)
print("INFORME EJECUTIVO — TECHSTORE")
print("=" * 60)

print(f"\n📊 MÉTRICAS PRINCIPALES:")
print(f"  • Ingresos totales: {ventas['total'].sum():,.2f}€")
print(f"  • Total pedidos: {len(ventas):,}")
print(f"  • Clientes únicos: {ventas['customer_id'].nunique():,}")
print(f"  • Ticket promedio: {ventas['total'].mean():,.2f}€")
print(f"  • Pedido máximo: {ventas['total'].max():,.2f}€")
print(f"  • Pedido mínimo: {ventas['total'].min():,.2f}€")

print(f"\n📈 TENDENCIAS:")
print(f"  • Región con más ventas: {ventas.groupby('region')['total'].sum().idxmax()}")
print(f"  • Mes con más ventas: {ventas.groupby('mes')['total'].sum().idxmax()}")
print(f"  • Día con más ventas: {ventas.groupby('día_semana')['total'].sum().idxmax()}")

print(f"\n⚠️ ANOMALÍAS:")
print(f"  • Pedidos cancelados: {len(ventas[ventas['status'] == 'Cancelado']):,}")
print(f"  • % cancelación: {len(ventas[ventas['status'] == 'Cancelado'])/len(ventas)*100:.1f}%")

print(f"\n✅ RECOMENDACIONES:")
print(f"  • Enfocar marketing en regiones con bajo ticket promedio")
print(f"  • Investigar causa de cancelaciones en meses altos")
print(f"  • Programa de fidelización para clientes con alta frecuencia")
```

## Ejercicios del Capítulo 5

1. Carga los datos de TechStore y realiza una visión general de cada tabla.
2. Crea un dashboard de 6 gráficos para el análisis univariante.
3. Analiza la relación entre región y ticket promedio.
4. Calcula la matriz de correlación entre precio, cantidad y total.
5. Realiza un análisis RFM básico de los clientes.
6. ¿Qué día de la semana tiene más ventas? ¿Y menos?
7. ¿Hay estacionalidad en las ventas? ¿Qué meses destacan?
8. ¿Qué región tiene la menor tasa de cancelación?
9. Genera un informe ejecutivo con las 5 métricas principales.
10. Escribe 3 recomendaciones basadas en tu EDA.

## Checklist de autoevaluación

- [ ] Sé realizar un EDA completo: univariante, bivariante, correlaciones
- [ ] Sé crear dashboards de múltiples gráficos
- [ ] Sé hacer análisis RFM básico
- [ ] Sé generar un informe ejecutivo con hallazgos
- [ ] Sé formular recomendaciones basadas en datos
- [ ] Entiendo el flujo completo del EDA
