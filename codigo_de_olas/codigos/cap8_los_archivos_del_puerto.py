"""Capitulo 8: Los Archivos del Puerto
Conceptos: Manejo de archivos, open(), with, read/write
"""

import os

# ============================================
# LECTURA DE ARCHIVOS DEL PUERTO
# ============================================

# Crear un archivo de ejemplo con datos del puerto
datos_puerto = """BITACORA DEL PUERTO DE ANCON
FECHA: 27-06-2026

EMBARCACIONES REGISTRADAS:
- B/T "Mares del Sur" - Pesquero - 15:30
- Yate "Costa Azul" - Privado - 16:45
- Bote "Don Eulogio" - Pesquero artesanal - 05:00

ACTIVIDADES SOSPECHOSAS:
- 22:00 - Ruido submarino en sector norte
- 23:30 - Luces intermitentes en zona de boyas
- 01:00 - Embarcacion no identificada

NOTA: Se recomienda no investigar.
"""

with open("bitacora_puerto.txt", "w", encoding="utf-8") as f:
    f.write(datos_puerto)

# Leer el archivo completo
with open("bitacora_puerto.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

print("=== BITACORA DEL PUERTO ===")
print(contenido)

# Leyendo linea por linea
print("\n=== LEYENDO LINEA POR LINEA ===")
with open("bitacora_puerto.txt", "r", encoding="utf-8") as f:
    for num, linea in enumerate(f, 1):
        print(f"{num:3}: {linea.strip()}")

# --- PROCESANDO CSV DE EMBARCACIONES ---

csv_embarcaciones = """nombre,tipo,horario,dias_activo
Mares del Sur,Pesquero,15:30-23:00,30
Costa Azul,Yate privado,16:00-02:00,45
Don Eulogio,Pesquero artesanal,05:00-12:00,60
Lancha Rapida,No identificada,23:00-03:00,15
"""

with open("embarcaciones.csv", "w", encoding="utf-8") as f:
    f.write(csv_embarcaciones)

print("\n=== EMBARCACIONES SOSPECHOSAS ===\n")

with open("embarcaciones.csv", "r", encoding="utf-8") as f:
    encabezados = f.readline().strip().split(",")
    print(f"Columnas: {encabezados}\n")

    for linea in f:
        datos = linea.strip().split(",")
        nombre, tipo, horario, dias = datos
        print(f"  * {nombre:25} | {tipo:25} | {horario:15} | {dias} dias activo")

        # Detectar embarcaciones sospechosas
        if int(dias) < 20 and "no identificada" in tipo.lower():
            print(f"    ! !SOSPECHOSA! Poco tiempo activo y no identificada")

# Lectura con list comprehension
print("\n=== EMBARCACIONES NO IDENTIFICADAS ===")
with open("embarcaciones.csv", "r", encoding="utf-8") as f:
    next(f)  # Saltar encabezados
    no_id = [linea.strip().split(",") for linea in f if "no identificada" in linea.lower()]

for emb in no_id:
    print(f"  -> {emb[0]} - Horario: {emb[2]}")

# --- DIARIO DE INVESTIGACION ---

print("\n=== DOCUMENTANDO EL CASO ===\n")

with open("diario_mateo.txt", "w", encoding="utf-8") as d:
    d.write("== DIARIO DE INVESTIGACION ==\n")
    d.write("Caso: Proyecto LOCUENTO - Contaminacion de olas en Ancon\n")
    d.write("Investigador: Mateo Sanchez\n\n")
    d.write("--- DIA 1 ---\n")
    d.write("Encontre patrones anomalos en las olas de Ancon.\n")
    d.write("Descubri el generador submarino.\n")
    d.write("El firmware del generador tiene funciones en Python.\n")

# Verificar
with open("diario_mateo.txt", "r", encoding="utf-8") as d:
    print(d.read())

# Agregar mas datos
print("=== AGREGANDO EVIDENCIA ===\n")
with open("diario_mateo.txt", "a", encoding="utf-8") as d:
    d.write("\n--- DIA 2 ---\n")
    d.write("Identifique a los implicados.\n")
    d.write("El proyecto LOCUENTO es una fachada para privatizar Ancon.\n")
    d.write("El operador del generador sigue siendo desconocido.\n")

with open("diario_mateo.txt", "r", encoding="utf-8") as d:
    print(d.read())

# --- ARCHIVO DEL OPERADOR ---

with open("operador.log", "w", encoding="utf-8") as f:
    f.write("""OPERADOR: DESCONOCIDO
ULTIMO ACCESO: 27-06-2026 23:45
FIRMA DIGITAL: 4a8f2c1e9d3b7a0c5f6e

COMANDOS EJECUTADOS:
- generar_ola(2.4, 8, "LOCUENTO")
- transmitir_mensaje("MAR CONTAMINADO")
- generar_ola(1.8, 12, "SOS")
- transmitir_mensaje("AYUDA")
""")

print("=== ARCHIVO DEL OPERADOR ===\n")

with open("operador.log", "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    linea = linea.strip()
    print(f"  {linea}")

# Buscar comandos sospechosos
print("\n=== COMANDOS SOSPECHOSOS ===")
with open("operador.log", "r", encoding="utf-8") as f:
    for linea in f:
        if "transmitir_mensaje" in linea:
            print(f"  Antenna {linea.strip()}")

# --- ENIGMAS ---

print("\n=== ENIGMA 8.1: Crea tu bitacora ===")
with open("mi_diario_mar.txt", "w", encoding="utf-8") as f:
    f.write("Fecha: 27-06-2026\n")
    f.write("Hoy aprendi sobre archivos en Python.\n")
with open("mi_diario_mar.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("\n=== ENIGMA 8.2: Procesa el archivo de temperaturas ===")
with open("temperaturas_mar.txt", "w", encoding="utf-8") as f:
    f.write("18.2\n19.0\n17.5\n18.5\n19.1\n")
temp_total = 0
temp_count = 0
with open("temperaturas_mar.txt", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea:
            temp_total += float(linea)
            temp_count += 1
print(f"Promedio de temperaturas: {temp_total / temp_count:.2f}C")

print("\n=== ENIGMA 8.3: Agregando datos ===")
observacion = "Vi una ola extrana en el horizonte."
with open("observaciones_mar.txt", "a", encoding="utf-8") as f:
    f.write(observacion + "\n")
with open("observaciones_mar.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("\n=== ENIGMA 8.4: Buscador en archivos ===")
conteo_sospechosa = 0
with open("bitacora_puerto.txt", "r", encoding="utf-8") as f:
    for linea in f:
        conteo_sospechosa += linea.lower().count("sospechosa")
print(f"La palabra 'sospechosa' aparece {conteo_sospechosa} veces.")
