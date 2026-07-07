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

