# Apéndice: Soluciones a los Enigmas

### Capítulo 1: El Primer Estilo

**Enigma 1.1:**
```css
a {
  color: #006400;
  text-decoration: none;
  font-weight: bold;
}
```

**Enigma 1.2:**
```css
.autor {
  font-style: italic;
  color: #666;
  font-size: 14px;
  text-align: right;
}
```

**Enigma 1.3:**
Un selector de clase (`.clase`) puede usarse en múltiples elementos. Un selector de ID (`#id`) debe ser único en la página. Usa clases para estilos reutilizables (ej: `.destacado`, `.tarjeta`). Usa ID para elementos únicos (ej: `#logo`, `#menu-principal`).

**Enigma 1.4:**
```css
#titulo {
  color: navy;
  text-align: center;
  font-size: 40px;
}

.subtitulo {
  color: gray;
  font-size: 20px;
  text-transform: uppercase;
}

.intro {
  background-color: #eef;
  padding: 20px;
}
```

**Enigma 1.5:**
"En cascada" significa que cuando hay múltiples reglas CSS que afectan al mismo elemento, se aplica un orden de prioridad: la regla más específica o la que está definida después prevalece. También implica que los estilos se heredan de elementos padres a hijos (como el `font-family` del `body`).

---

### Capítulo 2: La Paleta de Colores

**Enigma 2.1:**
```css
body {
  background: linear-gradient(#f5f0eb, #e8d5c4);
  min-height: 100vh;
}
```

**Enigma 2.2:**
```css
a {
  color: #333;
  transition: color 0.3s ease;
}

a:hover {
  color: #8B0000;
}
```

**Enigma 2.3:**
HTML (en el `<head>`):
```html
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700&family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
```
CSS:
```css
article, .articulo {
  font-family: "Merriweather", Georgia, serif;
}

nav, .menu, .navegacion {
  font-family: "Montserrat", Arial, sans-serif;
}
```

**Enigma 2.4:**
- `#FFFFFF` → rgb(255, 255, 255)
- `#000000` → rgb(0, 0, 0)
- `#8B0000` → rgb(139, 0, 0)
- `#2E8B57` → rgb(46, 139, 87)

**Enigma 2.5:**
`background-size: cover` escala la imagen para que cubra todo el contenedor, manteniendo la proporción. Recorta los bordes si es necesario. Sin `cover`, la imagen se muestra en su tamaño original y puede repetirse, dejando espacios blancos o distorsionándose.

---

### Capítulo 3: El Espacio entre Líneas

**Enigma 3.1:**
Con `content-box` (por defecto):
ancho total = 200 + 15 + 15 + 3 + 3 = **236px**

Con `border-box`:
ancho total = **200px** (el padding y borde se restan del contenido).

**Enigma 3.2:**
```css
.tarjeta-perfil {
  width: 280px;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin-bottom: 25px;
  background-color: white;
}
```

**Enigma 3.3:**
Los márgenes colapsados ocurren cuando dos márgenes verticales se encuentran y se fusionan en uno solo (el mayor). Ejemplo: un `h1` con `margin-bottom: 30px` seguido de un `p` con `margin-top: 20px`. El espacio entre ellos será 30px, no 50px.

**Enigma 3.4:**
```css
.boton {
  background-color: #8B0000;
  color: white;
  text-decoration: none;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.boton:hover {
  background-color: #a52a2a;
}
```

**Enigma 3.5:**
- `block`: ocupa todo el ancho disponible, respeta width/height, genera saltos de línea. Ej: `<div>`, `<p>`, `<h1>`.
- `inline`: ocupa solo el espacio necesario, ignora width/height, NO genera saltos. Ej: `<span>`, `<a>`, `<strong>`.
- `inline-block`: como inline, PERO respeta width, height, margin y padding. Ej: botones en una fila, tarjetas en grid.

---

### Capítulo 4: Poniendo Orden

**Enigma 4.1:**
```css
.btn-volver-arriba {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 9999;
  background-color: #8B0000;
  color: white;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-size: 24px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  cursor: pointer;
}
```

**Enigma 4.2:**
`position: absolute` se posiciona en relación al ancestro posicionado más cercano. `position: fixed` se posiciona en relación al viewport (ventana del navegador). Usa `absolute` para elementos dentro de un contenedor (ej: etiqueta sobre imagen). Usa `fixed` para elementos que siempre deben estar visibles (ej: header, botón flotante).

**Enigma 4.3:**
```css
.contenedor-tarjeta {
  position: relative;
}

.etiqueta-nuevo {
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: #8B0000;
  color: white;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
}
```

**Enigma 4.4:**
Cuando los hijos tienen `float`, el contenedor padre colapsa (altura 0) porque los hijos flotantes salen del flujo normal. `overflow: hidden` (o `auto`) hace que el contenedor reconozca la altura de los hijos flotantes y se expanda para contenerlos. También se puede usar el `clearfix`.

**Enigma 4.5:**
El contexto de apilamiento es un grupo de elementos que comparten el mismo espacio en el eje Z. Se crea con `position` + `z-index`, `opacity < 1`, `transform`, etc. El `z-index` solo compara elementos dentro del mismo contexto. Si dos elementos están en diferentes contextos de apilamiento, sus `z-index` no se comparan directamente.

---

### Capítulo 5: Flexibilidad

**Enigma 5.1:**
```css
.contenedor {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
  gap: 20px;
}
```

**Enigma 5.2:**
```css
.nav-barra {
  display: flex;
  align-items: center;
  padding: 0 20px;
}

.nav-links {
  display: flex;
  gap: 20px;
  margin: 0 auto;
}

.btn-suscribirse {
  margin-left: auto;
}
```

**Enigma 5.3:**
`justify-content` alinea en el **eje principal** (horizontal por defecto). `align-items` alinea en el **eje transversal** (vertical por defecto). Si `flex-direction` cambia a `column`, los ejes se intercambian.

**Enigma 5.4:**
```css
.tarjeta { flex: 1; }
.tarjeta.medio { flex: 2; }
```
Flex: 1 divide el espacio disponible en 4 partes iguales (1+2+1). La tarjeta del medio ocupa 2 partes (la mitad), las otras ocupan 1 parte cada una (un cuarto).

**Enigma 5.5:**
`flex-wrap: wrap` permite que los elementos flexibles salten a la siguiente línea si no caben en el ancho del contenedor. Es esencial para diseño responsivo porque evita que los elementos se encojan demasiado o se salgan del contenedor.

---

### Capítulo 6: La Grilla Perfecta

**Enigma 6.1:**
```css
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 15px;
}
```

**Enigma 6.2:**
```css
.layout {
  display: grid;
  grid-template-columns: 200px 1fr 250px;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header  header"
    "menu    main    widget"
    "footer  footer  footer";
  min-height: 100vh;
  gap: 15px;
}

.header  { grid-area: header; }
.menu    { grid-area: menu; }
.main    { grid-area: main; }
.widget  { grid-area: widget; }
.footer  { grid-area: footer; }
```

**Enigma 6.3:**
`repeat(auto-fit, minmax(200px, 1fr))` crea tantas columnas de mínimo 200px como quepan en el contenedor. Si el contenedor es de 450px, crea 2 columnas. Si es de 650px, crea 3. Es responsivo automático.

`repeat(3, 1fr)` siempre crea exactamente 3 columnas iguales, sin importar el tamaño del contenedor.

**Enigma 6.4:**
```css
.galeria-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.galeria-grid .destacada {
  grid-column: span 2;
  grid-row: span 2;
}
```

**Enigma 6.5:**
Usa **Flexbox** cuando trabajes en una sola dirección: filas de tarjetas, barras de navegación, centrar elementos, alinear contenido en un eje.

Usa **Grid** cuando necesites control bidimensional (filas y columnas): layouts de página completa, galerías complejas, portadas de revistas, dashboards.

---

### Capítulo 7: Adaptándose al Mundo

**Enigma 7.1:**
```css
.nav-menu {
  display: flex;
  gap: 20px;
  list-style: none;
}

@media (max-width: 600px) {
  .nav-menu {
    flex-direction: column;
    gap: 10px;
  }
}
```

**Enigma 7.2:**
`em` es relativa al `font-size` del elemento padre. `rem` es relativa al `font-size` del elemento `<html>` (raíz). Usa `rem` para tamaños globales (tipografía, espaciado) porque permite escalar todo el sitio cambiando un solo valor. Usa `em` para tamaños que deben escalar con su contenedor local.

**Enigma 7.3:**
```css
.tarjeta {
  width: 300px;
  display: inline-block;
}

@media (max-width: 480px) {
  .tarjeta {
    width: 100%;
    display: block;
  }
}
```

**Enigma 7.4:**
La etiqueta `<meta name="viewport">` le dice al navegador móvil que use el ancho real del dispositivo en lugar de simular una pantalla de escritorio. Sin ella, los sitios se ven "zoomados" y el usuario debe hacer pinza para leer el contenido.

**Enigma 7.5:**
```css
.hero {
  height: 100vh;
  background-image: url("hero.jpg");
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
}
```

---

### Capítulo 8: El Toque Mágico

**Enigma 8.1:**
```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.elemento {
  animation: bounce 1s ease-in-out infinite;
}
```

**Enigma 8.2:**
```css
.boton {
  background-color: #8B0000;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
}

.boton:hover {
  background-color: #a52a2a;
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(139, 0, 0, 0.3);
}
```

**Enigma 8.3:**
```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #ddd;
  border-top-color: #8B0000;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
```

**Enigma 8.4:**
`transition` anima cambios de un estado a otro (ej: hover a normal). Se activa automáticamente cuando cambia una propiedad. Ideal para hover effects y cambios simples.

`animation` permite animaciones más complejas con múltiples pasos, repeticiones, y control independiente. Necesita `@keyframes`. Ideal para animaciones continuas (spinners), secuencias, o animaciones de entrada.

**Enigma 8.5:**
`animation-fill-mode: forwards` mantiene el estado final de la animación cuando esta termina. Sin esto, el elemento vuelve a su estado inicial. Es útil para animaciones de entrada (fadeIn, slideIn) donde el elemento debe quedarse visible después de la animación.

---

### Capítulo 9: Detalles que Importan

**Enigma 9.1:**
```css
.destacados li::before {
  content: "★";
  color: gold;
  margin-right: 8px;
}
```

**Enigma 9.2:**
```css
.nav-menu a {
  position: relative;
  text-decoration: none;
  color: #333;
}

.nav-menu a::after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #8B0000;
  transition: width 0.3s ease;
}

.nav-menu a:hover::after {
  width: 100%;
}
```

**Enigma 9.3:**
```css
.galeria-item:nth-child(3),
.galeria-item:nth-child(6) {
  border: 3px solid gold;
  border-radius: 8px;
}
```

**Enigma 9.4:**
```css
[data-tooltip] {
  position: relative;
  cursor: help;
}

[data-tooltip]::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #333;
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 13px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
}

[data-tooltip]:hover::after {
  opacity: 1;
}
```

**Enigma 9.5:**
Pseudo-clases (`:`) describen un estado del elemento: `:hover` (mouse encima), `:focus` (enfocado), `:nth-child(2)` (segundo hijo).

Pseudo-elementos (`::`) crean elementos virtuales: `::before` (contenido antes del elemento), `::after` (después), `::first-letter` (primera letra).

---

### Capítulo 10: El Lanzamiento

**Enigma 10.1:**
```css
.header-principal.translucido {
  background-color: rgba(26, 26, 46, 0.9);
  backdrop-filter: blur(10px);
}
```
(La clase `.translucido` se agregaría con JavaScript al hacer scroll)

**Enigma 10.2:**
```css
.grid-articulos .tarjeta-articulo {
  animation: fadeInUp 0.6s ease-out both;
}

.grid-articulos .tarjeta-articulo:nth-child(1) { animation-delay: 0s; }
.grid-articulos .tarjeta-articulo:nth-child(2) { animation-delay: 0.2s; }
.grid-articulos .tarjeta-articulo:nth-child(3) { animation-delay: 0.4s; }
```

**Enigma 10.3:**
```css
.hero {
  background-image: url("hero.jpg");
  background-size: cover;
  background-position: center;
  position: relative;
}

.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(26, 26, 46, 0.6);
}

.hero-contenido {
  position: relative;
  z-index: 1;
}
```

**Enigma 10.4:**
```css
.suscripcion-seccion {
  background-attachment: fixed;
}
```

**Enigma 10.5:**
Respuesta libre. Ejemplos de mejoras:
1. Menú hamburguesa en móvil con animación
2. Modo oscuro con variables CSS y `prefers-color-scheme`
3. Loader de página con animación de entrada
4. Efecto de scroll reveal con `Intersection Observer` + CSS

---

**Nota:** Estas soluciones son una guía. No hay una única forma correcta de resolver los enigmas. Si tu solución funciona y tiene sentido, ¡es válida!
