# Capítulo 6: El Significado de las Cosas

## HTML Semántico

---

Una tarde, mientras Valentina revisaba el código que Don Eduardo había dejado, notó algo curioso. Todas las páginas usaban la misma estructura:

```html
<div class="header">
    <div class="nav">
        <!-- enlaces -->
    </div>
</div>
<div class="main">
    <div class="article">
        <!-- contenido -->
    </div>
</div>
<div class="footer">
    <!-- pie de página -->
</div>
```

—Don Eduardo solo usaba `<div>` —dijo Valentina, pensativa.

Don Carlos, que estaba organizando fotos, levantó la vista.

—¿Y eso es malo?

—No es malo —respondió Valentina—. Pero Don Eduardo no sabía que HTML tiene etiquetas especiales para cada parte de la página.

—¿Como cuáles?

—Como `<header>`, `<nav>`, `<main>`, `<footer>`. Etiquetas que le dicen al navegador y a los buscadores qué significa cada parte.

Valentina había descubierto el **HTML semántico**: usar etiquetas que describen el significado del contenido, no solo su apariencia.

---

## ¿Qué es HTML semántico?

**HTML semántico** significa usar etiquetas que describen el **propósito** del contenido, no solo cómo se ve.

| Etiqueta | Significado | ¿Para qué sirve? |
|----------|-------------|------------------|
| `<header>` | Encabezado | Parte superior de una página o sección |
| `<nav>` | Navegación | Menú de navegación |
| `<main>` | Contenido principal | El contenido central de la página |
| `<section>` | Sección | Una sección temática |
| `<article>` | Artículo | Contenido independiente y reutilizable |
| `<aside>` | Lateral | Contenido complementario (sidebar) |
| `<footer>` | Pie de página | Pie de una página o sección |
| `<figure>` | Figura | Imagen con pie de foto |
| `<figcaption>` | Pie de figura | Descripción de la figura |
| `<time>` | Fecha/hora | Fechas y horas legibles por máquina |
| `<address>` | Dirección | Información de contacto |

---

## Reestructurando el sitio del periódico

Valentina decidió reescribir la página principal usando HTML semántico.

### Antes (con divs):

```html
<div class="header">
    <h1>La Voz del Barrio</h1>
    <div class="nav">
        <a href="index.html">Inicio</a>
        <a href="noticias.html">Noticias</a>
    </div>
</div>
<div class="main">
    <div class="article">
        <h2>Noticia del día</h2>
        <p>Contenido...</p>
    </div>
</div>
<div class="footer">
    <p>© 2026 La Voz del Barrio</p>
</div>
```

### Después (con etiquetas semánticas):

```html
<header>
    <h1>La Voz del Barrio</h1>
    <nav>
        <a href="index.html">Inicio</a>
        <a href="noticias.html">Noticias</a>
        <a href="deportes.html">Deportes</a>
        <a href="cultura.html">Cultura</a>
        <a href="opinion.html">Opinión</a>
        <a href="contacto.html">Contacto</a>
    </nav>
</header>

<main>
    <section>
        <h2>Últimas Noticias</h2>

        <article>
            <h3>La plaza del barrio será remodelada</h3>
            <p>Publicado el <time datetime="2026-03-20">20 de marzo de 2026</time></p>
            <p>La municipalidad anunció la remodelación total de la plaza principal...</p>
        </article>

        <article>
            <h3>Feria gastronómica este domingo</h3>
            <p>Publicado el <time datetime="2026-03-18">18 de marzo de 2026</time></p>
            <p>Más de 20 puestos de comida típica se darán cita en el parque central...</p>
        </article>
    </section>

    <aside>
        <h3>Anuncios</h3>
        <p>¿Quieres publicitar tu negocio? <a href="contacto.html">Contáctanos</a></p>

        <h3>Suscripción</h3>
        <p>Recibe el periódico en tu correo. <a href="suscripcion.html">Suscríbete</a></p>
    </aside>
</main>

<footer>
    <p>© 2026 La Voz del Barrio — Fundado por Don Eduardo Zapata</p>
    <address>
        Dirección: Jr. Los Periodistas 456, Lima<br>
        Correo: contacto@lavozdelbarrio.com<br>
        Teléfono: 555-0400
    </address>
</footer>
```

—Se ve igual —observó Don Carlos, comparando las dos versiones en el navegador.

—Visualmente es igual —dijo Valentina—. Pero para los buscadores y los lectores de pantalla, la diferencia es enorme. Ahora el navegador sabe que esto es un artículo, esto es navegación, esto es el pie de página.

---

## `<figure>` y `<figcaption>`: Fotos con descripción

```html
<figure>
    <img src="fotos/plaza_remodelacion.jpg" alt="Maqueta de la nueva plaza del barrio" width="600">
    <figcaption>La nueva plaza incluirá áreas verdes, juegos infantiles y una pérgola para eventos.</figcaption>
</figure>
```

---

## `<time>`: Fechas legibles por máquinas

```html
<p>El evento se realizará el <time datetime="2026-04-12">12 de abril de 2026</time>.</p>
<p>La reunión comienza a las <time datetime="19:00">7:00 pm</time>.</p>
<p>Publicado el <time datetime="2026-03-20T10:30:00-05:00">20 de marzo de 2026 a las 10:30 am</time>.</p>
```

El atributo `datetime` usa el formato estándar ISO 8601, que los buscadores y calendarios pueden interpretar automáticamente.

---

## `<address>`: Información de contacto

```html
<footer>
    <address>
        <p><strong>La Voz del Barrio</strong></p>
        <p>Jr. Los Periodistas 456, Lima, Perú</p>
        <p>Teléfono: <a href="tel:+5115550400">(01) 555-0400</a></p>
        <p>Correo: <a href="mailto:contacto@lavozdelbarrio.com">contacto@lavozdelbarrio.com</a></p>
    </address>
</footer>
```

---

## Página completa con HTML semántico

Valentina reescribió la página de inicio completa:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>La Voz del Barrio — Edición Digital</title>
</head>
<body>

    <header>
        <h1>La Voz del Barrio</h1>
        <p><em>El periódico de nuestro barrio desde 1991</em></p>

        <nav>
            <a href="index.html">Inicio</a> |
            <a href="noticias.html">Noticias</a> |
            <a href="deportes.html">Deportes</a> |
            <a href="cultura.html">Cultura</a> |
            <a href="opinion.html">Opinión</a> |
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>

    <hr>

    <main>

        <section>
            <h2>Últimas Noticias</h2>

            <article>
                <h3>La plaza del barrio será remodelada</h3>
                <p><time datetime="2026-03-20">20 de marzo de 2026</time> — La municipalidad anunció la <strong>remodelación total</strong> de la plaza principal. Las obras comenzarán en mayo.</p>

                <figure>
                    <img src="fotos/plaza_actual.jpg" alt="Estado actual de la plaza del barrio" width="400">
                    <figcaption>La plaza necesita una renovación urgente, según los vecinos.</figcaption>
                </figure>
            </article>

            <article>
                <h3>Feria gastronómica: 20 puestos confirmados</h3>
                <p><time datetime="2026-03-18">18 de marzo de 2026</time> — La feria gastronómica del barrio contará con <em>más de 20 puestos</em> de comida típica peruana.</p>
            </article>

            <article>
                <h3>Club de barrio celebra 50 años</h3>
                <p><time datetime="2026-03-15">15 de marzo de 2026</time> — El Club Deportivo Local cumple medio siglo de fundación. Habrá eventos especiales todo el mes.</p>
            </article>
        </section>

        <hr>

        <section>
            <h2>Próximos Eventos</h2>
            <ol>
                <li><time datetime="2026-04-12">12 de abril</time> — Feria gastronómica en la plaza</li>
                <li><time datetime="2026-04-20">20 de abril</time> — Torneo de fútbol interbarrial</li>
                <li><time datetime="2026-05-01">1 de mayo</time> — Aniversario del periódico</li>
            </ol>
        </section>

    </main>

    <aside>
        <h3>Anuncios</h3>
        <p><strong>Panadería El Trigal</strong> — Pan artesanal todos los días. Jr. Las Flores 123.</p>
        <p><strong>Farmacia del Barrio</strong> — Descuentos para vecinos. Jr. La Merced 789.</p>
        <p><a href="contacto.html">Publicita aquí tu negocio</a></p>
    </aside>

    <hr>

    <footer>
        <p>© 2026 La Voz del Barrio</p>
        <address>
            Contacto: <a href="mailto:contacto@lavozdelbarrio.com">contacto@lavozdelbarrio.com</a><br>
            Dirección: Jr. Los Periodistas 456, Lima<br>
            Teléfono: <a href="tel:+5115550400">(01) 555-0400</a>
        </address>
        <p><small>Fundado por Don Eduardo Zapata — 1991</small></p>
    </footer>

</body>
</html>
```

---

## Beneficios del HTML semántico

| Beneficio | Explicación |
|-----------|-------------|
| **SEO** | Los buscadores entienden mejor tu contenido |
| **Accesibilidad** | Los lectores de pantalla navegan mejor |
| **Legibilidad** | El código es más fácil de entender y mantener |
| **Estandarización** | Sigue las mejores prácticas de la web |

---

## Enigmas del Capítulo 6

### Enigma 6.1: Identifica las etiquetas semánticas

Toma una página HTML que hayas creado antes y reescríbela usando al menos 6 etiquetas semánticas diferentes: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<figure>`, `<figcaption>` o `<time>`.

### Enigma 6.2: Blog personal

Crea la estructura de un blog personal con HTML semántico que incluya:

1. `<header>` con el nombre del blog y `<nav>` con enlaces
2. `<main>` con al menos 2 `<article>` (cada uno con `<time>`)
3. `<aside>` con información del autor
4. `<footer>` con datos de contacto usando `<address>`
5. `<figure>` con una imagen y `<figcaption>`

### Enigma 6.3: Comparación div vs semántico

Escribe el mismo contenido dos veces:

1. **Versión 1:** Usando solo `<div>` (como Don Eduardo)
2. **Versión 2:** Usando etiquetas semánticas

¿Cuál es más fácil de leer? ¿Cuál crees que los buscadores entienden mejor?

### Enigma 6.4: La página del artículo

Don Eduardo escribió un artículo de opinión. Estructúralo con HTML semántico:

- `<header>` con el título del artículo y la fecha (`<time>`)
- `<main>` con el contenido del artículo (mínimo 3 párrafos)
- `<figure>` con una foto y `<figcaption>`
- `<footer>` con el nombre del autor
- `<address>` con información de contacto

---

## Lo que aprendiste

- **HTML semántico** usa etiquetas que describen el significado del contenido
- **`<header>`** — encabezado de página o sección
- **`<nav>`** — navegación principal
- **`<main>`** — contenido principal (solo uno por página)
- **`<section>`** — agrupa contenido temático
- **`<article>`** — contenido independiente (noticia, post, comentario)
- **`<aside>`** — contenido complementario
- **`<footer>`** — pie de página o sección
- **`<figure>`** y **`<figcaption>`** — imágenes con descripción
- **`<time>`** — fechas y horas en formato estándar
- **`<address>`** — información de contacto
- El HTML semántico mejora **SEO**, **accesibilidad** y **mantenibilidad**

---

—Ahora entiendo por qué Don Eduardo usaba tantos divs —dijo Valentina—. Porque no sabía que existían estas etiquetas. Es como tener todas las herramientas en una sola caja, sin saber que cada una tiene su lugar.

Don Carlos asintió, observando el código.

—Don Eduardo siempre decía: "Lo importante no es cómo se ve, sino lo que significa". Nunca supe que aplicaba también al código.

Valentina sonrió. El sitio de "La Voz del Barrio" no solo se veía bien. Ahora también significaba algo.
