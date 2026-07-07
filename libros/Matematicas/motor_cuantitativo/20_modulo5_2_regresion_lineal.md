# Regresión Lineal Simple y Múltiple

La regresión lineal es el punto de partida de casi todo modelado predictivo. Es simple, interpretable y sorprendentemente poderosa. En este capítulo entenderás cómo funciona por dentro, no solo cómo llamarla desde sklearn.

## El Modelo de Regresión Lineal

La regresión lineal modela la relación entre una variable dependiente (Y) y una o más variables independientes (X):

```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε
```

Donde β₀ es el *intercepto*, βᵢ son los *coeficientes* y ε es el *error* (lo que no podemos explicar).

## Regresión Lineal Simple

### Desde Cero con Mínimos Cuadrados

```python
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# Datos simulados: horas de estudio → puntuación en examen
horas = np.random.uniform(0, 10, 100)
puntuacion = 30 + 5 * horas + np.random.normal(0, 8, 100)

# Cálculo manual de coeficientes
def regresion_lineal_simple(x, y):
    n = len(x)
    x_mean, y_mean = np.mean(x), np.mean(y)

    # β₁ = Σ(xi - x̄)(yi - ȳ) / Σ(xi - x̄)²
    beta_1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)

    # β₀ = ȳ - β₁ · x̄
    beta_0 = y_mean - beta_1 * x_mean

    return beta_0, beta_1

beta_0, beta_1 = regresion_lineal_simple(horas, puntuacion)
print(f"Intercepto (β₀): {beta_0:.2f}")
print(f"Pendiente (β₁): {beta_1:.2f}")
print(f"Interpretación: por cada hora extra, la puntuación aumenta {beta_1:.2f} puntos")
# Intercepto (β₀): 29.85
# Pendiente (β₁): 5.05
```

### Con Scikit-learn

```python
from sklearn.linear_model import LinearRegression

X = horas.reshape(-1, 1)  # sklearn requiere 2D
modelo = LinearRegression()
modelo.fit(X, puntuacion)

print(f"β₀: {modelo.intercept_:.2f}")
print(f"β₁: {modelo.coef_[0]:.2f}")
# Mismos resultados

# Predicción
predicciones = modelo.predict(X)
print(f"Primeras 5 predicciones: {np.round(predicciones[:5], 1)}")
```

## Supuestos de la Regresión Lineal

La validez del modelo depende de estos supuestos:

```python
def verificar_supuestos(modelo, X, y):
    """Verifica los supuestos de la regresión lineal"""
    y_pred = modelo.predict(X)
    residuos = y - y_pred

    # 1. Linealidad: residuos vs predicciones (sin patrón)
    # 2. Homocedasticidad: varianza constante de residuos
    # 3. Normalidad de residuos
    # 4. Independencia de residuos

    # Test de Normalidad (Shapiro-Wilk)
    _, p_normalidad = stats.shapiro(residuos)

    # Test de Homocedasticidad (Breusch-Pagan)
    # Aproximación: correlación entre |residuos| y predicciones
    r_hetero, p_hetero = stats.spearmanr(np.abs(residuos), y_pred)

    print("Verificación de supuestos:")
    print(f"  Normalidad (Shapiro): p = {p_normalidad:.4f} {'✓' if p_normalidad > 0.05 else '✗'}")
    print(f"  Homocedasticidad: p = {p_hetero:.4f} {'✓' if p_hetero > 0.05 else '✗'}")

verificar_supuestos(modelo, X, puntuacion)
# Normalidad: p > 0.05 ✓
# Homocedasticidad: p > 0.05 ✓
```

| Supuesto | Qué significa | Cómo verificarlo | Qué hacer si falla |
|----------|---------------|------------------|-------------------|
| Linealidad | La relación es lineal | Gráfico de residuos | Transformar variables (log, polinomios) |
| Homocedasticidad | Varianza constante | Breusch-Pagan, gráfico | Mínimos cuadrados ponderados |
| Normalidad | Errores ∼ N(0, σ²) | Q-Q plot, Shapiro | n grande → TLC, transformaciones |
| Independencia | Errores no correlacionados | Durbin-Watson | Modelos de series temporales |
| No multicolinealidad | Predictores no correlacionados | VIF | Eliminar/regularizar variables |

## Regresión Lineal Múltiple

```python
# Más predictores
np.random.seed(42)
n = 200

horas_estudio = np.random.uniform(0, 10, n)
horas_sueno = np.random.uniform(4, 10, n)
ejercicio = np.random.uniform(0, 7, n)

# Puntuación real: 20 + 5*estudio + 3*sueño + 2*ejercicio + ruido
puntuacion = (20 + 5 * horas_estudio +
              3 * horas_sueno +
              2 * ejercicio +
              np.random.normal(0, 5, n))

# DataFrame para statsmodels
import statsmodels.api as sm

df = pd.DataFrame({
    'puntuacion': puntuacion,
    'horas_estudio': horas_estudio,
    'horas_sueno': horas_sueno,
    'ejercicio': ejercicio
})

# Regresión múltiple
X = df[['horas_estudio', 'horas_sueno', 'ejercicio']]
X = sm.add_constant(X)  # Añadir intercepto
modelo_sm = sm.OLS(df['puntuacion'], X).fit()

print(modelo_sm.summary())
```

### Interpretación de Coeficientes

```python
print("Coeficientes:")
print(modelo_sm.params.round(3))
# const           20.734
# horas_estudio    4.932  (cada hora de estudio → +4.93 puntos)
# horas_sueno      2.962  (cada hora de sueño → +2.96 puntos)
# ejercicio        2.053  (cada hora de ejercicio → +2.05 puntos)

# Errores estándar e intervalos de confianza
print("\nIC 95%:")
print(modelo_sm.conf_int().round(3))

# Valor p de cada coeficiente
print("\nValores p:")
print(modelo_sm.pvalues.round(4))
```

## Multicolinealidad

Cuando los predictores están correlacionados entre sí, los coeficientes se vuelven inestables:

```python
# Introducir multicolinealidad
df['estudio_x2'] = df['horas_estudio'] * 2 + np.random.normal(0, 0.5, n)

X_multi = df[['horas_estudio', 'estudio_x2', 'horas_sueno']]
X_multi = sm.add_constant(X_multi)
modelo_multi = sm.OLS(df['puntuacion'], X_multi).fit()

print("Coeficientes con multicolinealidad:")
print(modelo_multi.params.round(3))
# Los coeficientes de estudio y estudio_x2 serán inestables
# y sus errores estándar se dispararán

# Factor de Inflación de Varianza (VIF)
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data['Variable'] = X_multi.columns
vif_data['VIF'] = [variance_inflation_factor(X_multi.values, i)
                    for i in range(X_multi.shape[1])]
print("\nVIF:")
print(vif_data.round(2))
# VIF > 10 indica multicolinealidad severa
# horas_estudio y estudio_x2 tendrán VIF muy alto
```

## Comparación de Modelos

### R² y R² Ajustado

```python
# R²: proporción de varianza explicada
r2 = modelo_sm.rsquared
r2_adj = modelo_sm.rsquared_adj

print(f"R²: {r2:.4f} ({r2*100:.1f}% de varianza explicada)")
print(f"R² ajustado: {r2_adj:.4f}")

# Añadir predictores siempre aumenta R² (incluso si son ruido)
# R² ajustado penaliza la complejidad
```

### AIC y BIC

```python
print(f"AIC: {modelo_sm.aic:.1f}")
print(f"BIC: {modelo_sm.bic:.1f}")

# Menor AIC/BIC → mejor modelo (penaliza complejidad)
```

## Transformaciones para Relaciones No Lineales

```python
# Relación no lineal: rendimientos decrecientes
np.random.seed(42)
horas = np.random.uniform(0, 10, 100)
fatiga = 5 * np.log(horas + 1) + np.random.normal(0, 1, 100)

# Modelo lineal en nivel (mal ajuste)
X_lin = horas.reshape(-1, 1)
modelo_lin = LinearRegression().fit(X_lin, fatiga)
r2_lin = modelo_lin.score(X_lin, fatiga)

# Modelo log-transformado
X_log = np.log(horas + 1).reshape(-1, 1)
modelo_log = LinearRegression().fit(X_log, fatiga)
r2_log = modelo_log.score(X_log, fatiga)

print(f"R² lineal: {r2_lin:.4f}")
print(f"R² log: {r2_log:.4f}")
# El log captura mejor la relación
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Usando el dataset `sklearn.datasets.load_diabetes()`, ajusta una regresión lineal múltiple. ¿Qué variable tiene el coeficiente más grande? ¿Cuál es el más significativo?

2. **Ejercicio 2:** Simula un dataset donde la relación entre X e Y sea cuadrática (Y = X² + ε). Ajusta una regresión lineal simple y una regresión con X² como predictor. Compara los R².

3. **Ejercicio 3:** Verifica los supuestos de la regresión en el dataset de diabetes. ¿Se cumplen? Si no, ¿qué transformaciones propondrías?

4. **Ejercicio 4:** Implementa la regresión lineal desde cero usando la ecuación normal (álgebra lineal) y compárala con sklearn. Verifica que obtienes los mismos coeficientes.

## 📝 Resumen del Capítulo

- La **regresión lineal** modela Y = β₀ + β₁X₁ + ... + βₚXₚ + ε
- Los **coeficientes** se estiman por mínimos cuadrados ordinarios (OLS)
- El **intercepto** es el valor esperado cuando todos los predictores son 0
- Las **pendientes** miden el cambio en Y por unidad de cambio en X
- Los **supuestos** (linealidad, homocedasticidad, normalidad, independencia) son críticos
- La **multicolinealidad** infla la varianza de los coeficientes (VIF > 10 es problemático)
- El **R² ajustado** y el **AIC/BIC** sirven para comparar modelos
- Las **transformaciones** (log, polinomios) capturan relaciones no lineales

**Conceptos clave aprendidos:** OLS, coeficiente, intercepto, supuestos, multicolinealidad, VIF, R², R² ajustado, AIC, BIC, transformación logarítmica
