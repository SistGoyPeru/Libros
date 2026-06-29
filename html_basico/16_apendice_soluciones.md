# Apéndice: Soluciones a los Enigmas

### Capítulo 1: El Desafío de la Web

**Enigma 1.1:**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Primer Sitio</title>
</head>
<body>
    <!-- Página creada en 2026 -->
    <h1>Bienvenidos</h1>
    <hr>
    <p>Soy [tu nombre] y estoy aprendiendo HTML.</p>
    <p>Este es mi primer sitio web creado con el libro HTML Básico.</p>
</body>
</html>
```

**Enigma 1.2:**
El mensaje de Don Eduardo decía: *"Valentina: si estás leyendo esto, es porque encontraste el camino. El periódico necesita una voz digital. Tú puedes ser esa voz. Revisa la carpeta 'proyecto' para más archivos. — Don Eduardo"*

**Enigma 1.3:**
Errores corregidos:
- `<h1>La Voz del Barrio<h1>` → `<h1>La Voz del Barrio</h1>` (la etiqueta de cierre tenía h1 en lugar de /h1)
- `<p><strong>Edición digital</p></strong>` → `<p><strong>Edición digital</strong></p>` (anidamiento incorrecto: la etiqueta strong debe cerrarse antes que p)

Código corregido:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>La Voz del Barrio</title>
</head>
<body>
    <h1>La Voz del Barrio</h1>
    <p>El periódico del barrio desde 1991.</p>
    <p><strong>Edición digital</strong></p>
</body>
</html>
```

**Enigma 1.4:**
Al hacer clic derecho > "Inspeccionar" o "Ver código fuente", verás el mismo HTML que escribiste, pero el navegador puede haberlo interpretado y mostrado en el árbol DOM. La pestaña "Elements" muestra cómo el navegador entiende tu código.

---

### Capítulo 2: Las Primeras Palabras

**Enigma 2.1:**
Ejemplo de artículo HTML:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Artículo</title>
</head>
<body>
    <h1>El Título de mi Artículo</h1>
    <hr>
    <h2>Introducción</h2>
    <p>Este es el primer párrafo de mi artículo. Aquí <strong>presento</strong> el tema del que voy a hablar.</p>
    <h2>Desarrollo</h2>
    <p>En este segundo párrafo, <em>desarrollo</em> las ideas principales. Es importante dar detalles relevantes.</p>
    <h2>Conclusión</h2>
    <p>Finalmente, cierro el artículo con una reflexión personal.</p>
    <hr>
    <p><small>Escrito por [tu nombre] — 2026</small></p>
</body>
</html>
```

**Enigma 2.2:**

```html
<h2>Pendientes del sitio web</h2>
<ol>
    <li>Terminar página principal</li>
    <li>Subir galería de fotos</li>
    <li>Configurar formulario de contacto</li>
    <li>Publicar archivo histórico</li>
    <li>Agregar mapa del barrio</li>
</ol>

<h2>Secciones de mi interés</h2>
<ul>
    <li>Noticias</li>
    <li>Cultura</li>
    <li>Deportes</li>
</ul>
```

**Enigma 2.3:**
Jerarquía correcta:

```html
<h1>La Voz del Barrio</h1>
<h2>Edición Digital</h2>
<h3>Noticias Locales</h3>
<h4>La plaza del barrio</h4>
```

Los headings deben seguir una jerarquía sin saltos: h1 → h2 → h3 → h4, no h1 → h4 → h2 → h5.

**Enigma 2.4:**

```html
<blockquote>
    <p>"El periodismo local no es pequeño: es íntimo. No habla de todos, habla de ti."</p>
    <footer>— Don Eduardo Zapata</footer>
</blockquote>
```

---

### Capítulo 3: El Mapa del Sitio

**Enigma 3.1:**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mapa del Sitio</title>
</head>
<body>
    <h1>Mapa del Sitio</h1>
    <ul>
        <li><a href="index.html">Página principal</a></li>
        <li><a href="articulos.html">Artículos</a></li>
        <li><a href="galeria.html">Galería</a></li>
        <li><a href="contacto.html">Contacto</a></li>
        <li><a href="https://www.bbc.com/mundo" target="_blank">Noticias externas</a></li>
    </ul>
</body>
</html>
```

**Enigma 3.3:**

```html
<nav>
    <a href="#seccion1">Ir a Sección 1</a>
    <a href="#seccion2">Ir a Sección 2</a>
    <a href="#seccion3">Ir a Sección 3</a>
</nav>

<h2 id="seccion1">Sección 1</h2>
<p>Contenido de la sección 1...</p>
<p>Más contenido...</p>
<p>Más contenido...</p>

<h2 id="seccion2">Sección 2</h2>
<p>Contenido de la sección 2...</p>
<p>Más contenido...</p>
<p>Más contenido...</p>

<h2 id="seccion3">Sección 3</h2>
<p>Contenido de la sección 3...</p>
<p>Más contenido...</p>
<p>Más contenido...</p>
```

**Enigma 3.4:**
`%20` es el código URL-encoded para un espacio. En las URLs no se permiten espacios, por lo que se reemplazan con `%20`. El enlace completo se vería así:

```html
<a href="mailto:lectores@lavozdelbarrio.com?subject=Carta%20al%20director">
    Enviar carta al director
</a>
```

---

### Capítulo 4: Organizando la Información

**Enigma 4.1:**
Ejemplo de horario semanal:

```html
<table>
    <caption>Mi Horario Semanal</caption>
    <tr>
        <th>Hora</th>
        <th>Lunes</th>
        <th>Martes</th>
        <th>Miércoles</th>
        <th>Jueves</th>
        <th>Viernes</th>
    </tr>
    <tr>
        <td>8:00 - 9:00</td>
        <td>Desayuno</td>
        <td>Desayuno</td>
        <td>Desayuno</td>
        <td>Desayuno</td>
        <td>Desayuno</td>
    </tr>
    <tr>
        <td>9:00 - 12:00</td>
        <td>Trabajo</td>
        <td>Trabajo</td>
        <td>Trabajo</td>
        <td>Trabajo</td>
        <td>Trabajo</td>
    </tr>
    <tr>
        <td>12:00 - 13:00</td>
        <td colspan="5">Almuerzo</td>
    </tr>
    <tr>
        <td>15:00 - 17:00</td>
        <td>Estudio</td>
        <td>Estudio</td>
        <td>Gimnasio</td>
        <td>Estudio</td>
        <td>Gimnasio</td>
    </tr>
</table>
```

**Enigma 4.3:**

```html
<table>
    <tr>
        <th>DÍA</th>
        <th>MAÑANA</th>
        <th>TARDE</th>
    </tr>
    <tr>
        <td>Lunes a Viernes</td>
        <td>9:00 - 12:00</td>
        <td>2:00 - 6:00</td>
    </tr>
    <tr>
        <td>Sábado</td>
        <td colspan="2">9:00 - 1:00</td>
    </tr>
    <tr>
        <td>Domingo</td>
        <td colspan="2">Cerrado</td>
    </tr>
</table>
```

---

### Capítulo 5: La Voz del Barrio

**Enigma 5.1:**

```html
<form action="#" method="post">
    <fieldset>
        <legend>Datos del lector</legend>
        <p>
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
        </p>
        <p>
            <label for="edad">Edad:</label>
            <input type="number" id="edad" name="edad" min="1" max="120">
        </p>
        <p>
            <label for="email">Correo:</label>
            <input type="email" id="email" name="email" required>
        </p>
    </fieldset>

    <fieldset>
        <legend>Frecuencia de lectura</legend>
        <p>
            <input type="radio" id="diario" name="frecuencia" value="diario">
            <label for="diario">Diario</label>
        </p>
        <p>
            <input type="radio" id="semanal" name="frecuencia" value="semanal">
            <label for="semanal">Semanal</label>
        </p>
        <p>
            <input type="radio" id="mensual" name="frecuencia" value="mensual">
            <label for="mensual">Mensual</label>
        </p>
        <p>
            <input type="radio" id="ocasional" name="frecuencia" value="ocasional">
            <label for="ocasional">Ocasional</label>
        </p>
    </fieldset>

    <fieldset>
        <legend>Sección favorita</legend>
        <label for="seccion">Selecciona:</label>
        <select id="seccion" name="seccion">
            <option value="noticias">Noticias</option>
            <option value="deportes">Deportes</option>
            <option value="cultura">Cultura</option>
            <option value="opinion">Opinión</option>
        </select>
    </fieldset>

    <fieldset>
        <legend>Temas de interés</legend>
        <p><input type="checkbox" id="tema1" name="interes" value="educacion"> <label for="tema1">Educación</label></p>
        <p><input type="checkbox" id="tema2" name="interes" value="salud"> <label for="tema2">Salud</label></p>
        <p><input type="checkbox" id="tema3" name="interes" value="seguridad"> <label for="tema3">Seguridad</label></p>
        <p><input type="checkbox" id="tema4" name="interes" value="medioambiente"> <label for="tema4">Medio ambiente</label></p>
    </fieldset>

    <p>
        <label for="comentarios">Comentarios:</label>
        <textarea id="comentarios" name="comentarios" rows="4"></textarea>
    </p>

    <p><input type="submit" value="Enviar encuesta"></p>
</form>
```

**Enigma 5.4:**
Ejemplo con input types especiales:

```html
<p>
    <label for="fecha">Fecha de nacimiento:</label>
    <input type="date" id="fecha" name="fecha">
</p>
<p>
    <label for="color_favorito">Color favorito:</label>
    <input type="color" id="color_favorito" name="color_favorito">
</p>
<p>
    <label for="volumen">Volumen de notificaciones:</label>
    <input type="range" id="volumen" name="volumen" min="0" max="10">
</p>
<p>
    <label for="sitio_web">Tu sitio web:</label>
    <input type="url" id="sitio_web" name="sitio_web" placeholder="https://ejemplo.com">
</p>
```

---

### Capítulo 6: El Significado de las Cosas

**Enigma 6.2:**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Blog Personal</title>
</head>
<body>
    <header>
        <h1>Mi Blog</h1>
        <nav>
            <a href="index.html">Inicio</a> |
            <a href="sobre-mi.html">Sobre mí</a> |
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>

    <main>
        <article>
            <h2>Aprendiendo HTML</h2>
            <p><time datetime="2026-03-20">20 de marzo de 2026</time></p>
            <p>Hoy aprendí sobre HTML semántico...</p>
        </article>

        <article>
            <h2>Mi primer sitio web</h2>
            <p><time datetime="2026-03-18">18 de marzo de 2026</time></p>
            <p>Después de semanas de estudio, finalmente...</p>
        </article>
    </main>

    <aside>
        <h3>Sobre el autor</h3>
        <figure>
            <img src="fotos/autor.jpg" alt="Foto del autor del blog" width="150">
            <figcaption>El autor del blog</figcaption>
        </figure>
        <p>Soy un estudiante de desarrollo web.</p>
    </aside>

    <footer>
        <address>
            Contacto: <a href="mailto:autor@ejemplo.com">autor@ejemplo.com</a>
        </address>
        <p><small>© 2026 Mi Blog</small></p>
    </footer>
</body>
</html>
```

---

### Capítulo 7: Más Allá del Texto

**Enigma 7.1:**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página de Videos</title>
</head>
<body>
    <header>
        <h1>Mis Videos Favoritos</h1>
    </header>

    <main>
        <h2>Video de ejemplo</h2>
        <video controls width="560" poster="https://picsum.photos/560/315">
            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
            <p>Tu navegador no soporta video HTML5.</p>
        </video>
    </main>
</body>
</html>
```

**Enigma 7.2:**

```html
<section>
    <h2>Podcast: Voces del Barrio</h2>

    <article>
        <h3>Episodio 1: La historia del mercado</h3>
        <p><time datetime="2025-01-10">10 de enero de 2025</time></p>
        <audio controls>
            <source src="https://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
        </audio>
    </article>

    <article>
        <h3>Episodio 2: Entrevista a la Sra. María</h3>
        <p><time datetime="2025-02-25">25 de febrero de 2025</time></p>
        <audio controls>
            <source src="https://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
        </audio>
    </article>

    <article>
        <h3>Episodio 3: El club de barrio</h3>
        <p><time datetime="2025-03-15">15 de marzo de 2025</time></p>
        <audio controls>
            <source src="https://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
        </audio>
    </article>
</section>
```

---

### Capítulo 8: El Código Invisible

**Enigma 8.1:**
Ejemplo de página optimizada:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Artículos y tutoriales sobre desarrollo web para principiantes. Aprende HTML, CSS y JavaScript desde cero.">
    <meta name="keywords" content="desarrollo web, HTML, CSS, JavaScript, tutoriales, principiantes">
    <meta name="author" content="Tu Nombre">
    <title>Aprende Desarrollo Web — Tutoriales para principiantes</title>
</head>
<body>
    <h1>Bienvenido a mi sitio de tutoriales</h1>
    <!-- resto del contenido -->
</body>
</html>
```

**Enigma 8.2:**

```html
<meta property="og:title" content="Aprende Desarrollo Web — Tutoriales">
<meta property="og:description" content="Tutoriales gratuitos de HTML, CSS y JavaScript para principiantes.">
<meta property="og:image" content="https://tusitio.com/imagen-og.jpg">
<meta property="og:url" content="https://tusitio.com">
<meta property="og:type" content="website">
```

**Enigma 8.3:**
Favicon con emoji:

```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🌐</text></svg>">
```

**Enigma 8.4:**
Sitemap en HTML:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mapa del Sitio</title>
</head>
<body>
    <h1>Mapa del Sitio</h1>
    <ul>
        <li><a href="index.html">Inicio</a></li>
        <li><a href="sobre-mi.html">Sobre mí</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="contacto.html">Contacto</a></li>
    </ul>
</body>
</html>
```

---

### Capítulo 9: Para Todos

**Enigma 9.2:**
Textos alt descriptivos:

1. `alt="Plaza del barrio decorada con banderines de colores durante el festival anual, con un escenario al fondo y familias paseando"`
2. `alt="Logo de La Voz del Barrio con el nombre del periódico en tipografía serif y una V estilizada como símbolo"`
3. `alt="Don Eduardo Zapata sentado frente a su máquina de escribir, con una sonrisa y un fondo de periódicos antiguos"`
4. `alt="Gráfico de barras que muestra el crecimiento de lectores de 500 en 2020 a 2000 en 2026"`

**Enigma 9.3:**

```html
<form action="#" method="post">
    <p>
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" placeholder="Nombre">
    </p>
    <p>
        <label for="correo">Correo:</label>
        <input type="email" id="correo" name="correo" placeholder="Correo">
    </p>
    <p>
        <input type="checkbox" id="terminos" name="terminos">
        <label for="terminos">Acepto los términos y condiciones</label>
    </p>
    <p>
        <button type="submit" aria-label="Enviar formulario">Enviar</button>
    </p>
</form>
```

---

### Capítulo 10: La Gran Publicación

**Enigma 10.1:**
No hay una única solución para el proyecto integrador. Tu sitio debe incluir:

- Mínimo 4 páginas HTML enlazadas entre sí
- HTML semántico (header, nav, main, section, footer)
- Meta tags para SEO
- Formulario con label y fieldset
- Tabla con datos
- Imágenes con alt descriptivo
- Al menos un elemento multimedia (video, audio o iframe)
- Atributos de accesibilidad (aria-label, lang, skip link)

**Enigma 10.4:**
Ejemplo de página de mensaje:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mensaje para el Futuro</title>
</head>
<body>
    <header>
        <h1>Mensaje para quien herede este proyecto</h1>
    </header>

    <main>
        <p><time datetime="2026-06-29">29 de junio de 2026</time></p>

        <p>Querida persona que está leyendo esto:</p>

        <p>Si has llegado hasta aquí, es porque has heredado este proyecto. No sé quién eres ni en qué circunstancias lo encontraste, pero quiero que sepas algo importante:</p>

        <p><strong>Este sitio fue construido con esfuerzo, dedicación y mucho aprendizaje.</strong> Cada línea de código representa horas de estudio, errores corregidos y lecciones aprendidas.</p>

        <p>No tengas miedo de modificar, mejorar o incluso rehacer lo que encuentres aquí. La web está viva y evoluciona constantemente. Lo importante no es el código en sí, sino lo que construyes con él.</p>

        <p>Sigue aprendiendo. Sigue creando. Y recuerda: <em>cada etiqueta que escribes es un ladrillo en la construcción de la web.</em></p>

        <p>— [Tu nombre]</p>
    </main>

    <footer>
        <p><small>© 2026 — El legado continúa</small></p>
    </footer>
</body>
</html>
```

---

**Nota:** Estas soluciones son una guía. No hay una única forma correcta de resolver los enigmas. Si tu solución funciona y tiene sentido, ¡es válida!
