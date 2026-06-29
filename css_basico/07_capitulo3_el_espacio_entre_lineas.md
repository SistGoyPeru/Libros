# Capítulo 3: El Espacio entre Líneas

*Tema: Modelo de caja (Box Model)*

---

Pasó una semana. Mateo había mejorado el estilo del sitio significativamente. Los textos se veían bien, los colores funcionaban. Pero algo no andaba bien.

—Carolina —dijo Mateo, frustrado—. No entiendo por qué mis elementos no se alinean. Pongo un `h2` y un `p` uno al lado del otro y... mira esta página.

En la pantalla, la sección "Eventos" de "Cultura Viva" mostraba una lista de tarjetas anunciando exposiciones de arte. Pero en lugar de verse ordenadas, los elementos se superponían, los espacios eran irregulares, y el diseño se sentía "apretado" o "desordenado".

Carolina sonrió.

—Bienvenido al **modelo de caja**. Es el concepto más importante de CSS para entender layouts. Una vez que lo domines, todo lo demás tendrá sentido.

## El Box Model

—Cada elemento HTML es una **caja** rectangular —dijo Carolina, dibujando en una pizarra virtual—. CSS ve el mundo como cajas dentro de cajas. Y cada caja tiene cuatro partes:

```
┌─────────────────────────────────┐
│            MARGEN               │
│  ┌───────────────────────────┐  │
│  │          BORDE            │  │
│  │  ┌─────────────────────┐  │  │
│  │  │       PADDING       │  │  │
│  │  │  ┌───────────────┐  │  │  │
│  │  │  │   CONTENIDO   │  │  │  │
│  │  │  │  (width/height)│  │  │  │
│  │  │  └───────────────┘  │  │  │
│  │  │                     │  │  │
│  │  └─────────────────────┘  │  │
│  │                           │  │
│  └───────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

—De adentro hacia afuera:

1. **Contenido** — El contenido real del elemento (texto, imagen)
2. **Padding** — Espacio interno entre el contenido y el borde
3. **Border** — El borde que rodea el padding
4. **Margin** — Espacio externo entre el borde y otros elementos

### Padding

—El **padding** es como el espacio dentro de una habitación entre los muebles y las paredes. Separa el contenido del borde.

```css
.tarjeta {
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 10px;
  padding-left: 20px;

  /* Shorthand: arriba | derecha | abajo | izquierda */
  padding: 10px 20px 10px 20px;

  /* Shorthand: vertical | horizontal */
  padding: 10px 20px;

  /* Shorthand: todos igual */
  padding: 15px;
}
```

### Margin

—El **margin** es el espacio *entre* elementos. Es como la distancia entre una casa y la siguiente.

```css
.tarjeta {
  margin-top: 20px;
  margin-bottom: 30px;

  /* Shorthand (misma lógica que padding) */
  margin: 20px auto; /* auto centra horizontalmente */
  margin: 10px 20px 30px 40px; /* arriba, derecha, abajo, izquierda */
}
```

—Un detalle importante: el **margin collapse**. Cuando dos márgenes verticales se encuentran, se fusionan en uno solo (el mayor de los dos).

```css
/* Si un h1 tiene margin-bottom: 30px */
/* y un p tiene margin-top: 20px */
/* El espacio entre ellos será 30px, no 50px */
```

### Border

—El **border** es el borde visible de la caja.

```css
.tarjeta {
  border-width: 2px;
  border-style: solid;
  border-color: #8B0000;
  border-radius: 8px;

  /* Shorthand */
  border: 2px solid #8B0000;

  /* Borde solo en un lado */
  border-bottom: 3px solid #1a1a2e;

  /* Esquinas redondeadas */
  border-radius: 10px;
  border-radius: 50%; /* círculo perfecto si es un cuadrado */
}
```

## Width y Height

—Puedes controlar el tamaño de la caja con `width` y `height`:

```css
.tarjeta {
  width: 300px;
  height: 400px;
  max-width: 100%;
  min-height: 200px;
}
```

—Pero cuidado —advirtió Carolina—: el `width` que declaras es solo el ancho del **contenido**. El ancho total del elemento es contenido + padding + border + margin.

## box-sizing: la salvación

—Aquí viene el problema que estabas teniendo —dijo Carolina—. Por defecto, CSS calcula el tamaño total como:

```
ancho total = width + padding-left + padding-right + border-left + border-right
```

—Eso significa que si declaras `width: 300px` y `padding: 20px`, el ancho real será 340px. Eso rompe los layouts.

—La solución: **`box-sizing: border-box`**:

```css
/* Solución global */
* {
  box-sizing: border-box;
}
```

—Con `border-box`, el `width` que declaras incluye el padding y el borde. El ancho real será exactamente el que declaraste. El contenido se encoge para acomodar el padding.

## Display: block, inline, inline-block

—El comportamiento de las cajas depende de su **display**:

```css
/* Ocupa todo el ancho disponible. Respeta width y height */
display: block;  /* <div>, <p>, <h1>, <section> */

/* Ocupa solo el espacio necesario. Ignora width y height */
display: inline;  /* <span>, <a>, <strong> */

/* Como inline, pero respeta width, height, margin y padding */
display: inline-block;  /* Lo mejor de ambos mundos */
```

## box-shadow

—Las sombras dan profundidad visual:

```css
.tarjeta {
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.15);
  /*    offset-x  offset-y  blur  color           */
}

/* Sombra solo en un lado */
.tarjeta {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Múltiples sombras */
.tarjeta {
  box-shadow: 0 2px 4px rgba(0,0,0,0.1), 0 4px 8px rgba(0,0,0,0.05);
}
```

## Poniendo en práctica

Mateo aplicó el modelo de caja a las tarjetas de eventos de "Cultura Viva":

```css
* {
  box-sizing: border-box;
}

.contenedor-eventos {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.tarjeta-evento {
  width: 350px;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 25px;
  margin: 15px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  display: inline-block;
  vertical-align: top;
}

.tarjeta-evento h3 {
  font-family: "Playfair Display", serif;
  color: #8B0000;
  margin-top: 0;
  border-bottom: 2px solid #eee;
  padding-bottom: 10px;
}

.tarjeta-evento p {
  line-height: 1.5;
  margin-bottom: 0;
}

.tarjeta-evento .fecha {
  display: inline-block;
  background-color: #8B0000;
  color: white;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
}
```

Mateo guardó y recargó. Las tarjetas ahora se veían ordenadas, con espacio uniforme entre ellas. Cada tarjeta era una caja limpia con bordes redondeados y sombra suave.

—Entendí —dijo Mateo—. Cada elemento es una caja. Padding es el espacio interno. Margin es el espacio externo. Y `box-sizing: border-box` hace que todo sea predecible.

—Exactamente —respondió Carolina—. El modelo de caja es la base de todo layout en CSS. Domínalo y dominarás el diseño web.

---

## Enigmas del Capítulo 3

**Enigma 3.1:** Si tienes un `div` con `width: 200px`, `padding: 15px`, `border: 3px solid black`, y `box-sizing: content-box` (valor por defecto), ¿cuál es el ancho total del elemento? ¿Y si usaras `box-sizing: border-box`?

**Enigma 3.2:** Crea una tarjeta de perfil con:
- Ancho 280px
- Padding interno de 20px
- Borde redondeado de 12px
- Sombra suave
- Margen inferior de 25px
- Color de fondo blanco

**Enigma 3.3:** ¿Qué son los márgenes colapsados? Da un ejemplo de cuándo ocurren.

**Enigma 3.4:** Escribe el CSS para un botón con:
- Color de fondo `#8B0000`
- Texto blanco, sin subrayado
- Padding: 12px arriba/abajo, 24px izquierda/derecha
- Borde: sin borde (`none`)
- Border-radius: 6px
- Al pasar el mouse, el fondo se aclara un poco

**Enigma 3.5:** Explica la diferencia entre `display: block`, `display: inline`, y `display: inline-block` con ejemplos de cuándo usar cada uno.
