# Capítulo 5: Flexibilidad

*Tema: Flexbox*

---

—Mateo, ven aquí —dijo Carolina una mañana, señalando su pantalla—. La revista quiere una **galería de arte** en su sitio web. Necesito que las imágenes se muestren en filas, que se adapten al tamaño de la pantalla, y que estén bien espaciadas.

Mateo miró el diseño. Había imágenes de diferentes tamaños que debían organizarse en una cuadrícula flexible. Algunas filas tendrían cuatro imágenes, otras tres, según el espacio disponible.

—Podría usar `inline-block` otra vez —dijo Mateo, dubitativo.

—Podrías —respondió Carolina—, pero sería un dolor de cabeza. Hay una herramienta mucho mejor: **Flexbox**.

## ¿Qué es Flexbox?

—**Flexbox** (Flexible Box Layout) es un modelo de layout unidimensional —explicó Carolina—. Distribuye el espacio en una sola dirección: fila (horizontal) o columna (vertical). Es perfecto para alinear elementos, distribuir espacio, y crear diseños flexibles.

—Piénsalo así: tienes una caja flexible (el **flex container**) y dentro tienes elementos (los **flex items**). El contenedor decide cómo se distribuyen los hijos.

## display: flex

```css
.contenedor-galeria {
  display: flex; /* Activa Flexbox en el contenedor */
}
```

—Con solo esa línea, los hijos del contenedor se alinean horizontalmente uno al lado del otro.

## flex-direction

```css
/* Dirección principal: fila (por defecto) */
flex-direction: row;

/* Fila invertida */
flex-direction: row-reverse;

/* Columna */
flex-direction: column;

/* Columna invertida */
flex-direction: column-reverse;
```

—El **eje principal** (main axis) sigue la dirección de `flex-direction`. El **eje transversal** (cross axis) es perpendicular.

## justify-content: Alineación en el eje principal

```css
.contenedor {
  display: flex;
  justify-content: flex-start;   /* Al inicio (por defecto) */
  justify-content: flex-end;     /* Al final */
  justify-content: center;       /* Centrado */
  justify-content: space-between; /* Espacio igual entre elementos */
  justify-content: space-around;  /* Espacio alrededor de cada elemento */
  justify-content: space-evenly;  /* Espacio uniforme */
}
```

Carolina mostró un diagrama textual:

```
flex-start:    [A][B][C]                      
center:               [A][B][C]               
flex-end:                        [A][B][C]    
space-between: [A]    [B]    [C]             
space-around:   [A]   [B]   [C]              
space-evenly:   [A]  [B]  [C]               
```

## align-items: Alineación en el eje transversal

```css
.contenedor {
  display: flex;
  align-items: stretch;     /* Estirar al alto del contenedor (por defecto) */
  align-items: flex-start;  /* Alinear al inicio del eje transversal */
  align-items: flex-end;    /* Alinear al final */
  align-items: center;      /* Centrar verticalmente */
  align-items: baseline;    /* Alinear por la línea base del texto */
}
```

## flex-wrap

```css
.contenedor {
  display: flex;
  flex-wrap: nowrap;    /* No saltan de línea (por defecto) */
  flex-wrap: wrap;      /* Saltan a la siguiente línea si no caben */
  flex-wrap: wrap-reverse; /* Saltan en dirección inversa */
}
```

## gap: Espacio entre elementos

—La forma más limpia de agregar espacio entre elementos flex:

```css
.contenedor {
  display: flex;
  gap: 20px;           /* Espacio de 20px entre cada elemento */
  gap: 15px 30px;      /* row-gap y column-gap */
}
```

## flex-grow, flex-shrink, flex-basis

—Estas propiedades se aplican a los **hijos** (flex items):

```css
/* Los elementos crecen para llenar el espacio disponible */
.item {
  flex-grow: 1;   /* Todos crecen por igual */
}

.item-doble {
  flex-grow: 2;   /* Crece el doble que los demás */
}

/* Los elementos se encogen si no hay espacio */
.item {
  flex-shrink: 1;   /* Valor por defecto */
}

/* Tamaño base antes de crecer o encoger */
.item {
  flex-basis: 200px;  /* Tamaño inicial */
}

/* Shorthand */
.item {
  flex: 1;             /* flex-grow: 1, flex-shrink: 1, flex-basis: 0 */
  flex: 1 0 200px;     /* grow, shrink, basis */
}
```

## order y align-self

```css
/* Cambiar el orden visual (no el orden en HTML) */
.item-important {
  order: -1;  /* Valores menores = aparecen primero */
}

.item-final {
  order: 1;   /* Valores mayores = aparecen al final */
}

/* Alinear un elemento individual en el eje transversal */
.item-especial {
  align-self: flex-end;  /* Solo este elemento se alinea al final */
}
```

## La galería de arte

Mateo construyó la galería para "Cultura Viva":

```css
/* === Contenedor de la galería === */
.galeria {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  padding: 20px 0;
}

/* === Cada imagen en la galería === */
.galeria-item {
  flex: 1 0 250px;      /* Crece, se encoge, base 250px */
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.galeria-item:hover {
  transform: scale(1.03);
}

.galeria-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;    /* Recorta la imagen para llenar el espacio */
  display: block;
}

/* === Tarjetas de artículos con Flexbox === */
.fila-articulos {
  display: flex;
  gap: 25px;
  margin: 30px 0;
}

.tarjeta-articulo {
  flex: 1;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.tarjeta-articulo .contenido {
  padding: 20px;
}

.tarjeta-articulo h3 {
  margin-bottom: 10px;
}

.tarjeta-articulo .meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  padding-top: 10px;
  border-top: 1px solid #eee;
  font-size: 13px;
  color: #888;
}

/* === Barra de navegación con Flexbox === */
.nav-links {
  display: flex;
  align-items: center;
  gap: 25px;
  list-style: none;
}

.nav-links li:last-child {
  margin-left: auto;    /* Empuja el último elemento al extremo opuesto */
}
```

Mateo probó la galería. Redimensionó la ventana y las imágenes se reordenaron solas. Cuando la pantalla era ancha, aparecían cuatro por fila. Cuando se hacía estrecha, pasaban a tres, luego a dos, luego a una. Sin una sola línea de JavaScript.

—Es mágico —dijo Mateo.

—No es magia —respondió Carolina—. Es Flexbox. Una de las herramientas más poderosas de CSS. Con Flexbox puedes hacer layouts que antes requerían trucos complicados o JavaScript.

—¿Entonces Flexbox sirve para todo? —preguntó Mateo.

—No todo —dijo Carolina, con una sonrisa misteriosa—. Para layouts bidimensionales —filas y columnas al mismo tiempo— hay algo incluso mejor. Pero eso será mañana.

---

## Enigmas del Capítulo 5

**Enigma 5.1:** Usando Flexbox, crea un contenedor que tenga 3 elementos centrados horizontal y verticalmente dentro de él. El contenedor debe medir 400px de alto.

**Enigma 5.2:** Crea una barra de navegación horizontal con Flexbox donde:
- El logo esté a la izquierda
- Los enlaces de navegación estén centrados
- Un botón "Suscribirse" esté a la derecha

**Enigma 5.3:** ¿Cuál es la diferencia entre `justify-content: center` y `align-items: center`? ¿En qué eje trabaja cada uno?

**Enigma 5.4:** Diseña tres tarjetas de igual ancho usando `flex: 1`. La tarjeta del medio debe tener `flex: 2` (el doble de ancho). Explica por qué funciona.

**Enigma 5.5:** ¿Qué hace `flex-wrap: wrap` y por qué es importante para el diseño responsivo?
