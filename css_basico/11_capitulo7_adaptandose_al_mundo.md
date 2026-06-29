# Capítulo 7: Adaptándose al Mundo

*Tema: Responsive Design y Media Queries*

---

—Mateo —dijo Carolina una mañana, con el teléfono en la mano—, tenemos un problema.

Mateo levantó la vista de su pantalla.

—Acabo de recibir un correo del editor de "Cultura Viva". Dice que varios lectores se han quejado. El sitio se ve bien en computadora, pero en el móvil... —Carolina giró su teléfono para mostrarle—. Mira.

En la pantalla del teléfono, el sitio de "Cultura Viva" era un desastre. El texto era minúsculo, las imágenes se desbordaban, los menús se superponían. Era ilegible.

—El problema —dijo Carolina— es que diseñaste para una pantalla específica. Pero la web se ve en miles de dispositivos diferentes: teléfonos, tablets, laptops, monitores enormes. Necesitas hacer que el sitio sea **responsivo**.

## El viewport meta

—Lo primero: el **viewport**. Sin esta etiqueta, los navegadores móviles muestran el sitio como si fuera una pantalla de escritorio, obligando al usuario a hacer zoom.

```html
<!-- En el <head> del HTML -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

—`width=device-width` hace que el ancho del viewport sea el del dispositivo. `initial-scale=1.0` establece el zoom inicial al 100%.

## Media Queries

—Las **media queries** son la herramienta principal del diseño responsivo. Te permiten aplicar estilos diferentes según ciertas condiciones: ancho de pantalla, orientación, tipo de dispositivo.

```css
/* Si la pantalla mide 768px o menos */
@media (max-width: 768px) {
  body {
    font-size: 14px;
  }

  .sidebar {
    display: none;
  }
}
```

—Sintaxis básica:

```css
@media (condición) {
  /* Reglas CSS que se aplican solo cuando se cumple la condición */
}
```

### Operadores comunes

```css
/* Pantallas de hasta 600px */
@media (max-width: 600px) { }

/* Pantallas de 601px en adelante */
@media (min-width: 601px) { }

/* Entre 601px y 1024px */
@media (min-width: 601px) and (max-width: 1024px) { }

/* Orientación horizontal */
@media (orientation: landscape) { }

/* Pantallas táctiles */
@media (hover: none) and (pointer: coarse) { }
```

## Mobile-first vs Desktop-first

—Hay dos enfoques para escribir CSS responsivo —explicó Carolina—.

### Desktop-first

```css
/* Estilos base para desktop */
.header { ... }

/* Luego se sobreescriben para pantallas más pequeñas */
@media (max-width: 768px) {
  .header { ... }
}

@media (max-width: 480px) {
  .header { ... }
}
```

### Mobile-first

```css
/* Estilos base para móvil */
.header { ... }

/* Luego se mejoran para pantallas más grandes */
@media (min-width: 768px) {
  .header { ... }
}

@media (min-width: 1024px) {
  .header { ... }
}
```

—Hoy en día se recomienda **mobile-first** —dijo Carolina—. Empiezas con el diseño más simple (móvil) y vas agregando complejidad a medida que hay más espacio.

## Breakpoints comunes

—Los **breakpoints** son los puntos donde el diseño cambia. No hay valores mágicos, pero estos son puntos de referencia:

```css
/* Móvil pequeño: < 480px */
/* Móvil: 480px - 768px */
/* Tablet: 768px - 1024px */
/* Desktop: 1024px - 1440px */
/* Pantallas grandes: > 1440px */
```

## Imágenes responsivas

```css
/* La imagen nunca supera el ancho de su contenedor */
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

—Con `max-width: 100%`, las imágenes se encogen cuando el contenedor es más pequeño que la imagen, pero no se estiran más allá de su tamaño original.

## Unidades relativas

—Usar píxeles fijos para todo hace que el diseño sea rígido. Las **unidades relativas** son clave para la flexibilidad:

| Unidad | Relativa a | Ejemplo |
|--------|-----------|---------|
| `%` | El contenedor padre | `width: 50%` |
| `em` | El font-size del elemento | `padding: 2em` |
| `rem` | El font-size del `<html>` | `font-size: 1.2rem` |
| `vw` | 1% del ancho del viewport | `width: 80vw` |
| `vh` | 1% del alto del viewport | `height: 100vh` |

—`rem` es excelente para tipografía porque escala con la configuración del usuario:

```css
html {
  font-size: 16px; /* Tamaño base */
}

h1 {
  font-size: 2.5rem; /* 40px */
}

p {
  font-size: 1rem; /* 16px */
}

@media (max-width: 768px) {
  html {
    font-size: 14px; /* Reduce todo proporcionalmente */
  }
}
```

## Haciendo "Cultura Viva" responsivo

Mateo reescribió el CSS para que fuera mobile-first:

```css
/* === ESTILOS BASE (móvil primero) === */

html {
  font-size: 16px;
}

body {
  font-size: 1rem;
  margin: 0;
  padding: 15px;
}

/* Header: simple en móvil */
.header-principal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  padding: 0 15px;
  display: flex;
  align-items: center;
}

.header-principal nav a {
  font-size: 12px;
  margin-left: 10px;
}

.contenido-principal {
  margin-top: 60px;
  padding: 15px;
}

/* Galería: una columna en móvil */
.galeria {
  display: grid;
  grid-template-columns: 1fr;
  gap: 15px;
}

/* Columnas: apiladas en móvil */
.layout-columnas {
  display: block;
}

.barra-lateral {
  position: static; /* Vuelve al flujo normal */
  margin-top: 30px;
}

/* Footer: simple en móvil */
.footer-grid {
  grid-template-columns: 1fr;
  text-align: center;
}

/* === TABLET (>= 768px) === */
@media (min-width: 768px) {
  body {
    padding: 20px;
  }

  .galeria {
    grid-template-columns: repeat(2, 1fr);
  }

  .layout-columnas {
    display: flex;
    gap: 25px;
  }

  .barra-lateral {
    position: sticky;
    top: 80px;
    flex: 0 0 300px;
  }

  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
    text-align: left;
  }
}

/* === DESKTOP (>= 1024px) === */
@media (min-width: 1024px) {
  .contenido-principal {
    max-width: 1200px;
    margin: 70px auto 0;
    padding: 30px;
  }

  .galeria {
    grid-template-columns: repeat(3, 1fr);
  }

  .footer-grid {
    grid-template-columns: repeat(4, 1fr);
  }

  .header-principal {
    padding: 0 40px;
  }

  .header-principal nav a {
    font-size: 14px;
    margin-left: 25px;
  }
}

/* === PANTALLAS GRANDES (>= 1440px) === */
@media (min-width: 1440px) {
  .galeria {
    grid-template-columns: repeat(4, 1fr);
  }

  html {
    font-size: 18px; /* Texto más grande en monitores grandes */
  }
}
```

Mateo guardó los cambios, agarró su teléfono, y abrió el sitio. El diseño se veía limpio. El menú era legible. Las imágenes se ajustaban al ancho de la pantalla. Hizo scroll, giró el teléfono a horizontal, y todo seguía funcionando.

—Ahora sí —dijo Carolina, asintiendo con satisfacción—. Esto es un sitio web moderno.

---

## Enigmas del Capítulo 7

**Enigma 7.1:** Usando media queries, haz que un menú de navegación horizontal se convierta en un menú vertical apilado cuando la pantalla sea menor a 600px.

**Enigma 7.2:** ¿Cuál es la diferencia entre `em` y `rem`? ¿Cuándo usarías cada uno?

**Enigma 7.3:** Diseña una tarjeta que en desktop tenga `width: 300px` y esté en `inline-block`, pero en móvil (< 480px) ocupe el 100% del ancho.

**Enigma 7.4:** Explica por qué es importante la etiqueta `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. ¿Qué pasa si no la incluyes?

**Enigma 7.5:** Crea un hero (banner principal) que ocupe `100vh` de alto (toda la pantalla) y tenga una imagen de fondo responsiva.
