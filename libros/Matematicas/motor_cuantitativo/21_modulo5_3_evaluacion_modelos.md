# Evaluación de Modelos: R², MSE, RMSE

Un modelo es tan bueno como su capacidad para predecir. Este capítulo cubre las métricas para evaluar qué tan bien funciona un modelo de regresión, cómo interpretarlas y cómo usarlas para mejorar.

## Las Métricas Fundamentales

### Error Absoluto Medio (MAE)

```python
import numpy as np
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error,
    r2_score, explained_variance_score
)

# Datos simulados
np.random.seed(42)
y_real = np.random.normal(100, 20, 200)
y_pred = y_real + np.random.normal(0, 5, 200)

# MAE: promedio de errores absolutos
mae = mean_absolute_error(y_real, y_pred)
print(f"MAE: {mae:.2f}")
print(f"Interpretación: en promedio, el modelo se equivoca por {mae:.2f} unidades")
# MAE: 3.98
```

### Error Cuadrático Medio (MSE)

```python
# MSE: promedio de errores al cuadrado
mse = mean_squared_error(y_real, y_pred)
print(f"MSE: {mse:.2f}")
# MSE: 25.31

# Penaliza más los errores grandes que el MAE
# Si un error es 2x, MSE lo penaliza 4x
```

### Raíz del Error Cuadrático Medio (RMSE)

```python
# RMSE: raíz cuadrada del MSE (misma unidad que Y)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.2f}")
print(f"Interpretación: error típico del modelo en las mismas unidades que Y")
# RMSE: 5.03
```

### R² (Coeficiente de Determinación)

```python
# R²: proporción de varianza explicada
r2 = r2_score(y_real, y_pred)
print(f"R²: {r2:.4f} ({r2*100:.1f}%)")
# R²: 0.9360 → el modelo explica el 93.6% de la varianza
```

## Comparación de Métricas

| Métrica | Rango | Interpretación | Unidad |
|---------|-------|----------------|--------|
| MAE | [0, ∞) | Error promedio absoluto | Misma que Y |
| MSE | [0, ∞) | Error cuadrático promedio | Y² |
| RMSE | [0, ∞) | Error típico | Misma que Y |
| R² | (-∞, 1] | Proporción de varianza explicada | Adimensional |

```python
def reporte_regresion(y_real, y_pred):
    """Reporte completo de métricas de regresión"""
    mae = mean_absolute_error(y_real, y_pred)
    mse = mean_squared_error(y_real, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_real, y_pred)
    mape = np.mean(np.abs((y_real - y_pred) / y_real)) * 100

    print("=== Métricas de Regresión ===")
    print(f"MAE:  {mae:.3f}")
    print(f"MSE:  {mse:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R²:   {r2:.4f}")
    print(f"MAPE: {mape:.2f}%")
    return {'MAE': mae, 'MSE': mse, 'RMSE': rmse, 'R²': r2, 'MAPE': mape}

# Ejemplo completo
np.random.seed(42)
X = np.random.randn(100, 3)
y = 2 + 1.5*X[:, 0] - 0.5*X[:, 1] + 1.0*X[:, 2] + np.random.randn(100)*0.5

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
modelo = LinearRegression().fit(X_train, y_train)
y_pred = modelo.predict(X_test)

reporte_regresion(y_test, y_pred)
```

## R² Explicado en Detalle

```python
# R² = 1 - SS_res / SS_tot
ss_res = np.sum((y_real - y_pred)**2)          # Varianza no explicada
ss_tot = np.sum((y_real - np.mean(y_real))**2)  # Varianza total

r2_manual = 1 - ss_res / ss_tot
print(f"R² manual: {r2_manual:.4f}")
print(f"R² sklearn: {r2_score(y_real, y_pred):.4f}")
# Idénticos

# Interpretación de R²
print("\nInterpretación:")
print(f"  SS_tot = {ss_tot:.1f} (varianza total de Y)")
print(f"  SS_res = {ss_res:.1f} (varianza NO explicada)")
print(f"  SS_reg = {ss_tot - ss_res:.1f} (varianza explicada por el modelo)")
```

## Sobreajuste (Overfitting)

El sobreajuste ocurre cuando el modelo aprende el ruido en lugar de la señal:

```python
# Demostración de sobreajuste
np.random.seed(42)
n_train = 20
n_test = 100

X_train = np.random.rand(n_train, 1) * 10
y_train = np.sin(X_train).ravel() + np.random.randn(n_train) * 0.3

X_test = np.random.rand(n_test, 1) * 10
y_test = np.sin(X_test).ravel() + np.random.randn(n_test) * 0.3

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

for grado in [1, 3, 15]:
    pipe = Pipeline([
        ('poly', PolynomialFeatures(degree=grado, include_bias=False)),
        ('lin', LinearRegression())
    ])
    pipe.fit(X_train, y_train)

    r2_train = pipe.score(X_train, y_train)
    r2_test = pipe.score(X_test, y_test)

    print(f"Grado {grado:2d}: R²_train = {r2_train:.4f}, R²_test = {r2_test:.4f}")
# Grado  1: R²_train = 0.5432, R²_test = 0.5021 (subajuste)
# Grado  3: R²_train = 0.8476, R²_test = 0.8204 (buen ajuste)
# Grado 15: R²_train = 0.9989, R²_test = 0.5101 (SOBREAJUSTE)
```

> **⚠️ Advertencia:**
> Un R² muy alto en entrenamiento (cercano a 1) con un R² bajo en prueba es la señal clásica de sobreajuste. Siempre evalúa en datos no vistos.

## Validación Cruzada (Cross-Validation)

```python
from sklearn.model_selection import cross_val_score, KFold

# K-Fold Cross Validation (k=5)
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(LinearRegression(), X, y, cv=kf, scoring='r2')

print(f"R² en cada fold: {np.round(scores, 4)}")
print(f"R² promedio (CV): {np.mean(scores):.4f} ± {np.std(scores):.4f}")
# R² en cada fold: [0.83 0.85 0.86 0.81 0.84]
# R² promedio (CV): 0.838 ± 0.018

# Comparación de modelos con CV
from sklearn.linear_model import Ridge, Lasso

modelos = {
    'Linear': LinearRegression(),
    'Ridge': Ridge(alpha=1.0),
    'Lasso': Lasso(alpha=0.1)
}

print("\nComparación con CV (5-fold):")
for nombre, modelo in modelos.items():
    scores = cross_val_score(modelo, X, y, cv=5, scoring='r2')
    print(f"  {nombre}: R² = {np.mean(scores):.4f} ± {np.std(scores):.4f}")
```

## Análisis de Residuales

Los residuales (y_real - y_pred) contienen información valiosa:

```python
import matplotlib.pyplot as plt
from scipy import stats

def analisis_residuales(y_real, y_pred):
    """Análisis completo de residuales"""
    residuos = y_real - y_pred

    # 1. Media de residuales (debe ser ~0)
    print(f"Media de residuales: {np.mean(residuos):.4f} (ideal: 0)")

    # 2. Distribución
    _, p_norm = stats.shapiro(residuos)
    print(f"Normalidad residuos (Shapiro): p = {p_norm:.4f}")

    # 3. Homocedasticidad
    r, p_hetero = stats.spearmanr(np.abs(residuos), y_pred)
    print(f"Heterocedasticidad: ρ = {r:.4f}, p = {p_hetero:.4f}")

    # 4. Outliers (residuos estandarizados > 3)
    residuos_std = residuos / np.std(residuos)
    n_outliers = np.sum(np.abs(residuos_std) > 3)
    print(f"Outliers (|residuo| > 3σ): {n_outliers} ({n_outliers/len(residuos)*100:.1f}%)")

    return residuos

analisis_residuales(y_test, y_pred)
```

## MAPE: Error Porcentual Absoluto Medio

```python
def mape(y_real, y_pred):
    """Error porcentual absoluto medio"""
    return np.mean(np.abs((y_real - y_pred) / y_real)) * 100

# MAPE es útil cuando el error relativo importa más que el absoluto
y_real_ej = np.array([100, 200, 150, 300])
y_pred_ej = np.array([110, 190, 160, 280])

print(f"MAPE: {mape(y_real_ej, y_pred_ej):.2f}%")
# MAPE: 6.39% → error relativo promedio del 6.4%
```

## Guía de Selección de Métricas

| Si te importa... | Usa... | Por qué |
|------------------|--------|---------|
| Error en unidades originales | RMSE o MAE | Misma escala que Y |
| Penalizar errores grandes | RMSE o MSE | Eleva al cuadrado los errores |
| Interpretación intuitiva | MAE | Promedio simple de errores |
| Proporción explicada | R² | [0, 1], fácil de comunicar |
| Error relativo | MAPE | Cuando el tamaño importa |
| Comparar modelos con distinta escala | R² o RMSE normalizado | Estandarizado |

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Para el dataset `diabetes` de sklearn, ajusta una regresión lineal y calcula MAE, MSE, RMSE y R² en entrenamiento y prueba. ¿Hay evidencia de sobreajuste?

2. **Ejercicio 2:** Crea un polinomio de grado 10 para datos generados con una relación cuadrática simple. Muestra cómo el R² de entrenamiento aumenta monótonamente mientras el R² de prueba empeora después de cierto punto.

3. **Ejercicio 3:** Implementa tu propia validación cruzada de 5 folds sin usar sklearn. Compara los resultados con `cross_val_score`.

4. **Ejercicio 4:** Dado un conjunto de predicciones, identifica qué puntos son outliers analizando los residuales estandarizados. ¿Qué harías con esos puntos?

## 📝 Resumen del Capítulo

- **MAE:** error promedio absoluto (robusto a outliers)
- **MSE:** error cuadrático promedio (penaliza errores grandes)
- **RMSE:** raíz del MSE, en unidades originales
- **R²:** proporción de varianza explicada (rango típico [0, 1])
- **MAPE:** error porcentual promedio
- El **sobreajuste** ocurre cuando R²_train >> R²_test
- La **validación cruzada** estima el rendimiento real del modelo
- Los **residuales** deben tener media 0, ser normales y homocedásticos
- Ninguna métrica es perfecta; usa varias complementarias

**Conceptos clave aprendidos:** MAE, MSE, RMSE, R², MAPE, sobreajuste, validación cruzada, K-Fold, análisis de residuales
