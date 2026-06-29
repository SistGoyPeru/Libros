"""Capitulo 14: Revelacion en el Muelle
Conceptos: Repaso final - Poniendo todo junto
"""

# === REPASO FINAL: EL CODIGO DE LA VERDAD ===

mensajes_olas = {
    "15s": "ANCON",
    "18s": "PRIVATO",
    "20s": "COSTAZUL",
    "25s": "PLAN",
    "30s": "OLASDECODIFICADO"
}

print("=== DECODIFICACION COMPLETA ===")
for freq, msg in mensajes_olas.items():
    print(f"  Frecuencia {freq} -> {msg}")

mensaje = " ".join(mensajes_olas.values())
print(f"\nKey Mensaje completo: {mensaje}")

# La evidencia final
evidencias = [
    "Firmware del generador (modulo secreto)",
    "Registros de activacion (30 dias)",
    "Transferencias de Costa Azul S.A.",
    "Mensajes descifrados en 9 olas artificiales",
    "Testimonio del capitan del Don Eulogio",
]

print("\n=== EVIDENCIAS RECOPILADAS ===")
for i, ev in enumerate(evidencias, 1):
    print(f"  {i}. {ev}")

# Busqueda de complices
implicados = {
    "Soto (Costa Azul)": {
        "rol": "Financiamiento",
        "evidencias": 4,
        "nivel": "Alto"
    },
    "Parra (Ingeniero)": {
        "rol": "Construccion del generador",
        "evidencias": 3,
        "nivel": "Alto"
    },
    "Rivas (Biologa)": {
        "rol": "Informes ambientales falsos",
        "evidencias": 2,
        "nivel": "Medio"
    },
}

print("\n=== NIVEL DE IMPLICACION ===")
for nombre, datos in implicados.items():
    print(f"  {nombre}:")
    print(f"    Rol: {datos['rol']}")
    print(f"    Evidencias: {datos['evidencias']}")
    print(f"    Nivel: {datos['nivel']}")

# El USB de Don Eulogio
evidencia_final = {
    "firmware": "locuento_v2_original.bin",
    "planos": ["generador.dwg", "sistema_comunicacion.dwg"],
    "transferencias": [
        {"de": "Costa Azul S.A.", "a": "Parra Ingenieria", "monto": 150000},
        {"de": "Costa Azul S.A.", "a": "Soto Holding", "monto": 500000},
        {"de": "Soto Holding", "a": "Municipalidad de Ancon", "monto": 20000},
    ],
    "testigos": ["Eulogio Quispe", "Ana Maria Huerta", "Pedro Castillo"],
    "fecha_inicio": "2025-03-15",
}

print("\n=== EVIDENCIA FINAL (USB DON EULOGIO) ===")
for clave, valor in evidencia_final.items():
    print(f"  {clave}: {valor}")

# --- ENIGMAS ---

print("\n=== ENIGMA 14.1: Sistema de alertas ===")
def revisar_registros(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                if "sospechosa" in linea.lower():
                    print(f"! Alerta: {linea.strip()}")
    except FileNotFoundError:
        print("Archivo no encontrado")

revisar_registros("bitacora_puerto.txt")

print("\n=== ENIGMA 14.2: Base de datos de playas ===")
import json
playas_db = {
    "Ancon": {"protegida": True, "amenazada": False},
    "Miraflores": {"protegida": False, "amenazada": True},
}
with open("playas.json", "w", encoding="utf-8") as f:
    json.dump(playas_db, f, indent=2)
with open("playas.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
for nombre, info in datos.items():
    estado = "protegida" if info["protegida"] else "amenazada"
    print(f"  {nombre}: {estado}")

print("\n=== ENIGMA 14.3: Cifrado propio ===")
def cifrar_ola(texto):
    frecuencias = []
    for letra in texto.upper():
        if letra.isalpha():
            frecuencias.append(ord(letra) - 64)
    return frecuencias

def descifrar_ola(frecuencias):
    return ''.join(chr(f + 64) for f in frecuencias if 1 <= f <= 26)

mensaje_original = "OLA LIBRE"
cifrado = cifrar_ola(mensaje_original)
descifrado = descifrar_ola(cifrado)
print(f"Original: {mensaje_original}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")
