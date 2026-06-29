# El Teorema del Límite Central

Si solo pudieras recordar un teorema de toda la estadística, este debería serlo. El Teorema del Límite Central (TLC) es la razón por la que podemos hacer inferencia estadística, construir intervalos de confianza y probar hipótesis sin conocer la distribución subyacente de los datos.

## La Idea Intuitiva

El TLC dice: **la distribución de la media muestral se aproxima a una normal a medida que el tamaño de muestra crece, independientemente de la forma de la distribución original.**

No importa si tus datos vienen de una distribución exponencial, uniforme, binomial o incluso de una mezcla extraña: el promedio de muchas observaciones se comportará como una normal.

## Demostración Práctica

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Población con distribución exponencial (muy sesgada)
poblacion = np.random.exponential(scale=2, size=100000)

print(f"Media poblacional: {np.mean(poblacion):.3f}")
print(f"Asimetría poblacional: {stats.skew(poblacion):.3f}")
# Media poblacional: 2.003
# Asimetría poblacional: ~2.0 (muy sesgada)

# Función para simular el TLC
def simular_tlc(poblacion, n_muestra, n_simulaciones=10000):
    medias_muestrales = []

    for _ in range(n_simulaciones):
        muestra = np.random.choice(poblacion, size=n_muestra)
        medias_muestrales.append(np.mean(muestra))

    return np.array(medias_muestrales)

# Probar con diferentes tamaños de muestra
for n in [2, 5, 30, 100]:
    medias = simular_tlc(poblacion, n, n_simulaciones=10000)

    media_teorica = np.mean(poblacion)
    error_std_teorico = np.std(poblacion) / np.sqrt(n)

    print(f"\nn = {n}:")
    print(f"  Media muestral: {np.mean(medias):.3f} (teórica: {media_teorica:.3f})")
    print(f"  Desv. media muestral: {np.std(medias):.3f} (teórica: {error_std_teorico:.3f})")
    print(f"  Asimetría: {stats.skew(medias):.3f}")
# n = 2:
#   Media muestral: 2.002 (teórica: 2.003)
#   Desv. media muestral: 1.413 (teórica: 1.414)
#   Asimetría: 1.444 (todavía sesgada)
#
# n = 5:
#   Media muestral: 2.001 (teórica: 2.003)
#   Desv. media muestral: 0.889 (teórica: 0.894)
#   Asimetría: 0.872 (menos sesgada)
#
# n = 30:
#   Media muestral: 2.000 (teórica: 2.003)
#   Desv. media muestral: 0.362 (teórica: 0.365)
#   Asimetría: 0.301 (casi simétrica)
#
# n = 100:
#   Media muestral: 2.002 (teórica: 2.003)
#   Desv. media muestral: 0.199 (teórica: 0.200)
#   Asimetría: 0.152 (muy cercana a normal)
```

> **💡 Consejo del Analista:**
> La "magia" ocurre alrededor de n=30. Con muestras menores, la distribución de la media aún refleja la forma de la población original. Con n ≥ 30, la normalidad es una aproximación razonable en la mayoría de los casos prácticos.

## La Fórmula del TLC

```
X̄ ~ N(μ, σ/√n)
```

Donde:
- X̄: media muestral
- μ: media poblacional
- σ: desviación estándar poblacional
- n: tamaño de muestra

El error estándar (SE = σ/√n) disminuye con la raíz cuadrada del tamaño muestral. Para reducir el error a la mitad, necesitas cuadruplicar la muestra.

```python
# Relación entre n y error estándar
sigma = 10
for n in [10, 40, 100, 400, 1000]:
    se = sigma / np.sqrt(n)
    print(f"n={n:4d}: SE = {se:.2f}")
# n=  10: SE = 3.16
# n=  40: SE = 1.58
# n= 100: SE = 1.00
# n= 400: SE = 0.50
# n=1000: SE = 0.32
```

## El TLC Explica Tres Fenómenos Clave

### 1. Por qué los promedios son normales

Aunque los datos individuales no lo sean, el promedio de muchos sí lo es. Esto justifica el uso de la media como estadístico.

### 2. Por qué importa el tamaño muestral

Muestras más grandes → distribución de la media más estrecha → estimaciones más precisas.

### 3. Por qué la variabilidad se reduce con √n

No es lineal: para duplicar precisión necesitas 4x los datos. Esto tiene implicaciones prácticas en diseño experimental y A/B testing.

## El TLC en Acción: Distribuciones No Normales

```python
# Demostración con múltiples distribuciones
distribuciones = {
    'Uniforme': np.random.uniform(0, 10, 100000),
    'Exponencial': np.random.exponential(2, 100000),
    'Binomial (p=0.1)': np.random.binomial(1, 0.1, 100000),
    'Mixta': np.concatenate([
        np.random.normal(-5, 1, 50000),
        np.random.normal(5, 1, 50000)
    ])
}

from scipy import stats

n = 30

for nombre, poblacion in distribuciones.items():
    medias = [np.mean(np.random.choice(poblacion, n))
              for _ in range(10000)]

    print(f"{nombre}:")
    print(f"  Asimetría original: {stats.skew(poblacion):.2f}")
    print(f"  Asimetría de medias (n={n}): {stats.skew(medias):.2f}")
    print(f"  ¿Normal? (p-valor Shapiro): {stats.shapiro(medias[:5000]).pvalue:.4f}\n")
# Uniforme:
#   Asimetría original: 0.00
#   Asimetría de medias (n=30): 0.00 ✓
#
# Exponencial:
#   Asimetría original: 2.00
#   Asimetría de medias (n=30): 0.30 ✓
#
# Binomial (p=0.1):
#   Asimetría original: 2.67
#   Asimetría de medias (n=30): 0.48 ✓
#
# Mixta (bimodal):
#   Asimetría original: 0.00
#   Asimetría de medias (n=30): 0.00 ✓ (¡incluso bimodal!)
```

## Aplicación: Tamaño de Muestra para una Encuesta

```python
# ¿Cuántas personas necesitas encuestar para estimar
# la intención de voto con margen de error ±3% (IC 95%)?

# Para una proporción, el error estándar máximo es con p=0.5
# SE = sqrt(p(1-p)/n)
# Margen = 1.96 * SE

def tamano_muestra(margen=0.03, confianza=0.95, p=0.5):
    """Calcula n necesario para cierto margen de error"""
    z = stats.norm.ppf(1 - (1 - confianza) / 2)
    n = (z**2 * p * (1 - p)) / (margen**2)
    return int(np.ceil(n))

print(f"n necesaria para margen ±3%: {tamano_muestra(0.03)}")
print(f"n necesaria para margen ±5%: {tamano_muestra(0.05)}")
print(f"n necesaria para margen ±1%: {tamano_muestra(0.01)}")
# n necesaria para margen ±3%: 1068
# n necesaria para margen ±5%: 385
# n necesaria para margen ±1%: 9604
```

## El TLC y su Hermano: La Ley de los Grandes Números

El TLC se confunde a menudo con la Ley de los Grandes Números (LGN). Son complementarias:

| Ley | Dice | Ejemplo |
|-----|------|---------|
| LGN | La media muestral converge a la media poblacional | Con más lanzamientos, la frecuencia de cara → 0.5 |
| TLC | La distribución de la media muestral se vuelve normal | Esa frecuencia se distribuye normalmente alrededor de 0.5 |

## Limitaciones del TLC

El TLC no es una solución universal:

1. **Colas extremadamente pesadas:** Distribuciones como Cauchy (sin media definida) no cumplen el TLC
2. **Dependencia:** Los datos deben ser (aproximadamente) independientes
3. **Muestras muy pequeñas:** Con n < 5-10, la aproximación puede ser pobre
4. **Tamaño de muestra vs población:** La muestra debe ser pequeña comparada con la población

```python
# Demostración: la distribución de Cauchy NO cumple el TLC
from scipy import stats

cauchy = stats.cauchy()
muestras_cauchy = cauchy.rvs(size=(1000, 100))
medias_cauchy = np.mean(muestras_cauchy, axis=1)

print(f"Media de las medias: {np.mean(medias_cauchy):.2f}")
print(f"Desv. de las medias: {np.std(medias_cauchy):.2f}")
print(f"¿Normal? Shapiro p-valor: {stats.shapiro(medias_cauchy[:5000]).pvalue:.4f}")
# Media de las medias: -0.18 (inestable, no converge)
# Desv. de las medias: 2.51 (no se reduce con √n)
# p-valor < 0.001 → definitivamente no normal
```

> **⚠️ Advertencia:**
> No asumas automáticamente normalidad solo porque n > 30. Verifica siempre con Q-Q plots o tests de normalidad. El TLC dice que la *media* es normal, no que los *datos individuales* lo sean.

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Toma la distribución uniforme U(0,1). Simula 5000 experimentos obteniendo la media de n=2, n=5, n=15, n=30. Para cada n, genera un histograma de las medias. ¿En qué n empieza a verse normal?

2. **Ejercicio 2:** Explica con tus palabras: ¿por qué el margen de error en encuestas se reduce con la raíz cuadrada del tamaño de muestra? Si una encuesta con 1000 personas tiene ±3%, ¿cuántas personas necesitas para ±1%?

3. **Ejercicio 3:** Genera una población con distribución bimodal (mezcla de dos normales). Demuestra que la distribución de la media muestral con n=30 es aproximadamente normal, aunque la población no lo sea.

4. **Ejercicio 4:** Encuentra un dataset real (por ejemplo, precios de viviendas) y demuestra empíricamente el TLC: la media de muestras de tamaño 50 se distribuye aproximadamente normal aunque los precios tengan una distribución sesgada.

## 📝 Resumen del Capítulo

- El **TLC** establece que la media muestral se distribuye normalmente para n grande
- La **media** de la distribución de medias muestrales = μ poblacional
- El **error estándar** (σ/√n) disminuye con la raíz cuadrada de n
- El TLC funciona independientemente de la distribución original
- La **LGN** (convergencia) y el **TLC** (forma de la distribución) son complementarios
- n ≥ 30 es una regla práctica, no un límite mágico
- El TLC tiene limitaciones: datos dependientes, colas infinitas, muestras muy pequeñas

**Conceptos clave aprendidos:** Teorema del Límite Central, error estándar, Ley de Grandes Números, distribución muestral, tamaño de muestra, margen de error
