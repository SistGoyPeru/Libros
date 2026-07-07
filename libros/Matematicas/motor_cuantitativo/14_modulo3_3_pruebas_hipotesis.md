# Pruebas de Hipótesis: Valor p, Errores Tipo I y II

Las pruebas de hipótesis son el mecanismo formal para tomar decisiones basadas en datos. ¿Un nuevo fármaco funciona mejor que el placebo? ¿El rediseño de la web aumentó las conversiones? Las pruebas de hipótesis responden estas preguntas con rigor estadístico.

## La Estructura de una Prueba de Hipótesis

Toda prueba de hipótesis sigue el mismo esquema:

1. **H₀ (Hipótesis nula):** No hay efecto, no hay diferencia, el status quo
2. **H₁ (Hipótesis alternativa):** Hay efecto, hay diferencia, lo que queremos demostrar
3. **Estadístico de prueba:** Valor calculado de los datos
4. **Valor p:** Probabilidad de observar algo tan extremo como lo observado, asumiendo H₀ cierta
5. **Conclusión:** Rechazar H₀ si p < α, o no rechazar H₀

```python
import numpy as np
from scipy import stats

# Ejemplo clásico: ¿la media es diferente de 100?
np.random.seed(42)
datos = np.random.normal(105, 15, 30)  # Media real 105

# H₀: μ = 100
# H₁: μ ≠ 100 (prueba bilateral)

t_stat, p_valor = stats.ttest_1samp(datos, popmean=100)
print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p: {p_valor:.4f}")
# Estadístico t: 1.8745
# Valor p: 0.0710

alpha = 0.05
if p_valor < alpha:
    print("Rechazamos H₀: la media es diferente de 100")
else:
    print("No rechazamos H₀: no hay evidencia suficiente")
# No rechazamos H₀: no hay evidencia suficiente
```

## Valor p: La Interpretación Correcta

El *valor p* es la probabilidad de obtener un resultado tan extremo o más que el observado, asumiendo que la hipótesis nula es verdadera.

> **⚠️ Advertencia:**
| Muchas cosas que el valor p **NO** es:
| - No es la probabilidad de que H₀ sea cierta
| - No es la probabilidad de que H₁ sea cierta
| - No es la probabilidad de que el resultado se deba al azar
| - No es el tamaño del efecto

```python
# Demostración: valor p bajo H₀ verdadera
np.random.seed(42)
p_valores_bajo_H0 = []

for _ in range(10000):
    # Generar datos bajo H₀ (media = 100)
    datos = np.random.normal(100, 15, 30)
    _, p = stats.ttest_1samp(datos, 100)
    p_valores_bajo_H0.append(p)

# Bajo H₀, los valores p son uniformes
print(f"Proporción p < 0.05: {np.mean(np.array(p_valores_bajo_H0) < 0.05):.4f}")
print(f"Proporción p < 0.01: {np.mean(np.array(p_valores_bajo_H0) < 0.01):.4f}")
# Proporción p < 0.05: ~0.050 (¡exactamente α!)
# Proporción p < 0.01: ~0.010 (¡exactamente α!)
```

## Errores Tipo I y Tipo II

| Decisión | H₀ verdadera | H₀ falsa |
|----------|-------------|----------|
| No rechazar H₀ | ✅ Correcto | ❌ Error Tipo II (β) |
| Rechazar H₀ | ❌ Error Tipo I (α) | ✅ Correcto (Potencia) |

```python
def simular_errores(media_h0=100, media_real=103, sigma=15, n=50,
                    alpha=0.05, n_sim=5000):
    """Simula errores Tipo I y Tipo II"""
    # Bajo H₀ (para error tipo I)
    rechazos_bajo_H0 = 0
    for _ in range(n_sim):
        datos = np.random.normal(media_h0, sigma, n)
        _, p = stats.ttest_1samp(datos, media_h0)
        if p < alpha:
            rechazos_bajo_H0 += 1

    error_tipo_I = rechazos_bajo_H0 / n_sim

    # Bajo H₁ (para error tipo II = 1 - potencia)
    no_rechazos_bajo_H1 = 0
    for _ in range(n_sim):
        datos = np.random.normal(media_real, sigma, n)
        _, p = stats.ttest_1samp(datos, media_h0)
        if p >= alpha:
            no_rechazos_bajo_H1 += 1

    error_tipo_II = no_rechazos_bajo_H1 / n_sim
    potencia = 1 - error_tipo_II

    print(f"Error Tipo I (α real): {error_tipo_I:.4f} (nominal: {alpha})")
    print(f"Error Tipo II (β): {error_tipo_II:.4f}")
    print(f"Potencia (1-β): {potencia:.4f}")
    return error_tipo_I, error_tipo_II, potencia

print("--- Escenario: efecto pequeño (μ=103, n=50) ---")
simular_errores(media_real=103, n=50)

print("\n--- Escenario: efecto grande (μ=110, n=50) ---")
simular_errores(media_real=110, n=50)

print("\n--- Escenario: muestra grande (μ=103, n=200) ---")
simular_errores(media_real=103, n=200)
# Error Tipo I siempre ~0.05 (controlado por α)
# Error Tipo II varía: mayor efecto o mayor n → menor β → mayor potencia
```

## Factores que Afectan la Potencia

La *potencia* (1 - β) es la probabilidad de detectar un efecto cuando realmente existe.

| Factor | Aumentar factor | Efecto en potencia |
|--------|----------------|-------------------|
| Tamaño de muestra (n) | Aumentar | Aumenta |
| Tamaño del efecto | Mayor | Aumenta |
| Variabilidad (σ) | Menor | Aumenta |
| α | Aumentar α | Aumenta (pero más errores Tipo I) |

```python
def calcular_potencia(tamano_efecto=0.5, n=50, alpha=0.05):
    """Potencia de un t-test usando análisis analítico"""
    df = n - 1
    t_critico = stats.t.ppf(1 - alpha/2, df)
    # Potencia = P(|T| > t_critico | δ)
    potencia = stats.nct.sf(t_critico, df, tamano_efecto*np.sqrt(n)) + \
               stats.nct.cdf(-t_critico, df, tamano_efecto*np.sqrt(n))
    return potencia

# Mapa de calor de potencia
print("Potencia según n y tamaño del efecto (d de Cohen):")
print("n\\td=0.2\td=0.5\td=0.8")
for n in [20, 50, 100, 200]:
    potencias = [calcular_potencia(d, n) for d in [0.2, 0.5, 0.8]]
    print(f"{n}\t{potencias[0]:.2f}\t{potencias[1]:.2f}\t{potencias[2]:.2f}")
# n	d=0.2	d=0.5	d=0.8
# 20	0.09	0.33	0.66
# 50	0.14	0.70	0.97
# 100	0.29	0.94	1.00
# 200	0.61	1.00	1.00
```

## Pruebas Unilaterales vs Bilaterales

```python
# Prueba unilateral: H₁: μ > 100
def ttest_unilateral_derecha(datos, mu0=100):
    t_stat, p_bilateral = stats.ttest_1samp(datos, mu0)
    p_unilateral = p_bilateral / 2 if t_stat > 0 else 1 - p_bilateral / 2
    return t_stat, p_unilateral

# Prueba bilateral: H₁: μ ≠ 100
# Prueba unilateral derecha: H₁: μ > 100
# Prueba unilateral izquierda: H₁: μ < 100

np.random.seed(42)
datos = np.random.normal(103, 15, 50)

_, p_bil = stats.ttest_1samp(datos, 100)
_, p_uni = ttest_unilateral_derecha(datos, 100)
print(f"p bilateral: {p_bil:.4f}")
print(f"p unilateral (μ > 100): {p_uni:.4f}")
# p bilateral: 0.1420
# p unilateral: 0.0710

# La unilateral tiene más potencia si la dirección es correcta
```

> **💡 Consejo del Analista:**
| Usa pruebas bilaterales por defecto. Las unilaterales solo cuando tengas una justificación sólida y previa de por qué solo una dirección es relevante.

## Potencia y Tamaño de Muestra

```python
from scipy.stats import nct

def n_para_potencia(tamano_efecto=0.5, potencia=0.80, alpha=0.05):
    """Calcula n necesario para alcanzar cierta potencia"""
    for n in range(5, 10000):
        df = n - 1
        t_crit = stats.t.ppf(1 - alpha/2, df)
        noncentral = tamano_efecto * np.sqrt(n)
        pot = nct.sf(t_crit, df, noncentral) + nct.cdf(-t_crit, df, noncentral)
        if pot >= potencia:
            return n
    return None

print("n necesario para potencia 80%:")
for d in [0.2, 0.3, 0.5, 0.8]:
    n_req = n_para_potencia(tamano_efecto=d, potencia=0.80)
    print(f"  d = {d}: n = {n_req}")
# d = 0.2: n = 199
# d = 0.3: n = 89
# d = 0.5: n = 33
# d = 0.8: n = 14
```

## El Debate del Valor p

El valor p es controvertido. La American Statistical Association emitió en 2016 seis principios sobre su uso:

1. Los valores p pueden indicar cuán incompatibles son los datos con H₀
2. Los valores p no miden la probabilidad de que H₀ sea cierta
3. Los cortes científicos (como p < 0.05) no deben usarse mecánicamente
4. La inferencia adecuada requiere transparencia y reporte completo
5. El valor p no mide el tamaño del efecto ni la importancia
6. Por sí solo, el valor p no proporciona evidencia sólida

```python
# Ejemplo: efecto pequeño pero n grande → p pequeño
np.random.seed(42)
# Diferencia minúscula pero n enorme
grupo_a = np.random.normal(100, 15, 10000)
grupo_b = np.random.normal(100.5, 15, 10000)  # Solo 0.5 de diferencia

t_stat, p_val = stats.ttest_ind(grupo_a, grupo_b)
d_cohen = (np.mean(grupo_b) - np.mean(grupo_a)) / np.std(np.concatenate([grupo_a, grupo_b]))

print(f"Diferencia: {np.mean(grupo_b) - np.mean(grupo_a):.3f}")
print(f"Valor p: {p_val:.6f}")
print(f"d de Cohen: {d_cohen:.4f} (efecto muy pequeño)")
# p < 0.05 pero el efecto es trivial
```

> **⚠️ Advertencia:**
| Un valor p pequeño no significa un efecto importante. Con muestras grandes, incluso diferencias triviales producen p < 0.05. Reporta siempre el tamaño del efecto y el intervalo de confianza.

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Simula 1000 experimentos bajo H₀ verdadera (μ=50, σ=10, n=30). ¿Qué proporción de valores p es menor que 0.05? ¿Qué proporción menor que 0.01?

2. **Ejercicio 2:** Para un efecto de d=0.4 con α=0.05, ¿cuántos sujetos necesitas para potencia del 80%? ¿Y para potencia del 95%?

3. **Ejercicio 3:** Explica con tus palabras la diferencia entre significancia estadística y significancia práctica. Da un ejemplo donde un resultado sea estadísticamente significativo pero no importante.

4. **Ejercicio 4:** Usando `scipy.stats.ttest_ind`, compara dos grupos: A (media=52, σ=10, n=30) y B (media=48, σ=10, n=30). Reporta el valor p, el IC de la diferencia y el d de Cohen. Interpreta.

## 📝 Resumen del Capítulo

- Las pruebas de hipótesis evalúan evidencia contra H₀
- El **valor p** es P(datos | H₀), no P(H₀ | datos)
- **Error Tipo I:** rechazar H₀ verdadera (α, controlado por el investigador)
- **Error Tipo II:** no rechazar H₀ falsa (β, depende de n, efecto, variabilidad)
- La **potencia** (1-β) es la probabilidad de detectar un efecto real
- n más grande → mayor potencia
- El valor p no mide el tamaño del efecto
- Siempre reporta IC y tamaño del efecto, no solo el valor p

**Conceptos clave aprendidos:** hipótesis nula y alternativa, valor p, error Tipo I, error Tipo II, potencia, tamaño del efecto, d de Cohen, prueba unilateral/bilateral
