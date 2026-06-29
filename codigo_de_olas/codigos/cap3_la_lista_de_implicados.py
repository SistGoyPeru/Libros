"""Capitulo 3: La Lista de Implicados
Conceptos: Listas, tuplas, indexing, metodos de listas
"""

# ============================================
# LISTA DE IMPLICADOS EN EL CASO
# ============================================

# Personas relacionadas al proyecto LOCUENTO
implicados = [
    "Carlos Parra (Ingeniero Naval)",
    "Dra. Luisa Rivas (Biologa Marina)",
    "Miguel Angel Soto (Empresario)",
    "Capitan Paredes (Capitan del Puerto)",
    "Rafa (testigo)"
]

print("=== IMPLICADOS EN EL CASO ===")
print(implicados)
print(f"Total de implicados: {len(implicados)}")

# Accediendo a elementos
print(f"\nPrimer implicado: {implicados[0]}")
print(f"Ultimo implicado: {implicados[-1]}")
print(f"Los 3 primeros: {implicados[:3]}")
print(f"Los 2 ultimos: {implicados[-2:]}")

# Listas de listas: Datos anidados
# [nombre, edad, rol, sabe_del_generador, nivel_confianza]
fichas_implicados = [
    ["Carlos Parra", 45, "Ingeniero Naval", True, 8],
    ["Luisa Rivas", 38, "Biologa Marina", False, 6],
    ["Miguel Angel Soto", 62, "Empresario", True, 9],
    ["Capitan Paredes", 55, "Capitan del Puerto", False, 4],
    ["Rafa", 29, "Amigo / Testigo", True, 10],
]

print("\n=== FICHAS COMPLETAS ===")
for ficha in fichas_implicados:
    print(f"Nombre: {ficha[0]:30} | Edad: {ficha[1]} | Confianza: {ficha[4]}/10")

# --- TUPLAS: DATOS INMUTABLES ---

# Coordenadas de Ancon (no cambian)
coordenadas_ancon = (-11.7758, -77.1897)
print(f"\nCoordenadas de Ancon: {coordenadas_ancon}")
print(f"Latitud: {coordenadas_ancon[0]}")
print(f"Longitud: {coordenadas_ancon[1]}")

# Puntos de monitoreo (tuplas fijas)
puntos_monitoreo = [
    (-11.7730, -77.1880),
    (-11.7760, -77.1900),
    (-11.7780, -77.1870),
    (-11.7740, -77.1850)
]

print(f"\nPuntos de monitoreo: {len(puntos_monitoreo)}")
for i, punto in enumerate(puntos_monitoreo, 1):
    print(f"  Punto {i}: ({punto[0]}, {punto[1]})")

# --- METODOS DE LISTAS ---
print("\n=== MANIPULANDO LA LISTA ===")

# .append() - Agregar
implicados.append("Desconocido (operador del generador)")
print(f"Agregado: {implicados}")

# .remove() - Eliminar
implicados.remove("Rafa (testigo)")
print(f"Sin Rafa (es amigo, no implicado): {implicados}")

# .sort() - Ordenar
implicados.sort()
print(f"Ordenados alfabeticamente: {implicados}")

# .reverse() - Invertir
implicados.reverse()
print(f"Orden inverso: {implicados}")

# .pop() - Extraer el ultimo
ultimo = implicados.pop()
print(f"Extraido: {ultimo}")

# .index() - Buscar posicion
if "Carlos Parra (Ingeniero Naval)" in implicados:
    pos = implicados.index("Carlos Parra (Ingeniero Naval)")
    print(f"Carlos Parra esta en posicion: {pos}")

# .count() - Contar
print(f"Total actual: {len(implicados)}")

# --- EVIDENCIAS ---

evidencias_tecnicas = [
    "Patron de olas anomalas cada 3 horas",
    "Coordenadas del generador submarino",
    "Mensaje cifrado: 'MAR CONTAMINADO'",
    "Nombre del proyecto: LOCUENTO",
    "Frecuencias convertidas a letras"
]

testigos = [
    "Rafa (vio el generador desde su bote)",
    "Pescadores locales (oyeron ruido submarino)",
    "Capitan Paredes (recibio quejas)"
]

sospechosos_directos = [
    "Miguel Angel Soto (financia el proyecto)",
    "Carlos Parra (diseno el generador)",
]

print("\n=== EVIDENCIA DEL CASO ===")
print(f"\nEvidencias tecnicas ({len(evidencias_tecnicas)}):")
for e in evidencias_tecnicas:
    print(f"  * {e}")

print(f"\nTestigos ({len(testigos)}):")
for t in testigos:
    print(f"  * {t}")

print(f"\nSospechosos directos ({len(sospechosos_directos)}):")
for s in sospechosos_directos:
    print(f"  * {s}")

# --- FRECUENCIAS DE OLAS ANOMALAS ---

frecuencias_anomalas = [12, 15, 9, 21, 5, 14, 20, 15]

print(f"\nFrecuencias anomalas: {frecuencias_anomalas}")
print(f"Promedio: {sum(frecuencias_anomalas) / len(frecuencias_anomalas):.1f}")
print(f"Maxima: {max(frecuencias_anomalas)}")
print(f"Minima: {min(frecuencias_anomalas)}")

# Patron en las frecuencias?
for i in range(len(frecuencias_anomalas) - 1):
    diferencia = frecuencias_anomalas[i+1] - frecuencias_anomalas[i]
    print(f"Diferencia entre {i+1} y {i+2}: {diferencia}")

# --- ENIGMAS ---

print("\n=== ENIGMA 3.1: Tu lista de playas ===")
playas_de_lima = ["Ancon", "Miraflores", "Barranco", "La Punta", "Costa Verde"]
playas_de_lima.append("Santa Maria")
playas_de_lima.sort()
print(f"Total playas: {len(playas_de_lima)}")
print(f"Primera: {playas_de_lima[0]}")
print(f"Ultima: {playas_de_lima[-1]}")
print(f"Lista completa: {playas_de_lima}")

print("\n=== ENIGMA 3.2: Matriz de accesos ===")
matriz_accesos = [
    ["Ancon", True, True, "Estacionamiento"],
    ["Miraflores", True, False, "Parque"],
    ["Barranco", True, True, "Escaleras"],
]
print("Playas con acceso para discapacitados:")
for fila in matriz_accesos:
    if fila[2]:
        print(f"  * {fila[0]}")

print("\n=== ENIGMA 3.3: Tuplas de coordenadas ===")
coordenadas_playas = [
    (-11.7758, -77.1897),
    (-12.1200, -77.0300),
    (-12.1500, -77.0200),
]
for lat, lon in coordenadas_playas:
    print(f"Playa en latitud {lat}, longitud {lon}")
