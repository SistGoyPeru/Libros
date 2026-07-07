# Capítulo 1: El Desafío de la Web

## Introducción a HTML, Estructura del Documento, Etiquetas Básicas

---

La oficina de "La Voz del Barrio" olía a papel, a tinta y a historia. Valentina empujó la puerta de madera que Don Eduardo había pintado de azul veinte años atrás, y sintió que el tiempo se detenía.

Las paredes estaban cubiertas de periódicos antiguos enmarcados: "La Voz del Barrio" había cubierto terremotos, elecciones, campeonatos de fútbol y fiestas patronales. En el centro, una mesa larga de madera servía como escritorio compartido. Y en un rincón, sobre un escritorio atestado de papeles, estaba la computadora portátil de Don Eduardo.

Don Carlos, el fotógrafo, un hombre de sesenta años con barba canosa y una cámara colgada al cuello, la esperaba con dos tazas de café.

—Don Eduardo pasaba las noches aquí —dijo, señalando la computadora—. Decía que estaba construyendo "el futuro del periódico". Nosotros creíamos que jugaba solitario.

Valentina sonrió. Se sentó frente a la computadora y movió el ratón. La pantalla cobró vida. El escritorio mostraba un fondo de pantalla con la foto de la plaza del barrio, llena de gente en una feria dominical.

Y allí, en el centro del escritorio, un archivo llamado "index.html".

—Bueno, Don Eduardo —murmuró Valentina—. Vamos a ver qué me dejaste.

---

## La primera vez que ves código HTML

Valentina hizo doble clic en el archivo. Se abrió un programa que ella no reconocía: el editor de texto. En la pantalla aparecieron líneas de código:

```html
<html>
<head>
    <title>La Voz del Barrio</title>
</head>
<body>
    <h1>La Voz del Barrio</h1>
    <p>El periódico de nuestro barrio desde 1991.</p>
</body>
</html>
```

—¿Qué es todo esto? —preguntó en voz alta.

Don Carlos se acercó, secándose las manos en el pantalón.

—Don Eduardo siempre decía que esto era como escribir una carta, pero para la computadora.

Valentina frunció el ceño. Había diseñado logos, folletos, identidades visuales, pero esto era diferente. Esto era código.

—¿Y esto cómo se ve en internet? —preguntó.

—No sé —admitió Don Carlos—. Él decía que había que "abrirlo en el navegador". Haz doble clic en ese otro archivo que dice "Chrome".

Valentina abrió el navegador y luego arrastró el archivo index.html a la ventana. La pantalla mostró:

# La Voz del Barrio

El periódico de nuestro barrio desde 1991.

—¡Funciona! —exclamó Valentina—. Pero... es muy simple.

—Eso decía Don Eduardo —rió Don Carlos—. Siempre decía: "Esto es como un edificio. Ahora solo tengo los cimientos".

---

## ¿Qué es HTML?

HTML significa **HyperText Markup Language** (Lenguaje de Marcado de Hipertexto). No es un lenguaje de programación como JavaScript o Python. Es un **lenguaje de marcado**: usas etiquetas para decirle al navegador cómo debe mostrar el contenido.

| Concepto | Significado |
|----------|-------------|
| **HyperText** | Texto que puede contener enlaces a otros documentos |
| **Markup** | Marcado: usas etiquetas para marcar el contenido |
| **Language** | Lenguaje con reglas y sintaxis |

### La estructura básica de un documento HTML

Todo documento HTML tiene esta estructura:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Título de la página</title>
</head>
<body>
    Aquí va todo el contenido visible
</body>
</html>
```

**Explicación de cada parte:**

- `<!DOCTYPE html>` — Le dice al navegador que estamos usando HTML5 (la versión más reciente).
- `<html>` — La etiqueta raíz. Todo el contenido va dentro de ella. El atributo `lang="es"` indica que el idioma es español.
- `<head>` — Contiene información **no visible** para el usuario: título de la pestaña, meta tags, enlaces a CSS.
- `<body>` — Contiene todo el contenido **visible** de la página.
- `<meta charset="UTF-8">` — Define la codificación de caracteres (permite usar tildes y ñ).
- `<title>` — El texto que aparece en la pestaña del navegador.

### Etiquetas de apertura y cierre

Las etiquetas HTML generalmente vienen en pares:

- **Apertura:** `<etiqueta>`
- **Cierre:** `</etiqueta>`

La barra inclinada (`/`) indica que es una etiqueta de cierre.

```html
<p>Este es un párrafo.</p>
<h1>Este es un encabezado.</h1>
```

Algunas etiquetas no tienen contenido y se cierran a sí mismas (etiquetas vacías):

```html
<br>  <!-- Salto de línea -->
<hr>  <!-- Línea horizontal -->
```

### Anidamiento de etiquetas

Las etiquetas pueden contener otras etiquetas. Esto se llama **anidamiento**.

```html
<body>
    <h1>Título principal</h1>
    <p>Un párrafo con <strong>texto en negrita</strong>.</p>
</body>
```

**Regla importante:** las etiquetas deben cerrarse en orden inverso al que se abrieron.

✅ Correcto: `<p><strong>Texto</strong></p>`
❌ Incorrecto: `<p><strong>Texto</p></strong>`

### Comentarios en HTML

Los comentarios no se muestran en el navegador. Sirven para dejar notas en el código.

```html
<!-- Este es un comentario -->
<!-- Los comentarios pueden
    ocupar varias líneas -->
```

---

## El proyecto de Don Eduardo

Valentina abrió el archivo index.html en el editor y lo estudió con atención. Don Eduardo había escrito:

```html
<!DOCTYPE html>
<html>
<head>
    <title>La Voz del Barrio</title>
</head>
<body>
    <h1>La Voz del Barrio</h1>
    <p>El periódico de nuestro barrio desde 1991.</p>
    <p>Bienvenidos a la versión digital de nuestro semanario.</p>
</body>
</html>
```

—Falta el `<meta charset="UTF-8">` —notó Valentina, después de leer un tutorial rápido en internet—. Por eso las tildes no se ven bien.

Agregó la línea que faltaba y guardó el archivo.

—Don Carlos —dijo—, ¿cuántas páginas necesita tener el sitio web?

Don Carlos se sentó a su lado y comenzó a enumerar con los dedos:

—La página principal, una página de nosotros, una de servicios, una de contacto, una galería de fotos, y las páginas de cada sección del periódico: noticias, deportes, cultura, opinión.

Valentina suspiró. Eran muchas páginas.

—Pero primero —dijo—, tengo que entender cómo funciona esto. ¿Me prestas la computadora de Don Eduardo por unos días?

—Es tuya —respondió Don Carlos—. Don Eduardo hubiera querido que tú la tuvieras.

---

## Creando tu primera página HTML

Vamos a crear nuestra primera página web. Necesitas dos cosas:

1. **Un editor de texto** (recomiendo Visual Studio Code, pero cualquier editor sirve)
2. **Un navegador web** (Chrome, Firefox, Edge)

### Paso 1: Crear el archivo

Abre tu editor de texto y crea un nuevo archivo. Escríbelo exactamente así:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Primera Página</title>
</head>
<body>
    <h1>¡Hola, mundo!</h1>
    <p>Esta es mi primera página web.</p>
    <p>Estoy aprendiendo HTML con Valentina y Don Eduardo.</p>
</body>
</html>
```

### Paso 2: Guardar el archivo

Guarda el archivo con el nombre `mi_pagina.html`. Es importante que la extensión sea `.html`.

### Paso 3: Abrir en el navegador

Haz doble clic en el archivo o arrástralo a una ventana del navegador.

¡Felicidades! Acabas de crear tu primera página web.

---

## Enigmas del Capítulo 1

### Enigma 1.1: Reconoce tu primera página

Crea un archivo HTML con la estructura básica que incluya:

1. Un título en la pestaña que diga "Mi Primer Sitio"
2. Un encabezado h1 que diga "Bienvenidos"
3. Dos párrafos que hablen sobre ti
4. Una línea horizontal después del encabezado
5. Un comentario que diga "Página creada en 2026"

### Enigma 1.2: El mensaje de Don Eduardo

Don Eduardo dejó una nota en un comentario HTML que Valentina no ha visto. Busca en el código:

```html
<!DOCTYPE html>
<html>
<head>
    <title>La Voz del Barrio</title>
</head>
<body>
    <!-- Valentina: si estás leyendo esto, es porque encontraste el camino.
         El periódico necesita una voz digital. Tú puedes ser esa voz.
         Revisa la carpeta "proyecto" para más archivos.
         — Don Eduardo -->
    <h1>La Voz del Barrio</h1>
</body>
</html>
```

¿Qué mensaje dejó Don Eduardo? Escribe tu propia página HTML con un mensaje similar para alguien que herede tu proyecto.

### Enigma 1.3: Arregla los errores

El siguiente código tiene errores. Encuéntralos y corrígelos:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>La Voz del Barrio</title>
</head>
<body>
    <h1>La Voz del Barrio<h1>
    <p>El periódico del barrio desde 1991.</p>
    <p><strong>Edición digital</p></strong>
</body>
</html>
```

Pista: revisa las etiquetas de cierre y el anidamiento.

### Enigma 1.4: Explora el navegador

Abre tu página HTML en el navegador y luego haz clic derecho en cualquier parte de la página. Selecciona "Inspeccionar" o "Ver código fuente". ¿Qué ves? ¿Se parece al código que escribiste?

Busca la pestaña "Elements" o "Elementos" en las herramientas de desarrollador. Allí puedes ver cómo el navegador interpretó tu HTML.

---

## Lo que aprendiste

- **HTML** significa HyperText Markup Language — es un lenguaje de marcado, no de programación
- Todo documento HTML tiene la estructura: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`
- Las etiquetas generalmente vienen en pares: apertura `<etiqueta>` y cierre `</etiqueta>`
- Las etiquetas se **anidan** — deben cerrarse en orden inverso
- Los **comentarios** se escriben con `<!-- -->` y no se muestran en el navegador
- El `<meta charset="UTF-8">` permite usar tildes y caracteres especiales
- El `<title>` define el texto de la pestaña del navegador

---

Valentina cerró la computadora y estiró los brazos. Había entendido la estructura básica de HTML. Era como aprender un nuevo idioma: al principio todo parecía extraño, pero comenzaba a tener sentido.

—Mañana vuelvo —le dijo a Don Carlos—. Y empezamos a darle contenido a este periódico digital.

Al salir, miró por última vez la pantalla de la computadora. El archivo index.html parpadeaba en el editor, como un faro en la oscuridad.

Don Eduardo había dejado los cimientos. Ahora solo faltaba construir la casa.
