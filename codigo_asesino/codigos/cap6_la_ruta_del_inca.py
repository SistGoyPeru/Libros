"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 6 - La Ruta del Qhapaq Ñan
Conceptos: Bucles for/while, range(), enumerate(), break/continue
Autor: Alex Goyzueta Delgado
"""

import time

# ============================================
# RECORRIENDO EL QHAPAQ ÑAN DIGITAL
# ============================================

estaciones_qhapaq_ñan = [
    "Cusco",
    "Ollantaytambo",
    "Machu Picchu",
    "Vilcashuamán",
    "Huánuco Pampa",
    "Cajamarca",
    "Tomebamba",
    "Quito"
]

print("=== RECORRIENDO EL QHAPAQ ÑAN ===\n")
print("Ruta completa:")
for estacion in estaciones_qhapaq_ñan:
    print(f"  → {estacion}")

# --- range() ---
print("\n=== ESTACIONES CON NÚMERO DE RUTA ===")
for i in range(len(estaciones_qhapaq_ñan)):
    print(f"Estación {i+1}: {estaciones_qhapaq_ñan[i]} (posición {i})")

# --- enumerate() ---
print("\n=== ENUMERANDO LA RUTA ===")
for indice, estacion in enumerate(estaciones_qhapaq_ñan):
    print(f"  [{indice}] → {estacion}")

# --- CÓDIGO OCULTO EN LAS ESTACIONES ---
codigo_estaciones = {
    "Cusco": "def",
    "Ollantaytambo": " descifrar",
    "Machu Picchu": "_mensaje",
    "Vilcashuamán": "():",
    "Huánuco Pampa": "    quipu",
    "Cajamarca": " = '",
    "Tomebamba": "YACHAY",
    "Quito": "'"
}

print("\n=== RECONSTRUYENDO EL CÓDIGO ===")
codigo_completo = ""
for estacion in estaciones_qhapaq_ñan:
    parte = codigo_estaciones.get(estacion, "")
    codigo_completo += parte
    print(f"{estacion}: '{parte}'")

print(f"\n--- Código resultante ---")
print(codigo_completo)

# --- while ---
print("\n=== EXPLORANDO EL PASAJE SECRETO ===")
pasos = 0
luz_encontrada = False

while not luz_encontrada:
    pasos += 1
    print(f"Paso {pasos}: Avanzando en la oscuridad...")
    if pasos >= 15:
        luz_encontrada = True
        print(f"¡Luz encontrada después de {pasos} pasos!")
    time.sleep(0.1)

print("Hemos llegado al interior del laboratorio.\n")

# --- break ---
print("=== BUSCANDO EL ARCHIVO YACHAY ===")
archivos_del_lab = [
    "informe_quipus.docx",
    "proyecto_yachay.py",
    "datos_experimentales.csv",
    "mensaje_cifrado.txt",
    "yachay_core.py",
    "notas_personales.md"
]

print("Buscando 'yachay_core.py' en los archivos...\n")
for archivo in archivos_del_lab:
    print(f"  Revisando: {archivo}")
    if "yachay" in archivo.lower():
        print(f"  → ¡ENCONTRADO! Archivo clave: {archivo}")
        break

# --- continue ---
print("\n=== FILTRANDO ARCHIVOS RELEVANTES ===")
for archivo in archivos_del_lab:
    if archivo.endswith(".csv") or archivo.endswith(".md"):
        continue
    print(f"  Archivo relevante: {archivo}")

# --- ANALIZANDO MOVIMIENTOS CON BUCLES ---
registro_accesos = [
    {"nombre": "Lara", "hora": "08:15", "accion": "entrada"},
    {"nombre": "Inti", "hora": "08:30", "accion": "entrada"},
    {"nombre": "Carlos", "hora": "09:00", "accion": "entrada"},
    {"nombre": "Lara", "hora": "12:30", "accion": "salida"},
    {"nombre": "Lara", "hora": "13:30", "accion": "entrada"},
    {"nombre": "Carlos", "hora": "14:00", "accion": "salida"},
    {"nombre": "Sarah", "hora": "14:30", "accion": "entrada"},
    {"nombre": "Sarah", "hora": "16:00", "accion": "salida"},
    {"nombre": "Inti", "hora": "18:00", "accion": "salida"},
    {"nombre": "Inti", "hora": "22:00", "accion": "entrada"},
    {"nombre": "Lara", "hora": "02:34", "accion": "entrada"},
    {"nombre": "Lara", "hora": "02:45", "accion": "salida"},
]

print("\n=== LÍNEA DE TIEMPO DEL CASO ===")
nombre_anterior = ""
for registro in registro_accesos:
    if nombre_anterior and nombre_anterior != registro["nombre"]:
        print()
    print(f"  {registro['hora']} | {registro['nombre']:7} | {registro['accion']}")
    nombre_anterior = registro["nombre"]

# --- ¿QUIÉNES ESTABAN A LAS 2:34 AM? ---
print("\n=== ¿QUIÉNES ESTABAN A LAS 2:34 AM? ===")
hora_crimen = "02:34"
presentes = []
for registro in registro_accesos:
    if registro["hora"] <= hora_crimen and registro["accion"] == "entrada":
        if registro["nombre"] not in presentes:
            presentes.append(registro["nombre"])
    if registro["hora"] > hora_crimen and registro["accion"] == "salida":
        if registro["nombre"] in presentes:
            presentes.remove(registro["nombre"])

print(f"A la hora del crimen ({hora_crimen}), estaban presentes:")
for p in presentes:
    print(f"  • {p}")

# --- ENIGMA 6.4: Range piramidal ---
print("\n--- Enigma 6.4: Pirámide de números ---")
num = 1
for fila in range(1, 5):
    for col in range(fila):
        print(num, end=" ")
        num += 1
    print()
