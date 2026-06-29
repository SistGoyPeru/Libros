# Capítulo 1: El Primer Estilo

*Tema: Introducción a CSS, selectores básicos, propiedades de texto*

---

Mateo llegó temprano a PixelLab. Eran las 8:30 de la mañana y la oficina aún estaba en silencio, iluminada por la luz grisácea del invierno limeño que entraba por los ventanales del tercer piso. Dejó su mochila en el escritorio que le habían asignado —una esquina modesta con un monitor Dell y una planta de plástico que parecía tan nerviosa como él— y abrió el editor de texto.

Carolina apareció media hora después con un café en una mano y una laptop en la otra.

—¿Listo para tu primera lección? —preguntó, sentándose a su lado.

Mateo asintió.

—Primero, veamos qué estamos construyendo —dijo Carolina, abriendo el archivo `index.html` de "Cultura Viva".

La pantalla mostró el código HTML de la portada de la revista. Había encabezados, párrafos, imágenes, enlaces. Todo perfectamente estructurado, pero visualmente plano.

—El HTML es el esqueleto —explicó Carolina—. Define qué es cada cosa: un título, un párrafo, una imagen. Pero no dice cómo se ve. Eso es trabajo de CSS.

## ¿Qué es CSS?

—CSS significa **Cascading Style Sheets** —dijo Carolina, escribiendo en un documento nuevo—. En español: Hojas de Estilo en Cascada. Es el lenguaje que usamos para describir la presentación visual de un documento HTML.

—¿Y lo de "en cascada"? —preguntó Mateo.

—Ya veremos. Por ahora, piensa en CSS como la pintura, los muebles y la decoración de una casa. El HTML son las paredes y el techo. Con CSS decides de qué color pintar, dónde poner los muebles, qué tipo de cortinas usar.

## Formas de incluir CSS

Carolina abrió tres pestañas en el navegador para mostrar los métodos:

### 1. CSS en línea (inline)

```html
<p style="color: blue; font-size: 18px;">Este párrafo es azul y grande.</p>
```

—Se aplica directamente a un elemento con el atributo `style` —explicó Carolina—. Es rápido, pero desordenado. Mezclas contenido con presentación.

### 2. CSS interno

```html
<head>
  <style>
    p {
      color: blue;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <p>Este párrafo es azul y grande.</p>
</body>
```

—Se escribe dentro de la etiqueta `<style>` en el `<head>` del documento. Mejor que inline, pero solo funciona para una página.

### 3. CSS externo (el más recomendado)

```css
/* estilo.css */
p {
  color: blue;
  font-size: 18px;
}
```

```html
<head>
  <link rel="stylesheet" href="estilo.css">
</head>
```

—Un archivo separado con extensión `.css` que enlazamos desde el HTML con `<link>`. Así mantenemos el estilo separado del contenido y podemos reutilizarlo en muchas páginas.

—Este es el método que usaremos en "Cultura Viva" —dijo Carolina—. Un solo archivo CSS para todo el sitio.

## Sintaxis básica de CSS

Carolina abrió un archivo nuevo y escribió:

```css
selector {
  propiedad: valor;
  propiedad: valor;
}
```

—Cada regla CSS tiene tres partes: un **selector** (¿a qué elementos aplicamos el estilo?), una **propiedad** (¿qué aspecto queremos cambiar?) y un **valor** (¿cómo queremos que sea?).

—Por ejemplo:

```css
h1 {
  color: darkred;
  font-size: 36px;
  text-align: center;
}
```

—Esto dice: "todos los encabezados `h1` deben ser de color rojo oscuro, tamaño 36 píxeles, y centrados".

## Selectores básicos

—Ahora, lo más importante: los **selectores** —dijo Carolina, abriendo el HTML de "Cultura Viva" en el navegador—. Necesitas una forma de apuntar a elementos específicos. Hay tres selectores básicos que usarás todo el tiempo:

### Selector de tipo (etiqueta)

```css
/* Afecta a TODOS los elementos de ese tipo */
p {
  font-family: Georgia, serif;
  line-height: 1.6;
}

h2 {
  color: #333;
}
```

### Selector de clase

En HTML:

```html
<p class="destacado">Este párrafo especial necesita destacar.</p>
```

En CSS:

```css
/* Las clases comienzan con un punto (.) */
.destacado {
  background-color: #ffffcc;
  font-weight: bold;
  padding: 10px;
}
```

—Las **clases** son reutilizables. Puedes aplicar la misma clase a muchos elementos diferentes.

### Selector de ID

En HTML:

```html
<h1 id="titulo-principal">Cultura Viva</h1>
```

En CSS:

```css
/* Los ID comienzan con numeral (#) */
#titulo-principal {
  color: #8B0000;
  font-size: 48px;
  text-transform: uppercase;
}
```

—Los **ID** deben ser únicos. Solo un elemento por página puede tener un ID específico.

Carolina mostró una tabla comparativa:

| Selector | Sintaxis | Uso | Reutilizable |
|----------|----------|-----|-------------|
| Tipo | `p { }` | Todos los `<p>` | Sí |
| Clase | `.clase { }` | Múltiples elementos | Sí |
| ID | `#id { }` | Un solo elemento | No |

## Propiedades de texto básicas

—Ahora, lo que más necesitarás para empezar: propiedades para dar estilo al texto.

Carolina escribió un ejemplo completo:

```css
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  color: #333333;
}

h1 {
  font-size: 32px;
  font-weight: bold;
  color: #1a1a1a;
  text-align: center;
}

p {
  font-size: 16px;
  line-height: 1.5;
  text-align: justify;
}

.destacado {
  color: #cc0000;
  font-weight: bold;
  font-size: 18px;
}
```

Propiedades explicadas:

| Propiedad | ¿Qué hace? | Valores comunes |
|-----------|------------|-----------------|
| `color` | Color del texto | nombres, hex, rgb |
| `font-size` | Tamaño de letra | px, em, rem |
| `font-family` | Tipo de letra | Arial, Georgia, serif, sans-serif |
| `font-weight` | Grosor | normal, bold, 100-900 |
| `text-align` | Alineación | left, center, right, justify |
| `line-height` | Espaciado entre líneas | 1.2, 1.5, 2.0 (sin unidad) |
| `text-transform` | Transformación | uppercase, lowercase, capitalize |

## Manos a la obra

Mateo abrió el archivo `estilo.css` que Carolina había creado para el proyecto. Hasta ahora estaba vacío.

—Tu primera tarea —dijo Carolina—: dale estilo al encabezado principal y los párrafos de la portada.

Mateo escribió:

```css
/* estilo.css — Cultura Viva */

body {
  font-family: Georgia, "Times New Roman", serif;
  color: #222;
  background-color: #fafafa;
}

h1 {
  font-size: 42px;
  color: #800000;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
}

h2 {
  font-size: 28px;
  color: #444;
  border-bottom: 2px solid #800000;
  padding-bottom: 5px;
}

p {
  font-size: 16px;
  line-height: 1.6;
  text-align: justify;
}

.destacado {
  background-color: #fff3e0;
  padding: 15px;
  font-style: italic;
  border-left: 4px solid #800000;
}
```

Mateo guardó el archivo y recargó el navegador. El sitio de "Cultura Viva" se veía diferente. No radicalmente, pero se notaba. Los títulos tenían presencia. Los párrafos se leían con fluidez. El fondo no era blanco puro, sino un crema suave.

—Se ve mejor —dijo, sonriendo.

—Se ve *humano* —corrigió Carolina—. Eso es lo que hace CSS: humaniza la tecnología.

---

## Enigmas del Capítulo 1

**Enigma 1.1:** Escribe el CSS necesario para que todos los enlaces (`<a>`) del sitio sean de color verde oscuro (`#006400`), sin subrayado, y en negrita.

**Enigma 1.2:** Crea una clase llamada `.autor` que ponga el texto en cursiva, color gris (`#666`), tamaño 14px, y alineado a la derecha.

**Enigma 1.3:** ¿Cuál es la diferencia entre un selector de clase y un selector de ID? ¿Cuándo usarías cada uno?

**Enigma 1.4:** Dado el siguiente HTML, escribe el CSS para que:
- El título principal sea azul marino, centrado, de 40px
- El subtítulo sea gris, tamaño 20px, en mayúsculas
- El párrafo con clase `intro` tenga fondo color `#eef` y un padding de 20px

```html
<h1 id="titulo">Bienvenidos a Cultura Viva</h1>
<h2 class="subtitulo">Arte y pensamiento desde 1998</h2>
<p class="intro">La revista que conecta a los amantes del arte.</p>
<p>Conoce nuestras próximas exposiciones.</p>
```

**Enigma 1.5:** Explica con tus palabras qué significa que CSS sea "en cascada".
