"""
Capítulo 7: La Correlación del Secreto
Correlación de Pearson, correlación vs causalidad
"""
import numpy as np
import random

# Ejemplos de correlación
horas_estudio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas_examen = [2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 9.0, 10.0]
r_positivo = np.corrcoef(horas_estudio, notas_examen)[0, 1]
print(f"Correlacion (horas estudio vs nota): {r_positivo:.3f}")

edad_auto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
precio_auto = [30000, 27000, 24000, 21000, 18000, 15000, 12000, 9000, 6000, 3000]
r_negativo = np.corrcoef(edad_auto, precio_auto)[0, 1]
print(f"Correlacion (edad auto vs precio): {r_negativo:.3f}")

random.seed(42)
x_aleatorio = [random.gauss(0, 1) for _ in range(50)]
y_aleatorio = [random.gauss(0, 1) for _ in range(50)]
r_cero = np.corrcoef(x_aleatorio, y_aleatorio)[0, 1]
print(f"Correlacion (datos aleatorios): {r_cero:.3f}")

# Correlaciones falsas
ventas_helados = [10, 12, 15, 25, 40, 55, 60, 58, 45, 30, 18, 12]
ahogados_playa = [2, 3, 4, 8, 15, 22, 25, 24, 16, 9, 5, 3]
r_falsa = np.corrcoef(ventas_helados, ahogados_playa)[0, 1]
print(f"\nCorrelacion falsa (helados vs ahogados): {r_falsa:.3f}")
print("¡Los helados NO causan ahogados!")
print("Variable oculta: el calor (verano → mas helados + mas playa)")

# Matriz de correlación del caso
import pandas as pd
datos_caso = pd.DataFrame({
    'sospechoso': ['Ramiro', 'Hugo', 'Sofia', 'Proveedor', 'Consultor'],
    'acceso_fisico': [1, 1, 1, 0, 1],
    'acceso_datos': [0.7, 0.9, 0.8, 0.1, 1.0],
    'motivo': [0.5, 0.3, 0.2, 0.8, 0.6],
    'coartada': [0.1, 0.7, 0.5, 0.3, 0.4],
    'ip_nocturna': [0, 1, 0.2, 0, 0.3],
    'manipulacion': [0.3, 0.7, 0.8, 0.2, 0.6]
})

matriz_corr = datos_caso.select_dtypes(include=[np.number]).corr()
print(f"\n=== MATRIZ DE CORRELACION ===")
print(matriz_corr.round(3))
print(f"\nCorrelacion manipulación - IP nocturna: {matriz_corr.loc['manipulacion', 'ip_nocturna']:.3f}")
