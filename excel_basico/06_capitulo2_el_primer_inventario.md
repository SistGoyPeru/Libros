# Capítulo 2: El Primer Inventario

## Ingreso de Datos, Tipos de Datos y Selección

---

Eran las siete de la mañana cuando Sofía llegó al taller. El sol de Lima apenas comenzaba a filtrarse por las ventanas polvorientas, iluminando partículas de viruta que flotaban en el aire como pequeños tesoros.

Don Manuel ya estaba trabajando, lijando una tabla de cedro con movimientos precisos y rítmicos.

—Buenos días, mija —dijo sin dejar de lijar—. ¿Lista para poner orden?

Sofía asintió. Había pasado la noche pensando en el inventario de su abuelo. Los datos estaban allí, pero sentía que podía hacer más. Podía organizarlos mejor, categorizarlos, darles sentido.

—Don Manuel —preguntó—, mi abuelo tenía algún sistema para la madera. Usted sabe algo de eso?

El viejo carpintero dejó la lija y se secó la frente.

—Claro. Tu abuelo clasificaba la madera por calidad. Usaba colores. La madera de primera era... —hizo una pausa, pensativo—. Sí, creo que lo anotó en su cuaderno.

Sofía recordó el cuaderno de pasta negra que había visto en el escritorio. Lo abrió y encontró páginas llenas de anotaciones:

*"Madera de cedro: calidad A (rojo). Roble: calidad A (rojo). Pino: calidad B (amarillo). Triplay: calidad C (verde)."*

—Colores —murmuró Sofía—. Usaba un sistema de colores para la calidad. Rojo para primera, amarillo para segunda, verde para tercera.

Miró la pantalla de Excel. Los datos de su abuelo estaban allí, pero sin colores, sin formato, sin vida. Era hora de cambiar eso.

---

## Tipos de datos en Excel

Cuando Sofía comenzó a trabajar con los datos, notó algo interesante: Excel trataba diferente cada tipo de información.

—Mira —le dijo a Don Manuel, señalando la pantalla—. Cuando escribo texto, Excel lo alinea a la izquierda. Cuando escribo números, los alinea a la derecha.

Excel reconoce automáticamente tres tipos principales de datos:

### Texto (cadenas de caracteres)
- Se alinea a la izquierda por defecto
- Puede incluir letras, números, símbolos
- Ejemplos: "Cedro", "Maderas Pérez", "Tornillos #10"

### Números
- Se alinean a la derecha por defecto
- Incluyen enteros y decimales
- Ejemplos: 50, 45.00, 0.50
- El separador decimal es el punto (.) o la coma (,) según la configuración regional

### Fechas
- Se alinean a la derecha por defecto
- Excel almacena las fechas como números seriales
- Ejemplos: 15/03/2026, 01/01/2026

### Fórmulas
- Comienzan con el signo igual (=)
- Realizan cálculos con los valores de otras celdas
- Ejemplos: =A1+B1, =C2*D2

| Tipo de Dato | Alineación por defecto | Ejemplo |
|--------------|----------------------|---------|
| Texto | Izquierda | "Cedro" |
| Número | Derecha | 45.00 |
| Fecha | Derecha | 15/03/2026 |
| Fórmula | Derecha | =A1+B1 |

---

## Ingresando datos como Sofía

Sofía decidió mejorar el inventario de su abuelo. Agregó nuevas columnas y datos:

1. En la columna F, escribió **"Calidad"**
2. En la columna G, escribió **"Fecha de Ingreso"**
3. En la columna H, escribió **"Ubicación"**

Luego comenzó a llenar los datos:

| E | F | G | H |
|---|---|---|---|
| **Proveedor** | **Calidad** | **Fecha Ingreso** | **Ubicación** |
| Maderas Pérez | A | 15/01/2026 | Estante 1 |
| Maderas Pérez | A | 15/01/2026 | Estante 1 |
| El Maderero | B | 20/01/2026 | Estante 2 |
| Maderas Pérez | C | 20/01/2026 | Estante 3 |
| Pinturas Unidas | - | 10/02/2026 | Anaquel 1 |
| Pinturas Unidas | - | 10/02/2026 | Anaquel 1 |
| Ferretería El Tornillo | - | 05/02/2026 | Caja 1 |
| Ferretería El Tornillo | - | 05/02/2026 | Caja 1 |
| Ferretería El Tornillo | - | 05/02/2026 | Anaquel 2 |
| Ferretería El Tornillo | - | 05/02/2026 | Anaquel 2 |
| Pinturas Unidas | - | 10/02/2026 | Anaquel 1 |

Sofía notó algo: cuando escribió "15/01/2026", Excel automáticamente lo reconoció como fecha y lo alineó a la derecha. Pero cuando escribió "-" en la columna Calidad, lo trató como texto.

—Excel es más inteligente de lo que parece —pensó.

### Trucos de ingreso de datos

Mientras trabajaba, Sofía descubrió algunos atajos útiles:

- **Ctrl + D:** Copia el contenido de la celda de arriba hacia abajo
- **Ctrl + R:** Copia el contenido de la celda de la izquierda hacia la derecha
- **Ctrl + Z:** Deshace la última acción
- **Ctrl + Y:** Rehace la última acción deshecha
- **Ctrl + Enter:** Ingresa el mismo dato en todas las celdas seleccionadas
- **Completado automático:** Cuando empiezas a escribir un texto que ya existe en la columna, Excel sugiere completarlo

---

## El sistema de colores del abuelo

Sofía abrió el cuaderno de su abuelo en una página donde había un dibujo hecho a mano:

*"Calidad A (Rojo) = Madera de primera. Sin nudos. Perfecta para muebles finos.*
*Calidad B (Amarillo) = Madera de segunda. Algunos nudos. Para muebles estándar.*
*Calidad C (Verde) = Madera de tercera. Con imperfecciones. Para estructuras internas."*

Sofía quería aplicar este sistema de colores a su hoja de Excel. Todavía no sabía cómo, pero anotó la idea mentalmente. Por ahora, se conformaría con escribir las letras A, B, C en la columna de Calidad.

Pero mientras trabajaba, notó otro detalle en el cuaderno de su abuelo. En la última página, escritas con letra pequeña y temblorosa:

*"Si estás leyendo esto, Sofía, es porque estás haciendo exactamente lo que esperaba. El inventario es solo el principio. Cada número en esta hoja cuenta una historia. Aprende a leerlos."*

Sofía sintió un escalofrío. Su abuelo sabía que ella estaría allí, frente a esa computadora, tratando de descifrar su legado.

---

## Selección de celdas y rangos

Para trabajar eficientemente en Excel, necesitas dominar la selección. Sofía practicó con el inventario:

### Seleccionar un rango contiguo

Hizo clic en A1, mantuvo presionado y arrastró hasta E11. El rango A1:E11 quedó resaltado en gris (excepto la primera celda, que permanece blanca).

### Seleccionar columnas completas

Hizo clic en la letra "C" para seleccionar toda la columna Cantidad. Luego presionó Ctrl y hizo clic en "D" para seleccionar también la columna Precio Unitario.

### Seleccionar filas completas

Hizo clic en el número "1" para seleccionar la primera fila (los encabezados).

### Seleccionar toda la hoja

Hizo clic en el triángulo entre la columna A y la fila 1, o presionó Ctrl + E (en inglés Ctrl + A).

### Rangos no contiguos

Para seleccionar celdas que no están juntas, presiona Ctrl mientras haces clic en cada celda o rango. Esto es útil para dar formato especial solo a ciertas celdas.

---

## Editando datos

Sofía cometió un error: escribió "Cedr" en lugar de "Cedro". Para corregirlo:

1. **Doble clic en la celda:** Entra en modo de edición directamente en la celda.
2. **F2:** También entra en modo de edición.
3. **Barra de fórmulas:** Haz clic en la barra de fórmulas para editar allí.

Sofía prefirió el doble clic, porque le permitía ver el contexto de la celda mientras editaba.

---

## Enigmas del Capítulo 2

### Enigma 2.1: El inventario de herramientas

Don Manuel encontró más herramientas en el almacén. Agrega estos datos a tu hoja de Excel (puedes continuar desde el Enigma 1.2):

| Producto | Cantidad | Precio Unitario | Calidad |
|----------|----------|-----------------|---------|
| Taladro inalámbrico | 2 | S/ 280.00 | A |
| Sierra circular | 3 | S/ 350.00 | A |
| Lijadora orbital | 2 | S/ 180.00 | B |
| Juego de brocas | 5 | S/ 45.00 | B |
| Extensión eléctrica 10m | 4 | S/ 25.00 | C |

Practica ingresar cada dato. Observa cómo Excel alinea automáticamente los números a la derecha y el texto a la izquierda.

### Enigma 2.2: El código secreto del abuelo

En el cuaderno de Don Rafael hay una anotación críptica:

*"A=1, B=2, C=3. La suma de las calidades revela el camino."*

Interpreta: si Calidad A vale 1 punto, Calidad B vale 2, y Calidad C vale 3, ¿cuánto suman las calidades del inventario de herramientas del Enigma 2.1? (Calcula mentalmente o en papel — las fórmulas las veremos pronto).

### Enigma 2.3: Selección eficiente

Abre el archivo "Inventario_Taller.xlsx" que creaste (o usa los datos de ejemplo del capítulo). Practica:

1. Selecciona el rango A1:E11 (todos los productos).
2. Sin deseleccionar, presiona Ctrl y selecciona también el rango F1:H11.
3. Selecciona toda la columna C (Cantidad) haciendo clic en la letra C.
4. Selecciona las filas 1, 3, 5, 7, 9 y 11 manteniendo Ctrl mientras haces clic en los números de fila.
5. Presiona Ctrl + E para seleccionar toda la hoja.

### Enigma 2.4: Ingreso rápido

En Excel, ingresa la siguiente lista de productos en la columna A, un dato por celda:

Sillón, Mesa, Silla, Banquito, Estante, Cómoda, Ropero

Luego, en la columna B, asígnale a cada producto una cantidad (usa números del 1 al 10). Practica usando Tab para moverte a la derecha y Enter para ir hacia abajo.

---

## Lo que aprendiste

- Excel reconoce **tipos de datos**: texto, número, fecha y fórmula
- El texto se alinea a la **izquierda**; los números y fechas a la **derecha**
- Puedes **seleccionar celdas** de muchas formas: clic, arrastre, Ctrl, Shift
- Para **editar** una celda, haz doble clic o presiona F2
- **Ctrl + Z** deshace errores — tu mejor aliado
- El **completado automático** acelera el ingreso de datos repetitivos

---

Sofía cerró el archivo y estiró los brazos. Había pasado toda la mañana ingresando datos y organizando el inventario. La hoja de cálculo comenzaba a tomar forma.

—¿Sabes qué es lo mejor? —le dijo a Don Manuel—. Mi abuelo no solo dejó los números. Dejó un sistema. Un método. Yo solo tengo que seguirlo.

Don Manuel sonrió, sus ojos arrugados por los años de trabajo.

—Eso mismo decía tu abuelo: "El trabajo está hecho. Solo falta quien lo entienda".

Sofía guardó los cambios. El taller comenzaba a tener orden. Pero sabía que el verdadero desafío estaba por venir: entender las fórmulas que su abuelo había mencionado en su cuaderno.
