"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 2 - Los Nudos del Quipu
Conceptos: Strings, métodos de string, slicing, formateo
Autor: Alex Goyzueta Delgado
"""

# ============================================
# CASO: El quipus de Inti - Decodificación
# ============================================

# El quipus tiene cuerdas de 5 colores
# Representaremos cada cuerda como un string
# donde 'n' = nudo y '-' = espacio vacío

cuerda_roja = "n--n---n----n"
cuerda_verde = "-n--n---n----n"
cuerda_azul = "n---n---n---n"
cuerda_amarilla = "--n----n----n-"
cuerda_blanca = "n-n-n-n-n-n-n"

print("=== QUIPUS FÍSICO: TRANSCRIPCIÓN ===")
print(f"Cuerda Roja:    {cuerda_roja}")
print(f"Cuerda Verde:   {cuerda_verde}")
print(f"Cuerda Azul:    {cuerda_azul}")
print(f"Cuerda Amarilla:{cuerda_amarilla}")
print(f"Cuerda Blanca:  {cuerda_blanca}")

# --- SLICING: Accediendo a posiciones ---

print("\n--- Analizando la cuerda roja ---")
print(f"Posición 0: '{cuerda_roja[0]}'")
print(f"Posición 1: '{cuerda_roja[1]}'")
print(f"Posición 2: '{cuerda_roja[2]}'")
print(f"Posición 3: '{cuerda_roja[3]}'")

primeros_4 = cuerda_roja[0:4]
print(f"\nPrimeros 4 caracteres: '{primeros_4}'")

ultimo = cuerda_roja[-1]
print(f"Último carácter: '{ultimo}'")

cada_2 = cuerda_roja[0:12:2]
print(f"Cada 2 posiciones: '{cada_2}'")

# --- MÉTODOS DE STRING ---

mensaje_encontrado = "  EL CODIGO ESTA EN EL QUIPU BLANCO  "

limpio = mensaje_encontrado.strip()
print(f"\nOriginal: '{mensaje_encontrado}'")
print(f"Sin espacios: '{limpio}'")

minusculas = limpio.lower()
print(f"En minúsculas: '{minusculas}'")

mayusculas = limpio.upper()
print(f"En mayúsculas: '{mayusculas}'")

reemplazado = limpio.replace("QUIPU", "CODIGO")
print(f"Reemplazado: '{reemplazado}'")

conteo_n = limpio.count("Q")
print(f"Veces que aparece 'Q': {conteo_n}")

posicion = limpio.find("BLANCO")
print(f"El texto 'BLANCO' empieza en posición: {posicion}")

longitud = len(limpio)
print(f"Longitud del mensaje: {longitud} caracteres")

# --- SISTEMA DE BIENVENIDA DEL LABORATORIO ---

visitante_1 = "policia"
visitante_2 = "Raúl"
visitante_3 = "Wayra"

saludo = "Bienvenido, {}. Te estaba esperando."

print(f"\n{saludo.format(visitante_1)}")
print(saludo.format(visitante_2))
print(saludo.format(visitante_3))

# --- ENIGMA 2.1: El mensaje oculto ---
print("\n--- Enigma 2.1 ---")
mensaje_codificado = "ÑAN*QHAPAQ*TAMBO*WAYRA*INTI"
print(f"Minúsculas: {mensaje_codificado.lower()}")
print(f"Reemplazado: {mensaje_codificado.replace('*', ' -> ')}")
print(f"Posición de WAYRA: {mensaje_codificado.find('WAYRA')}")
print(f"Veces que aparece A: {mensaje_codificado.count('A')}")
print(f"Longitud: {len(mensaje_codificado)}")

# --- ENIGMA 2.2: Extrayendo el nombre ---
print("\n--- Enigma 2.2 ---")
pos = mensaje_codificado.find("WAYRA")
print(f"Nombre extraído: '{mensaje_codificado[pos:pos+5]}'")

# --- ENIGMA 2.3: El quipu invertido ---
print("\n--- Enigma 2.3 ---")
quipu_invertido = "ATAM-ATAK-AP"
inverso = quipu_invertido[::-1]
print(f"Original: {quipu_invertido}")
print(f"Invertido: {inverso}")
