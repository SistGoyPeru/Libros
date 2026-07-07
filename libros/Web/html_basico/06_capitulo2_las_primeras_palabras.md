# Capítulo 2: Las Primeras Palabras

## Headings, Párrafos, Formato de Texto, Listas

---

Eran las ocho de la mañana cuando Valentina llegó a la oficina del periódico. El sol de Lima se filtraba por las persianas, iluminando el polvo que flotaba sobre los montones de periódicos viejos.

Don Carlos ya estaba allí, revisando fotos en su computadora.

—Buenos días, Valentina —dijo sin levantar la vista—. Anoche encontré algo que Don Eduardo quería publicar en la web.

Le mostró un cuaderno de pasta azul. En la primera página, escrito con letra firme:

*"Artículos pendientes para la web:*
1. *Editorial: ¿Qué significa tener voz en el siglo XXI?*
2. *Noticia: La plaza del barrio será remodelada*
3. *Reportaje: Los últimos artesanos del distrito*
4. *Opinión: La educación pública en crisis*
5. *Deportes: El club de barrio cumple 50 años"*

—Don Eduardo escribió estos artículos —dijo Don Carlos—, pero no alcanzó a pasarlos a la web.

Valentina abrió la computadora. Necesitaba aprender a escribir contenido en HTML. No solo párrafos, sino títulos, subtítulos, listas, énfasis. Todo lo que un artículo periodístico necesita.

---

## Headings: los títulos en HTML

Los **headings** o encabezados se usan para definir títulos y subtítulos. Van de `<h1>` (el más importante) a `<h6>` (el menos importante).

```html
<h1>Título principal del sitio</h1>
<h2>Título de sección</h2>
<h3>Subtítulo de sección</h3>
<h4>Encabezado de cuarto nivel</h4>
<h5>Encabezado de quinto nivel</h5>
<h6>Encabezado de sexto nivel</h6>
```

**Reglas importantes:**
- Solo debe haber un `<h1>` por página (es el título principal)
- Los headings crean una jerarquía: no saltes de h1 a h4 sin usar h2 y h3 antes
- Los buscadores usan los headings para entender la estructura de tu contenido

Valentina empezó a escribir la página de inicio del periódico:

```html
<h1>La Voz del Barrio</h1>
<h2>Edición Digital</h2>
<h3>Artículos de la Semana</h3>
```

—Cada número es como un nivel en un esquema —pensó—. H1 es el título del periódico, H2 es la sección, H3 es el artículo.

---

## Párrafos: la etiqueta `<p>`

Los párrafos se escriben con la etiqueta `<p>`. Cada párrafo es un bloque de texto separado.

```html
<p>Este es un párrafo de texto. El navegador lo mostrará como un bloque separado de otros elementos.</p>
<p>Este es otro párrafo. Automáticamente tendrá un espacio arriba y abajo.</p>
```

**Importante:** en HTML, los saltos de línea en el código no se muestran en el navegador. Si escribes:

```html
<p>
    Este texto está
    en varias líneas
    en el código
</p>
```

El navegador lo mostrará como: "Este texto está en varias líneas en el código"

Para forzar un salto de línea dentro de un párrafo, usa `<br>`:

```html
<p>Primera línea<br>Segunda línea</p>
```

---

## Formato de texto: énfasis e importancia

Valentina recordó que en los artículos de Don Eduardo, ciertas palabras debían resaltarse. En HTML, el formato se hace con etiquetas que dan **significado** al texto.

### `<strong>` — Importancia (generalmente se ve en negrita)

```html
<p>Este es un <strong>texto muy importante</strong> que debe resaltarse.</p>
```

### `<em>` — Énfasis (generalmente se ve en cursiva)

```html
<p>Ella <em>realmente</em> quería ayudar al periódico.</p>
```

### `<b>` y `<i>` — Alternativas visuales

Aunque existen `<b>` para negrita y `<i>` para cursiva, se recomienda usar `<strong>` y `<em>` porque tienen **significado semántico** (no solo visual). Los lectores de pantalla los interpretan de manera diferente.

### `<mark>` — Texto resaltado

```html
<p>El plazo para <mark>entregar los artículos</mark> vence el viernes.</p>
```

### `<small>` — Texto secundario

```html
<p><small>© 2026 La Voz del Barrio. Todos los derechos reservados.</small></p>
```

### `<blockquote>` — Citas largas

```html
<blockquote>
    <p>"El periodismo local es el alma de la democracia. Sin él, las historias de nuestra gente se pierden en el ruido del mundo."</p>
    <footer>— Don Eduardo Zapata</footer>
</blockquote>
```

---

## Escribiendo el primer artículo

Valentina decidió escribir el editorial de Don Eduardo. Así quedó su código:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Editorial — La Voz del Barrio</title>
</head>
<body>
    <h1>La Voz del Barrio</h1>
    <h2>Editorial</h2>
    <h3>¿Qué significa tener voz en el siglo XXI?</h3>

    <p>Por <strong>Don Eduardo Zapata</strong></p>

    <p>En un mundo donde las redes sociales amplifican cualquier opinión, <em>¿qué valor tiene un periódico local?</em> Mucho, diríamos nosotros. Porque no es lo mismo hablarle al mundo que hablarle a tu vecino.</p>

    <p>Este periódico nació en 1991, en una época donde el internet era un lujo y la información viajaba en papel. Hoy, <strong>35 años después</strong>, damos el salto al mundo digital. No para abandonar el papel, sino para abrazar el futuro.</p>

    <p>La voz del barrio sigue viva. Y ahora, llega más lejos que nunca.</p>

    <hr>

    <p><small>Publicado originalmente el 15 de marzo de 2026</small></p>
</body>
</html>
```

—Don Eduardo escribía muy bien —dijo Valentina, mostrándole el resultado a Don Carlos.

—Era un periodista de los de antes —respondió Don Carlos—. Los que creen que las palabras pueden cambiar el mundo.

---

## Listas: ordenando la información

Valentina necesitaba listar las secciones del periódico y los próximos eventos del barrio. Para eso estaban las listas.

### Listas desordenadas `<ul>`

Se usan cuando el orden de los elementos **no importa**. Cada elemento va dentro de `<li>` (list item).

```html
<h3>Secciones del periódico</h3>
<ul>
    <li>Noticias</li>
    <li>Deportes</li>
    <li>Cultura</li>
    <li>Opinión</li>
    <li>Servicios</li>
</ul>
```

### Listas ordenadas `<ol>`

Se usan cuando el orden **sí importa**. Los elementos se numeran automáticamente.

```html
<h3>Pasos para suscribirse</h3>
<ol>
    <li>Completa el formulario de contacto</li>
    <li>Elige tu plan de suscripción</li>
    <li>Realiza el pago</li>
    <li>Recibe el periódico en tu correo</li>
</ol>
```

### Anidando listas

Las listas pueden contener otras listas:

```html
<h3>Horarios de entrega</h3>
<ul>
    <li>Zona Norte
        <ul>
            <li>Lunes y jueves: 8:00 am</li>
            <li>Sábado: 10:00 am</li>
        </ul>
    </li>
    <li>Zona Sur
        <ul>
            <li>Martes y viernes: 8:00 am</li>
            <li>Sábado: 10:00 am</li>
        </ul>
    </li>
</ul>
```

---

## La primera página del periódico

Valentina combinó todo lo aprendido y creó la página principal del periódico:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>La Voz del Barrio — Edición Digital</title>
</head>
<body>
    <h1>La Voz del Barrio</h1>
    <p><em>El periódico de nuestro barrio desde 1991</em></p>
    <hr>

    <h2>Últimas Noticias</h2>

    <h3>La plaza del barrio será remodelada</h3>
    <p>La municipalidad anunció la <strong>remodelación total</strong> de la plaza principal. Las obras comenzarán en mayo y durarán aproximadamente 6 meses.</p>

    <h3>Los últimos artesanos del distrito</h3>
    <p>Un reportaje sobre los talleres artesanales que aún sobreviven en el barrio. <em>Una tradición que se niega a morir.</em></p>

    <hr>

    <h2>Secciones</h2>
    <ul>
        <li><strong>Noticias:</strong> Todo lo que pasa en el barrio</li>
        <li><strong>Deportes:</strong> El club local y sus logros</li>
        <li><strong>Cultura:</strong> Eventos, arte y tradiciones</li>
        <li><strong>Opinión:</strong> Editoriales y cartas de lectores</li>
    </ul>

    <hr>

    <h2>Próximos Eventos</h2>
    <ol>
        <li>Feria gastronómica — 12 de abril</li>
        <li>Torneo de fútbol interbarrial — 20 de abril</li>
        <li>Aniversario del periódico — 1 de mayo</li>
    </ol>

    <hr>

    <p><small>© 2026 La Voz del Barrio — Fundado por Don Eduardo Zapata</small></p>
</body>
</html>
```

Valentina guardó el archivo y lo abrió en el navegador. La página se veía simple pero ordenada. Tenía estructura. Tenía jerarquía visual.

—No está mal para ser mi primer día —sonrió.

---

## Enigmas del Capítulo 2

### Enigma 2.1: Tu primer artículo

Escribe un artículo HTML sobre un tema que te guste. Debe incluir:

1. Un título principal (`<h1>`)
2. Al menos dos subtítulos (`<h2>`)
3. Mínimo 3 párrafos (`<p>`)
4. Una palabra en **negrita** y una en *cursiva*
5. Una línea horizontal (`<hr>`) entre secciones
6. Un pie de página con texto pequeño (`<small>`)

### Enigma 2.2: Lista de pendientes

Don Eduardo tenía una lista de pendientes para el sitio web. Crea una lista ordenada con estos elementos:

1. Terminar página principal
2. Subir galería de fotos
3. Configurar formulario de contacto
4. Publicar archivo histórico
5. Agregar mapa del barrio

Luego, debajo de la lista ordenada, crea una lista desordenada con las secciones del periódico que más te interesen.

### Enigma 2.3: La jerarquía correcta

El siguiente código tiene errores en la jerarquía de headings. Corrígelo:

```html
<h1>La Voz del Barrio</h1>
<h4>Edición Digital</h4>
<h2>Noticias Locales</h2>
<h5>La plaza del barrio</h5>
<p>Artículo completo aquí...</p>
```

¿Cuál es la jerarquía correcta?

### Enigma 2.4: Cita memorable

Don Eduardo dejó varias frases célebres. Una de ellas era:

*"El periodismo local no es pequeño: es íntimo. No habla de todos, habla de ti."*

Usa la etiqueta `<blockquote>` para mostrar esta cita. Añade un `<footer>` dentro del blockquote que diga "— Don Eduardo Zapata".

---

## Lo que aprendiste

- Los **headings** (`<h1>` a `<h6>`) definen la jerarquía del contenido
- Los **párrafos** (`<p>`) contienen bloques de texto
- **`<strong>`** da importancia al texto (negrita)
- **`<em>`** da énfasis al texto (cursiva)
- Las **listas desordenadas** (`<ul>`) muestran elementos sin orden
- Las **listas ordenadas** (`<ol>`) muestran elementos numerados
- Los elementos de lista van dentro de **`<li>`**
- **`<blockquote>`** se usa para citas largas
- **`<hr>`** crea una línea horizontal divisoria
- **`<br>`** forza un salto de línea dentro de un párrafo

---

Valentina guardó el archivo y cerró la computadora. Había escrito su primera página web completa. No era la más bonita del mundo, pero tenía contenido real, estructura y propósito.

—Don Eduardo —dijo en voz baja—, voy a terminar lo que empezaste. Te lo prometo.

Don Carlos, desde la puerta, la observó con una sonrisa.

—¿Sabes qué decía Don Eduardo cuando empezó a aprender HTML?

—¿Qué?

—Decía: "Esto es como escribir un periódico, pero las palabras no se imprimen: se publican. Y una vez publicadas, llegan a todo el mundo".

Valentina sintió un nudo en la garganta. Mañana aprendería a conectar páginas con enlaces y a mostrar las fotos de Don Carlos.
