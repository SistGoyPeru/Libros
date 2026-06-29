"""Capitulo 2: El Lenguaje del Mar
Conceptos: Strings, metodos de string, slicing
"""

# ============================================
# MENSAJES DEL MAR
# ============================================

# Patrones de espuma observados en la orilla
# Cada caracter representa la forma de la espuma:
# '-' = linea recta, '/' = diagonal, 'O' = circulo

patron_1 = "--//O--//O--//O"
patron_2 = "O--O--O--O--O--"
patron_3 = "-/O-/-/O-/-/O--"

print("=== PATRONES DE ESPUMA ===")
print(f"Patron 1: {patron_1}")
print(f"Patron 2: {patron_2}")
print(f"Patron 3: {patron_3}")

# Accediendo a posiciones especificas
print(f"\n--- Analizando Patron 1 ---")
print(f"Primer caracter: '{patron_1[0]}'")
print(f"Tercer caracter: '{patron_1[2]}'")
print(f"Ultimo caracter: '{patron_1[-1]}'")
print(f"Primeros 3: '{patron_1[0:3]}'")
print(f"Ultimos 4: '{patron_1[-4:]}'")

# Slicing: [inicio:fin:paso]
print(f"\n--- Slicing de patrones ---")

# Primeros 6 caracteres
primeras_6 = patron_1[:6]
print(f"Primeras 6 posiciones: '{primeras_6}'")

# Cada 2 caracteres (saltando uno)
cada_dos = patron_1[::2]
print(f"Cada 2 posiciones: '{cada_dos}'")

# Invertir el patron
inverso = patron_1[::-1]
print(f"Patron invertido: '{inverso}'")

# --- METODOS DE STRING ---

mensaje_del_mar = "  EL CODIGO ESTA EN LA FRECUENCIA  "

# strip() - elimina espacios
limpio = mensaje_del_mar.strip()
print(f"\nOriginal: '{mensaje_del_mar}'")
print(f"Limpio: '{limpio}'")

# lower() / upper()
print(f"Minusculas: '{limpio.lower()}'")
print(f"Mayusculas: '{limpio.upper()}'")

# replace() - reemplazar texto
reemplazado = limpio.replace("FRECUENCIA", "ALTURA")
print(f"Reemplazado: '{reemplazado}'")

# find() - encontrar posicion
pos = limpio.find("FRECUENCIA")
print(f"'FRECUENCIA' esta en posicion: {pos}")

# count() - contar ocurrencias
conteo_e = limpio.count("E")
print(f"Veces que aparece 'E': {conteo_e}")

# len() - longitud
print(f"Longitud del mensaje: {len(limpio)}")

# --- DESCIFRANDO EL MENSAJE ---

ola_1 = "M-A-R"
ola_2 = "C-O-N"
ola_3 = "T-A-M"
ola_4 = "I-N-A"
ola_5 = "D-O--"

# Unir las olas para formar el mensaje
mensaje_completo = ola_1 + ola_2 + ola_3 + ola_4 + ola_5
print(f"\nMensaje completo: {mensaje_completo}")

# Limpiar el mensaje (quitar guiones)
mensaje_limpio = mensaje_completo.replace("-", "")
print(f"Mensaje limpio: {mensaje_limpio}")

# Convertir a minusculas
print(f"En minusculas: {mensaje_limpio.lower()}")

# Verificar si contiene palabras clave
if "CONTAMINACION" in mensaje_limpio.upper():
    print("!El mensaje habla de contaminacion!")
if "MAR" in mensaje_limpio.upper():
    print("!El mensaje menciona el mar!")

# --- COORDENADA DEL GENERADOR ---

coordenada = "11*46'30.7''S 77*11'22.3''W"
print(f"\nCoordenada del generador: {coordenada}")

# Extraer latitud y longitud
latitud = coordenada[:15]
longitud = coordenada[16:]
print(f"Latitud: {latitud}")
print(f"Longitud: {longitud}")

# El nombre del proyecto estaba codificado en la frecuencia
frecuencias = "12-15-09-21-05-14-20-15"
letras = frecuencias.split("-")
nombre_proyecto = ""
for num in letras:
    letra = chr(int(num) + 64)  # A=1, B=2, etc.
    nombre_proyecto += letra
    print(f"{num} -> '{letra}'")

print(f"\nNombre del proyecto: {nombre_proyecto}")

# --- ENIGMAS ---

print("\n=== ENIGMA 2.1: Descifra la frecuencia ===")
frecuencia_cifrada = "03-15-12-01-19"
nums = frecuencia_cifrada.split("-")
palabra = ""
for n in nums:
    palabra += chr(int(n) + 64)
print(f"Frecuencia: {frecuencia_cifrada} -> {palabra}")

print("\n=== ENIGMA 2.2: Extrae el nombre del barco ===")
barco = "B/T-MARES-DE-ANCON-2026"
inicio = barco.find("ANCON")
fin = inicio + 5
extraido = barco[inicio:fin]
print(f"Barco: {barco}")
print(f"Extraido: {extraido}")

print("\n=== ENIGMA 2.3: Invertir el mensaje ===")
mensaje_arena = "ODATNEMIRP SE ODAGUA"
invertido = mensaje_arena[::-1]
print(f"Mensaje: {mensaje_arena}")
print(f"Invertido: {invertido}")

print("\n=== ENIGMA 2.4: Limpieza de datos ===")
sensor_datos = "  OLA: 2.4m - FREC: 12s  "
limpio_s = sensor_datos.strip()
partes_s = limpio_s.replace("-", ",").split(",")
print(f"Datos originales: '{sensor_datos}'")
for p in partes_s:
    print(f"  -> {p.strip()}")
