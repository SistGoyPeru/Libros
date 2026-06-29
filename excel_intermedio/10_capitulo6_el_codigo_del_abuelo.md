# Capítulo 6: El Código del Abuelo

## Tema: Herramientas de datos — texto en columnas, quitar duplicados, validación

---

El cuaderno azul estaba exactamente donde Sofía recordaba. En una caja de cartón detrás del archivador metálico, cubierto de polvo pero perfectamente conservado. La portada decía, en la caligrafía impecable de Don Rafael: *"Registros Varios — No extraviar"*.

Sofía sopló el polvo y abrió el cuaderno. Las páginas estaban llenas de anotaciones en columnas: fechas, códigos, números. Pero no era una tabla ordenada como las de Excel. Era un caos de información: a veces los datos estaban separados por guiones, a veces por espacios, a veces por barras inclinadas.

—El abuelo tenía un sistema —dijo Sofía, mostrándole el cuaderno a Carlos—. Pero no era consistente.

—Eso es típico de los datos del mundo real —respondió Carlos—. La gente escribe la misma información de mil maneras diferentes. Y cuando la pasas a Excel, terminas con un desastre.

—¿Cómo se limpia un desastre así?

—Con las **herramientas de datos** de Excel. Son como el equipo de limpieza de tu hoja de cálculo.

---

## Texto en columnas: separar lo que está junto

—Mira esta línea del cuaderno —dijo Sofía—: "15/01/2005-AX-1001-1450". Todo junto, separado por guiones.

—En Excel, eso es una sola celda con un texto. Pero en realidad son cuatro datos diferentes: fecha, código, tipo y valor. Necesitamos **separarlos**.

La herramienta es **Texto en columnas**:

1. Selecciona la columna con los datos combinados
2. Ve a **Datos > Texto en columnas**
3. Se abre un asistente de tres pasos

**Paso 1:** Elige "Delimitados" (si los datos están separados por un carácter) o "Ancho fijo" (si están en columnas de ancho constante).

—En este caso, "Delimitados".

**Paso 2:** Elige el delimitador. Puede ser tabulador, punto y coma, coma, espacio, o "Otro". Escribe el guión (-).

—En la vista previa, Excel muestra cómo quedarán separados los datos.

**Paso 3:** Elige el formato de cada columna (General, Texto, Fecha) y el destino (dónde colocar los datos separados).

—Acepta.

Instantáneamente, la columna original se dividió en cuatro columnas:

| Fecha | Código | Tipo | Valor |
|------|--------|------|-------|
| 15/01/2005 | 1001 | AX | 1450 |

—¡Magia! —exclamó Sofía.

—No es magia, es Excel. Y hay más opciones:

**Ancho fijo:** Cuando los datos están alineados en columnas de ancho fijo (como los datos de mainframe). En lugar de elegir un delimitador, arrastras líneas para indicar dónde cortar.

**Delimitadores múltiples:** Puedes marcar varios delimitadores. Por ejemplo, si los datos usan guiones y espacios, Excel tratará ambos como separadores.

**Tratar delimitadores consecutivos como uno solo:** Útil cuando hay espacios extras: "Hola    mundo" se trata como "Hola" y "mundo", no "Hola", "", "", "mundo".

---

## Quitar duplicados: datos únicos

—Ahora que tenemos los datos separados, revisemos si hay duplicados —dijo Carlos—. En diez años de registros, es probable que algunos estén repetidos.

**Datos > Quitar duplicados**

—Selecciona todo el rango. En el cuadro de diálogo, elige las columnas que deben ser únicas. Si marcas todas las columnas, eliminará filas completamente idénticas. Si marcas solo "Código", eliminará filas con códigos repetidos.

Sofía seleccionó todas las columnas. Excel informó: "Se encontraron 12 valores duplicados; se eliminaron. Quedan 988 valores únicos."

—Doce registros duplicados —dijo Sofía—. ¿Por qué el abuelo tendría registros duplicados?

—Tal vez los anotó dos veces sin darse cuenta. O tal vez alguien más los anotó.

—O tal vez los duplicados son una pista —dijo Sofía—. Revisemos cuáles eran.

Carlos le mostró cómo recuperar la información: antes de quitar duplicados, aplica **Formato condicional > Reglas para resaltar celdas > Valores duplicados**. Los duplicados se resaltan en rojo. Puedes revisarlos antes de eliminarlos.

Los doce registros duplicados tenían una característica común: todos eran del tipo AX (ingresos) y todos eran de valores especialmente altos.

—Interesante —murmuró Carlos—. Los valores altos están duplicados. Como si alguien los hubiera registrado dos veces intencionalmente.

—¿Para inflar los ingresos?

—O para ocultar algo. Un movimiento puede disfrazarse entre duplicados.

---

## Validación de datos para calidad

—Ahora que limpiamos los datos, debemos asegurarnos de que los datos nuevos que ingresemos cumplan con ciertos estándares —dijo Carlos—. Para eso sirve la **validación de datos** que vimos antes, pero aplicada a la calidad.

Algunas validaciones útiles para este proyecto:

**Fechas válidas:**
```
Permitir: Fecha
Datos: entre
Fecha inicial: 01/01/2005
Fecha final: 31/12/2015
```

**Códigos con formato específico:**
```
Permitir: Longitud de texto
Datos: igual a
Longitud: 7
```
(Asumiendo que los códigos tipo "AX-1001" tienen 7 caracteres)

**Valores positivos:**
```
Permitir: Decimal
Datos: mayor que
Mínimo: 0
```

—Y la validación más útil de todas —dijo Carlos—: **Personalizada con fórmula**.

—¿Como cuál?

—Que el código comience con las letras permitidas (A, B, C, D):

```
=Y(IZQUIERDA(A2;1)="A"; O(DERECHA(A2;1)="X"))
```

Bueno, esta es muy específica. Una más general:

```
=O(IZQUIERDA(A2;2)="AX"; IZQUIERDA(A2;2)="BX"; IZQUIERDA(A2;2)="CX"; IZQUIERDA(A2;2)="DX")
```

—Así, si alguien escribe "ZX-1001", Excel lo rechazará.

---

## Relleno rápido: el aliado invisible

—Hay otra herramienta que te va a encantar —dijo Carlos—: **Relleno rápido** (Flash Fill). Es como magia predictiva.

—¿Qué hace?

—Reconoce patrones en tus datos y los completa automáticamente. Mira, en tu columna de códigos tienes "AX-1001". Quiero separar las letras de los números. En una columna nueva, escribe "AX" en la primera fila. En la siguiente fila, empieza a escribir "BX"... y Excel te sugerirá el resto.

Sofía probó: escribió "AX" en B2, "BX" en B3. Excel mostró una vista previa en gris para el resto de las celdas. Presionó Enter.

—¡Completó todo!

—Relleno rápido es ideal para:
- Separar nombres completos en nombre y apellido
- Extraer partes de códigos
- Formatear texto inconsistente
- Combinar datos de múltiples columnas

Se activa automáticamente cuando Excel detecta un patrón, o manualmente con **Datos > Relleno rápido** (Ctrl+E).

—Pero cuidado —advirtió Carlos—: Relleno rápido no es dinámico. Si cambias los datos originales, no se actualiza. Es una herramienta de transformación única, no una fórmula.

---

### Enigma 6.1: Limpieza de datos

El cuaderno azul tiene una entrada que dice: "2008/03/15_BX_1002_890_12". En Excel, escribe esto en una celda. Usa **Texto en columnas** con delimitadores "/", "_" para separar todos los componentes.

¿Cuántas columnas obtienes? ¿Reconoció Excel la fecha automáticamente?

---

### Enigma 6.2: Detecta y analiza duplicados

En el archivo secreto original, aplica formato condicional para resaltar duplicados en la columna "Código" + "Valor_A" combinados (usa una columna auxiliar con =A2&B2 para crear un identificador único). ¿Cuántos duplicados exactos hay?

---

### Enigma 6.3: Validación de integridad

Crea una validación personalizada en la columna "Valor_A" que solo acepte valores que sean múltiplos de 10 (pista: usa la función RESIDUO). ¿Cuántos valores en el archivo original NO son múltiplos de 10?

---

## Lo que aprendiste

- **Texto en columnas** separa datos combinados en columnas individuales usando delimitadores o ancho fijo
- **Quitar duplicados** elimina filas repetidas basándose en una o más columnas
- **Relleno rápido** (Flash Fill) detecta patrones y completa datos automáticamente
- La **validación de datos personalizada** con fórmulas asegura la integridad de los datos
- Los datos del mundo real casi siempre necesitan limpieza antes de ser analizados

---

—El cuaderno azul tiene más información de la que pensaba —dijo Sofía, hojeando las páginas—. Pero está todo mezclado. Fechas, códigos, nombres de personas...

—¿Nombres? —preguntó Carlos—. ¿Qué nombres?

—Aquí dice "Montenegro" —Sofía señaló una página—. "2009-04-12: Entregado a Montenegro." Y aquí: "2010-11-03: Montenegro confirma."

—El abogado —dijo Carlos—. El mismo que mencionó que tenía instrucciones de tu abuelo.

—¿Qué le habrá entregado el abuelo?

—No lo sé. Pero tal vez sea momento de visitar al señor Montenegro.

Sofía guardó el cuaderno en su mochila. El rompecabezas tenía cada vez más piezas, y algunas empezaban a encajar. Pero todavía faltaba la imagen completa.

—Antes de visitar al abogado —dijo—, quiero entender mejor estos números. Hay algo que no cuadra.

—Mañana te enseño **rangos con nombre** —dijo Carlos—. Te va a ayudar a organizar todo esto de una manera más clara.

—¿Más claro que tener los datos limpios?

—Mucho más. Porque no se trata solo de tener los datos limpios, sino de poder **referenciarlos** de manera que las fórmulas tengan sentido.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
