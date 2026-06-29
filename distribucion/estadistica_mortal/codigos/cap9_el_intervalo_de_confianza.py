"""
Capítulo 9: El Intervalo de Confianza
Intervalo de confianza, nivel de confianza, margen de error
"""
import numpy as np
import random
import math

# Muestra de edades
random.seed(42)
muestra_edades = [random.gauss(25, 5) for _ in range(50)]
edad_media = np.mean(muestra_edades)
desv_std = np.std(muestra_edades, ddof=1)
n = len(muestra_edades)

print("=== INTERVALO DE CONFIANZA ===")
print(f"n = {n}")
print(f"Media muestral = {edad_media:.2f}")
print(f"Desv. estandar = {desv_std:.2f}\n")

# IC 95%
valor_critico = 1.96
error_estandar = desv_std / math.sqrt(n)
margen_error = valor_critico * error_estandar
ic_inf = edad_media - margen_error
ic_sup = edad_media + margen_error

print(f"IC 95%: [{ic_inf:.2f}, {ic_sup:.2f}]")
print(f"Margen de error: ±{margen_error:.2f}\n")

# Efecto del tamaño de muestra
print("=== EFECTO DEL TAMAÑO DE MUESTRA ===")
print(f"{'n':<8} {'Error Estandar':<18} {'Margen Error':<15} {'IC'}")
for n_muestra in [10, 30, 50, 100, 500, 1000]:
    ee = desv_std / math.sqrt(n_muestra)
    me = 1.96 * ee
    print(f"{n_muestra:<8} {ee:<18.3f} ±{me:<13.2f} [{25-me:.1f}, {25+me:.1f}]")
