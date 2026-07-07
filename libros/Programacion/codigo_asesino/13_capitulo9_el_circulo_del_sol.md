# Capítulo 9: El Círculo del Sol

## Conceptos: Manejo de errores, `try`/`except`/`finally`, excepciones personalizadas

---

Wayra presionó Enter.

El laboratorio entero crujió. Las luces parpadearon. Los monitores mostraron líneas de error en rojo. Y luego, silencio.

—¿Qué hiciste? —preguntó Raúl, alarmado.

—Forcé una división entre cero en el sistema Yachay —respondió Wayra, observando la pantalla—. En Python, cuando algo sale mal, el programa lanza una **excepción**. Y las excepciones revelan información.

En la terminal, un mensaje de error apareció:

```
Traceback (most recent call last):
  File "yachay_core.py", line 147, in descifrar_quipu
    resultado = quipu_data["cuerdas"][0]["nudos"] / 0
ZeroDivisionError: division by zero
```

—Mira —dijo Wayra, señalando—. El error nos muestra la ruta del archivo: `yachay_core.py`, línea 147, función `descifrar_quipu`. Y algo más... la estructura de datos: `quipu_data["cuerdas"][0]["nudos"]`. Yachay está organizado como un diccionario de cuerdas.

—¿Pero y si el error hubiera roto algo importante?

—Por eso vamos a aprender a manejar los errores. En Python, puedes **capturar** las excepciones y decidir qué hacer con ellas. Como un tejedor que, cuando se le rompe un hilo, no abandona el tejido: hace un nudo y sigue.

## Try/Except: Tejiendo a prueba de errores

El bloque `try/except` permite intentar código que podría fallar y manejar el error si ocurre:

```python
# ============================================
# MANEJO DE ERRORES EN EL LABORATORIO
# ============================================

print("=== SISTEMA DE ANÁLISIS TOLERANTE A FALLOS ===\n")

def analizar_quipu_seguro(quipu_data):
    """Analiza un quipu de forma segura, manejando errores."""
    try:
        # Intentar acceder a los datos del quipu
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

# Probar con datos válidos
quipu_valido = {
    "nombre": "Quipu ceremonial",
    "cuerdas": [
        {"color": "rojo", "nudos": [1, 4, 9]},
        {"color": "blanco", "nudos": [1, 3, 5, 7, 9]}
    ]
}

# Probar con datos inválidos
quipu_sin_nombre = {
    "cuerdas": [{"color": "rojo", "nudos": [1, 2, 3]}]
}

quipu_sin_cuerdas = {
    "nombre": "Quipu vacío"
}

quipu_invalido = "Esto no es un quipu"

analizar_quipu_seguro(quipu_valido)
analizar_quipu_seguro(quipu_sin_nombre)
analizar_quipu_seguro(quipu_sin_cuerdas)
analizar_quipu_seguro(quipu_invalido)
```

### Capturando múltiples excepciones

Wayra necesitaba procesar los archivos cifrados de Inti, pero muchos estaban dañados o tenían formatos inesperados:

```python
print("\n=== PROCESANDO ARCHIVOS DEL LABORATORIO ===\n")

def procesar_archivo_cifrado(ruta_archivo):
    """Intenta leer y descifrar un archivo del laboratorio."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        # Intentar convertir a número
        try:
            numero = int(contenido.strip())
            print(f"  ✓ Archivo numérico: {numero}")
        except ValueError:
            # No es un número, intentar como quipu
            if ":" in contenido:
                partes = contenido.split(":")
                print(f"  ✓ Formato quipu: {partes[0]} → {partes[1:]}")
            else:
                print(f"  ✓ Texto plano: {contenido[:50]}...")
        
    except FileNotFoundError:
        print(f"  ✗ Archivo no encontrado: {ruta_archivo}")
    except PermissionError:
        print(f"  ✗ Sin permisos para leer: {ruta_archivo}")
    except UnicodeDecodeError:
        print(f"  ✗ Codificación no soportada: {ruta_archivo}")
    except Exception as e:
        print(f"  ✗ Error desconocido procesando {ruta_archivo}: {e}")

# Simular archivos del laboratorio
import os

# Crear archivos de prueba
archivos_prueba = {
    "quipu_rojo.txt": "ROJO:1:4:9",
    "quipu_blanco.txt": "BLANCO:1:3:5:7:9",
    "numero_secreto.txt": "42",
    "nota_inti.txt": "Mama Killa sabe la verdad sobre el quipu",
    "archivo_secreto.bin": "datos_binarios_×_@_#_",
}

for nombre, contenido in archivos_prueba.items():
    with open(nombre, "w", encoding="utf-8") as f:
        f.write(contenido if not nombre.endswith(".bin") else contenido)

# Intentar procesar cada uno (incluyendo uno que no existe)
archivos_a_procesar = list(archivos_prueba.keys()) + ["archivo_inexistente.txt"]

for archivo in archivos_a_procesar:
    procesar_archivo_cifrado(archivo)
```

### Else y Finally: El tejido completo

El bloque `try/except` puede tener dos bloques adicionales:
- `else`: se ejecuta si **no** hubo excepción
- `finally`: se ejecuta **siempre**, haya o no error

```python
print("\n=== PROCESO FORENSE CON GARANTÍAS ===\n")

def proceso_forense_seguro(archivo_evidencia):
    """Procesa una evidencia con registro de actividad."""
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
    except Exception as e:
        print(f"  ERROR INESPERADO: {e}")
        resultado = -1
    else:
        # Solo se ejecuta si NO hubo error
        print(f"  ✓ Evidencia procesada: {resultado} bytes")
        print(f"  ✓ Contenido: {datos[:50]}...")
    finally:
        # Siempre se ejecuta
        print(f"  → Registro: Análisis de {archivo_evidencia} completado\n")
    
    return resultado

# Probar con diferentes archivos
proceso_forense_seguro("quipu_rojo.txt")
proceso_forense_seguro("archivo_inexistente.txt")

# Crear archivo vacío para probar ValueError
with open("evidencia_vacia.txt", "w") as f:
    f.write("")

proceso_forense_seguro("evidencia_vacia.txt")
```

## Excepciones personalizadas: Nudos propios

En Python, puedes crear tus propias excepciones. Como un tejedor que crea un nuevo tipo de nudo para un propósito específico:

```python
# ============================================
# EXCEPCIONES PERSONALIZADAS DEL CASO
# ============================================

class QuipuCorruptoError(Exception):
    """Error cuando un quipu digital está dañado o incompleto."""
    pass

class EvidenciaInconsistenteError(Exception):
    """Error cuando dos evidencias se contradicen."""
    def __init__(self, evidencia1, evidencia2, mensaje="Contradicción entre evidencias"):
        self.evidencia1 = evidencia1
        self.evidencia2 = evidencia2
        self.mensaje = mensaje
        super().__init__(f"{mensaje}: {evidencia1} vs {evidencia2}")

class AccesoNoAutorizadoError(Exception):
    """Error cuando alguien sin permiso intenta acceder."""
    def __init__(self, usuario, archivo):
        super().__init__(f"Acceso no autorizado: {usuario} intentó acceder a {archivo}")

# --- USANDO EXCEPCIONES PERSONALIZADAS ---

def verificar_quipu(quipu):
    """Verifica que un quipu tenga la estructura correcta."""
    if not isinstance(quipu, dict):
        raise QuipuCorruptoError("El quipu debe ser un diccionario")
    if "cuerdas" not in quipu:
        raise QuipuCorruptoError("El quipu no tiene cuerdas")
    if len(quipu["cuerdas"]) == 0:
        raise QuipuCorruptoError("El quipu está vacío")
    return True

def verificar_consistencia(evidencia1, evidencia2):
    """Verifica que dos evidencias no se contradigan."""
    if evidencia1["hora"] != evidencia2["hora"]:
        raise EvidenciaInconsistenteError(
            evidencia1["id"], evidencia2["id"],
            f"Horas diferentes: {evidencia1['hora']} vs {evidencia2['hora']}"
        )
    return True

# Probar las excepciones personalizadas
print("\n=== VALIDACIÓN CON EXCEPCIONES PERSONALIZADAS ===\n")

# 1. Quipu inválido
try:
    verificar_quipu("no_soy_un_quipu")
except QuipuCorruptoError as e:
    print(f"  ✗ Quipu corrupto: {e}")

# 2. Quipu válido
try:
    verificar_quipu({"cuerdas": [{"color": "rojo", "nudos": [1, 2, 3]}]})
    print("  ✓ Quipu válido")
except QuipuCorruptoError as e:
    print(f"  ✗ {e}")

# 3. Evidencias inconsistentes
evidencia_a = {"id": "Cámara 1", "hora": "02:30", "contenido": "Vio a alguien salir"}
evidencia_b = {"id": "Cámara 2", "hora": "02:35", "contenido": "No vio a nadie"}

try:
    verificar_consistencia(evidencia_a, evidencia_b)
except EvidenciaInconsistenteError as e:
    print(f"  ✗ {e}")
```

## El error que reveló la verdad

Wayra volvió a forzar errores en Yachay, pero esta vez con un propósito específico:

```python
print("\n=== SONDEANDO YACHAY CON ERRORES CONTROLADOS ===\n")

# Simular consultas a Yachay que fuerzan errores para revelar estructura
consultas = [
    "",                           # Vacío
    "42",                         # Número
    "{'cuerdas': []}",           # Dict vacío  
    "__import__('os').system('ls')",  # Intento de inyección
]

for consulta in consultas:
    try:
        # Intentar procesar la consulta
        resultado = eval(consulta) if consulta else None
        print(f"  ✓ Consulta válida: {resultado}")
    except SyntaxError as e:
        print(f"  ⚠ Error de sintaxis: {e}")
    except NameError as e:
        print(f"  ⚠ Variable no definida: {e}")
    except Exception as e:
        print(f"  ⚠ Error controlado: {type(e).__name__}: {e}")

# Finalmente, la consulta que reveló la estructura de Yachay
try:
    # Esta consulta falla pero revela la estructura de datos
    yachay_interno = {}
    x = yachay_interno["secretos"][0]["clave"]
except (KeyError, IndexError) as e:
    print(f"\n  → Yachay usa estructura: dict → list → dict")
    print(f"  → Error: {e}")
```

De repente, la pantalla de Yachay mostró algo inesperado. No un error, sino un mensaje:

```
[YACHAY] Has demostrado conocimiento de los errores.
[YACHAY] Has manejado las excepciones con sabiduría.
[YACHAY] El Círculo del Sol te da la bienvenida.

— No todos los errores son fracasos.
— Algunos son puertas que no sabías que existían.
— Has abierto la primera puerta.

Próxima clave: YACHAY_MODULES
```

El mensaje parpadeó y desapareció.

—El Círculo del Sol... —murmuró Wayra—. La organización de la que hablaba Inti. No es solo una leyenda. Es real. Y Yachay me acaba de dar acceso a su primer nivel.

—¿Y ahora? —preguntó Raúl.

—Ahora necesito organizar lo que he aprendido. No puedo seguir escribiendo todo en un solo archivo. Necesito **módulos**. Como las diferentes cuerdas de un quipu, cada una con su propósito, pero todas conectadas por el hilo principal.

## Enigmas

### Enigma 9.1: Calculadora forense segura

Escribe una función `dividir_evidencias(a, b)` que intente dividir `a` entre `b`. Si `b` es 0, captura `ZeroDivisionError` y muestra "Error: No se puede dividir una evidencia en cero partes". Si todo sale bien, muestra el resultado.

### Enigma 9.2: Lector de archivos tolerante

Pide al usuario un nombre de archivo con `input()`. Intenta abrirlo y leer su contenido. Si el archivo no existe, muestra "Archivo no encontrado. ¿Olvidaste la extensión?".

### Enigma 9.3: Tu propia excepción

Crea una clase `EvidenciaFaltanteError` que herede de `Exception`. Luego escribe una función `verificar_evidencia(lista_evidencias, evidencia_buscada)` que lance esa excepción si la evidencia no está en la lista.

### Enigma 9.4: Finally para limpiar

Escribe un programa que intente abrir un archivo, y use `finally` para mostrar "Cerrando conexión con la base de datos de evidencias" pase lo que pase.

---

## Lo que aprendiste

- `try/except` captura y maneja excepciones sin romper el programa
- Se pueden capturar **tipos específicos** de excepción (`ValueError`, `KeyError`, etc.)
- `else` se ejecuta si **no** hubo excepción
- `finally` se ejecuta **siempre** (haya o no error)
- Puedes crear **excepciones personalizadas** heredando de `Exception`
- Las excepciones revelan información sobre la estructura interna del programa
- Manejar errores es esencial para programas robustos

Wayra cerró la terminal de Yachay. Había logrado que el sistema hablara con ella a través de sus propios errores. Pero el mensaje mencionaba "YACHAY_MODULES". Necesitaba entender cómo Inti había organizado su creación.

—Módulos —dijo—. Inti dividió Yachay en módulos. Como las cuerdas separadas de un gran quipu. Cada módulo hace algo específico: uno lee quipus, otro descifra, otro gestiona usuarios...

—¿Y cómo accedemos a ellos?

—En Python, los módulos se importan. Y para importar, necesitamos saber los nombres.

Wayra abrió el explorador de archivos del sistema. En la carpeta principal de Yachay, encontró algo que no había visto antes:

```
yachay/
  __init__.py
  core.py
  quipus.py
  descifrado.py
  usuarios.py
  circulo_del_sol.py  ← NUEVO
```

—El Círculo del Sol no solo es una organización externa —dijo lentamente—. Es parte del código de Yachay. Inti lo puso dentro del sistema.

—Entonces, ¿el Círculo del Sol... es un programa?

—No. El Círculo del Sol es un programa **y** una organización. O la organización se llama igual que el módulo. O el módulo controla la organización.

Wayra sintió que estaba al borde de algo enorme. Pero para entenderlo, necesitaba dominar los **módulos** de Python.

---
