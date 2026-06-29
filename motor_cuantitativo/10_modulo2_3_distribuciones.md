# Distribuciones de Probabilidad Clave

Una distribución de probabilidad describe cómo se comporta una variable aleatoria. Es el puente entre los datos que ves y el proceso que los generó. Conocer distribuciones es reconocer patrones universales en los datos.

## Variables Aleatorias Discretas vs Continuas

| Tipo | Valores | Ejemplo | Distribuciones típicas |
|------|---------|---------|------------------------|
| Discreta | Conjunto contable | Número de clientes | Binomial, Poisson |
| Continua | Intervalo real | Altura, tiempo, precio | Normal, Exponencial |

## Distribuciones Discretas

### Distribución Bernoulli

Modela un experimento con dos resultados: éxito (1) o fracaso (0).

```python
from scipy import stats
import numpy as np

# Bernoulli: p = 0.7 (70% de éxito)
p = 0.7
bernoulli = stats.bernoulli(p)

# Probabilidad de cada resultado
print(f"P(X=0) = {bernoulli.pmf(0):.3f}")  # 0.300
print(f"P(X=1) = {bernoulli.pmf(1):.3f}")  # 0.700

# Media y varianza
print(f"Media: {bernoulli.mean():.3f}, Varianza: {bernoulli.var():.3f}")
# Media: 0.700, Varianza: 0.210

# Simular 10 lanzamientos
muestra = bernoulli.rvs(size=10, random_state=42)
print(f"Muestra: {muestra}")
# Muestra: [1 1 0 1 1 1 1 1 1 1]
```

### Distribución Binomial

Modela el número de éxitos en n ensayos independientes de Bernoulli.

```python
# Binomial: n=20, p=0.3
n, p = 20, 0.3
binomial = stats.binom(n, p)

# P(X = 6) - probabilidad de exactamente 6 éxitos
print(f"P(X=6) = {binomial.pmf(6):.4f}")
# P(X=6) = 0.1916

# P(X ≤ 6) - probabilidad acumulada
print(f"P(X ≤ 6) = {binomial.cdf(6):.4f}")
# P(X ≤ 6) = 0.6077

# Media: np, Varianza: np(1-p)
print(f"Media: {binomial.mean():.1f}, Varianza: {binomial.var():.2f}")
# Media: 6.0, Varianza: 4.20

# Simulación
simulacion = binomial.rvs(size=10000, random_state=42)
print(f"Frecuencia relativa de 6 éxitos: {np.mean(simulacion == 6):.4f}")
# ~0.19 (cercano a la pmf teórica)
```

### Distribución Poisson

Modela el número de eventos en un intervalo de tiempo fijo (llamadas por hora, accidentes por día).

```python
# Poisson: λ = 3 (promedio de 3 eventos por unidad de tiempo)
lam = 3.0
poisson = stats.poisson(lam)

# P(X = 2)
print(f"P(X=2) = {poisson.pmf(2):.4f}")
# P(X=2) = 0.2240

# P(X ≤ 2)
print(f"P(X ≤ 2) = {poisson.cdf(2):.4f}")
# P(X ≤ 2) = 0.4232

# Media = Varianza = λ
print(f"Media: {poisson.mean():.1f}, Varianza: {poisson.var():.1f}")
# Media: 3.0, Varianza: 3.0

# Comparación Binomial vs Poisson para n grande, p pequeño
n, p = 1000, 0.005  # λ = np = 5
binom = stats.binom(n, p)
poiss = stats.poisson(n * p)

x = np.arange(0, 15)
print("Comparación Binomial(1000, 0.005) vs Poisson(5):")
for xi in x[:5]:
    print(f"  P(X={xi}): Binom={binom.pmf(xi):.4f}, Poisson={poiss.pmf(xi):.4f}")
# P(X=0): Binom=0.0067, Poisson=0.0067
# P(X=1): Binom=0.0336, Poisson=0.0337
# P(X=2): Binom=0.0840, Poisson=0.0842
```

> **💡 Consejo del Analista:**
> La distribución Poisson aproxima la Binomial cuando n es grande (>100) y p es pequeño (<0.01). Esto es útil porque Poisson solo depende de λ = np, simplificando los cálculos.

## Distribuciones Continuas

### Distribución Normal (Gaussiana)

La distribución más importante en estadística. Descrita por dos parámetros: media μ y desviación estándar σ.

```python
# Normal estándar: N(0, 1)
normal_std = stats.norm(0, 1)

# Percentiles clave (para intervalos de confianza)
print(f"z(0.975) = {normal_std.ppf(0.975):.4f}")  # 1.9600
print(f"z(0.995) = {normal_std.ppf(0.995):.4f}")  # 2.5758
print(f"z(0.841) = {normal_std.ppf(0.8413):.4f}") # 1.0000

# Valores personalizados
media, desv = 100, 15  # Ejemplo: CI
normal_personalizada = stats.norm(media, desv)

# ¿Qué porcentaje tiene CI entre 85 y 115?
p_85_115 = normal_personalizada.cdf(115) - normal_personalizada.cdf(85)
print(f"P(85 ≤ X ≤ 115) = {p_85_115:.4f} ({p_85_115*100:.1f}%)")
# P(85 ≤ X ≤ 115) = 0.6827 (68.3%)

# Regla empírica (68-95-99.7)
for k, pct in [(1, 68.27), (2, 95.45), (3, 99.73)]:
    p = normal_personalizada.cdf(media + k*desv) - normal_personalizada.cdf(media - k*desv)
    print(f"  ±{k}σ: {p*100:.1f}% (teórico: {pct}%)")
# ±1σ: 68.3% (teórico: 68.27%)
# ±2σ: 95.4% (teórico: 95.45%)
# ±3σ: 99.7% (teórico: 99.73%)
```

### Distribución Exponencial

Modela el tiempo entre eventos en un proceso Poisson (tiempo hasta la próxima llamada, vida útil de un componente).

```python
# Exponencial: λ = 0.5 (tasa de 0.5 eventos por unidad de tiempo)
lam = 0.5
exponencial = stats.expon(scale=1/lam)

# Tiempo promedio entre eventos: 1/λ = 2
print(f"Media: {exponencial.mean():.2f}")
# Media: 2.00

# P(X > 3) - probabilidad de esperar más de 3 unidades
p_mayor_3 = 1 - exponencial.cdf(3)
print(f"P(X > 3) = {p_mayor_3:.4f}")
# P(X > 3) = 0.2231

# Simular tiempos de espera
muestra_exp = exponencial.rvs(size=10, random_state=42)
print(f"Tiempos de espera: {np.round(muestra_exp, 2)}")
# Tiempos de espera: [1.46 0.42 2.56 0.11 2.69 ...]
```

### Distribución t de Student

Similar a la normal pero con colas más pesadas. Se usa cuando el tamaño de muestra es pequeño y la varianza poblacional es desconocida.

```python
# Comparación t-student vs normal
from scipy import stats

normal = stats.norm(0, 1)
t_3 = stats.t(df=3)    # 3 grados de libertad
t_30 = stats.t(df=30)  # 30 gl (casi normal)

print("Percentil 97.5%:")
print(f"  Normal: {normal.ppf(0.975):.4f}")
print(f"  t(3):   {t_3.ppf(0.975):.4f}")
print(f"  t(30):  {t_30.ppf(0.975):.4f}")
# Normal: 1.9600
# t(3):   3.1824 (colas más pesadas → intervalo más amplio)
# t(30):  2.0423 (casi normal)

# A medida que df → ∞, t → Normal
```

> **⚠️ Advertencia:**
> Con pocos grados de libertad (digamos, df < 30), la t-student produce intervalos de confianza más amplios que la normal. Esto es correcto: refleja la mayor incertidumbre cuando tenemos pocos datos.

### Distribución Chi-cuadrado (χ²)

Modela la suma de cuadrados de normales estándar independientes. Se usa en pruebas de independencia y bondad de ajuste.

```python
chi2 = stats.chi2(df=5)  # 5 grados de libertad

print(f"Media: {chi2.mean():.1f}")   # 5 (igual a df)
print(f"Varianza: {chi2.var():.1f}")  # 10 (2*df)

# Valor crítico para α = 0.05
print(f"χ²(0.95, df=5) = {chi2.ppf(0.95):.4f}")
# χ²(0.95, df=5) = 11.0705
```

### Distribución F de Fisher

Modela el cociente de dos chi-cuadrados independientes. Fundamental para ANOVA.

```python
f_dist = stats.f(dfn=3, dfd=20)  # 3 y 20 grados de libertad

print(f"Media: {f_dist.mean():.4f}")  # dfd/(dfd-2) ≈ 1.11
# Valor crítico para α = 0.05
print(f"F(0.95, 3, 20) = {f_dist.ppf(0.95):.4f}")
# F(0.95, 3, 20) = 3.0984
```

## Cómo Elegir la Distribución Correcta

Esta tabla te ayuda a seleccionar:

| Situación | Distribución | Parámetros clave |
|-----------|-------------|------------------|
| ¿Éxito/fracaso en un ensayo? | Bernoulli | p |
| ¿Éxitos en n ensayos? | Binomial | n, p |
| ¿Eventos raros en intervalo fijo? | Poisson | λ |
| ¿Datos simétricos, muchos valores? | Normal | μ, σ |
| ¿Tiempo entre eventos? | Exponencial | λ (tasa) |
| ¿Muestra pequeña, varianza desconocida? | t-Student | df |
| ¿Bondad de ajuste/independencia? | χ² | df |
| ¿Comparación de varianzas/ANOVA? | F | dfn, dfd |

## Verificación de Distribuciones (Q-Q Plot)

Un *Q-Q plot* compara los cuantiles de tus datos con los de una distribución teórica:

```python
import matplotlib.pyplot as plt
from scipy import stats

# Generar datos que NO son normales
np.random.seed(42)
datos_exponencial = np.random.exponential(2, 100)

# Q-Q plot contra normal
stats.probplot(datos_exponencial, dist="norm", plot=plt)
plt.title("Q-Q Plot: Datos Exponenciales vs Normal")
plt.grid(True, alpha=0.3)
# Los puntos se desvían de la línea recta → no es normal

# Para datos normales
datos_normales = np.random.normal(0, 1, 100)
stats.probplot(datos_normales, dist="norm", plot=plt)
plt.title("Q-Q Plot: Datos Normales vs Normal")
plt.grid(True, alpha=0.3)
# Los puntos siguen la línea recta → es normal
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Simula 1000 lanzamientos de una moneda (Bernoulli p=0.5). Calcula la media muestral y compárala con la media teórica. Repite con p=0.1, p=0.9. ¿Qué observas sobre la varianza?

2. **Ejercicio 2:** Un call center recibe un promedio de 5 llamadas por hora. ¿Cuál es la probabilidad de recibir exactamente 3 llamadas en una hora? ¿Y más de 8? Usa la distribución Poisson.

3. **Ejercicio 3:** Genera 100 datos de una distribución uniforme U(0, 1). Aplica la transformada de Box-Muller para convertirla en normal. Compara el histograma resultante con la distribución normal teórica.

4. **Ejercicio 4:** Toma el dataset `iris` y genera Q-Q plots para cada característica. ¿Cuáles parecen distribuirse normalmente?

## 📝 Resumen del Capítulo

- Las distribuciones **discretas** (Bernoulli, Binomial, Poisson) modelan conteos
- Las distribuciones **continuas** (Normal, Exponencial, t, χ², F) modelan mediciones
- La **Normal** es la distribución central por el TLC; todo analista debe conocerla
- La **t-Student** reemplaza a la normal con muestras pequeñas
- La **Poisson** modela eventos raros; aproxima la Binomial con n grande y p pequeño
- La **Exponencial** modela tiempos entre eventos
- El **Q-Q plot** verifica visualmente si los datos siguen una distribución

**Conceptos clave aprendidos:** función de masa (pmf), función de densidad (pdf), función de distribución (cdf), Normal, Binomial, Poisson, Exponencial, t-Student, Chi-cuadrado, Q-Q plot
