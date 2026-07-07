## Módulo 2: Estadística Descriptiva y Probabilidad

# Medidas de Tendencia Central, Dispersión y Forma

Antes de construir modelos, necesitas entender tus datos. La estadística descriptiva es el primer paso en cualquier análisis cuantitativo: reduce un dataset completo a unas pocas métricas que resumen su comportamiento.

## Medidas de Tendencia Central

Responden a la pregunta: "¿cuál es el valor típico o central de mis datos?"

### Media Aritmética (Promedio)

La medida más conocida, pero también la más sensible a valores extremos:

```python
import numpy as np
import pandas as pd

datos = np.array([2, 3, 5, 7, 11, 13, 17, 100])

# Cálculo manual
media = np.sum(datos) / len(datos)
print(f"Media: {media:.2f}")
# Media: 19.75

# Con NumPy
print(f"Media (numpy): {np.mean(datos):.2f}")
# Media (numpy): 19.75
```

> **⚠️ Advertencia:**
> La media es engañosa con distribuciones sesgadas. En el ejemplo anterior, el 100 infla la media hasta 19.75, cuando la mayoría de valores están por debajo de 20.

### Mediana

El valor central cuando los datos están ordenados. Robusta a outliers:

```python
# Mediana
mediana = np.median(datos)
print(f"Mediana: {mediana:.2f}")
# Mediana: 9.00

# Comparación con datos sin outlier
datos_limpios = np.array([2, 3, 5, 7, 11, 13, 17])
print(f"Media sin outlier: {np.mean(datos_limpios):.2f}")
print(f"Mediana sin outlier: {np.median(datos_limpios):.2f}")
# Media sin outlier: 8.29
# Mediana sin outlier: 7.00
```

### Moda

El valor que más se repite. Útil para variables categóricas:

```python
from scipy import stats

categorias = np.array(['A', 'B', 'A', 'C', 'A', 'B', 'A', 'C', 'C', 'C'])
moda_resultado = stats.mode(categorias)
print(f"Moda: {moda_resultado.mode} (frecuencia: {moda_resultado.count})")
# Moda: C (frecuencia: 4)
```

> **💡 Consejo del Analista:**
> No hay una medida "mejor" de tendencia central. La media es eficiente pero frágil; la mediana es robusta pero ignora información; la moda es la única útil para datos nominales.

### Comparación de las Tres Medidas

| Medida | Robusta a outliers | Usa todos los datos | Tipo de datos |
|--------|-------------------|---------------------|---------------|
| Media | No | Sí | Numéricos |
| Mediana | Sí | No (solo orden) | Numéricos ordinales |
| Moda | Sí | No (solo frecuencia) | Cualquier tipo |

```python
# Demostración de asimetría
np.random.seed(42)
simetrico = np.random.normal(50, 10, 1000)
sesgado = np.random.exponential(2, 1000)

for nombre, datos in [("Simétrico", simetrico), ("Sesgado (exponencial)", sesgado)]:
    print(f"{nombre}:")
    print(f"  Media: {np.mean(datos):.2f}")
    print(f"  Mediana: {np.median(datos):.2f}")
    print(f"  Diferencia: {np.mean(datos) - np.median(datos):.2f}\n")
# Simétrico: Media=49.98, Mediana=49.81, Diferencia=0.17
# Sesgado: Media=2.01, Mediana=1.40, Diferencia=0.61
```

## Medidas de Dispersión

Responden a: "¿qué tan dispersos están los datos?"

### Varianza y Desviación Estándar

```python
# Varianza poblacional (divide por n)
var_pob = np.var(datos_limpios)

# Varianza muestral (divide por n-1, corrección de Bessel)
var_muestral = np.var(datos_limpios, ddof=1)

print(f"Varianza poblacional: {var_pob:.2f}")
print(f"Varianza muestral: {var_muestral:.2f}")
print(f"Desviación estándar muestral: {np.std(datos_limpios, ddof=1):.2f}")
# Varianza poblacional: 26.24
# Varianza muestral: 30.62
# Desviación estándar muestral: 5.53
```

> **💡 Consejo del Analista:**
> Cuando trabajes con *muestras* (casi siempre), usa `ddof=1`. Cuando trabajes con toda la *población* (raro), `ddof=0`. Por defecto, NumPy asume población.

### Rango Intercuartil (IQR)

El IQR mide la dispersión del 50% central de los datos. Robusto a outliers:

```python
Q1 = np.percentile(datos_limpios, 25)
Q3 = np.percentile(datos_limpios, 75)
IQR = Q3 - Q1

print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
# Q1: 4.0, Q3: 12.0, IQR: 8.0

# Regla del IQR para detectar outliers
outliers = datos[(datos < Q1 - 1.5*IQR) | (datos > Q3 + 1.5*IQR)]
print(f"Outliers (IQR): {outliers}")
# Outliers (IQR): [100]
```

### Rango y Rango Interdecílico

```python
rango = np.max(datos) - np.min(datos)
print(f"Rango: {rango}")
# Rango: 98

# Rango interdecílico (10% a 90%)
D1, D9 = np.percentile(datos_limpios, [10, 90])
print(f"Rango interdecílico: {D9 - D1:.2f}")
# Rango interdecílico: 11.60
```

## Medidas de Forma

Responden a: "¿cómo se distribuyen los datos alrededor del centro?"

### Asimetría (Skewness)

Mide la simetría de la distribución:

```python
from scipy import stats

datos_sesgo_pos = np.random.exponential(1, 1000)
datos_sesgo_neg = -np.random.exponential(1, 1000)
datos_simetricos = np.random.normal(0, 1, 1000)

print(f"Asimetría positiva: {stats.skew(datos_sesgo_pos):.2f}")
print(f"Asimetría negativa: {stats.skew(datos_sesgo_neg):.2f}")
print(f"Simétrica: {stats.skew(datos_simetricos):.2f}")
# Asimetría positiva: ~2.0 (cola a la derecha)
# Asimetría negativa: ~-2.0 (cola a la izquierda)
# Simétrica: ~0.0
```

| Valor | Interpretación |
|-------|----------------|
| 0 | Distribución simétrica |
| > 0 | Cola a la derecha, media > mediana |
| < 0 | Cola a la izquierda, media < mediana |

### Curtosis (Kurtosis)

Mide el "grosor" de las colas:

```python
normal = np.random.normal(0, 1, 1000)
pesada = np.random.standard_t(3, 1000)  # Distribución t con colas pesadas

print(f"Curtosis normal: {stats.kurtosis(normal, fisher=True):.2f}")
print(f"Curtosis colas pesadas: {stats.kurtosis(pesada, fisher=True):.2f}")
# Curtosis normal: ~0.0
# Curtosis colas pesadas: > 0
```

> **💡 Consejo del Analista:**
> La curtosis de *Fisher* (por defecto) da 0 para la normal. La curtosis de *Pearson* (exceso + 3) da 3 para la normal. Siempre verifica cuál estás usando.

## Aplicación Práctica: Resumen Automático de un Dataset

```python
import pandas as pd
import numpy as np
from scipy import stats

def reporte_descriptivo(df, columna):
    """Genera un reporte descriptivo completo para una columna numérica"""
    datos = df[columna].dropna()

    reporte = {
        'n': len(datos),
        'Media': np.mean(datos),
        'Mediana': np.median(datos),
        'Moda': stats.mode(datos).mode[0] if len(stats.mode(datos).mode) > 0 else np.nan,
        'Desv. Est.': np.std(datos, ddof=1),
        'Varianza': np.var(datos, ddof=1),
        'Mínimo': np.min(datos),
        'Máximo': np.max(datos),
        'Q1 (25%)': np.percentile(datos, 25),
        'Q2 (50%)': np.percentile(datos, 50),
        'Q3 (75%)': np.percentile(datos, 75),
        'IQR': np.percentile(datos, 75) - np.percentile(datos, 25),
        'Asimetría': stats.skew(datos),
        'Curtosis': stats.kurtosis(datos, fisher=True),
        'Outliers (IQR)': int(np.sum(
            (datos < np.percentile(datos, 25) - 1.5*(np.percentile(datos, 75) - np.percentile(datos, 25))) |
            (datos > np.percentile(datos, 75) + 1.5*(np.percentile(datos, 75) - np.percentile(datos, 25)))
        )),
        'Datos Faltantes': int(df[columna].isna().sum()),
    }
    return reporte

# Ejemplo con datos simulados
np.random.seed(42)
df = pd.DataFrame({
    'ingresos': np.random.exponential(50, 1000),
    'edad': np.random.normal(40, 12, 1000).clip(18, 90).astype(int),
    'puntuacion': np.random.uniform(0, 100, 1000),
})

reporte = reporte_descriptivo(df, 'ingresos')
for metrica, valor in reporte.items():
    print(f"{metrica:15s}: {valor:.2f}" if isinstance(valor, (int, float)) else f"{metrica:15s}: {valor}")
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Genera un dataset con 1000 valores de una distribución uniforme U(0, 10). Calcula media, mediana, varianza y asimetría. ¿Qué observas sobre la asimetría?
   - Pista: Usa `np.random.uniform(0, 10, 1000)`

2. **Ejercicio 2:** Crea una función que detecte outliers usando tanto la regla del IQR como la desviación estándar (valores más allá de 3σ). Compáralas en un dataset con valores extremos.

3. **Ejercicio 3:** Toma el dataset de `sklearn.datasets.load_diabetes()` y calcula las medidas descriptivas para cada característica. ¿Qué variables tienen mayor asimetría?

## 📝 Resumen del Capítulo

- La **media** es el promedio aritmético; sensible a outliers
- La **mediana** es robusta; recomendada para distribuciones sesgadas
- La **moda** es el valor más frecuente; única para datos nominales
- La **varianza** y **desviación estándar** miden dispersión
- El **IQR** es robusto a outliers; base para detección de anomalías
- La **asimetría** indica sesgo; la **curtosis** indica peso de colas
- Siempre reporta múltiples métricas; ninguna es suficiente por sí sola

**Conceptos clave aprendidos:** media, mediana, moda, varianza, desviación estándar, IQR, asimetría, curtosis, outliers
