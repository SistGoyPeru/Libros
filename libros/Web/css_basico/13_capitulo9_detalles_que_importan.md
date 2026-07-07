# Capítulo 9: Detalles que Importan

*Tema: Pseudo-clases y pseudo-elementos*

---

—El sitio se ve bien —dijo Carolina, recorriendo las páginas—. Pero los grandes diseñadores se distinguen en los detalles.

—¿Qué detalles? —preguntó Mateo.

—Ven. Mira esta lista de artículos. ¿Notas algo?

Mateo observó. La lista era funcional, pero carecía de los pequeños toques que hacen que un diseño se sienta pulido: los bordes de las tablas no tenían ritmo, los enlaces no daban feedback visual, no había indicadores de posición ni elementos decorativos sutiles.

—Hora de aprender sobre **pseudo-clases** y **pseudo-elementos** —dijo Carolina.

## Pseudo-clases

—Las **pseudo-clases** describen un estado especial de un elemento. Se escriben con `:` después del selector.

### :hover — El estado más usado

```css
.enlace:hover {
  color: #8B0000;
  text-decoration: underline;
}

.tarjeta:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}
```

—Se activa cuando el usuario pasa el mouse sobre el elemento.

### :focus y :active

```css
/* Cuando el elemento recibe foco (teclado o clic) */
input:focus {
  border-color: #8B0000;
  outline: 2px solid rgba(139, 0, 0, 0.3);
  box-shadow: 0 0 0 4px rgba(139, 0, 0, 0.1);
}

/* Cuando el elemento está siendo clickeado */
.boton:active {
  transform: scale(0.98);
}
```

—`:focus` es importante para accesibilidad: los usuarios de teclado necesitan ver qué elemento está activo.

### :nth-child() — Selectores posicionales

```css
/* El tercer hijo de su padre */
li:nth-child(3) {
  font-weight: bold;
}

/* Los hijos pares */
li:nth-child(even) {
  background-color: #f9f9f9;
}

/* Los hijos impares */
li:nth-child(odd) {
  background-color: white;
}

/* Cada 3 elementos, empezando por el 2 */
li:nth-child(3n+2) {
  color: #8B0000;
}
```

Carolina mostró una tabla con ejemplos:

| Selector | Selecciona |
|----------|-----------|
| `:first-child` | El primer hijo |
| `:last-child` | El último hijo |
| `:nth-child(2)` | El segundo hijo |
| `:nth-child(odd)` | Hijos en posición impar |
| `:nth-child(even)` | Hijos en posición par |
| `:nth-child(3n)` | Cada 3 elementos |
| `:nth-last-child(2)` | El segundo desde el final |

### :not() — La negación

```css
/* Todos los párrafos excepto los de clase .intro */
p:not(.intro) {
  color: #555;
}

/* Todos los elementos excepto el último */
li:not(:last-child) {
  border-bottom: 1px solid #eee;
}
```

## Pseudo-elementos

—Los **pseudo-elementos** crean elementos "fantasma" que no existen en el HTML. Se escriben con `::` (doble dos puntos).

### ::before y ::after

—Los más poderosos. Insertan contenido antes o después de un elemento.

```css
/* Agregar una comilla decorativa antes de las citas */
blockquote::before {
  content: "\201C";  /* Comilla doble izquierda Unicode */
  font-size: 60px;
  color: #8B0000;
  font-family: Georgia, serif;
  position: absolute;
  top: -10px;
  left: -10px;
}

/* Agregar un icono de enlace externo */
a[target="_blank"]::after {
  content: " ↗";
  font-size: 12px;
}

/* Decoración de listas personalizadas */
.lista-articulos li::before {
  content: "◆";
  color: #8B0000;
  margin-right: 10px;
}
```

—`::before` crea un elemento como primer hijo. `::after` lo crea como último hijo. Ambos requieren la propiedad `content` para existir.

### ::first-line y ::first-letter

```css
/* Primera línea del párrafo */
p::first-line {
  font-weight: bold;
  color: #333;
}

/* Primera letra (capital) */
.articulo p::first-letter {
  font-size: 48px;
  font-weight: 900;
  color: #8B0000;
  float: left;
  margin-right: 8px;
  line-height: 1;
  font-family: "Playfair Display", serif;
}
```

—Esto crea un efecto de **capitular** (letra capital) como en los libros antiguos.

## Detalles que marcan la diferencia en "Cultura Viva"

Mateo aplicó pseudo-clases y pseudo-elementos en todo el sitio:

```css
/* === Tabla de eventos con filas alternadas === */
.tabla-eventos tr:nth-child(even) {
  background-color: #f9f5f0;
}

.tabla-eventos tr:hover {
  background-color: #f0e8dd;
}

.tabla-eventos td {
  padding: 12px 15px;
  border-bottom: 1px solid #e0d6cc;
}

.tabla-eventos tr:last-child td {
  border-bottom: none;
}

/* === Estilo de listas con indicador visual === */
.lista-categorias li {
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

.lista-categorias li:last-child {
  border-bottom: none;
}

.lista-categorias li::before {
  content: "▸";
  color: #8B0000;
  margin-right: 10px;
  font-weight: bold;
}

/* === Enlaces con feedback visual === */
.enlace-articulo {
  color: #1a1a2e;
  text-decoration: none;
  transition: color 0.2s ease;
  position: relative;
}

.enlace-articulo:hover {
  color: #8B0000;
}

/* Línea decorativa que aparece al hacer hover */
.enlace-articulo::after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #8B0000;
  transition: width 0.3s ease;
}

.enlace-articulo:hover::after {
  width: 100%;
}

/* === Capital inicial en artículos destacados === */
.articulo-destacado p:first-of-type::first-letter {
  font-size: 3em;
  font-weight: 900;
  color: #8B0000;
  float: left;
  margin-right: 10px;
  margin-top: 5px;
  line-height: 0.8;
  font-family: "Playfair Display", serif;
}

/* === Tooltips con CSS === */
[data-tooltip] {
  position: relative;
  cursor: help;
}

[data-tooltip]:hover::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background-color: #333;
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 12px;
  white-space: nowrap;
  z-index: 100;
}

/* === Formulario de suscripción === */
.campo-formulario {
  border: 2px solid #ddd;
  border-radius: 6px;
  padding: 12px 15px;
  font-size: 16px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.campo-formulario:focus {
  border-color: #8B0000;
  outline: none;
  box-shadow: 0 0 0 3px rgba(139, 0, 0, 0.1);
}

.campo-formulario:invalid {
  border-color: #e74c3c;
}

.campo-formulario:valid {
  border-color: #27ae60;
}

/* === Mensajes de error con pseudo-clase === */
.error-mensaje {
  display: none;
  color: #e74c3c;
  font-size: 13px;
  margin-top: 5px;
}

.campo-formulario:invalid ~ .error-mensaje {
  display: block;
}
```

—Fíjate —dijo Carolina— cómo usamos `::after` para crear la línea decorativa que crece bajo los enlaces. No hay un solo elemento extra en el HTML. Todo el detalle visual está en el CSS.

Mateo observó el resultado. Los pequeños detalles transformaban la experiencia: las filas de la tabla se leían con facilidad, los enlaces tenían una animación sutil, los formularios daban feedback visual, las listas tenían indicadores elegantes.

—Los detalles no son detalles —dijo Mateo, recordando una frase que había leído en algún lado—. Los detalles son el diseño.

—Exactamente —sonrió Carolina—. Ahora entiendes.

---

## Enigmas del Capítulo 9

**Enigma 9.1:** Usando `::before`, agrega un icono de estrella (★) antes de cada elemento de una lista con clase `.destacados`.

**Enigma 9.2:** Crea un efecto de "línea que crece" (underline animation) para los enlaces del menú de navegación usando `::after` y `transition`.

**Enigma 9.3:** Usando `:nth-child`, haz que en una galería de 6 imágenes, la tercera y la sexta tengan un borde de color diferente (por ejemplo, dorado).

**Enigma 9.4:** Diseña un efecto de "tooltip" (información emergente) usando `::after` y el atributo `data-tooltip`. El tooltip debe aparecer al hacer hover y desvanecerse suavemente.

**Enigma 9.5:** Explica la diferencia entre pseudo-clases (`:hover`) y pseudo-elementos (`::before`). Da dos ejemplos de cada uno.
