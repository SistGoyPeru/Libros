"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 8 - Los Archivos del Laboratorio
Conceptos: Manejo de archivos, open(), with, read/write, rutas
Autor: Alex Goyzueta Delgado
"""

import os

# ============================================
# SISTEMA DE LECTURA DE ARCHIVOS
# ============================================

# --- CREAR Y LEER UN ARCHIVO ---
evidencias_texto = """=== EVIDENCIAS DEL CASO INTI QUISPE ===

1. Quipus digital modificado el 27/06/2026 a las 02:34
2. Registro de acceso con cuenta de Lara Mamani
3. Mensaje en pantalla OLED: "Bienvenido, Wayra"
4. Pasaje secreto del Qhapaq Ñan restaurado
5. Código fuente de Yachay modificado

NOTA: El quipus blanco contiene la clave.
"""

with open("evidencias_caso.txt", "w", encoding="utf-8") as archivo:
    archivo.write(evidencias_texto)

with open("evidencias_caso.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print("=== CONTENIDO DEL ARCHIVO ===")
print(contenido)

# --- LEYENDO LÍNEA POR LÍNEA ---
print("\n=== LEYENDO LÍNEA POR LÍNEA ===")
with open("evidencias_caso.txt", "r", encoding="utf-8") as archivo:
    for numero_linea, linea in enumerate(archivo, 1):
        print(f"Línea {numero_linea}: {linea.strip()}")

# --- PROCESANDO CSV ---
csv_content = """nombre,edad,rol,acceso,motivo
Lara Mamani,32,Asistente,True,7
Carlos Huamán,55,Colega,True,8
Sarah Chen,40,Colaboradora,True,6
Rodrigo Mamani,60,Empresario,False,9
Mama Killa,70,Hermana,True,5
"""

with open("sospechosos.csv", "w", encoding="utf-8") as f:
    f.write(csv_content)

print("\n=== DATOS DE SOSPECHOSOS (CSV) ===")
with open("sospechosos.csv", "r", encoding="utf-8") as f:
    encabezados = f.readline().strip().split(",")
    print(f"Columnas: {encabezados}\n")
    for linea in f:
        datos = linea.strip().split(",")
        nombre, edad, rol, acceso, motivo = datos
        print(f"  • {nombre:25} | Edad: {edad:3} | {rol:20} | Acceso: {acceso:5} | Motivo: {motivo}")

# --- ESCRITURA DE ARCHIVO ---
print("\n=== DOCUMENTANDO EL CASO ===")
with open("diario_wayra.txt", "w", encoding="utf-8") as diario:
    diario.write("== DIARIO DE INVESTIGACIÓN ==\n")
    diario.write("Caso: Asesinato del Dr. Inti Quispe\n")
    diario.write("Investigadora: Wayra Condori\n\n")
    diario.write("--- DÍA 1 ---\n")
    diario.write("Descubrí el cuerpo a través de Raúl.\n")
    diario.write("Encontré un quipus digital con mensaje cifrado.\n")
    diario.write("El sistema de bienvenida sabía que yo llegaría.\n")

with open("diario_wayra.txt", "r", encoding="utf-8") as diario:
    print(diario.read())

# --- APPEND: AGREGANDO DATOS ---
print("=== AGREGANDO NUEVA EVIDENCIA ===")
with open("diario_wayra.txt", "a", encoding="utf-8") as diario:
    diario.write("\n--- NUEVA EVIDENCIA ---\n")
    diario.write("Encontré un pasaje secreto del Qhapaq Ñan.\n")
    diario.write("El quipus blanco contiene coordenadas.\n")
    diario.write("Alguien está usando Yachay en este momento.\n")

with open("diario_wayra.txt", "r", encoding="utf-8") as diario:
    print(diario.read())

# --- ARCHIVO CIFRADO ---
with open("quipu_legado.txt", "w", encoding="utf-8") as f:
    f.write("""qUiPu DiGiTaL v2.0
ÑaN:1:3:5:7:9:11:13
YaChAy:2:4:6:8:10:12:14
CoRiCaNcHa:1:4:9:16:25
PaChAcUtEc:3:6:12:24:48""")

print("\n=== QUIPU LEGADO: ARCHIVO ENCONTRADO ===")
with open("quipu_legado.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
print(f"Total de líneas: {len(lineas)}\n")
for linea in lineas:
    linea = linea.strip()
    if ":" in linea:
        partes = linea.split(":")
        nombre = partes[0]
        numeros = [int(x) for x in partes[1:]]
        print(f"  • {nombre}: {numeros}")
        if nombre.isupper():
            print(f"    → TODO MAYÚSCULAS: Palabra clave")
        if len(numeros) >= 3:
            diferencias = [numeros[i+1] - numeros[i] for i in range(len(numeros)-1)]
            if len(set(diferencias)) == 1:
                print(f"    → Progresión aritmética (diferencia: {diferencias[0]})")

# --- METADATOS DE ARCHIVOS ---
print("\n=== METADATOS DE ARCHIVOS ===")
if os.path.exists("quipu_legado.txt"):
    tamano = os.path.getsize("quipu_legado.txt")
    print(f"Archivo: quipu_legado.txt")
    print(f"Tamaño: {tamano} bytes")
    print(f"Existe: {os.path.exists('quipu_legado.txt')}")
    print(f"Es archivo: {os.path.isfile('quipu_legado.txt')}")

archivos_txt = [f for f in os.listdir('.') if f.endswith('.txt')]
print("\nArchivos de texto encontrados:")
for archivo in archivos_txt:
    tamano = os.path.getsize(archivo)
    print(f"  • {archivo:30} ({tamano} bytes)")

# --- ARCHIVO OCULTO ---
with open(".quipu_maestro.txt", "w", encoding="utf-8") as f:
    f.write("""ERES LA HEREDERA DEL CONOCIMIENTO.
BUSCA EN LOS NUDOS DEL QUIPU BLANCO.
LA RESPUESTA ESTÁ EN EL CÓDIGO FUENTE DE YACHAY.
NO CONFÍES EN LARA. NO CONFÍES EN CARLOS.
MAMA KILLA SABE LA VERDAD PERO NO LA DIRÁ.
EL ASESINO ESTÁ MÁS CERCA DE LO QUE CREES.

-- INTI""")

with open(".quipu_maestro.txt", "r", encoding="utf-8") as f:
    mensaje_oculto = f.read()
print("\n=== MENSAJE OCULTO ENCONTRADO ===")
print(mensaje_oculto)
