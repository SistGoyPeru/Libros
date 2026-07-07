# Capítulo 4: Poniendo Orden

*Tema: Display y positioning*

---

El sitio de "Cultura Viva" comenzaba a tomar forma. Los colores funcionaban, la tipografía era elegante, las tarjetas se alineaban correctamente. Pero Mateo enfrentaba un nuevo desafío: el diseño necesitaba un **header fijo** que permaneciera visible mientras el usuario hacía scroll, una **barra lateral** con los artículos más populares, y un layout general que no se desarmara al cambiar el tamaño de la ventana.

—Lo que necesitas —dijo Carolina, viendo a Mateo forcejear con el CSS— es entender **position** y controlar el flujo de los elementos.

## Position: La posición de los elementos

—Por defecto, los elementos tienen `position: static`. Siguen el flujo normal del documento: uno tras otro, de arriba a abajo.

```css
position: static; /* Valor por defecto: flujo normal */
```

—Pero a veces necesitas sacar elementos del flujo normal y posicionarlos en lugares específicos.

### position: relative

```css
.header {
  position: relative;
  top: 10px;     /* Se desplaza 10px hacia abajo desde su posición original */
  left: 20px;    /* Se desplaza 20px hacia la derecha */
}
```

—**Relative** mantiene el elemento en el flujo normal (su espacio original se reserva), pero puedes desplazarlo visualmente usando `top`, `right`, `bottom`, `left`.

### position: absolute

```css
.boton-flotante {
  position: absolute;
  top: 20px;
  right: 20px;
}
```

—**Absolute** saca el elemento del flujo normal. Se posiciona en relación al **ancestro posicionado** más cercano (el primer ancestro con `position` diferente de `static`). Si no hay ninguno, se posiciona en relación al `<html>`.

—Esto es muy útil para superponer elementos —dijo Carolina—. Por ejemplo, una etiqueta sobre una imagen:

```css
.contenedor-imagen {
  position: relative; /* El ancestro de referencia */
}

.etiqueta {
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: rgba(139, 0, 0, 0.8);
  color: white;
  padding: 5px 10px;
}
```

### position: fixed

```css
.header-principal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  background-color: #1a1a2e;
  color: white;
  z-index: 1000;
}
```

—**Fixed** es como absolute, pero se posiciona en relación a la ventana del navegador (viewport). El elemento permanece fijo incluso cuando haces scroll.

—Perfecto para el header —dijo Mateo.

### position: sticky

```css
.barra-lateral {
  position: sticky;
  top: 80px; /* Se vuelve fijo cuando el scroll llega a 80px del tope */
}
```

—**Sticky** es un híbrido. El elemento se comporta como `relative` hasta que el scroll alcanza cierta posición, luego se comporta como `fixed`.

## z-index: La profundidad

—Cuando los elementos se superponen, necesitas controlar qué elemento está adelante y cuál atrás.

```css
.header-principal {
  z-index: 1000;  /* Mayor valor = más al frente */
}

.modal {
  z-index: 2000;
}

.menu-desplegable {
  z-index: 1500;
}
```

—El **z-index** solo funciona en elementos posicionados (con `position` diferente de `static`).

## Overflow: ¿Qué hacer con el contenido que se desborda?

```css
.contenedor {
  width: 300px;
  height: 200px;
  overflow: hidden;      /* Oculta el contenido que desborda */
  overflow: scroll;      /* Muestra barras de scroll siempre */
  overflow: auto;        /* Muestra scroll solo cuando es necesario */
  overflow-x: hidden;    /* Control horizontal */
  overflow-y: auto;      /* Control vertical */
}
```

## Float y Clear

—Antes de Flexbox y Grid, **float** era la forma principal de crear layouts. Hoy se usa menos, pero aún es útil para imágenes envueltas en texto.

```css
.imagen-articulo {
  float: left;   /* La imagen flota a la izquierda, el texto la rodea */
  margin-right: 20px;
  margin-bottom: 10px;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

—**Clear** "limpia" los floats: evita que elementos posteriores se vean afectados por el float.

## Construyendo el layout

Mateo aplicó todo lo aprendido para el layout de "Cultura Viva":

```css
/* === Reset básico === */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* === Header fijo === */
.header-principal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 70px;
  background-color: #1a1a2e;
  color: white;
  z-index: 100;
  display: flex;
  align-items: center;
  padding: 0 30px;
}

.header-principal .logo {
  font-family: "Playfair Display", serif;
  font-size: 24px;
  color: white;
  text-decoration: none;
}

.header-principal nav {
  margin-left: auto;
}

.header-principal nav a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  margin-left: 20px;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.header-principal nav a:hover {
  color: white;
}

/* === Espacio para el contenido (por el header fijo) === */
.contenido-principal {
  margin-top: 70px;
  padding: 30px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

/* === Artículo con imagen flotante === */
.articulo {
  margin-bottom: 40px;
  overflow: hidden;
}

.articulo img {
  float: left;
  margin-right: 25px;
  margin-bottom: 15px;
  border-radius: 6px;
  max-width: 300px;
}

.articulo h2 {
  margin-bottom: 15px;
}

/* === Barra lateral sticky === */
.layout-columnas {
  display: flex;
  gap: 30px;
}

.columna-principal {
  flex: 2;
}

.barra-lateral {
  flex: 1;
  position: sticky;
  top: 90px;
  align-self: flex-start;
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.barra-lateral h3 {
  font-size: 18px;
  border-bottom: 2px solid #8B0000;
  padding-bottom: 8px;
  margin-bottom: 15px;
}

.barra-lateral ul {
  list-style: none;
}

.barra-lateral li {
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.barra-lateral li a {
  color: #333;
  text-decoration: none;
}

.barra-lateral li a:hover {
  color: #8B0000;
}
```

Mateo probó el resultado. El header se mantenía fijo en la parte superior. La barra lateral seguía al usuario hasta cierto punto y luego se quedaba pegada. Las imágenes flotaban dentro de los artículos con el texto rodeándolas. El layout se veía profesional.

—Esto ya parece un sitio web de verdad —dijo Mateo.

—Esto ya es un sitio web de verdad —corrigió Carolina—. Ahora entiendes por qué la posición de los elementos es tan importante como su estilo. Controlar dónde está cada cosa es lo que separa un diseño amateur de uno profesional.

---

## Enigmas del Capítulo 4

**Enigma 4.1:** Crea un botón "Volver arriba" que esté fijo en la esquina inferior derecha de la pantalla. Debe tener un z-index alto para que siempre esté visible.

**Enigma 4.2:** Explica la diferencia entre `position: absolute` y `position: fixed`. ¿Cuándo usarías cada uno?

**Enigma 4.3:** Diseña una tarjeta de artículo que tenga una etiqueta "Nuevo" superpuesta en la esquina superior izquierda usando `position: absolute`.

**Enigma 4.4:** ¿Qué problema resuelve `overflow: hidden` en un contenedor que tiene hijos con `float`?

**Enigma 4.5:** ¿Qué es el contexto de apilamiento? ¿Cómo afecta `z-index` a los elementos que están en diferentes contenedores posicionados?
