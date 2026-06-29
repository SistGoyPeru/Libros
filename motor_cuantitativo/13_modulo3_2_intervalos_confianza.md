# Intervalos de Confianza

Una estimación puntual (como "la media es 23.5") es útil pero incompleta. No nos dice qué tan precisa es esa estimación. Los intervalos de confianza (IC) solucionan esto: proporcionan un rango de valores plausibles para el parámetro poblacional, junto con un nivel de confianza.

## ¿Qué es un Intervalo de Confianza?

Un IC al 95% significa: "si repitiéramos este estudio muchas veces, el 95% de los intervalos calculados contendrían el verdadero parámetro poblacional".

> **⚠️ Advertencia:**
> Un IC al 95% **NO** significa que hay 95% de probabilidad de que el parámetro esté en el intervalo. El parámetro es fijo (aunque desconocido); es el intervalo el que es aleatorio.

## IC para la Media (Varianza Conocida)

Cuando conoces σ (raro en la práctica) y los datos son normales o n es grande:

```
IC: X̄ ± z_{α/2} · σ/√n
```

```python
import numpy as np
from scipy import stats

def ic_media_conocida(datos, sigma, confianza=0.95):
    """IC para la media con varianza poblacional conocida"""
    n = len(datos)
    media = np.mean(datos)
    z = stats.norm.ppf(1 - (1 - confianza) / 2)
    margen = z * sigma / np.sqrt(n)

    return {
        'media': media,
        'margen': margen,
        'ic_inf': media - margen,
        'ic_sup': media + margen
    }

# Ejemplo: sabemos que σ = 15 (como en IQ)
np.random.seed(42)
muestra = np.random.normal(100, 15, 50)
ic = ic_media_conocida(muestra, sigma=15, confianza=0.95)
print(f"IC 95% para la media: [{ic['ic_inf']:.2f}, {ic['ic_sup']:.2f}]")
# IC 95% para la media: [96.72, 105.06]
```

## IC para la Media (Varianza Desconocida)

El caso realista: no conocemos σ, así que lo estimamos con la desviación estándar muestral s. Usamos la distribución *t de Student*:

```
IC: X̄ ± t_{α/2, n-1} · s/√n
```

```python
def ic_media_desconocida(datos, confianza=0.95):
    """IC para la media con varianza poblacional desconocida"""
    n = len(datos)
    media = np.mean(datos)
    s = np.std(datos, ddof=1)  # Desviación estándar muestral
    error_std = s / np.sqrt(n)
    t = stats.t.ppf(1 - (1 - confianza) / 2, df=n-1)
    margen = t * error_std

    return {
        'media': media,
        's': s,
        'error_std': error_std,
        'margen': margen,
        'ic_inf': media - margen,
        'ic_sup': media + margen,
        'distribucion': f't({n-1})'
    }

# Ejemplo con datos reales simulados
np.random.seed(123)
pesos = np.random.normal(70, 10, 25)  # 25 personas, media 70, desv 10
ic = ic_media_desconocida(pesos, 0.95)
print(f"Media muestral: {ic['media']:.2f}")
print(f"Desv. estándar muestral: {ic['s']:.2f}")
print(f"Error estándar: {ic['error_std']:.3f}")
print(f"IC 95%: [{ic['ic_inf']:.2f}, {ic['ic_sup']:.2f}]")
# Media muestral: 69.43
# Desv. estándar muestral: 10.74
# Error estándar: 2.148
# IC 95%: [65.00, 73.87]
```

## IC para una Proporción

Para variables binarias (éxito/fracaso):

```python
def ic_proporcion(x, n, confianza=0.95):
    """IC para una proporción (método de Wilson)"""
    p_hat = x / n
    z = stats.norm.ppf(1 - (1 - confianza) / 2)

    # Fórmula de Wilson (mejor que la aproximación normal simple)
    denominador = 1 + z**2 / n
    centro = (p_hat + z**2 / (2*n)) / denominador
    margen = z * np.sqrt(p_hat*(1-p_hat)/n + z**2/(4*n**2)) / denominador

    return {
        'proporcion': p_hat,
        'n': n,
        'ic_inf': centro - margen,
        'ic_sup': centro + margen,
        'metodo': 'Wilson'
    }

# Encuesta: 340 de 1000 votantes prefieren al candidato A
resultado = ic_proporcion(340, 1000, 0.95)
print(f"Proporción estimada: {resultado['proporcion']:.3f}")
print(f"IC 95%: [{resultado['ic_inf']:.3f}, {resultado['ic_sup']:.3f}]")
# Proporción estimada: 0.340
# IC 95%: [0.311, 0.370]
```

## Interpretación Correcta de IC

```python
# Demostración de cobertura: ¿cuántos IC contienen el verdadero parámetro?
np.random.seed(42)
media_poblacional = 100
sigma = 15
n = 30
n_experimentos = 10000

contiene = 0
for _ in range(n_experimentos):
    muestra = np.random.normal(media_poblacional, sigma, n)
    ic = ic_media_desconocida(muestra, 0.95)
    if ic['ic_inf'] <= media_poblacional <= ic['ic_sup']:
        contiene += 1

print(f"Cobertura real: {contiene/n_experimentos:.4f} (esperado: 0.95)")
# Cobertura real: ~0.9490 (muy cercano al 95%)
```

## Factores que Afectan la Amplitud del IC

| Factor | Cambio | Efecto en IC |
|--------|--------|-------------|
| Más datos (↑ n) | n = 100 en vez de 25 | Se reduce (más preciso) |
| Mayor confianza | 99% en vez de 95% | Se amplía (más seguro) |
| Más variabilidad | σ = 20 en vez de 10 | Se amplía (más incierto) |

```python
def ancho_ic(n, sigma, confianza=0.95):
    z = stats.norm.ppf(1 - (1 - confianza) / 2)
    return 2 * z * sigma / np.sqrt(n)

print("Ancho del IC para diferentes escenarios:")
print(f"n=30,  σ=10, 95%: {ancho_ic(30, 10, 0.95):.2f}")
print(f"n=100, σ=10, 95%: {ancho_ic(100, 10, 0.95):.2f}")
print(f"n=30,  σ=20, 95%: {ancho_ic(30, 20, 0.95):.2f}")
print(f"n=30,  σ=10, 99%: {ancho_ic(30, 10, 0.99):.2f}")
# n=30,  σ=10, 95%: 7.16
# n=100, σ=10, 95%: 3.92
# n=30,  σ=20, 95%: 14.31
# n=30,  σ=10, 99%: 9.42
```

## IC para la Diferencia de Dos Medias

Comparar dos grupos (la base del A/B testing):

```python
def ic_diferencia_medias(muestra1, muestra2, confianza=0.95):
    """IC para la diferencia de medias (varianzas desiguales - Welch)"""
    n1, n2 = len(muestra1), len(muestra2)
    media1, media2 = np.mean(muestra1), np.mean(muestra2)
    s1, s2 = np.std(muestra1, ddof=1), np.std(muestra2, ddof=1)

    # Error estándar de la diferencia
    se = np.sqrt(s1**2/n1 + s2**2/n2)

    # Grados de libertad (Welch-Satterthwaite)
    num = (s1**2/n1 + s2**2/n2)**2
    den = (s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1)
    df = num / den

    t = stats.t.ppf(1 - (1 - confianza) / 2, df=df)
    diferencia = media1 - media2
    margen = t * se

    return {
        'diferencia': diferencia,
        'ic_inf': diferencia - margen,
        'ic_sup': diferencia + margen,
        'df': df,
        'metodo': 'Welch'
    }

# Simular: grupo control vs tratamiento
np.random.seed(42)
control = np.random.normal(50, 10, 100)
tratamiento = np.random.normal(53, 10, 100)  # 3 puntos más

ic_diff = ic_diferencia_medias(control, tratamiento)
print(f"Diferencia (trat - control): {ic_diff['diferencia']:.2f}")
print(f"IC 95%: [{ic_diff['ic_inf']:.2f}, {ic_diff['ic_sup']:.2f}]")
# Diferencia (trat - control): 3.21
# IC 95%: [0.44, 5.98]
```

## IC vs Testing de Hipótesis

Los IC son complementarios a las pruebas de hipótesis:

```python
# Si un IC del 95% para la diferencia NO contiene 0,
# entonces un test de hipótesis al 5% rechazaría H₀: diferencia = 0
print(f"¿El IC contiene 0? {ic_diff['ic_inf'] <= 0 <= ic_diff['ic_sup']}")
# ¿El IC contiene 0? False → rechazamos H₀ con α=0.05
```

> **💡 Consejo del Analista:**
> Los intervalos de confianza son más informativos que los valores p porque muestran la magnitud del efecto y su precisión. Cuando reportes resultados, incluye siempre el IC.

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Toma una muestra de tamaño n=50 de una distribución normal(100, 15). Calcula el IC del 90%, 95% y 99% para la media. ¿Cómo cambia la amplitud?

2. **Ejercicio 2:** Simula un experimento donde el verdadero parámetro es 50. Genera 1000 muestras de tamaño n=20 y calcula el IC al 95% para cada una. ¿Qué porcentaje contiene al 50?

3. **Ejercicio 3:** En una encuesta, 120 de 500 personas prefieren el producto A. Calcula el IC del 95% para la proporción usando el método de Wilson. Interpreta el resultado.

4. **Ejercicio 4:** Dos grupos: control (n=80, media=45, s=12) y tratamiento (n=75, media=50, s=11). Calcula el IC del 95% para la diferencia de medias. ¿Hay diferencia significativa?

## 📝 Resumen del Capítulo

- Un **IC** proporciona un rango de valores plausibles para un parámetro
- El **nivel de confianza** es la frecuencia con que el IC contiene al parámetro en repeticiones del estudio
- Usa **t de Student** cuando la varianza poblacional es desconocida
- El **método de Wilson** es superior para proporciones
- IC más amplios = más confianza, menos precisión
- n más grande → IC más estrecho
- Los IC son más informativos que los valores p solos

**Conceptos clave aprendidos:** intervalo de confianza, nivel de confianza, error estándar, margen de error, t de Student, método de Wilson, IC para diferencia de medias
