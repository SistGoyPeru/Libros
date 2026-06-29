# Capítulo 2: El Lenguaje del Mar

## Conceptos: Strings, métodos de string, slicing

---

Eran las 2:00 a.m. cuando Mateo se despertó sobresaltado. El sonido del mar golpeando el muelle de Ancón era distinto. Más rítmico. Casi musical.

Se puso los shorts y salió corriendo a la playa. La luna llena iluminaba el agua como un reflector plateado. Y entonces lo vio.

Las olas no solo tenían patrones: tenían **mensajes**.

Cada ola, al romper, dejaba una línea de espuma en la orilla. La espuma no se dispersaba al azar: formaba líneas rectas. Como código de barras en la arena.

—Son strings —susurró Mateo—. Cadenas de caracteres escritas en el agua.

## Strings: El alfabeto del mar

Los **strings** son secuencias de caracteres. Como las olas: una tras otra, formando un mensaje.

Mateo corrió a su laptop y comenzó a transcribir los patrones de espuma:

```python
# ============================================
# MENSAJES DEL MAR
# ============================================

# Patrones de espuma observados en la orilla
# Cada carácter representa la forma de la espuma:
# '-' = línea recta, '/' = diagonal, 'O' = círculo

patron_1 = "--//O--//O--//O"
patron_2 = "O--O--O--O--O--"
patron_3 = "-/O-/-/O-/-/O--"

print("=== PATRONES DE ESPUMA ===")
print(f"Patrón 1: {patron_1}")
print(f"Patrón 2: {patron_2}")
print(f"Patrón 3: {patron_3}")
```

### Accediendo a caracteres: La posición de la ola

Cada carácter en un string tiene una posición (índice). Como cada ola en el mar tiene un orden:

```python
# Accediendo a posiciones específicas
print(f"\n--- Analizando Patrón 1 ---")
print(f"Primer carácter: '{patron_1[0]}'")
print(f"Tercer carácter: '{patron_1[2]}'")
print(f"Último carácter: '{patron_1[-1]}'")
print(f"Primeros 3: '{patron_1[0:3]}'")
print(f"Últimos 4: '{patron_1[-4:]}'")
```

### Slicing: Leyendo entre olas

El **slicing** permite extraer porciones de un string. Como elegir solo ciertas olas para surfear:

```python
# Slicing: [inicio:fin:paso]
print(f"\n--- Slicing de patrones ---")

# Primeros 6 caracteres
primeras_6 = patron_1[:6]
print(f"Primeras 6 posiciones: '{primeras_6}'")

# Cada 2 caracteres (saltando uno)
cada_dos = patron_1[::2]
print(f"Cada 2 posiciones: '{cada_dos}'")

# Invertir el patrón
inverso = patron_1[::-1]
print(f"Patrón invertido: '{inverso}'")
```

### Métodos de string: Herramientas del surfista digital

Mateo necesitaba herramientas más potentes. Los **métodos de string** son funciones que pertenecen al string y permiten manipularlo:

```python
# --- MÉTODOS DE STRING ---

mensaje_del_mar = "  EL CODIGO ESTA EN LA FRECUENCIA  "

# strip() - elimina espacios
limpio = mensaje_del_mar.strip()
print(f"\nOriginal: '{mensaje_del_mar}'")
print(f"Limpio: '{limpio}'")

# lower() / upper()
print(f"Minúsculas: '{limpio.lower()}'")
print(f"Mayúsculas: '{limpio.upper()}'")

# replace() - reemplazar texto
reemplazado = limpio.replace("FRECUENCIA", "ALTURA")
print(f"Reemplazado: '{reemplazado}'")

# find() - encontrar posición
pos = limpio.find("FRECUENCIA")
print(f"'FRECUENCIA' está en posición: {pos}")

# count() - contar ocurrencias
conteo_e = limpio.count("E")
print(f"Veces que aparece 'E': {conteo_e}")

# len() - longitud
print(f"Longitud del mensaje: {len(limpio)}")
```

## El mensaje cifrado en las olas

Mateo transcribió los patrones de 5 olas consecutivas y notó que, al unirlos, formaban algo:

```python
# --- DESCIFRANDO EL MENSAJE ---

ola_1 = "M-A-R"
ola_2 = "C-O-N"
ola_3 = "T-A-M"
ola_4 = "I-N-A"
ola_5 = "D-O--"

# Unir las olas para formar el mensaje
mensaje_completo = ola_1 + ola_2 + ola_3 + ola_4 + ola_5
print(f"\nMensaje completo: {mensaje_completo}")

# Limpiar el mensaje (quitar guiones)
mensaje_limpio = mensaje_completo.replace("-", "")
print(f"Mensaje limpio: {mensaje_limpio}")

# Convertir a minúsculas
print(f"En minúsculas: {mensaje_limpio.lower()}")

# Verificar si contiene palabras clave
if "CONTAMINACION" in mensaje_limpio.upper():
    print("¡El mensaje habla de contaminación!")
if "MAR" in mensaje_limpio.upper():
    print("¡El mensaje menciona el mar!")
```

—"MARCONTAMINADO" —leyó Mateo—. El mensaje del mar dice "mar contaminado". Alguien está enviando una advertencia.

## El nombre del generador

En el parte de olas, Mateo encontró una coordenada que se repetía:

```python
# --- COORDENADA DEL GENERADOR ---

coordenada = "11°46'30.7\"S 77°11'22.3\"W"
print(f"\nCoordenada del generador: {coordenada}")

# Extraer latitud y longitud
latitud = coordenada[:15]
longitud = coordenada[16:]
print(f"Latitud: {latitud}")
print(f"Longitud: {longitud}")

# El nombre del proyecto estaba codificado en la frecuencia
frecuencias = "12-15-09-21-05-14-20-15"
letras = frecuencias.split("-")
nombre_proyecto = ""
for num in letras:
    letra = chr(int(num) + 64)  # A=1, B=2, etc.
    nombre_proyecto += letra
    print(f"{num} → '{letra}'")

print(f"\nNombre del proyecto: {nombre_proyecto}")
```

—"L O C U E N T O" —dijo Mateo—. "LOCUENTO". ¿Qué significa?

Buscó en Google. "Locuento" no existía. Pero "LOCUENTO" sonaba a "LOC-uento". O "LOC" como "location". O tal vez era un acrónimo.

Lo anotó y siguió investigando.

## Enigmas

### Enigma 2.1: Descifra la frecuencia

Las frecuencias de las olas anómalas son: "03-15-12-01-19". Convierte cada número a letra (A=1, B=2, ...) usando `chr(num + 64)` y descubre la palabra.

### Enigma 2.2: Extrae el nombre del barco

Del string `"B/T-MARES-DE-ANCÓN-2026"`, extrae solo "ANCÓN" usando slicing y `find()`.

### Enigma 2.3: Invertir el mensaje

El mar dejó este mensaje en la arena: `"ODATNEMIRP SE ODAGUA"`. Inviértelo con `[::-1]`. ¿Qué dice?

### Enigma 2.4: Limpieza de datos

El sensor de olas registró: `"  OLA: 2.4m - FREC: 12s  "`. Usa `strip()`, `replace()`, y `split()` para obtener solo los valores numéricos.

---

## Lo que aprendiste

- Los **strings** son secuencias de caracteres con posiciones (índices)
- El **slicing** `[inicio:fin:paso]` extrae partes de un string
- Los **índices negativos** cuentan desde el final
- **Métodos**: `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.find()`, `.count()`
- `len()` da la longitud
- `+` concatena strings
- `[::-1]` invierte un string

Mateo tenía el mensaje: "MAR CONTAMINADO" y un nombre: "LOCUENTO". Pero necesitaba más. Necesitaba saber quién más estaba involucrado.

—Si esto es una conspiración —pensó—, debe haber más personas. Una red. Una lista.

Y para eso, necesitaba **listas** de Python.

---
