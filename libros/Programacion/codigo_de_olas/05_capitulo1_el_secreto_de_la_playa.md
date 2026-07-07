# Capítulo 1: El Secreto de la Playa

## Conceptos: Variables, tipos de datos, `print()`, f-strings

---

Mateo Sánchez remó contra la corriente. Eran las 6:15 a.m. y el sol apenas comenzaba a teñir de naranja el horizonte del Pacífico. Desde su tabla, Ancón se veía distinto: el muelle de piedra alargándose como un brazo dormido, las caletas vacías, las casas de colores subiendo por el cerro.

Era su rutina. Madrugar, revisar el parte de olas en su teléfono, y meterse al agua antes de que el viento arruinara la superficie.

Pero hoy algo era diferente.

La ola que venía no se comportaba como debía. Rompió en un punto extraño, demasiado perfecto. Como si alguien hubiera trazado una línea recta en el agua.

—¿Viste eso? —le gritó su amigo Rafa, desde la orilla.

—Lo vi —respondió Mateo—. Parece... código.

—¿Código?

—Como cuando programo. Patrones. Esto no es natural.

Mateo guardó silencio. Desde pequeño había sido el raro: surfista y programador. Mientras sus amigos veían YouTube, él aprendía Python en una laptop prestada de la biblioteca municipal de Ancón. Mientras ellos salían de fiesta, él se quedaba descifrando APIs.

Y ahora, el mar le estaba hablando en el único idioma que entendía: datos.

---

## La primera ola digital

Mateo salió del agua, tomó su laptop y comenzó a escribir. Lo primero: entender qué datos tenía.

En Python, todo comienza con **variables**. Son como cajas donde guardas información del mundo real. Esa información tiene un **tipo**: números, texto, booleanos.

```python
# ============================================
# OLA DIGITAL: ANÁLISIS DE PATRONES
# Surfista: Mateo Sánchez
# Fecha: 27 de junio, 2026
# ============================================

# --- DATOS DE LA OLA ---

nombre_playa = "Ancón"
hora_observacion = "06:15"
altura_ola = 1.8  # metros
frecuencia_ola = 12  # segundos entre olas
temperatura_agua = 18.5  # grados Celsius
direccion_viento = "sur-oeste"
es_anomalia = True

print("=== INFORME DE OLA ===")
print("Playa:", nombre_playa)
print("Hora:", hora_observacion)
print("Altura:", altura_ola, "metros")
print("Frecuencia:", frecuencia_ola, "segundos")
print("Anomalía detectada:", es_anomalia)
```

Pero la forma más elegante de mostrar datos en Python es con **f-strings**:

```python
print(f"\n--- Resumen ---")
print(f"Playa {nombre_playa} a las {hora_observacion}")
print(f"Ola de {altura_ola}m cada {frecuencia_ola} segundos")
print(f"¿Anomalía? {es_anomalia}")
```

## El primer patrón

Mateo observó los datos más de cerca. La ola no solo era extraña: tenía una firma. Como una variable en Python que guarda un valor específico, la ola guardaba información en su estructura.

—Si la ola fuera una variable —murmuró—, tendría un nombre, un tipo y un valor.

Anotó en su laptop:

```python
# --- TIPOS DE DATOS DE LA OLA ---

nombre_ola = "Ancón_01"          # str - texto
altura_maxima = 2.4               # float - decimal
frecuencia_segundos = 12          # int - entero
es_generada_artificialmente = True # bool - booleano (True/False)

print(f"\nOla: {nombre_ola}")
print(f"Tipo de nombre_ola: {type(nombre_ola)}")
print(f"Tipo de altura_maxima: {type(altura_maxima)}")
print(f"Tipo de frecuencia_segundos: {type(frecuencia_segundos)}")
print(f"Tipo de es_generada: {type(es_generada_artificialmente)}")
```

El resultado le confirmó algo: la ola tenía datos medibles. Pero necesitaba más. Necesitaba el parte de olas completo.

## El parte de olas digital

El amigo de Mateo, Rafa, trabajaba en la Capitanía del Puerto de Ancón. Tenía acceso a los datos históricos de oleaje. Llamó por teléfono:

—Rafa, ¿me puedes pasar los datos de las últimas 48 horas?

—¿Para qué?

—Hay algo raro en el agua. Las olas tienen patrones que se repiten. Como código binario.

—Estás loco.

—Puede ser. Pero pásame los datos.

Rafa le envió un archivo. Mateo lo abrió y comenzó a analizarlo:

```python
# --- PARTE DE OLAS DE ANCÓN ---

fecha_parte = "27-06-2026"
total_olas_registradas = 147
ola_mas_alta = 2.8
ola_promedio = 1.6
direccion_olas = "SO"

print(f"\n=== PARTE DE OLAS: {fecha_parte} ===")
print(f"Total de olas: {total_olas_registradas}")
print(f"Ola más alta: {ola_mas_alta}m")
print(f"Promedio: {ola_promedio}m")
print(f"Dirección: {direccion_olas}")

# Porcentaje de olas anómalas
total_anomalias = 23
porcentaje = (total_anomalias / total_olas_registradas) * 100
print(f"Anomalías: {total_anomalias} ({porcentaje:.1f}%)")
```

—23 anomalías en 48 horas —dijo Mateo—. Eso es demasiado. En un mar natural, las anomalías son menos del 5%. Aquí estamos en 15.6%.

Alguien está generando olas artificiales. Y esas olas están codificando algo.

## Tu primer enigma

### Enigma 1.1: Tu parte de olas

Crea variables para los siguientes datos de una playa:
- `nombre_playa`: "Ancón Norte"
- `temperatura_agua`: 19.2
- `altura_ola`: 2.1
- `es_segura`: True
- `hora_medicion`: "07:30"

Muéstralos con `print()` y f-strings.

### Enigma 1.2: Calcula el promedio

Tienes 5 alturas de ola: 1.5, 2.0, 1.8, 2.2, 1.9. Calcula el promedio y muéstralo. Pista: suma las alturas y divide entre 5.

### Enigma 1.3: La ola binaria

El patrón de la ola se codifica así: `"1.8:0.5:2.1"` (altura:frecuencia:velocidad). Separa los valores usando `.split(":")` y muestra cada uno por separado.

---

## Lo que aprendiste

- Las **variables** guardan información en la memoria
- Los **tipos básicos** son: `int`, `float`, `str`, `bool`
- `print()` muestra datos en pantalla
- Los **f-strings** (`f"texto {variable}"`) incrustan variables en texto
- `type()` revela el tipo de una variable
- `.split()` separa texto en partes

Mateo cerró su laptop. Tenía datos. Tenía patrones. Pero lo más inquietante estaba por venir.

Cuando revisó el parte de olas más detenidamente, notó que las anomalías seguían un patrón horario: ocurrían exactamente cada 3 horas. Como si un programa estuviera ejecutando un bucle.

—Alguien está programando el mar —dijo en voz alta—. Y voy a descubrir quién.

---
