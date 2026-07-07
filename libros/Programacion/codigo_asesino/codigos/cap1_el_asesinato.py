"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 1 - El Asesinato en el Templo del Sol
Conceptos: Variables, tipos de datos, print(), f-strings
Autor: Alex Goyzueta Delgado
"""

# ============================================
# CASO: El asesinato del Dr. Inti Quispe
# Analista: Wayra Condori
# Fecha: 27 de junio, 2026
# ============================================

# --- DATOS BÁSICOS DEL CASO ---

nombre_victima = "Dr. Inti Quispe"
edad_victima = 67
lugar_crimen = "Templo del Sol (Coricancha)"
hora_descubrimiento = "06:30"
puerta_cerrada = True
tiene_herederos = False

print("=== INFORME INICIAL ===")
print("Víctima:", nombre_victima)
print("Edad:", edad_victima)
print("Lugar:", lugar_crimen)
print("Hora del descubrimiento:", hora_descubrimiento)
print("Puerta cerrada por dentro:", puerta_cerrada)

# --- F-STRINGS (forma elegante) ---

print(f"\nLa víctima es {nombre_victima}, de {edad_victima} años.")
print(f"El crimen ocurrió en {lugar_crimen} a las {hora_descubrimiento}.")

# --- EL PRIMER QUIPU DIGITAL ---

quipu_digital_001 = "Ñan:1:3:5:7:9"
print(f"\nMensaje original del quipu: {quipu_digital_001}")

# Separamos los elementos por los dos puntos
elementos = quipu_digital_001.split(":")
print(f"Elementos separados: {elementos}")

# El primer elemento es el tipo de quipu
tipo_quipu = elementos[0]
print(f"Tipo de camino: {tipo_quipu}")

# Los siguientes son las posiciones de los nudos
nudos = elementos[1:]
print(f"Posiciones de nudos: {nudos}")

# --- ENIGMA 1.2: El mensaje cifrado ---
quipu_digital_002 = "Yachay:2:4:6:8:10"
elementos2 = quipu_digital_002.split(":")
tipo2 = elementos2[0]
numeros2 = elementos2[1:]
print(f"\n--- Enigma 1.2 ---")
print(f"Tipo: {tipo2}")
print(f"Números: {numeros2}")

# --- ENIGMA 1.3: Mi propia teoría ---
mi_teoria = "Creo que el asesino conocía a Inti y tenía acceso al laboratorio"
print(f"\nMi teoría inicial: {mi_teoria}")
