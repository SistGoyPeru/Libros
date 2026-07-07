# Introducción a Series Temporales

Una serie temporal es una secuencia de observaciones ordenadas en el tiempo. Ventas diarias, precios de acciones, tráfico web, temperatura: todos son ejemplos de series temporales. Su análisis requiere técnicas específicas porque las observaciones NO son independientes.

## Conceptos Fundamentales

### Componentes de una Serie Temporal

Toda serie temporal puede descomponerse en:

1. **Tendencia (T):** dirección a largo plazo
2. **Estacionalidad (S):** patrones periódicos predecibles
3. **Ciclo (C):** fluctuaciones sin período fijo
4. **Residuo (R):** ruido aleatorio

```python
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf
from sklearn.metrics import mean_absolute_error

np.random.seed(42)

# Crear una serie temporal sintética
t = np.arange(0, 200)

# Tendencia lineal
tendencia = 10 + 0.05 * t

# Estacionalidad anual (período 20)
estacionalidad = 3 * np.sin(2 * np.pi * t / 20)

# Ruido
ruido = np.random.normal(0, 0.5, len(t))

serie = tendencia + estacionalidad + ruido

print(f"Serie temporal: {len(serie)} puntos")
print(f"Media: {np.mean(serie):.2f}")
print(f"Desv. estándar: {np.std(serie):.2f}")
```

### Descomposición de Series Temporales

```python
# Convertir a pandas Series con índice temporal
idx = pd.date_range('2024-01-01', periods=len(serie), freq='D')
serie_ts = pd.Series(serie, index=idx)

# Descomposición aditiva
descomposicion = seasonal_decompose(serie_ts, model='additive', period=20)

# Extraer componentes
tendencia_est = descomposicion.trend
estacionalidad_est = descomposicion.seasonal
residuo_est = descomposicion.resid

print("Descomposición completada:")
print(f"  Tendencia: {tendencia_est.dropna().shape[0]} puntos")
print(f"  Estacionalidad: {estacionalidad_est.dropna().shape[0]} puntos")
print(f"  Residuo: {residuo_est.dropna().shape[0]} puntos")
```

## Estacionariedad

Una serie es *estacionaria* si sus propiedades estadísticas (media, varianza, autocorrelación) no cambian con el tiempo. La mayoría de los modelos de series temporales requieren estacionariedad.

### Test de Dickey-Fuller Aumentado

```python
def test_estacionariedad(serie, nombre='Serie'):
    """Test ADF para estacionariedad"""
    resultado = adfuller(serie.dropna())
    adf_stat, p_valor = resultado[0], resultado[1]

    print(f"Test ADF - {nombre}:")
    print(f"  Estadístico: {adf_stat:.4f}")
    print(f"  Valor p: {p_valor:.4f}")

    if p_valor < 0.05:
        print(f"  Conclusión: ESTACIONARIA (p < 0.05)")
        return True
    else:
        print(f"  Conclusión: NO ESTACIONARIA (p >= 0.05)")
        return False

test_estacionariedad(serie, 'Original')
# La serie con tendencia no es estacionaria

# Diferenciación: restar el valor anterior
serie_diff = np.diff(serie)
test_estacionariedad(serie_diff, 'Diferenciada (orden 1)')
# La serie diferenciada es estacionaria
```

## Autocorrelación

Mide la correlación de una serie consigo misma en diferentes rezagos (lags):

```python
# Función de Autocorrelación (ACF)
acf_vals, acf_ci = acf(serie_diff, nlags=20, alpha=0.05)

print("ACF (primeros 10 rezagos):")
for i in range(10):
    print(f"  Lag {i}: {acf_vals[i]:.4f}")
# Lag 0: 1.000 (siempre)
# Lag 1: -0.502 (correlación negativa con el valor anterior)
# Lags siguientes: decrecen

# Función de Autocorrelación Parcial (PACF)
pacf_vals, pacf_ci = pacf(serie_diff, nlags=20, alpha=0.05)

print("\nPACF (primeros 5 rezagos):")
for i in range(5):
    print(f"  Lag {i}: {pacf_vals[i]:.4f}")
```

## Modelos ARIMA

ARIMA (AutoRegressive Integrated Moving Average) es el modelo clásico para series temporales:

- **AR (p):** usa valores pasados como predictores
- **I (d):** diferenciación para hacer la serie estacionaria
- **MA (q):** usa errores pasados como predictores

```python
from statsmodels.tsa.arima.model import ARIMA

# Dividir en entrenamiento y prueba
train_size = 160
train, test = serie[:train_size], serie[train_size:]

# Modelo ARIMA(1,1,1) - p=1, d=1, q=1
modelo_arima = ARIMA(train, order=(1, 1, 1))
modelo_arima_fit = modelo_arima.fit()

print(modelo_arima_fit.summary().tables[1])
#                coef    std err    z      P>|z|
# ar.L1        0.5234    0.083    6.307   0.000
# ma.L1       -0.9152    0.047   -19.562  0.000
# sigma2       0.2041    0.022    9.375   0.000
```

### Predicción

```python
# Predicción en test
predicciones = modelo_arima_fit.forecast(steps=len(test))

# Error
error = mean_absolute_error(test, predicciones)
print(f"MAE en test: {error:.3f}")

# Últimos valores reales vs predichos
print("\nÚltimas 5 predicciones:")
for i in range(-5, 0):
    print(f"  Real: {test[i]:.2f}, Pred: {predicciones[i]:.2f}, Diff: {test[i]-predicciones[i]:.2f}")
```

## Cómo Elegir p, d, q

```python
# 1. d: número de diferencias para estacionariedad
# Ya determinamos d=1

# 2. p: orden AR → mirar PACF (pico significativo en lag p)
# 3. q: orden MA → mirar ACF (pico significativo en lag q)

# Búsqueda automática de ARIMA
def mejor_arima(serie, max_p=5, max_q=5, d=1):
    mejor_aic = np.inf
    mejor_orden = None
    mejor_modelo = None

    for p in range(max_p + 1):
        for q in range(max_q + 1):
            try:
                modelo = ARIMA(serie, order=(p, d, q)).fit()
                if modelo.aic < mejor_aic:
                    mejor_aic = modelo.aic
                    mejor_orden = (p, d, q)
                    mejor_modelo = modelo
            except:
                continue

    return mejor_orden, mejor_modelo

mejor_orden, mejor_modelo = mejor_arima(train, max_p=3, max_q=3)
print(f"Mejor ARIMA (por AIC): {mejor_orden}")
# Por ejemplo: (1, 1, 1)
```

## Validación de Modelos de Series Temporales

La validación cruzada estándar no funciona porque el orden temporal importa. Usamos *walk-forward validation*:

```python
def walk_forward_validation(serie, model_order, n_test=30):
    """Validación walk-forward para series temporales"""
    n = len(serie)
    predicciones = []

    for i in range(n - n_test, n):
        # Entrenar con datos hasta i-1
        train = serie[:i]
        modelo = ARIMA(train, order=model_order).fit()
        # Predecir el siguiente punto
        pred = modelo.forecast(steps=1)
        predicciones.append(pred[0])

    reales = serie[-n_test:]
    mae = mean_absolute_error(reales, predicciones)
    return mae, np.array(predicciones)

mae_wf, preds_wf = walk_forward_validation(serie, mejor_orden, n_test=30)
print(f"Walk-forward MAE: {mae_wf:.3f}")
```

## Más Allá de ARIMA

```python
# Prophet (desarrollado por Meta)
# Maneja estacionalidades múltiples y días festivos
# from prophet import Prophet

# SARIMA (estacional)
# ARIMA + componente estacional: SARIMA(p,d,q)(P,D,Q,s)
from statsmodels.tsa.statespace.sarimax import SARIMAX

# SARIMA(1,1,1)(1,1,1,20) - estacionalidad de período 20
modelo_sarima = SARIMAX(train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 20))
modelo_sarima_fit = modelo_sarima.fit(disp=False)
preds_sarima = modelo_sarima_fit.forecast(steps=len(test))
mae_sarima = mean_absolute_error(test, preds_sarima)

print(f"MAE ARIMA: {error:.3f}")
print(f"MAE SARIMA: {mae_sarima:.3f}")
# SARIMA suele ser mejor si hay estacionalidad fuerte
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Carga un dataset de series temporales (por ejemplo, `airline passengers` de statsmodels o cualquier serie de `yfinance`). Descompón la serie en tendencia, estacionalidad y residuo.

2. **Ejercicio 2:** Para la serie del ejercicio anterior, aplica el test ADF antes y después de diferenciar. ¿Cuántas diferencias necesita para ser estacionaria?

3. **Ejercicio 3:** Ajusta un modelo ARIMA a la serie de pasajeros aéreos. Usa walk-forward validation para evaluar su rendimiento. ¿Qué orden (p,d,q) funciona mejor?

4. **Ejercicio 4:** Compara las predicciones de tu modelo ARIMA con un modelo naive (el valor del período anterior). ¿Cuánto mejora el ARIMA en términos de MAE?

## 📝 Resumen del Capítulo

- Las series temporales tienen **dependencia temporal** (no son i.i.d.)
- Se descomponen en **tendencia, estacionalidad, ciclo y residuo**
- La **estacionariedad** es requisito para la mayoría de modelos
- El **test ADF** determina si una serie es estacionaria
- La **diferenciación** elimina tendencias y hace la serie estacionaria
- **ACF** y **PACF** revelan dependencias entre rezagos
- **ARIMA(p,d,q)** combina componentes autorregresivos, integrados y de media móvil
- **SARIMA** añade un componente estacional
- La **walk-forward validation** respeta el orden temporal
- Siempre compara contra un modelo **naive** (benchmark)

**Conceptos clave aprendidos:** tendencia, estacionalidad, estacionariedad, ADF, ACF, PACF, ARIMA, SARIMA, diferenciación, walk-forward validation
