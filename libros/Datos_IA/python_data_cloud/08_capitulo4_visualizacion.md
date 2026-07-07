# Capítulo 4: Visualización con Matplotlib y Seaborn

## Por qué visualizar

Un gráfico bien diseñado comunica en segundos lo que una tabla tarda minutos. En análisis de datos, la visualización es tu herramienta más poderosa para:

1. **Explorar** datos (EDA)
2. **Comunicar** hallazgos
3. **Detectar** patrones y anomalías

## Matplotlib: el clásico

Matplotlib es la biblioteca fundacional de visualización en Python. Es flexible y potente, pero requiere más código.

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ventas = pd.read_csv("codigos/datos_ventas.csv")
```

### Gráfico de líneas

```python
# Ventas mensuales
ventas["order_date"] = pd.to_datetime(ventas["order_date"])
ventas["mes"] = ventas["order_date"].dt.to_period("M")
mensual = ventas.groupby("mes")["total"].sum().reset_index()
mensual["mes"] = mensual["mes"].astype(str)

plt.figure(figsize=(12, 6))
plt.plot(mensual["mes"], mensual["total"], marker="o", linewidth=2, color="#2E75B6")
plt.title("Evolución Mensual de Ventas", fontsize=16, pad=20)
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Ingresos (€)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Gráfico de barras

```python
# Ventas por región
region = ventas.groupby("region")["total"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
colors = ["#2E75B6", "#4BACC6", "#F4B183", "#A9D18E", "#D6A3E4"]
bars = plt.bar(region.index, region.values, color=colors[:len(region)], edgecolor="white")

# Añadir etiquetas
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f"{height:,.0f}€", ha="center", va="bottom", fontsize=10)

plt.title("Ventas por Región", fontsize=16, pad=20)
plt.xlabel("Región", fontsize=12)
plt.ylabel("Ingresos (€)", fontsize=12)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
```

### Histograma

```python
# Distribución del ticket
plt.figure(figsize=(10, 6))
plt.hist(ventas["total"], bins=50, color="#2E75B6", edgecolor="white", alpha=0.8)
plt.title("Distribución del Ticket Promedio", fontsize=16, pad=20)
plt.xlabel("Total del pedido (€)", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.axvline(ventas["total"].mean(), color="red", linestyle="--", label=f"Media: {ventas['total'].mean():.2f}€")
plt.axvline(ventas["total"].median(), color="green", linestyle="--", label=f"Mediana: {ventas['total'].median():.2f}€")
plt.legend()
plt.tight_layout()
plt.show()
```

### Boxplot

```python
# Distribución por región
plt.figure(figsize=(12, 6))
regiones = [ventas[ventas["region"] == r]["total"] for r in ventas["region"].unique()]
plt.boxplot(regiones, labels=ventas["region"].unique())
plt.title("Distribución de Ventas por Región", fontsize=16, pad=20)
plt.ylabel("Total del pedido (€)", fontsize=12)
plt.xticks(rotation=30)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## Seaborn: visualización estadística

Seaborn está construido sobre matplotlib y ofrece gráficos estadísticos con menos código.

```python
import seaborn as sns
sns.set_theme(style="whitegrid")
```

### Barplot con Seaborn

```python
plt.figure(figsize=(10, 6))
sns.barplot(data=ventas, x="region", y="total", estimator=sum, ci=None,
            palette="Blues_d", order=ventas.groupby("region")["total"].sum().sort_values(ascending=False).index)
plt.title("Ventas Totales por Región", fontsize=16)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
```

### Boxplot con Seaborn

```python
plt.figure(figsize=(12, 6))
sns.boxplot(data=ventas, x="region", y="total", palette="Set2")
plt.title("Distribución de Ventas por Región", fontsize=16)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
```

### Distribuciones

```python
# Histograma + KDE
plt.figure(figsize=(10, 6))
sns.histplot(ventas["total"], bins=50, kde=True, color="#2E75B6")
plt.title("Distribución del Valor de Pedidos", fontsize=16)
plt.xlabel("Total (€)")
plt.tight_layout()
plt.show()
```

### Pairplot (matriz de correlaciones)

```python
# Solo para columnas numéricas
num_cols = ventas.select_dtypes(include=np.number).columns[:4]
sns.pairplot(ventas[num_cols], diag_kind="kde")
plt.show()
```

### Heatmap de correlaciones

```python
# Matriz de correlación
corr = ventas.select_dtypes(include=np.number).corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f",
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title("Matriz de Correlaciones", fontsize=16, pad=20)
plt.tight_layout()
plt.show()
```

### Countplot

```python
plt.figure(figsize=(8, 5))
sns.countplot(data=ventas, x="status", palette="Set2",
              order=ventas["status"].value_counts().index)
plt.title("Distribución de Estados de Pedido", fontsize=16)
plt.tight_layout()
plt.show()
```

## Personalización avanzada

```python
# Estilo profesional global
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("Blues_d")

# Configuración global
plt.rcParams.update({
    "figure.figsize": (12, 6),
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 150,
})

# Guardar gráficos
plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
plt.savefig("grafico.pdf", bbox_inches="tight")
```

## Dashboard de 4 gráficos

```python
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 1. Ventas por región
region = ventas.groupby("region")["total"].sum().sort_values()
axes[0, 0].barh(region.index, region.values, color="#2E75B6")
axes[0, 0].set_title("Ventas por Región")

# 2. Evolución mensual
mensual = ventas.groupby("mes")["total"].sum()
axes[0, 1].plot(mensual.index.astype(str), mensual.values, marker="o", color="#2E75B6")
axes[0, 1].set_title("Tendencia Mensual")
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Distribución de pedidos
axes[1, 0].hist(ventas["total"], bins=30, color="#4BACC6", edgecolor="white")
axes[1, 0].set_title("Distribución de Pedidos")

# 4. Estado de pedidos
status = ventas["status"].value_counts()
axes[1, 1].pie(status.values, labels=status.index, autopct="%1.1f%%",
               colors=["#2E75B6", "#4BACC6", "#F4B183", "#A9D18E"])
axes[1, 1].set_title("Estado de Pedidos")

plt.tight_layout()
plt.show()
```

## Ejercicios del Capítulo 4

1. Crea un gráfico de barras con las ventas totales por región usando matplotlib.
2. Crea un histograma de la distribución del total de pedidos.
3. Usa seaborn para crear un boxplot de ventas por región.
4. Crea un heatmap de correlaciones entre columnas numéricas.
5. Genera un gráfico de líneas con la evolución mensual de ventas.
6. Crea un countplot de los estados de pedido.
7. Diseña un dashboard de 2x2 con 4 gráficos diferentes.
8. Guarda un gráfico en PNG con 300 DPI.
9. Personaliza los colores y el estilo del gráfico de barras.
10. Crea un pairplot con 4 variables numéricas y analiza las correlaciones visuales.

## Checklist de autoevaluación

- [ ] Sé crear gráficos de líneas, barras y histogramas con matplotlib
- [ ] Sé crear boxplots, heatmaps y pairplots con seaborn
- [ ] Sé personalizar colores, etiquetas y estilos
- [ ] Sé crear dashboards de múltiples gráficos
- [ ] Sé guardar gráficos en alta resolución
- [ ] Entiendo cuándo usar cada tipo de gráfico
