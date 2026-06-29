# Capítulo 7: Más Allá del Texto

## Multimedia

---

Don Carlos llegó a la oficina con una mochila más grande de lo habitual. La dejó caer sobre la mesa con un ruido metálico.

—Encontré esto en el archivo de Don Eduardo —dijo, abriendo la mochila.

Valentina se asomó. Dentro había docenas de CDs y DVDs, cada uno etiquetado con marcador negro: "Entrevista Alcalde 2018", "Fiestas Patronales 2019", "Reportaje Artesanos 2020", "Podcast: Voces del Barrio #01".

—Don Eduardo también grababa videos y audio —dijo Don Carlos—. Quería subir todo a la web.

Valentina tomó uno de los discos. "Podcast: Voces del Barrio #01 — La historia del mercado central".

—Esto es oro puro —dijo—. Treinta años de historia en audio y video.

Pero había un problema: Valentina no sabía cómo insertar multimedia en HTML.

---

## Video: la etiqueta `<video>`

La etiqueta `<video>` permite reproducir videos directamente en la página.

```html
<video src="entrevista-alcalde.mp4" width="640" controls>
    Tu navegador no soporta el elemento de video.
</video>
```

**Atributos importantes:**

| Atributo | Descripción |
|----------|-------------|
| `src` | Ruta del archivo de video |
| `controls` | Muestra los controles de reproducción |
| `autoplay` | Reproduce automáticamente (evitar en lo posible) |
| `loop` | Repite el video en bucle |
| `muted` | Inicia sin sonido |
| `width` / `height` | Dimensiones del reproductor |
| `poster` | Imagen de portada antes de reproducir |

```html
<video controls width="640" poster="portada-entrevista.jpg">
    <source src="entrevista-alcalde.mp4" type="video/mp4">
    <source src="entrevista-alcalde.webm" type="video/webm">
    <p>Tu navegador no puede reproducir este video.</p>
</video>
```

---

## Audio: la etiqueta `<audio>`

Similar a `<video>` pero para archivos de sonido.

```html
<audio src="podcast-voces-01.mp3" controls>
    Tu navegador no soporta el elemento de audio.
</audio>
```

**Atributos:**

```html
<audio controls>
    <source src="podcast-voces-01.mp3" type="audio/mpeg">
    <source src="podcast-voces-01.ogg" type="audio/ogg">
    <p>Tu navegador no puede reproducir este audio.</p>
</audio>
```

---

## `<source>`: Múltiples formatos

Con `<source>` puedes ofrecer el mismo contenido en diferentes formatos. El navegador usará el primero que pueda reproducir.

```html
<video controls width="640">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    <source src="video.ogv" type="video/ogg">
    <p>Tu navegador no soporta videos HTML5.</p>
</video>
```

**Formatos comunes:**

| Medio | Formatos |
|-------|----------|
| Video | MP4 (H.264), WebM, OGV |
| Audio | MP3, OGG, WAV, AAC |

---

## Iframe: contenido incrustado

`<iframe>` permite incrustar contenido de otras páginas web: videos de YouTube, mapas de Google, publicaciones de redes sociales.

```html
<iframe src="https://www.youtube.com/embed/CODIGO_DEL_VIDEO" width="560" height="315" allowfullscreen>
</iframe>
```

### Cómo obtener el código de un video de YouTube

1. Abre el video en YouTube
2. Haz clic en **Compartir** > **Insertar**
3. Copia el código `<iframe>` que te dan

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="Video de YouTube" allowfullscreen>
</iframe>
```

### Incrustar un mapa de Google Maps

```html
<iframe src="https://www.google.com/maps/embed?pb=DIRECCION" width="600" height="450" allowfullscreen>
</iframe>
```

---

## La página de multimedia del periódico

Valentina creó una página para alojar los videos y podcasts del archivo:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Multimedia — La Voz del Barrio</title>
</head>
<body>

    <header>
        <h1>La Voz del Barrio</h1>
        <nav>
            <a href="index.html">Inicio</a> |
            <a href="noticias.html">Noticias</a> |
            <a href="multimedia.html">Multimedia</a> |
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>

    <hr>

    <main>
        <h2>Multimedia</h2>
        <p>Explora los videos, podcasts y galerías de nuestro archivo histórico.</p>

        <section>
            <h3>Videos destacados</h3>

            <article>
                <h4>Entrevista al Alcalde (2018)</h4>
                <video controls width="560" poster="fotos/portada-alcalde.jpg">
                    <source src="videos/entrevista-alcalde.mp4" type="video/mp4">
                    <p>Tu navegador no puede reproducir este video.</p>
                </video>
                <p><small>Grabado el 15 de junio de 2018. Duración: 12:34</small></p>
            </article>

            <article>
                <h4>Reportaje: Los últimos artesanos (2020)</h4>
                <video controls width="560">
                    <source src="videos/artesanos.mp4" type="video/mp4">
                    <p>Tu navegador no puede reproducir este video.</p>
                </video>
                <p><small>Grabado el 3 de octubre de 2020. Duración: 8:20</small></p>
            </article>
        </section>

        <hr>

        <section>
            <h3>Podcast: Voces del Barrio</h3>

            <article>
                <h4>#01 — La historia del mercado central</h4>
                <audio controls>
                    <source src="audios/podcast-01.mp3" type="audio/mpeg">
                    <p>Tu navegador no puede reproducir este audio.</p>
                </audio>
                <p><small>Publicado el 10 de enero de 2025. Duración: 25:00</small></p>
            </article>

            <article>
                <h4>#02 — Entrevista a la Sra. María, 90 años de historia</h4>
                <audio controls>
                    <source src="audios/podcast-02.mp3" type="audio/mpeg">
                    <p>Tu navegador no puede reproducir este audio.</p>
                </audio>
                <p><small>Publicado el 25 de febrero de 2025. Duración: 30:15</small></p>
            </article>
        </section>

        <hr>

        <section>
            <h3>Nuestro barrio en video</h3>

            <p>Así se veía la plaza del barrio durante las Fiestas Patronales 2025 (video de YouTube):</p>

            <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="Video de ejemplo" allowfullscreen>
            </iframe>

            <p><small>Video de muestra — reemplazar con URL real del periódico</small></p>
        </section>
    </main>

    <hr>

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

## La etiqueta `<picture>`: imágenes responsivas

`<picture>` permite ofrecer diferentes versiones de una imagen según el tamaño de pantalla o el formato soportado.

```html
<picture>
    <source srcset="foto-grande.webp" type="image/webp" media="(min-width: 800px)">
    <source srcset="foto-mediana.webp" type="image/webp" media="(min-width: 400px)">
    <source srcset="foto-grande.jpg" type="image/jpeg" media="(min-width: 800px)">
    <img src="foto-pequena.jpg" alt="Descripción de la foto">
</picture>
```

El navegador elige la primera imagen que pueda mostrar según el tamaño de la pantalla y el formato soportado.

---

## Buenas prácticas con multimedia

1. **Siempre incluye `controls`** para que el usuario controle la reproducción
2. **Evita `autoplay`** — los usuarios encuentran molestos los videos que se reproducen solos
3. **Usa `poster`** en videos para mostrar una imagen de portada
4. **Proporciona múltiples formatos** con `<source>` para compatibilidad
5. **Incluye texto alternativo** dentro de `<video>` y `<audio>` para navegadores antiguos
6. **Comprime los archivos** para que carguen rápido

---

## Enigmas del Capítulo 7

### Enigma 7.1: Tu página de videos

Crea una página HTML con:

1. Un encabezado y navegación
2. Un video local (o usa un video de prueba de internet)
3. Controles de reproducción
4. Un póster (imagen de portada)
5. Texto alternativo si el video no carga

Si no tienes un video local, puedes usar este video de muestra:
```html
<video controls width="560" poster="https://picsum.photos/560/315">
    <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
    Tu navegador no soporta video HTML5.
</video>
```

### Enigma 7.2: Tu podcast

Crea una sección de podcast con:

1. Al menos 3 episodios usando `<audio>`
2. Controles de reproducción
3. Título y descripción para cada episodio
4. Fecha de publicación usando `<time>`

Usa este audio de prueba si no tienes archivos:
```html
<audio controls>
    <source src="https://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
</audio>
```

### Enigma 7.3: Video de YouTube incrustado

Incrusta un video real de YouTube en tu página. Si no tienes uno, usa un video educativo:

1. Ve a YouTube y busca un video que te guste
2. Haz clic en Compartir > Insertar
3. Copia el código `<iframe>`
4. Pégalo en tu página HTML

### Enigma 7.4: Galería con picture

Crea una galería de al menos 3 imágenes usando `<picture>` para ofrecer diferentes tamaños. Usa el servicio https://picsum.photos para generar imágenes de diferentes dimensiones:

```html
<picture>
    <source srcset="https://picsum.photos/800/600" media="(min-width: 800px)">
    <source srcset="https://picsum.photos/400/300" media="(min-width: 400px)">
    <img src="https://picsum.photos/200/150" alt="Descripción">
</picture>
```

---

## Lo que aprendiste

- **`<video>`** reproduce videos con atributos como `controls`, `autoplay`, `poster`
- **`<audio>`** reproduce archivos de sonido
- **`<source>`** ofrece múltiples formatos para compatibilidad
- **`<iframe>`** incrusta contenido externo (YouTube, Google Maps)
- **`<picture>`** ofrece imágenes adaptativas según el tamaño de pantalla
- Siempre incluye **controles** y texto alternativo para accesibilidad

---

Don Carlos observó los videos y podcasts funcionando en la página. Tenía los ojos brillantes.

—Todo este tiempo —dijo—, Don Eduardo guardó estos tesoros. Y ahora, gracias a ti, el mundo puede verlos.

Valentina sonrió. El archivo histórico de "La Voz del Barrio" ya no estaba encerrado en CDs y DVDs. Estaba vivo en la web.

—Y esto es solo el principio —dijo—. Quiero que la gente encuentre el periódico cuando busque en Google. Para eso necesito aprender sobre SEO y meta tags.

Don Carlos asintió, todavía mirando la pantalla donde un video de 2018 mostraba a Don Eduardo entrevistando al alcalde.

—Don Eduardo —murmuró— siempre quiso ser escuchado. Ahora lo será. Por siempre.
