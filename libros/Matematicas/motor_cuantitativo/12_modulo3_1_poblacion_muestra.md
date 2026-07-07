## Módulo 3: Inferencia Estadística

# Población vs Muestra, Estimadores y Sesgo

La inferencia estadística responde a una pregunta fundamental: ¿qué podemos decir sobre un grupo grande (población) a partir de un subconjunto pequeño (muestra)? Este capítulo sienta las bases conceptuales y matemáticas para hacerlo correctamente.

## Población y Muestra

La *población* es el conjunto completo de individuos que te interesa estudiar. La *muestra* es un subconjunto de esa población.

```python
import numpy as np
import pandas as pd
from scipy import stats

# Población: 1 millón de ingresos anuales (distribución log-normal)
np.random.seed(42)
poblacion = np.random.lognormal(mean=10, sigma=0.5, size=1_000_000)
print(f"Población: n={len(poblacion):,}, media=${np.mean(poblacion):.2f}")
# Población: n=1,000,000, media=$22,646.68

# Una muestra aleatoria de 100 personas
muestra = np.random.choice(poblacion, size=100, replace=False)
print(f"Muestra: n={len(muestra)}, media=${np.mean(muestra):.2f}")
# Muestra: n=100, media=$22,184.72 (cercano pero no igual)

# Las muestras varían
for i in range(3):
    m = np.random.choice(poblacion, 100)
    print(f"  Muestra {i+1}: media=${np.mean(m):.2f}")
# Muestra 1: media=$21,847.23
# Muestra 2: media=$23,156.89
# Muestra 3: media=$22,512.34
```

> **⚠️ Advertencia:**
| Una muestra no es un espejo perfecto de la población. La variabilidad muestral es inevitable. La inferencia estadística cuantifica esa incertidumbre.

## Tipos de Muestreo

La forma en que seleccionas la muestra determina la validez de tus conclusiones.

```python
# Muestreo aleatorio simple (el estándar de oro)
poblacion = np.arange(1, 10001)
muestra_aleatoria = np.random.choice(poblacion, size=100, replace=False)

# Muestreo estratificado
# Dividir la población en estratos y muestrear cada uno
def muestreo_estratificado(poblacion, estratos, n_por_estrato):
    indices = []
    for estrato in np.unique(estratos):
        idx_estrato = np.where(estratos == estrato)[0]
        idx_seleccion = np.random.choice(idx_estrato, n_por_estrato, replace=False)
        indices.extend(idx_seleccion)
    return poblacion[indices]

# Muestreo por conglomerados (cluster)
# Seleccionar grupos completos al azar
conglomerados = np.arange(100)
conglomerados_seleccionados = np.random.choice(conglomerados, 10, replace=False)
```

## Parámetros y Estimadores

- **Parámetro:** valor numérico que describe a la población (casi siempre desconocido)
- **Estimador:** fórmula o regla para calcular un valor a partir de la muestra
- **Estimación:** el valor numérico que obtienes al aplicar el estimador a una muestra concreta

```python
# Relación parámetro-estimador
def analizar_estimadores(poblacion, n_muestra=50, n_simulaciones=10000):
    """Analiza el comportamiento de diferentes estimadores"""
    estimaciones_media = []
    estimaciones_mediana = []
    estimaciones_var_n = []   # Divide por n
    estimaciones_var_n1 = []  # Divide por n-1

    for _ in range(n_simulaciones):
        muestra = np.random.choice(poblacion, n_muestra)
        estimaciones_media.append(np.mean(muestra))
        estimaciones_mediana.append(np.median(muestra))
        estimaciones_var_n.append(np.var(muestra, ddof=0))   # Varianza muestral (n)
        estimaciones_var_n1.append(np.var(muestra, ddof=1))  # Varianza muestral (n-1)

    parametro_media = np.mean(poblacion)
    parametro_varianza = np.var(poblacion)

    print(f"Parámetro poblacional (media): {parametro_media:.2f}")
    print(f"Media de las estimaciones de media: {np.mean(estimaciones_media):.2f} (sesgo={np.mean(estimaciones_media)-parametro_media:.3f})")
    print(f"Media de las estimaciones de mediana: {np.mean(estimaciones_mediana):.2f} (sesgo={np.mean(estimaciones_mediana)-parametro_media:.3f})")
    print(f"Media de var(n): {np.mean(estimaciones_var_n):.2f} (sesgo={np.mean(estimaciones_var_n)-parametro_varianza:.3f})")
    print(f"Media de var(n-1): {np.mean(estimaciones_var_n1):.2f} (sesgo={np.mean(estimaciones_var_n1)-parametro_varianza:.3f})")

analizar_estimadores(poblacion, n_muestra=30, n_simulaciones=5000)
# Parámetro poblacional (media): 22646.68
# Media de las estimaciones de media: 22638.21 (sesgo=-8.47) ← insesgado
# Media de las estimaciones de mediana: 18824.92 (sesgo=-3821.76) ← sesgado
# Media de var(n): 49022361.34 (sesgo=-1757493.29) ← sesgado
# Media de var(n-1): 50158803.42 (sesgo=-620119.21) ← menos sesgado
```

## Sesgo de un Estimador

El *sesgo* (bias) es la diferencia entre el valor esperado del estimador y el valor real del parámetro:

```
Sesgo(θ̂) = E[θ̂] - θ
```

Un estimador es **insesgado** si su valor esperado coincide con el parámetro.

### Corrección de Bessel (n-1)

La varianza muestral con n-1 es insesgada para la varianza poblacional. ¿Por qué n-1 y no n? Porque la media muestral es un estimador que "consume" un grado de libertad:

```python
# Demostración visual de la corrección de Bessel
n_muestra = 10
sesgo_n = []
sesgo_n1 = []

for n in range(5, 100, 5):
    estimaciones_n = []
    estimaciones_n1 = []
    for _ in range(10000):
        muestra = np.random.normal(50, 10, n)
        estimaciones_n.append(np.var(muestra, ddof=0))
        estimaciones_n1.append(np.var(muestra, ddof=1))

    var_pob = 100  # σ² = 100
    sesgo_n.append(np.mean(estimaciones_n) - var_pob)
    sesgo_n1.append(np.mean(estimaciones_n1) - var_pob)

print("Sesgo de la varianza muestral según n:")
print(f"  Con n:   promedio = {np.mean(sesgo_n):.2f} (subestima sistemáticamente)")
print(f"  Con n-1: promedio = {np.mean(sesgo_n1):.2f} (prácticamente insesgado)")
# Con n:   promedio = -1.02 (subestima)
# Con n-1: promedio = 0.01 (insesgado)
```

## Error Cuadrático Medio (MSE)

El MSE combina sesgo y varianza en una sola métrica:

```
MSE = Sesgo²(θ̂) + Var(θ̂)
```

```python
# Trade-off sesgo-varianza
from scipy import stats

def mse_sesgo_varianza(poblacion, estimador_func, n_muestra, n_simulaciones=10000):
    estimaciones = []
    for _ in range(n_simulaciones):
        muestra = np.random.choice(poblacion, n_muestra)
        estimaciones.append(estimador_func(muestra))

    param = np.mean(poblacion)
    sesgo = np.mean(estimaciones) - param
    varianza = np.var(estimaciones, ddof=1)
    mse = np.mean((np.array(estimaciones) - param)**2)

    print(f"Sesgo: {sesgo:.3f}")
    print(f"Varianza: {varianza:.3f}")
    print(f"MSE: {mse:.3f}")
    print(f"Sesgo² + Varianza: {sesgo**2 + varianza:.3f}")

# Comparar media vs mediana para estimar la media poblacional
# en una distribución normal (sin outliers)
poblacion_normal = np.random.normal(50, 10, 100000)

print("--- Estimando la media con la MEDIA muestral ---")
mse_sesgo_varianza(poblacion_normal, np.mean, n_muestra=30)

print("\n--- Estimando la media con la MEDIANA muestral ---")
mse_sesgo_varianza(poblacion_normal, np.median, n_muestra=30)
# La media muestral es mejor (menor MSE) para datos normales
```

## Consistencia y Eficiencia

Un estimador es **consistente** si converge al parámetro a medida que n crece:

```python
# Consistencia de la media muestral
parametro = np.mean(poblacion)
sesgos = []

for n in [5, 10, 50, 100, 500, 1000]:
    estimaciones = [np.mean(np.random.choice(poblacion, n)) for _ in range(1000)]
    sesgo = abs(np.mean(estimaciones) - parametro)
    sesgos.append(sesgo)

print("Consistencia de la media muestral:")
for n, s in zip([5, 10, 50, 100, 500, 1000], sesgos):
    print(f"  n={n:4d}: |sesgo| = {s:.2f}")
# n=   5: |sesgo| = 173.54
# n=  10: |sesgo| = 124.30
# n=  50: |sesgo| = 41.94
# n= 100: |sesgo| = 32.13
# n= 500: |sesgo| = 13.92
# n=1000: |sesgo| = 10.75
```

La **eficiencia** compara la varianza de dos estimadores insesgados. El más eficiente tiene menor varianza.

## Aplicación Práctica: Estimación de la Media con Intervalo

```python
def estimar_media(datos, confianza=0.95):
    """Estima la media poblacional con intervalo de confianza"""
    n = len(datos)
    media_muestral = np.mean(datos)
    error_std = np.std(datos, ddof=1) / np.sqrt(n)
    z = stats.norm.ppf(1 - (1 - confianza) / 2)

    return {
        'media': media_muestral,
        'error_std': error_std,
        'margen': z * error_std,
        'ic_inf': media_muestral - z * error_std,
        'ic_sup': media_muestral + z * error_std,
        'confianza': confianza
    }

muestra_ejemplo = np.random.choice(poblacion, 200)
resultado = estimar_media(muestra_ejemplo, 0.95)
print(f"Media estimada: {resultado['media']:.2f}")
print(f"IC 95%: [{resultado['ic_inf']:.2f}, {resultado['ic_sup']:.2f}]")
print(f"Media poblacional real: {np.mean(poblacion):.2f}")
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Genera una población de 100,000 valores con `np.random.exponential(scale=3)`. Toma 1000 muestras de tamaño n=20 y calcula la media de cada una. ¿La media de las medias muestrales se aproxima a la media poblacional?

2. **Ejercicio 2:** Demuestra que la varianza muestral con ddof=0 es sesgada. Simula 10000 muestras de tamaño n=10 de una normal(0,1). Compara la media de `np.var(muestra, ddof=0)` con la varianza poblacional.

3. **Ejercicio 3:** Para una distribución asimétrica (exponencial), compara el MSE de la media vs la mediana como estimadores de la media poblacional. ¿Cuál tiene menor MSE? ¿Por qué?

4. **Ejercicio 4:** Implementa una función que calcule el tamaño de muestra necesario para estimar una media con un margen de error dado, usando la fórmula: n = (z·σ/M)².

## 📝 Resumen del Capítulo

- La **población** es el conjunto total; la **muestra** es un subconjunto
- La **inferencia** usa la muestra para concluir sobre la población
- El **sesgo** es la diferencia sistemática entre estimador y parámetro
- La **varianza muestral** con n-1 (corrección de Bessel) es insesgada
- El **MSE** = sesgo² + varianza; captura el trade-off entre ambos
- Un estimador **consistente** mejora al aumentar n
- La **eficiencia** compara la varianza de estimadores competidores

**Conceptos clave aprendidos:** población, muestra, parámetro, estimador, sesgo, corrección de Bessel, MSE, consistencia, eficiencia, error estándar
