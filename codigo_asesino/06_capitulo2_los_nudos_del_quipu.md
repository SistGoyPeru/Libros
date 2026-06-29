# Capítulo 2: Los Nudos del Quipu

## Conceptos: Strings, métodos de string, slicing, formateo

---

El corazón de Wayra latía con fuerza mientras leía el mensaje en la pantalla OLED.

```
Bienvenido, Wayra. Te estaba esperando.
```

—Raúl... —susurró—. ¿Tocaste algo aquí?

—¡No! Te lo juro, no toqué nada. Llegué, vi el cuerpo, llamé a la policía y luego te escribí. No toqué nada.

Wayra observó el quipus físico. Tenía cuerdas de cinco colores diferentes: rojo, verde, azul, amarillo y blanco. Cada cuerda tenía nudos en posiciones específicas. Pero lo más intrigante era el código integrado en la base del quipus: una pequeña tira de fibra óptica tejida entre las cuerdas, conectada a la pantalla OLED.

—Esto no es un quipus histórico —dijo Wayra—. Es un quipus digital. Inti fusionó la tecnología textil ancestral con componentes electrónicos. Las cuerdas son los cables, los nudos son los datos.

Tomó una foto del quipus con su teléfono y comenzó a transcribir los colores y posiciones de los nudos en su laptop.

—Voy a necesitar decodificar esto. Cada color representa un tipo de información diferente. Y los nudos... los nudos son como caracteres en un string.

## La magia de los strings

Los **strings** son probablemente el tipo de dato más versátil en Python. Un string es simplemente una secuencia de caracteres: letras, números, símbolos, espacios.

Pero un string tiene "magia" oculta. Al igual que un quipus tiene nudos en posiciones específicas que dan significado a la cuerda, un string tiene caracteres en posiciones que dan significado al texto.

Wayra abrió un nuevo archivo:

```python
# ============================================
# CASO: El quipus de Inti - Decodificación
# ============================================

# El quipus tiene cuerdas de 5 colores
# Representaremos cada cuerda como un string
# donde 'n' = nudo y '-' = espacio vacío

cuerda_roja = "n--n---n----n"
cuerda_verde = "-n--n---n----n"
cuerda_azul = "n---n---n---n"
cuerda_amarilla = "--n----n----n-"
cuerda_blanca = "n-n-n-n-n-n-n"

print("=== QUIPUS FÍSICO: TRANSCRIPCIÓN ===")
print(f"Cuerda Roja:    {cuerda_roja}")
print(f"Cuerda Verde:   {cuerda_verde}")
print(f"Cuerda Azul:    {cuerda_azul}")
print(f"Cuerda Amarilla:{cuerda_amarilla}")
print(f"Cuerda Blanca:  {cuerda_blanca}")
```

Pero esto solo mostraba los patrones. Wayra necesitaba entender el mensaje. Para eso, necesitaba herramientas más poderosas.

## Slicing: Cortando el quipu

En Python, puedes acceder a cualquier carácter de un string usando `[]` con un índice. Los índices empiezan en **0**. Así como en un quipus, el primer nudo está en la "posición 0" de la cuerda.

```python
# Accediendo a posiciones específicas en la cuerda roja
print("\n--- Analizando la cuerda roja ---")
print(f"Posición 0: '{cuerda_roja[0]}'")  # 'n'
print(f"Posición 1: '{cuerda_roja[1]}'")  # '-'
print(f"Posición 2: '{cuerda_roja[2]}'")  # '-'
print(f"Posición 3: '{cuerda_roja[3]}'")  # 'n'

# Slicing: tomando porciones del string
# [inicio:fin] - el fin NO se incluye
primeros_4 = cuerda_roja[0:4]   # "n--n" (posiciones 0, 1, 2, 3)
print(f"\nPrimeros 4 caracteres: '{primeros_4}'")

# También podemos usar índices negativos
# -1 es el último carácter
ultimo = cuerda_roja[-1]
print(f"Último carácter: '{ultimo}'")

# [inicio:fin:paso]
cada_2 = cuerda_roja[0:12:2]
print(f"Cada 2 posiciones: '{cada_2}'")
```

—Interesante —murmuró Wayra—. Si tomamos cada dos posiciones en la cuerda roja, obtenemos "n-n-n-". Tres nudos separados por espacios. Como un mensaje en código.

Pero había más. Python ofrece una gran cantidad de **métodos de string** —funciones que pertenecen al string y permiten manipularlo.

## Métodos de string: Las herramientas del tejedor

Wayra recordaba a su abuela Teodora hablando de los quipus. "Cada nudo tiene un propósito", decía. "Nudo simple es un número. Nudo compuesto es una historia. Nudo en forma de 'S' es una advertencia."

Los métodos de string son como esos diferentes tipos de nudos: cada uno hace algo específico.

```python
# --- MÉTODOS DE STRING ---

mensaje_encontrado = "  EL CODIGO ESTA EN EL QUIPU BLANCO  "

# strip() - elimina espacios al inicio y final
limpio = mensaje_encontrado.strip()
print(f"Original: '{mensaje_encontrado}'")
print(f"Sin espacios: '{limpio}'")

# lower() - convierte a minúsculas
minusculas = limpio.lower()
print(f"En minúsculas: '{minusculas}'")

# upper() - convierte a mayúsculas
mayusculas = limpio.upper()
print(f"En mayúsculas: '{mayusculas}'")

# replace() - reemplaza texto
reemplazado = limpio.replace("QUIPU", "CODIGO")
print(f"Reemplazado: '{reemplazado}'")

# count() - cuenta ocurrencias
conteo_n = limpio.count("Q")
print(f"Veces que aparece 'Q': {conteo_n}")

# find() - encuentra posición
posicion = limpio.find("BLANCO")
print(f"El texto 'BLANCO' empieza en posición: {posicion}")

# len() - longitud del string (no es un método, es una función)
longitud = len(limpio)
print(f"Longitud del mensaje: {longitud} caracteres")
```

Pero el mensaje en la pantalla OLED seguía siendo un misterio. ¿Cómo sabía el sistema que ella llegaría? Wayra decidió investigar el código que generaba ese mensaje.

## Construyendo mensajes como un quipu

Inti había construido un sistema que, al detectar movimiento en el laboratorio, mostraba un mensaje personalizado. Wayra encontró el archivo fuente en la computadora:

```python
# ============================================
# Sistema de bienvenida del laboratorio
# Dr. Inti Quispe - Proyecto Yachay
# ============================================

# Nombres de posibles visitantes
visitante_1 = "policia"
visitante_2 = "Raúl"
visitante_3 = "Wayra"

# Mensaje base
saludo = "Bienvenido, {}. Te estaba esperando."

# Formateo con .format()
print(saludo.format(visitante_1))
print(saludo.format(visitante_2))
print(saludo.format(visitante_3))
```

Wayra sintió un escalofrío. No era un mensaje sobrenatural. Inti había programado el sistema para que detectara quién entraba y mostrara un saludo personalizado. Pero la pregunta era: ¿cómo sabía Inti que ella vendría?

Quizás la respuesta estaba en la cuerda blanca. Todos los quipus ceremoniales incas tenían una cuerda blanca que representaba la conexión espiritual, el puente entre el mundo físico y el digital.

## Enigmas: Decodifica el mensaje

Wayra necesita tu ayuda para decodificar completamente el quipus.

### Enigma 2.1: El mensaje oculto

Dado el siguiente string:

```python
mensaje_codificado = "ÑAN*QHAPAQ*TAMBO*WAYRA*INTI"
```

Usa métodos de string para:
1. Convertir todo a minúsculas
2. Reemplazar `*` por ` -> `
3. Encontrar en qué posición aparece "WAYRA"
4. Contar cuántas veces aparece la letra "A"
5. Mostrar la longitud total del mensaje

### Enigma 2.2: Extrayendo el nombre

Usando slicing en el string del enigma anterior, extrae solo el nombre "WAYRA". Pista: usa `find()` para encontrar dónde empieza, y luego slicing para extraerlo.

### Enigma 2.3: El quipu invertido

Los incas a veces leían los quipus de derecha a izquierda. Dado el siguiente string, inviértelo usando slicing con paso negativo:

```python
quipu_invertido = "ATAM-ATAK-AP"
```

Pista: `[::-1]` invierte un string.

---

## Lo que aprendiste

- Los **strings** son secuencias de caracteres con posiciones (índices)
- El **slicing** `[inicio:fin:paso]` permite extraer partes de un string
- Los **índices negativos** cuentan desde el final (`-1` es el último)
- Los **métodos de string**: `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.count()`, `.find()`
- `len()` devuelve la longitud de un string
- `.format()` y f-strings son formas de insertar variables en texto
- `[::-1]` invierte un string completamente

Wayra guardó su progreso y miró las cuerdas del quipus frente a ella. Los patrones empezaban a tener sentido. La cuerda blanca, la que representaba la conexión espiritual, tenía nudos intercalados: nudo, espacio, nudo, espacio... como un código binario.

—Raúl —dijo—. La cuerda blanca no es decoración. Es la clave. Cada nudo es un 1, cada espacio es un 0. Es un mensaje binario convertido en textil.

Raúl se acercó, incrédulo.

—¿Estás diciendo que Inti escribió código... en un tejido?

Wayra sonrió.

—No "en" un tejido. El tejido **es** el código. Bienvenido al mundo de los quipus digitales.

---
