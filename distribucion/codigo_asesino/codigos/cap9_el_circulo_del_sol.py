"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 9 - El Círculo del Sol
Conceptos: Manejo de errores, try/except/finally, excepciones personalizadas
Autor: Alex Goyzueta Delgado
"""

# ============================================
# SISTEMA DE ANÁLISIS TOLERANTE A FALLOS
# ============================================

def analizar_quipu_seguro(quipu_data):
    """Analiza un quipu de forma segura, manejando errores."""
    try:
        nombre = quipu_data["nombre"]
        cuerdas = quipu_data["cuerdas"]
        nudos_totales = sum(len(c["nudos"]) for c in cuerdas)
        print(f"  ✓ Quipu '{nombre}' analizado: {nudos_totales} nudos en {len(cuerdas)} cuerdas")
        return nudos_totales
    except KeyError as e:
        print(f"  ✗ Error: Falta la clave {e} en el quipu")
        return 0
    except TypeError as e:
        print(f"  ✗ Error de tipo: {e}")
        return 0
    except Exception as e:
        print(f"  ✗ Error inesperado: {e}")
        return 0

quipu_valido = {
    "nombre": "Quipu ceremonial",
    "cuerdas": [
        {"color": "rojo", "nudos": [1, 4, 9]},
        {"color": "blanco", "nudos": [1, 3, 5, 7, 9]}
    ]
}
quipu_sin_nombre = {"cuerdas": [{"color": "rojo", "nudos": [1, 2, 3]}]}
quipu_sin_cuerdas = {"nombre": "Quipu vacío"}
quipu_invalido = "Esto no es un quipu"

print("=== SISTEMA DE ANÁLISIS TOLERANTE A FALLOS ===\n")
analizar_quipu_seguro(quipu_valido)
analizar_quipu_seguro(quipu_sin_nombre)
analizar_quipu_seguro(quipu_sin_cuerdas)
analizar_quipu_seguro(quipu_invalido)

# --- PROCESANDO ARCHIVOS DEL LABORATORIO ---
print("\n=== PROCESANDO ARCHIVOS DEL LABORATORIO ===")

def procesar_archivo_cifrado(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        try:
            numero = int(contenido.strip())
            print(f"  ✓ Archivo numérico: {numero}")
        except ValueError:
            if ":" in contenido:
                partes = contenido.split(":")
                print(f"  ✓ Formato quipu: {partes[0]} → {partes[1:]}")
            else:
                print(f"  ✓ Texto plano: {contenido[:50]}...")
    except FileNotFoundError:
        print(f"  ✗ Archivo no encontrado: {ruta_archivo}")
    except Exception as e:
        print(f"  ✗ Error: {e}")

archivos_prueba = {
    "quipu_rojo.txt": "ROJO:1:4:9",
    "quipu_blanco.txt": "BLANCO:1:3:5:7:9",
    "numero_secreto.txt": "42",
    "nota_inti.txt": "Mama Killa sabe la verdad sobre el quipu",
}
for nombre, contenido in archivos_prueba.items():
    with open(nombre, "w", encoding="utf-8") as f:
        f.write(contenido)

for archivo in list(archivos_prueba.keys()) + ["archivo_inexistente.txt"]:
    procesar_archivo_cifrado(archivo)

# --- ELSE Y FINALLY ---
print("\n=== PROCESO FORENSE CON GARANTÍAS ===")

def proceso_forense_seguro(archivo_evidencia):
    print(f"Iniciando análisis de: {archivo_evidencia}")
    try:
        with open(archivo_evidencia, "r", encoding="utf-8") as f:
            datos = f.read()
        if not datos.strip():
            raise ValueError("El archivo de evidencia está vacío")
        resultado = len(datos)
    except FileNotFoundError:
        print(f"  ERROR: Evidencia no encontrada")
        resultado = -1
    except ValueError as e:
        print(f"  ERROR: {e}")
        resultado = -1
    else:
        print(f"  ✓ Evidencia procesada: {resultado} bytes")
    finally:
        print(f"  → Registro: Análisis de {archivo_evidencia} completado\n")
    return resultado

proceso_forense_seguro("quipu_rojo.txt")
proceso_forense_seguro("archivo_inexistente.txt")
with open("evidencia_vacia.txt", "w") as f:
    f.write("")
proceso_forense_seguro("evidencia_vacia.txt")

# --- EXCEPCIONES PERSONALIZADAS ---
print("=== EXCEPCIONES PERSONALIZADAS ===")

class QuipuCorruptoError(Exception):
    pass

class EvidenciaInconsistenteError(Exception):
    def __init__(self, evidencia1, evidencia2, mensaje="Contradicción entre evidencias"):
        self.evidencia1 = evidencia1
        self.evidencia2 = evidencia2
        super().__init__(f"{mensaje}: {evidencia1} vs {evidencia2}")

def verificar_quipu(quipu):
    if not isinstance(quipu, dict):
        raise QuipuCorruptoError("El quipu debe ser un diccionario")
    if "cuerdas" not in quipu:
        raise QuipuCorruptoError("El quipu no tiene cuerdas")
    if len(quipu["cuerdas"]) == 0:
        raise QuipuCorruptoError("El quipu está vacío")
    return True

try:
    verificar_quipu("no_soy_un_quipu")
except QuipuCorruptoError as e:
    print(f"  ✗ Quipu corrupto: {e}")

try:
    verificar_quipu({"cuerdas": [{"color": "rojo", "nudos": [1, 2, 3]}]})
    print("  ✓ Quipu válido")
except QuipuCorruptoError as e:
    print(f"  ✗ {e}")

evidencia_a = {"id": "Cámara 1", "hora": "02:30", "contenido": "Vio a alguien salir"}
evidencia_b = {"id": "Cámara 2", "hora": "02:35", "contenido": "No vio a nadie"}
try:
    if evidencia_a["hora"] != evidencia_b["hora"]:
        raise EvidenciaInconsistenteError(evidencia_a["id"], evidencia_b["id"],
                                          f"Horas diferentes: {evidencia_a['hora']} vs {evidencia_b['hora']}")
except EvidenciaInconsistenteError as e:
    print(f"  ✗ {e}")
