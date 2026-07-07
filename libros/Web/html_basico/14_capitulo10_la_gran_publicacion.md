# Capítulo 10: La Gran Publicación

## Proyecto Final: Armar Todo el Sitio

---

Pasaron tres meses desde aquel primer día en que Valentina abrió el archivo index.html de Don Eduardo sin saber ni por dónde empezar. Ahora, el sitio web de "La Voz del Barrio" no solo existía: estaba completo.

Los artículos estaban escritos. Las fotos de Don Carlos brillaban en la galería. Los formularios de suscripción funcionaban. El sitio era accesible, tenía meta tags para SEO, y el favicon del periódico —una pequeña V dentro de un círculo— aparecía en la pestaña del navegador.

Pero Valentina quería dar un paso más. Quería crear la **página principal definitiva**: un sitio que integrara todo lo aprendido, que fuera la puerta de entrada digital a "La Voz del Barrio".

—Voy a crear el sitio final —le anunció a Don Carlos—. El sitio que Don Eduardo siempre soñó.

Don Carlos se sentó a su lado, y los dos aprendices que habían estado ayudando en la oficina se acercaron también. Era el momento de poner todo junto.

---

## El proyecto integrador: Sitio web de "La Voz del Barrio"

Valentina abrió su editor. El proyecto tenía esta estructura de carpetas:

```
lavozdelbarrio/
│
├── index.html
├── sobre-nosotros.html
├── contacto.html
├── suscripcion.html
├── multimedia.html
├── favicon.ico
│
├── secciones/
│   ├── noticias.html
│   ├── deportes.html
│   ├── cultura.html
│   └── opinion.html
│
├── fotos/
│   ├── logo.png
│   ├── plaza.jpg
│   ├── redaccion.jpg
│   └── ...
│
├── videos/
│   ├── entrevista-alcalde.mp4
│   └── artesanos.mp4
│
└── audios/
    ├── podcast-01.mp3
    └── podcast-02.mp3
```

---

## index.html — La página principal completa

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="La Voz del Barrio — El periódico local de nuestro distrito desde 1991. Noticias, deportes, cultura y opinión para toda la comunidad.">
    <meta name="keywords" content="La Voz del Barrio, periódico local, noticias del barrio, periodismo local, Lima, Perú">
    <meta name="author" content="La Voz del Barrio">

    <meta property="og:title" content="La Voz del Barrio — Edición Digital">
    <meta property="og:description" content="El periódico de nuestro barrio desde 1991. Ahora en versión digital.">
    <meta property="og:image" content="https://www.lavozdelbarrio.com/fotos/logo-og.jpg">
    <meta property="og:url" content="https://www.lavozdelbarrio.com">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="es_PE">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="La Voz del Barrio">

    <link rel="icon" href="favicon.ico" type="image/x-icon">

    <title>La Voz del Barrio — Noticias locales, cultura y comunidad</title>
</head>
<body>

    <!-- Skip link para accesibilidad -->
    <a href="#contenido-principal" style="position:absolute;left:-9999px;top:0;">Saltar al contenido principal</a>

    <header role="banner">
        <h1>La Voz del Barrio</h1>
        <p><em>El periódico de nuestro barrio desde 1991</em></p>

        <nav role="navigation" aria-label="Navegación principal">
            <a href="index.html">Inicio</a> |
            <a href="secciones/noticias.html">Noticias</a> |
            <a href="secciones/deportes.html">Deportes</a> |
            <a href="secciones/cultura.html">Cultura</a> |
            <a href="secciones/opinion.html">Opinión</a> |
            <a href="multimedia.html">Multimedia</a> |
            <a href="sobre-nosotros.html">Nosotros</a> |
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>

    <hr>

    <main id="contenido-principal">

        <!-- Sección de bienvenida -->
        <section aria-label="Bienvenida">
            <h2>Bienvenidos a la Edición Digital</h2>
            <p>Después de <strong>35 años</strong> llevando las noticias del barrio en papel, <em>La Voz del Barrio</em> llega a internet. Aquí encontrarás las mismas historias de siempre, pero ahora al alcance de un clic.</p>

            <figure>
                <img src="fotos/redaccion.jpg" alt="La redacción de La Voz del Barrio en 1995, con Don Eduardo escribiendo en su máquina de escribir" width="600">
                <figcaption>La redacción del periódico en 1995. Don Eduardo al centro.</figcaption>
            </figure>
        </section>

        <hr>

        <!-- Sección de últimas noticias -->
        <section aria-label="Últimas noticias">
            <h2>Últimas Noticias</h2>

            <article>
                <h3><a href="secciones/noticias.html">La plaza del barrio será remodelada</a></h3>
                <p><time datetime="2026-03-20">20 de marzo de 2026</time> — La municipalidad anunció la <strong>remodelación total</strong> de la plaza principal. Las obras comenzarán en mayo y durarán aproximadamente 6 meses.</p>
            </article>

            <article>
                <h3><a href="secciones/noticias.html">Feria gastronómica: 20 puestos confirmados</a></h3>
                <p><time datetime="2026-03-18">18 de marzo de 2026</time> — La feria gastronómica del barrio contará con <em>más de 20 puestos</em> de comida típica peruana. Se espera una asistencia récord.</p>

                <figure>
                    <img src="fotos/feria.jpg" alt="Puestos de comida en la feria gastronómica del año pasado, con gente haciendo cola" width="400">
                    <figcaption>La feria del año anterior fue todo un éxito.</figcaption>
                </figure>
            </article>

            <article>
                <h3><a href="secciones/deportes.html">Club de barrio celebra 50 años</a></h3>
                <p><time datetime="2026-03-15">15 de marzo de 2026</time> — El Club Deportivo Local cumple medio siglo de fundación. Habrá eventos especiales durante todo el mes.</p>
            </article>
        </section>

        <hr>

        <!-- Sección de próximos eventos -->
        <section aria-label="Próximos eventos">
            <h2>Próximos Eventos</h2>

            <table>
                <caption>Calendario de eventos del barrio — Abril 2026</caption>
                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Evento</th>
                        <th>Lugar</th>
                        <th>Hora</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><time datetime="2026-04-12">12 abril</time></td>
                        <td>Feria gastronómica</td>
                        <td>Plaza principal</td>
                        <td>10:00 am</td>
                    </tr>
                    <tr>
                        <td><time datetime="2026-04-20">20 abril</time></td>
                        <td>Torneo de fútbol interbarrial</td>
                        <td>Estadio Municipal</td>
                        <td>9:00 am</td>
                    </tr>
                    <tr>
                        <td><time datetime="2026-04-27">27 abril</time></td>
                        <td>Taller de periodismo ciudadano</td>
                        <td>Biblioteca del barrio</td>
                        <td>4:00 pm</td>
                    </tr>
                    <tr>
                        <td><time datetime="2026-05-01">1 mayo</time></td>
                        <td>Aniversario de La Voz del Barrio</td>
                        <td>Oficina del periódico</td>
                        <td>11:00 am</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <hr>

        <!-- Sección multimedia -->
        <section aria-label="Multimedia destacada">
            <h2>Multimedia Destacada</h2>

            <article>
                <h3>Podcast: Voces del Barrio #01</h3>
                <p>La historia del mercado central de nuestro barrio, contada por sus propios comerciantes.</p>
                <audio controls aria-label="Reproducir podcast Voces del Barrio">
                    <source src="audios/podcast-01.mp3" type="audio/mpeg">
                    <p>Tu navegador no puede reproducir este audio.</p>
                </audio>
                <p><small>Duración: 25:00 — Publicado el <time datetime="2025-01-10">10 de enero de 2025</time></small></p>
            </article>
        </section>

        <hr>

        <!-- Sección de suscripción -->
        <section aria-label="Suscripción al periódico">
            <h2>Suscríbete</h2>
            <p>Recibe el periódico en tu correo o en tu casa. Tenemos planes para todos.</p>

            <table>
                <caption>Planes de suscripción</caption>
                <thead>
                    <tr>
                        <th>Plan</th>
                        <th>Precio</th>
                        <th>Incluye</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Digital Básico</strong></td>
                        <td>S/ 15.00/mes</td>
                        <td>Acceso web + newsletter semanal</td>
                    </tr>
                    <tr>
                        <td><strong>Digital Premium</strong></td>
                        <td>S/ 40.00/trimestre</td>
                        <td>Web + newsletter + archivo histórico</td>
                    </tr>
                    <tr>
                        <td><strong>Anual Completo</strong></td>
                        <td>S/ 150.00/año</td>
                        <td>Todo incluido (ahorra 20%)</td>
                    </tr>
                </tbody>
            </table>

            <p><a href="suscripcion.html">Formulario de suscripción →</a></p>
        </section>

    </main>

    <hr>

    <!-- Barra lateral -->
    <aside aria-label="Anuncios y enlaces útiles">
        <h3>Anuncios del Barrio</h3>
        <ul>
            <li><strong>Panadería El Trigal</strong> — Pan artesanal. Jr. Las Flores 123.</li>
            <li><strong>Farmacia del Barrio</strong> — Descuentos para vecinos. Jr. La Merced 789.</li>
            <li><strong>Taller Mecánico Don José</strong> — Revisión técnica gratuita. Av. Talleres 456.</li>
        </ul>
        <p><a href="contacto.html">Publicita tu negocio aquí</a></p>
    </aside>

    <hr>

    <footer role="contentinfo">
        <p>© 2026 La Voz del Barrio — Fundado por Don Eduardo Zapata (1991)</p>
        <address aria-label="Información de contacto">
            <p><strong>La Voz del Barrio</strong></p>
            <p>Jr. Los Periodistas 456, Lima, Perú</p>
            <p>Correo: <a href="mailto:contacto@lavozdelbarrio.com">contacto@lavozdelbarrio.com</a></p>
            <p>Teléfono: <a href="tel:+5115550400">(01) 555-0400</a></p>
        </address>
        <p><small>Este sitio web fue construido en memoria de Don Eduardo Zapata, periodista y soñador.</small></p>
    </footer>

</body>
</html>
```

---

## Las otras páginas del sitio

Valentina también creó las páginas restantes siguiendo el mismo estilo. Cada una debía tener:

1. **Mismo header y footer** (navegación consistente)
2. **Meta tags únicas** para cada página
3. **HTML semántico** (header, nav, main, section, article, footer)
4. **Atributos de accesibilidad** (alt, aria-label, lang)
5. **Contenido relevante** del periódico

---

## El momento de la verdad

Valentina reunió a Don Carlos y al pequeño equipo frente a la computadora.

—Señores —dijo, con el nerviosismo de quien va a presentar algo importante—, les presento el sitio web de <strong>La Voz del Barrio</strong>.

Hizo clic en el archivo index.html. El navegador mostró la página completa: el encabezado con el nombre del periódico, la navegación, las noticias, la tabla de eventos, el reproductor de audio, la tabla de suscripciones y el pie de página.

Don Carlos silbó suavemente.

—Esto es... enorme —dijo—. Don Eduardo estaría saltando de alegría.

—Pero lo más importante —dijo Valentina— es que todo funciona junto. Los enlaces conectan las páginas. Las imágenes tienen descripciones. Los formularios están listos para recibir datos. Y cuando Google nos encuentre, la descripción será la correcta.

Valentina abrió la página "Sobre Nosotros" y leyó en voz alta el texto que había escrito:

*"La Voz del Barrio nació en 1991, fundada por el periodista Eduardo Zapata. Durante más de tres décadas, hemos cubierto cada terremoto, cada elección, cada campeonato de fútbol y cada fiesta patronal. Hemos denunciado injusticias, celebrado logros y, sobre todo, dado voz a quienes no la tienen."*

—Eso es exactamente lo que Don Eduardo quería —dijo Don Carlos, con la voz entrecortada.

---

## El cierre del círculo

Esa noche, después de que todos se fueron, Valentina se quedó sola en la oficina. La luz de la luna se filtraba por las ventanas, iluminando los periódicos antiguos en las paredes.

Abrió la computadora de Don Eduardo. En el escritorio, junto a los archivos del sitio web, había una carpeta llamada "Proyecto". Valentina la abrió.

Dentro encontró un archivo de texto llamado "nota_para_valentina.txt". Lo abrió.

*"Valentina:*

*Si estás leyendo esto, significa que encontraste el proyecto y decidiste terminarlo. Sabía que lo harías.*

*No sé si mi sitio web será bonito. No sé si las etiquetas estarán bien puestas. Pero sé una cosa: la voz del barrio merece ser escuchada. Y tú tienes el talento para hacer que eso suceda.*

*Gracias por tomar la posta.*

*— Don Eduardo"*

Valentina sintió que los ojos se le llenaban de lágrimas. Don Eduardo había confiado en ella desde el principio.

Tomó su laptop y, en el archivo index.html, agregó una línea al footer:

```html
<p><small>Este sitio web fue construido en memoria de Don Eduardo Zapata, periodista y soñador.</small></p>
```

Guardó el archivo. Apagó la computadora. Y al salir de la oficina, miró el letrero que Don Eduardo había pintado treinta y cinco años atrás:

**LA VOZ DEL BARRIO**
*El periódico de todos desde 1991*

—La voz sigue viva, Don Eduardo —dijo en voz baja—. Y ahora llega más lejos que nunca.

---

## Enigmas del Capítulo 10

### Enigma 10.1: Crea tu propio sitio web completo

Ahora es tu turno. Crea un sitio web completo (mínimo 4 páginas HTML) sobre un tema que te guste. Puede ser:

- Un blog personal
- El sitio de un negocio ficticio
- Una página de homenaje a alguien
- Un sitio sobre tu hobby favorito

**Requisitos mínimos:**

1. **Página principal** (`index.html`) con:
   - Header con navegación
   - Main con al menos 3 secciones
   - Footer con información de contacto
   - Al menos una imagen con `alt` descriptivo
   - Al menos un enlace a otra página del sitio

2. **Página "Sobre Nosotros"** con:
   - Historia o descripción del sitio
   - Una imagen
   - Una lista (ordenada o desordenada)

3. **Página de contacto** con:
   - Formulario con mínimo 4 campos
   - Label para cada campo
   - Fieldset y legend
   - Botón de enviar

4. **Página de contenido** (artículos, productos, etc.) con:
   - Al menos 2 artículos
   - Tabla con datos
   - Una lista

5. **Todas las páginas deben tener:**
   - Meta tags (description, viewport)
   - HTML semántico (header, nav, main, section, footer)
   - Atributos de accesibilidad (alt, aria-label donde corresponda)
   - Título único en cada página

### Enigma 10.2: Multimedia

Agrega a tu sitio al menos uno de estos elementos:

1. Un video (puede ser de YouTube en iframe)
2. Un audio (puede ser de prueba)
3. Una galería de imágenes con figure y figcaption

### Enigma 10.3: Accesibilidad

Audita tu sitio y asegúrate de que:

1. Todas las imágenes tienen `alt`
2. Todos los formularios tienen `label`
3. El `lang` está definido en `<html>`
4. Hay un enlace de salto (skip link) al contenido principal
5. Los botones e iconos tienen `aria-label` cuando sea necesario

### Enigma 10.4: El mensaje final

Así como Valentina encontró el mensaje de Don Eduardo, crea una página llamada `mensaje.html` con una carta o mensaje inspirador para alguien que herede tu proyecto. Usa HTML semántico y formato adecuado.

---

## Lo que aprendiste en este libro

| Concepto | Capítulo | Aplicación en "La Voz del Barrio" |
|----------|----------|-----------------------------------|
| Estructura HTML | Cap 1 | La base de toda página web |
| Texto y listas | Cap 2 | Artículos del periódico |
| Enlaces e imágenes | Cap 3 | Conectar páginas y mostrar fotos |
| Tablas | Cap 4 | Horarios, tarifas y directorios |
| Formularios | Cap 5 | Suscripciones y contacto |
| HTML Semántico | Cap 6 | Dar significado al contenido |
| Multimedia | Cap 7 | Videos y podcasts del barrio |
| Meta tags y SEO | Cap 8 | Posicionamiento en buscadores |
| Accesibilidad | Cap 9 | Un sitio para todos los lectores |
| Proyecto integrador | Cap 10 | Sitio web completo del periódico |
