"""
Capítulo 11: La Prueba del Chi-Cuadrado
Chi-cuadrado, tablas de contingencia, frecuencias observadas vs esperadas
"""
import numpy as np
import math

# Tabla de contingencia: Persona vs Acceso Nocturno
tabla_observada = np.array([
    [5,  73],    # Hugo
    [1,  45],    # Ramiro
    [3,  89],    # Sofia
    [12, 28],    # Viceministro
    [8,  736]    # Otros
])

personas = ['Hugo', 'Ramiro', 'Sofia', 'Viceministro', 'Otros']
total_obs = np.sum(tabla_observada)

print("=== TABLA DE CONTINGENCIA ===")
print(f"{'Persona':<15} {'Nocturnos':<12} {'Diurnos':<12} {'Total':<8}")
print("-" * 47)
for i, p in enumerate(personas):
    print(f"{p:<15} {tabla_observada[i,0]:<12} {tabla_observada[i,1]:<12} {tabla_observada[i,0]+tabla_observada[i,1]:<8}")
print("-" * 47)
print(f"{'Total':<15} {np.sum(tabla_observada, axis=0)[0]:<12} {np.sum(tabla_observada, axis=0)[1]:<12} {total_obs:<8}")

# Frecuencias esperadas
totales_col = np.sum(tabla_observada, axis=0)
tabla_esperada = np.zeros_like(tabla_observada, dtype=float)
for i in range(len(personas)):
    total_fila = np.sum(tabla_observada[i, :])
    for j in range(2):
        tabla_esperada[i, j] = (total_fila * totales_col[j]) / total_obs

print(f"\n=== FRECUENCIAS ESPERADAS ===")
for i, p in enumerate(personas):
    print(f"  {p:<15} Noct: {tabla_esperada[i,0]:.1f}  Diur: {tabla_esperada[i,1]:.1f}")

# Cálculo chi-cuadrado
chi2 = 0
for i in range(len(personas)):
    for j in range(2):
        o = tabla_observada[i, j]
        e = tabla_esperada[i, j]
        contrib = (o - e) ** 2 / e
        chi2 += contrib
        if contrib > 1:
            print(f"\n{personas[i]}: contribucion = {contrib:.2f}")

gl = (len(personas) - 1) * (2 - 1)
valor_critico = 9.49  # α=0.05, gl=4
print(f"\n=== RESULTADO ===")
print(f"χ² = {chi2:.2f}")
print(f"gl = {gl}")
print(f"Valor critico (α=0.05) = {valor_critico}")
print(f"→ {'RECHAZAMOS H0' if chi2 > valor_critico else 'NO RECHAZAMOS H0'}")

# Bondad de ajuste
print(f"\n=== PRUEBA DE BONDAD DE AJUSTE ===")
mejora_obs = 470
no_mejora_obs = 30
tasa_control = 0.48
mejora_esp = 500 * tasa_control
no_mejora_esp = 500 * (1 - tasa_control)
chi2_bondad = (mejora_obs - mejora_esp)**2 / mejora_esp + (no_mejora_obs - no_mejora_esp)**2 / no_mejora_esp
print(f"χ² bondad = {chi2_bondad:.2f}")
print(f"Valor critico (α=0.05, gl=1) = 3.84")
print(f"→ {'RECHAZAMOS H0 - datos NO siguen distribucion esperada' if chi2_bondad > 3.84 else 'NO RECHAZAMOS H0'}")
