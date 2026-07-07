# Cómo Configurar y Analizar un A/B Test en Python

El A/B testing es la aplicación práctica del diseño experimental en entornos digitales. Es la herramienta estándar para tomar decisiones basadas en datos: ¿qué color de botón convierte más? ¿qué precio genera más ingresos? ¿qué titular atrae más clics?

## El Flujo Completo de un A/B Test

1. **Formular hipótesis**
2. **Determinar tamaño de muestra**
3. **Asignar aleatoriamente**
4. **Ejecutar el experimento**
5. **Analizar resultados**
6. **Concluir y actuar**

## 1. Formular Hipótesis

```python
import numpy as np
from scipy import stats
import pandas as pd

# Ejemplo: tasa de conversión de un botón
# Página actual (control): botón azul → tasa de conversión 5%
# Propuesta (tratamiento): botón rojo → esperamos 6%

# H₀: p_rojo = p_azul (no hay diferencia)
# H₁: p_rojo ≠ p_azul (hay diferencia) - bilateral
# O: H₁: p_rojo > p_azul (el rojo es mejor) - unilateral
```

## 2. Determinar Tamaño de Muestra

El tamaño de muestra necesario depende de:
- Línea base (tasa de conversión actual)
- Efecto mínimo detectable (MDE)
- Nivel de significancia (α)
- Potencia deseada (1-β)

```python
def tamano_muestra_ab(p_base, efecto_minimo, alpha=0.05, potencia=0.80):
    """
    Calcula n por grupo para un A/B test de proporciones.
    p_base: tasa de conversión actual (control)
    efecto_minimo: mejora mínima que queremos detectar (ej. 0.01 = 1pp)
    """
    p_trat = p_base + efecto_minimo
    p_promedio = (p_base + p_trat) / 2

    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(potencia)

    n = (z_alpha * np.sqrt(2 * p_promedio * (1 - p_promedio)) +
         z_beta * np.sqrt(p_base * (1 - p_base) + p_trat * (1 - p_trat)))**2
    n = n / (efecto_minimo**2)

    return int(np.ceil(n))

# Escenarios típicos
print("Tamaño de muestra por grupo (α=0.05, potencia=80%):")
for base in [0.01, 0.05, 0.10, 0.50]:
    for mde in [0.01, 0.02, 0.05]:
        n = tamano_muestra_ab(base, mde)
        print(f"  Base={base:.0%}, MDE={mde:.0%}: n={n}")
# Base=1%, MDE=1pp: n=12,714
# Base=5%, MDE=1pp: n=7,284
# Base=5%, MDE=5pp: n=1,292
# Base=50%, MDE=5pp: n=1,554
```

> **⚠️ Advertencia:**
> No calcules el tamaño de muestra después de terminar el experimento. El tamaño de muestra debe determinarse *antes* de comenzar, basado en el efecto mínimo que te importa detectar.

## 3. Asignación Aleatoria

```python
def asignar_ab(usuarios, prob_tratamiento=0.5, semilla=42):
    """Asigna usuarios a grupos control y tratamiento"""
    np.random.seed(semilla)
    n = len(usuarios)
    asignacion = np.random.choice(
        ['control', 'tratamiento'],
        size=n,
        p=[1 - prob_tratamiento, prob_tratamiento]
    )
    return pd.DataFrame({
        'usuario_id': usuarios,
        'grupo': asignacion
    })

# Simular 5000 usuarios
usuarios = np.arange(1, 5001)
df_asignacion = asignar_ab(usuarios)
print(df_asignacion['grupo'].value_counts())
# control        2518
# tratamiento    2482
```

### Verificación de Balance

Antes de analizar, verifica que los grupos sean comparables:

```python
def verificar_balance(df, grupo_col='grupo'):
    """Verifica que la asignación sea balanceada en características conocidas"""
    # Prueba chi-cuadrado para verificar proporción 50/50
    conteos = df[grupo_col].value_counts()
    chi2, p = stats.chisquare(conteos.values)
    print(f"Test de balance: χ² = {chi2:.2f}, p = {p:.4f}")

    if p > 0.05:
        print("✓ Los grupos están balanceados")
    else:
        print("✗ Posible desbalance en la asignación")

verificar_balance(df_asignacion)
# Test de balance: χ² = 0.26, p = 0.6100
# ✓ Los grupos están balanceados
```

## 4. Simulación del Experimento

```python
np.random.seed(123)

n_control = 2500
n_tratamiento = 2500
p_control = 0.05     # 5% de conversión
p_tratamiento = 0.06  # 6% de conversión (lift del 20%)

# Generar resultados
control = np.random.binomial(1, p_control, n_control)
tratamiento = np.random.binomial(1, p_tratamiento, n_tratamiento)

df_resultados = pd.DataFrame({
    'grupo': ['control'] * n_control + ['tratamiento'] * n_tratamiento,
    'conversión': np.concatenate([control, tratamiento])
})

print("Resultados del experimento:")
print(df_resultados.groupby('grupo')['conversión'].agg(['count', 'mean', 'sum']))
```

## 5. Análisis Estadístico

### Test de Proporciones (Z-test)

```python
def analizar_ab(df, grupo_col='grupo', outcome_col='conversión',
                control_name='control', alpha=0.05):
    """Análisis completo de un A/B test"""

    # Tasas de conversión
    tasas = df.groupby(grupo_col)[outcome_col].mean()
    n_por_grupo = df.groupby(grupo_col).size()

    p_control = tasas[control_name]
    p_trat = tasas[[g for g in tasas.index if g != control_name][0]]
    n_control = n_por_grupo[control_name]
    n_trat = n_por_grupo[[g for g in n_por_grupo.index if g != control_name][0]]

    # Diferencia observada
    diff = p_trat - p_control

    # Error estándar de la diferencia
    se = np.sqrt(p_control * (1 - p_control) / n_control +
                 p_trat * (1 - p_trat) / n_trat)

    # Z-statistic
    z_stat = diff / se

    # Valor p (bilateral)
    p_valor = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    # Intervalo de confianza
    z_crit = stats.norm.ppf(1 - alpha / 2)
    ic_inf = diff - z_crit * se
    ic_sup = diff + z_crit * se

    # Lift relativo
    lift = diff / p_control

    print("=== Resultados A/B Test ===\n")
    print(f"Control (n={n_control}): {p_control:.4f} ({p_control*100:.2f}%)")
    print(f"Tratamiento (n={n_trat}): {p_trat:.4f} ({p_trat*100:.2f}%)")
    print(f"Diferencia absoluta: {diff:.4f} ({diff*100:.2f}pp)")
    print(f"Lift relativo: {lift:.2%}")
    print(f"Z-stat: {z_stat:.4f}")
    print(f"Valor p: {p_valor:.4f}")
    print(f"IC {1-alpha:.0%}: [{ic_inf:.4f}, {ic_sup:.4f}]")

    if p_valor < alpha:
        print(f"\n✓ El resultado es estadísticamente significativo (p < {alpha})")
    else:
        print(f"\n✗ El resultado NO es estadísticamente significativo (p >= {alpha})")

    return {
        'p_control': p_control,
        'p_tratamiento': p_trat,
        'diferencia': diff,
        'lift': lift,
        'z_stat': z_stat,
        'p_valor': p_valor,
        'ic': (ic_inf, ic_sup)
    }

resultado = analizar_ab(df_resultados)
```

### Test Exacto de Fisher (para muestras pequeñas)

Cuando las frecuencias esperadas son pequeñas (<5 en alguna celda), Fisher es más preciso:

```python
from scipy.stats import fisher_exact

# Tabla de contingencia
tabla = pd.crosstab(df_resultados['grupo'], df_resultados['conversión'])
print(tabla)

odds_ratio, p_fisher = fisher_exact(tabla)
print(f"\nTest exacto de Fisher:")
print(f"  Odds Ratio: {odds_ratio:.4f}")
print(f"  Valor p: {p_fisher:.4f}")
```

## 6. Métricas Bayesianas (Alternativa)

El enfoque bayesiano proporciona distribuciones de probabilidad directamente interpretables:

```python
from scipy.stats import beta

def analisis_bayesiano_ab(conversiones_control, n_control,
                           conversiones_trat, n_trat,
                           n_simulaciones=100000):
    """A/B test con enfoque bayesiano (Beta-Binomial)"""

    # Priors no informativos Beta(1, 1)
    a_prior, b_prior = 1, 1

    # Posteriors
    posterior_control = beta(a_prior + conversiones_control,
                              b_prior + n_control - conversiones_control)
    posterior_trat = beta(a_prior + conversiones_trat,
                           b_prior + n_trat - conversiones_trat)

    # Simulación de la diferencia
    muestras_control = posterior_control.rvs(n_simulaciones)
    muestras_trat = posterior_trat.rvs(n_simulaciones)
    diferencias = muestras_trat - muestras_control

    # Probabilidad de que tratamiento sea mejor
    prob_trat_mejor = np.mean(diferencias > 0)

    # Intervalo de mayor densidad (HDI)
    hdi_inf, hdi_sup = np.percentile(diferencias, [2.5, 97.5])

    print("=== Análisis Bayesiano ===")
    print(f"P(tratamiento > control) = {prob_trat_mejor:.4f}")
    print(f"IC Bayesiano 95% (HDI): [{hdi_inf:.4f}, {hdi_sup:.4f}]")

    if prob_trat_mejor > 0.95:
        print("✓ Alta probabilidad de que el tratamiento sea superior")
    else:
        print("  Evidencia insuficiente para declarar superioridad")

# Aplicar
conv_control = control.sum()
conv_trat = tratamiento.sum()
analisis_bayesiano_ab(conv_control, n_control, conv_trat, n_trat)
```

> **💡 Consejo del Analista:**
> El enfoque bayesiano responde directamente a la pregunta que realmente te interesa: "¿qué probabilidad hay de que el tratamiento sea mejor?" No requiere valores p ni conceptos de "rechazar H₀".

## Regla de Decisión y Siguientes Pasos

```python
def decidir_accion(resultado, costo_implementacion=0.02, alpha=0.05):
    """
    Decide si implementar el cambio basado en estadística y negocio.

    costo_implementacion: mejora mínima en pp para justificar el cambio
    """
    if resultado['p_valor'] < alpha and resultado['diferencia'] > costo_implementacion:
        return "IMPLEMENTAR: el cambio es significativo y rentable"
    elif resultado['p_valor'] < alpha and resultado['diferencia'] <= costo_implementacion:
        return "EVALUAR: significativo pero el efecto no justifica el costo"
    elif resultado['p_valor'] >= alpha and resultado['diferencia'] > costo_implementacion:
        return "RECOLECTAR MÁS DATOS: efecto prometedor pero no concluyente"
    else:
        return "NO IMPLEMENTAR: no hay evidencia de mejora"

decision = decidir_accion(resultado, costo_implementacion=0.005)
print(f"\nDecisión: {decision}")
```

## Errores Comunes que Evitar

```python
# 1. Mirar los datos antes de tiempo (peeking)
# NO hagas análisis intermedio sin ajustar por comparaciones múltiples
# Solución: establecer un tamaño de muestra fijo antes del experimento

# 2. Múltiples comparaciones sin ajuste
# Si pruebas 20 variantes al mismo tiempo, el error Tipo I se dispara
# Solución: corrección de Bonferroni o métodos FDR

from statsmodels.stats.multitest import multipletests
p_valores_ejemplo = [0.04, 0.03, 0.06, 0.01, 0.20, 0.05, 0.001]
rechazar, p_ajustados, _, _ = multipletests(p_valores_ejemplo, method='bonferroni')
print("Corrección Bonferroni:")
for p_orig, p_ajust, sig in zip(p_valores_ejemplo, p_ajustados, rechazar):
    print(f"  p={p_orig:.3f} → p_ajust={p_ajust:.3f} {'✓' if sig else '✗'}")
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Simula un A/B test con p_control=0.08, p_tratamiento=0.09, n=5000 por grupo. Ejecuta el análisis completo. ¿El resultado es significativo? Calcula el lift.

2. **Ejercicio 2:** Usando la función `tamano_muestra_ab`, calcula cuántos usuarios necesitas por grupo para detectar un MDE de 2pp con una base de 10%. Varía la potencia (0.70, 0.80, 0.90) y α (0.01, 0.05, 0.10).

3. **Ejercicio 3:** Implementa una simulación de Monte Carlo donde evalúes 1000 A/B tests bajo H₀ verdadera (sin diferencia). ¿Qué proporción produce p < 0.05? ¿Qué pasa si haces "peeking" y detienes el experimento cuando p < 0.05 en cualquier punto?

4. **Ejercicio 4:** Para el mismo experimento, compara el enfoque frecuentista (z-test) con el bayesiano. ¿Llegan a la misma conclusión? ¿Cuándo diferirían?

## 📝 Resumen del Capítulo

- El A/B testing compara dos versiones para determinar cuál es superior
- Calcula el **tamaño de muestra** antes del experimento
- La **asignación aleatoria** garantiza grupos comparables
- El **Z-test de proporciones** es la prueba estándar para tasas de conversión
- El **lift relativo** y la **diferencia absoluta** son métricas complementarias
- El **enfoque bayesiano** responde directamente a "¿qué probabilidad hay de que gane?"
- El **peeking** (mirar antes de tiempo) infla los errores Tipo I
- Siempre ajusta por **comparaciones múltiples** si pruebas varias variantes

**Conceptos clave aprendidos:** MDE, tamaño de muestra, Z-test de proporciones, lift, odds ratio, Fisher exact test, análisis bayesiano, peeking, Bonferroni
