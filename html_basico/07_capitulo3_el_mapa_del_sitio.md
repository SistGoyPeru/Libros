# Capítulo 3: El Mapa del Sitio

## Enlaces e Imágenes

---

Don Carlos llegó a la oficina con una caja de cartón bajo el brazo. La puso sobre la mesa con cuidado, como si contuviera algo frágil.

—Esto es lo que Don Eduardo guardaba —dijo, abriendo la caja.

Valentina se asomó. La caja estaba llena de sobres de papel manila, cada uno etiquetado con una fecha y un título: "Festival del Barrio 2025", "Campaña de Vacunación", "Entrevista al Alcalde", "Aniversario del Club Deportivo".

—¿Fotos? —preguntó Valentina.

—Fotos y documentos —respondió Don Carlos—. Treinta años de historia del barrio. Don Eduardo quería que todo esto estuviera en la web.

Valentina sacó un sobre al azar. Contenía fotos de la plaza del barrio durante las fiestas patronales. Gente bailando, niños con globos, puestos de comida. Había vida en esas imágenes.

—Necesito aprender a poner imágenes en HTML —dijo—. Y también necesito conectar las páginas entre sí. El sitio debe tener navegación.

Don Carlos asintió.

—Tu abuelo... digo, Don Eduardo, siempre decía que un periódico sin fotos es como un día sin sol.

Valentina sonrió. Abrió la computadora y empezó a investigar.

---

## Enlaces: la etiqueta `<a>`

Los enlaces son lo que hace que la web sea "web". Sin enlaces, cada página sería una isla. Los enlaces se crean con la etiqueta `<a>` (anchor — ancla).

```html
<a href="https://www.ejemplo.com">Texto del enlace</a>
```

El atributo `href` (hypertext reference) define la dirección a la que apunta el enlace.

### Rutas absolutas vs. relativas

**Rutas absolutas:** URL completa, incluyendo `https://`.

```html
<a href="https://www.google.com">Ir a Google</a>
```

**Rutas relativas:** Dirección dentro de tu propio sitio.

```html
<a href="contacto.html">Contáctanos</a>
<a href="secciones/noticias.html">Noticias</a>
```

### El atributo `target`

Controla dónde se abre el enlace.

```html
<a href="https://www.ejemplo.com" target="_blank">Abrir en nueva pestaña</a>
<a href="contacto.html" target="_self">Abrir en la misma pestaña (predeterminado)</a>
```

| Valor | Comportamiento |
|-------|----------------|
| `_self` | Abre en la misma pestaña (por defecto) |
| `_blank` | Abre en una nueva pestaña |

### Enlaces internos (anclas)

Para navegar dentro de la misma página:

```html
<a href="#seccion-deportes">Ir a Deportes</a>

<!-- Más abajo en la página... -->
<h2 id="seccion-deportes">Sección Deportes</h2>
```

### Enlaces de correo

```html
<a href="mailto:contacto@lavozdelbarrio.com">Enviar correo</a>
```

---

## Creando la navegación del sitio

Valentina creó la barra de navegación del periódico:

```html
<h1>La Voz del Barrio</h1>
<nav>
    <a href="index.html">Inicio</a> |
    <a href="noticias.html">Noticias</a> |
    <a href="deportes.html">Deportes</a> |
    <a href="cultura.html">Cultura</a> |
    <a href="opinion.html">Opinión</a> |
    <a href="contacto.html">Contacto</a>
</nav>
```

—Cada una de estas será una página —explicó Valentina—. Por ahora, todas apuntan a archivos que aún no existen. Pero ya tenemos el mapa del sitio.

---

## Imágenes: la etiqueta `<img>`

Las imágenes se insertan con la etiqueta `<img>`. Es una etiqueta **vacía** (no tiene cierre).

```html
<img src="foto.jpg" alt="Descripción de la foto">
```

### Atributos obligatorios

- **`src`** (source): la ruta de la imagen
- **`alt`** (alternative text): descripción textual de la imagen (importante para accesibilidad y SEO)

### Atributos opcionales útiles

```html
<img src="foto.jpg" alt="Plaza del barrio en fiestas" width="600" height="400" title="Fiestas Patronales 2025">
```

- **`width`** y **`height`**: definen el tamaño en píxeles
- **`title`**: texto que aparece al pasar el ratón sobre la imagen

### Formatos de imagen para web

| Formato | Cuándo usarlo |
|---------|---------------|
| **JPG/JPEG** | Fotos y imágenes con muchos colores |
| **PNG** | Imágenes con transparencia o texto |
| **GIF** | Animaciones simples |
| **SVG** | Iconos, logotipos, gráficos vectoriales |
| **WebP** | Formato moderno, mejor compresión |

---

## La galería de fotos del periódico

Don Carlos tenía las fotos organizadas por año. Valentina creó una galería simple:

```html
<h2>Galería: Fiestas Patronales 2025</h2>

<img src="fotos/fiesta01.jpg" alt="Plaza del barrio decorada para las fiestas patronales" width="300">
<img src="fotos/fiesta02.jpg" alt="Niños bailando en la plaza" width="300">
<img src="fotos/fiesta03.jpg" alt="Puestos de comida típica" width="300">
<img src="fotos/fiesta04.jpg" alt="Orquesta tocando en el escenario" width="300">
```

—Se ven muy pequeñas —observó Don Carlos.

—Puedo hacerlas más grandes —respondió Valentina—. Pero también puedo hacer que al hacer clic se vean completas.

### Imagen como enlace

Puedes combinar `<a>` e `<img>` para hacer que una imagen sea un enlace:

```html
<a href="fotos/fiesta01_grande.jpg" target="_blank">
    <img src="fotos/fiesta01.jpg" alt="Plaza del barrio decorada" width="300">
</a>
```

---

## La página "Sobre Nosotros"

Valentina creó una página que contaba la historia del periódico:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Sobre Nosotros — La Voz del Barrio</title>
</head>
<body>

    <h1>La Voz del Barrio</h1>
    <nav>
        <a href="index.html">Inicio</a> |
        <a href="noticias.html">Noticias</a> |
        <a href="deportes.html">Deportes</a> |
        <a href="cultura.html">Cultura</a> |
        <a href="opinion.html">Opinión</a> |
        <a href="contacto.html">Contacto</a>
    </nav>

    <hr>

    <h2>Sobre Nosotros</h2>

    <img src="fotos/redaccion.jpg" alt="La redacción de La Voz del Barrio en 1995" width="600">

    <p><strong>La Voz del Barrio</strong> nació en 1991, fundada por el periodista <strong>Eduardo Zapata</strong>. Lo que comenzó como un boletín de una página repartido en las tiendas del barrio, se convirtió en el semanario local más querido del distrito.</p>

    <p>Durante más de tres décadas, hemos cubierto cada terremoto, cada elección, cada campeonato de fútbol y cada fiesta patronal. Hemos denunciado injusticias, celebrado logros y, sobre todo, <em>dado voz a quienes no la tienen</em>.</p>

    <p>Hoy, damos el salto al mundo digital sin olvidar nuestras raíces. Porque la voz del barrio <strong>merece ser escuchada en todas partes</strong>.</p>

    <hr>

    <h3>Nuestro equipo</h3>
    <ul>
        <li><strong>Eduardo Zapata</strong> — Fundador y director (Q.E.P.D.)</li>
        <li><strong>Carlos Mendoza</strong> — Fotografía y archivo</li>
        <li><strong>Valentina Rivas</strong> — Diseño y desarrollo web</li>
    </ul>

    <hr>

    <p><a href="index.html">Volver al inicio</a></p>

    <p><small>© 2026 La Voz del Barrio</small></p>

</body>
</html>
```

—Esto ya parece un sitio web de verdad —dijo Don Carlos, observando la pantalla—. Don Eduardo estaría orgulloso.

Valentina sonrió. Pero sabía que aún faltaba mucho.

---

## Rutas de archivos

Un concepto importante que Valentina aprendió fue cómo organizar las rutas de los archivos.

### Estructura de carpetas

```
lavozdelbarrio/
│
├── index.html
├── sobre-nosotros.html
├── contacto.html
│
├── secciones/
│   ├── noticias.html
│   ├── deportes.html
│   ├── cultura.html
│   └── opinion.html
│
└── fotos/
    ├── redaccion.jpg
    ├── fiesta01.jpg
    ├── fiesta02.jpg
    └── ...
```

### Referenciar archivos desde diferentes niveles

**Desde la raíz a una subcarpeta:**
```html
<img src="fotos/fiesta01.jpg" alt="...">
<a href="secciones/noticias.html">Noticias</a>
```

**Desde una subcarpeta a la raíz:**
```html
<img src="../fotos/fiesta01.jpg" alt="...">
<a href="../index.html">Inicio</a>
```

El prefijo `../` significa "sube un nivel de carpeta".

---

## Enigmas del Capítulo 3

### Enigma 3.1: El mapa del sitio

Crea un archivo HTML llamado `mapa_sitio.html` que contenga enlaces a:

1. Tu página principal (`index.html`)
2. Una página de artículos (`articulos.html`)
3. Una página de galería (`galeria.html`)
4. Una página de contacto (`contacto.html`)
5. Un enlace externo a un sitio de noticias real

Usa `target="_blank"` para el enlace externo.

### Enigma 3.2: Tu galería personal

Crea una galería de 4 imágenes sobre un tema que te guste. Usa imágenes de prueba (puedes usar el servicio <a href="https://picsum.photos" target="_blank">https://picsum.photos</a> para generar imágenes aleatorias).

Cada imagen debe:
- Tener un atributo `alt` descriptivo
- Tener un ancho de 250 píxeles
- Ser un enlace a la imagen en tamaño grande

```html
<a href="https://picsum.photos/800/600" target="_blank">
    <img src="https://picsum.photos/250/200" alt="Descripción" width="250">
</a>
```

### Enigma 3.3: Navegación con anclas

Crea una página larga con tres secciones (mínimo 3 párrafos cada una). Al inicio de la página, crea enlaces que lleven directamente a cada sección usando el atributo `id`.

```html
<nav>
    <a href="#seccion1">Sección 1</a>
    <a href="#seccion2">Sección 2</a>
    <a href="#seccion3">Sección 3</a>
</nav>

<h2 id="seccion1">Sección 1</h2>
<p>Contenido...</p>
```

### Enigma 3.4: Correo del lector

Don Eduardo recibía muchas cartas de lectores. Crea un enlace de correo electrónico que abra el cliente de correo con un asunto predefinido:

```html
<a href="mailto:lectores@lavozdelbarrio.com?subject=Carta%20al%20director">
    Enviar carta al director
</a>
```

Investiga: ¿qué significa `%20` en esa URL?

---

## Lo que aprendiste

- Los **enlaces** se crean con `<a href="...">`
- Las **rutas absolutas** son URL completas; las **relativas** son rutas dentro del sitio
- **`target="_blank"`** abre el enlace en una nueva pestaña
- Las **anclas** (`#id`) permiten navegar dentro de la misma página
- Las **imágenes** se insertan con `<img src="..." alt="...">`
- El atributo **`alt`** es obligatorio y describe la imagen
- Puedes combinar `<a>` e `<img>` para hacer imágenes cliqueables
- **`../`** sube un nivel en la estructura de carpetas

---

Valentina guardó todos los archivos y organizó las carpetas del proyecto. El sitio comenzaba a tomar forma. Tenía página principal, páginas de contenido, navegación entre ellas y fotos de la historia del barrio.

—Don Carlos —dijo—, mañana vamos a organizar datos. Tablas, horarios, tarifas. El periódico necesita mostrar información de manera ordenada.

Don Carlos asintió, revisando las fotos que Valentina había subido.

—Se parecen mucho a las que tomó Don Eduardo —dijo, con los ojos brillantes—. Él siempre decía que una foto bien tomada vale más que mil palabras. Pero una foto en la web... esa vale millones.
