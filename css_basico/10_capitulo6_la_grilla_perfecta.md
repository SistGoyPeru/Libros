# Capítulo 6: La Grilla Perfecta

*Tema: CSS Grid*

---

—Bien —dijo Carolina al día siguiente, abriendo el diseño de la portada digital de "Cultura Viva"—. La portada de la revista. Aquí es donde Flexbox se queda corto.

Mateo miró el diseño. Era un layout complejo: un título grande que ocupaba dos columnas, una imagen destacada, tres artículos secundarios, una cita lateral, y una barra de "lo más leído". Todo en una cuadrícula de filas y columnas que se entrecruzaban.

—Esto necesita **CSS Grid** —dijo Carolina—. Flexbox es unidimensional (una sola fila o columna). Grid es bidimensional: puedes controlar filas y columnas al mismo tiempo.

## ¿Qué es CSS Grid?

—**CSS Grid** es un sistema de layout bidimensional. Piensa en una hoja de papel cuadriculado donde puedes ubicar elementos en celdas específicas, combinando celdas para formar áreas más grandes.

## display: grid

```css
.contenedor-portada {
  display: grid;
}
```

—Así de simple se activa Grid. Pero para que haga algo útil, necesitas definir las columnas y filas.

## grid-template-columns y grid-template-rows

```css
.contenedor {
  display: grid;
  grid-template-columns: 200px 200px 200px;    /* 3 columnas de 200px */
  grid-template-rows: 100px 200px;              /* 2 filas de 100px y 200px */
}
```

### La unidad fr

—La unidad más poderosa de Grid: **fr** (fracción). Divide el espacio disponible en fracciones.

```css
.contenedor {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;  /* 4 fracciones: la del medio es el doble */
}

/* Equivalente a: 25% 50% 25% */
```

### repeat() y minmax()

```css
/* 3 columnas iguales */
grid-template-columns: repeat(3, 1fr);

/* 4 columnas, mínimo 200px, máximo 1fr (se expanden) */
grid-template-columns: repeat(4, minmax(200px, 1fr));

/* Columnas automáticas */
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
/* Crea tantas columnas de 250px como quepan */
```

## gap en Grid

```css
.contenedor {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;           /* Espacio entre filas y columnas */
  row-gap: 15px;       /* Solo entre filas */
  column-gap: 25px;    /* Solo entre columnas */
}
```

## Colocar elementos: grid-column y grid-row

—Los hijos del grid se colocan automáticamente en celdas consecutivas. Pero puedes controlar su posición:

```css
.header-portada {
  grid-column: 1 / 3;      /* De la línea 1 a la línea 3 (ocupa 2 columnas) */
  grid-row: 1 / 2;         /* De la línea 1 a la línea 2 (1 fila) */
}

.articulo-principal {
  grid-column: 1 / 3;      /* Ocupa 2 columnas */
  grid-row: 2 / 4;         /* Ocupa 2 filas */
}

.barra-lateral {
  grid-column: 3 / 4;      /* Tercera columna */
  grid-row: 1 / 4;         /* Toda la altura */
}
```

—También puedes usar `span`:

```css
grid-column: span 2;   /* Ocupa 2 columnas */
grid-row: span 3;      /* Ocupa 3 filas */
```

## grid-area

—Puedes nombrar áreas del grid para hacerlo más legible:

```css
.contenedor {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: auto auto auto;
  grid-template-areas:
    "header     header"
    "principal  sidebar"
    "footer     footer";
  gap: 20px;
}

.header  { grid-area: header; }
.main    { grid-area: principal; }
.aside   { grid-area: sidebar; }
.footer  { grid-area: footer; }
```

—Esto hace que el CSS sea mucho más legible. Ves el layout directamente en el código.

## place-items: Centrado en Grid

```css
.contenedor {
  display: grid;
  place-items: center;  /* Centra los hijos horizontal y verticalmente */
  height: 500px;
}
```

—`place-items` es shorthand para `align-items` y `justify-items`.

## La portada digital

Mateo construyó el layout de la portada:

```css
/* === Layout de la portada === */
.portada {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-rows: auto auto auto;
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* === Áreas de la portada === */
.titulo-principal {
  grid-column: 1 / 2;
  grid-row: 1 / 3;
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  color: white;
  padding: 40px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.titulo-principal h1 {
  font-size: 48px;
  line-height: 1.2;
  margin-bottom: 20px;
}

.imagen-destacada {
  grid-column: 2 / 4;
  grid-row: 1 / 2;
}

.imagen-destacada img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
}

/* === Los 3 artículos secundarios en fila === */
.articulos-secundarios {
  grid-column: 1 / 4;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.articulo-secundario {
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

/* === Cita lateral === */
.cita-lateral {
  grid-column: 1 / 2;
  background-color: #f5f0eb;
  padding: 30px;
  border-radius: 8px;
  border-left: 5px solid #8B0000;
  font-style: italic;
  font-size: 18px;
}

/* === Lo más leído === */
.mas-leido {
  grid-column: 2 / 4;
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.mas-leido ol {
  list-style-position: inside;
}

.mas-leido li {
  padding: 10px 0;
  border-bottom: 1px solid #eee;
  font-weight: 600;
}

/* === Pie de página con Grid === */
.footer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  background-color: #1a1a2e;
  color: white;
  padding: 50px;
  margin-top: 50px;
  border-radius: 12px 12px 0 0;
}

.footer-grid h4 {
  font-family: "Playfair Display", serif;
  margin-bottom: 15px;
  color: #e8d5c4;
}

.footer-grid a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  display: block;
  margin-bottom: 8px;
}
```

Mateo probó el layout. Redimensionó la ventana y, aunque el grid se mantenía firme, notó que en pantallas pequeñas el diseño se rompía.

—Ya veo el problema —dijo—. Esto no funciona bien en móvil.

—Exacto —respondió Carolina—. Y de eso hablaremos mañana.

---

## Enigmas del Capítulo 6

**Enigma 6.1:** Crea un grid de 4 columnas iguales usando `repeat()`. Cada columna debe tener un gap de 15px.

**Enigma 6.2:** Usando `grid-template-areas`, crea un layout con:
- Header en la parte superior (ocupa todo el ancho)
- Menú lateral a la izquierda (200px)
- Contenido principal al centro (ocupa el resto)
- Widget a la derecha (250px)
- Footer al fondo (todo el ancho)

**Enigma 6.3:** ¿Cuál es la diferencia entre `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))` y `grid-template-columns: repeat(3, 1fr)`?

**Enigma 6.4:** Diseña un grid para una galería de imágenes donde:
- La primera imagen ocupe 2 columnas y 2 filas
- Las demás imágenes ocupen 1 columna y 1 fila cada una
- Usa `grid-column` y `grid-row`

**Enigma 6.5:** Explica cuándo usarías Flexbox y cuándo usarías Grid. Da ejemplos concretos de cada uno.
