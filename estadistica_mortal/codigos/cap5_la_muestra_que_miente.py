"""
Capítulo 5: La Muestra que Miente
Población vs muestra, tipos de muestreo, sesgo de selección
"""
import random
import numpy as np

# Población total
poblacion = list(range(1, 10001))
print(f"Poblacion total: {len(poblacion)}")

# 1. Muestreo aleatorio simple
muestra_aleatoria = random.sample(poblacion, 100)
print(f"\n1. Muestreo aleatorio simple: {len(muestra_aleatoria)} elementos")
print(f"   Primeros 10: {muestra_aleatoria[:10]}")

# 2. Muestreo sistemático
k = 100
muestra_sistematica = poblacion[::k]
print(f"\n2. Muestreo sistematico (k=100): {len(muestra_sistematica)} elementos")

# 3. Muestreo estratificado
estratos = {
    'jovenes': list(range(1, 4001)),
    'adultos': list(range(4001, 7001)),
    'mayores': list(range(7001, 10001))
}
muestra_estratificada = []
total_pob = sum(len(e) for e in estratos.values())
for nombre, elementos in estratos.items():
    n = int(len(elementos) / total_pob * 300)
    muestra_estratificada.extend(random.sample(elementos, min(n, len(elementos))))
print(f"\n3. Muestreo estratificado: {len(muestra_estratificada)} elementos")

# Sesgo de selección
poblacion_satisfaccion = np.random.normal(7.0, 1.5, 1000)
sesgo_seleccion = [s for s in poblacion_satisfaccion if s < 3 or s > 8]
print(f"\n=== SESGO DE SELECCION ===")
print(f"Media real: {np.mean(poblacion_satisfaccion):.2f}")
print(f"Media sesgada: {np.mean(sesgo_seleccion):.2f}")
print(f"Error: {abs(np.mean(poblacion_satisfaccion) - np.mean(sesgo_seleccion)):.2f}")

# Análisis de logs
logs_disponibles = 52
total_estimado = 500
proporcion = logs_disponibles / total_estimado
margen_error = 1 / (logs_disponibles ** 0.5)
print(f"\nProporcion muestra: {proporcion:.1%}")
print(f"Margen de error potencial: ±{margen_error*100:.1f}%")
