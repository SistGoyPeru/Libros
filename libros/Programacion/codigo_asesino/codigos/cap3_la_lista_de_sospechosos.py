"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 3 - La Lista de Sospechosos
Conceptos: Listas, tuplas, indexing, métodos de listas
Autor: Alex Goyzueta Delgado
"""

# ============================================
# LISTA DE SOSPECHOSOS
# ============================================

sospechosos = [
    "Lara Mamani",
    "Dr. Carlos Huamán",
    "Dra. Sarah Chen",
    "Rodrigo Mamani",
    "Mama Killa"
]

print("=== SOSPECHOSOS DEL CASO ===")
print(sospechosos)
print(f"Cantidad de sospechosos: {len(sospechosos)}")

# --- Accediendo a elementos ---
print(f"\nPrimer sospechoso: {sospechosos[0]}")
print(f"Último sospechoso: {sospechosos[-1]}")
print(f"Tres primeros: {sospechosos[0:3]}")
print(f"Dos últimos: {sospechosos[-2:]}")

# --- Listas de listas: fichas completas ---
fichas_sospechosos = [
    ["Lara Mamani", 32, "Asistente", True, 7],
    ["Dr. Carlos Huamán", 55, "Colega", True, 8],
    ["Dra. Sarah Chen", 40, "Colaboradora", True, 6],
    ["Rodrigo Mamani", 60, "Empresario", False, 9],
    ["Mama Killa", 70, "Hermana", True, 5]
]

print("\n=== FICHAS COMPLETAS ===")
for ficha in fichas_sospechosos:
    print(f"Nombre: {ficha[0]} | Edad: {ficha[1]} | Rol: {ficha[2]} | Acceso: {ficha[3]} | Sospecha: {ficha[4]}/10")

# --- TUPLAS: Datos inmutables ---
escena_crimen = (-13.5167, -71.9781)
print(f"\nCoordenadas del crimen: {escena_crimen}")
print(f"Latitud: {escena_crimen[0]}")
print(f"Longitud: {escena_crimen[1]}")

# Intentar modificar una tupla causa error
# escena_crimen[0] = 0.0  # ¡Descomentar para ver TypeError!

# --- MÉTODOS DE LISTAS ---
print("\n=== MANIPULANDO LA LISTA ===")
sospechosos.append("Oficial Paredes (policía)")
print(f"Agregamos al oficial: {sospechosos}")

sospechosos.remove("Oficial Paredes (policía)")
print(f"Quitamos al oficial: {sospechosos}")

sospechosos.sort()
print(f"Ordenados alfabéticamente: {sospechosos}")

sospechosos.reverse()
print(f"Orden inverso: {sospechosos}")

ultimo = sospechosos.pop()
print(f"Extraído: {ultimo}")
print(f"Lista actualizada: {sospechosos}")

posicion = sospechosos.index("Dra. Sarah Chen")
print(f"La Dra. Sarah Chen está en posición: {posicion}")

conteo = sospechosos.count("Lara Mamani")
print(f"Lara Mamani aparece {conteo} veces")

# --- EVIDENCIA RECOPILADA ---
evidencias_fisicas = [
    "Quipus digital en escritorio",
    "Taza de café frío",
    "Puerta sin cerradura forzada",
    "Código en pantalla OLED"
]

evidencias_digitales = [
    "Mensaje: quipu_digital_001 = 'Ñan:1:3:5:7:9'",
    "Sistema de bienvenida personalizado",
    "Archivos del Proyecto Yachay encriptados",
    "Registro de acceso de las últimas 24 horas"
]

testigos = [
    "Raúl (periodista, descubrió el cuerpo)",
    "Guardia de seguridad (no vio nada sospechoso)",
    "Vecino del laboratorio (escuchó discusión)"
]

print("\n=== EVIDENCIA DEL CASO ===")
print(f"\nEvidencias físicas ({len(evidencias_fisicas)}):")
for evidencia in evidencias_fisicas:
    print(f"  • {evidencia}")

print(f"\nEvidencias digitales ({len(evidencias_digitales)}):")
for evidencia in evidencias_digitales:
    print(f"  • {evidencia}")

print(f"\nTestigos ({len(testigos)}):")
for testigo in testigos:
    print(f"  • {testigo}")

# --- ENIGMA 3.1: Lista de coartadas ---
print("\n--- Enigma 3.1 ---")
coartadas = [
    "Lara: Estaba en mi departamento, viendo series.",
    "Carlos: Trabajaba en mi oficina de la universidad.",
    "Sarah: Tenía una videollamada con el MIT.",
    "Rodrigo: Estaba en una cena de negocios.",
    "Killa: Dormía. A mi edad, no salgo de noche.",
]
coartadas.append("Yo: Estaba trabajando en mi código.")
coartadas.sort()
print(f"Total de coartadas: {len(coartadas)}")
print(f"Primera: {coartadas[0]}")
print(f"Última: {coartadas[-1]}")

# --- ENIGMA 3.2: Matriz de acceso ---
print("\n--- Enigma 3.2 ---")
matriz_acceso = [
    ["Lara", True, True, True, True],
    ["Carlos", True, False, True, False],
    ["Sarah", True, True, False, False],
    ["Rodrigo", False, False, False, False],
    ["Killa", True, False, True, True],
]
print("Matriz de acceso:")
for fila in matriz_acceso:
    print(f"  {fila}")
print(f"\nQuiénes tienen acceso al Servidor: {[f[0] for f in matriz_acceso if f[2]]}")

# --- ENIGMA 3.3: Tuplas de coordenadas ---
print("\n--- Enigma 3.3 ---")
coordenadas_sagradas = [
    (-13.5167, -71.9781),
    (-13.1631, -72.5450),
    (-13.3333, -72.0833),
    (-13.3167, -72.1167),
]
coordenadas_sagradas.append((-13.5090, -71.9820))
for lat, lon in coordenadas_sagradas:
    print(f"  ({lat}, {lon})")
