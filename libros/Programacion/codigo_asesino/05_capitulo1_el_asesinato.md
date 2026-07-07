# Capítulo 1: El Asesinato en el Templo del Sol

## Conceptos: Variables, tipos de datos, `print()`, f-strings

---

Wayra Condori ajustó los auriculares y dio un sorbo a su café de muña, amargo y humeante. Frente a ella, tres monitores mostraban líneas de código en azul y verde. En el cuarto piso de un edificio casi en ruinas en el barrio de San Blas, su pequeño departamento servía también como oficina. Desde la ventana, alcanzaba a ver las luces del centro de Neo-Cusco titilando en la neblina matutina.

Eran las 6:47 a.m. cuando su teléfono vibró.

El mensaje era de su amigo Raúl, periodista de investigación en *El Sol del Cusco*:

```
Wayra, ¿viste las noticias? Mataron al Dr. Inti Quispe.
En su laboratorio. En el Templo del Sol.
La policía dice que fue un robo.
Yo digo que es mentira.
Ven. Te necesito.
```

Wayra dejó el café. Conocía a Inti Quispe de nombre —todo el mundo tecnológico de Neo-Cusco lo conocía— pero también lo conocía de una manera más personal. Su abuela, Mama Teodora, había tejido con la hermana de Inti en las comunidades altas. Y el Dr. Quispe había sido el único académico que había tratado a su abuela como una igual, no como una "informante".

Se puso la chamarra de lana de alpaca y salió. El caso ya la tenía atrapada.

---

## La escena del crimen

El laboratorio de Inti Quispe estaba en el ala este del Coricancha, el antiguo Templo del Sol. Pero no era un templo cualquiera: la estructura original inca servía ahora como base para un centro de investigación de última generación. Muros de piedra perfectamente ensamblada sostenían paredes de vidrio inteligente. El suelo de la época imperial había sido cubierto con paneles táctiles.

Wayra llegó y encontró a Raúl esperándola afuera.

—No te voy a mentir —dijo Raúl en voz baja—. Esto es más grande de lo que parece. Inti estaba trabajando en algo llamado "Proyecto Yachay". Una IA que... bueno, nadie sabe exactamente qué hace. Pero ayer recibió un mensaje. Y hoy está muerto.

—¿Qué mensaje? —preguntó Wayra.

—Eso es lo que necesito que descubras. Vamos.

Entraron. El laboratorio era un desorden controlado: papeles, cables, una computadora central con tres monitores. En el monitor principal, una ventana de terminal mostraba algo que parecía un mensaje.

Raúl tomó una foto con su teléfono y se la envió a Wayra.

—Mira esto. Es lo único que dejaron. Un código.

Wayra miró la foto. En la pantalla se leía:

```
quipu_digital_001 = "Ñan:1:3:5:7:9"
print(quipu_digital_001)
```

—Esto no tiene sentido... —murmuró Wayra.

—Por eso te llamé. Dijiste que el código habla, ¿no?

Wayra sonrió. En efecto, el código habla. Y este código acababa de decirle algo importante.

---

## Python: La primera conversación

Antes de entender el mensaje, Wayra necesitaba establecer los fundamentos. En Python, todo comienza con las **variables**. Piensa en una variable como una caja donde guardas información. Esa información puede ser de diferentes **tipos**:

- **Números enteros** (`int`): como la edad de alguien o la cantidad de pistas
- **Números decimales** (`float`): como una coordenada o una probabilidad
- **Texto** (`str`): como un nombre o un mensaje cifrado
- **Booleanos** (`bool`): `True` o `False`, como una respuesta de sí o no

Y la forma más básica de ver qué contiene una variable es con `print()`.

Wayra abrió su laptop y comenzó a escribir.

```python
# ============================================
# CASO: El asesinato del Dr. Inti Quispe
# Analista: Wayra Condori
# Fecha: 27 de junio, 2026
# ============================================

# --- DATOS BÁSICOS DEL CASO ---

nombre_victima = "Dr. Inti Quispe"
edad_victima = 67
lugar_crimen = "Templo del Sol (Coricancha)"
hora_descubrimiento = "06:30"
puerta_cerrada = True
tiene_herederos = False

print("=== INFORME INICIAL ===")
print("Víctima:", nombre_victima)
print("Edad:", edad_victima)
print("Lugar:", lugar_crimen)
print("Hora del descubrimiento:", hora_descubrimiento)
print("Puerta cerrada por dentro:", puerta_cerrada)
```

Al ejecutar, la terminal mostró:

```
=== INFORME INICIAL ===
Víctima: Dr. Inti Quispe
Edad: 67
Lugar: Templo del Sol (Coricancha)
Hora del descubrimiento: 06:30
Puerta cerrada por dentro: True
```

Pero había una forma más elegante de mostrar esa información. Python 3.6+ tiene los **f-strings** (cadenas formateadas), que permiten insertar variables directamente dentro del texto:

```python
print(f"La víctima es {nombre_victima}, de {edad_victima} años.")
print(f"El crimen ocurrió en {lugar_crimen} a las {hora_descubrimiento}.")
```

Resultado:

```
La víctima es Dr. Inti Quispe, de 67 años.
El crimen ocurrió en Templo del Sol (Coricancha) a las 06:30.
```

## El primer quipu digital

Wayra volvió al mensaje que había visto en la pantalla:

```python
quipu_digital_001 = "Ñan:1:3:5:7:9"
print(quipu_digital_001)
```

—¿Qué significa "Ñan"? —preguntó Raúl.

—"Ñan" significa "camino" o "ruta" en quechua —respondió Wayra—. Y los números separados por dos puntos... son posiciones. Son nudos en un camino.

—¿Nudos?

—Los quipus, Raúl. Inti estaba dejando un mensaje con el sistema de sus ancestros. Cada número representa un nudo en una cuerda. La posición del nudo, el tipo de nudo, la dirección... todo tiene significado.

Wayra escribió un nuevo script:

```python
# Decodificando el quipu digital
quipu_mensaje = "Ñan:1:3:5:7:9"
print(f"Mensaje original del quipu: {quipu_mensaje}")

# Separamos los elementos por los dos puntos
elementos = quipu_mensaje.split(":")
print(f"Elementos separados: {elementos}")

# El primer elemento es el tipo de quipu
tipo_quipu = elementos[0]
print(f"Tipo de camino: {tipo_quipu}")

# Los siguientes son las posiciones de los nudos
nudos = elementos[1:]
print(f"Posiciones de nudos: {nudos}")
```

—Este quipu dice "Camino: 1, 3, 5, 7, 9" —explicó Wayra—. Son números impares. En la numeración inca, los impares representan... preguntas. Un camino de preguntas.

—¿Un camino de preguntas? ¿Qué tipo de preguntas?

Wayra señaló la pantalla.

—Eso es lo que vamos a descubrir. Pero primero, necesito más datos.

## Tu primer enigma

Antes de seguir, tienes que practicar lo que Wayra acaba de aprender.

### Enigma 1.1: La ficha del caso

Crea un programa que guarde en variables los siguientes datos del caso y los muestre usando `print()` y f-strings:

- **Nombre del sospechoso:** Lara Mamani
- **Edad:** 32 años
- **Rol:** Asistente de laboratorio
- **Coartada:** "Estaba en mi departamento"
- **Tiene acceso al laboratorio:** `True`

El output debe verse así:

```
=== FICHA DE SOSPECHOSO ===
Nombre: Lara Mamani
Edad: 32
Rol: Asistente de laboratorio
Coartada: Estaba en mi departamento
Acceso: True
```

### Enigma 1.2: El mensaje cifrado

El Dr. Inti dejó otro mensaje. Este quipu dice:

```
quipu_digital_002 = "Yachay:2:4:6:8:10"
```

Modifica el código de decodificación para trabajar con este nuevo quipu. ¿Qué observas? Los números ya no son impares. En la numeración inca, los pares representan **respuestas**. ¿Qué podría significar?

### Enigma 1.3: Tu propia variable

Crea una variable llamada `mi_teoria` que contenga un texto con tu primera teoría sobre el caso. Luego muéstrala con `print()`. Ejemplo:

```python
mi_teoria = "Creo que el asesino conocía a Inti y tenía acceso al laboratorio"
print(f"Mi teoría inicial: {mi_teoria}")
```

---

[Facilito] → Soluciones en el Apéndice al final del libro.

---

## Lo que aprendiste

- Las **variables** guardan información en la memoria del computador
- Los **tipos de datos básicos** son: `int` (entero), `float` (decimal), `str` (texto), `bool` (booleano)
- `print()` muestra información en la pantalla
- Los **f-strings** (`f"texto {variable}"`) permiten incrustar variables en texto
- Los quipus digitales usan el formato `"Tipo:num1:num2:num3"` para codificar mensajes
- `.split()` separa un string en una lista usando un delimitador

Wayra guardó el archivo y miró a Raúl.

—Necesito ver el quipu original. El físico. El que Inti tenía en su escritorio.

Raúl asintió y la guió hacia el interior del laboratorio. Pero cuando llegaron al escritorio de Inti, algo los detuvo.

Sobre la madera tallada a mano, junto a una taza de café frío, había un quipus real: cuerdas de lana de vicuña de varios colores, con nudos en posiciones precisas. Pero no era un quipus histórico. Al lado, una pequeña pantalla OLED mostraba un código que parpadeaba lentamente.

Wayra se inclinó para leerlo y su sangre se heló.

El código decía:

```python
print("Bienvenido, Wayra. Te estaba esperando.")
```

Alguien sabía que ella vendría.

---
