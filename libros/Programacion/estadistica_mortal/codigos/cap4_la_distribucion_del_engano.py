"""
Capítulo 4: La Distribución del Engaño
Distribución normal, Z-score, regla empírica
"""
import numpy as np
import random

# Cargar datos originales
random.seed(42)
datos_originales = np.random.normal(71.23, 2.11, 10000)

media = np.mean(datos_originales)
mediana = np.median(datos_originales)
desv_std = np.std(datos_originales)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviacion estandar: {desv_std:.2f}")

# Regla empírica
dentro_1sigma = np.sum(np.abs(datos_originales - media) <= desv_std)
dentro_2sigma = np.sum(np.abs(datos_originales - media) <= 2 * desv_std)
dentro_3sigma = np.sum(np.abs(datos_originales - media) <= 3 * desv_std)
total = len(datos_originales)

print(f"\n=== REGLA EMPIRICA ===")
print(f"68% teorico: 6800")
print(f"Dentro de 1σ: {dentro_1sigma} ({100*dentro_1sigma/total:.1f}%)")
print(f"95% teorico: 9500")
print(f"Dentro de 2σ: {dentro_2sigma} ({100*dentro_2sigma/total:.1f}%)")
print(f"99.7% teorico: 9970")
print(f"Dentro de 3σ: {dentro_3sigma} ({100*dentro_3sigma/total:.1f}%)")

# Z-score
def z_score(valor, media, desv_std):
    return (valor - media) / desv_std

z_scores = np.abs((datos_originales - media) / desv_std)
indices_extremos = np.argsort(z_scores)[-5:]

print(f"\n=== VALORES EXTREMOS (Z-score) ===")
for i in indices_extremos:
    z = z_score(datos_originales[i], media, desv_std)
    print(f"  Valor: {datos_originales[i]:.2f}, Z-score: {z:.2f}")

# Tasa observada extrema
media_sim = 0.71
std_sim = 0.02
tasa_obs = 0.94
z_tasa = (tasa_obs - media_sim) / std_sim
print(f"\nZ-score de tasa observada (94%): {z_tasa:.2f}")
print(f"Esto es {z_tasa:.0f} desviaciones estandar sobre la media")
