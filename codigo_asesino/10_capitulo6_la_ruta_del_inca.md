# Capítulo 6: La Ruta del Qhapaq Ñan

## Conceptos: Bucles `for`/`while`, `range()`, `enumerate()`, `break`/`continue`

---

La noche había caído sobre Neo-Cusco cuando Wayra llegó al Callejón de las Siete Culebras, una estrecha vía peatonal que serpenteaba detrás del Coricancha. No había usado la entrada principal. No había usado ninguna entrada visible.

—El Qhapaq Ñan —dijo en voz baja, mirando un tramo de muro inca que parecía sólido—. El Camino del Inca. Treinta mil kilómetros de caminos que conectaban todo el imperio. Y todos los caminos pasaban por el Coricancha.

Su abuela le había enseñado que el Templo del Sol no solo era un centro religioso: era un **nodo** de comunicaciones. Los chasquis (mensajeros incas) llegaban desde los cuatro suyos (direcciones del imperio) con quipus y mensajes. Y había entradas secretas que solo los guardianes conocían.

Wayra presionó una piedra en la base del muro. No pasó nada. Presionó otra, tres piedras a la izquierda. Un crujido. Luego una tercera, dos piedras arriba. El muro se abrió lentamente, revelando un pasaje oscuro.

—Los caminos de los incas no desaparecieron —susurró—. Solo se volvieron digitales.

## For: Recorriendo caminos

Los **bucles** permiten repetir acciones. En Python, el bucle `for` es perfecto para **recorrer** colecciones: listas, strings, diccionarios, archivos. Como un chasqui que recorre el Qhapaq Ñan, el `for` visita cada elemento de una secuencia.

```python
# ============================================
# RECORRIENDO EL QHAPAQ ÑAN DIGITAL
# ============================================

# Las estaciones del Qhapaq Ñan (en orden)
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
```

—¿Y esto cómo nos ayuda? —preguntó Raúl, que la seguía por el pasaje oscuro.

—Inti dejó pistas en lugares específicos. Cada pista está asociada a una estación del Qhapaq Ñan. Si recorremos las estaciones en orden, encontramos el mensaje completo.

### `range()`: Caminos numerados

A veces necesitas recorrer un camino sabiendo la posición de cada paso. Para eso sirve `range()`:

```python
print("\n=== ESTACIONES CON NÚMERO DE RUTA ===")

# range(n) genera números de 0 a n-1
for i in range(len(estaciones_qhapaq_ñan)):
    print(f"Estación {i+1}: {estaciones_qhapaq_ñan[i]} (posición {i})")
```

### `enumerate()`: El índice y el valor

Pero hay una forma más elegante:

```python
print("\n=== ENUMERANDO LA RUTA ===")

for indice, estacion in enumerate(estaciones_qhapaq_ñan):
    print(f"  [{indice}] → {estacion}")
```

—Enumerar —dijo Wayra—. Como los nudos en un quipu. Cada posición tiene un significado. `enumerate()` te da el índice y el valor al mismo tiempo.

## El mensaje en las estaciones

Wayra encontró una pequeña cavidad en la pared del pasaje. Dentro, un datastick con una nota: "Para Wayra. Cada estación guarda una parte del código."

Conectó el datastick a su laptop:

```python
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

print("\n=== RECONSTRUYENDO EL CÓDIGO ===\n")

codigo_completo = ""
for estacion in estaciones_qhapaq_ñan:
    parte = codigo_estaciones.get(estacion, "")
    codigo_completo += parte
    print(f"{estacion}: '{parte}'")

print(f"\n--- Código resultante ---")
print(codigo_completo)
```

El código reconstruido era:

```
def descifrar_mensaje():
    quipu = 'YACHAY'
```

—Es una función —dijo Wayra—. Inti dejó el esqueleto de una función. La primera línea de lo que será el programa final. Pero está incompleto.

## While: Hasta encontrar la verdad

Hay otro tipo de bucle: `while`. Este se ejecuta **mientras** una condición sea verdadera. Es como caminar por un túnel hasta ver la luz.

```python
# ============================================
# EXPLORANDO EL PASAJE SECRETO
# ============================================

import time

print("\n=== EXPLORANDO EL PASAJE SECRETO ===\n")

pasos = 0
luz_encontrada = False

while not luz_encontrada:
    pasos += 1
    print(f"Paso {pasos}: Avanzando en la oscuridad...")
    
    # Simulación: después de 15 pasos, encontramos luz
    if pasos >= 15:
        luz_encontrada = True
        print(f"¡Luz encontrada después de {pasos} pasos!")
    
    time.sleep(0.3)  # Pequeña pausa para dramatismo

print("Hemos llegado al interior del laboratorio.")
```

### `break`: Salir del camino

A veces, encuentras lo que buscas antes de llegar al final del camino. `break` te permite salir de un bucle inmediatamente:

```python
print("\n=== BUSCANDO EL ARCHIVO YACHAY ===\n")

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
        break  # Salimos del bucle, no necesitamos seguir

print("\nBúsqueda completada.")
```

### `continue`: Saltar lo irrelevante

`continue` salta a la siguiente iteración, ignorando el resto del código del bucle. Es como ignorar las piedras en el camino y seguir avanzando:

```python
print("\n=== FILTRANDO ARCHIVOS RELEVANTES ===\n")

for archivo in archivos_del_lab:
    if archivo.endswith(".csv") or archivo.endswith(".md"):
        continue  # Saltamos archivos de datos y notas
    
    print(f"  Archivo relevante: {archivo}")
```

## El camino de los sospechosos

Wayra usó bucles para analizar los movimientos de los sospechosos:

```python
# ============================================
# ANALIZANDO MOVIMIENTOS CON BUCLES
# ============================================

# Registro de acceso del laboratorio (simplificado)
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
    {"nombre": "Lara", "hora": "02:34", "accion": "entrada"},  # ¿Lara?
    {"nombre": "Lara", "hora": "02:45", "accion": "salida"},   # ¿Lara?
]

print("=== LÍNEA DE TIEMPO DEL CASO ===\n")

nombre_anterior = ""
for registro in registro_accesos:
    if nombre_anterior and nombre_anterior != registro["nombre"]:
        print()  # Línea en blanco entre personas
    
    emoji = "🚪" if registro["accion"] == "entrada" else "🚶"
    print(f"  {registro['hora']} | {registro['nombre']:7} | {registro['accion']}")
    nombre_anterior = registro["nombre"]

# ANÁLISIS: ¿Quién estaba cuando?
print("\n=== ¿QUIÉNES ESTABAN A LAS 2:34 AM? ===\n")

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
```

Los resultados mostraron algo inquietante: según los registros, a las 2:34 a.m., solo "Lara" (o quien usó su cuenta) estaba en el laboratorio. Pero eso era exactamente lo que los registros **querían** mostrar.

—Falso —dijo Wayra—. Si alguien usó la cuenta de Lara, podría haber manipulado los registros. O podría haber entrado sin ser detectado.

—¿Por dónde? —preguntó Raúl.

Wayra señaló el túnel por el que acababan de llegar.

—Por aquí. Por el Qhapaq Ñan digital. Hay caminos que los sistemas modernos no monitorean. Caminos que los incas construyeron y que Inti restauró.

## El bucle infinito del engaño

Wayra escribió un último análisis:

```python
# --- SIMULACIÓN: ¿QUIÉN PUDO HABER ENTRADO? ---

sospechosos_con_acceso_secreto = []

# Todos los que sabían del Qhapaq Ñan digital
conocian_ruta = ["Inti", "Mama Killa", "Lara"]

print("\n=== ¿QUIÉN CONOCÍA LA RUTA SECRETA? ===\n")

for s in sospechosos:
    if s["nombre"].split()[0] in conocian_ruta:
        print(f"{s['nombre']}: Conocía la ruta")
        sospechosos_con_acceso_secreto.append(s["nombre"])
    else:
        # Pero alguien pudo haber descubierto la ruta
        if s["motivo"] >= 8:
            print(f"{s['nombre']}: No conocía la ruta, pero tenía motivo para investigar")
            sospechosos_con_acceso_secreto.append(s["nombre"])

print(f"\nPosibles culpables (con acceso secreto): {sospechosos_con_acceso_secreto}")
```

—Mama Killa conocía la ruta. Lara también. Pero Rodrigo... Rodrigo no tenía acceso, pero sí motivo. Y dinero. Dinero para pagar a alguien que sí conociera la ruta.

## Enigmas

### Enigma 6.1: Recorriendo la lista de evidencias

Dada la lista de evidencias del caso, usa un bucle `for` para mostrar cada evidencia con su número (usando `enumerate`):

```python
evidencias = [
    "Quipus digital en escritorio",
    "Registro de acceso manipulado",
    "Código en la pantalla OLED",
    "Mensaje cifrado en las estaciones",
    "Pasaje secreto del Qhapaq Ñan"
]
```

### Enigma 6.2: El filtro de archivos

Usando `continue`, escribe un bucle que recorra una lista de archivos y solo muestre los que terminan en `.py` (ignorando `.docx`, `.csv`, `.md`).

### Enigma 6.3: Buscar hasta encontrar

Usando `while` y `break`, simula la búsqueda de un sospechoso en una lista. Recorre la lista y cuando encuentres al sospechoso "Rodrigo Mamani", muestra "SOSPECHOSO ENCONTRADO" y rompe el bucle.

### Enigma 6.4: Range piramidal

Usando `range()` y bucles anidados, crea un patrón que muestre:

```
1
2 3
4 5 6
7 8 9 10
```

---

## Lo que aprendiste

- `for elemento in coleccion:` recorre secuencias
- `range(n)` genera números del 0 al n-1
- `enumerate()` da índice y valor simultáneamente
- `while condicion:` se ejecuta mientras la condición sea True
- `break` sale del bucle inmediatamente
- `continue` salta a la siguiente iteración
- Los bucles pueden anidarse
- Los bucles permiten procesar colecciones de datos completas

Wayra salió del pasaje secreto directamente al sótano del laboratorio. Estaba dentro. El sistema de seguridad no la había detectado porque su entrada no estaba en ningún registro.

—Los incas construyeron caminos que ni la tecnología moderna puede ver —dijo, más para sí misma que para Raúl—. Y el asesino usó uno de esos caminos.

Pero cuando llegó al escritorio de Inti, algo había cambiado. La pantalla OLED ahora mostraba un nuevo mensaje:

```
Has llegado lejos, Wayra. Pero el verdadero camino
no está en el Qhapaq Ñan físico. Está en el código.
Para encontrar al asesino, primero debes descifrar
la función que Inti dejó incompleta.

int yachay_runner(funcion, parametros):
    return funcion(parametros)
```

—Eso no es Python válido —dijo Raúl.

—No —respondió Wayra—. Pero es una pista. Necesito **funciones**. Necesito entender cómo Inti construyó Yachay. Y para eso, tengo que aprender a construir herramientas propias.

---
