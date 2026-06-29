# Manejo de Datos Faltantes y Outliers

Los datos reales nunca son perfectos. Valores faltantes y outliers son la norma, no la excepción. Ignorarlos o manejarlos incorrectamente sesga tus análisis y modelos. Este capítulo te da las herramientas para tratarlos con rigor.

## Datos Faltantes: Tipos y Mecanismos

Antes de imputar, debes entender por qué faltan los datos:

| Mecanismo | Significado | Ejemplo | Tratamiento |
|-----------|-------------|---------|-------------|
| **MCAR** | Falta completamente al azar | Sensor se apagó aleatoriamente | Eliminar o imputar sin sesgo |
| **MAR** | Falta al azar (depende de otras variables) | Mujeres no reportan edad | Imputación condicional |
| **MNAR** | No falta al azar (depende del valor faltante) | Personas con ingresos altos no reportan ingresos | Modelos especializados |

```python
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

np.random.seed(42)
n = 500

# Dataset completo
df_completo = pd.DataFrame({
    'edad': np.random.normal(40, 12, n).astype(int).clip(18, 90),
    'ingresos': np.random.lognormal(10, 0.5, n),
    'educacion': np.random.choice([0, 1, 2, 3], n, p=[0.1, 0.3, 0.4, 0.2]),
    'puntuacion': np.random.normal(75, 15, n).clip(0, 100),
})

# Introducir valores faltantes (MCAR)
mask_mcar = np.random.random(df_completo.shape) < 0.1
df_missing = df_completo.copy()
df_missing[mask_mcar] = np.nan

print(f"Dataset original: {df_completo.shape}")
print(f"Valores faltantes:\n{df_missing.isna().sum()}")
```

### Estrategia 1: Eliminación

```python
# Eliminar filas con cualquier valor faltante (listwise deletion)
df_sin_faltantes = df_missing.dropna()
print(f"Después de eliminar filas con NaN: {df_sin_faltantes.shape}")
print(f"  Perdimos {len(df_missing) - len(df_sin_faltantes)} filas ({100*(1-len(df_sin_faltantes)/len(df_missing)):.1f}%)")

# Eliminar columnas con muchos faltantes
threshold = 0.3  # 30% faltantes
cols_a_eliminar = df_missing.columns[df_missing.isna().mean() > threshold]
print(f"  Columnas a eliminar (>30% faltantes): {list(cols_a_eliminar)}")
```

> **⚠️ Advertencia:**
> Eliminar filas con faltantes solo es aceptable si los datos son MCAR y la pérdida es pequeña (<5%). Si pierdes >5% de tus datos, la imputación es casi siempre mejor.

### Estrategia 2: Imputación Simple

```python
def comparar_imputaciones(df_original, df_missing, columna):
    """Compara diferentes métodos de imputación"""
    valores_reales = df_original[columna]
    mascara = df_missing[columna].isna()

    # Media
    imputer_mean = SimpleImputer(strategy='mean')
    df_mean = imputer_mean.fit_transform(df_missing[[columna]])
    error_mean = np.abs(valores_reales[mascara] - df_mean[mascara, 0]).mean()

    # Mediana (robusta a outliers)
    imputer_median = SimpleImputer(strategy='median')
    df_median = imputer_median.fit_transform(df_missing[[columna]])
    error_median = np.abs(valores_reales[mascara] - df_median[mascara, 0]).mean()

    print(f"\nComparación de imputaciones para '{columna}':")
    print(f"  MAE - Media:   {error_mean:.2f}")
    print(f"  MAE - Mediana: {error_median:.2f}")

comparar_imputaciones(df_completo, df_missing, 'edad')
comparar_imputaciones(df_completo, df_missing, 'ingresos')
```

### Estrategia 3: Imputación por KNN

```python
# Imputación basada en vecinos más cercanos
imputer_knn = KNNImputer(n_neighbors=5)
df_knn = pd.DataFrame(
    imputer_knn.fit_transform(df_missing),
    columns=df_missing.columns
)

# Error para ingresos (variable con outliers)
mascara = df_missing['ingresos'].isna()
error_knn_ingresos = np.abs(
    df_completo['ingresos'][mascara] - df_knn['ingresos'][mascara]
).mean()

print(f"MAE KNN para ingresos: {error_knn_ingresos:.2f}")
```

### Estrategia 4: Imputación Múltiple (MICE)

```python
# MICE (Multiple Imputation by Chained Equations)
imputer_mice = IterativeImputer(max_iter=10, random_state=42)
df_mice = pd.DataFrame(
    imputer_mice.fit_transform(df_missing),
    columns=df_missing.columns
)

error_mice_ingresos = np.abs(
    df_completo['ingresos'][mascara] - df_mice['ingresos'][mascara]
).mean()
print(f"MAE MICE para ingresos: {error_mice_ingresos:.2f}")
```

## Outliers: Detección y Tratamiento

Los valores atípicos (outliers) pueden ser errores, anomalías reales o información valiosa. El contexto determina el tratamiento.

### Método 1: Rango Intercuartil (IQR)

```python
def detectar_outliers_iqr(datos, factor=1.5):
    """Detecta outliers usando la regla del IQR"""
    Q1 = np.percentile(datos, 25)
    Q3 = np.percentile(datos, 75)
    IQR = Q3 - Q1

    limite_inf = Q1 - factor * IQR
    limite_sup = Q3 + factor * IQR

    outliers = (datos < limite_inf) | (datos > limite_sup)
    return outliers, limite_inf, limite_sup

# Ejemplo con ingresos (distribución log-normal)
ingresos = np.random.lognormal(10, 0.5, 1000)
outliers_iqr, lim_inf, lim_sup = detectar_outliers_iqr(ingresos)

print(f"Outliers detectados (IQR): {outliers_iqr.sum()} ({outliers_iqr.mean()*100:.1f}%)")
print(f"  Límite inferior: {lim_inf:.0f}")
print(f"  Límite superior: {lim_sup:.0f}")
```

### Método 2: Desviación Estándar (Z-Score)

```python
def detectar_outliers_zscore(datos, umbral=3):
    """Detecta outliers usando Z-score"""
    z = np.abs(stats.zscore(datos))
    return z > umbral

outliers_z = detectar_outliers_zscore(ingresos)
print(f"Outliers detectados (Z-score, 3σ): {outliers_z.sum()} ({outliers_z.mean()*100:.1f}%)")
```

### Método 3: Isolation Forest

```python
from sklearn.ensemble import IsolationForest

# Para datos multivariados
np.random.seed(42)
X_normal = np.random.randn(500, 2)
X_outliers = np.random.uniform(low=-6, high=6, size=(20, 2))
X = np.vstack([X_normal, X_outliers])

iso_forest = IsolationForest(contamination=0.05, random_state=42)
predicciones = iso_forest.fit_predict(X)
# -1 = outlier, 1 = inlier

outliers_if = predicciones == -1
print(f"Outliers detectados (Isolation Forest): {outliers_if.sum()} ({outliers_if.mean()*100:.1f}%)")
```

## Tratamiento de Outliers

```python
def tratar_outliers(datos, metodo='clip', limite_inf=None, limite_sup=None):
    """Aplica diferentes estrategias de tratamiento de outliers"""
    if metodo == 'clip':
        # Winsorización: reemplazar por los límites
        q1, q99 = np.percentile(datos, [1, 99])
        return np.clip(datos, q1, q99)

    elif metodo == 'remove':
        # Eliminar (no siempre recomendado)
        Q1 = np.percentile(datos, 25)
        Q3 = np.percentile(datos, 75)
        IQR = Q3 - Q1
        mascara = (datos >= Q1 - 1.5*IQR) & (datos <= Q3 + 1.5*IQR)
        return datos[mascara]

    elif metodo == 'log':
        # Transformación logarítmica (comprime colas largas)
        return np.log1p(datos)

    elif metodo == 'missing':
        # Convertir outliers en NaN
        Q1 = np.percentile(datos, 25)
        Q3 = np.percentile(datos, 75)
        IQR = Q3 - Q1
        mascara = (datos >= Q1 - 1.5*IQR) & (datos <= Q3 + 1.5*IQR)
        datos_tratados = datos.copy()
        datos_tratados[~mascara] = np.nan
        return datos_tratados

# Comparar métodos
ingresos_con_outliers = np.random.lognormal(10, 0.5, 1000)
print(f"Original: media={np.mean(ingresos_con_outliers):.0f}, std={np.std(ingresos_con_outliers):.0f}")
print(f"Clipped:  media={np.mean(tratar_outliers(ingresos_con_outliers, 'clip')):.0f}")
print(f"Log:      media={np.mean(tratar_outliers(ingresos_con_outliers, 'log')):.0f}")
```

## Impacto en Modelos

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Demostrar cómo los outliers afectan a la regresión
np.random.seed(42)
X = np.random.randn(100, 1) * 10
y = 3 + 2 * X.ravel() + np.random.randn(100) * 2

# Añadir outliers
X_out = np.vstack([X, [[50], [55]]])  # Dos outliers lejanos
y_out = np.concatenate([y, [100, 120]])

# Modelo sin outliers
modelo_limpio = LinearRegression().fit(X, y)
r2_limpio = modelo_limpio.score(X, y)

# Modelo con outliers
modelo_sucio = LinearRegression().fit(X_out, y_out)
r2_sucio = modelo_sucio.score(X_out, y_out)

print(f"R² sin outliers: {r2_limpio:.4f}")
print(f"R² con outliers: {r2_sucio:.4f}")
print(f"Coef sin outliers: {modelo_limpio.coef_[0]:.2f} (real: 2.0)")
print(f"Coef con outliers: {modelo_sucio.coef_[0]:.2f} (real: 2.0)")
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Toma un dataset real (por ejemplo, `load_diabetes` de sklearn) e introduce artificialmente valores faltantes al azar (10%, 20%, 30%). Compara el rendimiento de un modelo con y sin imputación.

2. **Ejercicio 2:** Genera un dataset con outliers en una variable. Compara el efecto de winsorización (clip), eliminación y transformación logarítmica en la media y varianza.

3. **Ejercicio 3:** Implementa una función que automáticamente decida la estrategia de imputación basada en el porcentaje de valores faltantes y el tipo de variable.

4. **Ejercicio 4:** Usando Isolation Forest, detecta outliers multivariados en el dataset Iris. ¿Coinciden con alguna especie en particular? ¿Tiene sentido biológico?

## 📝 Resumen del Capítulo

- Los datos faltantes tienen **mecanismos** (MCAR, MAR, MNAR) que determinan el tratamiento
- La **eliminación** solo es apropiada para MCAR con baja pérdida
- La **imputación por media/mediana** es simple pero ignora correlaciones
- **KNN** y **MICE** capturan relaciones entre variables
- Los **outliers** se detectan por IQR, Z-score o Isolation Forest
- El **tratamiento** incluye winsorización, transformación, eliminación o conversión a NaN
- Los outliers afectan desproporcionadamente a modelos basados en distancia y varianza
- El contexto del dominio determina si un outlier es error o señal valiosa

**Conceptos clave aprendidos:** MCAR/MAR/MNAR, imputación, MICE, KNN imputer, IQR, Z-score, Isolation Forest, winsorización, transformación logarítmica
