# Capítulo 9: Para Todos

## Accesibilidad Web

---

Un jueves por la mañana, Valentina recibió un correo que la hizo reflexionar profundamente.

*"Estimados señores de La Voz del Barrio:*

*Soy Pedro Gutiérrez, lector del periódico desde hace 20 años. Lamentablemente, perdí la vista hace 5 años debido a una enfermedad. Mi hija me dijo que ahora tienen un sitio web, pero cuando intenté acceder con mi lector de pantalla, no pude navegar correctamente. Los botones no tenían descripciones, las imágenes no tenían texto alternativo, y los formularios eran imposibles de llenar.*

*¿Podrían hacer algo para que el sitio sea accesible para personas como yo?*

*Atentamente,*
*Pedro Gutiérrez"*

Valentina sintió un nudo en el estómago. Había estado tan concentrada en hacer que el sitio funcionara, que nunca consideró que alguien con discapacidad visual pudiera usarlo.

—Don Carlos —dijo, con la voz entrecortada—, hemos estado excluyendo a personas como Don Pedro.

Don Carlos leyó el correo y asintió gravemente.

—Don Eduardo siempre decía que el periódico era para todos. Literalmente, para todos. No podemos tener un sitio web que deje fuera a nadie.

---

## ¿Qué es la accesibilidad web?

La **accesibilidad web** (a11y — por las 11 letras entre la "a" y la "y") significa diseñar y desarrollar sitios web que puedan ser utilizados por **todas las personas**, independientemente de sus capacidades físicas o técnicas.

**¿A quién beneficia la accesibilidad?**

- Personas con discapacidad visual (ceguera, baja visión, daltonismo)
- Personas con discapacidad auditiva
- Personas con discapacidad motriz (dificultad para usar el ratón)
- Personas con discapacidad cognitiva
- Personas mayores
- Cualquier persona en un entorno con limitaciones (sol en la pantalla, ruido, manos ocupadas)

---

## Texto alternativo en imágenes (`alt`)

Ya aprendimos que `alt` es obligatorio en `<img>`. Pero su función principal no es el SEO: es la **accesibilidad**.

```html
<!-- ✅ Bueno: describe el contenido de la imagen -->
<img src="plaza-remodelacion.jpg" alt="Maqueta digital de la nueva plaza del barrio con áreas verdes y juegos infantiles">

<!-- ❌ Malo: no aporta información -->
<img src="plaza-remodelacion.jpg" alt="imagen">

<!-- ❌ Malo: redundante -->
<img src="plaza-remodelacion.jpg" alt="imagen de la plaza">

<!-- ✅ Imagen decorativa: alt vacío -->
<img src="decoracion.png" alt="" role="presentation">
```

**Reglas para el texto alternativo:**
- Describe lo que se ve en la imagen
- Sé conciso pero descriptivo
- Si la imagen tiene texto, inclúyelo en el `alt`
- Si la imagen es decorativa, usa `alt=""` (vacío)
- No empieces con "imagen de..." o "foto de..."

---

## `aria-label` y `role`: etiquetas para accesibilidad

**ARIA** (Accessible Rich Internet Applications) es un conjunto de atributos que mejoran la accesibilidad.

### `aria-label` — etiqueta invisible

```html
<!-- Sin aria-label: el lector de pantalla solo leería el ícono -->
<button>✉</button>

<!-- Con aria-label: el lector dice "Enviar correo" -->
<button aria-label="Enviar correo">✉</button>
```

### `role` — rol del elemento

```html
<nav role="navigation">
    <!-- enlaces -->
</nav>

<button role="button">Haz clic</button>

<!-- Rol para elementos decorativos -->
<img src="decoracion.png" alt="" role="presentation">
```

---

## Idioma de la página: `lang`

El atributo `lang` en `<html>` le dice al lector de pantalla en qué idioma está la página.

```html
<html lang="es">
```

Si tienes contenido en otro idioma, indícalo con `lang` en el elemento específico:

```html
<p>El periódico se llama <span lang="en">"The Voice of the Neighborhood"</span> en inglés.</p>
```

---

## `tabindex`: orden de navegación con teclado

Algunas personas navegan usando solo el teclado (tecla Tab). El atributo `tabindex` controla el orden de navegación.

```html
<!-- Orden natural (recomendado) -->
<a href="index.html">Inicio</a>
<a href="noticias.html">Noticias</a>
<a href="contacto.html">Contacto</a>

<!-- Orden personalizado (usar con precaución) -->
<a href="contacto.html" tabindex="3">Contacto</a>
<a href="index.html" tabindex="1">Inicio</a>
<a href="noticias.html" tabindex="2">Noticias</a>
```

**Regla de oro:** no uses `tabindex` a menos que sea estrictamente necesario. El orden natural del HTML es el mejor.

---

## Skip navigation (saltar navegación)

Para usuarios de teclado, navegar por el menú en cada página puede ser tedioso. Un **enlace de salto** permite ir directamente al contenido principal.

```html
<body>
    <!-- Enlace invisible que aparece al enfocarse con teclado -->
    <a href="#contenido-principal" class="skip-link">Saltar al contenido principal</a>

    <header>
        <nav>
            <a href="index.html">Inicio</a>
            <a href="noticias.html">Noticias</a>
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>

    <main id="contenido-principal">
        <h1>Bienvenidos a La Voz del Barrio</h1>
        <!-- Contenido principal -->
    </main>
</body>
```

---

## Contraste de colores

El texto debe tener suficiente contraste con el fondo para ser legible.

| Elemento | Contraste mínimo recomendado |
|----------|------------------------------|
| Texto normal | 4.5:1 |
| Texto grande (18px+ o 14px bold+) | 3:1 |

**Herramientas para verificar contraste:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Lighthouse en Chrome DevTools

---

## Formularios accesibles

Los formularios deben tener `<label>` asociado a cada campo.

```html
<!-- ✅ Accesible -->
<label for="nombre">Nombre completo:</label>
<input type="text" id="nombre" name="nombre" required>

<!-- ❌ No accesible (sin label) -->
<input type="text" name="nombre" placeholder="Nombre">
```

Para agrupar campos relacionados:

```html
<fieldset>
    <legend>Información personal</legend>

    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre">

    <label for="email">Correo:</label>
    <input type="email" id="email" name="email">
</fieldset>
```

---

## Página de contacto accesible

Valentina reescribió el formulario de contacto con accesibilidad en mente:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Contacta con La Voz del Barrio. Formulario accesible para todos los lectores.">
    <title>Contacto — La Voz del Barrio</title>
</head>
<body>

    <a href="#contenido-principal" style="position:absolute;left:-9999px;">Saltar al contenido principal</a>

    <header>
        <h1>La Voz del Barrio</h1>
        <nav role="navigation" aria-label="Navegación principal">
            <a href="index.html">Inicio</a> |
            <a href="noticias.html">Noticias</a> |
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>

    <hr>

    <main id="contenido-principal">
        <h2>Contáctanos</h2>

        <p>¿Tienes una noticia, sugerencia o consulta? Este formulario es accesible para lectores de pantalla.</p>

        <form action="#" method="post">
            <fieldset>
                <legend>Tus datos</legend>

                <p>
                    <label for="nombre">Nombre completo:</label>
                    <input type="text" id="nombre" name="nombre" required aria-required="true">
                </p>

                <p>
                    <label for="email">Correo electrónico:</label>
                    <input type="email" id="email" name="email" required aria-required="true">
                </p>
            </fieldset>

            <fieldset>
                <legend>Tu mensaje</legend>

                <p>
                    <label for="asunto">Asunto:</label>
                    <select id="asunto" name="asunto">
                        <option value="">Selecciona un asunto</option>
                        <option value="suscripcion">Suscripción</option>
                        <option value="noticia">Sugerir noticia</option>
                        <option value="queja">Queja o sugerencia</option>
                        <option value="otro">Otro</option>
                    </select>
                </p>

                <p>
                    <label for="mensaje">Mensaje:</label>
                    <textarea id="mensaje" name="mensaje" rows="6" required aria-required="true"></textarea>
                </p>
            </fieldset>

            <p>
                <button type="submit" aria-label="Enviar mensaje de contacto">Enviar mensaje</button>
            </p>
        </form>
    </main>

    <hr>

    <footer role="contentinfo">
        <p>© 2026 La Voz del Barrio</p>
        <address aria-label="Información de contacto">
            Correo: <a href="mailto:contacto@lavozdelbarrio.com">contacto@lavozdelbarrio.com</a><br>
            Teléfono: <a href="tel:+5115550400">(01) 555-0400</a>
        </address>
    </footer>

</body>
</html>
```

---

## Principios de accesibilidad (WCAG)

Las **Pautas de Accesibilidad para el Contenido Web (WCAG)** se basan en cuatro principios:

| Principio | Significado |
|-----------|-------------|
| **Perceptible** | La información debe presentarse de forma que los usuarios puedan percibirla |
| **Operable** | Los componentes de la interfaz deben ser operables |
| **Comprensible** | La información y operaciones deben ser comprensibles |
| **Robusto** | El contenido debe ser interpretable por diferentes tecnologías |

---

## Enigmas del Capítulo 9

### Enigma 9.1: Audita tu página

Toma una página HTML que hayas creado antes y verifica:

1. ¿Todas las imágenes tienen `alt` descriptivo?
2. ¿Los formularios tienen `<label>` asociado a cada campo?
3. ¿El HTML tiene `lang="es"`?
4. ¿Hay un enlace para saltar la navegación?
5. ¿Los botones tienen `aria-label` si usan iconos?

Corrige todo lo que encuentres.

### Enigma 9.2: Alt descriptivo

Escribe textos `alt` descriptivos para estas imágenes:

1. Una foto de la plaza del barrio durante un festival
2. El logo del periódico (que dice "La Voz del Barrio")
3. Una foto de Don Eduardo escribiendo en su máquina de escribir
4. Un gráfico que muestra el crecimiento de lectores

### Enigma 9.3: Formulario accesible

Convierte este formulario no accesible en uno accesible:

```html
<form>
    <input type="text" placeholder="Nombre">
    <input type="email" placeholder="Correo">
    <input type="checkbox"> Acepto los términos
    <button>Enviar</button>
</form>
```

### Enigma 9.4: Skip link

Agrega un enlace de salto (skip to content) a una de tus páginas. Debe:

1. Ser el primer elemento enfocable de la página
2. Llevar al contenido principal (usando `id="contenido-principal"`)
3. Ser invisible hasta que alguien navegue con Tab (puedes usar CSS inline)

### Enigma 9.5: Carta a Don Pedro

Escribe una página HTML que sea una carta de respuesta a Don Pedro Gutiérrez, explicándole las mejoras de accesibilidad que has implementado en el sitio. Usa HTML semántico y asegúrate de que la página sea accesible.

---

## Lo que aprendiste

- La **accesibilidad web** asegura que todos puedan usar tu sitio
- El atributo **`alt`** describe imágenes para lectores de pantalla
- **`aria-label`** da etiquetas a elementos sin texto visible
- **`role`** define el propósito de un elemento
- **`lang`** indica el idioma de la página
- Los **formularios accesibles** usan `<label>` en todos los campos
- El **enlace de salto** (skip link) permite ir directo al contenido
- Un buen **contraste de colores** mejora la legibilidad
- Las pautas **WCAG** son el estándar internacional de accesibilidad

---

Valentina respondió el correo de Don Pedro:

*"Estimado Don Pedro:*

*Gracias por escribirnos. Tiene toda la razón: nuestro sitio no estaba preparado para personas con discapacidad visual. Pero gracias a su mensaje, hemos implementado mejoras significativas.*

*Todas las imágenes ahora tienen descripciones. Los formularios son navegables con lectores de pantalla. Hemos agregado un enlace para saltar la navegación y mejorado el contraste de colores.*

*La Voz del Barrio es para todos. Y eso incluye personas como usted, cuya opinión valoramos profundamente.*

*Atentamente,*
*Valentina Rivas*
*Diseñadora web de La Voz del Barrio"*

Don Carlos la observó mientras escribía.

—Don Eduardo estaría orgulloso —dijo—. No solo hiciste un sitio web. Hiciste un sitio web para todos.

Valentina sonrió. Faltaba el último paso: unir todo en el sitio web completo.
