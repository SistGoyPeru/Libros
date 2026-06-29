# Capítulo 2: Pistas Ocultas

## Tema: Validación de datos, listas desplegables, mensajes de entrada

---

—Ayer soñé con el archivo secreto —dijo Sofía mientras servía el café—. Soñé que los números se movían solos y formaban un mapa.

—Eso se llama obsesión —respondió Carlos, mordiendo un pan con mantequilla—. Pero es buena señal. Significa que tu cerebro está procesando el problema.

Eran las ocho de la mañana en el taller. Los primeros rayos de sol se colaban por las persianas de la oficina. Elena ya había abierto el taller y se escuchaba el rumor de los trabajadores preparando la maquinaria.

—Antes de seguir con el archivo —dijo Carlos—, vamos a trabajar con algo que necesitas para el día a día del taller: **validación de datos**.

—¿Validación de qué?

—Verás. Tu mamá me contó que a veces los empleados escriben mal los datos en las hojas de pedidos. Que ponen fechas en formato incorrecto, o escriben "Madera de Cedro" de tres maneras diferentes: "Cedro", "cedro", "CD".

—Es cierto —admitió Sofía—. Es un caos.

—La validación de datos evita ese caos. Controlas qué se puede escribir en cada celda. Es como ponerle un filtro a la entrada de datos.

---

## Listas desplegables: el poder de elegir

—Empecemos con algo simple: **listas desplegables**.

Carlos abrió una hoja nueva en Excel y creó una tabla simple para los pedidos del taller:

| Pedido | Cliente | Producto | Madera | Cantidad | Fecha |
|--------|---------|----------|--------|----------|-------|
| 001 | | | | | |

—Selecciona la columna "Madera" —dijo Carlos—. Ve a **Datos > Validación de datos > Configuración**.

En el cuadro de diálogo:
1. En "Permitir", selecciona **Lista**
2. En "Origen", escribe: `Caoba, Cedro, Roble, Pino, Tornillo, Nogal, Cerezo`

—Acepta.

Sofía hizo clic en la celda de la columna Madera. Apareció una pequeña flecha hacia abajo. Al hacer clic, se desplegó la lista de maderas.

—¡Qué útil! —exclamó—. Así nadie escribe "caoba" de formas diferentes.

—Exactamente. Y si intentan escribir algo que no está en la lista, Excel lo rechazará.

—¿Y si alguien quiere agregar una madera nueva?

—Tienes que editar la lista en la validación. O mejor aún, poner la lista en un rango aparte y referenciarlo. Así:

1. En una hoja aparte (o en celdas ocultas), escribe la lista de maderas: `H1:Caoba, H2:Cedro, H3:Roble, etc.`
2. En la validación, en lugar de escribir los valores, selecciona el rango: `=Hoja2!$H$1:$H$7`

—Ah —dijo Sofía—. Así, si agregas una madera al rango, la lista se actualiza automáticamente si usas una tabla de Excel o actualizas el rango.

—Exacto. Aunque hay un truco mejor: convierte ese rango en **Tabla de Excel** (Ctrl+T) y usa el nombre de la tabla en la validación. Así, al agregar un nuevo elemento, la lista se expande automáticamente.

---

## Mensajes de entrada y alertas de error

—Las listas están bien —dijo Carlos—, pero a veces necesitas más que eso. Necesitas **guiar al usuario** cuando va a escribir en una celda.

**Mensaje de entrada:** Selecciona una celda, ve a **Validación de datos > Mensaje de entrada**. Puedes escribir un título y un mensaje que aparecerá cuando alguien seleccione la celda.

—Ponle: Título = "Madera", Mensaje = "Seleccione el tipo de madera de la lista desplegable"

Sofía lo hizo. Ahora, al seleccionar la celda, aparecía un cuadro de texto informativo.

—Eso evita que los nuevos empleados se pregunten qué poner ahí.

**Alerta de error:** Ve a la pestaña **Mensaje de error**. Aquí defines qué pasa cuando alguien ingresa un dato inválido.

Hay tres estilos:
- **Detener:** No permite el dato incorrecto. El usuario debe reintentar o cancelar.
- **Advertencia:** Advierte que el dato es incorrecto, pero permite continuar.
- **Información:** Informa que el dato es inusual, pero lo acepta.

—Usa "Detener" para la lista de maderas —dijo Carlos—. Y pon un mensaje amigable: "Por favor, selecciona una madera de la lista desplegable".

Sofía asintió. —Esto es como enseñarle a Excel a ser el policía de los datos.

—Exacto. Y es mejor que tener a tu mamá persiguiendo a los empleados con el corrector en la mano.

---

## Validaciones más complejas

—Las listas son el uso más común, pero la validación de datos puede hacer mucho más.

Carlos mostró otras opciones en "Permitir":

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Número entero** | Solo acepta números enteros en un rango | Entre 1 y 1000 |
| **Decimal** | Acepta números decimales | Entre 0.01 y 9999.99 |
| **Fecha** | Solo fechas en un rango | Posteriores al 01/01/2024 |
| **Hora** | Solo horas | Entre 8:00 y 18:00 |
| **Longitud de texto** | Controla la cantidad de caracteres | Máximo 20 caracteres |
| **Personalizada** | Usa una fórmula para validar | `=SI(B2="";0;LARGO(B2)>3)` |

—La opción **personalizada** es la más poderosa —explicó Carlos—. Porque puedes usar cualquier fórmula de Excel como regla de validación.

—¿Por ejemplo? —preguntó Sofía.

—Supón que quieres asegurarte de que el valor en la columna "Cantidad" sea siempre un número par. La fórmula sería: `=RESIDUO(C2;2)=0`

—O que la fecha sea un día laborable: `=DIALAB(C2;1;2)` —le siguió el juego Sofía.

—¡Exacto! Ya estás pensando como una analista de datos.

---

## Pistas ocultas en el archivo secreto

—Ahora volvamos al archivo secreto —dijo Carlos—. Quiero que revises si alguna de las celdas tiene validación de datos o comentarios ocultos.

Sofía abrió el archivo. Seleccionó todo el rango de datos (Ctrl+E) y revisó.

—No veo indicadores de validación... pero sí hay celdas con comentarios.

En Excel, las celdas con comentarios tienen un pequeño triángulo rojo en la esquina superior derecha. Sofía los había confundido con marcas de error.

—Pasa el mouse sobre cada uno —dijo Carlos.

Sofía lo hizo. Los comentarios decían cosas como:

- *"Verificar con cuaderno azul"*
- *"AX-1001 a AX-1050 = lote experimental"*
- *"Revisar discrepancias con proveedor X"*
- *"Ver con Carlos (contabilidad)"*

—¡El abuelo te menciona en sus comentarios! —exclamó Sofía.

Carlos se inclinó para leer. Efectivamente, varias celdas tenían comentarios que mencionaban su nombre.

—Yo trabajé con tu abuelo durante unas semanas en 2006 —dijo Carlos lentamente—. Me pidió que ayudara con la contabilidad de unos pedidos especiales. Pero nunca supe de qué se trataba. Dijo que era "confidencial".

—¿Confidencial? ¿Qué tipo de pedidos?

—No me acuerdo bien. Fue hace casi veinte años. Pero recuerdo que me dijo: "Carlos, si algo me pasa, busca el archivo. Tú sabrás qué hacer."

—¿Y no hiciste nada?

—Pensé que era una exageración. Tu abuelo siempre fue dramático. Y luego... bueno, la vida siguió. Pero ahora que encontraste esto...

—Alguien más podría estar buscando este archivo —susurró Sofía—. ¿Qué pasaría si cayera en malas manos?

—No lo sé. Pero tenemos que descifrarlo antes que nadie.

---

## Comentarios vs Notas

—Excel tiene dos tipos de anotaciones —explicó Carlos mientras revisaba el archivo—: los **comentarios** (antiguos) y las **notas** (nuevas).

Los comentarios (versiones modernas de Excel) son como hilos de conversación: múltiples personas pueden responder y mencionarse. Las notas son anotaciones simples, como post-its digitales.

Para agregar un comentario moderno: **Revisar > Nuevo comentario** (o clic derecho > Nuevo comentario)
Para agregar una nota: **Revisar > Nueva nota** (o clic derecho > Nueva nota)

—El abuelo usaba comentarios antiguos —observó Sofía—. Los que tienen el triángulo rojo.

—Correcto. En Excel 365, esos son "Notas" ahora. Pero el concepto es el mismo: información adicional que no está en la celda pero la complementa.

---

### Enigma 2.1: Crea la lista de productos del taller

Crea una hoja de pedidos con las siguientes columnas: N° Pedido, Cliente, Producto, Madera, Cantidad, Precio Unitario, Total.

Aplica validación de datos con lista desplegable para:
- **Producto:** Silla, Mesa, Ropero, Estante, Cama, Banco, Puerta
- **Madera:** Caoba, Cedro, Roble, Pino, Tornillo, Nogal, Cerezo

Agrega mensajes de entrada descriptivos para cada columna.

---

### Enigma 2.2: Validación personalizada

En la columna Cantidad, aplica una validación personalizada que solo permita números entre 1 y 500. Agrega un mensaje de error personalizado que diga: "La cantidad debe estar entre 1 y 500 unidades".

Pista: usa "Permitir: Número entero" con valores mínimo y máximo.

---

### Enigma 2.3: Detecta validaciones ocultas

En el archivo "Libro_Secreto.xlsx", selecciona toda la hoja y ve a **Datos > Validación de datos > Circular celdas con validación inválida** para ver si hay datos que no cumplen las reglas. ¿Hay alguna celda con validación que no se está cumpliendo?

---

## Lo que aprendiste

- Las **listas desplegables** garantizan que los usuarios solo ingresen valores válidos
- Los **mensajes de entrada** guían al usuario antes de escribir
- Las **alertas de error** (Detener, Advertencia, Información) controlan la respuesta a datos inválidos
- La **validación de datos** va más allá de listas: permite controlar números, fechas, texto y validaciones personalizadas con fórmulas
- Los **comentarios y notas** guardan información adicional valiosa
- Las pistas pueden estar ocultas en lugares que no esperas: comentarios, validaciones, formatos

---

—No sabía que el abuelo te había involucrado en esto —dijo Sofía mientras cerraba el archivo—. ¿Qué más sabes que no me has contado?

Carlos se ajustó los lentes. —Sé que los números del archivo no son ingresos normales del taller. Son demasiado grandes. Y sé que hay al menos otra persona que sabe de la existencia de este archivo.

—¿Quién?

—El abogado de tu abuelo. El señor Montenegro. Él mencionó una vez que Don Rafael tenía un "proyecto especial" que le había confiado. Pero cuando le pregunté, dijo que tenía instrucciones estrictas de no revelar nada hasta que se cumpliera cierta condición.

—¿Qué condición?

—No lo sé. Pero ahora que tenemos el archivo, tal vez podamos descubrirlo.

Sofía miró la pantalla. Los números, los comentarios, las pistas. Todo empezaba a conectarse. Pero todavía faltaban muchas piezas del rompecabezas.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
