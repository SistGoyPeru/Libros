# Capítulo 4: Organizando la Información

## Tablas

---

Una semana después, la oficina del periódico estaba irreconocible. Valentina había organizado los archivos, creado varias páginas y establecido la navegación básica del sitio.

Pero un nuevo desafío la esperaba. Don Carlos colocó sobre la mesa varios documentos.

—Esto es lo que Don Eduardo usaba para llevar los registros del periódico —dijo.

Valentina revisó los papeles: horarios de distribución, tarifas de suscripción, directorio de comercios locales, calendario de eventos. Toda la información estaba organizada en filas y columnas.

—Don Eduardo amaba las tablas —dijo Don Carlos—. En papel, pero también quería tenerlas en la web.

Valentina observó los documentos. Eran perfectos para tablas HTML.

---

## Tablas en HTML: la etiqueta `<table>`

Las tablas se construyen con varias etiquetas que trabajan juntas:

```html
<table>
    <tr>
        <td>Celda 1</td>
        <td>Celda 2</td>
    </tr>
    <tr>
        <td>Celda 3</td>
        <td>Celda 4</td>
    </tr>
</table>
```

**Etiquetas básicas:**
- `<table>` — Define la tabla
- `<tr>` — Table row (fila)
- `<td>` — Table data (celda de datos)
- `<th>` — Table header (celda de encabezado, en negrita por defecto)

---

## Tabla de horarios de distribución

Valentina empezó con el horario de distribución del periódico:

```html
<h2>Horarios de Distribución</h2>

<table>
    <tr>
        <th>Día</th>
        <th>Zona Norte</th>
        <th>Zona Sur</th>
        <th>Zona Centro</th>
    </tr>
    <tr>
        <td>Lunes</td>
        <td>8:00 am</td>
        <td>—</td>
        <td>10:00 am</td>
    </tr>
    <tr>
        <td>Martes</td>
        <td>—</td>
        <td>8:00 am</td>
        <td>10:00 am</td>
    </tr>
    <tr>
        <td>Miércoles</td>
        <td>8:00 am</td>
        <td>—</td>
        <td>10:00 am</td>
    </tr>
    <tr>
        <td>Jueves</td>
        <td>—</td>
        <td>8:00 am</td>
        <td>10:00 am</td>
    </tr>
    <tr>
        <td>Viernes</td>
        <td>8:00 am</td>
        <td>—</td>
        <td>10:00 am</td>
    </tr>
    <tr>
        <td>Sábado</td>
        <td>10:00 am</td>
        <td>10:00 am</td>
        <td>10:00 am</td>
    </tr>
</table>
```

—El guión significa que no hay distribución ese día —explicó Valentina.

---

## Encabezados de tabla: `<thead>`, `<tbody>`, `<tfoot>`

Para tablas más complejas, puedes agrupar las filas en tres secciones:

- `<thead>` — Encabezado (la primera fila o filas)
- `<tbody>` — Cuerpo (los datos)
- `<tfoot>` — Pie (totales, resúmenes)

```html
<table>
    <thead>
        <tr>
            <th>Producto</th>
            <th>Precio</th>
            <th>Cantidad</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Suscripción mensual</td>
            <td>S/ 15.00</td>
            <td>120</td>
        </tr>
        <tr>
            <td>Suscripción anual</td>
            <td>S/ 150.00</td>
            <td>45</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th>Totales</th>
            <td>—</td>
            <td>165</td>
        </tr>
    </tfoot>
</table>
```

---

## Tabla de tarifas de suscripción

Valentina creó la tabla de tarifas:

```html
<h2>Tarifas de Suscripción</h2>

<table>
    <thead>
        <tr>
            <th>Plan</th>
            <th>Precio</th>
            <th>Duración</th>
            <th>Beneficios</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Digital Básico</td>
            <td>S/ 15.00</td>
            <td>1 mes</td>
            <td>Acceso web, newsletter semanal</td>
        </tr>
        <tr>
            <td>Digital Premium</td>
            <td>S/ 40.00</td>
            <td>3 meses</td>
            <td>Acceso web, newsletter, archivo histórico</td>
        </tr>
        <tr>
            <td>Impreso + Digital</td>
            <td>S/ 25.00</td>
            <td>1 mes</td>
            <td>Periódico impreso + acceso web completo</td>
        </tr>
        <tr>
            <td>Anual Completo</td>
            <td>S/ 150.00</td>
            <td>12 meses</td>
            <td>Todo incluido + descuento del 20%</td>
        </tr>
    </tbody>
</table>
```

---

## Uniendo celdas: `colspan` y `rowspan`

A veces necesitas que una celda ocupe más de una columna o fila.

### `colspan` — Ocupa varias columnas

```html
<table>
    <tr>
        <th colspan="3">Horarios de Atención</th>
    </tr>
    <tr>
        <td>Lunes a Viernes</td>
        <td>9:00 am</td>
        <td>6:00 pm</td>
    </tr>
    <tr>
        <td>Sábados</td>
        <td>9:00 am</td>
        <td>1:00 pm</td>
    </tr>
    <tr>
        <td colspan="3">Domingos: Cerrado</td>
    </tr>
</table>
```

### `rowspan` — Ocupa varias filas

```html
<h2>Directorio de Comercios Locales</h2>

<table>
    <tr>
        <th>Negocio</th>
        <th>Dirección</th>
        <th>Teléfono</th>
    </tr>
    <tr>
        <td rowspan="2">Panadería El Trigal</td>
        <td>Jr. Las Flores 123</td>
        <td>555-0101</td>
    </tr>
    <tr>
        <td>Av. Principal 456 (Sucursal)</td>
        <td>555-0102</td>
    </tr>
    <tr>
        <td>Farmacia del Barrio</td>
        <td>Jr. La Merced 789</td>
        <td>555-0201</td>
    </tr>
    <tr>
        <td rowspan="2">Restaurante Don Ceviche</td>
        <td>Av. del Mar 321</td>
        <td>555-0301</td>
    </tr>
    <tr>
        <td>Delivery</td>
        <td>555-0302</td>
    </tr>
</table>
```

---

## La etiqueta `<caption>`

Puedes agregar un título a la tabla con `<caption>`:

```html
<table>
    <caption>Tarifas de Suscripción 2026 — La Voz del Barrio</caption>
    <thead>
        <tr>
            <th>Plan</th>
            <th>Precio</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Digital Básico</td>
            <td>S/ 15.00</td>
        </tr>
    </tbody>
</table>
```

Don Carlos observó la tabla en el navegador.

—Esto es mucho más claro que los papeles que tenía Don Eduardo —dijo—. Aquí puedes ver toda la información de un vistazo.

---

## Página completa: Servicios

Valentina integró todo en una página de servicios:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Servicios — La Voz del Barrio</title>
</head>
<body>

    <h1>La Voz del Barrio</h1>
    <nav>
        <a href="index.html">Inicio</a> |
        <a href="noticias.html">Noticias</a> |
        <a href="servicios.html">Servicios</a> |
        <a href="contacto.html">Contacto</a>
    </nav>

    <hr>

    <h2>Servicios del Periódico</h2>

    <h3>Tarifas de Suscripción</h3>

    <table>
        <caption>Planes de suscripción 2026</caption>
        <thead>
            <tr>
                <th>Plan</th>
                <th>Precio</th>
                <th>Duración</th>
                <th>Incluye</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Digital Básico</strong></td>
                <td>S/ 15.00</td>
                <td>1 mes</td>
                <td>Acceso web + newsletter</td>
            </tr>
            <tr>
                <td><strong>Digital Premium</strong></td>
                <td>S/ 40.00</td>
                <td>3 meses</td>
                <td>Web + newsletter + archivo</td>
            </tr>
            <tr>
                <td><strong>Anual Completo</strong></td>
                <td>S/ 150.00</td>
                <td>12 meses</td>
                <td>Todo incluido (ahorra 20%)</td>
            </tr>
        </tbody>
    </table>

    <h3>Horarios de Distribución</h3>

    <table>
        <tr>
            <th>Día</th>
            <th>Zona Norte</th>
            <th>Zona Sur</th>
            <th>Zona Centro</th>
        </tr>
        <tr>
            <td>Lunes a Viernes</td>
            <td>8:00 am</td>
            <td>8:00 am</td>
            <td>10:00 am</td>
        </tr>
        <tr>
            <td>Sábado</td>
            <td colspan="3">Distribución general: 10:00 am</td>
        </tr>
        <tr>
            <td>Domingo</td>
            <td colspan="3">No hay distribución</td>
        </tr>
    </table>

    <h3>Directorio de Comercios</h3>

    <table>
        <tr>
            <th>Negocio</th>
            <th>Dirección</th>
            <th>Teléfono</th>
        </tr>
        <tr>
            <td rowspan="2">Panadería El Trigal</td>
            <td>Jr. Las Flores 123</td>
            <td>555-0101</td>
        </tr>
        <tr>
            <td>Av. Principal 456</td>
            <td>555-0102</td>
        </tr>
        <tr>
            <td>Farmacia del Barrio</td>
            <td>Jr. La Merced 789</td>
            <td>555-0201</td>
        </tr>
    </table>

    <hr>

    <p><a href="index.html">Volver al inicio</a></p>
    <p><small>© 2026 La Voz del Barrio</small></p>

</body>
</html>
```

---

## Enigmas del Capítulo 4

### Enigma 4.1: Tu horario semanal

Crea una tabla HTML con tu horario semanal. Debe tener:

1. Días de la semana como encabezados de columna
2. Horas del día como primera columna (ej: 8:00, 9:00, 10:00...)
3. Tus actividades en las celdas correspondientes
4. Usa `colspan` si una actividad ocupa varias horas
5. Usa `<caption>` para el título

### Enigma 4.2: Tabla de precios

Crea una tabla de comparación de productos o servicios. Por ejemplo:

| Producto | Característica 1 | Característica 2 | Precio |
|----------|-----------------|-----------------|--------|
| Plan A   | 10 GB           | Soporte básico  | $10    |
| Plan B   | 50 GB           | Soporte premium | $25    |

Incluye `<thead>`, `<tbody>` y `<tfoot>` (con un total o resumen).

### Enigma 4.3: Tabla con colspan y rowspan

Crea una tabla que represente el horario de atención de un negocio usando `colspan` y `rowspan`:

```
| DÍA         | MAÑANA        | TARDE         |
| Lunes a Vie | 9:00 - 12:00  | 2:00 - 6:00   |
| Sábado      | colspan="2"   | 9:00 - 1:00   |
| Domingo     | colspan="2"   | Cerrado       |
```

### Enigma 4.4: El directorio del barrio

Investiga 5 negocios de tu barrio (o inventa nombres) y crea un directorio en tabla con: Nombre, Dirección, Teléfono, Horario, Categoría. Usa `rowspan` cuando un negocio tenga múltiples direcciones o teléfonos.

---

## Lo que aprendiste

- Las **tablas** se construyen con `<table>`, `<tr>`, `<td>`, `<th>`
- **`<thead>`**, **`<tbody>`**, **`<tfoot>`** agrupan filas por función
- **`<caption>`** agrega un título a la tabla
- **`colspan`** hace que una celda ocupe varias columnas
- **`rowspan`** hace que una celda ocupe varias filas
- Las tablas son ideales para datos estructurados: horarios, precios, directorios

---

Valentina cerró la computadora y estiró los brazos. Las tablas habían sido más fáciles de lo que pensaba.

—Don Carlos —dijo—, mañana voy a aprender formularios. El periódico necesita un formulario de suscripción y contacto.

—¿Formularios? —preguntó Don Carlos—. ¿Como los de papel que la gente llenaba?

—Sí —sonrió Valentina—. Pero digitales. La gente podrá suscribirse desde su casa, sin moverse del sofá.

Don Carlos silbó, impresionado.

—Don Eduardo siempre decía que el futuro llegaría. Y parece que llegó.
