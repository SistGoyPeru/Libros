# Errores Comunes en A/B Testing

El A/B testing parece simple: divides usuarios, muestras dos versiones, comparas resultados. Pero los errores sutiles invalidan la mayoría de los experimentos mal diseñados. Este capítulo cataloga los errores más frecuentes y cómo evitarlos.

## Error 1: Peeking (Mirar los Datos Antes de Tiempo)

Es el error más común. Detener el experimento cuando el valor p cruza 0.05, sin importar el tamaño de muestra acumulado.

```python
import numpy as np
from scipy import stats
import pandas as pd

# Simulación de peeking
np.random.seed(42)

def simular_peeking(p_control=0.05, p_trat=0.05, max_n=5000,
                    checkpoints=50, alpha=0.05):
    """
    Simula un A/B test con peeking.
    Bajo H₀ (p_control = p_trat), el peeking infla el error Tipo I.
    """
    n_por_paso = max_n // checkpoints
    resultados_acum = {'control': [], 'tratamiento': []}

    for paso in range(checkpoints):
        # Nuevos datos en cada paso
        nuevos_control = np.random.binomial(1, p_control, n_por_paso)
        nuevos_trat = np.random.binomial(1, p_trat, n_por_paso)

        resultados_acum['control'].extend(nuevos_control)
        resultados_acum['tratamiento'].extend(nuevos_trat)

        # Test en cada paso
        _, p_valor = stats.ttest_ind(
            resultados_acum['control'],
            resultados_acum['tratamiento']
        )

        if p_valor < alpha:
            return True, p_valor, (paso + 1) * n_por_paso

    return False, p_valor, max_n

# Simular bajo H₀ (sin efecto real)
np.random.seed(42)
n_sim = 500
peeking_positivos = 0

for _ in range(n_sim):
    detectado, _, _ = simular_peeking(0.05, 0.05, max_n=5000)
    if detectado:
        peeking_positivos += 1

print(f"Error Tipo I con peeking: {peeking_positivos/n_sim:.4f}")
print(f"Error Tipo I teórico (sin peeking): 0.0500")
# Error Tipo I con peeking: ~0.25 (5 INFLADO veces!)
```

> **💡 Consejo del Analista:**
> Si debes monitorear el experimento en tiempo real, usa un *límite de gasto alfa* (Pocock, O'Brien-Fleming) o un enfoque bayesiano que no sufra de este problema.

## Error 2: Múltiples Comparaciones

Cuantas más variantes pruebes, mayor probabilidad de encontrar un falso positivo.

```python
# Problema: probar 20 variantes contra control
n_variantes = 20
alpha = 0.05

# Probabilidad de al menos un falso positivo
p_al_menos_un_falso = 1 - (1 - alpha) ** n_variantes
print(f"P(al menos 1 falso positivo) con {n_variantes} variantes: {p_al_menos_un_falso:.3f}")
# P(al menos 1 falso positivo) con 20 variantes: 0.642 (64%!)

# Solución: corrección de Bonferroni
alpha_ajustado = alpha / n_variantes
print(f"α ajustado (Bonferroni): {alpha_ajustado:.4f}")
# α ajustado (Bonferroni): 0.0025
```

## Error 3: No Calcular el Tamaño de Muestra Anticipadamente

```python
# Escenario: ejecutas un test con n=500 por grupo
# El efecto real es pequeño (1pp de diferencia con base 5%)
n_actual = 500
base = 0.05
efecto = 0.01

poder = stats.FisherExactTest  # Placeholder
# Cálculo real:
from statsmodels.stats.power import NormalIndPower
power_analysis = NormalIndPower()
poder_real = power_analysis.solve_power(
    effect_size=efecto / np.sqrt(base * (1 - base)),
    nobs1=n_actual,
    alpha=0.05,
    ratio=1,
    alternative='two-sided'
)
print(f"Potencia con n=500: {poder_real:.2%}")
# Potencia con n=500: ~15% (de 100 experimentos, solo 15 detectarán el efecto)
```

## Error 4: Asignación No Aleatoria

```python
# Asignación por día de la semana (NO aleatoria)
# Los usuarios de fin de semana se comportan diferente

def sesgo_por_tiempo():
    np.random.seed(42)
    n_dias = 30

    # Tratamiento solo en fines de semana
    es_finde = np.array([i % 7 >= 5 for i in range(n_dias)])
    grupo = np.where(es_finde, 'tratamiento', 'control')

    # Tasa de conversión naturalmente más alta en findes
    conversion = np.where(
        es_finde,
        np.random.binomial(1, 0.08, n_dias),  # Findes: 8%
        np.random.binomial(1, 0.05, n_dias)   # Semana: 5%
    )

    # El análisis mostrará diferencia... pero es por el día, no por el tratamiento
    p_control = conversion[grupo == 'control'].mean()
    p_trat = conversion[grupo == 'tratamiento'].mean()
    print(f"Control: {p_control:.3f}, Tratamiento: {p_trat:.3f}")
    print(f"Diferencia espuria: {p_trat - p_control:.3f}")

sesgo_por_tiempo()
```

## Error 5: No Controlar por Efectos de Temporada

```python
# Ejemplo: prueba de 2 semanas, pero la primera semana es navidad
np.random.seed(42)

semana1 = np.random.normal(1000, 50, 7)  # Navidad: tráfico alto
semana2 = np.random.normal(700, 50, 7)   # Normal: tráfico bajo

# Si muestras control en semana 1 y tratamiento en semana 2
# La diferencia se deberá a la temporada, no al tratamiento
print(f"Semana 1 (Navidad): media = {np.mean(semana1):.0f}")
print(f"Semana 2 (Normal): media = {np.mean(semana2):.0f}")
print(f"Diferencia (espuria): {np.mean(semana1) - np.mean(semana2):.0f}")
```

**Solución:** ejecutar control y tratamiento simultáneamente, con asignación aleatoria continua.

## Error 6: Contaminación entre Grupos

Cuando los usuarios del grupo tratamiento influyen en los del control:

```python
# Ejemplo: red social donde usuarios del grupo A ven contenido del grupo B
# Solución: aislar los grupos (por ejemplo, por país o región)
```

## Error 7: Efecto Novedad (Novelty Effect)

Los usuarios reaccionan positivamente a cualquier cambio, solo porque es nuevo:

```python
# El efecto positivo inicial desaparece con el tiempo
# Solución: ejecutar el experimento el tiempo suficiente para que el efecto se estabilice

def efecto_novedad(n_dias=60):
    np.random.seed(42)
    # El tratamiento tiene un efecto inicial grande que decae
    dias = np.arange(n_dias)
    efecto = 0.15 * np.exp(-dias / 15)  # Decaimiento exponencial
    return dias, efecto

# Si detienes el test temprano, el efecto parece grande pero es insostenible
```

## Error 8: Segmentación Post-hoc

Encontrar segmentos donde el tratamiento "funciona" después de ver los datos:

```python
# Problema: si pruebas 20 segmentos, 1 será significativo por azar
# Solución: prueba de interacción (ANOVA de dos factores) antes de segmentar

def segmentacion_posthoc():
    np.random.seed(42)
    n_segmentos = 20
    n_por_grupo = 200

    # Generar datos donde NO hay efecto en ningún segmento
    p_valores = []
    for _ in range(n_segmentos):
        control = np.random.binomial(1, 0.05, n_por_grupo)
        trat = np.random.binomial(1, 0.05, n_por_grupo)
        _, p = stats.ttest_ind(control, trat)
        p_valores.append(p)

    significativos = sum(p < 0.05 for p in p_valores)
    print(f"De {n_segmentos} segmentos, {significativos} son 'significativos' por azar")

segmentacion_posthoc()
```

## Checklist para un A/B Test Válido

| Requisito | Por qué | Cómo verificarlo |
|-----------|---------|------------------|
| Tamaño de muestra calculado pre-experimento | Evita falsos positivos por peeking | Documentar n antes de empezar |
| Asignación aleatoria | Elimina sesgo de selección | Test χ² de balance |
| Grupos simultáneos | Controla estacionalidad | Verificar fechas |
| Sin contaminación | Aísla el efecto del tratamiento | Diseño del experimento |
| Duración suficiente (≥ 1 ciclo completo) | Captura variabilidad semanal | Mínimo 7-14 días |
| Corrección por múltiples comparaciones | Controla error Tipo I global | Bonferroni, FDR, etc. |
| Análisis pre-registrado | Evita p-hacking | Documentar plan de análisis |

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Simula 1000 experimentos con peeking y sin peeking. Compara las tasas de error Tipo I. ¿Cuánto se infla con peeking agresivo (revisión cada 10 observaciones)?

2. **Ejercicio 2:** Diseña un A/B test para una página web. Identifica potenciales fuentes de contaminación entre grupos y explica cómo las mitigarías.

3. **Ejercicio 3:** Un equipo ejecuta un test con 5 variantes y encuentra que 2 son significativas (p < 0.05). Aplica la corrección de Bonferroni. ¿Siguen siendo significativas?

4. **Ejercicio 4:** Simula un efecto novedad: un tratamiento que parece efectivo en los primeros 3 días pero cuyo efecto desaparece después de 2 semanas. ¿Cómo diseñarías el experimento para detectar esto?

## 📝 Resumen del Capítulo

- El **peeking** infla el error Tipo I (puede llegar a 25%+)
- Las **múltiples comparaciones** requieren corrección (Bonferroni, FDR)
- El **tamaño de muestra** debe calcularse antes del experimento
- La **asignación no aleatoria** introduce sesgos irreparables
- La **estacionalidad** y los **efectos de novedad** enmascaran resultados
- La **contaminación entre grupos** invalida la independencia
- La **segmentación post-hoc** sin ajuste produce falsos descubrimientos
- Usa un **checklist** de validación antes de lanzar cualquier experimento

**Conceptos clave aprendidos:** peeking, comparaciones múltiples, Bonferroni, contaminación, efecto novedad, segmentación post-hoc, p-hacking, pre-registro
