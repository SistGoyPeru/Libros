"""
Capítulo 2: La Probabilidad del Crimen
Probabilidad básica, regla de Laplace, ley de grandes números
"""
import random
from collections import Counter

# Simular lanzamiento de una moneda
caras = 0
total_lanzamientos = 1000

for _ in range(total_lanzamientos):
    if random.random() < 0.5:
        caras += 1

probabilidad_estimada = caras / total_lanzamientos
print(f"Lanzamientos: {total_lanzamientos}")
print(f"Caras obtenidas: {caras}")
print(f"Probabilidad estimada: {probabilidad_estimada:.4f}")
print(f"Probabilidad teorica: 0.5")

# Simulación de ensayo clínico
# Datos: 500 pacientes por grupo
resultados = Counter()

# Simular datos de ensayo
random.seed(42)
for _ in range(500):
    if random.random() < 0.94:
        resultados[('A', 'mejora')] += 1
    else:
        resultados[('A', 'no_mejora')] += 1
    if random.random() < 0.48:
        resultados[('B', 'mejora')] += 1
    else:
        resultados[('B', 'no_mejora')] += 1

print("\n=== RESULTADOS DEL ENSAYO ===")
for (tratamiento, resultado), conteo in sorted(resultados.items()):
    print(f"Tratamiento '{tratamiento}' - Resultado '{resultado}': {conteo}")

# Probabilidades
p_A_mejora = resultados[('A', 'mejora')] / 500
p_B_mejora = resultados[('B', 'mejora')] / 500
diferencia = p_A_mejora - p_B_mejora
print(f"\nP(mejora | A) = {p_A_mejora:.3f}")
print(f"P(mejora | B) = {p_B_mejora:.3f}")
print(f"Diferencia: {diferencia:.3f}")

# Simulación para valor p
simulaciones = 10000
diferencias_extremas = 0
resultados_totales = [1] * 710 + [0] * 290

for _ in range(simulaciones):
    random.shuffle(resultados_totales)
    grupo_A = resultados_totales[:500]
    grupo_B = resultados_totales[500:]
    pA = sum(grupo_A) / 500
    pB = sum(grupo_B) / 500
    if abs(pA - pB) >= diferencia:
        diferencias_extremas += 1

probabilidad_azar = diferencias_extremas / simulaciones
print(f"\nSimulaciones: {simulaciones}")
print(f"Probabilidad de que sea azar: {probabilidad_azar:.6f}")
