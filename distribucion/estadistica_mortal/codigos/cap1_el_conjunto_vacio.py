"""
Capítulo 1: El Conjunto Vacío
Estadística descriptiva: media, mediana, moda, min, max
"""
import csv
from collections import Counter

# Cargar datos del archivo CSV
datos_caso = []
with open('datos_caso.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    encabezados = next(lector)
    for fila in lector:
        datos_caso.append(fila)

print(f"Archivo cargado: {len(datos_caso)} registros encontrados")
print(f"Columnas: {encabezados}")

# Extraer edades
edades = []
for fila in datos_caso:
    if fila[2]:
        edades.append(int(fila[2]))

print(f"\n=== RESUMEN DE EDADES ===")
print(f"Cantidad total (n):    {len(edades)}")
print(f"Edad minima (min):     {min(edades)}")
print(f"Edad maxima (max):     {max(edades)}")

# Media
media = sum(edades) / len(edades)
print(f"Edad media (promedio): {media:.2f} anos")

# Mediana
edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)
if n % 2 == 0:
    mediana = (edades_ordenadas[n//2 - 1] + edades_ordenadas[n//2]) / 2
else:
    mediana = edades_ordenadas[n//2]
print(f"Edad mediana (central): {mediana:.2f} anos")

# Moda
conteo_edades = Counter(edades)
edad_moda, frecuencia_moda = conteo_edades.most_common(1)[0]
print(f"Edad moda (frecuente):  {edad_moda} anos ({frecuencia_moda} veces)")

# Datos faltantes
total_filas = len(datos_caso)
for i, encabezado in enumerate(encabezados):
    faltan = sum(1 for fila in datos_caso if not fila[i].strip())
    if faltan > 0:
        porcentaje = (faltan / total_filas) * 100
        print(f"Columna '{encabezado}': {faltan} valores faltantes ({porcentaje:.1f}%)")
