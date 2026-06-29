# Capítulo 8: El Código Invisible

## Meta Tags, SEO, Favicon

---

Una mañana, Valentina buscó "La Voz del Barrio" en Google. El resultado la dejó helada.

—Don Carlos —llamó—, ven a ver esto.

Don Carlos se acercó. En la pantalla, Google mostraba diez resultados. "La Voz del Barrio" no aparecía en ninguno.

—¿Dónde está nuestro periódico? —preguntó Don Carlos.

—No aparece —dijo Valentina—. Google no sabe que existimos.

Don Carlos frunció el ceño.

—Don Eduardo siempre decía: "Si no estás en Google, no existes". Pero él no alcanzó a configurar nada de esto.

Valentina respiró hondo. Había llegado el momento de aprender sobre **SEO** (Search Engine Optimization) y las meta tags que ayudan a los buscadores a encontrar y entender tu sitio web.

---

## Meta tags: información invisible

Las **meta tags** son etiquetas que van dentro del `<head>` y proporcionan información sobre la página que los usuarios no ven, pero los buscadores sí.

```html
<head>
    <meta charset="UTF-8">
    <meta name="description" content="Descripción de la página">
    <meta name="keywords" content="palabras, clave, separadas, por, comas">
    <meta name="author" content="Nombre del autor">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Voz del Barrio — Edición Digital</title>
</head>
```

### Meta tags esenciales

| Meta Tag | Propósito | Ejemplo |
|----------|-----------|---------|
| `charset` | Codificación de caracteres | `<meta charset="UTF-8">` |
| `description` | Descripción que aparece en Google | `<meta name="description" content="...">` |
| `viewport` | Adaptación a dispositivos móviles | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| `author` | Autor del sitio | `<meta name="author" content="...">` |
| `robots` | Instrucciones para buscadores | `<meta name="robots" content="index, follow">` |

---

## La meta tag `description`

Es la descripción que aparece debajo del título en los resultados de búsqueda. Debe ser atractiva y contener las palabras clave principales.

```html
<meta name="description" content="La Voz del Barrio — El periódico local de nuestro distrito desde 1991. Noticias, deportes, cultura y opinión. Tu voz en la web.">
```

**Recomendaciones:**
- Entre 150 y 160 caracteres
- Incluye palabras clave relevantes
- Debe ser única para cada página
- Debe invitar al clic

---

## La meta tag `keywords`

Antes era importante para el SEO; hoy los buscadores le dan menos peso. Pero no está de más incluirla.

```html
<meta name="keywords" content="periódico local, noticias del barrio, La Voz del Barrio, periodismo local, Lima, Perú, cultura, deportes, opinión">
```

---

## La meta tag `viewport`

**IMPORTANTE:** Sin esta meta tag, tu sitio no se verá bien en celulares.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

- `width=device-width` — el ancho de la página se adapta al ancho del dispositivo
- `initial-scale=1.0` — el zoom inicial es 1:1

---

## El título de la página `<title>`

El `<title>` es una de las cosas más importantes para el SEO. Es el título que aparece en la pestaña del navegador y en los resultados de búsqueda.

```html
<title>La Voz del Barrio — Noticias locales, cultura y más</title>
```

**Recomendaciones:**
- Entre 50 y 60 caracteres
- Incluye palabras clave principales
- Cada página debe tener un título único

---

## Meta tags para cada página

Valentina personalizó las meta tags para cada página del sitio:

### Página de inicio
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="La Voz del Barrio — El periódico local de nuestro distrito desde 1991. Noticias, deportes, cultura y opinión para toda la comunidad.">
    <meta name="keywords" content="La Voz del Barrio, periódico local, noticias del barrio, Lima, Perú">
    <title>La Voz del Barrio — Edición Digital</title>
</head>
```

### Página de noticias
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Últimas noticias del barrio. Mantente informado sobre eventos locales, anuncios municipales y la vida de nuestra comunidad.">
    <meta name="keywords" content="noticias locales, barrio, comunidad, eventos, municipalidad">
    <title>Noticias — La Voz del Barrio</title>
</head>
```

---

## Open Graph: el SEO para redes sociales

**Open Graph** son meta tags especiales que controlan cómo se ve tu página cuando se comparte en Facebook, WhatsApp, Twitter y otras redes.

```html
<meta property="og:title" content="La Voz del Barrio — Edición Digital">
<meta property="og:description" content="El periódico de nuestro barrio desde 1991. Ahora en versión digital.">
<meta property="og:image" content="https://www.lavozdelbarrio.com/imagenes/logo-facebook.jpg">
<meta property="og:url" content="https://www.lavozdelbarrio.com">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
```

| Propiedad | Descripción |
|-----------|-------------|
| `og:title` | Título para la red social |
| `og:description` | Descripción para la red social |
| `og:image` | Imagen que se muestra al compartir (1200x630 px recomendado) |
| `og:url` | URL canónica de la página |
| `og:type` | Tipo de contenido (website, article, video, etc.) |

Para Twitter, además:

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="La Voz del Barrio">
<meta name="twitter:description" content="El periódico de nuestro barrio desde 1991.">
```

---

## Favicon: el icono de la pestaña

El **favicon** es el pequeño icono que aparece en la pestaña del navegador, junto al título.

```html
<link rel="icon" href="favicon.ico" type="image/x-icon">
```

También puedes usar un icono PNG:

```html
<link rel="icon" href="favicon.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="favicon-grande.png" sizes="180x180">
```

Para crear un favicon, puedes:
1. Usar un servicio online como https://favicon.io
2. Crear una imagen cuadrada y convertirla a `.ico`
3. Usar un emoji como favicon (solo navegadores modernos)

---

## Enlazando CSS (hojas de estilo)

Aunque este libro es solo HTML, es bueno saber cómo se enlaza CSS para cuando quieras dar estilo a tus páginas:

```html
<link rel="stylesheet" href="estilos.css">
```

---

## La página de inicio optimizada para SEO

Valentina aplicó todo lo aprendido a la página principal:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="La Voz del Barrio — El periódico local de nuestro distrito desde 1991. Noticias, deportes, cultura y opinión para toda la comunidad.">
    <meta name="keywords" content="La Voz del Barrio, periódico local, noticias del barrio, periodismo local, Lima, Perú">
    <meta name="author" content="La Voz del Barrio">
    <meta name="robots" content="index, follow">

    <!-- Open Graph -->
    <meta property="og:title" content="La Voz del Barrio — Edición Digital">
    <meta property="og:description" content="El periódico de nuestro barrio desde 1991. Ahora en versión digital.">
    <meta property="og:image" content="https://www.lavozdelbarrio.com/imagenes/logo-og.jpg">
    <meta property="og:url" content="https://www.lavozdelbarrio.com">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="es_PE">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="La Voz del Barrio">
    <meta name="twitter:description" content="El periódico de nuestro barrio desde 1991.">

    <!-- Favicon -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">

    <title>La Voz del Barrio — Noticias locales, cultura y comunidad</title>
</head>
<body>
    <!-- Contenido de la página -->
    <header>
        <h1>La Voz del Barrio</h1>
        <nav>
            <a href="index.html">Inicio</a> |
            <a href="noticias.html">Noticias</a> |
            <a href="deportes.html">Deportes</a> |
            <a href="cultura.html">Cultura</a> |
            <a href="opinion.html">Opinión</a> |
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>Últimas Noticias</h2>

            <article>
                <h3><a href="noticias/plaza-remodelacion.html">La plaza del barrio será remodelada</a></h3>
                <p>La municipalidad anunció la remodelación total de la plaza principal. Las obras comenzarán en mayo.</p>
            </article>

            <article>
                <h3><a href="noticias/feria-gastronomica.html">Feria gastronómica este domingo</a></h3>
                <p>Más de 20 puestos de comida típica se darán cita en el parque central.</p>
            </article>
        </section>
    </main>

    <footer>
        <p>© 2026 La Voz del Barrio</p>
        <address>
            Contacto: <a href="mailto:contacto@lavozdelbarrio.com">contacto@lavozdelbarrio.com</a>
        </address>
    </footer>
</body>
</html>
```

---

## Validación HTML

Antes de publicar, es importante validar que tu HTML no tenga errores. El W3C (World Wide Web Consortium) ofrece un validador gratuito:

**https://validator.w3.org/**

Puedes:
1. Subir tu archivo HTML
2. Pegar la URL de tu sitio
3. Copiar y pegar el código

El validador te mostrará errores y advertencias para corregir.

---

## Enigmas del Capítulo 8

### Enigma 8.1: Optimiza tu página

Toma una página HTML que hayas creado antes (cualquier capítulo) y agrégale:

1. Meta tag de descripción (única para esa página)
2. Meta tag de viewport
3. Meta tag de keywords
4. Meta tag de autor
5. Un título (`<title>`) optimizado (entre 50-60 caracteres)

### Enigma 8.2: Open Graph

Agrega las meta tags de Open Graph a una de tus páginas:

1. `og:title`
2. `og:description`
3. `og:image` (usa la URL de una imagen de prueba)
4. `og:url`
5. `og:type`

### Enigma 8.3: Favicon

Crea un favicon para tu sitio. Puedes:

1. Dibujar un icono cuadrado simple (16x16 o 32x32 píxeles)
2. Usar un servicio online como favicon.io
3. O simplemente enlaza un favicon de prueba:

```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📰</text></svg>">
```

Este código usa un emoji como favicon.

### Enigma 8.4: Sitemap básico

Crea un archivo `sitemap.xml` simple (búscalo en internet para ver la estructura). Un sitemap ayuda a los buscadores a encontrar todas las páginas de tu sitio.

O bien, crea una página `sitemap.html` que sea un listado con enlaces a todas las páginas de tu sitio.

### Enigma 8.5: Valida tu código

Ve a https://validator.w3.org/ y pega el código de una de tus páginas. Corrige los errores que encuentres.

---

## Lo que aprendiste

- **Meta tags** van en `<head>` y dan información a los buscadores
- **`<meta charset="UTF-8">`** permite caracteres especiales
- **`<meta name="viewport">`** hace que el sitio se vea bien en celulares
- **`<meta name="description">`** es la descripción que aparece en Google
- **Open Graph** controla cómo se ve tu sitio al compartirlo en redes sociales
- **`<link rel="icon">`** agrega el favicon (icono de la pestaña)
- El **`<title>`** es crucial para el SEO
- **Validar** tu HTML con el validador del W3C ayuda a encontrar errores

---

—Ahora sí —dijo Valentina, después de agregar todas las meta tags—, Google va a encontrarnos.

Don Carlos observaba la pantalla con atención.

—¿Y cuánto tarda en aparecer en Google?

—Días o semanas —respondió Valentina—. Pero hay algo más que podemos hacer: compartir el sitio en redes sociales. Con las meta tags de Open Graph, cuando alguien comparta un enlace, se verá profesional.

Don Carlos sonrió.

—Don Eduardo siempre decía: "Lo importante no es solo estar, sino que te encuentren". Ahora entiendo lo que quería decir.

Valentina asintió. El sitio ya no era invisible. Tenía descripción, tenía título, tenía icono en la pestaña. "La Voz del Barrio" estaba lista para ser encontrada.
