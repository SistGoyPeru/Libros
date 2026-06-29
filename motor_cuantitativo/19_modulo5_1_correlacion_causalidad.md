## Módulo 5: Modelado Predictivo Básico

# Correlación vs Causalidad

"Correlación no implica causalidad" es la frase más repetida (y más ignorada) en análisis de datos. Este capítulo te da las herramientas para distinguir entre asociación y causalidad, y para identificar cuándo puedes (y cuándo no) hacer afirmaciones causales.

## Correlación: Midiendo Asociación

La *correlación* mide la fuerza y dirección de una relación lineal entre dos variables.

### Correlación de Pearson

Asume relación lineal y datos continuos:

```python
import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(42)

# Correlación positiva fuerte
x = np.random.normal(50, 10, 100)
y = 2 * x + np.random.normal(0, 10, 100)

r_pearson, p_valor = stats.pearsonr(x, y)
print(f"Correlación de Pearson: r = {r_pearson:.4f}, p = {p_valor:.4e}")
# r = 0.8938, p < 0.001 (fuerte y significativa)
```

### Correlación de Spearman

No asume linealidad; usa rangos. Robusta a outliers:

```python
# Relación monótona no lineal
x = np.random.uniform(1, 10, 100)
y = np.exp(x) + np.random.normal(0, 50, 100)

r_pearson, _ = stats.pearsonr(x, y)
r_spearman, _ = stats.spearmanr(x, y)

print(f"Pearson: r = {r_pearson:.4f}")
print(f"Spearman: ρ = {r_spearman:.4f}")
# Pearson puede subestimar si la relación no es lineal
# Spearman captura la relación monótona
```

### Matriz de Correlación

```python
import pandas as pd

# Dataset con múltiples variables correlacionadas
np.random.seed(42)
n = 100
datos = pd.DataFrame({
    'ingresos': np.random.normal(50000, 10000, n),
    'edad': np.random.normal(40, 12, n),
    'gastos': np.random.normal(30000, 8000, n),
})

# Introducir correlaciones
datos['gastos'] = datos['ingresos'] * 0.6 + np.random.normal(0, 3000, n)
datos['ahorros'] = datos['ingresos'] - datos['gastos'] + np.random.normal(0, 2000, n)

matriz_corr = datos.corr()
print("Matriz de correlación:")
print(matriz_corr.round(3))
#             ingresos   edad  gastos  ahorros
# ingresos      1.000  0.021   0.886    0.355
# edad          0.021  1.000   0.018    0.010
# gastos        0.886  0.018   1.000   -0.120
# ahorros       0.355  0.010  -0.120    1.000
```

## Por Qué Correlación No Es Causalidad

### 1. Causalidad Inversa

```python
# Ejemplo: ¿más bomberos causan más daños?
# O: ¿más incendios graves requieren más bomberos?

# Simulación
np.random.seed(42)
n = 50
gravedad_incendio = np.random.exponential(3, n)  # Tamaño del incendio
bomberos = 5 + 2 * gravedad_incendio + np.random.normal(0, 2, n)  # Más bomberos si es grave
danos = 100 * gravedad_incendio + np.random.normal(0, 10, n)  # Más daño si es grave

r, p = stats.pearsonr(bomberos, danos)
print(f"Correlación bomberos-daños: r = {r:.4f}, p = {p:.4f}")
# r = 0.98 (fuerte correlación positiva)
# Pero la causalidad es inversa: incendios graves → más bomberos Y más daños
```

### 2. Variable de Confusión

```python
# Ejemplo clásico: helados y ahogamientos
# La confusión es la temperatura (variable oculta)

def confundir():
    np.random.seed(42)
    temperatura = np.random.uniform(10, 35, 200)
    helados = 10 * temperatura + np.random.normal(0, 30, 200)
    ahogamientos = 0.3 * temperatura + np.random.normal(0, 2, 200)

    r, p = stats.pearsonr(helados, ahogamientos)
    print(f"Correlación helados-ahogamientos: r = {r:.4f}")
    # r ≈ 0.95 (falsa causalidad)

    # Control por temperatura (correlación parcial)
    def correlacion_parcial(x, y, z):
        r_xy = np.corrcoef(x, y)[0, 1]
        r_xz = np.corrcoef(x, z)[0, 1]
        r_yz = np.corrcoef(y, z)[0, 1]
        return (r_xy - r_xz * r_yz) / np.sqrt((1 - r_xz**2) * (1 - r_yz**2))

    r_parcial = correlacion_parcial(helados, ahogamientos, temperatura)
    print(f"Correlación parcial (controlando temp): r = {r_parcial:.4f}")
    # r ≈ 0.01 (desaparece)

confundir()
```

### 3. Sesgo de Selección

```python
# Ejemplo: los pacientes que toman el medicamento viven más...
# ... porque los pacientes más saludables tienden a tomar el medicamento

def sesgo_seleccion():
    np.random.seed(42)
    n = 500

    # Salud base (no observada)
    salud_base = np.random.normal(0, 1, n)

    # Decisión de tomar medicamento (sesgada: los más sanos lo toman)
    toma_med = (salud_base + np.random.normal(0, 0.5, n)) > 0

    # Resultado: años de vida restantes
    anos_vida = 20 + 5 * salud_base + 2 * toma_med + np.random.normal(0, 2, n)

    # Análisis ingenuo
    grupo_med = anos_vida[toma_med]
    grupo_no_med = anos_vida[~toma_med]
    print(f"Toman medicamento: media = {np.mean(grupo_med):.1f} años")
    print(f"No toman: media = {np.mean(grupo_no_med):.1f} años")
    print(f"Diferencia: {np.mean(grupo_med) - np.mean(grupo_no_med):.1f} años")
    # El efecto está inflado por el sesgo de selección

sesgo_seleccion()
```

## Criterios de Bradford Hill

Para fortalecer un argumento causal, Bradford Hill propuso 9 criterios (1965):

| Criterio | Descripción |
|----------|-------------|
| **Fuerza** | Asociación grande → más probable causal |
| **Consistencia** | Reproducible en diferentes estudios/poblaciones |
| **Especificidad** | Causa específica → efecto específico |
| **Temporalidad** | La causa precede al efecto (el más importante) |
| **Gradiente biológico** | Relación dosis-respuesta |
| **Plausibilidad** | Mecanismo explicable |
| **Coherencia** | No contradice el conocimiento existente |
| **Experimento** | Evidencia experimental |
| **Analogía** | Efectos similares tienen causas similares |

## Diseños para Establecer Causalidad

| Diseño | Validez causal | Factibilidad |
|--------|---------------|--------------|
| RCT (experimento aleatorizado) | ★★★★★ | ★★ |
| Experimentos naturales | ★★★★ | ★★★ |
| Diferencia en diferencias (DiD) | ★★★★ | ★★★ |
| Variables instrumentales (IV) | ★★★★ | ★ |
| Regresión discontinua (RDD) | ★★★★ | ★★★ |
| Cohortes prospectivos | ★★★ | ★★★★ |
| Casos y controles | ★★ | ★★★★★ |
| Transversales | ★ | ★★★★★ |

```python
# Simulación de Diferencia en Diferencias (DiD)
np.random.seed(42)

# Dos regiones: tratada y control, antes y después
n_periodo = 200
periodo = np.array([0] * n_periodo + [1] * n_periodo)
tratada = np.array([1] * n_periodo + [1] * n_periodo)
control = np.array([0] * n_periodo + [0] * n_periodo)

# Resultado: y = β₀ + β₁·post + β₂·tratada + β₃·(post×tratada)
y_control = 50 + 5 * periodo + np.random.normal(0, 5, n_periodo * 2)
y_tratada = 50 + 5 * periodo + 10 * (periodo == 1) + np.random.normal(0, 5, n_periodo * 2)

# El coeficiente de interacción (β₃ = 10) es el efecto causal estimado
import statsmodels.api as sm

df_did = pd.DataFrame({
    'y': np.concatenate([y_control, y_tratada]),
    'post': np.tile(periodo, 2),
    'tratada': np.repeat([0, 1], n_periodo * 2),
    'interaccion': np.tile(periodo, 2) * np.repeat([0, 1], n_periodo * 2)
})

modelo = sm.OLS.from_formula('y ~ post + tratada + interaccion', data=df_did).fit()
print(modelo.params)
# interaccion ≈ 10.0 → efecto causal estimado
```

> **⚠️ Advertencia:**
> Ningún método observacional puede probar causalidad con certeza absoluta. Incluso los RCT tienen limitaciones (validez externa, incumplimiento, etc.). La causalidad es un juicio que combina evidencia estadística, diseño y conocimiento del dominio.

## Correlación Espuria: El Humor de Datos

```python
# Las correlaciones espurias famosas
# - Consumo de queso per cápita ~ muertes por enredarse en sábanas
# - Número de ahogados en piscinas ~ películas de Nicolas Cage

def correlacion_espuria(n=50):
    np.random.seed(42)
    # Dos series temporales independientes
    t = np.arange(n)
    serie1 = 100 + 0.5 * t + np.random.normal(0, 10, n)  # Tendencia
    serie2 = 50 + 0.3 * t + np.random.normal(0, 8, n)   # Tendencia

    r, p = stats.pearsonr(serie1, serie2)
    print(f"Correlación entre series con tendencia: r = {r:.4f}, p = {p:.4f}")
    # r ≈ 0.90 (espuria: ambas tienen tendencia temporal)

    # Solución: analizar diferencias o residuales
    serie1_diff = np.diff(serie1)
    serie2_diff = np.diff(serie2)
    r_diff, p_diff = stats.pearsonr(serie1_diff, serie2_diff)
    print(f"Correlación de diferencias: r = {r_diff:.4f}, p = {p_diff:.4f}")
    # r ≈ 0.0 (la correlación espuria desaparece)

correlacion_espuria()
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Encuentra 3 ejemplos de correlaciones espurias en datos reales o simulados. Explica la posible variable de confusión en cada caso.

2. **Ejercicio 2:** Simula un escenario de causalidad inversa: los hospitales con más camas tienen mayor mortalidad. ¿La causalidad es que más camas causan muerte? Explica.

3. **Ejercicio 3:** Implementa un análisis de diferencia en diferencias con datos simulados. Crea un escenario donde una política implementada en una región (y no en otra vecina) produce un cambio en el resultado de interés.

4. **Ejercicio 4:** Usando el dataset `mtcars` (o cualquier otro), identifica pares de variables con alta correlación pero donde claramente no hay relación causal. Explica por qué.

## 📝 Resumen del Capítulo

- La **correlación** mide asociación, no causalidad
- **Pearson** asume linealidad; **Spearman** usa rangos (no paramétrica)
- **Causalidad inversa:** A causa B, o B causa A
- **Variables de confusión:** Z causa tanto a X como a Y
- **Sesgo de selección:** la muestra no representa a la población
- Los **criterios de Bradford Hill** guían el juicio causal
- **RCTs** son el estándar de oro para causalidad
- **DiD, IV, RDD** son alternativas observacionales
- Las **tendencias temporales** producen correlaciones espurias

**Conceptos clave aprendidos:** correlación de Pearson/Spearman, causalidad inversa, confusión, sesgo de selección, Bradford Hill, RCT, DiD, variable instrumental, correlación espuria
