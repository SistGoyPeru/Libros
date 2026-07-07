# Capítulo 1: El Taller Heredado

## Introducción a Excel, Interfaz y Navegación

---

El taller "Mendoza & Hijos" olía a madera, a barniz y a historia. Sofía empujó la puerta de madera maciza —tallada por su abuelo, por supuesto— y sintió que el tiempo se detenía.

Las vigas del techo sostenían lámparas de luz cálida. Las paredes estaban cubiertas de herramientas: serruchos, cepillos, formones, garlopas. En el centro, una gran mesa de trabajo mostraba las marcas de incontables proyectos. Y en un rincón, cubierta por un paño de lana, estaba la computadora que ella misma le había regalado a su abuelo tres años atrás.

Don Manuel la esperaba con una taza de café humeante.

—Tu abuelo pasaba las tardes aquí —dijo, señalando la computadora—. Decía que estaba organizando "el legado". Nosotros creíamos que jugaba solitario.

Sofía sonrió. Se sentó frente a la computadora, retiró el paño, y presionó el botón de encendido. La pantalla cobró vida. El escritorio mostraba un fondo de pantalla con una foto de ella cuando era niña, ayudando a su abuelo a lijar una silla.

Y allí, en el centro del escritorio, un icono azul con una "X" blanca: Excel.

—Bueno, abuelo —murmuró Sofía—. Vamos a ver qué me dejaste.

---

## La primera vez que abres Excel

Sofía hizo doble clic en el icono de Excel. La aplicación tardó unos segundos en cargar, y de repente se encontró frente a una pantalla que le resultaba tan familiar como extraña.

—¿Por dónde se empieza? —preguntó en voz alta.

Don Manuel se acercó, secándose las manos en el delantal de cuero.

—Tu abuelo siempre decía que Excel es como un taller: tienes que saber dónde están las herramientas.

Excel le mostraba una pantalla dividida en varias zonas:

1. **La Cinta de Opciones (Ribbon):** En la parte superior, una barra con pestañas: Inicio, Insertar, Diseño de Página, Fórmulas, Datos, Revisar, Vista. Cada pestaña contiene grupos de herramientas relacionadas.

2. **La Barra de Fórmulas:** Justo debajo de la cinta, una barra larga donde se muestran y escriben los datos y fórmulas.

3. **La Hoja de Cálculo:** Una cuadrícula inmensa de filas y columnas. Las columnas se identifican con letras (A, B, C, ...) y las filas con números (1, 2, 3, ...).

4. **Las Celdas:** Cada intersección de una fila y una columna es una **celda**. La celda activa —donde estás trabajando— se resalta con un borde más grueso.

5. **Las Hojas (Sheets):** En la parte inferior, pestañas llamadas "Hoja1", "Hoja2", "Hoja3". Puedes agregar más y renombrarlas.

| Parte de Excel | ¿Qué es? | ¿Para qué sirve? |
|----------------|----------|------------------|
| Cinta de opciones | Barra de pestañas con herramientas | Acceder a todas las funciones de Excel |
| Barra de fórmulas | Barra blanca larga | Escribir y ver datos y fórmulas |
| Columna | Letras (A, B, C...) | Identificar la posición vertical |
| Fila | Números (1, 2, 3...) | Identificar la posición horizontal |
| Celda | Intersección (ej: A1) | Contener datos individuales |
| Hoja | Pestaña inferior | Separar conjuntos de datos |

### La dirección de una celda

Sofía movió el ratón y notó que el cursor cambiaba a una cruz blanca. Hizo clic en una celda. En la esquina superior izquierda, un cuadro mostraba "A1". Esa es la **dirección de la celda**: columna A, fila 1.

—Así que si quiero ir a la celda que está en la columna C, fila 5 —pensó Sofía—, sería C5.

Probó: escribió "Hola, abuelo" en la celda A1 y presionó Enter. El texto apareció en la celda y también en la barra de fórmulas.

—Esto no es tan difícil —sonrió.

### Navegación básica

Sofía descubrió varias formas de moverse por la hoja:

- **Flechas del teclado:** Mueven la celda activa en esa dirección.
- **Tab:** Mueve a la siguiente celda a la derecha.
- **Enter:** Mueve a la celda de abajo.
- **Click:** Va directamente a la celda donde hagas clic.
- **Ctrl + Inicio:** Va a la celda A1.
- **Ctrl + Fin:** Va a la última celda con datos.

---

## Encontrando el archivo del abuelo

Sofía necesitaba abrir el archivo "Inventario_Taller.xlsx" que mencionaba la nota. Hizo clic en **Archivo > Abrir** y navegó hasta la carpeta "Documentos". Allí encontró varios archivos:

```
Inventario_Taller.xlsx
Clientes_Mendoza.xlsx
Presupuesto_2026.xlsx
Recetas_Secretas.txt
```

—¿Recetas secretas? —rió Sofía—. Abuelo, siempre tan misterioso.

Pero primero, lo primero. Abrió "Inventario_Taller.xlsx".

La hoja se desplegó mostrando datos que su abuelo había organizado meticulosamente:

| A | B | C | D | E |
|---|---|---|---|---|
| **Producto** | **Cantidad** | **Unidad** | **Precio Unitario** | **Proveedor** |
| Madera de Cedro | 50 | tablas | S/ 45.00 | Maderas Pérez |
| Madera de Roble | 30 | tablas | S/ 62.00 | Maderas Pérez |
| Madera de Pino | 100 | tablas | S/ 22.00 | El Maderero |
| Triplay | 40 | planchas | S/ 35.00 | Maderas Pérez |
| Barniz mate | 10 | galones | S/ 28.00 | Pinturas Unidas |
| Barniz brillante | 8 | galones | S/ 32.00 | Pinturas Unidas |
| Tornillos #10 | 500 | unidades | S/ 0.50 | Ferretería El Tornillo |
| Tornillos #8 | 300 | unidades | S/ 0.40 | Ferretería El Tornillo |
| Lija fina | 200 | hojas | S/ 1.20 | Ferretería El Tornillo |
| Lija gruesa | 150 | hojas | S/ 0.80 | Ferretería El Tornillo |
| Pegamento para madera | 12 | botellas | S/ 15.00 | Pinturas Unidas |

—Increíble —susurró Sofía—. Tenía todo registrado.

Pero había un problema: los números estaban en formato general, sin símbolos de moneda, sin colores, sin ningún tipo de organización visual. Era como un taller donde todas las herramientas están en el suelo: la información está, pero no es fácil de usar.

---

## Tu primer contacto con Excel

### Navegando la Cinta de Opciones

La **Cinta de Opciones** es el panel principal de herramientas en Excel. Veamos qué contiene cada pestaña principal:

**Inicio:**
- Portapapeles (copiar, pegar, cortar)
- Fuente (tipo de letra, tamaño, negrita, color)
- Alineación (izquierda, centro, derecha)
- Número (formato de número, decimales)
- Estilos (formato condicional, dar formato como tabla)
- Celdas (insertar, eliminar, formato)
- Modificar (ordenar, filtrar, buscar)

**Insertar:**
- Tablas (tabla dinámica, tabla)
- Ilustraciones (imágenes, formas, iconos)
- Gráficos (barras, columnas, líneas, circulares)
- Minigráficos
- Filtros (segmentación de datos)
- Vínculos
- Texto (cuadro de texto, encabezado, WordArt)

**Diseño de Página:**
- Temas
- Configurar página (márgenes, orientación, tamaño)
- Ajustar área de impresión
- Opciones de hoja

**Fórmulas:**
- Insertar función
- Autosuma
- Biblioteca de funciones
- Nombres definidos
- Auditoría de fórmulas
- Cálculo

### Seleccionar celdas

Para trabajar con datos, primero debes saber seleccionarlos:

- **Una celda:** Haz clic en ella.
- **Un rango de celdas:** Haz clic en la primera celda, mantén presionado, y arrastra hasta la última.
- **Una columna completa:** Haz clic en la letra de la columna.
- **Una fila completa:** Haz clic en el número de la fila.
- **Toda la hoja:** Haz clic en el triángulo en la esquina superior izquierda (entre la columna A y la fila 1).
- **Rangos no contiguos:** Selecciona el primer rango, presiona Ctrl, y selecciona otro rango.

### El cuadro de nombres

En la esquina superior izquierda, justo encima de la columna A, hay un cuadro que muestra la dirección de la celda activa. Puedes escribir una dirección allí y presionar Enter para ir directamente a esa celda. Por ejemplo, escribe "Z100" y presiona Enter para ir a la celda Z100.

---

Sofía pasó los dedos por el monitor, como si pudiera tocar el trabajo de su abuelo a través de la pantalla.

—Abuelo —dijo en voz baja—, no sé qué estoy haciendo. Pero voy a aprender. Por ti. Por el taller.

Don Manuel, desde la puerta del taller, la observó con una sonrisa.

—¿Sabes qué dijo tu abuelo la primera vez que abrió Excel? —preguntó.

—¿Qué?

—Dijo: "Esto es como un taller, pero los números son la madera y las fórmulas son las herramientas".

Sofía sintió un nudo en la garganta. Su abuelo, el hombre que nunca había ido a la universidad, había entendido Excel mejor que muchos profesionales.

—Vamos a hacer que este taller funcione, abuelo —prometió—. Te lo juro.

---

## Enigmas del Capítulo 1

### Enigma 1.1: Reconoce tu taller digital

Abre Excel y crea un nuevo libro. Identifica las siguientes partes y escríbelas en un papel o en un bloc de notas:

1. ¿Cuántas hojas tiene un libro nuevo de Excel por defecto?
2. ¿Qué letra de columna y número de fila tiene la celda que está tres columnas a la derecha de B y dos filas abajo de 5?
3. ¿Qué pestaña de la cinta de opciones contiene herramientas para cambiar el color de una celda?
4. ¿Cómo se llama la barra donde ves el contenido de la celda activa?

### Enigma 1.2: El primer inventario

Imagina que eres Sofía y encuentras estos materiales adicionales en el taller. Crea una nueva tabla en una hoja de Excel con los siguientes datos:

| Producto | Cantidad | Precio Unitario |
|----------|----------|-----------------|
| Cinceles | 15 | S/ 25.00 |
| Martillos | 8 | S/ 45.00 |
| Cepillos de carpintero | 6 | S/ 60.00 |
| Escuadras | 12 | S/ 18.00 |
| Niveles | 4 | S/ 35.00 |

Ingresa los datos manualmente. Practica moverte entre celdas con las flechas del teclado y con Tab.

### Enigma 1.3: Explorando la cinta

Ve a la pestaña **Insertar** en la cinta de opciones. ¿Qué tipos de gráficos puedes crear? Nombra al menos tres. Luego ve a la pestaña **Fórmulas** y busca el botón **Autosuma**. ¿Qué función crees que realiza?

### Enigma 1.4: El mensaje del abuelo

En la celda A1, escribe "Mendoza & Hijos". En la B1, escribe "Legado de Don Rafael". En la C1, escribe la fecha de hoy. Practica seleccionar todo el rango A1:C1 y luego borra el contenido presionando la tecla Suprimir.

---

## Lo que aprendiste

- Excel es una aplicación de hoja de cálculo organizada en **filas** (números) y **columnas** (letras)
- Cada **celda** tiene una dirección única (ej: A1, B5, Z100)
- La **Cinta de Opciones** agrupa las herramientas por categorías
- Puedes navegar con el teclado (flechas, Tab, Enter) o con el ratón
- Los archivos de Excel se llaman **libros** y pueden contener varias **hojas**
- El **Cuadro de Nombres** muestra la celda activa y permite navegar rápidamente

---

Sofía guardó el archivo que había estado explorando y suspiró. Había dado el primer paso. Pero sabía que el camino era largo.

—Mañana volvemos —le dijo a Don Manuel—. Y empezamos a poner orden en este taller.

Al salir, miró por última vez la pantalla de la computadora. El icono azul de Excel parpadeaba en la barra de tareas, como un faro en la oscuridad.

Su abuelo había dejado las herramientas listas. Ahora solo faltaba aprender a usarlas.
