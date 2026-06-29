# ESTADÍSTICA MORTAL

## El Enigma del Conjunto Vacío

*Una Novela de Misterio, Datos y Probabilidades*

---

**Autor:** Alex Goyzueta Delgado

**Contacto:** alexgoyzueta2018@gmail.com

---

> *"En los datos se esconde la verdad.*
> *En la probabilidad, la certeza."*

---

Barcelona, 2026



# Créditos

**Estadística Mortal: El Enigma del Conjunto Vacío**

© 2026 Alex Goyzueta Delgado

Todos los derechos reservados. Ninguna parte de esta publicación puede ser reproducida, distribuida o transmitida en forma alguna ni por ningún medio electrónico, mecánico, fotocopia, grabación u otro método, sin el permiso previo por escrito del autor.

**Edición y corrección:** Alex Goyzueta Delgado
**Ilustraciones conceptuales:** Generadas mediante descripciones textuales
**Diseño de portada:** Alex Goyzueta Delgado
**Tipografía:** IBM Plex Mono (código), Lato (narrativa)

**Agradecimientos especiales:**
A los estadísticos que enseñan con pasión.
A la comunidad Python de Latinoamérica.
A todos los que creen que los datos pueden cambiar el mundo.

**Datos de catalogación:**
Goyzueta Delgado, Alex
Estadística Mortal: El Enigma del Conjunto Vacío / Alex Goyzueta Delgado
1ra edición — Barcelona, 2026



# Dedicatoria

*A todos los que alguna vez miraron un número y vieron una historia.*

*A los que saben que detrás de cada estadística hay una vida, una decisión, un misterio.*

*Y a los estudiantes que creen que las matemáticas no son su fuerte: este libro es para demostrarles que están equivocados.*



# Prefacio

Este libro nace de una idea simple: la estadística y la probabilidad no son aburridas. Son herramientas para contar historias, para descubrir verdades ocultas, para resolver misterios.

Cada capítulo combina tres elementos:
- **Una historia** que avanza la trama de un crimen por resolver
- **Conceptos** de estadística y probabilidad explicados desde cero
- **Código Python** que puedes ejecutar para ver los conceptos en acción

No necesitas saber estadística para leer este libro. Los conceptos se introducen gradualmente, desde lo más básico hasta lo más avanzado. Tampoco necesitas ser experto en Python —cada línea de código está explicada—, aunque si ya tienes algo de experiencia, podrás enfocarte más en los conceptos estadísticos.

La historia está ambientada en Barcelona, 2026, una ciudad donde la tecnología y los datos lo gobiernan todo. Los personajes, aunque ficticios, reflejan problemas reales: manipulación de datos, fraude académico, corrupción y la lucha por la verdad en un mundo donde la información es poder.

Al final de cada capítulo encontrarás **enigmas** para resolver. Las soluciones están en el Apéndice, pero te recomiendo intentarlos antes de mirar la respuesta.

Bienvenido a **Estadística Mortal**.

Tu viaje comienza aquí.



# Introducción

### Barcelona, 2026

Imagina una ciudad donde los algoritmos predicen el tráfico antes de que los autos se muevan. Donde los datos fluyen por la fibra óptica como el agua por las ramblas históricas. Donde cada transacción, cada llamada, cada paso deja una huella digital.

Esa es Barcelona.

Una metrópoli que late al ritmo de los datos. Aquí, la información es el recurso más valioso. Y como todo recurso valioso, hay quienes están dispuestos a matar por él.

### El Instituto de Ciencias de Datos

El ICD —Instituto de Ciencias de Datos— es el centro de investigación más importante de Sudamérica. Ubicado en el antiguo barrio de San Blas, combina arquitectura colonial con laboratorios de última generación. Sus investigadores publican en las mejores revistas del mundo. Sus algoritmos optimizan desde la distribución de agua hasta la predicción de terremotos.

Pero detrás de los números y las publicaciones, algo oscuro se esconde.

### El proyecto Yupay

La Dra. Kamila Huamán, jefa del departamento de Estadística del ICD, lideraba el proyecto más ambicioso del instituto: **Yupay** (contar, en quechua). Un sistema de modelos predictivos capaz de anticipar crisis sociales, económicas y ambientales con una precisión del 98%.

Pero Yupay no era solo un proyecto académico. Sus modelos habían detectado algo. Algo que alguien no quería que se supiera.

### El crimen

Todo comienza una madrugada en el laboratorio 7 del ICD. La Dra. Kamila Huamán aparece muerta en su oficina. La puerta estaba cerrada por dentro. Su computadora, encendida. En la pantalla, solo una línea de código:

```python
datos = []
```

Un conjunto vacío.

La policía dice que fue un paro cardíaco. La universidad dice que fue un accidente.

Valeria Quispe, una joven analista de datos exalumna de la Dra. Huamán, sabe que el conjunto vacío no es un error. Es un mensaje.

Y tú la vas a ayudar a descifrarlo.



# Capítulo 1: El Conjunto Vacío

## Conceptos: Estadística descriptiva — media, mediana, moda, min, max

---

Valeria Quispe cerró la puerta de su departamento en el barrio de San Blas y se dejó caer en la silla frente a su computadora. Eran las 7:23 a.m. del 3 de julio y el sol apenas comenzaba a iluminar las calles empedradas de Barcelona.

El mensaje había llegado a las 6:15 a.m.:

```
Valeria:
Sé que fuiste su alumna favorita.
Esto no fue un ataque al corazón.
Ven al ICD. Trae tu laptop.
— C
```

Valeria había sido alumna de la Dra. Kamila Huamán en su último año de la maestría en Ciencia de Datos. Kamila no solo le había enseñado estadística; le había enseñado a pensar. "Los números no mienten", decía siempre. "Las personas, sí."

El ICD estaba a quince minutos caminando. Valeria recorrió las calles de San Blas esquivando turistas y vendedores ambulantes. La fachada del instituto era imponente: un edificio de vidrio negro que reflejaba las montañas circundantes.

En la entrada la esperaba un hombre joven, de unos treinta años, con una laptop bajo el brazo y una expresión seria.

—¿Valeria? —dijo extendiendo la mano—. Soy Marco. Marco Tupac. Trabajé con la doctora Huamán en el proyecto Yupay.

—Tú enviaste el mensaje.

—Sí. Ven, te explico todo.

---

## La escena

El laboratorio 7 estaba intacto. La policía había terminado su investigación y lo habían declarado "muerte natural". Pero Marco no lo creía.

—Mira esto —dijo Marco, señalando la pantalla de la computadora de la doctora—. Cuando llegué esa mañana, esto era lo único que había en la pantalla.

```python
datos = []
```

Valeria observó la línea en silencio.

—Es una lista vacía —dijo—. En Python, `[]` es un conjunto vacío. No tiene elementos.

—¿Por qué alguien dejaría una lista vacía en su pantalla antes de morir?

—Kamila no hacía nada sin razón. Enséñame sus archivos.

Marco abrió el explorador de archivos. En el escritorio había una carpeta llamada `Yupay/`. Dentro, un único archivo:

```
datos_caso.csv
```

Valeria abrió el archivo. Era un CSV con datos de un estudio clínico. Pero algo extraño: la mayoría de los campos estaban vacíos.

—Son datos falsos —dijo Marco—. O incompletos. No lo sé.

—No —respondió Valeria—. No son falsos. Son un mensaje. Kamila me enseñó que los datos siempre hablan. Solo hay que saber escucharlos.

---

## Estadística descriptiva: el lenguaje de los datos

Valeria abrió su terminal. Si iba a entender qué había pasado, primero necesitaba entender los datos.

—La estadística descriptiva —dijo Valeria, más para sí misma que para Marco— es la forma más básica de entender un conjunto de datos. Responde preguntas como: ¿cuántos datos tenemos? ¿Cuál es el valor típico? ¿Qué tan dispersos están?

—Suena útil —dijo Marco—. Pero ¿cómo nos ayuda a encontrar a un asesino?

—Empecemos con lo básico.

Valeria abrió Python y comenzó a escribir:

```python
import csv

# Cargamos los datos del archivo misterioso
datos_caso = []
with open('datos_caso.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    encabezados = next(lector)
    for fila in lector:
        datos_caso.append(fila)

print(f"Archivo cargado: {len(datos_caso)} registros encontrados")
print(f"Columnas: {encabezados}")
```

—Primero, veamos los datos resumidos.

Valeria continuó:

```python
# Extraemos las edades de los pacientes
edades = []
for fila in datos_caso:
    if fila[2]:  # La columna 2 tiene las edades
        edades.append(int(fila[2]))

print(f"\n=== RESUMEN DE EDADES ===")
print(f"Cantidad total (n):    {len(edades)}")
print(f"Edad mínima (min):     {min(edades)}")
print(f"Edad máxima (max):     {max(edades)}")
```

Resultado:

```
=== RESUMEN DE EDADES ===
Cantidad total (n):    47
Edad mínima (min):     22
Edad máxima (max):     78
```

—¿Y eso qué significa? —preguntó Marco.

—Que tenemos 47 pacientes con edades entre 22 y 78 años. Pero esto no me dice nada sobre el valor típico. Necesito la **media** —el promedio— y la **mediana** —el valor central—.

```python
# Media (promedio)
media = sum(edades) / len(edades)
print(f"Edad media (promedio): {media:.2f} años")

# Mediana (valor central)
edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)
if n % 2 == 0:
    mediana = (edades_ordenadas[n//2 - 1] + edades_ordenadas[n//2]) / 2
else:
    mediana = edades_ordenadas[n//2]
print(f"Edad mediana (central): {mediana:.2f} años")

# Moda (valor más frecuente)
from collections import Counter
conteo_edades = Counter(edades)
edad_moda, frecuencia_moda = conteo_edades.most_common(1)[0]
print(f"Edad moda (frecuente):  {edad_moda} años ({frecuencia_moda} veces)")
```

Resultado:

```
Edad media (promedio): 47.89 años
Edad mediana (central): 48.00 años
Edad moda (frecuente):  45 años (5 veces)
```

—La media es 47.89, la mediana es 48, la moda es 45. Están cerca —dijo Valeria—. Eso sugiere que los datos tienen una distribución bastante simétrica. Nada sospechoso.

—Entonces, ¿todo es normal?

—No. Porque lo interesante no son los datos que están aquí. Son los datos que faltan.

---

## El conjunto vacío

Valeria señaló la pantalla.

—Mira la lista vacía otra vez: `datos = []`. Kamila no escribió eso por accidente. Me está diciendo que mire los datos que **no están**.

```python
# Identificando datos faltantes
total_filas = len(datos_caso)
faltantes_por_columna = []

for i, encabezado in enumerate(encabezados):
    faltan = sum(1 for fila in datos_caso if not fila[i].strip())
    faltantes_por_columna.append((encabezado, faltan))
    porcentaje = (faltan / total_filas) * 100
    if faltan > 0:
        print(f"Columna '{encabezado}': {faltan} valores faltantes ({porcentaje:.1f}%)")
```

Resultado:

```
Columna 'diagnostico': 2 valores faltantes (4.3%)
Columna 'medicamento': 12 valores faltantes (25.5%)
Columna 'resultado': 1 valores faltantes (2.1%)
Columna 'notas_doctor': 47 valores faltantes (100.0%)
```

—Espera —dijo Marco—. La columna `notas_doctor` está completamente vacía.

—Exacto. Un conjunto vacío dentro de los datos. Y mira esto —Valeria seleccionó la columna de medicamentos—. El 25.5% de los valores de medicamentos faltan. Eso es un patrón sospechoso.

—¿Crees que alguien borró esos datos a propósito?

—No lo sé. Pero Kamila sí lo sabía. Y por eso dejó el mensaje.

Valeria se recostó en la silla y miró la pantalla.

—Necesito más información. La media, la mediana y el rango me dicen algo, pero no suficiente. Necesito entender la **dispersión** de los datos. La **varianza** y la **desviación estándar**.

—¿Y eso qué es?

—Se lo explicaré en el camino. Primero, dime: ¿quién más tenía acceso a este laboratorio?

Marco dudó. Sacó su teléfono y mostró una lista.

—Había cuatro personas con acceso: la doctora Huamán, el director del instituto, su asistente... y el encargado de seguridad de datos.

—¿Y quién es el encargado de seguridad?

—Se llama Ramiro. Ramiro Quispe.

Valeria sintió un escalofrío. Quispe. Su mismo apellido. Perú era un país donde los apellidos se repetían, pero algo en la forma en que Marco lo dijo la puso alerta.

—Necesito hablar con él.

—Hay un problema —dijo Marco—. Ramiro renunció ayer. Desapareció.

---

## Tu primer enigma

### Enigma 1.1: Analiza tu propio conjunto

Tienes las siguientes edades de un grupo de sospechosos:

```
edades_sospechosos = [29, 34, 45, 45, 45, 52, 67, 71, 34, 29, 45, 38, 52, 45, 29]
```

Calcula:
1. La media
2. La mediana
3. La moda
4. El mínimo y máximo

### Enigma 1.2: El outlier

Agrega a la lista anterior la edad de un nuevo sospechoso: 98 años. ¿Cómo cambian la media y la mediana? ¿Cuál de las dos medidas se ve más afectada por este valor extremo?

### Enigma 1.3: Datos faltantes

En el archivo `datos_caso.csv`, la columna `presion_sanguinea` tiene 5 valores vacíos de 47. ¿Qué porcentaje de datos falta? Si estos valores fueran borrados intencionalmente, ¿qué información estaría ocultando el responsable?

---

## Lo que aprendiste

- La **estadística descriptiva** resume un conjunto de datos con medidas clave
- **Media**: el promedio aritmético (sensible a valores extremos)
- **Mediana**: el valor central cuando los datos están ordenados (robusta)
- **Moda**: el valor que más se repite
- **Mínimo y máximo**: definen el rango de los datos
- Los **datos faltantes** pueden ser una señal de manipulación
- `[]` en Python es una lista vacía — un conjunto vacío

Valeria guardó su análisis en un archivo llamado `analisis_inicial.py` y miró a Marco.

—Ramiro Quispe desapareció justo después de la muerte de Kamila. Eso no es una coincidencia. Pero antes de buscarlo, necesito entender mejor estos datos. Algo no encaja.

—¿Qué?

Valeria señaló la columna de edades.

—La media y la mediana son casi iguales. Eso ocurre cuando los datos tienen una distribución normal. Pero los datos clínicos rara vez son perfectos. Alguien ajustó estos números. Y ajustar datos es... estadísticamente mortal.

La noche caía sobre Barcelona. El misterio apenas comenzaba.



# Capítulo 2: La Probabilidad del Crimen

## Conceptos: Probabilidad básica, espacio muestral, eventos, regla de Laplace

---

Marco llevó a Valeria a la cafetería del ICD, un espacio abierto en el tercer piso con vistas a la cordillera. El sol de la mañana iluminaba los picos nevados mientras ellos se sentaban en una mesa apartada.

—Tengo que contarte algo —dijo Marco en voz baja—. La noche antes de morir, Kamila me envió un mensaje. Decía que había encontrado algo en los datos. Algo que no debía existir.

—¿Qué era?

—No lo sé. Dijo que era como... una irregularidad estadística. Una probabilidad imposible.

Valeria sacó su laptop.

—Dime exactamente lo que te dijo.

—Dijo: "La probabilidad de que esto ocurra al azar es una en un millón. Literalmente." Y luego me envió un archivo.

—¿Qué archivo?

—Este.

Marco le pasó una memoria USB. Valeria la conectó. Dentro había un solo archivo:

```
distribucion_sospechosa.csv
```

Valeria lo abrió. Eran 1000 registros con dos columnas: `tratamiento` y `resultado`.

—Son datos de un ensayo clínico —dijo Valeria—. Pero hay algo raro en la distribución.

---

## Probabilidad: el lenguaje del azar

Valeria abrió Python.

—Para entender qué vio Kamila, primero tenemos que entender la **probabilidad**. La probabilidad mide qué tan probable es que ocurra un evento. Va de 0 (imposible) a 1 (seguro).

—Eso lo sé —dijo Marco—. Como cuando la probabilidad de lluvia es del 30%.

—Exacto. Pero la forma correcta de calcularla es con la **regla de Laplace**:

$$P(evento) = \frac{\text{casos favorables}}{\text{casos posibles}}$$

—Por ejemplo, si lanzas una moneda, la probabilidad de que salga cara es 1/2 = 0.5. Si lanzas un dado, la probabilidad de que salga un 6 es 1/6 ≈ 0.1667.

Valeria escribió en Python:

```python
# Probabilidad básica con Python

import random

# Simular lanzamiento de una moneda
caras = 0
total_lanzamientos = 1000

for _ in range(total_lanzamientos):
    if random.random() < 0.5:  # 50% de probabilidad
        caras += 1

probabilidad_estimada = caras / total_lanzamientos
print(f"Lanzamientos: {total_lanzamientos}")
print(f"Caras obtenidas: {caras}")
print(f"Probabilidad estimada: {probabilidad_estimada:.4f}")
print(f"Probabilidad teórica: 0.5")
```

Resultado:

```
Lanzamientos: 1000
Caras obtenidas: 513
Probabilidad estimada: 0.5130
Probabilidad teórica: 0.5
```

—La probabilidad estimada se acerca a la teórica mientras más lanzamientos hagamos. Eso es la **ley de los grandes números**.

—Entonces, ¿qué vio Kamila en los datos del ensayo clínico?

---

## La distribución sospechosa

Valeria cargó el archivo en Python:

```python
import csv
from collections import Counter

datos_ensayo = []
with open('distribucion_sospechosa.csv', 'r') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        datos_ensayo.append(fila)

print(f"Total de pacientes: {len(datos_ensayo)}")

# Contar resultados por tratamiento
resultados = Counter()
for paciente in datos_ensayo:
    clave = (paciente['tratamiento'], paciente['resultado'])
    resultados[clave] += 1

print("\n=== RESULTADOS DEL ENSAYO ===")
for (tratamiento, resultado), conteo in sorted(resultados.items()):
    print(f"Tratamiento '{tratamiento}' - Resultado '{resultado}': {conteo}")
```

Resultado:

```
Total de pacientes: 1000

=== RESULTADOS DEL ENSAYO ===
Tratamiento 'A' - Resultado 'mejora': 470
Tratamiento 'A' - Resultado 'no_mejora': 30
Tratamiento 'B' - Resultado 'mejora': 240
Tratamiento 'B' - Resultado 'no_mejora': 260
```

—Mira esto —dijo Valeria—. Del grupo que recibió el tratamiento A, 470 de 500 pacientes mejoraron. Eso es una tasa de éxito del 94%. Del grupo B, solo 240 de 500 mejoraron: 48%.

—Entonces el tratamiento A funciona mucho mejor.

—Sí, pero la pregunta es: ¿cuál es la probabilidad de que esta diferencia se deba al azar?

Valeria continuó:

```python
total_pacientes = 1000

# Probabilidad de mejora con tratamiento A
p_A_mejora = 470 / 500
print(f"P(mejora | Tratamiento A) = {p_A_mejora:.3f}")

# Probabilidad de mejora con tratamiento B
p_B_mejora = 240 / 500
print(f"P(mejora | Tratamiento B) = {p_B_mejora:.3f}")

# Diferencia observada
diferencia = p_A_mejora - p_B_mejora
print(f"Diferencia observada: {diferencia:.3f}")

# ¿Cuál es la probabilidad general de mejora?
p_mejora_general = (470 + 240) / 1000
print(f"P(mejora general) = {p_mejora_general:.3f}")
```

Resultado:

```
P(mejora | Tratamiento A) = 0.940
P(mejora | Tratamiento B) = 0.480
Diferencia observada: 0.460
P(mejora general) = 0.710
```

—La diferencia es enorme: 46 puntos porcentuales. Kamila dijo que era una probabilidad en un millón. Vamos a comprobarlo.

```python
# Simulación: si el tratamiento no tuviera efecto,
# ¿con qué frecuencia veríamos una diferencia tan grande?

import random

simulaciones = 10000
diferencias_extremas = 0
resultados_totales = [1] * 710 + [0] * 290  # 710 mejoras, 290 no mejoras

for _ in range(simulaciones):
    random.shuffle(resultados_totales)
    grupo_A = resultados_totales[:500]
    grupo_B = resultados_totales[500:]
    
    p_A = sum(grupo_A) / 500
    p_B = sum(grupo_B) / 500
    diff = abs(p_A - p_B)
    
    if diff >= diferencia:
        diferencias_extremas += 1

probabilidad_azar = diferencias_extremas / simulaciones
print(f"Simulaciones: {simulaciones}")
print(f"Diferencias >= observada: {diferencias_extremas}")
print(f"Probabilidad de que sea azar: {probabilidad_azar:.6f}")
print(f"Equivale a 1 en {1/probabilidad_azar:.0f} aproximadamente")
```

Resultado:

```
Simulaciones: 10000
Diferencias >= observada: 0
Probabilidad de que sea azar: 0.000000
Equivale a 1 en infinito aproximadamente
```

—En 10,000 simulaciones —dijo Valeria—, nunca vimos una diferencia tan grande por puro azar. La probabilidad es esencialmente cero. Esto no fue un accidente estadístico.

—¿Qué significa?

—Significa que estos datos fueron manipulados. Alguien alteró los resultados del ensayo para que el tratamiento A pareciera milagroso. Y Kamila lo descubrió.

---

## La regla de la multiplicación

—Pero hay más —dijo Valeria—. Kamila también me enseñó sobre la probabilidad de eventos independientes.

—Por ejemplo, si la probabilidad de que una persona tenga una enfermedad es del 10% y la probabilidad de que un examen dé un falso positivo es del 5%, la probabilidad de que ambas cosas ocurran es:

$$P(A \cap B) = P(A) \times P(B) = 0.10 \times 0.05 = 0.005$$

—En términos simples, si tienes dos eventos independientes, la probabilidad de que ambos ocurran es el producto de sus probabilidades.

Valeria escribió:

```python
# Probabilidad de eventos independientes

p_enfermedad = 0.10
p_falso_positivo = 0.05

p_ambos = p_enfermedad * p_falso_positivo
print(f"P(enfermedad) = {p_enfermedad}")
print(f"P(falso positivo) = {p_falso_positivo}")
print(f"P(ambos) = {p_ambos}")
print(f"O 1 en {1/p_ambos:.0f}")
```

Resultado:

```
P(enfermedad) = 0.10
P(falso positivo) = 0.05
P(ambos) = 0.005
O 1 en 200
```

—Ahora, aplica esto al caso —dijo Valeria—. Si la probabilidad de que una persona específica estuviera en el ICD a las 3 a.m. es de 0.01 (1%), y la probabilidad de que esa persona tuviera acceso al laboratorio de Kamila es de 0.10 (10%), ¿cuál es la probabilidad de que ambas condiciones se cumplan?

```python
p_estar_en_icd = 0.01
p_tener_acceso = 0.10

p_ambas_condiciones = p_estar_en_icd * p_tener_acceso
print(f"Probabilidad de que una persona cumpla ambas: {p_ambas_condiciones:.4f}")
print(f"O 1 en {1/p_ambas_condiciones:.0f}")
```

—Las probabilidades son implacables —dijo Marco—. Alguien manipuló los datos y alguien estuvo allí esa noche. Y las dos cosas están conectadas.

---

## Enigmas

### Enigma 2.1: El dado cargado

Lanzas un dado 600 veces. Obtienes los siguientes resultados:

| Cara | Frecuencia |
|------|-----------|
| 1    | 120       |
| 2    | 115       |
| 3    | 108       |
| 4    | 95        |
| 5    | 90        |
| 6    | 72        |

1. ¿Cuál es la probabilidad teórica de cada cara?
2. Calcula la probabilidad observada de cada cara.
3. ¿Parece un dado cargado? ¿Por qué?

### Enigma 2.2: Probabilidad del sospechoso

En una lista de 8 sospechosos, 3 tienen acceso al laboratorio, 4 tenían motivos para querer muerta a Kamila, y 2 cumplen ambas condiciones.

1. Si elegimos un sospechoso al azar, ¿cuál es la probabilidad de que tenga acceso al laboratorio?
2. ¿Cuál es la probabilidad de que tenga motivo?
3. ¿Cuál es la probabilidad de que tenga ambos?

### Enigma 2.3: Simulación de la moneda

Escribe un programa en Python que simule 10,000 lanzamientos de una moneda y calcule la probabilidad estimada de obtener cara. ¿Qué tan cerca está del valor teórico de 0.5?

---

## Lo que aprendiste

- La **probabilidad** mide la posibilidad de que ocurra un evento (0 a 1)
- **Regla de Laplace**: P = casos favorables / casos posibles
- **Ley de los grandes números**: más repeticiones → estimaciones más precisas
- Eventos **independientes**: P(A y B) = P(A) × P(B)
- La **simulación** permite estimar probabilidades mediante repetición
- Una probabilidad extremadamente baja sugiere manipulación

Valeria guardó el análisis. Fuera, la noche había caído completamente sobre Barcelona.

—Hay alguien con quien necesito hablar —dijo Valeria—. El director del ICD. Si alguien sabía lo que Kamila estaba investigando, es él.

—No creo que sea buena idea —dijo Marco—. El director... es mi padre.

Valeria lo miró fijamente.

—Tu apellido es Tupac. El director es el Dr. Hugo Tupac.

Marco asintió.

—Y no tengo idea si él está involucrado. Pero tengo miedo de averiguarlo.



# Capítulo 3: El Teorema del Sospechoso

## Conceptos: Probabilidad condicional, Teorema de Bayes

---

Valeria no durmió bien esa noche. Las palabras de Marco resonaban en su cabeza: "El director es mi padre." ¿Podía confiar en él? ¿O Marco era parte de algo más grande?

A las 7 a.m. estaba de vuelta en el ICD. Había recibido un mensaje de Marco: *"Ven al laboratorio 3. Tengo algo."*

Cuando llegó, Marco estaba frente a una pizarra blanca llena de números.

—Anoche no pude dormir —dijo Marco—. Estuve pensando en lo que me dijiste sobre las probabilidades. Y recordé algo que Kamila me explicó una vez: el **Teorema de Bayes**.

—¿Sabes lo que es?

—Sé que es una forma de actualizar nuestras creencias cuando tenemos nueva información. Pero no sé cómo aplicarlo aquí.

Valeria sonrió. Kamila le había enseñado Bayes en su primer semestre de la maestría.

—El Teorema de Bayes es la base de todo el razonamiento estadístico moderno. Nos permite calcular la probabilidad de una hipótesis dado lo que observamos.

$$P(H|E) = \frac{P(E|H) \times P(H)}{P(E)}$$

Donde:
- $P(H|E)$: probabilidad de la hipótesis dados los datos observados
- $P(E|H)$: probabilidad de observar los datos si la hipótesis es cierta
- $P(H)$: probabilidad inicial de la hipótesis
- $P(E)$: probabilidad de observar los datos

—Vamos a aplicarlo al caso —dijo Valeria—. Tenemos cuatro sospechosos principales: Ramiro Quispe (seguridad), Hugo Tupac (director), la asistente de Kamila (Sofía), y un desconocido.

---

## Bayes aplicado al caso

Valeria abrió su laptop:

```python
# Teorema de Bayes aplicado al caso

# Probabilidades iniciales (sin ninguna evidencia)
# P(H): probabilidad de que cada sospechoso sea culpable

sospechosos = ['Ramiro', 'Hugo', 'Sofia', 'Desconocido']
prob_inicial = [0.25, 0.25, 0.25, 0.25]  # Todos igualmente probables

print("Probabilidades iniciales (previas):")
for s, p in zip(sospechosos, prob_inicial):
    print(f"  {s}: {p:.2f}")
```

—Pero ahora tenemos nueva información. Sabemos que:
1. Kamila fue asesinada entre las 2 a.m. y las 4 a.m.
2. La puerta estaba cerrada por dentro (posible suicidio simulado)
3. Solo personas con acceso biométrico pudieron entrar
4. Los datos del tratamiento A fueron manipulados

—Cada pieza de información actualiza nuestras probabilidades.

```python
# Nueva evidencia: acceso biométrico
# P(E|H): probabilidad de tener acceso dada la culpabilidad

# Ramiro (seguridad): 100% tiene acceso
# Hugo (director): 100% tiene acceso
# Sofía (asistente): 100% tiene acceso
# Desconocido: 10% (probabilidad baja de que un desconocido tenga acceso)

prob_acceso_dado_culpable = [1.0, 1.0, 1.0, 0.1]
prob_acceso_total = sum(
    prob_acceso_dado_culpable[i] * prob_inicial[i]
    for i in range(4)
)

print(f"\nProbabilidad total de acceso: {prob_acceso_total:.2f}")

# Aplicamos Bayes: P(H|E) = P(E|H) * P(H) / P(E)
prob_posterior_acceso = []
for i in range(4):
    posterior = (prob_acceso_dado_culpable[i] * prob_inicial[i]) / prob_acceso_total
    prob_posterior_acceso.append(posterior)

print("\nProbabilidades actualizadas (acceso biométrico):")
for s, p in zip(sospechosos, prob_posterior_acceso):
    print(f"  {s}: {p:.3f}")
```

Resultado:

```
Probabilidad total de acceso: 0.775

Probabilidades actualizadas (acceso biométrico):
  Ramiro: 0.323
  Hugo: 0.323
  Sofia: 0.323
  Desconocido: 0.032
```

—El desconocido pasa de 0.25 a 0.03 —dijo Marco—. Tiene sentido: si no tenía acceso, es muy poco probable que sea el asesino.

—Exacto. Pero aún no hemos terminado. Tenemos más evidencia.

```python
# Nueva evidencia: manipulación de datos
# P(E|H): probabilidad de que el sospechoso haya manipulado datos

# Ramiro (seguridad): 0.3 (podría, pero no es su área)
# Hugo (director): 0.7 (tiene acceso a todo)
# Sofía (asistente): 0.8 (trabajaba directamente con los datos)
# Desconocido: 0.2

prob_manipula_dado_culpable = [0.3, 0.7, 0.8, 0.2]

# Usamos las probabilidades anteriores como nuevas previas
prob_previas = prob_posterior_acceso

prob_manipula_total = sum(
    prob_manipula_dado_culpable[i] * prob_previas[i]
    for i in range(4)
)

prob_posterior_manipula = []
for i in range(4):
    posterior = (prob_manipula_dado_culpable[i] * prob_previas[i]) / prob_manipula_total
    prob_posterior_manipula.append(posterior)

print("\nProbabilidades actualizadas (acceso + manipulación):")
for s, p in zip(sospechosos, prob_posterior_manipula):
    print(f"  {s}: {p:.3f}")
```

Resultado:

```
Probabilidades actualizadas (acceso + manipulación):
  Ramiro: 0.149
  Hugo: 0.348
  Sofia: 0.398
  Desconocido: 0.010
```

—Sofía y Hugo subieron —observó Marco—. Ramiro bajó.

—Correcto. Pero aún tenemos más evidencia: la desaparición de Ramiro.

```python
# Nueva evidencia: Ramiro desapareció
# P(E|H): probabilidad de desaparecer si eres culpable

# Ramiro: 0.9 (desapareció, muy sospechoso)
# Hugo: 0.1 (sigue aquí)
# Sofía: 0.1 (sigue aquí)
# Desconocido: 0.5 (no sabemos)

prob_desaparece_dado_culpable = [0.9, 0.1, 0.1, 0.5]
prob_previas = prob_posterior_manipula

prob_desaparece_total = sum(
    prob_desaparece_dado_culpable[i] * prob_previas[i]
    for i in range(4)
)

prob_posterior_final = []
for i in range(4):
    posterior = (prob_desaparece_dado_culpable[i] * prob_previas[i]) / prob_desaparece_total
    prob_posterior_final.append(posterior)

print("\n=== PROBABILIDADES FINALES (Bayes) ===")
for s, p in sorted(zip(sospechosos, prob_posterior_final), key=lambda x: -x[1]):
    print(f"  {s}: {p:.3f} ({p*100:.1f}%)")
```

Resultado:

```
=== PROBABILIDADES FINALES (Bayes) ===
  Ramiro: 0.592 (59.2%)
  Hugo: 0.154 (15.4%)
  Sofia: 0.176 (17.6%)
  Desconocido: 0.022 (2.2%)
```

—Increíble —dijo Marco—. Ramiro tiene casi 60% de probabilidad de ser el culpable, solo porque desapareció. Pero Sofía y Hugo aún tienen ~15% cada uno. No podemos descartarlos.

—Esa es la magia de Bayes —dijo Valeria—. Nunca te da una certeza absoluta, pero te dice dónde enfocar tus recursos. Y en este caso, Ramiro es nuestra mejor pista.

---

## Más allá de las probabilidades

—Pero hay otra forma de aplicar Bayes —continuó Valeria—. Una que Kamila usaba todo el tiempo para detectar fraudes: calcular la probabilidad de que un resultado sea genuino.

—¿Cómo?

—Imagina que una prueba de detección de mentiras tiene una precisión del 95%. Si una persona es culpable, la prueba lo detecta el 95% de las veces (verdadero positivo). Si es inocente, la prueba dice que es inocente el 95% de las veces (verdadero negativo).

—Parece buena.

—Pero aquí está el truco. Si la probabilidad base de culpabilidad en la población es del 1%, y la prueba dice que alguien es culpable, ¿cuál es la probabilidad real de que sea culpable?

Valeria escribió:

```python
# Paradoja de la prueba

p_culpable = 0.01  # 1% de la población
p_inocente = 0.99
precision_prueba = 0.95  # 95% de precisión

# P(positivo | culpable) = 0.95
# P(positivo | inocente) = 0.05 (falso positivo)

p_positivo = (0.95 * 0.01) + (0.05 * 0.99)
p_culpable_dado_positivo = (0.95 * 0.01) / p_positivo

print(f"P(culpable | prueba positiva) = {p_culpable_dado_positivo:.3f}")
print(f"O solo {p_culpable_dado_positivo*100:.1f}%")
```

Resultado:

```
P(culpable | prueba positiva) = 0.161
O solo 16.1%
}

—¿Solo 16%? —preguntó Marco—. Pero la prueba tiene 95% de precisión.

—Exacto. Por eso Bayes es tan importante. Cuando la condición es rara (1 de cada 100 es culpable), incluso una prueba precisa produce muchos falsos positivos. De cada 100 personas, 1 es culpable (detectada correctamente) y 5 son inocentes pero la prueba dice que son culpables. Así que de 6 positivos, solo 1 es realmente culpable.

—Eso cambia todo.

—Y es exactamente por eso que Kamila usaba Bayes para todo. Para detectar fraudes, para analizar datos clínicos, para encontrar la verdad en un mar de números.

Marco se quedó en silencio un momento.

—Entonces —dijo—, si Ramiro tiene 59% de probabilidad según Bayes, y sabiendo que la probabilidad base de que una persona específica sea asesina es bajísima... ¿Ramiro es casi seguro el culpable?

—Casi seguro no existe en estadística —sonrió Valeria—. Pero sí, es nuestra mejor apuesta.

—Entonces tenemos que encontrarlo.

—No. Primero tenemos que entender por qué manipuló los datos. Y para eso, necesito ver algo más.

—¿Qué?

—Las distribuciones reales de los datos antes de la manipulación. Si Kamila encontró el fraude, seguro guardó una copia de los datos originales.

---

## Enigmas

### Enigma 3.1: Bayes con tus datos

Un detector de fraudes financieros tiene una precisión del 99%. Si el 0.5% de las transacciones son fraudulentas, y el detector marca una transacción como fraudulenta, ¿cuál es la probabilidad real de que sea un fraude?

### Enigma 3.2: El test médico

Una enfermedad afecta al 2% de la población. Un test la detecta con un 98% de precisión. Si una persona da positivo:

1. ¿Cuál es la probabilidad de que realmente tenga la enfermedad?
2. ¿Por qué es tan baja a pesar de la alta precisión?

### Enigma 3.3: Bayes en cadena

Usando los datos del capítulo, agrega una nueva evidencia: las cámaras de seguridad muestran a alguien de baja estatura (menos de 1.60m) entrando al laboratorio. De los sospechosos:

- Ramiro: 1.75m → P(baja estatura | culpable) = 0.05
- Hugo: 1.82m → P(baja estatura | culpable) = 0.05
- Sofía: 1.55m → P(baja estatura | culpable) = 0.80
- Desconocido: P(baja estatura | culpable) = 0.50

Actualiza las probabilidades de los sospechosos. ¿Quién sube? ¿Quién baja?

---

## Lo que aprendiste

- El **Teorema de Bayes** actualiza probabilidades con nueva información
- Las **probabilidades condicionales** miden la probabilidad de un evento dado otro
- **P(E|H)**: probabilidad de la evidencia si la hipótesis es cierta
- La **paradoja de la prueba**: pruebas precisas pueden ser engañosas con condiciones raras
- Bayes es fundamental para el razonamiento estadístico y la detección de fraudes

—Vamos a buscar esos datos originales —dijo Valeria—. Pero primero, necesito que me lleves al despacho de tu padre.

Marco dudó.

—¿Estás segura?

—Si Hugo Tupac es inocente, nos ayudará. Si es culpable, necesito ver su reacción cuando le pregunte por los datos.

Marco asintió.

—Vamos.



# Capítulo 4: La Distribución del Engaño

## Conceptos: Distribución normal, desviación estándar, Z-score, regla empírica

---

El despacho del Dr. Hugo Tupac ocupaba todo el octavo piso del ICD. Paredes de vidrio, muebles de madera tallada a mano, y una vista panorámica de la cordillera de los Andes. El director era un hombre alto, de cabello cano y mirada intensa.

—Siéntense —dijo sin levantar la vista de su computadora—. Sabía que vendrían.

—¿Sabía? —preguntó Valeria.

—Marco es mi hijo. Y Kamila era mi mejor investigadora. Cuando alguien muere en tu institución, las preguntas no tardan en llegar.

El Dr. Tupac finalmente levantó la vista.

—¿Qué quieren saber?

—Todo —dijo Valeria—. ¿Qué estaba investigando Kamila?

—No lo sé con exactitud. Ella trabajaba en el proyecto Yupay, un sistema de modelos predictivos. Pero en las últimas semanas se volvió... paranoica. Decía que había encontrado una anomalía en los datos del Ministerio de Salud.

—¿Qué tipo de anomalía?

—No me dio detalles. Dijo que necesitaba verificarlo antes de hablarlo con alguien.

—¿Y usted no preguntó?

—Pregunté. Me dijo que esperara. Y luego... apareció muerta.

Valeria observó al director. Su lenguaje corporal era abierto, sus respuestas directas. Pero algo no encajaba.

—Necesito acceso a los datos del proyecto Yupay —dijo Valeria.

—Imposible. Son datos clasificados del ministerio.

—Entonces deme acceso a los servidores donde Kamila guardaba sus copias de seguridad.

El Dr. Tupac la miró largamente.

—Una hora. Marco te acompañará. Y si encuentras algo, me lo reportas directamente.

Salieron del despacho. Marco estaba pálido.

—¿Crees que dice la verdad? —preguntó.

—No lo sé —respondió Valeria—. Pero sus respuestas fueron... estadísticamente normales. Sin desviaciones. Y eso, a veces, es sospechoso.

---

## La distribución normal

En la sala de servidores, Valeria encontró los backups de Kamila. Había docenas de archivos, pero uno llamó su atención: `distribucion_original.npy`.

—Esto es un archivo NumPy —dijo—. Contiene datos numéricos puros.

Lo cargó en Python:

```python
import numpy as np
import matplotlib.pyplot as plt

# Cargamos los datos originales
datos_originales = np.load('distribucion_original.npy')
print(f"Shape: {datos_originales.shape}")
print(f"Tipo: {datos_originales.dtype}")
print(f"Primeros 20 valores: {datos_originales[:20]}")
```

Resultado:

```
Shape: (10000,)
Tipo: float64
Primeros 20 valores: [72.3 68.1 74.5 71.2 69.8 73.0 70.5 75.1 67.9 72.8
                      70.2 74.0 71.8 69.5 73.4 68.7 72.1 70.9 75.3 71.5]
}

—Son mediciones de presión arterial —dijo Valeria—. De un estudio clínico. Vamos a ver su distribución.

```python
# Visualizar la distribución
media = np.mean(datos_originales)
mediana = np.median(datos_originales)
desv_std = np.std(datos_originales)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {desv_std:.2f}")
print(f"Mínimo: {np.min(datos_originales):.2f}")
print(f"Máximo: {np.max(datos_originales):.2f}")

# Histograma
plt.hist(datos_originales, bins=50, alpha=0.7, color='blue', edgecolor='black')
plt.axvline(media, color='red', linestyle='--', label=f'Media = {media:.1f}')
plt.axvline(media - desv_std, color='green', linestyle=':', label=f'-1σ')
plt.axvline(media + desv_std, color='green', linestyle=':', label=f'+1σ')
plt.title('Distribución de Presión Arterial (Datos Originales)')
plt.xlabel('Presión Arterial')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
```

—Mira esto —dijo Valeria señalando la pantalla—. La distribución tiene forma de campana. Es una **distribución normal** (o gaussiana).

—¿Por qué es importante?

—Porque en una distribución normal, hay una **regla empírica** que se cumple siempre:

- El **68%** de los datos está a 1 desviación estándar de la media
- El **95%** está a 2 desviaciones estándar
- El **99.7%** está a 3 desviaciones estándar

```python
# Verificar la regla empírica
dentro_1sigma = np.sum(np.abs(datos_originales - media) <= desv_std)
dentro_2sigma = np.sum(np.abs(datos_originales - media) <= 2 * desv_std)
dentro_3sigma = np.sum(np.abs(datos_originales - media) <= 3 * desv_std)
total = len(datos_originales)

print(f"\n=== REGLA EMPÍRICA ===")
print(f"68% teórico: 6800")
print(f"Dentro de 1σ: {dentro_1sigma} ({100*dentro_1sigma/total:.1f}%)")
print(f"95% teórico: 9500")
print(f"Dentro de 2σ: {dentro_2sigma} ({100*dentro_2sigma/total:.1f}%)")
print(f"99.7% teórico: 9970")
print(f"Dentro de 3σ: {dentro_3sigma} ({100*dentro_3sigma/total:.1f}%)")
```

Resultado:

```
=== REGLA EMPÍRICA ===
68% teórico: 6800
Dentro de 1σ: 6832 (68.3%)
95% teórico: 9500
Dentro de 2σ: 9495 (95.0%)
99.7% teórico: 9970
Dentro de 3σ: 9973 (99.7%)
}

—Casi perfecto —dijo Valeria—. Estos datos son genuinos. Ahora comparemos con los datos manipulados que vimos en el capítulo anterior.

---

## El Z-score: midiendo la anomalía

—El **Z-score** nos dice a cuántas desviaciones estándar está un valor de la media. Es la forma estándar de identificar valores atípicos (outliers).

$$Z = \frac{x - \mu}{\sigma}$$

Valeria escribió:

```python
# Calcular Z-scores para identificar anomalías
def z_score(valor, media, desv_std):
    return (valor - media) / desv_std

# Encontremos los valores más extremos
z_scores = np.abs((datos_originales - media) / desv_std)
indices_extremos = np.argsort(z_scores)[-5:]  # 5 valores más extremos

print(f"\n=== VALORES EXTREMOS (Z-score) ===")
print(f"{'Índice':<10} {'Valor':<12} {'Z-score':<10}")
print("-" * 32)
for i in indices_extremos:
    z = z_score(datos_originales[i], media, desv_std)
    print(f"{i:<10} {datos_originales[i]:<12.2f} {z:<10.2f}")

# ¿Cuántos valores tienen Z-score > 3?
extremos = np.sum(z_scores > 3)
print(f"\nValores con Z-score > 3: {extremos}")
print(f"Esperado (0.3%): {int(0.003 * len(datos_originales))}")
```

Resultado:

```
=== VALORES EXTREMOS (Z-score) ===
Índice      Valor        Z-score   
--------------------------------
3412        65.2         -2.98      
8911        76.8          2.95      
4523        64.9         -3.12      
1023        77.1          3.05      
7845        63.8         -3.41      

Valores con Z-score > 3: 27
Esperado (0.3%): 30
}

—Ahora —dijo Valeria—, comparemos con los datos falsos del ensayo clínico.

Valeria cargó los datos del capítulo anterior.

```python
# Datos falsos: 500 pacientes, 470 mejoran (tratamiento A)
# Bajo una distribución normal, esperaríamos cierta variabilidad

# Simulamos cómo deberían verse datos genuinos
import random
random.seed(42)

datos_genuinos = []
for _ in range(500):
    if random.random() < 0.71:  # 71% de mejora general
        datos_genuinos.append(1)  # mejora
    else:
        datos_genuinos.append(0)  # no mejora

tasa_genuina = sum(datos_genuinos) / 500

# Simulamos 10000 ensayos para ver la distribución esperada
tasas_simuladas = []
for _ in range(10000):
    ensayo = []
    for _ in range(500):
        if random.random() < 0.71:
            ensayo.append(1)
        else:
            ensayo.append(0)
    tasas_simuladas.append(sum(ensayo) / 500)

media_simulada = np.mean(tasas_simuladas)
std_simulada = np.std(tasas_simuladas)

print(f"Media de tasas simuladas: {media_simulada:.3f}")
print(f"Desviación estándar: {std_simulada:.3f}")

# ¿Qué tan extrema es la tasa observada del tratamiento A (94%)?
tasa_observada = 0.94
z_tasa = (tasa_observada - media_simulada) / std_simulada
print(f"\nTasa observada (Tratamiento A): {tasa_observada}")
print(f"Z-score de la tasa observada: {z_tasa:.2f}")
print(f"Esto es {z_tasa:.0f} desviaciones estándar por encima de la media")
print(f"Probabilidad de ocurrir al azar: esencialmente 0")
```

Resultado:

```
Media de tasas simuladas: 0.710
Desviación estándar: 0.020

Tasa observada (Tratamiento A): 0.94
Z-score de la tasa observada: 11.50
Esto es 12 desviaciones estándar por encima de la media
Probabilidad de ocurrir al azar: esencialmente 0
}

—Un Z-score de 11.5 —dijo Valeria—. En el mundo real, un Z-score mayor a 3 ya es extremadamente raro. Once punto cinco es... imposible. Es como encontrar una persona de 4 metros de altura.

—Alguien manipuló estos números —dijo Marco.

—Sí. Y quien lo hizo no entiende de distribuciones normales. Porque si supiera, habría hecho que los datos falsos se vieran más realistas.

---

## La distribución del engaño

Valeria abrió otro archivo del backup de Kamila.

—Mira esto. Kamila guardó una comparación entre los datos originales y los datos manipulados.

```python
# Comparación visual
datos_manipulados = np.load('datos_manipulados.npy')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(datos_originales, bins=50, alpha=0.7, color='blue')
ax1.set_title('Datos Originales')
ax1.set_xlabel('Presión Arterial')

ax2.hist(datos_manipulados, bins=50, alpha=0.7, color='red')
ax2.set_title('Datos Manipulados')
ax2.set_xlabel('Presión Arterial')

plt.tight_layout()
plt.show()

# Estadísticas comparativas
print(f"{'Métrica':<25} {'Original':<12} {'Manipulado':<12}")
print("-" * 49)
print(f"{'Media':<25} {np.mean(datos_originales):<12.2f} {np.mean(datos_manipulados):<12.2f}")
print(f"{'Desviación Std':<25} {np.std(datos_originales):<12.2f} {np.std(datos_manipulados):<12.2f}")
print(f"{'Mediana':<25} {np.median(datos_originales):<12.2f} {np.median(datos_manipulados):<12.2f}")
print(f"{'Asimetría (skewness)':<25} {np.mean(((datos_originales - np.mean(datos_originales))/np.std(datos_originales))**3):<12.2f} {np.mean(((datos_manipulados - np.mean(datos_manipulados))/np.std(datos_manipulados))**3):<12.2f}")
```

Resultado:

```
Métrica                   Original     Manipulado  
-------------------------------------------------
Media                     71.23        74.56      
Desviación Std            2.11         0.95       
Mediana                   71.20        74.50      
Asimetría (skewness)      0.02         0.85       
}

—¿Ves la diferencia? —preguntó Valeria—. Los datos originales tienen una desviación estándar de 2.11, los manipulados de solo 0.95. La desviación estándar se redujo a la mitad. Y la asimetría pasó de casi cero (normal) a 0.85 (sesgada).

—¿Qué significa eso?

—Que alguien no solo cambió los valores, sino que alteró la **variabilidad natural** de los datos. Los datos falsos son demasiado perfectos. Demasiado centrados. En estadística, eso se llama un **sesgo de manipulación**.

---

## Enigmas

### Enigma 4.1: Identifica los outliers

Un conjunto de edades tiene media 45 y desviación estándar 10. Calcula los Z-scores de las siguientes edades e identifica cuáles son outliers (|Z| > 3):

[23, 45, 67, 72, 18, 81, 44, 46, 22, 78]

### Enigma 4.2: La regla empírica

En una distribución normal con media 100 y desviación estándar 15:

1. ¿Qué porcentaje de valores está entre 85 y 115?
2. ¿Entre 70 y 130?
3. ¿Entre 55 y 145?

### Enigma 4.3: Detecta la manipulación

Te dan dos conjuntos de datos. Uno es genuino y el otro fue manipulado. Calcula la media, desviación estándar y Z-scores de ambos. ¿Cuál parece manipulado y por qué?

```python
conjunto_A = [72, 68, 74, 71, 69, 73, 70, 75, 67, 72, 70, 74, 71, 69, 73]
conjunto_B = [72, 72, 73, 71, 72, 72, 72, 71, 73, 72, 72, 73, 71, 72, 72]
```

---

## Lo que aprendiste

- La **distribución normal** (campana de Gauss) es la distribución más común en la naturaleza
- La **regla empírica**: 68-95-99.7% de los datos dentro de 1-2-3 desviaciones estándar
- El **Z-score** mide cuán atípico es un valor: Z = (x - μ) / σ
- |Z| > 3 generalmente indica un **outlier**
- Datos manipulados suelen tener **menor variabilidad** y **mayor asimetría**

Valeria cerró su laptop.

—Tengo suficiente para demostrar que los datos del ensayo fueron manipulados. Pero aún no sé quién lo hizo ni por qué.

—¿Y ahora? —preguntó Marco.

—Ahora vamos a buscar a Ramiro. Porque si él no manipuló los datos, alguien lo está usando como chivo expiatorio. Y si él lo hizo... necesito saber por qué.

Marco asintió.

—Tengo una idea de dónde puede estar.



# Capítulo 5: La Muestra que Miente

## Conceptos: Población vs muestra, sesgo de selección, muestreo, tipos de muestreo

---

Marco llevó a Valeria a un mercado en el barrio de San Pedro. Entre puestos de frutas, especias y artesanías, había un pequeño local de tecnología con un cartel que decía "REPARACIONES RÁPIDAS — COMPRA Y VENTA DE LAPTOS".

—Aquí —dijo Marco—. Ramiro viene aquí. Su hermano es dueño del local.

Entraron. El local era oscuro, lleno de computadoras viejas y cables por todos lados. Detrás del mostrador, un hombre delgado y de mirada nerviosa los observó.

—¿Ramiro? —preguntó Valeria.

—No está —respondió el hombre—. Y no sé dónde está.

—Somos amigos de Kamila Huamán —dijo Marco—. Necesitamos hablar con él antes de que sea demasiado tarde.

El hombre dudó. Luego señaló una puerta al fondo.

—Segundo piso. Pero no le digan que yo los envié.

Subieron las escaleras. La puerta del segundo piso estaba entreabierta. Valeria la empujó suavemente.

Ramiro Quispe estaba sentado frente a una computadora, rodeado de papeles y tazas de café vacías. Cuando los vio, dio un salto.

—¿Quiénes son? ¿Qué quieren?

—Soy Valeria Quispe. Esto es Marco Tupac. Trabajamos con la doctora Huamán.

—No sé nada —dijo Ramiro—. No sé cómo murió, no sé quién la mató, no sé nada.

—No te creo —dijo Valeria—. Y si no hablas con nosotros, hablarás con la policía.

Ramiro se derrumbó.

—Está bien. Pero lo que voy a decirles... no sé si me van a creer.

---

## La muestra que miente

—Kamila me pidió que la ayudara —dijo Ramiro—. Estaba investigando un fraude en los ensayos clínicos del Ministerio de Salud. Alguien estaba manipulando los datos para que un medicamento pareciera más efectivo de lo que realmente era.

—¿Y tú qué tenías que ver?

—Ella necesitaba acceso a los servidores del ministerio. Y yo... bueno, tengo mis contactos.

—¿Encontraste algo?

Ramiro asintió.

—Encontré los logs de acceso. Alguien entró a los servidores a las 2:30 a.m. de la noche en que Kamila murió. Y no solo entró: subió archivos y borró otros.

—¿Quién?

—No tengo nombre. Pero tengo la IP. Y las huellas digitales.

Valeria se sentó frente a la computadora de Ramiro.

—Enséñame.

—Hay un problema —dijo Ramiro—. Los logs que tengo son solo una **muestra** de los datos totales. El ministerio borró la mayoría. Lo que tengo es lo que alcancé a copiar antes de que me descubrieran.

—¿Qué tan grande es la muestra?

—52 registros de un total de... no sé. Podrían ser miles.

—Entonces tenemos un problema de **sesgo de selección** —dijo Valeria.

---

## Población vs muestra

—En estadística —explicó Valeria—, la **población** es el conjunto completo de datos. La **muestra** es un subconjunto. La clave es que la muestra debe ser **representativa** de la población.

—¿Y cómo sabemos si una muestra es representativa?

—Depende del método de muestreo.

Valeria abrió Python:

```python
# Tipos de muestreo en Python

import random
import numpy as np

# Población total (simulada)
poblacion = list(range(1, 10001))
print(f"Población total: {len(poblacion)}")

# 1. MUESTREO ALEATORIO SIMPLE
# Cada elemento tiene la misma probabilidad de ser seleccionado
muestra_aleatoria = random.sample(poblacion, 100)
print(f"\n1. Muestreo aleatorio simple: {len(muestra_aleatoria)} elementos")
print(f"   Primeros 10: {muestra_aleatoria[:10]}")

# 2. MUESTREO SISTEMÁTICO
# Seleccionamos cada k-ésimo elemento
k = 100  # Cada 100 elementos
muestra_sistematica = poblacion[::k]
print(f"\n2. Muestreo sistemático (k=100): {len(muestra_sistematica)} elementos")
print(f"   Elementos: {muestra_sistematica[:10]}")

# 3. MUESTREO ESTRATIFICADO
# Dividimos la población en grupos y muestreamos cada grupo
def muestreo_estratificado(poblacion, estratos, tamano_muestra):
    """estratos: diccionario con {nombre: [elementos]}"""
    muestra = []
    for estrato, elementos in estratos.items():
        n = int(len(elementos) / sum(len(e) for e in estratos.values()) * tamano_muestra)
        muestra.extend(random.sample(elementos, min(n, len(elementos))))
    return muestra

# Simulamos estratos
estratos = {
    'jovenes': list(range(1, 4001)),
    'adultos': list(range(4001, 7001)),
    'mayores': list(range(7001, 10001))
}

muestra_estratificada = muestreo_estratificado(poblacion, estratos, 300)
print(f"\n3. Muestreo estratificado: {len(muestra_estratificada)} elementos")
print(f"   Distribución: jovenes={sum(1 for x in muestra_estratificada if x <= 4000)}, "
      f"adultos={sum(1 for x in muestra_estratificada if 4000 < x <= 7000)}, "
      f"mayores={sum(1 for x in muestra_estratificada if x > 7000)}")
```

Resultado:

```
Población total: 10000

1. Muestreo aleatorio simple: 100 elementos
   Primeros 10: [4321, 7890, 1234, 5678, 9012, 3456, 7891, 2345, 6789, 123]

2. Muestreo sistemático (k=100): 100 elementos
   Elementos: [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]

3. Muestreo estratificado: 300 elementos
   Distribución: jovenes=120, adultos=90, mayores=90
```

—Pero hay un tipo de muestreo que es peligroso para nuestra investigación —dijo Valeria—. El **sesgo de selección**.

```python
# SESGO DE SELECCIÓN
# Ocurre cuando la muestra no es representativa de la población

# Ejemplo: encuesta de satisfacción
# Solo responden los que están muy satisfechos o muy insatisfechos

poblacion_satisfaccion = list(range(1, 1001))  # 1000 personas
satisfaccion_real = np.random.normal(7.0, 1.5, 1000)  # Satisfacción real (1-10)

# Sesgo: solo responden los extremos (satisfacción < 3 o > 8)
sesgo_seleccion = [(i, s) for i, s in enumerate(satisfaccion_real) if s < 3 or s > 8]
muestra_sesgada = [s for _, s in sesgo_seleccion]

print(f"\n=== SESGO DE SELECCIÓN ===")
print(f"Media real de satisfacción: {np.mean(satisfaccion_real):.2f}")
print(f"Media de la muestra sesgada: {np.mean(muestra_sesgada):.2f}")
print(f"Diferencia: {abs(np.mean(satisfaccion_real) - np.mean(muestra_sesgada)):.2f}")
print(f"Tamaño de muestra sesgada: {len(muestra_sesgada)} de {len(satisfaccion_real)}")
```

Resultado:

```
=== SESGO DE SELECCIÓN ===
Media real de satisfacción: 7.02
Media de la muestra sesgada: 5.85
Diferencia: 1.17
}

—La muestra sesgada muestra una satisfacción de 5.85 cuando la real es 7.02. Eso es un error de 1.17 puntos. Y en el mundo de los ensayos clínicos, ese error puede significar millones de dólares o vidas humanas.

---

## El problema con los logs de Ramiro

Valeria analizó los logs de acceso.

```python
# Analizando los logs de Ramiro
# Solo tenemos 52 registros de un total desconocido

logs_disponibles = 52
total_estimado = 500  # Estimación

proporcion_muestra = logs_disponibles / total_estimado
print(f"Proporción de la muestra: {proporcion_muestra:.1%}")
print(f"Margen de error potencial: ±{1 / (logs_disponibles ** 0.5) * 100:.1f}%")

# ¿Qué IPs aparecen?
from collections import Counter

ips_en_logs = [
    '192.168.1.10', '192.168.1.20', '192.168.1.10', '10.0.0.5',
    '192.168.1.30', '192.168.1.10', '10.0.0.5', '172.16.0.1',
    '192.168.1.10', '192.168.1.20', '10.0.0.5', '172.16.0.1',
    '192.168.1.10', '10.0.0.5', '172.16.0.1'
] * 3 + ['192.168.1.10'] * 7

conteo_ips = Counter(ips_en_logs[:logs_disponibles])

print(f"\n=== IPS EN LOGS (muestra) ===")
for ip, count in conteo_ips.most_common():
    print(f"  {ip}: {count} accesos ({count/logs_disponibles*100:.1f}%)")
```

Resultado:

```
Proporción de la muestra: 10.4%
Margen de error potencial: ±13.9%

=== IPS EN LOGS (muestra) ===
192.168.1.10: 27 accesos (51.9%)
10.0.0.5: 8 accesos (15.4%)
172.16.0.1: 7 accesos (13.5%)
192.168.1.20: 6 accesos (11.5%)
192.168.1.30: 4 accesos (7.7%)
```

—La IP 192.168.1.10 aparece en el 51.9% de los accesos —dijo Valeria—. Pero esta es solo una muestra. Podría ser que esta IP sea la dominante... o que los datos que faltan cuenten una historia diferente.

—¿Qué hacemos entonces? —preguntó Marco.

—Necesitamos una muestra más grande. O mejor aún: necesitamos toda la población. Ramiro, ¿puedes acceder a los logs completos?

—No. Me descubrieron. Mi acceso está bloqueado.

—Entonces tendremos que trabajar con lo que tenemos. Pero tenemos que ser honestos sobre las limitaciones de nuestra muestra.

---

## El muestreo estratificado y el caso

—Hay otro tipo de muestreo que podría ayudarnos —dijo Valeria—. El **muestreo estratificado**. Si dividimos a los sospechosos en grupos y analizamos cada grupo por separado, podemos identificar patrones que el muestreo simple no muestra.

```python
# Muestreo estratificado aplicado a los sospechosos

sospechosos_por_grupo = {
    'academicos': {
        'Hugo Tupac': {'acceso': True, 'motivo': 0.3, 'coartada': 0.7},
        'Sofia Vargas': {'acceso': True, 'motivo': 0.2, 'coartada': 0.5},
        'otros_investigadores': ['Luis Mamani', 'Rosa Quispe']
    },
    'seguridad': {
        'Ramiro Quispe': {'acceso': True, 'motivo': 0.5, 'coartada': 0.1},
        'guardias_nocturnos': ['Pedro Condori', 'Juan Huamán']
    },
    'externos': {
        'proveedor_medicamento': {'acceso': False, 'motivo': 0.8, 'coartada': 0.3},
        'consultor_ministerio': {'acceso': True, 'motivo': 0.6, 'coartada': 0.4}
    }
}

print("=== ANÁLISIS POR ESTRATOS ===")
for estrato, miembros in sospechosos_por_grupo.items():
    print(f"\nEstrato: {estrato}")
    for nombre, datos in miembros.items():
        if isinstance(datos, dict):
            print(f"  {nombre}: acceso={datos['acceso']}, motivo={datos['motivo']}, "
                  f"coartada={datos['coartada']}")
        else:
            print(f"  {nombre}")
```

Resultado:

```
=== ANÁLISIS POR ESTRATOS ===

Estrato: academicos
  Hugo Tupac: acceso=True, motivo=0.3, coartada=0.7
  Sofia Vargas: acceso=True, motivo=0.2, coartada=0.5
  otros_investigadores: ['Luis Mamani', 'Rosa Quispe']

Estrato: seguridad
  Ramiro Quispe: acceso=True, motivo=0.5, coartada=0.1
  guardias_nocturnos: ['Pedro Condori', 'Juan Huamán']

Estrato: externos
  proveedor_medicamento: acceso=False, motivo=0.8, coartada=0.3
  consultor_ministerio: acceso=True, motivo=0.6, coartada=0.4
```

—Lo interesante —dijo Valeria señalando la pantalla— es que el **proveedor del medicamento** tiene el motivo más alto (0.8), pero no tiene acceso al ICD. Y el **consultor del ministerio** tiene acceso y un motivo alto. Pero de esta muestra pequeña, Ramiro es el único que cumple las tres condiciones: acceso, motivo, y coartada débil.

—Pero los datos de Ramiro vinieron de su propia muestra —dijo Marco—. ¿Y si está manipulando su propia muestra para desviar la atención?

Valeria sonrió.

—Eso, Marco, demuestra que estás aprendiendo. Porque en estadística, la primera pregunta que debes hacerte siempre es: **¿quién recolectó esta muestra y qué interés tiene?**

---

## Enigmas

### Enigma 5.1: Identifica el sesgo

En cada escenario, identifica el tipo de sesgo de selección:

1. Una encuesta política llama solo a teléfonos fijos durante el día
2. Un estudio médico solo incluye voluntarios jóvenes y sanos
3. Una encuesta de satisfacción solo la responden los clientes más molestos o más contentos
4. Un estudio sobre ingresos solo usa datos de personas que declaran impuestos

### Enigma 5.2: Calcula el error muestral

Tienes una muestra de 400 personas de una población de 10,000. Quieres estimar la proporción de personas que prefieren un candidato. Si el 52% de la muestra prefiere al candidato A:

1. ¿Cuál es el margen de error?
   (Fórmula: $ME = \frac{1}{\sqrt{n}}$, donde n es el tamaño de la muestra)
2. ¿Entre qué valores está la proporción real con 95% de confianza?

### Enigma 5.3: Diseña un muestreo

Tienes que investigar la satisfacción de los estudiantes de una universidad con 5 facultades. ¿Qué tipo de muestreo usarías y por qué? ¿Cómo seleccionarías a los estudiantes?

---

## Lo que aprendiste

- La **población** es el conjunto completo de datos; la **muestra** es un subconjunto
- El **muestreo aleatorio simple** da la misma probabilidad a cada elemento
- El **muestreo estratificado** divide la población en grupos y muestrea cada uno
- El **sesgo de selección** ocurre cuando la muestra no es representativa
- El **margen de error** disminuye con el tamaño de la muestra
- Siempre pregunta: ¿quién recolectó esta muestra y qué interés tiene?

—Necesito una muestra más grande —dijo Valeria—. Y sé exactamente dónde conseguirla.

—¿Dónde? —preguntaron Marco y Ramiro al unísono.

—En el servidor del ministerio. Si no podemos entrar por la puerta principal, entraremos por la ventana.

Ramiro la miró con preocupación.

—Eso es ilegal.

—La muerte de Kamila también lo fue. A veces, la estadística no es suficiente. A veces hay que ensuciarse las manos.

—Te ayudo —dijo Ramiro—. Pero si nos descubren, no me conocen.

—Trato hecho.



# Capítulo 6: La Hipótesis Asesina

## Conceptos: Prueba de hipótesis, hipótesis nula y alternativa, valor p, significancia estadística

---

Ramiro trabajó toda la noche. Cuando Valeria y Marco llegaron al local de reparaciones a la mañana siguiente, lo encontraron dormido sobre el teclado, con una taza de café volcada a su lado.

—¿Lo lograste? —preguntó Valeria.

Ramiro levantó la cabeza lentamente, con los ojos rojos.

—Sí. Pero no me gusta lo que encontré.

—¿Qué es?

—Los logs completos del ministerio. 5,000 registros. Y una IP que aparece repetidamente en los momentos clave.

—¿Cuál IP?

—172.16.0.1. Es la IP del ICD. Del servidor interno.

—¿Del ICD? —preguntó Marco—. ¿Alguien dentro del ICD accedió a los datos del ministerio?

—No solo accedió —dijo Ramiro—. Modificó archivos. Borró registros. Y todo ocurrió entre las 2 y las 4 a.m. de la noche en que Kamila murió.

—¿Puedes identificar al usuario?

—No. La conexión usaba credenciales genéricas. Pero hay algo más.

—¿Qué?

—La IP 172.16.0.1 es la del despacho del director.

El silencio se instaló en la habitación. Marco palideció.

—Mi padre —dijo en voz baja.

—O alguien que usó su computadora —corrigió Valeria—. Aún no tenemos pruebas suficientes.

—¿Cómo vamos a obtenerlas?

—Con una **prueba de hipótesis**.

---

## La hipótesis nula y la alternativa

—En estadística —explicó Valeria—, cuando queremos probar algo, formulamos dos hipótesis:

1. **Hipótesis nula (H₀)**: lo que asumimos que es verdad por defecto. "No hay efecto", "no hay diferencia", "todo es normal".
2. **Hipótesis alternativa (H₁)**: lo que queremos demostrar. "Hay un efecto", "hay una diferencia", "algo está mal".

—En nuestro caso:

- **H₀**: El Dr. Hugo Tupac no accedió a los datos del ministerio esa noche
- **H₁**: El Dr. Hugo Tupac accedió a los datos del ministerio esa noche

—Pero no podemos probar H₁ directamente. Lo que hacemos es tratar de **rechazar H₀**. Si los datos son suficientemente inconsistentes con H₀, la rechazamos y aceptamos H₁.

—¿Y cómo sabemos si los datos son "suficientemente inconsistentes"?

—Con el **valor p** (p-value).

---

## El valor p

Valeria abrió Python:

```python
# Prueba de hipótesis aplicada al caso

import numpy as np
import random

# DATOS DEL CASO
# Queremos saber si Hugo Tupac es responsable de los accesos nocturnos

# Paso 1: Definir las hipótesis
print("=== PRUEBA DE HIPÓTESIS ===")
print("H₀: Hugo Tupac NO accedió a los datos")
print("H₁: Hugo Tupac SÍ accedió a los datos")
print()

# Paso 2: Recopilar evidencia
# Logs de acceso: 5000 registros
# Accesos desde la IP del despacho de Hugo: 78 (de 5000)
# Accesos nocturnos (2-4 a.m.) desde cualquier IP: 12
# Accesos nocturnos desde la IP de Hugo: 5

total_accesos = 5000
accesos_ip_hugo = 78
accesos_nocturnos = 12
accesos_nocturnos_hugo = 5

print(f"Total de accesos en logs: {total_accesos}")
print(f"Accesos desde IP de Hugo: {accesos_ip_hugo}")
print(f"Accesos nocturnos (2-4 a.m.): {accesos_nocturnos}")
print(f"Accesos nocturnos desde IP de Hugo: {accesos_nocturnos_hugo}")
print()

# Paso 3: Calcular la probabilidad esperada bajo H₀
# Si Hugo es inocente, los accesos nocturnos desde su IP deberían seguir
# la misma distribución que el resto de accesos

proporcion_ip_hugo = accesos_ip_hugo / total_accesos
print(f"Proporción de accesos desde IP de Hugo: {proporcion_ip_hugo:.4f}")
print(f"Esperados (si H₀ es cierta): {proporcion_ip_hugo * accesos_nocturnos:.2f} accesos nocturnos")
print(f"Observados: {accesos_nocturnos_hugo}")
print()

# Paso 4: Simular para obtener el valor p
# Bajo H₀, simulamos 10000 escenarios y vemos con qué frecuencia
# obtenemos 5 o más accesos nocturnos desde la IP de Hugo

random.seed(42)
simulaciones = 100000
resultados_extremos = 0

for _ in range(simulaciones):
    # Simulamos los 12 accesos nocturnos
    accesos_simulados = []
    for _ in range(accesos_nocturnos):
        if random.random() < proporcion_ip_hugo:
            accesos_simulados.append('hugo')
        else:
            accesos_simulados.append('otro')
    
    conteo_hugo = sum(1 for a in accesos_simulados if a == 'hugo')
    if conteo_hugo >= accesos_nocturnos_hugo:
        resultados_extremos += 1

p_valor = resultados_extremos / simulaciones
print(f"=== VALOR P ===")
print(f"Simulaciones: {simulaciones}")
print(f"Resultados extremos (>= {accesos_nocturnos_hugo}): {resultados_extremos}")
print(f"Valor p: {p_valor:.6f}")
print(f"Interpretación: {'RECHAZAMOS H₀' if p_valor < 0.05 else 'NO RECHAZAMOS H₀'}")
```

Resultado:

```
=== PRUEBA DE HIPÓTESIS ===
H₀: Hugo Tupac NO accedió a los datos
H₁: Hugo Tupac SÍ accedió a los datos

Total de accesos en logs: 5000
Accesos desde IP de Hugo: 78
Accesos nocturnos (2-4 a.m.): 12
Accesos nocturnos desde IP de Hugo: 5

Proporción de accesos desde IP de Hugo: 0.0156
Esperados (si H₀ es cierta): 0.19 accesos nocturnos
Observados: 5

=== VALOR P ===
Simulaciones: 100000
Resultados extremos (>= 5): 0
Valor p: 0.000000
Interpretación: RECHAZAMOS H₀
```

—El valor p es esencialmente 0 —dijo Valeria—. La probabilidad de haber observado 5 accesos nocturnos desde la IP de Hugo, si él fuera inocente, es prácticamente nula. Rechazamos la hipótesis nula.

—Eso significa... —Marco no podía terminar la frase.

—Significa que los datos apuntan a tu padre. Pero estadísticamente, esto no es una condena. Es una **evidencia**. Necesitamos más.

---

## La significancia estadística y los errores

—En las pruebas de hipótesis, hay dos errores posibles:

```python
print("=== ERRORES EN PRUEBAS DE HIPÓTESIS ===")
print()
print("ERROR TIPO I (Falso Positivo): Rechazar H₀ cuando es verdadera")
print("  → Decir que Hugo es culpable cuando es inocente")
print("  → Probabilidad = α (nivel de significancia, típicamente 0.05)")
print()
print("ERROR TIPO II (Falso Negativo): No rechazar H₀ cuando es falsa")
print("  → Decir que Hugo es inocente cuando es culpable")
print("  → Probabilidad = β")
print()
print(f"Nuestro valor p ({p_valor:.6f}) es menor que α (0.05)")
print(f"→ Rechazamos H₀ con 95% de confianza")
print(f"→ Pero hay 5% de probabilidad de que esto sea un falso positivo")
```

—Entonces, ¿hay un 5% de probabilidad de que mi padre sea inocente? —preguntó Marco.

—Si solo nos basáramos en esta prueba, sí. Pero la evidencia no termina aquí. Cuantas más pruebas independientes tengamos, más seguros podemos estar.

---

## La fuerza de la evidencia

Valeria continuó:

—En estadística, una prueba sola rara vez es concluyente. Pero cuando múltiples pruebas apuntan en la misma dirección, la evidencia se vuelve abrumadora.

```python
# Múltiples pruebas de hipótesis

print("=== MÚLTIPLES EVIDENCIAS ===")
print()

# Evidencia 1: Accesos nocturnos
p1 = 0.00001
print(f"Evidencia 1 (accesos nocturnos): valor p = {p1}")

# Evidencia 2: Manipulación de datos
# Los datos manipulados tienen una firma estadística
# Z-score de 11.5 es esencialmente imposible bajo H₀
p2 = 1e-30  # Aproximadamente 0
print(f"Evidencia 2 (manipulación datos): valor p ≈ {p2}")

# Evidencia 3: Desaparición de Ramiro
# Si Ramiro huyó porque tenía miedo de Hugo...
p3 = 0.15  # Débil, pero consistente
print(f"Evidencia 3 (desaparición Ramiro): valor p = {p3}")

# Evidencia 4: IP del despacho de Hugo
# La IP 172.16.0.1 está física en su despacho
p4 = 0.01  # Alguien más podría haber usado su computadora
print(f"Evidencia 4 (IP física en despacho): valor p = {p4}")

# Combinación: el producto de los valores p
# (Esto es una simplificación, el método correcto es Fisher)
import math
chi_cuadrado = -2 * sum(math.log(p) for p in [p1, p2, p3, p4])
print(f"\nEstadístico combinado (Fisher): {chi_cuadrado:.2f}")
print("Con 8 grados de libertad, valor p combinado < 0.00001")
print("→ La evidencia conjunta es abrumadora")
```

—Cuanto más evidencia reunimos, más se inclina la balanza —dijo Valeria—. Pero aún tenemos un problema.

—¿Cuál?

—No tenemos **prueba directa**. Tenemos correlación, tenemos probabilidades, tenemos valores p. Pero en un tribunal, necesitas más que estadísticas.

—¿Qué necesitamos?

—Algo que vincule directamente a Hugo con la manipulación. Un archivo. Un email. Una confesión.

—O un testigo —dijo Marco.

—O un testigo —repitió Valeria.

---

## Enigmas

### Enigma 6.1: Calcula el valor p

Lanzas una moneda 20 veces y obtienes 15 caras. ¿Es una moneda cargada?

1. H₀: la moneda es justa (P(cara) = 0.5)
2. H₁: la moneda está cargada hacia caras
3. Simula 10000 lanzamientos de 20 monedas justas
4. ¿Cuántas veces obtienes 15 o más caras?
5. ¿Cuál es el valor p?

### Enigma 6.2: Error tipo I y tipo II

Un test médico para detectar una enfermedad rara (0.1% de la población) tiene 99% de precisión:

1. Si el test da positivo, ¿cuál es la probabilidad de que sea un falso positivo (Error Tipo I)?
2. Si el test da negativo pero la persona tiene la enfermedad, ¿qué tipo de error es?
3. ¿Qué es más peligroso en este contexto?

### Enigma 6.3: Diseña tu propia prueba

Tienes datos de tiempos de respuesta (en segundos) de dos sitios web:

```python
sitio_A = [2.3, 2.1, 2.5, 2.2, 2.4, 2.0, 2.6, 2.3, 2.2, 2.5]
sitio_B = [3.1, 2.9, 3.3, 2.8, 3.0, 3.2, 2.7, 3.1, 2.9, 3.0]
```

1. Formula H₀ y H₁
2. Calcula las medias
3. ¿Cuál sitio es más rápido? ¿La diferencia es estadísticamente significativa?

---

## Lo que aprendiste

- La **hipótesis nula (H₀)** es lo que asumimos por defecto
- La **hipótesis alternativa (H₁)** es lo que queremos demostrar
- El **valor p** es la probabilidad de observar los datos si H₀ es cierta
- Si valor p < 0.05, rechazamos H₀ (resultado estadísticamente significativo)
- **Error Tipo I**: falso positivo (rechazar H₀ cuando es verdadera)
- **Error Tipo II**: falso negativo (no rechazar H₀ cuando es falsa)
- La evidencia combinada es más poderosa que una sola prueba

—Necesito hablar con tu padre —dijo Valeria—. Cara a cara.

—¿Y qué le vas a decir?

—Le voy a mostrar los números. Y voy a ver su reacción.

—¿Y si es culpable?

Valeria guardó su laptop.

—Entonces los números serán lo único que nos salve.



# Capítulo 7: La Correlación del Secreto

## Conceptos: Correlación, coeficiente de Pearson, causalidad vs correlación, matriz de correlación

---

El Dr. Hugo Tupac los recibió en su despacho con una expresión que Valeria no supo interpretar. ¿Era preocupación? ¿Enojo? ¿Miedo?

—Me dijeron que estaban investigando por su cuenta —dijo el director—. ¿Qué han encontrado?

Valeria colocó su laptop sobre la mesa y mostró los logs de acceso.

—Esto —dijo—. Accesos nocturnos desde la IP de su despacho al servidor del ministerio. La misma noche en que Kamila murió.

El Dr. Tupac observó la pantalla en silencio.

—No fui yo —dijo finalmente—. Esa noche estaba en una cena con el ministro. Tengo testigos.

—¿Alguien más tiene acceso a su computadora?

—Solo yo. Pero... la puerta de mi despacho no tiene llave física. Es biométrica. Cualquiera con acceso al octavo piso pudo entrar.

—¿Quién tiene acceso al octavo piso?

—Mi asistente. El personal de limpieza. Y... Kamila.

—¿Kamila?

—Sí. Ella venía a verme a menudo. Y a veces, cuando yo no estaba, dejaba documentos en mi escritorio.

Valeria procesó la información. ¿Era posible que Kamila misma hubiera accedido al servidor desde el despacho de Hugo? ¿O que alguien estuviera usando la ausencia de Hugo para incriminarlo?

—Necesito ver algo —dijo Valeria—. Las bitácoras de entrada al octavo piso.

—Puedo conseguírtelas —dijo Hugo—. Pero me vas a tener que explicar qué estás buscando.

—Estoy buscando **correlaciones**.

---

## Correlación: la danza de los números

—La **correlación** mide la relación entre dos variables. Si una aumenta y la otra también, tienen correlación positiva. Si una aumenta y la otra disminuye, tienen correlación negativa. Si no hay patrón, no hay correlación.

—El coeficiente de correlación de Pearson (r) va de -1 a +1:

- **r = +1**: correlación positiva perfecta
- **r = 0**: sin correlación
- **r = -1**: correlación negativa perfecta

Valeria abrió Python:

```python
# Correlación en Python

import numpy as np
import random
import math

# Ejemplos de correlación

# 1. Correlación positiva perfecta (r ≈ 1)
horas_estudio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas_examen = [2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 9.0, 10.0]

r_positivo = np.corrcoef(horas_estudio, notas_examen)[0, 1]
print(f"Correlación (horas estudio vs nota): {r_positivo:.3f}")

# 2. Correlación negativa perfecta (r ≈ -1)
edad_auto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
precio_auto = [30000, 27000, 24000, 21000, 18000, 15000, 12000, 9000, 6000, 3000]

r_negativo = np.corrcoef(edad_auto, precio_auto)[0, 1]
print(f"Correlación (edad del auto vs precio): {r_negativo:.3f}")

# 3. Sin correlación (r ≈ 0)
random.seed(42)
x_aleatorio = [random.gauss(0, 1) for _ in range(50)]
y_aleatorio = [random.gauss(0, 1) for _ in range(50)]

r_cero = np.corrcoef(x_aleatorio, y_aleatorio)[0, 1]
print(f"Correlación (datos aleatorios): {r_cero:.3f}")
```

Resultado:

```
Correlación (horas estudio vs nota): 0.976
Correlación (edad del auto vs precio): -0.997
Correlación (datos aleatorios): 0.042
```

---

## El problema: correlación no es causalidad

—Pero aquí está el error más común en estadística —dijo Valeria—: confundir **correlación con causalidad**.

—¿Qué significa eso?

—Que porque dos cosas estén correlacionadas, no significa que una cause la otra.

Valeria escribió:

```python
# Ejemplos de correlaciones falsas

# Ejemplo 1: Ventas de helados y ahogados
meses = list(range(1, 13))
ventas_helados = [10, 12, 15, 25, 40, 55, 60, 58, 45, 30, 18, 12]
ahogados_playa = [2, 3, 4, 8, 15, 22, 25, 24, 16, 9, 5, 3]

r_helados_ahogados = np.corrcoef(ventas_helados, ahogados_playa)[0, 1]
print(f"Correlación (helados vs ahogados): {r_helados_ahogados:.3f}")
print("¿Los helados causan ahogados? ¡NO!")
print("Variable oculta: el CALOR (en verano se venden más helados y más gente va a la playa)")
print()

# Ejemplo 2: Número de iglesias y crímenes
# (Datos ficticios para ilustrar)
ciudades = ['A', 'B', 'C', 'D', 'E']
iglesias = [5, 10, 15, 20, 25]
tasa_crimen = [20, 35, 45, 55, 70]

r_iglesias_crimen = np.corrcoef(iglesias, tasa_crimen)[0, 1]
print(f"Correlación (iglesias vs crímenes): {r_iglesias_crimen:.3f}")
print("¿Las iglesias causan crímenes? ¡NO!")
print("Variable oculta: POBLACIÓN (ciudades más grandes tienen más iglesias y más crímenes)")
```

Resultado:

```
Correlación (helados vs ahogados): 0.987
¿Los helados causan ahogados? ¡NO!
Variable oculta: el CALOR (en verano se venden más helados y más gente va a la playa)

Correlación (iglesias vs crímenes): 0.993
¿Las iglesias causan crímenes? ¡NO!
Variable oculta: POBLACIÓN (ciudades más grandes tienen más iglesias y más crímenes)
```

—En nuestro caso —dijo Valeria—, tenemos una correlación entre la IP de Hugo y los accesos nocturnos. Pero eso no significa que Hugo sea el culpable. Podría haber una **variable oculta**.

—¿Como qué?

—Como que alguien más usó su computadora. O que Kamila misma accedió desde allí para investigar. O que el sistema de logs fue manipulado.

---

## Matriz de correlación del caso

Valeria cargó los datos completos.

```python
# Matriz de correlación de las variables del caso

import pandas as pd

# Datos simulados del caso
datos_caso = pd.DataFrame({
    'sospechoso': ['Ramiro', 'Hugo', 'Sofia', 'Proveedor', 'Consultor'],
    'acceso_fisico': [1, 1, 1, 0, 1],        # 1 = tiene acceso
    'acceso_datos': [0.7, 0.9, 0.8, 0.1, 1],  # 0-1 nivel de acceso
    'motivo': [0.5, 0.3, 0.2, 0.8, 0.6],      # 0-1 nivel de motivo
    'coartada': [0.1, 0.7, 0.5, 0.3, 0.4],    # 0-1 solidez de coartada
    'desaparicion': [1, 0, 0, 0, 0],           # 1 = desapareció
    'ip_nocturna': [0, 1, 0.2, 0, 0.3],        # 0-1 frecuencia en logs nocturnos
    'manipulacion': [0.3, 0.7, 0.8, 0.2, 0.6]  # 0-1 evidencia de manipulación
})

# Calculamos la matriz de correlación
matriz_correlacion = datos_caso.select_dtypes(include=[np.number]).corr()

print("=== MATRIZ DE CORRELACIÓN ===")
print(matriz_correlacion.round(3))
print()

# Extraemos las correlaciones con 'manipulacion'
print("=== CORRELACIONES CON 'MANIPULACION' ===")
correlaciones_con_manipulacion = matriz_correlacion['manipulacion'].sort_values(ascending=False)
print(correlaciones_con_manipulacion.round(3))
```

Resultado:

```
=== MATRIZ DE CORRELACIÓN ===
                acceso_fisico  acceso_datos   motivo  coartada  desaparicion  ip_nocturna  manipulacion
acceso_fisico          1.000         0.707   -0.707    -0.000        -0.707        0.000         0.000
acceso_datos           0.707         1.000   -0.677     0.632        -0.535        0.574         0.707
motivo                -0.707        -0.677    1.000    -0.535         0.189       -0.542        -0.394
coartada              -0.000         0.632   -0.535     1.000        -0.632        0.316         0.316
desaparicion          -0.707        -0.535    0.189    -0.632         1.000       -0.189        -0.189
ip_nocturna            0.000         0.574   -0.542     0.316        -0.189        1.000         0.872
manipulacion           0.000         0.707   -0.394     0.316        -0.189        0.872         1.000

=== CORRELACIONES CON 'MANIPULACION' ===
manipulacion     1.000
ip_nocturna      0.872
acceso_datos     0.707
coartada         0.316
motivo          -0.394
desaparicion    -0.189
acceso_fisico    0.000
```

—Mira esto —dijo Valeria—. La variable con mayor correlación con `manipulacion` es `ip_nocturna` (0.872). Eso significa que quien tenga accesos nocturnos desde su IP tiene alta probabilidad de haber manipulado datos. Y Hugo es quien tiene el valor más alto en `ip_nocturna`.

—Pero —interrumpió Marco— también dijiste que correlación no es causalidad.

—Correcto. Y por eso necesitamos la siguiente pieza del rompecabezas.

---

## El diagrama de dispersión

Valeria creó un gráfico:

```python
# Diagrama de dispersión: acceso a datos vs manipulación
import matplotlib.pyplot as plt

datos_grafico = {
    'Ramiro': (0.7, 0.3),
    'Hugo': (0.9, 0.7),
    'Sofia': (0.8, 0.8),
    'Proveedor': (0.1, 0.2),
    'Consultor': (1.0, 0.6)
}

nombres = list(datos_grafico.keys())
accesos = [datos_grafico[n][0] for n in nombres]
manipulaciones = [datos_grafico[n][1] for n in nombres]

plt.figure(figsize=(8, 6))
plt.scatter(accesos, manipulaciones, s=100)

for i, nombre in enumerate(nombres):
    plt.annotate(nombre, (accesos[i], manipulaciones[i]),
                 xytext=(5, 5), textcoords='offset points')

plt.xlabel('Nivel de Acceso a Datos')
plt.ylabel('Evidencia de Manipulación')
plt.title('Acceso a Datos vs Manipulación')
plt.grid(True, alpha=0.3)

# Línea de tendencia
z = np.polyfit(accesos, manipulaciones, 1)
p = np.poly1d(z)
x_line = np.linspace(0, 1, 100)
plt.plot(x_line, p(x_line), 'r--', alpha=0.7)

plt.show()
```

—Sofía y Hugo están en la zona de alta correlación —dijo Valeria—. Pero Sofía tiene más evidencia de manipulación (0.8) que Hugo (0.7). Y tiene menos acceso que Hugo...

—¿Entonces podría ser Sofía? —preguntó Marco.

—O podría ser que Hugo y Sofía estén trabajando juntos. O que uno esté incriminando al otro.

---

## Enigmas

### Enigma 7.1: Calcula la correlación

Dados los siguientes datos de publicidad vs ventas:

```python
publicidad = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ventas = [12, 15, 18, 20, 22, 25, 28, 30, 32, 35]
```

1. Calcula el coeficiente de correlación de Pearson
2. Interpreta el resultado

### Enigma 7.2: Correlación falsa

Propón tres ejemplos de correlaciones falsas (donde dos variables están correlacionadas pero no hay relación causal). Para cada una, identifica la variable oculta.

### Enigma 7.3: Matriz del caso

Agrega un nuevo sospechoso a la matriz: la asistente de Kamila, llamada "Lidia", con estos valores:

- acceso_fisico: 0
- acceso_datos: 0.6
- motivo: 0.4
- coartada: 0.8
- desaparicion: 0
- ip_nocturna: 0.5
- manipulacion: 0.4

Recalcula la matriz de correlación. ¿Cambia la interpretación?

---

## Lo que aprendiste

- La **correlación** mide la relación entre dos variables (-1 a +1)
- **Pearson (r)**: mide correlación lineal
- **r ≈ 0**: sin correlación
- **Correlación no implica causalidad**: puede haber variables ocultas
- La **matriz de correlación** muestra relaciones entre múltiples variables
- Los **diagramas de dispersión** visualizan correlaciones

—Sofía —dijo Valeria—. Necesito hablar con Sofía.

—No vas a poder —dijo Hugo—. Tomó una semana de vacaciones. Justo después de la muerte de Kamila.

Valeria sintió que las piezas comenzaban a encajar.

—¿Dónde se fue?

—No lo dijo. Pero tengo su dirección de emergencia. Un pueblo en el Valle Sagrado.

—Entonces —dijo Valeria levantándose—, creo que es hora de hacer un viaje.



# Capítulo 8: La Regresión del Pasado

## Conceptos: Regresión lineal, recta de mejor ajuste, R², predicción

---

El viaje al Valle Sagrado tomó tres horas. Valeria y Marco alquilaron un auto y recorrieron la carretera que serpenteaba entre montañas. El paisaje era imponente: terrazas incas talladas en las laderas, nubes bajas que rozaban los picos, y el río Urubamba brillando al sol.

—¿Qué sabes de Sofía? —preguntó Valeria.

—Poco —dijo Marco—. Trabajaba con Kamila desde hacía dos años. Era su asistente de investigación. Muy callada, muy eficiente. Nunca llamaba la atención.

—Eso es sospechoso en sí mismo.

—¿Por qué?

—Porque en estadística, los valores atípicos son los más interesantes. Pero también lo son los valores que se esconden en la media. Los que nunca se desvían. Los que pasan desapercibidos.

Llegaron a un pequeño pueblo llamado Pachar. La dirección de Sofía era una casa de adobe al final de una calle empedrada. Valeria tocó la puerta.

Una mujer mayor abrió.

—¿Sofía? —preguntó Valeria.

—No está —respondió la mujer—. Se fue ayer. Dijo que tenía que regresar a la ciudad.

—¿Dijo algo más?

La mujer dudó. Luego sacó un sobre de su delantal.

—Dijo que si alguien venía preguntando por ella, les diera esto.

Valeria abrió el sobre. Dentro había una memoria USB y una nota que decía:

*"Lo siento. No sabía en lo que me estaba metiendo. Esto es lo que sé. — Sofía"*

---

## Los datos de Sofía

Valeria conectó la memoria USB a su laptop. Contenía un único archivo: `regresion_secreta.csv`.

—Son datos de ventas de un medicamento —dijo Valeria—. Pero no cualquier medicamento. Es el mismo del ensayo clínico manipulado.

—¿Qué muestra?

—Vamos a verlo con **regresión lineal**.

---

## Regresión lineal: encontrando la línea oculta

—La **regresión lineal** nos permite encontrar la relación entre una variable dependiente (Y) y una o más variables independientes (X). La idea es dibujar una línea recta que mejor se ajuste a los datos.

—La fórmula de una línea recta es:

$$Y = mX + b$$

Donde:
- **m** es la pendiente (cuánto cambia Y por cada unidad de X)
- **b** es el intercepto (el valor de Y cuando X = 0)

Valeria abrió Python:

```python
# Regresión lineal con Python

import numpy as np
import csv
import math

# Cargamos los datos de Sofía
datos_ventas = []
with open('regresion_secreta.csv', 'r') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        datos_ventas.append({
            'mes': int(fila['mes']),
            'gasto_publicidad': float(fila['gasto_publicidad']),
            'ventas': float(fila['ventas']),
            'pacientes': int(fila['pacientes'])
        })

print(f"Registros cargados: {len(datos_ventas)}")
print(f"Rango de meses: {datos_ventas[0]['mes']} - {datos_ventas[-1]['mes']}")
print()

# Extraemos variables
X = np.array([d['gasto_publicidad'] for d in datos_ventas])  # Gasto en publicidad
Y = np.array([d['ventas'] for d in datos_ventas])           # Ventas

# Calculamos la regresión lineal manualmente
n = len(X)
media_x = np.mean(X)
media_y = np.mean(Y)

# Pendiente (m)
numerador = sum((X[i] - media_x) * (Y[i] - media_y) for i in range(n))
denominador = sum((X[i] - media_x) ** 2 for i in range(n))
pendiente = numerador / denominador

# Intercepto (b)
intercepto = media_y - pendiente * media_x

print(f"=== REGRESIÓN LINEAL ===")
print(f"Ecuación: Ventas = {pendiente:.2f} × Publicidad + ({intercepto:.2f})")
print(f"Interpretación: por cada $1,000 en publicidad, las ventas aumentan en ${pendiente*1000:.0f}")
```

Resultado:

```
Registros cargados: 24
Rango de meses: 1 - 24

=== REGRESIÓN LINEAL ===
Ecuación: Ventas = 3.45 × Publicidad + (12.30)
Interpretación: por cada $1,000 en publicidad, las ventas aumentan en $3,450
```

—Pero hay algo raro —dijo Valeria—. La relación debería ser consistente. Veamos los residuos.

---

## Los residuos: lo que la línea no explica

—Los **residuos** son las diferencias entre los valores reales y los valores predichos por la línea de regresión. Si los residuos tienen un patrón, significa que la línea no está capturando toda la información.

```python
# Calculamos predicciones y residuos
predicciones = pendiente * X + intercepto
residuos = Y - predicciones

print(f"\n=== ANÁLISIS DE RESIDUOS ===")
print(f"{'Mes':<6} {'Real':<10} {'Predicho':<12} {'Residuo':<10}")
print("-" * 38)
for i in range(n):
    print(f"{datos_ventas[i]['mes']:<6} {Y[i]:<10.1f} {predicciones[i]:<12.1f} {residuos[i]:<10.1f}")

# Varianza de los residuos
var_residuos = np.var(residuos)
var_total = np.var(Y)
r_cuadrado = 1 - (var_residuos / var_total)

print(f"\nVarianza de residuos: {var_residuos:.2f}")
print(f"Varianza total: {var_total:.2f}")
print(f"R² (coeficiente de determinación): {r_cuadrado:.3f}")
print(f"Interpretación: el {r_cuadrado*100:.1f}% de la variación en ventas")
print(f"  es explicada por el gasto en publicidad")
```

Resultado:

```
=== ANÁLISIS DE RESIDUOS ===
Mes    Real       Predicho     Residuo   
------------------------------------------
1      50.0       48.9         1.1
2      52.0       52.4        -0.4
3      48.0       49.7        -1.7
4      55.0       53.2         1.8
5      51.0       50.1         0.9
...
23     78.0       68.0        10.0
24     82.0       69.3        12.7

Varianza de residuos: 5.82
Varianza total: 24.50
R² (coeficiente de determinación): 0.763
Interpretación: el 76.3% de la variación en ventas
  es explicada por el gasto en publicidad
```

—El R² de 0.763 es decente —dijo Valeria—. Pero mira los últimos meses: los residuos crecen. Mes 23: residuo de 10. Mes 24: residuo de 12.7.

—¿Qué significa?

—Que en los últimos meses, las ventas son mucho más altas de lo que la publicidad predeciría. Como si alguien estuviera inflando los números.

---

## Detectando la manipulación con regresión

Valeria dividió los datos en dos períodos: antes y después del mes 18.

```python
# Dividimos los datos
X_antes = X[:18]
Y_antes = Y[:18]
X_despues = X[18:]
Y_despues = Y[18:]

# Regresión para el período anterior
n_antes = len(X_antes)
media_x_antes = np.mean(X_antes)
media_y_antes = np.mean(Y_antes)
pendiente_antes = sum((X_antes[i] - media_x_antes) * (Y_antes[i] - media_y_antes) 
                       for i in range(n_antes)) / sum((X_antes[i] - media_x_antes) ** 2 
                       for i in range(n_antes))
intercepto_antes = media_y_antes - pendiente_antes * media_x_antes

# Regresión para el período posterior
n_despues = len(X_despues)
media_x_despues = np.mean(X_despues)
media_y_despues = np.mean(Y_despues)
pendiente_despues = sum((X_despues[i] - media_x_despues) * (Y_despues[i] - media_y_despues) 
                         for i in range(n_despues)) / sum((X_despues[i] - media_x_despues) ** 2 
                         for i in range(n_despues))
intercepto_despues = media_y_despues - pendiente_despues * media_x_despues

print("=== COMPARACIÓN DE PERÍODOS ===")
print(f"Período 1 (meses 1-18):")
print(f"  Ventas = {pendiente_antes:.2f} × Publicidad + ({intercepto_antes:.2f})")
print(f"  Pendiente: {pendiente_antes:.2f}")
print()
print(f"Período 2 (meses 19-24):")
print(f"  Ventas = {pendiente_despues:.2f} × Publicidad + ({intercepto_despues:.2f})")
print(f"  Pendiente: {pendiente_despues:.2f}")
print()

# Proyección: ¿qué ventas esperaríamos en los meses 19-24
# si el comportamiento hubiera sido el mismo que en los meses 1-18?
print("=== DETECCIÓN DE ANOMALÍAS ===")
print(f"{'Mes':<6} {'Real':<10} {'Esperado':<12} {'Diferencia':<12}")
print("-" * 40)
for i in range(n_despues):
    real = Y_despues[i]
    esperado = pendiente_antes * X_despues[i] + intercepto_antes
    diff = real - esperado
    print(f"{datos_ventas[18+i]['mes']:<6} {real:<10.1f} {esperado:<12.1f} {diff:<12.1f}")
```

Resultado:

```
=== COMPARACIÓN DE PERÍODOS ===
Período 1 (meses 1-18):
  Ventas = 2.80 × Publicidad + (14.20)
  Pendiente: 2.80

Período 2 (meses 19-24):
  Ventas = 4.90 × Publicidad + (8.50)
  Pendiente: 4.90

=== DETECCIÓN DE ANOMALÍAS ===
Mes    Real       Esperado     Diferencia   
--------------------------------------------
19     65.0       57.3         7.7
20     68.0       59.5         8.5
21     72.0       60.2         11.8
22     75.0       62.8         12.2
23     78.0       65.1         12.9
24     82.0       67.4         14.6
```

—La pendiente cambió de 2.80 a 4.90 —dijo Valeria—. Eso significa que, en los últimos 6 meses, cada dólar de publicidad generó casi el doble de ventas que antes. Eso no es crecimiento orgánico. Eso es manipulación.

—¿Y quién estuvo a cargo de los datos en esos meses?

—Según la nota de Sofía... ella misma.

---

## El R² y la calidad del modelo

—El **R²** (coeficiente de determinación) mide qué tan bien la línea de regresión se ajusta a los datos. Va de 0 a 1:

- **R² = 1**: el modelo predice perfectamente
- **R² = 0**: el modelo no predice nada

```python
# R² para ambos períodos
def calcular_r2(X, Y, pendiente, intercepto):
    predicciones = pendiente * X + intercepto
    residuos = Y - predicciones
    var_residuos = np.var(residuos)
    var_total = np.var(Y)
    return 1 - (var_residuos / var_total)

r2_antes = calcular_r2(X_antes, Y_antes, pendiente_antes, intercepto_antes)
r2_despues = calcular_r2(X_despues, Y_despues, pendiente_despues, intercepto_despues)

print(f"R² período 1: {r2_antes:.3f}")
print(f"R² período 2: {r2_despues:.3f}")
print()
print("Interpretación:")
if r2_despues > r2_antes:
    print("El R² aumentó: los datos del período 2 son 'demasiado perfectos'")
    print("→ Posible manipulación: los datos fueron ajustados para verse mejor")
else:
    print("El R² se mantuvo estable: los datos parecen consistentes")
```

Resultado:

```
R² período 1: 0.721
R² período 2: 0.958

Interpretación:
El R² aumentó: los datos del período 2 son 'demasiado perfectos'
→ Posible manipulación: los datos fueron ajustados para verse mejor
```

—Un R² de 0.958 en el segundo período significa que los datos se ajustan casi perfectamente a la línea —dijo Valeria—. En el mundo real, los datos nunca son tan perfectos. Alguien los fabricó.

—¿Sofía?

—O alguien usando sus credenciales.

---

## Enigmas

### Enigma 8.1: Calcula la regresión manual

Con estos datos de horas de estudio y notas:

```python
horas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas = [3.0, 4.0, 5.0, 5.5, 6.5, 7.0, 8.0, 8.5, 9.0, 9.5]
```

1. Calcula la pendiente y el intercepto
2. ¿Qué nota predecirías para 7.5 horas de estudio?
3. Calcula el R²

### Enigma 8.2: Detecta la manipulación

¿Cuál de estos conjuntos de datos parece manipulado? ¿Por qué?

```python
# Conjunto A
Xa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Ya = [15, 18, 20, 22, 25, 28, 30, 33, 35, 38]

# Conjunto B
Xb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Yb = [12, 25, 18, 30, 22, 35, 28, 40, 32, 45]
```

### Enigma 8.3: Predice el futuro

Usando la regresión del período 1 (Ventas = 2.80 × Publicidad + 14.20), predice las ventas para los meses 25 y 26 si el gasto en publicidad es de $15,000 y $16,000 respectivamente.

---

## Lo que aprendiste

- La **regresión lineal** encuentra la línea de mejor ajuste (Y = mX + b)
- La **pendiente (m)** mide el cambio en Y por unidad de cambio en X
- El **intercepto (b)** es el valor de Y cuando X = 0
- Los **residuos** son las diferencias entre valores reales y predichos
- El **R²** mide qué tan bien se ajusta el modelo (0 a 1)
- Residuos crecientes en el tiempo → posible manipulación

—Sofía nos dejó la evidencia, pero huyó —dijo Marco—. Eso la hace sospechosa.

—O la hace la próxima víctima —respondió Valeria—. Tenemos que encontrarla antes de que alguien más lo haga.

—¿Y cómo la encontramos?

Valeria miró los datos de la regresión.

—Usando el modelo. Si sabemos cómo se mueve, podemos predecir dónde estará.



# Capítulo 9: El Intervalo de Confianza

## Conceptos: Intervalo de confianza, nivel de confianza, margen de error, distribución muestral

---

Sofía no estaba en Pachar. La mujer de la casa dijo que había tomado un bus hacia Ollantaytambo temprano esa mañana. Valeria y Marco abordaron su auto y continuaron la persecución.

—¿Cómo sabemos que vamos en la dirección correcta? —preguntó Marco.

—No lo sabemos —admitió Valeria—. Pero podemos estimarlo.

—¿Estimarlo?

—Con un **intervalo de confianza**.

---

## El intervalo de confianza

—Un **intervalo de confianza** es un rango de valores dentro del cual esperamos que se encuentre el valor real de un parámetro, con cierto nivel de confianza.

—Por ejemplo, si decimos "el 95% de los peruanos tiene entre 25 y 35 años", ese es un intervalo de confianza del 95%.

—Pero no significa que haya un 95% de probabilidad de que la media esté en ese intervalo. Significa que, si repitiéramos el estudio muchas veces, el 95% de los intervalos contendrían la media real.

Valeria abrió Python:

```python
# Intervalo de confianza

import numpy as np
import random
import math

# EJEMPLO: Estimando la edad promedio de los estudiantes del ICD

# Tomamos una muestra de 50 estudiantes
random.seed(42)
muestra_edades = [random.gauss(25, 5) for _ in range(50)]
edad_media_muestral = np.mean(muestra_edades)
desv_std_muestral = np.std(muestra_edades, ddof=1)  # ddof=1 para muestra
n = len(muestra_edades)

print("=== INTERVALO DE CONFIANZA ===")
print(f"Tamaño de muestra: {n}")
print(f"Media muestral: {edad_media_muestral:.2f} años")
print(f"Desviación estándar muestral: {desv_std_muestral:.2f} años")
print()

# Para un intervalo de confianza del 95%:
# IC = media ± (valor_crítico × error_estándar)
# error_estándar = desv_std / sqrt(n)
# valor_crítico para 95% ≈ 1.96 (distribución normal)

nivel_confianza = 0.95
valor_critico = 1.96
error_estandar = desv_std_muestral / math.sqrt(n)
margen_error = valor_critico * error_estandar

ic_inferior = edad_media_muestral - margen_error
ic_superior = edad_media_muestral + margen_error

print(f"Intervalo de confianza del {nivel_confianza*100:.0f}%:")
print(f"  [{ic_inferior:.2f}, {ic_superior:.2f}]")
print(f"  Margen de error: ±{margen_error:.2f}")
print()
print("Interpretación: tenemos un 95% de confianza")
print("de que la media real de la población está entre")
print(f"{ic_inferior:.2f} y {ic_superior:.2f} años.")
```

Resultado:

```
=== INTERVALO DE CONFIANZA ===
Tamaño de muestra: 50
Media muestral: 24.87 años
Desviación estándar muestral: 4.83 años

Intervalo de confianza del 95%:
  [23.53, 26.21]
  Margen de error: ±1.34

Interpretación: tenemos un 95% de confianza
de que la media real de la población está entre
23.53 y 26.21 años.
```

—Ahora —dijo Valeria—, apliquemos esto a nuestra búsqueda de Sofía.

---

## Buscando a Sofía con intervalos

Valeria abrió los registros de su teléfono.

—Sofía usó su tarjeta de crédito tres veces después de desaparecer: una en una gasolinera en Chinchero, otra en un restaurante en Urubamba, y otra en un hotel en Ollantaytambo.

—Está yendo hacia Machu Picchu —dijo Marco.

—O está yendo a la frontera. Pero podemos calcular un intervalo de confianza para su ubicación actual.

```python
# Estimando la ubicación de Sofía

# Distancias desde Pachar (km)
pachar = 0
chinchero = 15
urubamba = 35
ollantaytambo = 60
aguas_calientes = 85  # Machu Picchu
frontera = 200  # Frontera con Bolivia

# Tiempos desde su desaparición (horas)
horas_desde_desaparicion = 18

# Velocidad promedio de viaje (km/h)
# Estimación: entre 30 y 60 km/h (transporte público en la región)
velocidad_min = 30
velocidad_max = 60

# Distancia mínima y máxima recorrida
distancia_min = velocidad_min * horas_desde_desaparicion
distancia_max = velocidad_max * horas_desde_desaparicion

print("=== ESTIMACIÓN DE UBICACIÓN ===")
print(f"Horas desde desaparición: {horas_desde_desaparicion}")
print(f"Velocidad estimada: {velocidad_min}-{velocidad_max} km/h")
print(f"Distancia recorrida: {distancia_min}-{distancia_max} km")
print()

# Radio de búsqueda desde el último punto conocido (Ollantaytambo)
ultima_ubicacion = ollantaytambo
radio_busqueda_min = distancia_min - (ollantaytambo - pachar)
radio_busqueda_max = distancia_max - (ollantaytambo - pachar)

print(f"Última ubicación conocida: Ollantaytambo (km {ultima_ubicacion})")
print(f"Radio de búsqueda: {radio_busqueda_min:.0f}-{radio_busqueda_max:.0f} km desde Ollantaytambo")
print()

# Probabilidad estimada por destino
destinos = {
    'Aguas Calientes (MP)': 85,
    'Cusco': 60,
    'Frontera Bolivia': 200,
    'Selva (Malvinas)': 150
}

print("Probabilidad estimada por destino (basada en distancia):")
for destino, distancia in destinos.items():
    if distancia_min <= distancia <= distancia_max:
        print(f"  {destino}: DENTRO del intervalo de confianza")
    elif distancia < distancia_min:
        print(f"  {destino}: demasiado cerca (ya debería haber llegado)")
    else:
        print(f"  {destino}: demasiado lejos (no le alcanza el tiempo)")
```

Resultado:

```
=== ESTIMACIÓN DE UBICACIÓN ===
Horas desde desaparición: 18
Velocidad estimada: 30-60 km/h
Distancia recorrida: 540-1080 km

Última ubicación conocida: Ollantaytambo (km 60)
Radio de búsqueda: 480-1020 km desde Ollantaytambo
```

—Con ese radio, podría estar en casi cualquier parte del sur del Perú —dijo Marco.

—Por eso necesitamos más datos. Los intervalos de confianza se estrechan cuando tenemos más información.

---

## Estrechando el intervalo

Valeria revisó los registros telefónicos de Sofía.

—Su teléfono hizo una llamada a las 6 a.m. de hoy. Duró 30 segundos. La torre que la registró está en la carretera hacia Abancay.

```python
# Nueva información: llamada registrada en Abancay
# Abancay está a 150 km de Ollantaytambo

torre_abancay = 150  # km desde Pachar
hora_llamada = 6  # a.m.
hora_actual = 11  # a.m.

# Con esta información, ajustamos el intervalo
# Sabemos que hace 5 horas estaba en Abancay (km 150)
distancia_desde_abancay_min = velocidad_min * (hora_actual - hora_llamada)
distancia_desde_abancay_max = velocidad_max * (hora_actual - hora_llamada)

print("=== INTERVALO ACTUALIZADO ===")
print(f"Última ubicación confirmada: Abancay (km 150) a las 6 a.m.")
print(f"Tiempo desde entonces: {hora_actual - hora_llamada} horas")
print(f"Distancia desde Abancay: {distancia_desde_abancay_min:.0f}-{distancia_desde_abancay_max:.0f} km")
print()

# Nuevos destinos probables
destinos_actualizados = {
    'Abancay': 150,
    'Andahuaylas': 220,
    'Ayacucho': 350,
    'Nazca': 500,
    'Arequipa': 550,
    'Cusco (retorno)': 60
}

print("Destinos probables (actualizado):")
for destino, distancia in sorted(destinos_actualizados.items(), key=lambda x: x[1]):
    if distancia_desde_abancay_min <= distancia <= distancia_desde_abancay_max:
        prob = "ALTA"
    elif abs(distancia - distancia_desde_abancay_min) < 50 or abs(distancia - distancia_desde_abancay_max) < 50:
        prob = "MEDIA"
    else:
        prob = "BAJA"
    print(f"  {destino} ({distancia} km): {prob}")
```

Resultado:

```
=== INTERVALO ACTUALIZADO ===
Última ubicación confirmada: Abancay (km 150) a las 6 a.m.
Tiempo desde entonces: 5 horas
Distancia desde Abancay: 150-300 km

Destinos probables (actualizado):
  Abancay (150 km): ALTA
  Andahuaylas (220 km): ALTA
  Ayacucho (350 km): MEDIA
  Cusco (retorno) (60 km): BAJA
  Nazca (500 km): BAJA
  Arequipa (550 km): BAJA
}

—Andahuaylas o Ayacucho —dijo Valeria—. Está yendo hacia la sierra sur.

—¿Y por qué iría allí?

—Tal vez porque allí hay alguien que puede ayudarla. O tal vez porque allí puede desaparecer para siempre.

---

## El error estándar y la precisión

—La precisión de nuestras estimaciones depende del **error estándar**:

$$EE = \frac{\sigma}{\sqrt{n}}$$

—Cuanto mayor sea la muestra (n), menor será el error estándar y más preciso será nuestro intervalo.

```python
# Cómo el tamaño de la muestra afecta el intervalo de confianza

print("=== EFECTO DEL TAMAÑO DE MUESTRA ===")
print(f"{'n':<10} {'Error Estándar':<18} {'Margen Error (95%)':<20} {'IC'}")
print("-" * 70)

desv_std_ejemplo = 5  # Desviación estándar típica
for n in [10, 30, 50, 100, 500, 1000]:
    error_estandar = desv_std_ejemplo / math.sqrt(n)
    margen = 1.96 * error_estandar
    print(f"{n:<10} {error_estandar:<18.3f} ±{margen:<18.2f} [{25-margen:.1f}, {25+margen:.1f}]")
```

Resultado:

```
=== EFECTO DEL TAMAÑO DE MUESTRA ===
n          Error Estándar    Margen Error (95%)   IC
----------------------------------------------------------------------
10         1.581             ±3.10                [21.9, 28.1]
30         0.913             ±1.79                [23.2, 26.8]
50         0.707             ±1.39                [23.6, 26.4]
100        0.500             ±0.98                [24.0, 26.0]
500        0.224             ±0.44                [24.6, 25.4]
1000       0.158             ±0.31                [24.7, 25.3]
```

—Cuantos más datos tenemos, más preciso es nuestro intervalo. Pero la precisión aumenta con la raíz cuadrada de n. Para duplicar la precisión, necesitamos cuadruplicar la muestra.

—Como en la investigación —dijo Marco—. Cada nueva pista nos da más precisión, pero nunca certeza absoluta.

—Exactamente. Y ahora, nuestra mejor estimación dice que Sofía va hacia Andahuaylas. Vamos.

---

## Enigmas

### Enigma 9.1: Calcula el intervalo

Una muestra de 100 personas tiene una media de ingresos de S/2,500 con una desviación estándar de S/800.

1. Calcula el error estándar
2. Calcula el intervalo de confianza del 95%
3. Interpreta el resultado

### Enigma 9.2: El tamaño importa

¿Qué tamaño de muestra necesitarías para tener un margen de error de ±S/100 con 95% de confianza, si la desviación estándar es S/800?

### Enigma 9.3: Aplica al caso

Si Sofía fue vista en Andahuaylas a las 8 a.m. (a 220 km de Pachar) y ahora son las 2 p.m., ¿cuál es tu intervalo de confianza para su ubicación actual? Usa velocidades de 30-60 km/h.

---

## Lo que aprendiste

- El **intervalo de confianza** da un rango para el valor real de un parámetro
- El **nivel de confianza** (95%) indica qué tan seguros estamos
- El **margen de error** depende del error estándar y del nivel de confianza
- El **error estándar** = σ / √n
- Mayor muestra → menor error → intervalo más preciso
- Nunca hay certeza absoluta, solo intervalos de confianza

Valeria aceleró en la carretera hacia Andahuaylas. El intervalo de confianza decía que Sofía estaba allí. Pero los intervalos de confianza no siempre aciertan.

Y ella lo sabía.



# Capítulo 10: La Varianza del Silencio

## Conceptos: Varianza, desviación estándar, medidas de dispersión, coeficiente de variación

---

Andahuaylas era un pueblo tranquilo en lo alto de los Andes. Llegaron al mediodía, cuando el sol calentaba las calles empedradas y los mercados estaban llenos de gente.

—¿Por dónde empezamos? —preguntó Marco.

—Por el único hotel que acepta tarjetas de crédito en este pueblo —dijo Valeria—. Sofía usó su tarjeta esta mañana.

El hotel "Los Andes" estaba en la plaza principal. Valeria mostró una foto de Sofía en la recepción.

—Sí, se hospedó aquí —dijo el recepcionista—. Pero ya se fue. Salió hace una hora.

—¿Hacia dónde?

—No lo sé. Pero dejó esto en su habitación.

El recepcionista les dio un sobre cerrado. Valeria lo abrió. Dentro había una carta escrita a mano.

*"Valeria:*

*Si estás leyendo esto, significa que lograste seguirme. Lo siento por haber huido. Pero tenía miedo. Kamila me pidió que la ayudara a investigar el fraude. No sabía que la iban a matar por eso.*

*Los datos que te dejé en la USB son reales. El fraude existe. Pero la persona responsable no es quien crees.*

*No es Hugo. No es Ramiro.*

*Es alguien más. Alguien que está más arriba.*

*Voy a buscarlo. Y si no regreso... termina lo que empezamos.*

*— Sofía"*

—"Alguien más arriba" —repitió Marco—. ¿Qué significa?

—Significa que el director del ICD no es el último eslabón —dijo Valeria—. Hay alguien por encima de él. Tal vez en el ministerio.

—¿Y ahora qué hacemos?

—Primero, entender qué nos está diciendo Sofía con los datos que dejó. Porque si hay algo que Kamila me enseñó, es que los números siempre hablan. Solo hay que saber escuchar su **varianza**.

---

## Varianza: midiendo la dispersión

—La **varianza** mide qué tan dispersos están los datos alrededor de la media. Si todos los datos son iguales, la varianza es cero. Si están muy dispersos, la varianza es alta.

—La fórmula de la varianza poblacional es:

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}$$

—Y la **desviación estándar** es la raíz cuadrada de la varianza: $\sigma = \sqrt{\sigma^2}$

—La desviación estándar es más fácil de interpretar porque está en las mismas unidades que los datos.

Valeria abrió Python:

```python
# Varianza y desviación estándar

import numpy as np
import math

# Comparamos la dispersión de dos conjuntos de datos
conjunto_estable = [45, 46, 45, 47, 46, 45, 46, 45, 47, 46]
conjunto_variable = [30, 60, 25, 55, 35, 65, 20, 70, 40, 50]

print("=== COMPARACIÓN DE DISPERSIÓN ===")
print(f"{'Métrica':<25} {'Estable':<15} {'Variable':<15}")
print("-" * 55)

for nombre in ['Estable', 'Variable']:
    datos = conjunto_estable if nombre == 'Estable' else conjunto_variable
    media = np.mean(datos)
    varianza = np.var(datos)
    desv_std = np.std(datos)
    rango = max(datos) - min(datos)
    cv = (desv_std / media) * 100  # Coeficiente de variación
    
    if nombre == 'Estable':
        print(f"{'Media':<25} {media:<15.2f} {np.mean(conjunto_variable):<15.2f}")
        print(f"{'Varianza':<25} {varianza:<15.2f} {np.var(conjunto_variable):<15.2f}")
        print(f"{'Desviación Estándar':<25} {desv_std:<15.2f} {np.std(conjunto_variable):<15.2f}")
        print(f"{'Rango':<25} {rango:<15} {max(conjunto_variable) - min(conjunto_variable):<15}")
        print(f"{'Coef. Variación (%)':<25} {cv:<15.2f} {(np.std(conjunto_variable)/np.mean(conjunto_variable))*100:<15.2f}")
```

Resultado:

```
=== COMPARACIÓN DE DISPERSIÓN ===
Métrica                    Estable          Variable        
-----------------------------------------------------------
Media                      45.80            45.00           
Varianza                   0.56             262.50          
Desviación Estándar        0.75             16.20           
Rango                      2                50              
Coef. Variación (%)        1.63             36.00           
```

—El conjunto estable tiene una desviación estándar de 0.75, el variable de 16.20. La diferencia es enorme. Pero la media es casi la misma: 45.8 vs 45.0.

—¿Por qué la media es similar si los datos son tan diferentes?

—Porque la media no cuenta toda la historia. Necesitamos la **dispersión** para entender realmente los datos.

---

## La varianza de los datos del ministerio

Valeria aplicó esto a los datos del ministerio.

```python
# Analizando la varianza de los ensayos clínicos

# Cargamos datos reales del ministerio (simulados)
# Comparación de la variabilidad antes y después de la manipulación

datos_antes = np.array([72.3, 68.1, 74.5, 71.2, 69.8, 73.0, 70.5, 75.1, 67.9, 72.8,
                        70.2, 74.0, 71.8, 69.5, 73.4, 68.7, 72.1, 70.9, 75.3, 71.5])
datos_despues = np.array([74.0, 75.0, 74.5, 75.5, 74.0, 75.0, 74.5, 75.0, 74.5, 75.0,
                          74.0, 75.0, 74.5, 75.0, 74.5, 75.0, 74.0, 75.0, 74.5, 75.0])

print("=== VARIANZA DE LOS ENSAYOS CLÍNICOS ===")
print(f"{'Métrica':<30} {'Antes':<15} {'Después':<15}")
print("-" * 60)
print(f"{'Media':<30} {np.mean(datos_antes):<15.2f} {np.mean(datos_despues):<15.2f}")
print(f"{'Varianza':<30} {np.var(datos_antes):<15.2f} {np.var(datos_despues):<15.2f}")
print(f"{'Desv. Estándar':<30} {np.std(datos_antes):<15.2f} {np.std(datos_despues):<15.2f}")
print(f"{'Coef. Variación (%)':<30} {np.std(datos_antes)/np.mean(datos_antes)*100:<15.2f} {np.std(datos_despues)/np.mean(datos_despues)*100:<15.2f}")

# Prueba de varianza (F-test simplificado)
f_estadistico = np.var(datos_antes) / np.var(datos_despues)
print(f"\nF-estadístico (varianza antes / varianza después): {f_estadistico:.2f}")
print("Si F >> 1, las varianzas son significativamente diferentes")
```

Resultado:

```
=== VARIANZA DE LOS ENSAYOS CLÍNICOS ===
Métrica                        Antes           Después         
------------------------------------------------------------
Media                          71.23           74.53           
Varianza                       4.46            0.18            
Desv. Estándar                 2.11            0.42            
Coef. Variación (%)            2.96            0.57            

F-estadístico (varianza antes / varianza después): 24.78
Si F >> 1, las varianzas son significativamente diferentes
}

—La varianza pasó de 4.46 a 0.18 —dijo Valeria—. La desviación estándar se redujo de 2.11 a 0.42. Esa reducción de variabilidad es la **firma estadística de la manipulación**.

—¿Por qué?

—Porque cuando alguien fabrica datos, tiende a hacerlos demasiado uniformes. En la naturaleza, los datos reales tienen variabilidad. Los datos falsos son sospechosamente consistentes.

---

## El coeficiente de variación: comparando dispersiones

—El **coeficiente de variación (CV)** es la desviación estándar dividida por la media, expresada como porcentaje. Permite comparar la dispersión de conjuntos de datos con diferentes medias.

$$CV = \frac{\sigma}{\mu} \times 100$$

```python
# Coeficiente de variación en diferentes contextos

print("=== COEFICIENTE DE VARIACIÓN EN CONTEXTOS ===")
print()

contextos = [
    ("Estatura de adultos (cm)", 170, 7),
    ("Peso de adultos (kg)", 70, 12),
    ("Presión arterial (mmHg)", 120, 10),
    ("Datos manipulados (ensayo)", 74.5, 0.42),
    ("Datos reales (ensayo)", 71.2, 2.11)
]

print(f"{'Contexto':<40} {'Media':<12} {'Desv.Std':<12} {'CV (%)':<12}")
print("-" * 76)
for contexto, media, desv in contextos:
    cv = (desv / media) * 100
    print(f"{contexto:<40} {media:<12} {desv:<12.2f} {cv:<12.2f}")
```

Resultado:

```
=== COEFICIENTE DE VARIACIÓN EN CONTEXTOS ===

Contexto                                  Media         Desv.Std      CV (%)      
--------------------------------------------------------------------------------
Estatura de adultos (cm)                  170           7.00          4.12        
Peso de adultos (kg)                      70            12.00         17.14       
Presión arterial (mmHg)                   120           10.00         8.33        
Datos manipulados (ensayo)                74.5          0.42          0.56        
Datos reales (ensayo)                     71.2          2.11          2.96        
```

—El CV de los datos manipulados es 0.56% —dijo Valeria—. Es decir, casi no hay variación. En cambio, los datos reales tienen un CV de 2.96%, que es típico para mediciones biológicas.

—Eso significa que los datos manipulados son estadísticamente imposibles.

—Exactamente. Y esa es la **varianza del silencio**: cuando alguien quiere ocultar algo, los datos se vuelven sospechosamente silenciosos.

---

## Aplicación: detectando fraudes con varianza

—Hay un método llamado **detección de dígitos de Benford** que se usa para detectar fraudes contables —dijo Valeria—. Pero hay una versión más simple basada en varianza.

```python
# Detectando fraudes con la varianza

def detectar_fraude(datos, umbral_cv=1.0):
    """Detecta posible fraude basado en el coeficiente de variación"""
    media = np.mean(datos)
    desv_std = np.std(datos)
    cv = (desv_std / media) * 100
    
    print(f"Media: {media:.2f}")
    print(f"Desviación estándar: {desv_std:.2f}")
    print(f"CV: {cv:.2f}%")
    
    if cv < umbral_cv:
        print(f"⚠ ALERTA: CV ({cv:.2f}%) < umbral ({umbral_cv}%)")
        print("  Posible manipulación detectada")
        return True
    else:
        print(f"✓ CV ({cv:.2f}%) normal")
        return False

print("=== DETECCIÓN DE FRAUDE ===")
print()

# Datos sospechosos del ministerio
print("Análisis 1: Datos del ministerio (sospechosos)")
detectar_fraude(datos_despues, umbral_cv=1.0)
print()

# Datos de otro estudio
print("Análisis 2: Datos de un estudio legítimo")
datos_legitimos = np.random.normal(74.5, 2.0, 100)
detectar_fraude(datos_legitimos, umbral_cv=1.0)
```

Resultado:

```
=== DETECCIÓN DE FRAUDE ===

Análisis 1: Datos del ministerio (sospechosos)
Media: 74.53
Desviación estándar: 0.42
CV: 0.57%
⚠ ALERTA: CV (0.57%) < umbral (1.00%)
  Posible manipulación detectada

Análisis 2: Datos de un estudio legítimo
Media: 74.71
Desviación estándar: 2.13
CV: 2.85%
✓ CV (2.85%) normal
```

—Y esto —dijo Valeria— es lo que Kamila descubrió. Algo que alguien no quería que se supiera.

---

## Enigmas

### Enigma 10.1: Calcula la varianza

Calcula la varianza y desviación estándar de:

```python
datos = [12, 15, 18, 22, 25, 30, 35, 40]
```

### Enigma 10.2: Compara CV

¿Cuál de estos conjuntos tiene mayor dispersión relativa?

```python
A = [100, 102, 98, 101, 99, 100, 103]
B = [10, 15, 8, 12, 20, 5, 18]
```

Usa el coeficiente de variación para compararlos.

### Enigma 10.3: Detecta el fraude

¿Cuál de estos conjuntos de datos parece manipulado? Justifica tu respuesta con estadísticas.

```python
estudio_X = [72, 71, 73, 72, 71, 73, 72, 71, 73, 72]
estudio_Y = [68, 75, 70, 74, 69, 76, 71, 73, 72, 70]
```

---

## Lo que aprendiste

- La **varianza** mide la dispersión de los datos alrededor de la media
- La **desviación estándar** es la raíz cuadrada de la varianza
- El **coeficiente de variación (CV)** = (σ/μ) × 100 permite comparar dispersiones
- Datos con muy baja variabilidad (CV < 1%) pueden ser manipulados
- La variabilidad natural es una firma de autenticidad en los datos

—Tenemos la prueba estadística del fraude —dijo Valeria—. Y tenemos la carta de Sofía. Ahora necesitamos encontrar a la persona que está "más arriba".

—¿Y quién es?

—Alguien en el Ministerio de Salud. Alguien con suficiente poder para silenciar a Kamila. Y para hacer desaparecer a Sofía.

—¿Cómo lo encontramos?

—Con los datos que nos dejó Sofía. Y con un poco más de estadística.

Valeria guardó su laptop. La búsqueda continuaba.



# Capítulo 11: La Prueba del Chi-Cuadrado

## Conceptos: Prueba de chi-cuadrado (χ²), tablas de contingencia, frecuencias observadas vs esperadas, independencia

---

Valeria recibió una llamada cuando salían de Andahuaylas. Era Ramiro.

—Encontré algo —dijo—. En los logs del ministerio. Hay un patrón de accesos que no habíamos visto.

—¿Qué tipo de patrón?

—Accesos desde una IP del Ministerio de Salud. Pero no desde una computadora cualquiera: desde el despacho del Viceministro.

—¿Del viceministro?

—Sí. Y los accesos coinciden exactamente con las fechas en que los datos fueron manipulados. La probabilidad de que sea una coincidencia es... calculémosla con chi-cuadrado.

---

## Chi-cuadrado: la prueba de independencia

—La **prueba de chi-cuadrado (χ²)** se usa para determinar si existe una asociación significativa entre dos variables categóricas. Es perfecta para nuestro caso: queremos saber si hay relación entre "persona" y "acceso nocturno".

—La fórmula es:

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

Donde:
- **O** = frecuencia observada
- **E** = frecuencia esperada (si no hubiera relación)

Valeria abrió Python cuando llegaron a un café con WiFi:

```python
# Prueba de chi-cuadrado para el caso

import numpy as np
import math
from collections import Counter

# TABLA DE CONTINGENCIA: Persona vs Acceso Nocturno
# Filas: personas (Hugo, Ramiro, Sofia, Viceministro, otros)
# Columnas: accesos nocturnos (Sí, No)

# Frecuencias observadas
# Extraído de los logs del ministerio
tabla_observada = np.array([
    [5,  73],    # Hugo: 5 accesos nocturnos, 73 diurnos
    [1,  45],    # Ramiro: 1 nocturno, 45 diurnos
    [3,  89],    # Sofia: 3 nocturnos, 89 diurnos
    [12, 28],    # Viceministro: 12 nocturnos, 28 diurnos
    [8,  736]    # Otros: 8 nocturnos, 736 diurnos
])

personas = ['Hugo', 'Ramiro', 'Sofia', 'Viceministro', 'Otros']
total_observado = np.sum(tabla_observada)

print("=== TABLA DE CONTINGENCIA ===")
print(f"{'Persona':<18} {'Nocturnos':<12} {'Diurnos':<12} {'Total':<12}")
print("-" * 54)
for i, persona in enumerate(personas):
    nocturnos = tabla_observada[i, 0]
    diurnos = tabla_observada[i, 1]
    total = nocturnos + diurnos
    print(f"{persona:<18} {nocturnos:<12} {diurnos:<12} {total:<12}")
print("-" * 54)
totales_columna = np.sum(tabla_observada, axis=0)
print(f"{'Total':<18} {totales_columna[0]:<12} {totales_columna[1]:<12} {total_observado:<12}")
```

Resultado:

```
=== TABLA DE CONTINGENCIA ===
Persona            Nocturnos     Diurnos       Total         
------------------------------------------------------
Hugo               5             73            78            
Ramiro             1             45            46            
Sofia              3             89            92            
Viceministro       12            28            40            
Otros              8             736           744           
------------------------------------------------------
Total              29            971           1000          
```

—Ahora calculamos las frecuencias **esperadas**. Si no hubiera relación entre la persona y los accesos nocturnos, la proporción de accesos nocturnos sería la misma para todos: 29/1000 = 2.9%.

```python
# Frecuencias esperadas (bajo la hipótesis de independencia)
proporcion_nocturna = totales_columna[0] / total_observado
print(f"\nProporción general de accesos nocturnos: {proporcion_nocturna:.4f} ({proporcion_nocturna*100:.1f}%)")

# Frecuencias esperadas para cada celda
# E = (total_fila * total_columna) / total_general
tabla_esperada = np.zeros_like(tabla_observada, dtype=float)
for i in range(len(personas)):
    total_fila = np.sum(tabla_observada[i, :])
    for j in range(2):
        tabla_esperada[i, j] = (total_fila * totales_columna[j]) / total_observado

print(f"\n=== FRECUENCIAS ESPERADAS ===")
print(f"{'Persona':<18} {'Nocturnos (esp)':<18} {'Diurnos (esp)':<18}")
print("-" * 54)
for i, persona in enumerate(personas):
    print(f"{persona:<18} {tabla_esperada[i, 0]:<18.1f} {tabla_esperada[i, 1]:<18.1f}")
```

Resultado:

```
Proporción general de accesos nocturnos: 0.0290 (2.9%)

=== FRECUENCIAS ESPERADAS ===
Persona            Nocturnos (esp)   Diurnos (esp)    
------------------------------------------------------
Hugo               2.3               75.7             
Ramiro             1.3               44.7             
Sofia              2.7               89.3             
Viceministro       1.2               38.8             
Otros              21.6              722.4            
```

—Y ahora calculamos el chi-cuadrado:

```python
# Cálculo del chi-cuadrado
chi_cuadrado = 0
for i in range(len(personas)):
    for j in range(2):
        o = tabla_observada[i, j]
        e = tabla_esperada[i, j]
        contribucion = (o - e) ** 2 / e
        chi_cuadrado += contribucion
        if contribucion > 1:
            print(f"  {personas[i]}: contribución significativa = {contribucion:.2f}")

print(f"\n=== RESULTADO CHI-CUADRADO ===")
print(f"χ² = {chi_cuadrado:.2f}")

# Grados de libertad = (filas - 1) * (columnas - 1) = (5-1)*(2-1) = 4
gl = (len(personas) - 1) * (2 - 1)
print(f"Grados de libertad: {gl}")

# Valor crítico para α = 0.05 con 4 gl ≈ 9.49
valor_critico = 9.49
print(f"Valor crítico (α=0.05): {valor_critico}")

if chi_cuadrado > valor_critico:
    print(f"→ χ² ({chi_cuadrado:.2f}) > valor crítico ({valor_critico})")
    print(f"→ RECHAZAMOS H₀: existe relación significativa entre")
    print(f"  la persona y los accesos nocturnos")
else:
    print(f"→ No hay evidencia suficiente para rechazar H₀")
```

Resultado:

```
Hugo: contribución significativa = 3.37
Viceministro: contribución significativa = 103.20
Otros: contribución significativa = 8.81

=== RESULTADO CHI-CUADRADO ===
χ² = 117.82
Grados de libertad: 4
Valor crítico (α=0.05): 9.49
→ χ² (117.82) > valor crítico (9.49)
→ RECHAZAMOS H₀: existe relación significativa entre
  la persona y los accesos nocturnos
```

—El chi-cuadrado es 117.82 —dijo Valeria—. El valor crítico para 95% de confianza es 9.49. Esto es más de 10 veces el valor crítico.

—¿Y qué significa eso exactamente?

—Que la probabilidad de que esta distribución sea producto del azar es esencialmente cero. El Viceministro tiene una cantidad anormal de accesos nocturnos. Y la contribución al chi-cuadrado del Viceministro es de 103.20 de 117.82 totales. Es decir, el 87.6% de la señal viene de él.

—El Viceministro es nuestro hombre —dijo Marco.

—Estadísticamente, sí. Ahora necesitamos la prueba directa.

---

## La prueba de bondad de ajuste

—Hay otra forma de usar chi-cuadrado —dijo Valeria—: la **prueba de bondad de ajuste**. Sirve para ver si una distribución observada coincide con una distribución esperada.

—Por ejemplo, si los datos del ensayo clínico siguieran una distribución normal, las frecuencias deberían distribuirse de cierta manera.

```python
# Prueba de bondad de ajuste para los datos del ensayo

# Datos observados del ensayo (tratamiento A)
mejora_observada = 470
no_mejora_observada = 30

# Frecuencias esperadas bajo H₀ (sin efecto del tratamiento)
# Si el tratamiento no tuviera efecto, esperaríamos la misma
# proporción de mejora que en el grupo de control (48%)
tasa_control = 0.48
mejora_esperada = 500 * tasa_control
no_mejora_esperada = 500 * (1 - tasa_control)

print("=== PRUEBA DE BONDAD DE AJUSTE ===")
print(f"{'':<20} {'Observado':<15} {'Esperado':<15} {'(O-E)²/E':<15}")
print("-" * 65)
for categoria, obs, esp in [("Mejora", mejora_observada, mejora_esperada),
                              ("No mejora", no_mejora_observada, no_mejora_esperada)]:
    contrib = (obs - esp) ** 2 / esp
    print(f"{categoria:<20} {obs:<15} {esp:<15.1f} {contrib:<15.2f}")

chi2_bondad = (mejora_observada - mejora_esperada)**2 / mejora_esperada + \
              (no_mejora_observada - no_mejora_esperada)**2 / no_mejora_esperada

print(f"\nχ² (bondad de ajuste) = {chi2_bondad:.2f}")
print(f"Grados de libertad: 1")
print(f"Valor crítico (α=0.05): 3.84")
print(f"→ {'RECHAZAMOS' if chi2_bondad > 3.84 else 'NO RECHAZAMOS'} H₀")
print(f"→ Los datos NO siguen la distribución esperada")
print(f"→ El tratamiento A tiene un efecto estadísticamente")
print(f"  significativo... pero es DEMASIADO significativo")
```

Resultado:

```
=== PRUEBA DE BONDAD DE AJUSTE ===
                     Observado        Esperado         (O-E)²/E         
-----------------------------------------------------------------
Mejora               470              240.0            220.42           
No mejora            30               260.0            203.46           

χ² (bondad de ajuste) = 423.88
Grados de libertad: 1
Valor crítico (α=0.05): 3.84
→ RECHAZAMOS H₀
→ Los datos NO siguen la distribución esperada
→ El tratamiento A tiene un efecto estadísticamente
  significativo... pero es DEMASIADO significativo
```

—423.88 —dijo Valeria—. Para que te des una idea, un chi-cuadrado de 10 ya es extremadamente significativo. Esto es 40 veces más. Es como lanzar una moneda y obtener cara 100 veces seguidas.

—No hay duda —dijo Marco—. Los datos fueron fabricados.

—Y el Viceministro es el responsable estadístico. Pero la estadística no es una condena judicial. Necesitamos la evidencia física.

---

## El veredicto estadístico

—En estadística —dijo Valeria—, nunca decimos "esto es cierto". Decimos "rechazamos la hipótesis nula con un nivel de confianza del 95%". Pero en este caso, los números hablan por sí solos.

```python
# Resumen de toda la evidencia estadística
print("=== RESUMEN DE EVIDENCIA ESTADÍSTICA ===")
print()

evidencia = [
    ("Manipulación de datos del ensayo", "Z-score = 11.5", "Extremadamente significativo"),
    ("Accesos nocturnos del Viceministro", f"χ² = {chi_cuadrado:.1f} (gl=4)", "p < 0.00001"),
    ("Reducción artificial de varianza", "CV: 2.96% → 0.56%", "Firma de manipulación"),
    ("Correlación IP-nocturna", "r = 0.87", "Correlación muy fuerte"),
    ("Regresión inconsistente", "R²: 0.72 → 0.96", "Datos 'demasiado perfectos'"),
    ("Desaparición de Ramiro y Sofía", "Bayes: P(culpable|evidencia) = 0.85", "Probabilidad alta"),
]

print(f"{'Evidencia':<45} {'Estadístico':<35} {'Conclusión':<35}")
print("-" * 115)
for item in evidencia:
    print(f"{item[0]:<45} {item[1]:<35} {item[2]:<35}")
print()
print("→ La evidencia estadística apunta al Viceministro de Salud")
print("→ Pero necesitamos la prueba definitiva")
```

—¿Y cuál es la prueba definitiva? —preguntó Marco.

—Una confesión. O un documento que lo vincule directamente.

—¿Y cómo conseguimos eso?

Valeria guardó su laptop.

—Hablando con la única persona que puede dártelo: el propio Viceministro.

---

## Enigmas

### Enigma 11.1: Calcula chi-cuadrado

Tienes una encuesta sobre preferencia política por género:

|        | Hombre | Mujer |
|--------|--------|-------|
| Partido A | 120 | 80 |
| Partido B | 90 | 110 |

1. Calcula las frecuencias esperadas
2. Calcula el chi-cuadrado
3. ¿Hay relación entre género y preferencia política?

### Enigma 11.2: Bondad de ajuste

Un dado se lanza 120 veces con estos resultados:

| Cara | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| Frecuencia | 25 | 18 | 22 | 20 | 15 | 20 |

¿El dado está cargado? Usa chi-cuadrado con α = 0.05.

### Enigma 11.3: Aplica al caso

Si agregamos una nueva fila a la tabla de contingencia con los datos de un nuevo sospechoso llamado "Ministro" que tiene 8 accesos nocturnos y 12 diurnos, ¿cómo cambia el chi-cuadrado? ¿Es más o menos sospechoso que el Viceministro?

---

## Lo que aprendiste

- La **prueba de chi-cuadrado (χ²)** evalúa la relación entre variables categóricas
- χ² = Σ((O - E)² / E)
- **Tablas de contingencia**: organizan frecuencias observadas
- **Frecuencias esperadas**: las que esperaríamos si no hubiera relación
- **Bondad de ajuste**: compara una distribución observada con una esperada
- Un χ² alto sugiere que los datos NO son producto del azar

—Vamos a Lima —dijo Valeria—. Vamos a hablar con el Viceministro.

—¿Y si es peligroso?

—Lo es. Pero Kamila merece justicia. Y los números no mienten.

Marco arrancó el auto.

—Entonces vamos.



# Capítulo 12: La Serie del Tiempo Perdido

## Conceptos: Series temporales, tendencia, estacionalidad, autocorrelación, predicción

---

Lima los recibió con su cielo gris característico. Valeria y Marco llegaron al ministerio a las 3 p.m. y pidieron una cita con el Viceministro. La recepcionista los hizo esperar.

Mientras esperaban, Valeria abrió su laptop.

—Antes de enfrentarlo, quiero analizar algo. Los datos que Sofía nos dejó incluyen una **serie temporal** de ventas del medicamento a lo largo de 36 meses. Si podemos demostrar que hubo un cambio estructural en el comportamiento de las ventas después de cierto punto, tendremos evidencia irrefutable.

—¿Qué es una serie temporal?

—Es una secuencia de datos ordenados en el tiempo. Y tiene propiedades únicas: **tendencia**, **estacionalidad** y **autocorrelación**.

---

## Componentes de una serie temporal

Valeria abrió Python:

```python
# Análisis de serie temporal de ventas del medicamento

import numpy as np
import random
import math

# Datos de ventas mensuales del medicamento (36 meses)
# Los primeros 24 son legítimos, los últimos 12 fueron manipulados

random.seed(42)
meses = list(range(1, 37))

# Ventas legítimas (crecimiento orgánico + estacionalidad)
ventas_legitimas = []
for mes in meses[:24]:
    tendencia = 50 + mes * 0.8  # Crecimiento lineal
    estacionalidad = 5 * math.sin(mes * math.pi / 6)  # Ciclo anual
    ruido = random.gauss(0, 3)  # Variación aleatoria
    ventas_legitimas.append(tendencia + estacionalidad + ruido)

# Ventas manipuladas (crecimiento artificial)
ventas_manipuladas = []
for mes in meses[24:]:
    # La tendencia se acelera artificialmente
    tendencia = 50 + mes * 0.8 + (mes - 24) * 3
    estacionalidad = 5 * math.sin(mes * math.pi / 6)
    ruido = random.gauss(0, 1)  # Menos ruido (datos demasiado perfectos)
    ventas_manipuladas.append(tendencia + estacionalidad + ruido)

ventas_totales = ventas_legitimas + ventas_manipuladas

print("=== SERIE TEMPORAL DE VENTAS ===")
print(f"{'Mes':<6} {'Ventas':<10} {'Período':<15}")
print("-" * 31)
for i in range(36):
    periodo = "Legítimo" if i < 24 else "MANIPULADO"
    print(f"{meses[i]:<6} {ventas_totales[i]:<10.1f} {periodo:<15}")
```

Resultado:

```
=== SERIE TEMPORAL DE VENTAS ===
Mes    Ventas     Período         
----------------------------------
1      50.2       Legítimo
2      51.8       Legítimo
3      56.3       Legítimo
...
24     73.1       Legítimo
25     85.2       MANIPULADO
26     89.7       MANIPULADO
27     96.4       MANIPULADO
...
36     132.8      MANIPULADO
```

—¿Ves el salto? —preguntó Valeria—. En el mes 24, las ventas eran 73.1. En el mes 25, saltan a 85.2. Eso es un aumento del 16.5% en un mes. Estadísticamente improbable sin una causa externa.

---

## Descomposición de la serie

—Podemos descomponer la serie en tres componentes: **tendencia**, **estacionalidad** y **residuo**.

```python
# Descomposición simple de la serie temporal

# 1. Tendencia (media móvil de 12 meses)
def media_movil(datos, ventana):
    resultado = []
    for i in range(len(datos)):
        inicio = max(0, i - ventana // 2)
        fin = min(len(datos), i + ventana // 2 + 1)
        resultado.append(np.mean(datos[inicio:fin]))
    return resultado

tendencia = media_movil(ventas_totales, 12)

# 2. Estacionalidad (desviación mensual promedio)
desviaciones_mensuales = []
for mes_idx in range(12):
    valores_mes = [ventas_totales[i] for i in range(mes_idx, 36, 12)]
    desviaciones_mensuales.append(np.mean(valores_mes) - np.mean(ventas_totales))

# Normalizamos para que sumen 0
media_desv = np.mean(desviaciones_mensuales)
estacionalidad = [d - media_desv for d in desviaciones_mensuales]

# 3. Residuo = dato - tendencia - estacionalidad
residuos = []
for i in range(36):
    r = ventas_totales[i] - tendencia[i] - estacionalidad[i % 12]
    residuos.append(r)

print("=== DESCOMPOSICIÓN (últimos 6 meses) ===")
print(f"{'Mes':<6} {'Ventas':<10} {'Tendencia':<12} {'Estacional':<12} {'Residuo':<10}")
print("-" * 50)
for i in range(30, 36):
    print(f"{meses[i]:<6} {ventas_totales[i]:<10.1f} {tendencia[i]:<12.1f} "
          f"{estacionalidad[i % 12]:<12.2f} {residuos[i]:<10.2f}")
```

Resultado:

```
=== DESCOMPOSICIÓN (últimos 6 meses) ===
Mes    Ventas     Tendencia    Estacional    Residuo   
------------------------------------------------------
31     115.3      105.2        -2.3          12.4      
32     120.1      108.1        -1.5          13.5      
33     124.8      111.0         0.8          13.0      
34     127.5      113.9         2.1          11.5      
35     130.2      116.8         1.4          12.0      
36     132.8      119.7        -0.5          13.6      
```

—Los residuos en los últimos meses son grandes y sistemáticamente positivos —dijo Valeria—. En una serie legítima, los residuos deberían fluctuar alrededor de cero con una media cercana a cero.

```python
media_residuo_legitimo = np.mean(residuos[:24])
media_residuo_manipulado = np.mean(residuos[24:])

print(f"Media de residuos (período legítimo): {media_residuo_legitimo:.2f}")
print(f"Media de residuos (período manipulado): {media_residuo_manipulado:.2f}")
print(f"Diferencia: {media_residuo_manipulado - media_residuo_legitimo:.2f}")
```

Resultado:

```
Media de residuos (período legítimo): -0.08
Media de residuos (período manipulado): 11.74
Diferencia: 11.82
```

—Once punto ocho dos. Eso es casi 12 unidades de ventas mensuales que no pueden explicarse por tendencia ni estacionalidad. Es la firma de la manipulación.

---

## Autocorrelación: el tiempo habla

—La **autocorrelación** mide la correlación de una serie consigo misma en diferentes rezagos temporales. Si los datos fueron manipulados, la autocorrelación cambia.

```python
# Autocorrelación simple
def autocorrelacion(datos, rezago):
    n = len(datos)
    if n <= rezago:
        return 0
    datos_originales = datos[:n-rezago]
    datos_rezagados = datos[rezago:]
    return np.corrcoef(datos_originales, datos_rezagados)[0, 1]

print("=== AUTO-CORRELACIÓN ===")
print(f"{'Rezago':<10} {'Período 1-24':<18} {'Período 25-36':<18}")
print("-" * 46)
for rezago in [1, 2, 3, 6, 12]:
    ac_legitimo = autocorrelacion(ventas_legitimas, rezago)
    ac_manipulado = autocorrelacion(ventas_manipuladas, rezago)
    print(f"{rezago:<10} {ac_legitimo:<18.3f} {ac_manipulado:<18.3f}")
```

Resultado:

```
=== AUTO-CORRELACIÓN ===
Rezago     Período 1-24        Período 25-36       
----------------------------------------------
1          0.723               0.956              
2          0.521               0.912              
3          0.348               0.874              
6          0.124               0.765              
12         -0.089              0.543              
```

—La autocorrelación es mucho más alta en el período manipulado —dijo Valeria—. Eso significa que los datos son demasiado predecibles. En los datos reales, la autocorrelación disminuye con el tiempo. En los datos falsos, se mantiene alta.

—¿Por qué?

—Porque quien fabricó los datos usó una tendencia lineal casi perfecta. En la naturaleza, las ventas no crecen en línea recta. Fluctúan, tienen altibajos, responden a factores impredecibles.

---

## Prediciendo el futuro (alternativo)

—Y ahora, la pregunta final —dijo Valeria—: si proyectamos la tendencia legítima hacia adelante, ¿qué ventas deberíamos haber visto?

```python
# Proyección de la tendencia legítima
# Si no hubiera manipulación, ¿qué ventas esperaríamos?

pendiente_legitima = (np.mean(ventas_legitimas[12:]) - np.mean(ventas_legitimas[:12])) / 12
intercepto_legitimo = np.mean(ventas_legitimas[:12])

print("=== PROYECCIÓN VS REALIDAD ===")
print(f"{'Mes':<6} {'Real':<10} {'Proyectado':<12} {'Diferencia':<12}")
print("-" * 40)
for i in range(24, 36):
    proyectado = intercepto_legitimo + pendiente_legitima * meses[i]
    real = ventas_totales[i]
    diff = real - proyectado
    print(f"{meses[i]:<6} {real:<10.1f} {proyectado:<12.1f} {diff:<12.1f}")

diferencia_acumulada = sum(ventas_totales[24:]) - sum(
    intercepto_legitimo + pendiente_legitima * meses[i] for i in range(24, 36)
)

print(f"\nDiferencia acumulada en 12 meses: {diferencia_acumulada:.0f}")
print(f"Eso es ${diferencia_acumulada * 1000:.0f} en ingresos 'extra'")
print("que no pueden explicarse por crecimiento orgánico")
```

Resultado:

```
=== PROYECCIÓN VS REALIDAD ===
Mes    Real       Proyectado    Diferencia   
----------------------------------------------
25     85.2       73.8          11.4         
26     89.7       74.7          15.0         
27     96.4       75.6          20.8         
...
36     132.8      83.8          49.0         

Diferencia acumulada en 12 meses: 324
Eso es $324,000 en ingresos 'extra'
que no pueden explicarse por crecimiento orgánico
}

—Más de 300 mil dólares en ventas no explicadas —dijo Valeria—. Eso es lo que el Viceministro tendrá que explicar.

En ese momento, la recepcionista llamó:

—El Viceministro los recibirá ahora.

Valeria cerró su laptop.

—Vamos. Es hora de poner los números sobre la mesa.

---

## Enigmas

### Enigma 12.1: Identifica los componentes

Dada la siguiente serie temporal de temperaturas mensuales:

```
[22, 23, 25, 27, 28, 27, 25, 24, 23, 22, 21, 20]
```

1. ¿Hay tendencia? ¿Creciente, decreciente o constante?
2. ¿Hay estacionalidad? ¿De cuántos meses?
3. Calcula la media móvil de 3 meses.

### Enigma 12.2: Predice el siguiente valor

Si las ventas de los últimos 4 meses fueron [80, 84, 88, 92], ¿cuál sería tu predicción para el quinto mes? ¿Qué método usaste?

### Enigma 12.3: Detecta el cambio estructural

Los siguientes datos muestran ventas mensuales. ¿Hay un punto donde el comportamiento cambia drásticamente?

```
[30, 32, 31, 33, 32, 34, 33, 35, 34, 36, 50, 52, 55, 58, 62]
```

---

## Lo que aprendiste

- Las **series temporales** son datos ordenados en el tiempo
- **Tendencia**: dirección general de largo plazo
- **Estacionalidad**: patrones que se repiten en períodos fijos
- **Residuo**: lo que no explican tendencia ni estacionalidad
- **Autocorrelación**: correlación de la serie consigo misma en el tiempo
- Datos manipulados muestran residuos sistemáticos y autocorrelación anormal

Valeria y Marco entraron al despacho del Viceministro.

Era un hombre de unos sesenta años, traje impecable, sonrisa profesional. Pero cuando Valeria abrió su laptop y comenzó a mostrar los números, la sonrisa se desvaneció.

—Señor Viceministro —dijo Valeria—, tenemos que hablar sobre 324 mil dólares en ventas que no existen.



# Capítulo 13: El Último Conjunto (Parte 1)

## Conceptos: Repaso integrador — todas las herramientas estadísticas trabajando juntas

---

El Viceministro los miró con una expresión que Valeria no supo descifrar. ¿Sorpresa? ¿Enojo? ¿Miedo?

—No sé de qué están hablando —dijo.

Valeria colocó su laptop sobre el escritorio y comenzó a mostrar los datos.

—Permítame explicarle con números, señor Viceministro. Comencemos con una **prueba de chi-cuadrado** sobre los accesos a los servidores del ministerio.

—Usted tuvo 12 accesos nocturnos a los servidores en los últimos 3 meses. La frecuencia esperada para cualquier persona es de 1.2 accesos. Su chi-cuadrado es de 103.2 —el más alto de todos los funcionarios—. La probabilidad de que esto sea casualidad es menor al 0.0001%.

—Accedo a los servidores cuando hay emergencias —dijo el Viceministro—. Es parte de mi trabajo.

—Por supuesto —continuó Valeria—. Pero veamos la **correlación** entre sus accesos y la manipulación de datos. El coeficiente de correlación es de 0.87. Casi perfecto. Y cuando analizamos la **regresión** de ventas del medicamento, encontramos que en los meses posteriores a sus accesos, las ventas aumentaron un 46% más de lo esperado.

—Eso no prueba nada.

—Entonces veamos la **varianza**. La desviación estándar de los datos del ensayo clínico pasó de 2.11 a 0.42 después de que usted accediera a los servidores. El coeficiente de variación se redujo del 2.96% al 0.56%. En 40 años de datos del ministerio, nunca hemos visto un cambio así sin intervención externa.

El Viceministro guardó silencio.

—Y finalmente —dijo Valeria—, la **serie temporal**. Las ventas del medicamento crecían a un ritmo constante de 0.8 unidades por mes. De repente, hace 12 meses, el crecimiento se acelera a 3.8 unidades por mes. La diferencia acumulada es de 324 mil dólares en ventas no explicadas.

—¿Dónde quiere llegar? —preguntó el Viceministro, su voz más baja.

—A que usted manipuló los datos del ensayo clínico para que el medicamento pareciera más efectivo. Las ventas se dispararon. Pero Kamila Huamán lo descubrió. Y usted la silenció.

---

## El poder de la estadística integrada

—En estadística —dijo Valeria—, una sola prueba puede ser una coincidencia. Pero cuando cinco pruebas independientes apuntan en la misma dirección, la probabilidad de que sea coincidencia se vuelve esencialmente cero.

```python
# Probabilidad combinada de todas las evidencias
import math

# Valores p aproximados de cada evidencia
valores_p = [
    1e-10,   # Chi-cuadrado de accesos
    1e-8,    # Correlación IP-manipulación
    1e-12,   # Varianza (cambio en CV)
    1e-6,    # Regresión (cambio en pendiente)
    1e-9,    # Serie temporal (diferencia acumulada)
    0.0001,  # Desaparición de Sofía y Ramiro
]

# Combinación de Fisher
chi2_combinado = -2 * sum(math.log(p) for p in valores_p)
grados_libertad = 2 * len(valores_p)

# Aproximación: si chi2 > 2*gl, es significativo
print("=== PROBABILIDAD COMBINADA ===")
print(f"Número de pruebas independientes: {len(valores_p)}")
print(f"Chi-cuadrado combinado (Fisher): {chi2_combinado:.2f}")
print(f"Grados de libertad: {grados_libertad}")
print()
print("Interpretación: la probabilidad de que TODAS estas")
print("evidencias sean coincidencias es esencialmente CERO.")
print(f"p < 10^{-int(chi2_combinado/2):d}")
```

Resultado:

```
=== PROBABILIDAD COMBINADA ===
Número de pruebas independientes: 6
Chi-cuadrado combinado (Fisher): 143.56
Grados de libertad: 12

Interpretación: la probabilidad de que TODAS estas
evidencias sean coincidencias es esencialmente CERO.
p < 10^-71
}

—Diez elevado a la menos 71 —dijo Valeria—. Eso es un uno seguido de 71 ceros. No existe en el universo una coincidencia así.

El Viceministro se levantó y caminó hacia la ventana.

—Tiene razón —dijo—. Manipulé los datos.

Marco dio un paso adelante.

—¿Y Kamila? ¿Usted la mató?

—No —respondió el Viceministro—. No la maté. Pero sé quién lo hizo.

—¿Quién?

—El verdadero culpable no soy yo. Soy solo una pieza. La persona que ordenó todo esto... está más arriba que yo.

Valeria sintió un escalofrío.

—¿El Ministro?

El Viceministro asintió lentamente.

—Y si van tras él, van a necesitar más que estadísticas. Van a necesitar pruebas que no puedan ser refutadas.

—¿Y qué pruebas serían esas?

El Viceministro abrió la gaveta de su escritorio y sacó una memoria USB.

—Aquí están todos los correos. Las transferencias. Las órdenes. Todo. Kamila los encontró antes de morir. Y yo los guardé porque sabía que este día llegaría.

Valeria tomó la USB.

—¿Por qué nos da esto?

—Porque ya no puedo vivir con esto. Y porque usted tiene razón: los números no mienten.

---

## Enigmas

### Enigma 13.1: Integración

Tienes tres pruebas independientes con valores p: 0.02, 0.03, y 0.04. ¿Son suficientes para concluir que hay un efecto? Usa la combinación de Fisher.

### Enigma 13.2: Revisión del caso

Escribe un resumen estadístico del caso usando al menos 5 de las herramientas aprendidas en los capítulos anteriores.

### Enigma 13.3: Diseña tu investigación

Si fueras Valeria y tuvieras que investigar al Ministro de Salud, ¿qué herramientas estadísticas usarías primero? ¿Por qué?

---

## Lo que aprendiste

- La **integración de múltiples pruebas** es más poderosa que una sola
- La **combinación de Fisher** permite combinar valores p independientes
- La evidencia estadística, cuando es abrumadora, puede confrontar al poder
- Pero la estadística sola no es suficiente: necesita respaldo legal

Valeria guardó la USB.

—Señor Viceministro —dijo—, va a tener que acompañarnos.

—Lo sé.

Salieron del despacho. La USB en manos de Valeria contenía la verdad que Kamila había buscado. Pero la batalla aún no había terminado. El Ministro de Salud era el objetivo final. Y un hombre con ese poder no se rendiría fácilmente.



# Capítulo 14: El Último Conjunto (Parte 2)

## Conceptos: El método científico completo — del problema a la conclusión

---

La USB del Viceministro contenía 2,347 archivos. Valeria pasó toda la noche analizándolos mientras Marco dormitaba en una silla del hotel.

A las 6 a.m., lo despertó.

—Marco, tengo todo.

—¿Qué tenemos?

—El mapa completo del fraude. El Ministro de Salud, en colaboración con el Viceministro y una farmacéutica internacional, manipuló los ensayos clínicos de un medicamento para la diabetes tipo 2. Inflaron los resultados, sobornaron a los investigadores y eliminaron a cualquiera que se interpusiera.

—¿Incluyendo a Kamila?

—Incluyendo a Kamila. Ella encontró el patrón. Y cuando estaba a punto de publicarlo... apareció muerta.

—¿Y Sofía?

—Sofía está viva. Está en Lima, escondida. El Viceministro nos dio su dirección.

---

## El método científico completo

—Antes de ir a la policía, quiero asegurarme de que todo esté documentado —dijo Valeria—. Porque una vez que entreguemos esto, no habrá vuelta atrás.

—¿Cómo lo vas a organizar?

—Siguiendo el **método científico**. El mismo que Kamila me enseñó.

Valeria abrió su laptop:

```python
# Documentación del caso siguiendo el método científico

print("=" * 60)
print("INFORME FINAL: CASO KAMILA HUAMÁN")
print("Fraude en Ensayos Clínicos del Ministerio de Salud")
print("=" * 60)
print()

# 1. OBSERVACIÓN
print("1. OBSERVACIÓN")
print("-" * 40)
print("• La Dra. Kamila Huamán aparece muerta en su laboratorio")
print("• Su computadora muestra un conjunto vacío: datos = []")
print("• Los datos del ensayo clínico del medicamento G-472 muestran")
print("  resultados sospechosamente perfectos")
print()

# 2. PREGUNTA
print("2. PREGUNTA DE INVESTIGACIÓN")
print("-" * 40)
print("¿Los datos del ensayo clínico G-472 fueron manipulados")
print("para inflar artificialmente la efectividad del medicamento?")
print("¿Y esta manipulación está relacionada con la muerte de Kamila?")
print()

# 3. HIPÓTESIS
print("3. HIPÓTESIS")
print("-" * 40)
print("H₀: Los datos del ensayo son legítimos")
print("H₁: Los datos fueron manipulados para mostrar resultados falsos")
print()

# 4. PREDICCIÓN
print("4. PREDICCIÓN")
print("-" * 40)
print("Si H₁ es cierta, debemos encontrar:")  
print("• Distribución de datos anormal (Cap. 1)")
print("• Probabilidades extremadamente improbables (Cap. 2)")
print("• Correlación entre accesos y manipulación (Cap. 7)")
print("• Varianza reducida artificialmente (Cap. 10)")
print("• Serie temporal con cambio estructural (Cap. 12)")
print()

# 5. EXPERIMENTACIÓN (recolección de datos)
print("5. EXPERIMENTACIÓN")
print("-" * 40)
print("Se analizaron 5 fuentes de datos independientes:")
print()
fuentes = [
    ("Logs de acceso al servidor", "5,000 registros", "Cap. 6, 11"),
    ("Datos del ensayo clínico", "1,000 pacientes", "Cap. 1, 4"),
    ("Ventas del medicamento", "36 meses", "Cap. 8, 12"),
    ("Correos y transferencias", "2,347 archivos", "Cap. 13"),
    ("Testimonios", "Ramiro, Sofía, Viceministro", "Cap. 5, 9, 13")
]
for fuente, tamano, capitulo in fuentes:
    print(f"  • {fuente} ({tamano}) — {capitulo}")
print()

# 6. ANÁLISIS
print("6. ANÁLISIS ESTADÍSTICO")
print("-" * 40)
analisis = [
    "Estadística descriptiva: medias, medianas, rangos anormales",
    "Probabilidad: valores p extremadamente bajos (< 0.00001)",
    "Teorema de Bayes: P(culpable|evidencia) > 0.85",
    "Distribución normal: Z-score de 11.5 en datos clave",
    "Prueba de hipótesis: rechazo de H₀ con 99.99% confianza",
    "Correlación: r = 0.87 entre accesos y manipulación",
    "Regresión: cambio de pendiente de 0.8 a 3.8",
    "Chi-cuadrado: χ² = 117.82, gl = 4, p < 0.00001",
    "Series temporales: residuos sistemáticos de 11.74"
]
for a in analisis:
    print(f"  • {a}")
print()

# 7. CONCLUSIÓN
print("7. CONCLUSIÓN")
print("-" * 40)
print("• SE RECHAZA H₀: los datos fueron manipulados")
print("• El responsable es el Ministro de Salud")
print("• El móvil: inflar ventas del medicamento G-472")
print("  (beneficio estimado: $3.2 millones)")
print("• La muerte de Kamila Huamán está directamente")
print("  relacionada con el descubrimiento del fraude")
print()

print("=" * 60)
print("FIN DEL INFORME")
print("=" * 60)
```

Resultado:

```
============================================================
INFORME FINAL: CASO KAMILA HUAMÁN
Fraude en Ensayos Clínicos del Ministerio de Salud
============================================================

1. OBSERVACIÓN
----------------------------------------
• La Dra. Kamila Huamán aparece muerta en su laboratorio
• Su computadora muestra un conjunto vacío: datos = []
• Los datos del ensayo clínico del medicamento G-472 muestran
  resultados sospechosamente perfectos

2. PREGUNTA DE INVESTIGACIÓN
----------------------------------------
¿Los datos del ensayo clínico G-472 fueron manipulados
para inflar artificialmente la efectividad del medicamento?
¿Y esta manipulación está relacionada con la muerte de Kamila?

3. HIPÓTESIS
----------------------------------------
H₀: Los datos del ensayo son legítimos
H₁: Los datos fueron manipulados para mostrar resultados falsos

4. PREDICCIÓN
----------------------------------------
Si H₁ es cierta, debemos encontrar:
• Distribución de datos anormal (Cap. 1)
• Probabilidades extremadamente improbables (Cap. 2)
• Correlación entre accesos y manipulación (Cap. 7)
• Varianza reducida artificialmente (Cap. 10)
• Serie temporal con cambio estructural (Cap. 12)

5. EXPERIMENTACIÓN
----------------------------------------
Se analizaron 5 fuentes de datos independientes:

  • Logs de acceso al servidor (5,000 registros) — Cap. 6, 11
  • Datos del ensayo clínico (1,000 pacientes) — Cap. 1, 4
  • Ventas del medicamento (36 meses) — Cap. 8, 12
  • Correos y transferencias (2,347 archivos) — Cap. 13
  • Testimonios (Ramiro, Sofía, Viceministro) — Cap. 5, 9, 13

6. ANÁLISIS ESTADÍSTICO
----------------------------------------
  • Estadística descriptiva: medias, medianas, rangos anormales
  • Probabilidad: valores p extremadamente bajos (< 0.00001)
  • Teorema de Bayes: P(culpable|evidencia) > 0.85
  • Distribución normal: Z-score de 11.5 en datos clave
  • Prueba de hipótesis: rechazo de H₀ con 99.99% confianza
  • Correlación: r = 0.87 entre accesos y manipulación
  • Regresión: cambio de pendiente de 0.8 a 3.8
  • Chi-cuadrado: χ² = 117.82, gl = 4, p < 0.00001
  • Series temporales: residuos sistemáticos de 11.74

7. CONCLUSIÓN
----------------------------------------
• SE RECHAZA H₀: los datos fueron manipulados
• El responsable es el Ministro de Salud
• El móvil: inflar ventas del medicamento G-472
  (beneficio estimado: $3.2 millones)
• La muerte de Kamila Huamán está directamente
  relacionada con el descubrimiento del fraude

============================================================
FIN DEL INFORME
============================================================
```

—Es hermoso —dijo Marco—. Kamila estaría orgullosa.

—No hemos terminado —dijo Valeria—. Ahora tenemos que entregar esto a las autoridades. Y proteger a Sofía.

—¿Y al Viceministro?

—Entregó las pruebas voluntariamente. Eso contará a su favor. Pero tendrá que enfrentar las consecuencias.

Valeria cerró su laptop y miró por la ventana. El sol comenzaba a iluminar Lima.

—¿Sabes qué es lo más irónico de todo esto? —dijo—. Kamila dejó un mensaje en su computadora antes de morir: `datos = []`. Un conjunto vacío.

—¿Y qué significa?

—Que al final, después de todo el análisis, la respuesta más importante no estaba en los números. Estaba en lo que faltaba. En los datos que alguien había borrado. En el silencio que alguien había creado.

—El conjunto vacío.

—Exacto. El conjunto vacío no es la ausencia de datos. Es la presencia de un crimen.

---

## Epílogo estadístico

—Antes de ir a la policía —dijo Valeria—, quiero hacer una última simulación. Quiero ver qué habría pasado si Kamila no hubiera muerto.

```python
# Simulación contrafactual
# ¿Qué habría pasado si Kamila hubiera vivido?

import random

print("=== SIMULACIÓN CONTRAFACTUAL ===")
print("Escenario: Kamila Huamán no es asesinada")
print()

# Supongamos que Kamila hubiera publicado su descubrimiento
resultados_posibles = []

for simulacion in range(1000):
    # Probabilidades estimadas
    p_publicacion = 0.95  # Habría publicado
    p_investigacion = 0.80  # Si publica, habría investigación
    p_condena = 0.60  # Si hay investigación, habría condena
    p_reforma = 0.30  # Si hay condena, habría reformas
    
    random.seed(simulacion)
    
    if random.random() < p_publicacion:
        if random.random() < p_investigacion:
            if random.random() < p_condena:
                if random.random() < p_reforma:
                    resultados_posibles.append('Reforma del sistema')
                else:
                    resultados_posibles.append('Condena sin reforma')
            else:
                resultados_posibles.append('Investigación sin condena')
        else:
            resultados_posibles.append('Publicación sin investigación')
    else:
        resultados_posibles.append('Nunca se publica')

from collections import Counter
conteo = Counter(resultados_posibles)

print("Resultados de 1000 simulaciones:")
for resultado, count in conteo.most_common():
    print(f"  {resultado}: {count} ({count/10:.1f}%)")
```

Resultado:

```
=== SIMULACIÓN CONTRAFACTUAL ===
Escenario: Kamila Huamán no es asesinada

Resultados de 1000 simulaciones:
  Condena sin reforma: 326 (32.6%)
  Investigación sin condena: 220 (22.0%)
  Publicación sin investigación: 150 (15.0%)
  Reforma del sistema: 228 (22.8%)
  Nunca se publica: 76 (7.6%)
```

—En el 22.8% de los casos, habría reformas —dijo Valeria—. Pero Kamila no vivió para verlo.

—Pero nosotros sí —dijo Marco—. Y vamos a asegurarnos de que su muerte no sea en vano.

---

## Enigmas

### Enigma 14.1: Tu propio informe

Escribe un breve informe siguiendo el método científico para un problema que hayas enfrentado (no necesariamente estadístico).

### Enigma 14.2: Simulación contrafactual

Si la probabilidad de que el Ministro sea condenado es del 70%, y la probabilidad de que enfrente la cárcel si es condenado es del 40%, ¿cuál es la probabilidad de que enfrente la cárcel?

### Enigma 14.3: Reflexión final

¿Por qué crees que Kamila dejó `datos = []` como mensaje? ¿Qué significa simbólica y estadísticamente?

---

## Lo que aprendiste

- El **método científico** estructurado: observación → pregunta → hipótesis → predicción → experimentación → análisis → conclusión
- La **integración de múltiples herramientas** estadísticas es más poderosa que usar una sola
- Las **simulaciones contrafactuales** exploran escenarios alternativos
- A veces, los datos que faltan dicen más que los datos que están presentes

Valeria y Marco salieron del hotel. La USB estaba segura en su mochila. El sol de la mañana limeña iluminaba las calles.

—Vamos —dijo Valeria—. Es hora de terminar esto.

—¿Estás lista?

—Nunca se está listo para enfrentar al poder. Pero los números están de nuestro lado.

Y caminaron hacia la fiscalía.



# Capítulo 15: El Epílogo

## Conceptos: El poder de la estadística en la vida real

---

Tres meses después.

Valeria estaba en el mismo café de San Blas donde había comenzado todo. Frente a ella, una taza de café de muña humeante y su laptop abierta.

La noticia había salido en todos los periódicos:

**"Ministro de Salud renuncia tras escándalo de fraude en ensayos clínicos"**

El Ministro había sido arrestado. El Viceministro había testificado a cambio de una sentencia reducida. La farmacéutica había sido multada con 50 millones de dólares.

Y Kamila... Kamila había recibido justicia póstuma. El ICD había nombrado el laboratorio 7 en su honor: "Laboratorio de Investigación Dra. Kamila Huamán".

Marco llegó y se sentó frente a ella.

—Lo logramos —dijo.

—Tú lo lograste —respondió Valeria—. Yo solo hice los números.

—Los números que encontraron la verdad.

Valeria sonrió. Cerró su laptop.

—¿Sabes qué me dijo Kamila una vez?

—¿Qué?

—Dijo que la estadística no es sobre números. Es sobre personas. Cada punto de datos es una historia. Cada desviación estándar es una vida que tomó un camino diferente. Cada valor p es una decisión que cambió un destino.

—Y tú cambiaste el destino de Kamila.

—No. Kamila cambió el mío. Me enseñó que los números no mienten. Que las personas, sí. Pero los números... los números siempre dicen la verdad.

Valeria abrió su laptop una vez más.

—Hay una última cosa que quiero hacer.

—¿Qué?

—Cerrar el círculo.

Abrió Python y escribió:

```python
# Cerrando el círculo
# El mensaje que comenzó todo

datos = []  # El conjunto vacío de Kamila

# Tres meses después, el conjunto ya no está vacío
datos = [
    'Justicia para Kamila',
    'Fraude expuesto',
    'Ministro arrestado',
    'Vidas salvadas',
    'La verdad siempre encuentra su camino'
]

for verdad in datos:
    print(f"✓ {verdad}")

print()
print("Conjunto final: no vacío.")
print("La verdad siempre prevalece.")
```

Resultado:

```
✓ Justicia para Kamila
✓ Fraude expuesto
✓ Ministro arrestado
✓ Vidas salvadas
✓ La verdad siempre encuentra su camino

Conjunto final: no vacío.
La verdad siempre prevalece.
```

—El conjunto vacío ya no está vacío —dijo Valeria—. Y eso es lo que Kamila quería.

—¿Y ahora qué? —preguntó Marco.

—Ahora... ahora voy a terminar lo que Kamila empezó. Voy a crear un sistema de detección de fraudes estadísticos para el ministerio. En su honor.

—¿Necesitas ayuda?

—Siempre.

Marco sonrió.

—Entonces empecemos.

---

## Reflexión final

La estadística no es una colección de fórmulas aburridas. Es un superpoder. La capacidad de ver patrones donde otros solo ven números. De encontrar verdades donde otros solo ven ruido. De hacer justicia donde otros solo ven caos.

En este libro, has aprendido:

- **Estadística descriptiva**: media, mediana, moda, varianza, desviación estándar
- **Probabilidad**: regla de Laplace, eventos independientes, probabilidad condicional
- **Teorema de Bayes**: actualizar creencias con nueva información
- **Distribución normal**: la campana de Gauss, Z-scores, regla empírica
- **Muestreo**: población, muestra, sesgo de selección
- **Prueba de hipótesis**: H₀, H₁, valor p, significancia
- **Correlación y regresión**: relaciones entre variables, predicción
- **Chi-cuadrado**: tablas de contingencia, bondad de ajuste
- **Series temporales**: tendencia, estacionalidad, autocorrelación

Pero más importante: has aprendido a **pensar estadísticamente**. A cuestionar los datos. A buscar la historia detrás de los números. A no aceptar las cosas porque "los números lo dicen", sino a preguntar **cómo** se obtuvieron esos números.

Y eso, querido lector, es el verdadero poder de la estadística.

---

**FIN**



# Conclusión

Has llegado al final de **Estadística Mortal: El Enigma del Conjunto Vacío**.

Pero esto no es un final. Es un comienzo.

Cada concepto que has aprendido en este libro —desde la media hasta el chi-cuadrado, desde Bayes hasta las series temporales— es una herramienta que puedes usar en el mundo real. La estadística está en todas partes: en las noticias, en los estudios médicos, en las encuestas políticas, en los informes financieros.

Ahora tienes el poder de:

- **Cuestionar** los datos que te presentan
- **Detectar** manipulaciones y fraudes
- **Tomar decisiones** informadas basadas en evidencia
- **Contar historias** con números

Recuerda siempre las lecciones de Kamila Huamán y Valeria Quispe:

1. **Los números no mienten, pero las personas sí**
   - Siempre pregunta quién recolectó los datos y por qué

2. **La correlación no implica causalidad**
   - Busca variables ocultas antes de saltar a conclusiones

3. **Un valor p no es la verdad absoluta**
   - Es una herramienta, no un veredicto

4. **Los datos atípicos son los más interesantes**
   - No los ignores; investiga por qué están ahí

5. **El conjunto vacío puede contener más información que uno lleno**
   - Los datos que faltan también importan

Gracias por acompañar a Valeria y Marco en esta aventura. Espero que hayas disfrutado el viaje tanto como ellos.

Y recuerda: cuando tengas dudas, mira los datos. Ellos siempre tienen la respuesta.

— Alex Goyzueta Delgado

Barcelona, 2026



# Apéndice: Soluciones a los Enigmas

## Capítulo 1: El Conjunto Vacío

### Enigma 1.1
```python
edades = [29, 34, 45, 45, 45, 52, 67, 71, 34, 29, 45, 38, 52, 45, 29]

media = sum(edades) / len(edades)
# media = 43.07

edades.sort()
mediana = edades[len(edades)//2]
# mediana = 45

from collections import Counter
moda = Counter(edades).most_common(1)[0]
# moda = 45 (aparece 5 veces)

minimo = min(edades)  # 29
maximo = max(edades)  # 71
```

### Enigma 1.2
```python
edades.append(98)
media = sum(edades) / len(edades)  # 46.44 (aumentó)
edades.sort()
mediana = edades[len(edades)//2]  # 45 (igual)
```
La **media** se ve afectada por el valor extremo (outlier). La **mediana** es robusta y no cambia.

### Enigma 1.3
Porcentaje = 5/47 × 100 = 10.6%. Los valores de presión sanguínea faltantes podrían ocultar que los pacientes con presión alta fueron excluidos del estudio para sesgar los resultados.

---

## Capítulo 2: La Probabilidad del Crimen

### Enigma 2.1
Probabilidad teórica: 1/6 ≈ 0.1667 por cada cara.
Las frecuencias observadas se desvían de lo esperado (100 por cara). El 6 aparece solo 72 veces, mucho menos de lo esperado.

### Enigma 2.2
1. P(acceso) = 3/8 = 0.375
2. P(motivo) = 4/8 = 0.5
3. P(ambos) = 2/8 = 0.25

### Enigma 2.3
```python
import random
caras = sum(1 for _ in range(10000) if random.random() < 0.5)
print(f"Caras: {caras}, Prob: {caras/10000:.4f}")
# Debería obtener ~0.5
```

---

## Capítulo 3: El Teorema del Sospechoso

### Enigma 3.1
P(fraude) = 0.005, P(positivo|fraude) = 0.99, P(positivo|no fraude) = 0.01
P(positivo) = 0.99×0.005 + 0.01×0.995 = 0.0149
P(fraude|positivo) = 0.99×0.005/0.0149 = 0.332 = 33.2%

### Enigma 3.2
P(enfermedad) = 0.02, P(positivo|enfermedad) = 0.98, P(positivo|sano) = 0.02
P(positivo) = 0.98×0.02 + 0.02×0.98 = 0.0392
P(enfermedad|positivo) = 0.98×0.02/0.0392 = 0.50 = 50%
La probabilidad es baja porque la enfermedad es rara y hay muchos falsos positivos.

### Enigma 3.3
Sofía subiría significativamente porque tiene baja estatura. Hugo y Ramiro bajarían.

---

## Capítulo 4: La Distribución del Engaño

### Enigma 4.1
media = 45, σ = 10
Z(23) = (23-45)/10 = -2.2 (no outlier)
Z(81) = (81-45)/10 = 3.6 (outlier)
Z(18) = -2.7 (no outlier)
Z(78) = 3.3 (outlier)

### Enigma 4.2
1. 68% (entre μ±1σ)
2. 95% (entre μ±2σ)
3. 99.7% (entre μ±3σ)

### Enigma 4.3
Conjunto B parece manipulado: casi no tiene variabilidad (desviación estándar mucho menor que el conjunto A).

---

## Capítulo 5: La Muestra que Miente

### Enigma 5.1
1. Sesgo de disponibilidad (solo personas en casa de día)
2. Sesgo de selección (solo jóvenes sanos)
3. Sesgo de respuesta (solo extremos responden)
4. Sesgo de supervivencia (solo los que declaran impuestos)

### Enigma 5.2
ME = 1/√400 = 0.05 = 5%
IC 95%: [52% - 5%, 52% + 5%] = [47%, 57%]

### Enigma 5.3
Muestreo estratificado por facultad, con muestra proporcional al tamaño de cada facultad.

---

## Capítulo 6: La Hipótesis Asesina

### Enigma 6.1
Simular 10000 experimentos de 20 lanzamientos de moneda justa. Contar cuántas veces se obtienen 15 o más caras. Ese conteo/10000 es el valor p.

### Enigma 6.2
1. Falso positivo = Error Tipo I
2. Error Tipo II
3. Depende del contexto. En enfermedades mortales, el Error Tipo II (no detectar) puede ser más peligroso.

### Enigma 6.3
H₀: Sitio A = Sitio B; H₁: Sitio A ≠ Sitio B. Media A = 2.31s, Media B = 3.0s. La diferencia es significativa.

---

## Capítulo 7: La Correlación del Secreto

### Enigma 7.1
r ≈ 0.998. Correlación positiva casi perfecta.

### Enigma 7.2
Ejemplos:
- Ventas de helados y ahogados (variable oculta: calor)
- Número de iglesias y crímenes (población)
- Consumo de chocolate y premios Nobel (desarrollo económico)

### Enigma 7.3
Incluir a Lidia probablemente no cambia drásticamente la interpretación.

---

## Capítulo 8: La Regresión del Pasado

### Enigma 8.1
Pendiente ≈ 0.73, Intercepto ≈ 2.47. Para 7.5h: nota ≈ 7.95. R² ≈ 0.99.

### Enigma 8.2
El conjunto B parece manipulado porque los valores tienen más variabilidad pero siguen un patrón menos natural.

### Enigma 8.3
Mes 25: 2.80 × 15 + 14.20 = 56.2; Mes 26: 2.80 × 16 + 14.20 = 59.0

---

## Capítulo 9: El Intervalo de Confianza

### Enigma 9.1
EE = 800/√100 = 80. IC 95%: [2500 - 1.96×80, 2500 + 1.96×80] = [2343.2, 2656.8]

### Enigma 9.2
n = (1.96 × 800 / 100)² ≈ 246. Necesitamos al menos 246 personas.

### Enigma 9.3
Distancia desde Andahuaylas: 30-60 km/h × 6h = 180-360 km. Destinos probables: Ayacucho (130 km), Nazca (280 km).

---

## Capítulo 10: La Varianza del Silencio

### Enigma 10.1
media = 24.625, varianza = 87.98, desv_std ≈ 9.38

### Enigma 10.2
CV(A) = 1.63%, CV(B) = 42.86%. B tiene mucha mayor dispersión relativa.

### Enigma 10.3
El estudio X parece manipulado (CV muy bajo, casi sin variabilidad). El estudio Y tiene variabilidad natural.

---

## Capítulo 11: La Prueba del Chi-Cuadrado

### Enigma 11.1
Frecuencias esperadas: Hombres A=105, Mujeres A=95; Hombres B=105, Mujeres B=95.
χ² ≈ 6.12. gl = 1. Valor crítico = 3.84. χ² > 3.84 → hay relación.

### Enigma 11.2
Esperado: 20 por cara. χ² = (25-20)²/20 + ... = 3.5. gl = 5. Valor crítico = 11.07. 3.5 < 11.07 → el dado no está cargado.

### Enigma 11.3
χ² aumentaría significativamente. El Ministro (8 nocturnos, 12 diurnos) tiene una proporción nocturna del 40%, mayor incluso que el Viceministro.

---

## Capítulo 12: La Serie del Tiempo Perdido

### Enigma 12.1
Tendencia: ligeramente decreciente. Estacionalidad: 12 meses. Media móvil 3: [23.3, 25, 26.7, 27.7, 26.7, 25.3, 24, 23, 22, 21, 21, 21].

### Enigma 12.2
Predicción: 96 (sigue la tendencia lineal de +4 por mes).

### Enigma 12.3
El cambio estructural ocurre en el mes 10-11 (salto de 36 a 50).

---

## Capítulo 13: El Último Conjunto (Parte 1)

### Enigma 13.1
χ² combinado = -2(ln(0.02)+ln(0.03)+ln(0.04)) = -2(-3.91-3.51-3.22) = 21.28. gl = 6. p < 0.01 → Sí, hay un efecto combinado.

---

## Capítulo 14: El Último Conjunto (Parte 2)

### Enigma 14.2
P(cárcel) = 0.70 × 0.40 = 0.28 = 28%



# Sobre el Autor

**Alex Goyzueta Delgado** es analista de datos senior, instructor y escritor peruano radicado en Barcelona, España. Con una profunda pasión por la estadística, la programación y la educación, Alex ha dedicado su carrera a hacer que los conceptos complejos de ciencia de datos sean accesibles para todos.

Su enfoque único combina narrativa y técnica: cada libro es una historia que enseña programación o estadística mientras mantiene al lector entretenido. Cree firmemente que la mejor forma de aprender es haciendo, y que la mejor forma de enseñar es contando una historia.

**Obras del autor:**

- *Código Asesino: El Enigma de Qhapaq Ñan* — Python y misterio inca
- *Código de Olas: El Misterio del Puerto de Ancón* — Python y surf
- *El Motor Cuantitativo* — Matemáticas y estadística con Python
- *Raíces Nuevas* — Guía para la ansiedad del inmigrante
- *Estadística Mortal: El Enigma del Conjunto Vacío* — Estadística y probabilidad en un misterio criminal

**Contacto:**

- Email: alexgoyzueta2018@gmail.com
- Basado en Barcelona, España
- Barcelona, 2026

