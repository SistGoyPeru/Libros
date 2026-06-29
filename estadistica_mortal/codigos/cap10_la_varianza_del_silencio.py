"""
Capítulo 10: La Varianza del Silencio
Varianza, desviación estándar, coeficiente de variación
"""
import numpy as np
import random

# Comparación de dispersión
conjunto_estable = [45, 46, 45, 47, 46, 45, 46, 45, 47, 46]
conjunto_variable = [30, 60, 25, 55, 35, 65, 20, 70, 40, 50]

print("=== COMPARACION DE DISPERSION ===")
for nombre, datos in [('Estable', conjunto_estable), ('Variable', conjunto_variable)]:
    media = np.mean(datos)
    varianza = np.var(datos)
    desv = np.std(datos)
    cv = (desv / media) * 100
    rango = max(datos) - min(datos)
    print(f"\n{nombre}:")
    print(f"  Media: {media:.2f}")
    print(f"  Varianza: {varianza:.2f}")
    print(f"  Desv. Estandar: {desv:.2f}")
    print(f"  CV: {cv:.2f}%")
    print(f"  Rango: {rango}")

# Detección de fraude con varianza
random.seed(42)
datos_reales = np.random.normal(71.23, 2.11, 20)
datos_manipulados = np.random.normal(74.53, 0.42, 20)

print(f"\n=== DETECCION DE FRAUDE ===")
for nombre, datos in [('Reales', datos_reales), ('Manipulados', datos_manipulados)]:
    media = np.mean(datos)
    desv = np.std(datos)
    cv = (desv / media) * 100
    print(f"\n{nombre}:")
    print(f"  Media: {media:.2f}")
    print(f"  Desv. Std: {desv:.2f}")
    print(f"  CV: {cv:.2f}%")
    if cv < 1.0:
        print(f"  ⚠ ALERTA: CV extremadamente bajo (posible fraude)")

# Coeficiente de variación en contextos
print(f"\n=== COEFICIENTE DE VARIACION ===")
contextos = [
    ("Estatura adultos (cm)", 170, 7),
    ("Peso adultos (kg)", 70, 12),
    ("Presion arterial (mmHg)", 120, 10),
    ("Datos reales", 71.2, 2.11),
    ("Datos manipulados", 74.5, 0.42),
]
for ctx, media, desv in contextos:
    cv = (desv / media) * 100
    print(f"  {ctx:<30} Media={media:<6} σ={desv:<6.2f} CV={cv:.2f}%")
