"""Capitulo 9: El Error en la Red
Conceptos: Manejo de errores, try/except/finally, excepciones personalizadas
"""

# ============================================
# SISTEMA TOLERANTE A ERRORES
# ============================================

def conectar_generador(ip):
    """Intenta conectar con el generador submarino."""
    try:
        print(f"  Conectando a {ip}...")
        # Simular conexion fallida
        if "192.168" in ip:
            raise ConnectionError("Red local no disponible")
        elif "10.0" in ip:
            raise TimeoutError("Tiempo de espera agotado")
        else:
            print("  OK Conexion exitosa")
            return True
    except ConnectionError as e:
        print(f"  X Error de conexion: {e}")
        return False
    except TimeoutError as e:
        print(f"  X Timeout: {e}")
        return False
    except Exception as e:
        print(f"  X Error inesperado: {e}")
        return False

conectar_generador("192.168.1.100")
conectar_generador("10.0.0.5")
conectar_generador("172.16.0.1")

def leer_configuracion_generador(ruta_archivo):
    """Lee la configuracion del generador desde un archivo."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            config = f.read()

        try:
            niveles = [int(x) for x in config.split(",")]
            print(f"  OK Configuracion cargada: {niveles}")
            return niveles
        except ValueError:
            print(f"  X Formato invalido: '{config.strip()}' no es numerico")
            return []

    except FileNotFoundError:
        print(f"  X Archivo no encontrado: {ruta_archivo}")
        return []
    except PermissionError:
        print(f"  X Sin permisos para leer: {ruta_archivo}")
        return []

print("\n=== LEYENDO CONFIGURACION ===\n")

# Crear archivos de prueba
with open("config_valida.txt", "w", encoding="utf-8") as f:
    f.write("12,15,9,21,5,14,20,15")
with open("config_invalida.txt", "w", encoding="utf-8") as f:
    f.write("doce,quince,nueve")

leer_configuracion_generador("config_valida.txt")
leer_configuracion_generador("config_invalida.txt")
leer_configuracion_generador("no_existe.txt")

# Else y Finally
print("\n=== PROCESO CON GARANTIAS ===\n")

def procesar_mensaje_ola(archivo_mensaje):
    """Procesa un mensaje codificado en olas."""
    print(f"Iniciando procesamiento de: {archivo_mensaje}")

    try:
        with open(archivo_mensaje, "r", encoding="utf-8") as f:
            datos = f.read()

        if not datos.strip():
            raise ValueError("Mensaje vacio")

        resultado = len(datos)

    except FileNotFoundError:
        print(f"  ERROR: Mensaje no encontrado")
        resultado = -1
    except ValueError as e:
        print(f"  ERROR: {e}")
        resultado = -1
    else:
        print(f"  OK Mensaje procesado: {resultado} caracteres")
        if "SOS" in datos or "AYUDA" in datos:
            print(f"  ! !MENSAJE DE AUXILIO DETECTADO!")
    finally:
        print(f"  -> Operacion finalizada: {archivo_mensaje}\n")

    return resultado

with open("mensaje_mar.txt", "w", encoding="utf-8") as f:
    f.write("SOS: AYUDA - OPERADOR SECUESTRADO")
procesar_mensaje_ola("mensaje_mar.txt")
procesar_mensaje_ola("no_existe.txt")

# ============================================
# EXCEPCIONES PERSONALIZADAS
# ============================================

class GeneradorDesconectadoError(Exception):
    """Error cuando el generador no responde."""
    pass

class OlaAnomalaNoDetectadaError(Exception):
    """Error cuando no se encuentra el patron esperado."""
    def __init__(self, patron_esperado, patron_encontrado):
        super().__init__(f"Se esperaba '{patron_esperado}', se encontro '{patron_encontrado}'")

class EvidenciaInsuficienteError(Exception):
    """Error cuando no hay suficientes pruebas."""
    pass

# --- USANDO EXCEPCIONES PERSONALIZADAS ---

def verificar_generador(estado):
    """Verifica el estado del generador."""
    if estado == "desconectado":
        raise GeneradorDesconectadoError("El generador submarino no responde")
    elif estado == "anomalo":
        print("  OK Generador activo pero con comportamiento anomalo")
    else:
        print("  OK Generador funcionando normalmente")

def verificar_patron_ola(esperado, real):
    """Verifica que el patron de ola coincida."""
    if esperado != real:
        raise OlaAnomalaNoDetectadaError(esperado, real)
    return True

print("\n=== VALIDACIONES DEL GENERADOR ===\n")

try:
    verificar_generador("desconectado")
except GeneradorDesconectadoError as e:
    print(f"  X {e}")

try:
    verificar_patron_ola("--//O", "--//X")
except OlaAnomalaNoDetectadaError as e:
    print(f"  X {e}")

print("\n  OK Validaciones completadas")

# --- SIMULACION CON ERROR ---

try:
    # Intentar ejecutar el firmware original
    print("\n=== EJECUTANDO FIRMWARE ORIGINAL ===\n")

    usuarios_autorizados = ["carlos.parra", "miguel.soto", "luisa.rivas"]
    operador_actual = "carlos.parra"

    if operador_actual not in usuarios_autorizados:
        raise PermissionError(f"Operador '{operador_actual}' no autorizado")

    print(f"OK Acceso concedido a {operador_actual}")

    # Simular un comando
    try:
        raise NameError("variable 'firma_digital_LR2026' no definida")
    except NameError as e:
        print(f"  ! Error revelador: {e}")
        print(f"  -> La variable 'firma_digital_LR2026' sugiere:")
        print(f"    * Iniciales: LR = Luisa Rivas?")
        print(f"    * Anio: 2026")
        print(f"    * Firma digital: posiblemente de la biologa")

except PermissionError as e:
    print(f"X {e}")

print("\n  -> Analisis completo: el operador original podria ser Luisa Rivas")

# --- ENIGMAS ---

print("\n=== ENIGMA 9.1: Conexion segura al generador ===")
def conectar(ip, puerto):
    try:
        if ip == "0.0.0.0":
            raise ConnectionError("No se pudo conectar al generador")
        print(f"Conectado a {ip}:{puerto}")
    except ConnectionError as e:
        print(f"Error: {e}")

conectar("0.0.0.0", 8080)

print("\n=== ENIGMA 9.2: Lector de datos marinos tolerante ===")
nombre_archivo = "datos_marinos.txt"
try:
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("Contenido por defecto")
    print(f"Archivo {nombre_archivo} creado con contenido por defecto.")

print("\n=== ENIGMA 9.3: Excepcion personalizada ===")
class OlaNoDetectadaError(Exception):
    pass

def detectar_ola(altura):
    if altura == 0:
        raise OlaNoDetectadaError("No se detecto ninguna ola")
    print(f"Ola detectada con altura {altura}m")

try:
    detectar_ola(0)
except OlaNoDetectadaError as e:
    print(f"Error: {e}")

print("\n=== ENIGMA 9.4: Finally para cerrar conexion ===")
try:
    print("Conectando al generador submarino...")
    raise ConnectionError("Fallo de conexion")
except ConnectionError:
    print("Error durante la conexion")
finally:
    print("Cerrando conexion con el generador submarino")
