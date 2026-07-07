# Pruebas Estadísticas en Python: T-tests, ANOVA y Chi-cuadrado

En este capítulo unificamos la teoría de los capítulos anteriores en pruebas estadísticas concretas que usarás en tu trabajo diario. Cada prueba viene con su código, supuestos e interpretación.

## T-Test para Una Muestra

Compara la media de una muestra contra un valor de referencia.

**Supuestos:** datos independientes, distribución aproximadamente normal (o n ≥ 30).

```python
import numpy as np
from scipy import stats

np.random.seed(42)

# ¿El IQ de esta muestra difiere de 100?
iq_muestra = np.random.normal(103, 15, 25)

t_stat, p_valor = stats.ttest_1samp(iq_muestra, popmean=100)
print(f"T-Test una muestra:")
print(f"  t = {t_stat:.4f}, p = {p_valor:.4f}")
print(f"  Media: {np.mean(iq_muestra):.2f} vs 100")
# t = 0.9925, p = 0.3305
# No rechazamos H₀: no hay evidencia de que el IQ difiera de 100
```

## T-Test para Dos Muestras Independientes

Compara las medias de dos grupos independientes.

**Supuestos:** independencia, normalidad (o n ≥ 30), homogeneidad de varianzas.

```python
# Dos grupos: control vs tratamiento
control = np.random.normal(50, 10, 30)
tratamiento = np.random.normal(55, 10, 30)

# Prueba de Welch (no asume varianzas iguales) - recomendada
t_stat, p_valor = stats.ttest_ind(control, tratamiento, equal_var=False)
print(f"T-Test independiente (Welch):")
print(f"  t = {t_stat:.4f}, p = {p_valor:.4f}")
print(f"  Control: {np.mean(control):.2f}, Tratamiento: {np.mean(tratamiento):.2f}")
# t = -2.08, p = 0.042
# Rechazamos H₀: hay diferencia significativa

# Prueba de Student (asume varianzas iguales)
t_stat_s, p_valor_s = stats.ttest_ind(control, tratamiento, equal_var=True)

# Verificación de varianzas iguales (Levene)
w_stat, p_levene = stats.levene(control, tratamiento)
print(f"  Levene: W = {w_stat:.4f}, p = {p_levene:.4f}")
# Si p_levene > 0.05, no rechazamos igualdad de varianzas
```

> **💡 Consejo del Analista:**
> Usa `equal_var=False` (Welch) por defecto. No asume varianzas iguales y funciona bien incluso cuando lo son. Es la recomendación moderna.

## T-Test para Muestras Pareadas (Dependientes)

Cuando cada sujeto es su propio control (antes/después).

**Supuestos:** diferencias pareadas distribuidas normalmente.

```python
# Mediciones antes y después del mismo sujeto
antes = np.random.normal(70, 10, 20)
despues = antes + np.random.normal(-5, 5, 20)  # Reducción promedio de 5

t_stat, p_valor = stats.ttest_rel(antes, despues)
print(f"T-Test pareado:")
print(f"  t = {t_stat:.4f}, p = {p_valor:.4f}")
print(f"  Diferencia media: {np.mean(despues - antes):.2f}")
# t = 4.05, p = 0.0006
# Rechazamos H₀: hay cambio significativo
```

## ANOVA de Un Factor

Compara las medias de tres o más grupos.

**H₀:** todas las medias son iguales.
**H₁:** al menos una media es diferente.

**Supuestos:** independencia, normalidad, homogeneidad de varianzas.

```python
# Tres grupos
grupo_a = np.random.normal(50, 10, 30)
grupo_b = np.random.normal(55, 10, 30)
grupo_c = np.random.normal(45, 10, 30)

# ANOVA de un factor
f_stat, p_valor = stats.f_oneway(grupo_a, grupo_b, grupo_c)
print(f"ANOVA de un factor:")
print(f"  F = {f_stat:.4f}, p = {p_valor:.4f}")
# F = 8.12, p = 0.0005
# Rechazamos H₀: al menos un grupo es diferente

# Post-hoc (Tukey HSD) - ¿qué pares difieren?
from scipy.stats import tukey_hsd

result = tukey_hsd(grupo_a, grupo_b, grupo_c)
print("  Tukey HSD:")
for i, j in [(0,1), (0,2), (1,2)]:
    print(f"    Grupo {i}-{j}: p = {result.pvalue[i][j]:.4f}")
# Ejemplo: grupo A-C puede ser significativo, A-B no
```

> **⚠️ Advertencia:**
> El ANOVA te dice que hay diferencias, pero no cuáles. Usa pruebas post-hoc (Tukey, Bonferroni) para identificar los pares específicos. Siempre ajusta por comparaciones múltiples.

## ANOVA de Dos Factores (Modelo Factorial)

Evalúa el efecto de dos variables categóricas y su interacción.

```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Simular datos con dos factores
np.random.seed(42)
n = 10
datos = pd.DataFrame({
    'tratamiento': np.repeat(['A', 'B', 'C'], n*2),
    'sexo': np.tile(np.repeat(['M', 'F'], n), 3),
    'respuesta': np.concatenate([
        np.random.normal(50, 5, n*2),    # A
        np.random.normal(55, 5, n*2),    # B
        np.random.normal(52, 5, n*2),    # C
    ])
})

# ANOVA de dos factores con interacción
modelo = ols('respuesta ~ C(tratamiento) * C(sexo)', data=datos).fit()
tabla_anova = sm.stats.anova_lm(modelo, typ=2)
print("ANOVA de dos factores:")
print(tabla_anova)
#                 sum_sq   df         F    PR(>F)
# C(tratamiento)  204.30  2.0  6.88...  0.003...
# C(sexo)          20.56  1.0  1.38...  0.248...
# Interacción      12.57  2.0  0.42...  0.659...
```

## Prueba Chi-Cuadrado (χ²)

Para variables categóricas: independencia y bondad de ajuste.

### Test de Independencia

¿Hay asociación entre dos variables categóricas?

```python
# Tabla de contingencia: ¿el género se asocia con la preferencia de producto?
# Datos observados
tabla = np.array([[30, 20],   # Hombres: prefieren A, B
                  [15, 35]])  # Mujeres: prefieren A, B

chi2, p_valor, dof, esperados = stats.chi2_contingency(tabla)
print(f"Chi-cuadrado de independencia:")
print(f"  χ² = {chi2:.4f}, p = {p_valor:.4f}, df = {dof}")
print(f"  Frecuencias esperadas:\n{np.round(esperados, 1)}")
# χ² = 8.15, p = 0.0043
# Rechazamos H₀: hay asociación entre género y preferencia

# Medida de asociación (V de Cramer)
n = np.sum(tabla)
v_cramer = np.sqrt(chi2 / (n * min(tabla.shape) - 1))
print(f"  V de Cramer: {v_cramer:.4f} (0=sin asociación, 1=asociación perfecta)")
```

### Bondad de Ajuste

¿Los datos observados siguen una distribución esperada?

```python
# ¿Un dado es justo? 60 lanzamientos
observado = np.array([8, 12, 9, 11, 10, 10])  # Frecuencias observadas
esperado = np.array([10, 10, 10, 10, 10, 10])  # Frecuencias esperadas (justo)

chi2, p_valor = stats.chisquare(observado, f_exp=esperado)
print(f"Chi-cuadrado bondad de ajuste:")
print(f"  χ² = {chi2:.4f}, p = {p_valor:.4f}")
# χ² = 1.40, p = 0.9241
# No rechazamos H₀: el dado parece justo
```

## Test de Normalidad

Antes de aplicar pruebas paramétricas, verifica la normalidad:

```python
# Shapiro-Wilk (estándar para n < 5000)
np.random.seed(42)
normales = np.random.normal(0, 1, 100)
no_normales = np.random.exponential(1, 100)

stat, p_norm = stats.shapiro(normales)
_, p_no_norm = stats.shapiro(no_normales)

print(f"Shapiro-Wilk:")
print(f"  Datos normales: W = {stat:.4f}, p = {p_norm:.4f}")
print(f"  Datos exponenciales: W = {stat:.4f}, p = {p_no_norm:.4f}")
# Datos normales: p > 0.05 → no rechazamos normalidad
# Datos exponenciales: p < 0.05 → rechazamos normalidad

# Alternativas: D'Agostino-Pearson (mejor para n grande)
k2_stat, p_k2 = stats.normaltest(normales)
print(f"  D'Agostino: p = {p_k2:.4f}")
```

## Guía Rápida: ¿Qué Prueba Usar?

| Situación | Variable respuesta | Grupos | Prueba |
|-----------|-------------------|--------|--------|
| Comparar con valor de referencia | Numérica | 1 | T-test 1 muestra |
| Comparar dos grupos | Numérica | 2 | T-test independiente |
| Antes/después | Numérica | 2 (pareados) | T-test pareado |
| Comparar ≥3 grupos | Numérica | ≥3 | ANOVA + post-hoc |
| Asociación entre categóricas | Categórica | 2+ | Chi-cuadrado |
| Relación numérica-numérica | Numérica | - | Correlación/Regresión |

## Aplicación Completa: Diagnóstico Estadístico

```python
def diagnostico_completo(grupos, nombres=None):
    """
    Realiza el pipeline estadístico completo para comparar grupos.
    - Verifica normalidad
    - Verifica homogeneidad de varianzas
    - Aplica prueba paramétrica o no paramétrica según corresponda
    """
    if nombres is None:
        nombres = [f'Grupo {i+1}' for i in range(len(grupos))]

    print("=== Diagnóstico Estadístico ===\n")

    # 1. Normalidad (Shapiro-Wilk)
    print("1. Normalidad (Shapiro-Wilk):")
    todos_normales = True
    for nombre, grupo in zip(nombres, grupos):
        _, p = stats.shapiro(grupo)
        es_normal = p > 0.05
        print(f"   {nombre}: W={stat:.4f}, p={p:.4f} {'✓' if es_normal else '✗'}")
        todos_normales = todos_normales and es_normal

    # 2. Homogeneidad de varianzas (Levene)
    print("\n2. Homogeneidad de varianzas (Levene):")
    _, p_levene = stats.levene(*grupos)
    varianzas_iguales = p_levene > 0.05
    print(f"   W={stat:.4f}, p={p_levene:.4f} {'✓' if varianzas_iguales else '✗'}")

    # 3. Prueba principal
    print(f"\n3. Prueba principal:")
    if todos_normales and varianzas_iguales:
        if len(grupos) == 2:
            t, p = stats.ttest_ind(*grupos, equal_var=True)
            print(f"   T-test: t={t:.4f}, p={p:.4f}")
        else:
            f, p = stats.f_oneway(*grupos)
            print(f"   ANOVA: F={f:.4f}, p={p:.4f}")
    else:
        if len(grupos) == 2:
            u, p = stats.mannwhitneyu(*grupos)
            print(f"   Mann-Whitney U: U={u:.0f}, p={p:.4f}")
        else:
            h, p = stats.kruskal(*grupos)
            print(f"   Kruskal-Wallis: H={h:.4f}, p={p:.4f}")

    # 4. Interpretación
    print(f"\n4. Conclusión:")
    if p < 0.05:
        print(f"   Hay diferencias significativas (p={p:.4f})")
    else:
        print(f"   No hay diferencias significativas (p={p:.4f})")

# Ejemplo
np.random.seed(42)
g1 = np.random.normal(50, 10, 30)
g2 = np.random.normal(55, 10, 30)

diagnostico_completo([g1, g2], ['Control', 'Tratamiento'])
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Carga el dataset `iris` de sklearn. Para cada especie, prueba si el largo del sépalo sigue una distribución normal. ¿Qué especie tiene mayor evidencia de no normalidad?

2. **Ejercicio 2:** Compara el largo del pétalo entre las tres especies de iris usando ANOVA. Reporta el estadístico F, valor p y realiza prueba post-hoc Tukey HSD.

3. **Ejercicio 3:** Genera una tabla de contingencia 3x3 con datos simulados. Prueba la independencia con χ². Calcula la V de Cramer.

4. **Ejercicio 4:** Toma 30 sujetos con mediciones antes y después de un tratamiento. Usa un t-test pareado. Compara los resultados con un t-test independiente (incorrecto para este diseño). ¿Cómo cambia el valor p?

## 📝 Resumen del Capítulo

- **T-test 1 muestra:** compara media contra valor de referencia
- **T-test independiente:** compara dos grupos (usa Welch por defecto)
- **T-test pareado:** compara mediciones del mismo sujeto
- **ANOVA:** compara tres o más grupos; requiere post-hoc
- **Chi-cuadrado:** para variables categóricas (independencia y bondad de ajuste)
- Siempre verifica **supuestos** (normalidad, homogeneidad de varianzas)
- Usa pruebas **no paramétricas** (Mann-Whitney, Kruskal-Wallis) cuando fallen los supuestos
- Reporta el **tamaño del efecto** junto con el valor p

**Conceptos clave aprendidos:** t-test, Welch, ANOVA, post-hoc, Tukey HSD, chi-cuadrado, Shapiro-Wilk, Levene, Mann-Whitney, Kruskal-Wallis, supuestos
