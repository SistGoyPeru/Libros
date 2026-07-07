# Capítulo 2: La Paleta de Colores

*Tema: Colores, fondos, tipografía*

---

A la mañana siguiente, Carolina llamó a Mateo a su escritorio. Tenía abierto un documento con la identidad visual de "Cultura Viva".

—Cada revista tiene una personalidad —dijo, señalando la pantalla—. "Cultura Viva" es una revista de arte y pensamiento. Debe verse elegante, seria pero no aburrida, moderna pero clásica. Colores, tipografía y fondos son la base de esa personalidad.

## Colores en CSS

—Hay cuatro formas principales de definir colores en CSS —explicó Carolina, abriendo una paleta digital—.

### Nombres de colores

```css
color: red;
color: darkblue;
background-color: lightgray;
color: white;
```

—CSS reconoce 140 nombres de colores estándar. Son fáciles de recordar, pero limitados.

### Colores hexadecimales (hex)

```css
color: #FF5733;
color: #333333;
color: #fff;
color: #800000;
```

—El formato **hexadecimal** usa seis dígitos (o tres en versión corta) que representan los valores de rojo, verde y azul (RRGGBB). Cada par va de 00 a FF.

—`#FF0000` es rojo puro. `#00FF00` es verde puro. `#0000FF` es azul puro. Combinándolos obtienes cualquier color.

### RGB

```css
color: rgb(255, 87, 51);
color: rgb(51, 51, 51);
background-color: rgb(240, 240, 240);
```

—**RGB** es lo mismo que hexadecimal pero en números decimales del 0 al 255.

### HSL

```css
color: hsl(12, 100%, 60%);
background-color: hsl(0, 0%, 95%);
```

— **HSL** significa Hue (tono, 0-360°), Saturation (saturación, 0-100%), Lightness (luminosidad, 0-100%). Es más intuitivo para los diseñadores porque separa el tono de la intensidad.

—Mira —dijo Carolina, mostrando una tabla—:

| Formato | Ejemplo | ¿Cuándo usarlo? |
|---------|---------|------------------|
| Nombres | `red`, `white` | Prototipos rápidos |
| Hex | `#FF5733` | Lo más común en producción |
| RGB | `rgb(255,87,51)` | Cuando necesitas transparencia |
| HSL | `hsl(12,100%,60%)` | Cuando trabajas con paletas |


### Transparencia con rgba y hsla

—Puedes agregar un cuarto valor para la **opacidad** (alfa), de 0 a 1:

```css
color: rgba(255, 87, 51, 0.8);
background-color: hsla(200, 50%, 50%, 0.3);
```

—0 es completamente transparente. 1 es completamente opaco.

## background-color y background-image

—Ahora, hablemos de fondos —dijo Carolina, abriendo el CSS de la revista—.

```css
/* Color de fondo */
body {
  background-color: #f5f0eb;
}

.header {
  background-color: #1a1a2e;
}

/* Imagen de fondo */
.banner {
  background-image: url("imagenes/banner-cultura.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
```

Propiedades de fondo importantes:

| Propiedad | ¿Qué hace? |
|-----------|------------|
| `background-color` | Color de fondo |
| `background-image` | Imagen de fondo (url(...)) |
| `background-size` | Tamaño: cover, contain, auto |
| `background-position` | Posición: center, top, left |
| `background-repeat` | Repetición: no-repeat, repeat, repeat-x |
| `background` | Propiedad abreviada (shorthand) |

```css
/* Shorthand: todo en una línea */
body {
  background: #f5f0eb url("textura.png") no-repeat center top;
}
```

## Tipografía: font-family en profundidad

—El tipo de letra define la voz del texto —dijo Carolina, abriendo Google Fonts en el navegador—.

```css
/* Web safe: fuentes que todos los sistemas tienen */
body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Serif para títulos con elegancia */
h1, h2 {
  font-family: Georgia, "Times New Roman", serif;
}
```

### Buenas prácticas con font-family

—Siempre incluye una **fuente de respaldo** (fallback) y termina con una familia genérica:

```css
font-family: "Open Sans", Arial, Helvetica, sans-serif;
```

—Si la primera fuente no está disponible, se usa la siguiente, y así sucesivamente.

### Usando Google Fonts

—Mateo, vamos a usar una fuente elegante para los títulos de la revista.

Carolina fue a Google Fonts, seleccionó **Playfair Display** para títulos y **Lato** para el cuerpo, y copió el código:

```html
<!-- En el <head> del HTML -->
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
```

```css
/* En el CSS */
h1, h2, h3 {
  font-family: "Playfair Display", Georgia, serif;
  font-weight: 700;
}

body {
  font-family: "Lato", Arial, sans-serif;
  font-weight: 400;
}
```

## Propiedades tipográficas avanzadas

Carolina mostró más propiedades que transformarían el texto:

```css
.articulo {
  font-weight: 700;      /* 100 (light) a 900 (black) */
  font-style: italic;     /* normal, italic, oblique */
  line-height: 1.8;       /* Espaciado entre líneas */
  text-transform: uppercase; /* mayúsculas */
  text-decoration: underline; /* subrayado */
  letter-spacing: 2px;    /* Espaciado entre letras */
  word-spacing: 4px;      /* Espaciado entre palabras */
}
```

### Ejemplo completo

Mateo aplicó la identidad visual de "Cultura Viva":

```css
/* === CSS de Cultura Viva === */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Lato:wght@300;400;700&display=swap');

:root {
  --color-principal: #8B0000;
  --color-secundario: #1a1a2e;
  --color-fondo: #f5f0eb;
  --color-texto: #2d2d2d;
  --color-claro: #e8e0d5;
}

body {
  font-family: "Lato", Arial, sans-serif;
  color: var(--color-texto);
  background-color: var(--color-fondo);
  line-height: 1.7;
}

h1, h2, h3 {
  font-family: "Playfair Display", Georgia, serif;
  color: var(--color-principal);
}

h1 {
  font-size: 48px;
  font-weight: 900;
  letter-spacing: -0.5px;
  text-transform: capitalize;
}

h2 {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: 1px;
}

.cita {
  font-style: italic;
  font-size: 20px;
  line-height: 1.6;
  color: #555;
  border-left: 4px solid var(--color-principal);
  padding-left: 20px;
}

.fecha {
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 3px;
  color: #888;
  font-weight: 700;
}
```

Mateo guardó y recargó. La diferencia era notable. El sitio ahora tenía *personalidad*. Los títulos en Playfair Display se veían majestuosos; el cuerpo en Lato era limpio y legible. Los colores cálidos del fondo daban una sensación acogedora.

—Ahora sí parece una revista cultural —dijo Mateo.

—Ahora sí tiene identidad —corrigió Carolina—. La paleta de colores y la tipografía son la voz visual de la marca. Cada fuente, cada color, comunica algo.

---

## Enigmas del Capítulo 2

**Enigma 2.1:** Escribe el CSS para que el fondo del sitio use un degradado lineal de `#f5f0eb` a `#e8d5c4`. Pista: usa `background: linear-gradient(...)`.

**Enigma 2.2:** Crea una regla CSS que haga que todos los enlaces (`<a>`) cambien de color cuando el usuario pase el mouse por encima. Usa `:hover`.

**Enigma 2.3:** Usando Google Fonts, agrega la fuente **Merriweather** para los artículos y **Montserrat** para los menús de navegación. Escribe tanto el HTML de enlace como el CSS.

**Enigma 2.4:** Convierte estos colores hex a rgb:
- `#FFFFFF`
- `#000000`
- `#8B0000`
- `#2E8B57`

**Enigma 2.5:** Explica por qué es importante usar `background-size: cover` en una imagen de fondo. ¿Qué pasaría si no lo usas?
