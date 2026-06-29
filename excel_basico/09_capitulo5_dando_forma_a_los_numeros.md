# Capítulo 5: Dando Forma a los Números

## Formato de Celdas, Formatos Numéricos y Fechas

---

Una semana después, el taller "Mendoza & Hijos" tenía un inventario completo, costos calculados, y precios en soles y dólares. Pero cuando Sofía imprimió los reportes para mostrárselos a Don Manuel, algo no cuadraba.

—Mija —dijo Don Manuel, ajustándose los lentes—, estos números están todos amontonados. No se entiende nada.

Sofía miró la hoja impresa. Tenía razón. Los precios aparecían como 150, 350, 80 —sin el símbolo de soles. Las fechas se veían como números extraños: 45021, 45032, 45045. Los porcentajes eran decimales: 0.18, 0.6667, 0.2590.

—Esto es ilegible —admitió Sofía—. Mi abuelo tenía un sistema de colores para la madera. Necesito un sistema similar para los números.

Don Manuel sonrió.

—Tu abuelo siempre decía que "la presentación es parte del trabajo". Un mueble bien hecho necesita un buen acabado.

Sofía entendió la metáfora. Los datos estaban "en bruto". Necesitaba "lijarlos", "barnizarlos" y darles el acabado final.

---

## El formateo: el barniz de los datos

Dar **formato** a una celda en Excel significa cambiar su apariencia sin alterar su valor subyacente. Es como barnizar la madera: el material sigue siendo el mismo, pero su presentación mejora drásticamente.

### Cómo acceder al formato de celdas

1. Selecciona la celda o rango que quieres formatear
2. Haz clic derecho y selecciona **Formato de celdas** (o presiona Ctrl + 1)
3. Se abrirá un cuadro de diálogo con varias pestañas

Las pestañas principales son:

- **Número:** Controla cómo se muestran los números
- **Alineación:** Controla la posición del contenido
- **Fuente:** Controla el tipo de letra, tamaño, color
- **Borde:** Agrega bordes a las celdas
- **Relleno:** Controla el color de fondo
- **Proteger:** Bloquea celdas para evitar cambios

---

## Formatos numéricos

Sofía comenzó con los formatos numéricos. Seleccionó la columna de precios y abrió **Formato de celdas > Número**.

### Categorías de formato numérico

| Categoría | Descripción | Ejemplo |
|-----------|-------------|---------|
| General | Sin formato específico | 150 |
| Número | Con decimales y separador de miles | 150.00 |
| Moneda | Con símbolo de moneda | S/ 150.00 |
| Contabilidad | Moneda alineada | S/ 150.00 |
| Fecha | Muestra fechas | 15/01/2026 |
| Hora | Muestra horas | 14:30:00 |
| Porcentaje | Multiplica por 100 y añade % | 18% |
| Fracción | Muestra como fracción | 1/2 |
| Científico | Notación científica | 1.50E+02 |
| Texto | Trata el número como texto | 00150 |

### Moneda

Sofía seleccionó el rango de precios y aplicó **Moneda** con símbolo "S/." (soles peruanos):

150 → S/ 150.00
350 → S/ 350.00
80 → S/ 80.00

—Mucho mejor —dijo—. Ahora se ve como dinero de verdad.

También aplicó moneda a los costos y ganancias. La hoja comenzaba a verse profesional.

### Fechas

Las fechas en Excel son números seriales. El 1 de enero de 1900 es el número 1. El 15 de enero de 2026 es el número 46046.

Sofía seleccionó la columna de fechas de ingreso y eligió el formato **Fecha** con el tipo "14 de marzo de 2026":

45021 → 15 de enero de 2026
45032 → 26 de enero de 2026

—Ahora sí se entiende —sonrió.

### Porcentajes

Para la columna de % de ganancia, Sofía aplicó **Porcentaje** con 2 decimales:

0.6667 → 66.67%
0.2590 → 25.90%
0.6327 → 63.27%

### Decimales

Para los precios unitarios, usó **Número** con 2 decimales y separador de miles:

45 → 45.00
1500 → 1,500.00

---

## El mensaje oculto del abuelo

Mientras exploraba el archivo original de su abuelo, Sofías descubrió algo extraño. En la celda D5 (Precio Unitario del Triplay), el valor era 35. Pero cuando seleccionó la celda, notó que la barra de fórmulas mostraba algo diferente.

La celda tenía formato condicional.

—¿Qué es esto? —se preguntó.

En el cuaderno de su abuelo, encontró una anotación:

*"El formato condicional es como un código secreto. Cuando un número cumple una condición, la celda cambia de color. Así sé qué madera pedir sin tener que leer los números."*

Sofía investigó y descubrió que Don Rafael había configurado **Formato Condicional** en la columna de Cantidad:

- Si la cantidad era menor a 20 → la celda se ponía **roja** (necesita reposición urgente)
- Si la cantidad estaba entre 20 y 50 → la celda se ponía **amarilla** (comprar pronto)
- Si la cantidad era mayor a 50 → la celda se ponía **verde** (stock suficiente)

Para ver esto, Sofía fue a **Inicio > Formato Condicional > Administrar reglas**.

Allí encontró tres reglas que su abuelo había creado. Era como un semáforo para el inventario.

—Increíble —murmuró—. Mi abuelo creó un sistema visual para gestionar el stock sin tener que leer los números uno por uno.

### ¿Cómo aplicar formato condicional?

1. Selecciona el rango de celdas
2. Ve a **Inicio > Formato Condicional**
3. Elige una regla (por ejemplo, "Resaltar reglas de celdas > Mayor que...")
4. Establece el valor y el formato (color de relleno, color de fuente, etc.)

Sofía decidió expandir el sistema de su abuelo. Agregó formato condicional para la columna de calidad:

- Si la celda contiene "A" → relleno rojo (madera de primera)
- Si la celda contiene "B" → relleno amarillo (madera de segunda)
- Si la celda contiene "C" → relleno verde (madera de tercera)

Ahora, al ver la hoja, podía identificar instantáneamente la calidad de cada material.

---

## Alineación y fusión de celdas

Sofía también aprendió a mejorar la presentación con alineación:

- **Alinear a la izquierda:** Para texto (títulos, nombres)
- **Centrar:** Para encabezados de tabla
- **Alinear a la derecha:** Para números (estándar contable)
- **Combinar y centrar:** Para títulos que abarcan varias columnas

Para el título de su hoja, Sofía combinó las celdas A1:H1, escribió "INVENTARIO MENDOZA & HIJOS" y lo centró con letra negrita tamaño 14.

—Esto ya parece un documento de verdad —dijo orgullosa.

---

## Colores de relleno y fuente

Sofía aplicó color a los encabezados de las columnas:

1. Seleccionó la fila de encabezados (A2:H2)
2. Relleno de color: azul oscuro
3. Color de fuente: blanco, negrita

El resultado era limpio y profesional. Los encabezados contrastaban con los datos, haciendo la tabla fácil de leer.

---

## Enigmas del Capítulo 5

### Enigma 5.1: Formatea el inventario

Toma el inventario que creaste en los capítulos anteriores y aplícale los siguientes formatos:

1. Columna Precio Unitario: Formato **Moneda** con símbolo S/.
2. Columna Cantidad: Formato **Número** sin decimales.
3. Columna Fecha de Ingreso: Formato **Fecha** largo (ej: "15 de enero de 2026").
4. Título principal: Combinar celdas, centrar, negrita, tamaño 14.
5. Encabezados: Fondo azul, letra blanca, negrita.

### Enigma 5.2: El semáforo del inventario

Aplica formato condicional a la columna Cantidad:

1. Selecciona el rango de cantidades (ej: B2:B11)
2. Ve a **Formato Condicional > Resaltar reglas de celdas > Menor que**
3. Escribe 20 y elige "Relleno rojo claro con texto rojo oscuro"
4. Agrega otra regla: **Entre** 20 y 50, con "Relleno amarillo claro con texto amarillo oscuro"
5. Agrega otra regla: **Mayor que** 50, con "Relleno verde claro con texto verde oscuro"

¿Qué productos están en rojo (necesitan reposición urgente)?

### Enigma 5.3: El código de colores del abuelo

Don Rafael clasificaba los materiales así:

- **Tipo "Madera":** Color de fondo marrón claro
- **Tipo "Herramienta":** Color de fondo gris claro
- **Tipo "Insumo":** Color de fondo blanco

Crea una columna "Tipo" al lado de tus datos y asigna cada producto a una categoría. Luego usa **Formato Condicional > Resaltar reglas de celdas > Texto que contiene...** para aplicar los colores.

¿Cuántos productos de cada tipo tienes?

### Enigma 5.4: Bordes profesionales

Agrega bordes a tu tabla de inventario:

1. Selecciona toda la tabla (incluyendo encabezados)
2. Ve a **Inicio > Bordes > Todos los bordes**
3. Los bordes exteriores deben ser más gruesos. Usa **Bordes > Bordes gruesos exterior**
4. Aplica un borde inferior más grueso a la fila de encabezados

Esto hará que tu tabla se vea profesional y lista para imprimir.

---

## Lo que aprendiste

- El **formato de celdas** mejora la apariencia sin cambiar los valores
- Los **formatos numéricos** incluyen Moneda, Fecha, Porcentaje, Número, etc.
- **Ctrl + 1** abre el cuadro de diálogo Formato de celdas
- El **Formato Condicional** cambia el color de las celdas según reglas
- La **combinación de celdas** y la **alineación** mejoran la presentación
- Los **bordes** y **colores de relleno** hacen las tablas más legibles
- El formato convierte datos crudos en información clara y profesional

---

Sofía se recostó en la silla, contemplando su trabajo. La hoja de cálculo, que antes era un conjunto de números confusos, ahora era un documento claro, ordenado y profesional.

—Don Manuel —llamó—, venga a ver.

El viejo carpintero se acercó, secándose las manos. Miró la pantalla y silbó suavemente.

—Mija, esto parece hecho por un contador de verdad.

—Es el mismo trabajo de mi abuelo —dijo Sofía—. Solo le puse el acabado.

Don Manuel rió, reconociendo la metáfora del barniz.

El taller tenía ahora un inventario, costos, precios y un sistema visual para gestionar el stock. Pero Sofía sabía que necesitaba más. Necesitaba entender las funciones avanzadas de Excel.

Y su abuelo, desde el más allá, todavía tenía mucho que enseñarle.
