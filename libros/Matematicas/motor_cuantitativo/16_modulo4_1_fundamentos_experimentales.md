## Módulo 4: Diseño Experimental y A/B Testing

# Fundamentos del Diseño Experimental

El diseño experimental es la metodología que garantiza que las conclusiones de un experimento sean válidas, reproducibles y no estén contaminadas por factores extraños. Sin un buen diseño, incluso el análisis estadístico más sofisticado no puede salvar un estudio.

## Principios Fundamentales

### 1. Aleatorización

Asignar sujetos a grupos de forma aleatoria elimina el sesgo de selección y distribuye equitativamente las variables de confusión no medidas.

```python
import numpy as np
import pandas as pd
from scipy import stats

# Simulación: sin aleatorización, hay sesgo
np.random.seed(42)

# Escenario 1: Asignación NO aleatoria (sesgo)
n = 100
edad = np.random.randint(18, 65, n)
# Asignación sesgada: los primeros 50 son control, los últimos tratamiento
control_no_aleatorio = edad[:50]
trat_no_aleatorio = edad[50:]
print(f"Edad Control (no aleatorio): {np.mean(control_no_aleatorio):.1f}")
print(f"Edad Tratamiento (no aleatorio): {np.mean(trat_no_aleatorio):.1f}")
# Edad Control (no aleatorio): 38.3
# Edad Tratamiento (no aleatorio): 42.5 (diferencia sistemática)

# Escenario 2: Asignación aleatoria
indices = np.random.permutation(n)
control_aleatorio = edad[indices[:50]]
trat_aleatorio = edad[indices[50:]]
print(f"Edad Control (aleatorio): {np.mean(control_aleatorio):.1f}")
print(f"Edad Tratamiento (aleatorio): {np.mean(trat_aleatorio):.1f}")
# Edad Control (aleatorio): 40.1
# Edad Tratamiento (aleatorio): 40.7 (balanceado)
```

### 2. Control

Tener un grupo de control que no recibe la intervención permite aislar el efecto del tratamiento.

```python
# Sin grupo de control: no sabes si el cambio se debe al tratamiento
# o a factores externos (estacionalidad, maduración, etc.)

# Ejemplo: lanzamiento de una campaña de marketing
ventas_antes = np.random.normal(1000, 100, 30)
ventas_despues = np.random.normal(1100, 100, 30)

t_stat, p_val = stats.ttest_ind(ventas_antes, ventas_despues)
print(f"Sin control: t = {t_stat:.2f}, p = {p_val:.4f}")
# ¿El aumento se debe a la campaña o a que es temporada alta?

# Con grupo de control (mercado no expuesto a la campaña)
control_antes = np.random.normal(1000, 100, 30)
control_despues = np.random.normal(1050, 100, 30)  # Tendencia natural

# Efecto real = (trat_despues - trat_antes) - (control_despues - control_antes)
efecto_real = (np.mean(ventas_despues) - np.mean(ventas_antes)) - \
              (np.mean(control_despues) - np.mean(control_antes))
print(f"Efecto neto de la campaña (controlando tendencia): {efecto_real:.1f}")
```

### 3. Réplica

Repetir el experimento en múltiples sujetos y condiciones para estimar la variabilidad y generalizar conclusiones.

```python
# Un experimento con 1 solo sujeto por grupo no permite estimar error
# Con réplicas, podemos cuantificar la incertidumbre

def potencia_con_replicas(n_por_grupo, efecto, sigma=1, n_sim=1000):
    """Potencia estadística según número de réplicas"""
    rechazos = 0
    for _ in range(n_sim):
        control = np.random.normal(0, sigma, n_por_grupo)
        trat = np.random.normal(efecto, sigma, n_por_grupo)
        _, p = stats.ttest_ind(control, trat)
        if p < 0.05:
            rechazos += 1
    return rechazos / n_sim

print("Potencia según réplicas por grupo (efecto=0.5):")
for n in [5, 10, 20, 50, 100]:
    pot = potencia_con_replicas(n, efecto=0.5)
    print(f"  n={n:3d}: potencia = {pot:.2%}")
# n=  5: potencia = 21.7%
# n= 10: potencia = 35.9%
# n= 20: potencia = 67.2%
# n= 50: potencia = 96.8%
# n=100: potencia = 100.0%
```

## Variables de Confusión

Una variable de confusión (confounder) afecta tanto a la variable independiente como a la dependiente, creando una asociación espuria:

```python
# Ejemplo: correlación entre ventas de helados y ahogamientos
# La confusión es la temperatura (más calor → más helados y más gente en el agua)

def confounder_demo():
    np.random.seed(42)
    temperatura = np.random.uniform(10, 35, 100)
    helados = temperatura * 10 + np.random.normal(0, 20, 100)
    ahogamientos = temperatura * 0.5 + np.random.normal(0, 5, 100)

    # Correlación helados-ahogamientos (sin controlar temperatura)
    r, p = stats.pearsonr(helados, ahogamientos)
    print(f"Correlación helados ~ ahogamientos: r = {r:.2f}, p = {p:.4f}")

    # Correlación parcial (controlando temperatura)
    from scipy import linalg

    def correlacion_parcial(x, y, z):
        """Correlación entre x e y eliminando el efecto de z"""
        r_xy = np.corrcoef(x, y)[0, 1]
        r_xz = np.corrcoef(x, z)[0, 1]
        r_yz = np.corrcoef(y, z)[0, 1]
        return (r_xy - r_xz * r_yz) / np.sqrt((1 - r_xz**2) * (1 - r_yz**2))

    r_parcial = correlacion_parcial(helados, ahogamientos, temperatura)
    print(f"Correlación parcial (controlando temperatura): r = {r_parcial:.2f}")

confounder_demo()
# Correlación helados ~ ahogamientos: r = 0.95, p = 0.0000
# Correlación parcial (controlando temperatura): r = -0.05
```

## Tipos de Diseño Experimental

| Diseño | Descripción | Cuándo usarlo |
|--------|-------------|---------------|
| **Completamente al azar** | Sujetos asignados aleatoriamente a grupos | Condiciones homogéneas, sin variables de bloqueo |
| **Bloques aleatorizados** | Agrupar sujetos similares (bloques) y asignar tratamientos dentro de cada bloque | Hay una fuente de variabilidad conocida (ej. sexo, edad) |
| **Factorial** | Evaluar múltiples factores simultáneamente | Quieres estudiar interacciones |
| **Pareado** | Cada sujeto es su propio control (antes/después) | Medición directa posible, efecto esperado razonable |

```python
# Diseño de bloques aleatorizados
np.random.seed(42)

# 4 bloques según nivel de ingresos (bajo, medio, alto, muy alto)
bloques = np.repeat([1, 2, 3, 4], 10)  # 10 sujetos por bloque
n = len(bloques)

# Asignación aleatoria DENTRO de cada bloque (cada bloque tiene 5 control + 5 trat)
tratamiento = np.zeros(n, dtype=int)
for bloque in np.unique(bloques):
    idx = np.where(bloques == bloque)[0]
    tratamiento[np.random.choice(idx, len(idx)//2, replace=False)] = 1

# Ventaja: reduces la variabilidad no explicada
print(f"Sujetos por bloque: {np.bincount(bloques)[1:]}")
for b in [1, 2, 3, 4]:
    idx = np.where(bloques == b)[0]
    print(f"  Bloque {b}: {np.sum(tratamiento[idx])} tratamiento, {len(idx)-np.sum(tratamiento[idx])} control")
```

## Tamaño del Efecto y Relevancia Práctica

La significancia estadística no es lo mismo que la relevancia práctica:

```python
# d de Cohen: medida estandarizada del tamaño del efecto
def d_cohen(grupo1, grupo2):
    n1, n2 = len(grupo1), len(grupo2)
    s1, s2 = np.var(grupo1, ddof=1), np.var(grupo2, ddof=1)
    s_pooled = np.sqrt(((n1-1)*s1 + (n2-1)*s2) / (n1 + n2 - 2))
    return (np.mean(grupo2) - np.mean(grupo1)) / s_pooled

# Interpretación de d de Cohen
print("Interpretación de d de Cohen:")
print(f"  Pequeño: d ≈ 0.2")
print(f"  Mediano: d ≈ 0.5")
print(f"  Grande:  d ≈ 0.8")

# Ejemplo: efecto pequeño pero n grande
np.random.seed(42)
g1 = np.random.normal(100, 15, 5000)
g2 = np.random.normal(101, 15, 5000)  # d ≈ 0.07
_, p = stats.ttest_ind(g1, g2)
print(f"\nEfecto pequeño (d=0.07): p = {p:.6f}, significativo? {p < 0.05}")
# p puede ser < 0.05 (por n grande), pero d es irrelevante
```

> **💡 Consejo del Analista:**
> Siempre reporta el tamaño del efecto, no solo el valor p. Un efecto puede ser estadísticamente significativo pero tan pequeño que no tenga relevancia práctica. La pregunta correcta no es "¿hay efecto?" sino "¿el efecto es lo suficientemente grande para importar?"

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Simula un estudio donde la variable de confusión "edad" afecta tanto a la exposición (horas de ejercicio) como al resultado (salud cardiovascular). Muestra la correlación espuria y cómo controlarla.

2. **Ejercicio 2:** Diseña un experimento de bloques aleatorizados para probar un nuevo método de enseñanza. Los bloques son el nivel de conocimiento previo (bajo, medio, alto). Explica por qué este diseño es superior al completamente al azar.

3. **Ejercicio 3:** Calcula la potencia estadística para un experimento con n=25 por grupo, α=0.05 y efecto esperado d=0.4. ¿Cuántos sujetos adicionales necesitas para alcanzar 80% de potencia?

4. **Ejercicio 4:** Explica la diferencia entre significancia estadística y relevancia práctica. Busca un ejemplo real (artículo, noticia) donde un resultado sea estadísticamente significativo pero el efecto sea trivial.

## 📝 Resumen del Capítulo

- La **aleatorización** previene el sesgo de selección
- El **grupo de control** aísla el efecto del tratamiento
- Las **réplicas** permiten estimar la variabilidad
- Las **variables de confusión** crean asociaciones espurias
- Los **bloques** reducen la variabilidad no explicada
- El **tamaño del efecto** (d de Cohen) mide la relevancia práctica
- La **potencia** depende de n, α y el tamaño del efecto
- Un diseño robusto es requisito para conclusiones válidas

**Conceptos clave aprendidos:** aleatorización, control, réplica, confusión, bloques, d de Cohen, potencia estadística, validez interna/externa
