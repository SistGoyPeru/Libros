# Capítulo 9: El Error en la Red

## Conceptos: Manejo de errores, `try`/`except`/`finally`, excepciones personalizadas

---

Mateo había descargado el software del generador. Pero cuando intentó ejecutar una simulación, el programa falló. Y en el fallo, encontró una pista.

```
Traceback (most recent call last):
  File "generador.py", line 42, in transmitir_mensaje
    ola = generar_ola(altura, frecuencia, codigo_morse)
NameError: name 'codigo_morse' is not defined
```

—El error revela que hay una variable `codigo_morse` que no está definida —dijo Mateo—. Pero está siendo llamada desde `transmitir_mensaje`. Eso significa que el generador puede transmitir en código Morse. No solo en frecuencias.

—¿Y cómo nos ayuda eso?

—Porque si el sistema falla, revela información. Y en Python, podemos controlar esos fallos.

## Try/Except: Atrapando errores como olas

```python
# ============================================
# SISTEMA TOLERANTE A ERRORES
# ============================================

def conectar_generador(ip):
    """Intenta conectar con el generador submarino."""
    try:
        print(f"  Conectando a {ip}...")
        # Simular conexión fallida
        if "192.168" in ip:
            raise ConnectionError("Red local no disponible")
        elif "10.0" in ip:
            raise TimeoutError("Tiempo de espera agotado")
        else:
            print("  ✓ Conexión exitosa")
            return True
    except ConnectionError as e:
        print(f"  ✗ Error de conexión: {e}")
        return False
    except TimeoutError as e:
        print(f"  ✗ Timeout: {e}")
        return False
    except Exception as e:
        print(f"  ✗ Error inesperado: {e}")
        return False

conectar_generador("192.168.1.100")
conectar_generador("10.0.0.5")
conectar_generador("172.16.0.1")
```

### Capturando múltiples excepciones

```python
def leer_configuracion_generador(ruta_archivo):
    """Lee la configuración del generador desde un archivo."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            config = f.read()
        
        try:
            niveles = [int(x) for x in config.split(",")]
            print(f"  ✓ Configuración cargada: {niveles}")
            return niveles
        except ValueError:
            print(f"  ✗ Formato inválido: '{config.strip()}' no es numérico")
            return []
    
    except FileNotFoundError:
        print(f"  ✗ Archivo no encontrado: {ruta_archivo}")
        return []
    except PermissionError:
        print(f"  ✗ Sin permisos para leer: {ruta_archivo}")
        return []

print("\n=== LEYENDO CONFIGURACIÓN ===\n")

# Crear archivos de prueba
with open("config_valida.txt", "w", encoding="utf-8") as f:
    f.write("12,15,9,21,5,14,20,15")
with open("config_invalida.txt", "w", encoding="utf-8") as f:
    f.write("doce,quince,nueve")

leer_configuracion_generador("config_valida.txt")
leer_configuracion_generador("config_invalida.txt")
leer_configuracion_generador("no_existe.txt")
```

### Else y Finally

```python
print("\n=== PROCESO CON GARANTÍAS ===\n")

def procesar_mensaje_ola(archivo_mensaje):
    """Procesa un mensaje codificado en olas."""
    print(f"Iniciando procesamiento de: {archivo_mensaje}")
    
    try:
        with open(archivo_mensaje, "r", encoding="utf-8") as f:
            datos = f.read()
        
        if not datos.strip():
            raise ValueError("Mensaje vacío")
        
        resultado = len(datos)
        
    except FileNotFoundError:
        print(f"  ERROR: Mensaje no encontrado")
        resultado = -1
    except ValueError as e:
        print(f"  ERROR: {e}")
        resultado = -1
    else:
        print(f"  ✓ Mensaje procesado: {resultado} caracteres")
        if "SOS" in datos or "AYUDA" in datos:
            print(f"  ⚠ ¡MENSAJE DE AUXILIO DETECTADO!")
    finally:
        print(f"  → Operación finalizada: {archivo_mensaje}\n")
    
    return resultado

with open("mensaje_mar.txt", "w", encoding="utf-8") as f:
    f.write("SOS: AYUDA - OPERADOR SECUESTRADO")
procesar_mensaje_ola("mensaje_mar.txt")
procesar_mensaje_ola("no_existe.txt")
```

## Excepciones personalizadas: Nudos propios

Mateo creó sus propias excepciones para el caso:

```python
# ============================================
# EXCEPCIONES PERSONALIZADAS
# ============================================

class GeneradorDesconectadoError(Exception):
    """Error cuando el generador no responde."""
    pass

class OlaAnómalaNoDetectadaError(Exception):
    """Error cuando no se encuentra el patrón esperado."""
    def __init__(self, patron_esperado, patron_encontrado):
        super().__init__(f"Se esperaba '{patron_esperado}', se encontró '{patron_encontrado}'")

class EvidenciaInsuficienteError(Exception):
    """Error cuando no hay suficientes pruebas."""
    pass

# --- USANDO EXCEPCIONES PERSONALIZADAS ---

def verificar_generador(estado):
    """Verifica el estado del generador."""
    if estado == "desconectado":
        raise GeneradorDesconectadoError("El generador submarino no responde")
    elif estado == "anómalo":
        print("  ✓ Generador activo pero con comportamiento anómalo")
    else:
        print("  ✓ Generador funcionando normalmente")

def verificar_patron_ola(esperado, real):
    """Verifica que el patrón de ola coincida."""
    if esperado != real:
        raise OlaAnómalaNoDetectadaError(esperado, real)
    return True

print("\n=== VALIDACIONES DEL GENERADOR ===\n")

try:
    verificar_generador("desconectado")
except GeneradorDesconectadoError as e:
    print(f"  ✗ {e}")

try:
    verificar_patron_ola("--//O", "--//X")
except OlaAnómalaNoDetectadaError as e:
    print(f"  ✗ {e}")

print("\n  ✓ Validaciones completadas")
```

## El error que reveló al operador

Mateo ejecutó una simulación del generador con datos reales. El programa falló con un error que mostraba el nombre del operador:

```python
# --- SIMULACIÓN CON ERROR ---

try:
    # Intentar ejecutar el firmware original
    print("\n=== EJECUTANDO FIRMWARE ORIGINAL ===\n")
    
    usuarios_autorizados = ["carlos.parra", "miguel.soto", "luisa.rivas"]
    operador_actual = "carlos.parra"
    
    if operador_actual not in usuarios_autorizados:
        raise PermissionError(f"Operador '{operador_actual}' no autorizado")
    
    print(f"✓ Acceso concedido a {operador_actual}")
    
    # Simular un comando
    try:
        raise NameError("variable 'firma_digital_LR2026' no definida")
    except NameError as e:
        print(f"  ⚠ Error revelador: {e}")
        print(f"  → La variable 'firma_digital_LR2026' sugiere:")
        print(f"    • Iniciales: LR = ¿Luisa Rivas?")
        print(f"    • Año: 2026")
        print(f"    • Firma digital: posiblemente de la bióloga")

except PermissionError as e:
    print(f"✗ {e}")

print("\n  → Análisis completo: el operador original podría ser Luisa Rivas")
```

—Luisa Rivas —dijo Mateo—. La bióloga marina. La que denunció el ruido submarino... Pero firmó el código del generador. ¿Ella lo programó o alguien usó su firma?

—O ella está infiltrada —dijo Rafa—. Trabajando desde adentro para exponer el proyecto.

—Hay una forma de saberlo. Necesito ver el código completo. El firmware está dividido en **módulos**. Y cada módulo tiene un autor.

## Enigmas

### Enigma 9.1: Conexión segura al generador

Escribe una función `conectar(ip, puerto)` que intente la conexión y capture `ConnectionError` mostrando "No se pudo conectar al generador".

### Enigma 9.2: Lector de datos marinos tolerante

Pide al usuario un nombre de archivo. Intenta abrirlo. Si no existe, captura el error y crea el archivo con contenido por defecto.

### Enigma 9.3: Excepción personalizada

Crea `OlaNoDetectadaError` y una función `detectar_ola(altura)` que la lance si la altura es 0.

### Enigma 9.4: Finally para cerrar conexión

Simula una conexión al generador que use `finally` para mostrar "Cerrando conexión con el generador submarino" pase lo que pase.

---

## Lo que aprendiste

- `try/except` captura errores sin romper el programa
- Se capturan tipos específicos (`ValueError`, `FileNotFoundError`, etc.)
- `else` se ejecuta si no hubo error
- `finally` se ejecuta siempre
- Puedes crear **excepciones personalizadas**
- Los errores revelan información de la estructura interna

Mateo tenía un nuevo sospechoso: Luisa Rivas. Pero no estaba seguro de si era cómplice o víctima. La firma digital LR2026 podía haber sido plantada.

—Necesito entender la estructura completa del proyecto —dijo—. El firmware está organizado en **módulos**. Como las diferentes partes de un barco: motor, navegación, comunicaciones. Cada módulo es un archivo separado.

---
