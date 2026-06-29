# Capítulo 8: Los Archivos del Puerto

## Conceptos: Manejo de archivos, `open()`, `with`, `read`/`write`

---

Mateo tenía el firmware del generador. Pero necesitaba más: necesitaba los registros históricos del proyecto LOCUENTO. Esos registros estaban en la computadora de la Capitanía del Puerto.

—Rafa —dijo—. ¿Puedes conseguirme los archivos?

—Estás loco. Esa información es clasificada.

—El mar no tiene clasificaciones, Rafa. El mar es de todos.

Rafa suspiró y asintió. Esa noche, le envió un archivo cifrado.

## Leyendo archivos: Abriendo el mar

En Python, `open()` abre un archivo. El bloque `with` asegura que se cierre correctamente:

```python
# ============================================
# LECTURA DE ARCHIVOS DEL PUERTO
# ============================================

# Crear un archivo de ejemplo con datos del puerto
datos_puerto = """BITÁCORA DEL PUERTO DE ANCÓN
FECHA: 27-06-2026

EMBARCACIONES REGISTRADAS:
- B/T "Mares del Sur" - Pesquero - 15:30
- Yate "Costa Azul" - Privado - 16:45
- Bote "Don Eulogio" - Pesquero artesanal - 05:00

ACTIVIDADES SOSPECHOSAS:
- 22:00 - Ruido submarino en sector norte
- 23:30 - Luces intermitentes en zona de boyas
- 01:00 - Embarcación no identificada

NOTA: Se recomienda no investigar.
"""

with open("bitacora_puerto.txt", "w", encoding="utf-8") as f:
    f.write(datos_puerto)

# Leer el archivo completo
with open("bitacora_puerto.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

print("=== BITÁCORA DEL PUERTO ===")
print(contenido)
```

### Leyendo línea por línea

```python
print("\n=== LEYENDO LÍNEA POR LÍNEA ===")
with open("bitacora_puerto.txt", "r", encoding="utf-8") as f:
    for num, linea in enumerate(f, 1):
        print(f"{num:3}: {linea.strip()}")
```

### Diferentes modos de apertura

| Modo | Significado |
|------|-------------|
| `"r"` | Lectura |
| `"w"` | Escritura (sobrescribe) |
| `"a"` | Añadir (append) |
| `"r+"` | Lectura y escritura |

## Procesando el archivo de embarcaciones

Mateo encontró un archivo CSV con las embarcaciones que habían estado cerca del generador:

```python
# --- PROCESANDO CSV DE EMBARCACIONES ---

csv_embarcaciones = """nombre,tipo,horario,dias_activo
Mares del Sur,Pesquero,15:30-23:00,30
Costa Azul,Yate privado,16:00-02:00,45
Don Eulogio,Pesquero artesanal,05:00-12:00,60
Lancha Rápida,No identificada,23:00-03:00,15
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
        print(f"  • {nombre:25} | {tipo:25} | {horario:15} | {dias} días activo")
        
        # Detectar embarcaciones sospechosas
        if int(dias) < 20 and "no identificada" in tipo.lower():
            print(f"    ⚠ ¡SOSPECHOSA! Poco tiempo activo y no identificada")

# Lectura con list comprehension
print("\n=== EMBARCACIONES NO IDENTIFICADAS ===")
with open("embarcaciones.csv", "r", encoding="utf-8") as f:
    next(f)  # Saltar encabezados
    no_id = [linea.strip().split(",") for linea in f if "no identificada" in linea.lower()]

for emb in no_id:
    print(f"  → {emb[0]} - Horario: {emb[2]}")
```

## Escribiendo evidencia

Mateo documentó todo lo que había descubierto:

```python
# --- DIARIO DE INVESTIGACIÓN ---

print("\n=== DOCUMENTANDO EL CASO ===\n")

with open("diario_mateo.txt", "w", encoding="utf-8") as d:
    d.write("== DIARIO DE INVESTIGACIÓN ==\n")
    d.write("Caso: Proyecto LOCUENTO - Contaminación de olas en Ancón\n")
    d.write("Investigador: Mateo Sánchez\n\n")
    d.write("--- DÍA 1 ---\n")
    d.write("Encontré patrones anómalos en las olas de Ancón.\n")
    d.write("Descubrí el generador submarino.\n")
    d.write("El firmware del generador tiene funciones en Python.\n")

# Verificar
with open("diario_mateo.txt", "r", encoding="utf-8") as d:
    print(d.read())

# Agregar más datos
print("=== AGREGANDO EVIDENCIA ===\n")
with open("diario_mateo.txt", "a", encoding="utf-8") as d:
    d.write("\n--- DÍA 2 ---\n")
    d.write("Identifiqué a los implicados.\n")
    d.write("El proyecto LOCUENTO es una fachada para privatizar Ancón.\n")
    d.write("El operador del generador sigue siendo desconocido.\n")

with open("diario_mateo.txt", "r", encoding="utf-8") as d:
    print(d.read())
```

## El archivo del operador

Entre los archivos, Mateo encontró uno con un nombre extraño:

```python
# --- ARCHIVO DEL OPERADOR ---

with open("operador.log", "w", encoding="utf-8") as f:
    f.write("""OPERADOR: DESCONOCIDO
ÚLTIMO ACCESO: 27-06-2026 23:45
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
            print(f"  📡 {linea.strip()}")
```

## Enigmas

### Enigma 8.1: Crea tu bitácora

Usando `open()` y `with`, crea un archivo `mi_diario_mar.txt` con la fecha de hoy y un párrafo sobre lo que aprendiste. Luego léelo.

### Enigma 8.2: Procesa el archivo de temperaturas

Dado un archivo con temperaturas del mar por día (una por línea), lee el archivo y calcula el promedio.

### Enigma 8.3: Agregando datos

Crea un programa que:
1. Pregunte "¿Qué viste en el mar hoy?" (input)
2. Agregue esa observación al final de `observaciones_mar.txt` (modo append)
3. Muestre todo el contenido

### Enigma 8.4: Buscador en archivos

Escribe un programa que lea `bitacora_puerto.txt` y cuente cuántas veces aparece la palabra "sospechosa".

---

## Lo que aprendiste

- `open(archivo, modo)` abre un archivo
- El bloque `with` cierra automáticamente
- **Modos**: `"r"` (lectura), `"w"` (escritura), `"a"` (append)
- `.read()` lee todo, se puede iterar línea por línea
- Archivos CSV se procesan con `.split(",")`

Mateo encontró algo inquietante en el archivo del operador: el último comando era `transmitir_mensaje("AYUDA")`. Alguien estaba pidiendo ayuda. No era el generador transmitiendo un mensaje de prueba: era el operador.

—El operador no es parte de la conspiración —dijo Mateo—. Es un rehén. O está siendo forzado a operar el generador.

—¿O alguien que quiere ser descubierto? —sugirió Rafa.

—Hay una forma de saberlo. Forzar un error en el sistema. Porque cuando un programa falla, revela información que no debería.

---
