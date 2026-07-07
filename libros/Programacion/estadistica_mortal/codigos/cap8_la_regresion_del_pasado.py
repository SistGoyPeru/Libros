"""
Capítulo 8: La Regresión del Pasado
Regresión lineal, R², predicción, residuos
"""
import numpy as np
import random

# Datos de ventas (24 meses)
random.seed(42)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
              13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
Y = np.array([50, 52, 48, 55, 51, 53, 56, 54, 58, 55, 57, 60,
              62, 59, 63, 61, 65, 63, 68, 72, 75, 78, 82, 85])

n = len(X)

# Calcular regresión manualmente
media_x = np.mean(X)
media_y = np.mean(Y)

pendiente = sum((X[i] - media_x) * (Y[i] - media_y) for i in range(n)) / \
            sum((X[i] - media_x) ** 2 for i in range(n))
intercepto = media_y - pendiente * media_x

print(f"=== REGRESION LINEAL ===")
print(f"Ecuacion: Y = {pendiente:.2f} * X + ({intercepto:.2f})")
print(f"Interpretacion: las ventas aumentan {pendiente:.2f} unidades por mes")

# Predicciones y residuos
predicciones = pendiente * X + intercepto
residuos = Y - predicciones

print(f"\n=== ANALISIS DE RESIDUOS ===")
for i in range(n):
    if abs(residuos[i]) > 5:
        print(f"Mes {i+1}: Real={Y[i]:.0f}, Predicho={predicciones[i]:.1f}, Residuo={residuos[i]:.1f}")

# R²
var_residuos = np.var(residuos)
var_total = np.var(Y)
r_cuadrado = 1 - (var_residuos / var_total)
print(f"\nR² = {r_cuadrado:.3f}")
print(f"El {r_cuadrado*100:.1f}% de la variacion en ventas es explicada por el tiempo")

# Comparación de períodos
X_antes = X[:18]
Y_antes = Y[:18]
X_despues = X[18:]
Y_despues = Y[18:]

n_antes = len(X_antes)
mx = np.mean(X_antes)
my = np.mean(Y_antes)
pend_antes = sum((X_antes[i] - mx) * (Y_antes[i] - my) for i in range(n_antes)) / \
             sum((X_antes[i] - mx) ** 2 for i in range(n_antes))
int_antes = my - pend_antes * mx

print(f"\nPeriodo 1 (meses 1-18): Y = {pend_antes:.2f} * X + ({int_antes:.2f})")
print(f"Periodo 2 (meses 19-24): Y = ? (pendiente cambio)")
print("\nDiferencia de pendientes indica posible manipulacion")
