# Capítulo 8: Los Archivos del Laboratorio

## Conceptos: Manejo de archivos, `open()`, `with`, `read`/`write`, rutas

---

El laboratorio de Inti Quispe era un caos ordenado. Pero Wayra sabía que en ese caos había un patrón. Como en los quipus, donde cada cuerda tiene un lugar específico, cada archivo en el laboratorio tenía un propósito.

—Los archivos —dijo Wayra, abriendo el explorador de archivos— son como las cuerdas de un quipu. Algunas son principales, otras secundarias. Pero todas guardan información.

—¿Por dónde empezamos? —preguntó Raúl.

—Por el principio. Inti dejó pistas en archivos de texto. Pero no archivos normales: archivos con formato de quipu.

## Leyendo archivos: Escuchar las cuerdas

En Python, `open()` es la puerta de entrada a los archivos. Piensa en ello como tomar una cuerda de quipu en tus manos para leer sus nudos.

```python
# ============================================
# SISTEMA DE LECTURA DE ARCHIVOS
# ============================================

# --- MODO LECTURA: Leer el archivo completo ---

# Simulación: creamos un archivo de evidencias
evidencias_texto = """=== EVIDENCIAS DEL CASO INTI QUISPE ===

1. Quipus digital modificado el 27/06/2026 a las 02:34
2. Registro de acceso con cuenta de Lara Mamani
3. Mensaje en pantalla OLED: "Bienvenido, Wayra"
4. Pasaje secreto del Qhapaq Ñan restaurado
5. Código fuente de Yachay modificado

NOTA: El quipus blanco contiene la clave.
"""

# Primero, guardamos este texto en un archivo
with open("evidencias_caso.txt", "w", encoding="utf-8") as archivo:
    archivo.write(evidencias_texto)

# Ahora lo leemos
with open("evidencias_caso.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("=== CONTENIDO DEL ARCHIVO ===")
print(contenido)
```

### El bloque `with`: Tejiendo y destejendo

El bloque `with` es como tomar una cuerda, leerla y devolverla a su lugar. Se encarga de abrir **y cerrar** el archivo automáticamente. Sin `with`, tendrías que acordarte de cerrar el archivo manualmente.

### Diferentes modos de apertura

Los archivos pueden abrirse en diferentes modos, como diferentes formas de tejer:

| Modo | Significado |
|------|-------------|
| `"r"` | Lectura (read) |
| `"w"` | Escritura (write) - **sobrescribe** |
| `"a"` | Añadir (append) - agrega al final |
| `"r+"` | Lectura y escritura |

### Leyendo línea por línea

Para archivos grandes (como un quipu largo), es mejor leer línea por línea:

```python
print("=== LEYENDO LÍNEA POR LÍNEA ===\n")

with open("evidencias_caso.txt", "r", encoding="utf-8") as archivo:
    for numero_linea, linea in enumerate(archivo, 1):
        print(f"Línea {numero_linea}: {linea.strip()}")
```

## El archivo de los sospechosos

Wayra encontró un archivo llamado `sospechosos.csv` en el escritorio de Inti:

```python
# Simulamos el archivo CSV
csv_content = """nombre,edad,rol,acceso,motivo
Lara Mamani,32,Asistente,True,7
Carlos Huamán,55,Colega,True,8
Sarah Chen,40,Colaboradora,True,6
Rodrigo Mamani,60,Empresario,False,9
Mama Killa,70,Hermana,True,5
"""

with open("sospechosos.csv", "w", encoding="utf-8") as f:
    f.write(csv_content)

# Procesando el CSV manualmente
print("=== DATOS DE SOSPECHOSOS (CSV) ===\n")

with open("sospechosos.csv", "r", encoding="utf-8") as f:
    # Leer la primera línea (encabezados)
    encabezados = f.readline().strip().split(",")
    print(f"Columnas: {encabezados}\n")
    
    # Leer el resto de líneas
    for linea in f:
        datos = linea.strip().split(",")
        nombre, edad, rol, acceso, motivo = datos
        
        print(f"  • {nombre:25} | Edad: {edad:3} | {rol:20} | Acceso: {acceso:5} | Motivo: {motivo}")

# Lectura con list comprehension
print("\n=== SOLO NOMBRES Y MOTIVOS ===\n")

with open("sospechosos.csv", "r", encoding="utf-8") as f:
    next(f)  # Saltar encabezados
    sospechosos_lista = [linea.strip().split(",") for linea in f]

for s in sospechosos_lista:
    print(f"  {s[0]}: Motivo {s[4]}/10")
```

## Escribiendo archivos: Documentando el caso

Wayra necesitaba documentar todo lo que estaba descubriendo:

```python
# ============================================
# DIARIO DE INVESTIGACIÓN
# ============================================

print("=== DOCUMENTANDO EL CASO ===\n")

with open("diario_wayra.txt", "w", encoding="utf-8") as diario:
    diario.write("== DIARIO DE INVESTIGACIÓN ==\n")
    diario.write("Caso: Asesinato del Dr. Inti Quispe\n")
    diario.write(f"Fecha: 27 de junio, 2026\n")
    diario.write(f"Investigadora: Wayra Condori\n\n")
    
    diario.write("--- DÍA 1 ---\n")
    diario.write("Descubrí el cuerpo a través de Raúl.\n")
    diario.write("Encontré un quipus digital con mensaje cifrado.\n")
    diario.write("El sistema de bienvenida sabía que yo llegaría.\n\n")
    
    diario.write("--- SOSPECHOSOS INICIALES ---\n")
    for s in sospechosos_lista:
        diario.write(f"{s[0]}: {s[2]} - Sospecha: {s[4]}/10\n")

# Verificar que se escribió correctamente
print("Archivo 'diario_wayra.txt' creado.\n")

with open("diario_wayra.txt", "r", encoding="utf-8") as diario:
    print(diario.read())
```

### Añadiendo datos (modo append)

Más tarde, Wayra quiso agregar información sin borrar lo anterior:

```python
print("=== AGREGANDO NUEVA EVIDENCIA ===\n")

with open("diario_wayra.txt", "a", encoding="utf-8") as diario:
    diario.write("\n--- NUEVA EVIDENCIA ---\n")
    diario.write("Encontré un pasaje secreto del Qhapaq Ñan.\n")
    diario.write("El quipus blanco contiene coordenadas.\n")
    diario.write("Alguien está usando Yachay en este momento.\n")

# Leer el archivo actualizado
with open("diario_wayra.txt", "r", encoding="utf-8") as diario:
    print(diario.read())
```

## El archivo cifrado: El legado de Inti

Wayra encontró un archivo llamado `quipu_legado.txt`. Pero cuando intentó abrirlo, el contenido era un galimatías:

```python
# Simulando el archivo cifrado
with open("quipu_legado.txt", "w", encoding="utf-8") as f:
    f.write("""
qUiPu DiGiTaL v2.0
ÑaN:1:3:5:7:9:11:13
YaChAy:2:4:6:8:10:12:14
CoRiCaNcHa:1:4:9:16:25
PaChAcUtEc:3:6:12:24:48
    """.strip())

# Leer y procesar el archivo cifrado
print("=== QUIPU LEGADO: ARCHIVO ENCONTRADO ===\n")

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
        
        # Analizar patrón
        if nombre.isupper():
            print(f"    → TODO MAYÚSCULAS: Palabra clave")
        elif nombre[0].isupper():
            print(f"    → Capitalizado: Nombre propio")
        
        # ¿Patrón numérico?
        if len(numeros) >= 3:
            diferencias = [numeros[i+1] - numeros[i] for i in range(len(numeros)-1)]
            if len(set(diferencias)) == 1:
                print(f"    → Progresión aritmética (diferencia: {diferencias[0]})")
            elif numeros == [i**2 for i in range(1, len(numeros)+1)]:
                print(f"    → Números cuadrados")
            elif all(n % 2 == 1 for n in numeros):
                print(f"    → Solo impares (preguntas)")
            elif all(n % 2 == 0 for n in numeros):
                print(f"    → Solo pares (respuestas)")
        print()
```

## El archivo que cambió todo

Entre todos los archivos, uno llamó la atención de Wayra: `confesion_inti.txt`. Pero cuando fue a abrirlo,发现 estaba vacío.

—No está vacío —dijo Wayra—. Está cifrado. Es un archivo que Inti dejó preparado, pero el contenido se borró cuando... cuando lo mataron.

—¿Cómo sabes que tenía contenido? —preguntó Raúl.

Wayra señaló las propiedades del archivo:

```python
import os

# Ver metadatos del archivo
print("=== METADATOS DEL ARCHIVO ===\n")

if os.path.exists("quipu_legado.txt"):
    tamaño = os.path.getsize("quipu_legado.txt")
    print(f"Archivo: quipu_legado.txt")
    print(f"Tamaño: {tamaño} bytes")
    print(f"Existe: {os.path.exists('quipu_legado.txt')}")
    print(f"Es archivo: {os.path.isfile('quipu_legado.txt')}")

# Listar todos los archivos .txt del directorio
print("\n=== ARCHIVOS DE TEXTO ENCONTRADOS ===\n")

archivos_txt = [f for f in os.listdir('.') if f.endswith('.txt')]
for archivo in archivos_txt:
    tamaño = os.path.getsize(archivo)
    print(f"  • {archivo:30} ({tamaño} bytes)")
```

Pero Wayra notó algo más. Había un archivo oculto en el sistema: `.quipu_maestro.txt`. Los archivos que empiezan con punto son ocultos en sistemas Unix.

```python
# --- DESCUBRIENDO EL ARCHIVO OCULTO ---

contenido_oculto = """ERES LA HEREDERA DEL CONOCIMIENTO.
BUSCA EN LOS NUDOS DEL QUIPU BLANCO.
LA RESPUESTA ESTÁ EN EL CÓDIGO FUENTE DE YACHAY.
NO CONFÍES EN LARA. NO CONFÍES EN CARLOS.
MAMA KILLA SABE LA VERDAD PERO NO LA DIRÁ.
EL ASESINO ESTÁ MÁS CERCA DE LO QUE CREES.

-- INTI
"""

with open(".quipu_maestro.txt", "w", encoding="utf-8") as f:
    f.write(contenido_oculto)

# Leer el archivo oculto
with open(".quipu_maestro.txt", "r", encoding="utf-8") as f:
    mensaje_oculto = f.read()

print("=== MENSAJE OCULTO ENCONTRADO ===\n")
print(mensaje_oculto)
```

## Enigmas

### Enigma 8.1: Crea tu propio archivo de caso

Usando `open()` y `with`, crea un archivo llamado `mi_informe.txt` que contenga:
- Tu nombre como investigador
- La fecha de hoy
- Una lista de 3 sospechosos con sus datos
- Luego léelo y muéstralo en pantalla

### Enigma 8.2: Procesa el archivo de coartadas

Dado el siguiente contenido de archivo:

```
Lara Mamani:22:30:01:00
Carlos Huamán:01:00:02:30
Sarah Chen:02:30:04:00
```

Donde el formato es `nombre:hora_inicio:hora_fin`, escribe un programa que:
1. Lea el archivo
2. Por cada persona, determine si la hora del crimen (02:34) está dentro de su rango
3. Muestre quién tiene coartada y quién no

### Enigma 8.3: Bitácora de investigación

Crea un programa que:
1. Pregunte al usuario qué evidencia nueva encontró (input)
2. Agregue esa evidencia al final del archivo `bitacora.txt` (modo append)
3. Muestre todo el contenido actualizado de la bitácora

### Enigma 8.4: Buscador de palabras clave

Escribe un programa que lea un archivo de texto y cuente cuántas veces aparece la palabra "YACHAY" (en cualquier combinación de mayúsculas/minúsculas). Pista: usa `.lower()` para normalizar.

---

## Lo que aprendiste

- `open(archivo, modo)` abre un archivo en el modo especificado
- El bloque `with` asegura que el archivo se cierre automáticamente
- **Modos comunes**: `"r"` (lectura), `"w"` (escritura), `"a"` (añadir)
- `.read()` lee todo el contenido, `.readlines()` lee línea por línea
- Se puede iterar sobre un archivo directamente con `for linea in archivo`
- `os.path` proporciona funciones para trabajar con rutas y metadatos
- Los archivos ocultos empiezan con `.` en Unix/Linux
- Los archivos CSV se pueden procesar con `.split(",")` y list comprehension

Wayra guardó el mensaje del archivo oculto. Las advertencias de Inti eran claras: "No confíes en Lara. No confíes en Carlos. Mama Killa sabe la verdad."

Pero si no podía confiar en los sospechosos principales, ¿en quién podía confiar?

—Raúl —dijo—. ¿Confío en ti?

Raúl la miró, sorprendido.

—Wayra, llevamos años siendo amigos. Te llamé porque confío en ti.

—Lo sé. Pero Inti escribió ese mensaje antes de morir. Y sabía que alguien lo iba a traicionar. La pregunta es: ¿cuál de los sospechosos es el que realmente lo mató?

Wayra miró la pantalla. El sistema Yachay seguía activo. Y alguien seguía observándola.

—Hay una forma de descubrirlo —dijo—. Pero necesito hacer que el sistema falle. Necesito que muestre un error. Porque en los errores, en las excepciones, es donde se esconden las verdades que no deberían verse.

—¿Y si el sistema se bloquea?

—Entonces el asesino sabrá que estamos aquí. Pero también sabrá que estamos cerca de la verdad.

Wayra tomó el teclado. Era hora de forzar un error.

---
