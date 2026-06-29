# Capítulo 5: La Voz del Barrio

## Formularios

---

Una mañana, Valentina encontró a Don Carlos revisando una caja llena de sobres.

—Son cartas de lectores —dijo Don Carlos—. Don Eduardo las guardaba todas. Mira esta.

Valentina tomó la carta. Estaba fechada en 1994:

*"Estimado Don Eduardo: Gracias por publicar mi aviso de la venta de mi comedor. En una semana lo vendí gracias a usted. Adjunto el pago de mi suscripción por un año más. — María Rojas"*

—La gente usaba el periódico para todo —dijo Valentina—. Para vender cosas, para encontrar trabajo, para quejarse, para agradecer.

—Y ahora —dijo Don Carlos—, ¿cómo hace la gente para contactarnos?

Valentina se dio cuenta del problema. El sitio web no tenía forma de recibir mensajes de los lectores. Necesitaba un **formulario de contacto** y un **formulario de suscripción**.

---

## Formularios en HTML: la etiqueta `<form>`

Los formularios permiten al usuario enviar información al sitio web.

```html
<form action="procesar.php" method="post">
    <!-- Aquí van los campos del formulario -->
</form>
```

**Atributos principales de `<form>`:**

| Atributo | Descripción |
|----------|-------------|
| `action` | URL donde se envían los datos |
| `method` | Cómo se envían: `get` (visible en URL) o `post` (oculto) |

Para este libro, usaremos `method="post"` y `action="#"` (que significa "a la misma página").

---

## Input: el campo de entrada

La etiqueta `<input>` crea diferentes tipos de campos según su atributo `type`.

### Tipos de input

```html
<!-- Texto -->
<label for="nombre">Nombre:</label>
<input type="text" id="nombre" name="nombre" placeholder="Tu nombre">

<!-- Correo electrónico -->
<label for="email">Correo:</label>
<input type="email" id="email" name="email" placeholder="correo@ejemplo.com">

<!-- Número -->
<label for="edad">Edad:</label>
<input type="number" id="edad" name="edad" min="1" max="120">

<!-- Contraseña -->
<label for="password">Contraseña:</label>
<input type="password" id="password" name="password">

<!-- Teléfono -->
<label for="telefono">Teléfono:</label>
<input type="tel" id="telefono" name="telefono" placeholder="999-999-999">
```

**Atributos comunes de input:**

| Atributo | Descripción |
|----------|-------------|
| `type` | Tipo de campo (text, email, number, etc.) |
| `id` | Identificador único (para conectar con label) |
| `name` | Nombre del campo (se envía al servidor) |
| `placeholder` | Texto de ejemplo dentro del campo |
| `required` | Campo obligatorio |
| `value` | Valor predeterminado |

---

## La etiqueta `<label>`

El `<label>` asocia un texto descriptivo con un campo. Es importante para la accesibilidad.

```html
<!-- Opción 1: label envolviendo el input -->
<label>Nombre: <input type="text" name="nombre"></label>

<!-- Opción 2: label con for, input con id (RECOMENDADA) -->
<label for="nombre">Nombre:</label>
<input type="text" id="nombre" name="nombre">
```

---

## El formulario de contacto de "La Voz del Barrio"

Valentina creó el primer formulario del periódico:

```html
<h2>Contáctanos</h2>

<form action="#" method="post">
    <p>
        <label for="nombre">Nombre completo:</label>
        <input type="text" id="nombre" name="nombre" placeholder="Tu nombre" required>
    </p>

    <p>
        <label for="email">Correo electrónico:</label>
        <input type="email" id="email" name="email" placeholder="correo@ejemplo.com" required>
    </p>

    <p>
        <label for="telefono">Teléfono (opcional):</label>
        <input type="tel" id="telefono" name="telefono" placeholder="999-999-999">
    </p>

    <p>
        <label for="asunto">Asunto:</label>
        <select id="asunto" name="asunto">
            <option value="">Selecciona un asunto</option>
            <option value="suscripcion">Suscripción</option>
            <option value="publicidad">Publicidad</option>
            <option value="noticia">Sugerir noticia</option>
            <option value="carta">Carta al director</option>
            <option value="otro">Otro</option>
        </select>
    </p>

    <p>
        <label for="mensaje">Mensaje:</label>
        <textarea id="mensaje" name="mensaje" rows="6" placeholder="Escribe tu mensaje aquí..." required></textarea>
    </p>

    <p>
        <input type="submit" value="Enviar mensaje">
    </p>
</form>
```

---

## `<select>` y `<option>`: Listas desplegables

```html
<label for="pais">País:</label>
<select id="pais" name="pais">
    <option value="">Selecciona un país</option>
    <option value="pe">Perú</option>
    <option value="ar">Argentina</option>
    <option value="cl">Chile</option>
    <option value="co">Colombia</option>
    <option value="mx">México</option>
</select>
```

Para permitir selección múltiple: `<select id="..." name="..." multiple>`.

Para agrupar opciones: `<optgroup label="América del Sur">`.

---

## `<textarea>`: Área de texto

```html
<label for="comentarios">Comentarios:</label>
<textarea id="comentarios" name="comentarios" rows="4" cols="50" placeholder="Escribe aquí..."></textarea>
```

- `rows` — número de filas visibles (alto)
- `cols` — número de columnas visibles (ancho, aunque se recomienda usar CSS)

---

## Botones: submit, reset, button

```html
<!-- Botón para enviar el formulario -->
<input type="submit" value="Enviar">

<!-- Botón para limpiar el formulario -->
<input type="reset" value="Limpiar">

<!-- Botón genérico (requiere JavaScript) -->
<button type="button">Haz clic</button>

<!-- Botón con contenido HTML -->
<button type="submit">
    <strong>Enviar mensaje</strong>
</button>
```

---

## Radio buttons y checkboxes

### Radio buttons (selección única)

```html
<p>¿Cómo conociste el periódico?</p>

<input type="radio" id="recomendacion" name="conociste" value="recomendacion">
<label for="recomendacion">Recomendación</label>

<input type="radio" id="redes" name="conociste" value="redes">
<label for="redes">Redes sociales</label>

<input type="radio" id="calle" name="conociste" value="calle">
<label for="calle">En la calle</label>

<input type="radio" id="otro" name="conociste" value="otro">
<label for="otro">Otro</label>
```

**Importante:** todos los radio buttons del mismo grupo deben tener el mismo `name`.

### Checkboxes (selección múltiple)

```html
<p>Secciones de interés:</p>

<input type="checkbox" id="seccion_noticias" name="interes" value="noticias">
<label for="seccion_noticias">Noticias</label>

<input type="checkbox" id="seccion_deportes" name="interes" value="deportes">
<label for="seccion_deportes">Deportes</label>

<input type="checkbox" id="seccion_cultura" name="interes" value="cultura">
<label for="seccion_cultura">Cultura</label>

<input type="checkbox" id="seccion_opinion" name="interes" value="opinion">
<label for="seccion_opinion">Opinión</label>
```

---

## Formulario completo de suscripción

Valentina combinó todo lo aprendido:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Suscripción — La Voz del Barrio</title>
</head>
<body>

    <h1>La Voz del Barrio</h1>
    <nav>
        <a href="index.html">Inicio</a> |
        <a href="suscripcion.html">Suscripción</a> |
        <a href="contacto.html">Contacto</a>
    </nav>

    <hr>

    <h2>Formulario de Suscripción</h2>
    <p>Completa tus datos para recibir el periódico en tu correo o en tu casa.</p>

    <form action="#" method="post">

        <fieldset>
            <legend>Datos personales</legend>

            <p>
                <label for="nombre">Nombre completo:</label>
                <input type="text" id="nombre" name="nombre" required>
            </p>

            <p>
                <label for="email">Correo electrónico:</label>
                <input type="email" id="email" name="email" required>
            </p>

            <p>
                <label for="telefono">Teléfono:</label>
                <input type="tel" id="telefono" name="telefono">
            </p>
        </fieldset>

        <fieldset>
            <legend>Tipo de suscripción</legend>

            <p>
                <input type="radio" id="digital" name="plan" value="digital" checked>
                <label for="digital">Digital Básico — S/ 15.00/mes</label>
            </p>

            <p>
                <input type="radio" id="premium" name="plan" value="premium">
                <label for="premium">Digital Premium — S/ 40.00/trimestre</label>
            </p>

            <p>
                <input type="radio" id="completo" name="plan" value="completo">
                <label for="completo">Anual Completo — S/ 150.00/año</label>
            </p>
        </fieldset>

        <fieldset>
            <legend>Secciones de interés</legend>

            <p>
                <input type="checkbox" id="interes_noticias" name="interes" value="noticias" checked>
                <label for="interes_noticias">Noticias locales</label>
            </p>

            <p>
                <input type="checkbox" id="interes_deportes" name="interes" value="deportes">
                <label for="interes_deportes">Deportes</label>
            </p>

            <p>
                <input type="checkbox" id="interes_cultura" name="interes" value="cultura">
                <label for="interes_cultura">Cultura</label>
            </p>

            <p>
                <input type="checkbox" id="interes_opinion" name="interes" value="opinion">
                <label for="interes_opinion">Opinión</label>
            </p>
        </fieldset>

        <fieldset>
            <legend>Método de pago</legend>

            <p>
                <label for="metodo">Selecciona método:</label>
                <select id="metodo" name="metodo">
                    <option value="tarjeta">Tarjeta de crédito/débito</option>
                    <option value="transferencia">Transferencia bancaria</option>
                    <option value="yape">Yape/Plin</option>
                    <option value="efectivo">Pago en efectivo (oficina)</option>
                </select>
            </p>
        </fieldset>

        <p>
            <label for="notas">Notas adicionales:</label>
            <textarea id="notas" name="notas" rows="4" placeholder="¿Algo que debamos saber?"></textarea>
        </p>

        <p>
            <input type="submit" value="Suscribirme ahora">
            <input type="reset" value="Limpiar formulario">
        </p>

    </form>

    <hr>

    <p><a href="index.html">Volver al inicio</a></p>
    <p><small>© 2026 La Voz del Barrio</small></p>

</body>
</html>
```

---

## `<fieldset>` y `<legend>`: Agrupar campos

`<fieldset>` agrupa campos relacionados y `<legend>` le da un título al grupo.

```html
<fieldset>
    <legend>Información de contacto</legend>
    <!-- campos aquí -->
</fieldset>
```

---

## Enigmas del Capítulo 5

### Enigma 5.1: Formulario de encuesta

Crea un formulario de encuesta para los lectores del periódico. Debe incluir:

1. Nombre (texto)
2. Edad (número)
3. Correo electrónico
4. ¿Con qué frecuencia lees el periódico? (radio: diario, semanal, mensual, ocasional)
5. ¿Qué sección te gusta más? (select con opciones: Noticias, Deportes, Cultura, Opinión)
6. Comentarios (textarea)
7. Casillas de verificación para temas de interés (mínimo 4)
8. Botón de enviar

### Enigma 5.2: Formulario de sugerencias

El periódico quiere recibir sugerencias de los lectores. Crea un formulario con:

1. Nombre (texto, requerido)
2. Correo (email, requerido)
3. Tipo de sugerencia (select: mejora del sitio, contenido, evento, otro)
4. Sugerencia (textarea, requerido)
5. ¿Te gustaría recibir respuesta? (checkbox)
6. Botón enviar

Usa `fieldset` y `legend` para agrupar los campos.

### Enigma 5.3: Formulario de pedido de publicidad

Crea un formulario para que los comercios locales puedan solicitar publicidad en el periódico:

1. Nombre del negocio (texto)
2. Nombre del contacto (texto)
3. Correo (email)
4. Teléfono (tel)
5. Tipo de anuncio (radio: pequeño, mediano, grande, página completa)
6. Duración (select: 1 semana, 2 semanas, 1 mes, 3 meses)
7. Descripción del anuncio (textarea)
8. ¿Incluye logo? (checkbox)
9. Botón enviar

### Enigma 5.4: Input types especiales

Investiga y usa al menos 3 de estos tipos de input en un formulario:

- `date` — selector de fecha
- `color` — selector de color
- `range` — control deslizante
- `file` — subir archivo
- `url` — campo de URL
- `search` — campo de búsqueda

---

## Lo que aprendiste

- **`<form>`** define un formulario con `action` y `method`
- **`<input>`** crea campos de entrada con diferentes `type` (text, email, number, radio, checkbox, submit, etc.)
- **`<label>`** asocia texto a campos (mejora accesibilidad)
- **`<select>`** y **`<option>`** crean listas desplegables
- **`<textarea>`** crea áreas de texto multilínea
- **`<fieldset>`** y **`<legend>`** agrupan campos relacionados
- **`required`** hace que un campo sea obligatorio
- **`placeholder`** muestra un texto de ejemplo dentro del campo

---

Valentina guardó el formulario y lo probó. Al hacer clic en "Enviar", la página se recargaba (porque usamos `action="#"`). Pero en un sitio real, esos datos irían a un servidor.

—¿Y los datos llegan a algún lado? —preguntó Don Carlos.

—Todavía no —admitió Valentina—. Para eso necesito un lenguaje de servidor como PHP o JavaScript. Pero por ahora, el formulario está listo. Cuando aprendamos eso, solo tendremos que conectar los datos.

—Don Eduardo —dijo Don Carlos, sonriendo— siempre decía que lo importante es tener la puerta abierta. Después se ve quién entra.

Valentina asintió. La puerta estaba abierta. Los lectores ya podían escribir al periódico, suscribirse, sugerir noticias. La voz del barrio comenzaba a escucharse también en la web.
