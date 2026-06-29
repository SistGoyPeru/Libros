# Capítulo 8: La Feria de la Madera

## Ordenar y Filtrar Datos

---

El informe para el banco fue un éxito. El gerente, impresionado por la presentación profesional de Sofía, no solo renovó el préstamo sino que ofreció una línea de crédito adicional para "proyectos de expansión".

Pero Sofía no tuvo tiempo para celebrar. Se acercaba la **Feria de la Madera**, el evento más importante del año para los carpinteros de Lima. Era una oportunidad para mostrar productos, conseguir clientes, y ver lo que hacía la competencia.

El problema era organizar todo. Tenía decenas de productos, cada uno con diferentes precios, calidades y tiempos de entrega. Necesitaba un catálogo ordenado.

—Don Manuel —dijo—, ¿cómo organizaba mi abuelo los productos para la feria?

Don Manuel se rascó la barbilla.

—Tu abuelo tenía un sistema. Pero era mental. Él sabía qué producto era mejor para cada cliente. Pero cuando empezó a usar la computadora, creo que hizo una lista...

Sofía buscó en la computadora y encontró un archivo llamado "Catalogo_Feria.xlsx". Al abrirlo, vio una tabla con más de treinta productos, todos mezclados, sin orden alguno.

—Esto es un caos —murmuró—. Hay que ordenar esto.

---

## Ordenar datos

Ordenar datos en Excel es como organizar herramientas en un panel: pones cada cosa en su lugar para encontrarla rápidamente.

### Orden simple

1. Selecciona cualquier celda dentro de la columna por la que quieres ordenar
2. Ve a **Inicio > Ordenar y filtrar** (o a la pestaña **Datos**)
3. Elige **Ordenar de A a Z** (ascendente) o **Ordenar de Z a A** (descendente)

Sofía seleccionó la columna "Producto" y ordenó de A a Z. Inmediatamente, todos los productos se alinearon alfabéticamente:

| A | B | C |
|---|---|---|
| **Producto** | **Precio** | **Calidad** |
| Banquito | 80 | B |
| Cama king | 680 | A |
| Cama queen | 450 | A |
| Cómoda | 420 | A |
| Escritorio | 280 | B |
| Estante | 180 | C |
| Mesa de centro | 250 | B |
| Mesa de noche | 120 | B |
| Mesa comedor | 520 | A |
| Ropero | 890 | A |
| Silla | 150 | B |
| Sillón | 520 | A |

—Mucho mejor —dijo Sofía—. Ahora encuentro cualquier producto en segundos.

### Orden por múltiples columnas

Pero Sofía necesitaba un orden más específico: primero por Calidad (A, B, C) y luego por Precio (de mayor a menor).

1. Seleccionó toda la tabla
2. Fue a **Datos > Ordenar**
3. En el cuadro de diálogo, agregó el primer nivel: **Columna: Calidad, Orden: De A a Z**
4. Luego **Agregar nivel**: **Columna: Precio, Orden: De mayor a menor**

| A | B | C |
|---|---|---|
| **Producto** | **Precio** | **Calidad** |
| Ropero | 890 | A |
| Cama king | 680 | A |
| Cama queen | 450 | A |
| Cómoda | 420 | A |
| Mesa comedor | 520 | A |
| Sillón | 520 | A |
| Escritorio | 280 | B |
| Mesa de centro | 250 | B |
| Silla | 150 | B |
| Mesa de noche | 120 | B |
| Banquito | 80 | B |
| Estante | 180 | C |

—Ahora los productos de primera calidad (A) aparecen primero, ordenados del más caro al más barato. Los clientes que buscan lo mejor verán primero nuestras piezas premium.

### Orden personalizado

Sofía quería un orden aún más específico: quería que los productos aparecieran por categoría (Dormitorio, Sala, Comedor) y dentro de cada categoría, por precio descendente.

Para esto, usó **Orden personalizado**:

1. Datos > Ordenar
2. Columna: Categoría, Orden: Lista personalizada
3. Creó una lista: Dormitorio, Sala, Comedor, Accesorios
4. Agregó nivel: Precio, De mayor a menor

---

## Filtrar datos

Si ordenar es organizar, filtrar es como usar un imán para encontrar solo las piezas que necesitas. El filtro oculta temporalmente las filas que no cumplen una condición.

### Activar filtros

1. Selecciona cualquier celda de la tabla
2. Ve a **Datos > Filtro** (o **Inicio > Ordenar y filtrar > Filtro**)
3. Aparecen flechas en cada encabezado de columna

### Filtrar por valor

Sofía hizo clic en la flecha de la columna "Calidad" y desmarcó B y C, dejando solo A marcado. La tabla mostró solo los productos de primera calidad.

### Filtrar por condición numérica

Quería ver solo los productos que cuestan menos de S/ 300:

1. Flecha en columna Precio > **Filtros de número > Menor que...**
2. Escribió 300
3. Excel mostró solo los productos con precio menor a 300

### Filtrar por texto

Para encontrar productos que contengan "mesa":

1. Flecha en columna Producto > **Filtros de texto > Contiene...**
2. Escribió "mesa"
3. Aparecieron: Mesa de centro, Mesa de noche, Mesa comedor

### Filtros múltiples

Sofía combinó filtros: productos de Calidad A, con precio entre 400 y 700, y que sean de la categoría "Dormitorio".

—Esto es increíble —dijo—. Encuentro exactamente lo que necesito en segundos.

---

## Preparando el catálogo para la feria

Sofía usó ordenar y filtrar para crear diferentes vistas del catálogo:

**Vista 1: Productos premium (Calidad A)**
Filtro: Calidad = A, ordenado por precio descendente.

**Vista 2: Productos económicos (menos de S/ 200)**
Filtro: Precio < 200, ordenado por precio ascendente.

**Vista 3: Productos por categoría**
Orden: Categoría (personalizado), luego Precio descendente.

Para cada vista, Sofía copió los resultados a una hoja separada y les dio formato profesional con bordes y colores.

—El día de la feria —explicó a Don Manuel—, si un cliente me pregunta por muebles de dormitorio económicos, tengo la lista lista en segundos.

---

## El descubrimiento inesperado

Mientras exploraba los datos filtrando y ordenando, Sofía encontró algo curioso. Había un producto llamado "Banquito Tallado" que aparecía dos veces en el catálogo, con precios diferentes: S/ 80 y S/ 120.

—Don Manuel, ¿esto es un error?

El viejo carpintero se acercó a mirar.

—No, mija. Tu abuelo hacía dos versiones: una simple y una tallada a mano. Pero en el catálogo solo puso "Banquito Tallado" para ambas.

Sofía sonrió. Su abuelo no era perfecto con los datos. Pero gracias a Excel, ella podía encontrar y corregir estos errores.

Renombró los productos:
- "Banquito simple" → S/ 80
- "Banquito tallado a mano" → S/ 120

—Los datos solo son útiles si son precisos —dijo Sofía—. Y ahora lo son.

---

## Enigmas del Capítulo 8

### Enigma 8.1: Ordena el inventario

Usando el inventario del Capítulo 1, realiza los siguientes órdenes:

1. Ordena los productos alfabéticamente (A a Z)
2. Ordena por Precio Unitario de mayor a menor
3. Ordena por Proveedor (A a Z) y luego por Cantidad (mayor a menor)
4. ¿Cuál es el producto más caro? ¿Cuál es el más barato?

### Enigma 8.2: Filtra para encontrar

Usando el catálogo de productos del capítulo, aplica los siguientes filtros:

1. Muestra solo los productos de Calidad A
2. Muestra solo los productos con precio menor a S/ 300
3. Muestra solo los productos cuyo nombre contiene "cama" o "mesa"
4. Muestra los productos de Calidad B con precio entre 100 y 300
5. ¿Cuántos productos de Calidad A tienen precio mayor a S/ 500?

### Enigma 8.3: Limpieza de datos

Revisa el catálogo de Don Rafael. Encuentra los siguientes problemas y corrígelos:

1. "Silla comedor" y "Silla de Comedor" aparecen como productos diferentes pero son el mismo
2. "Mesa centr" tiene un error ortográfico (debe ser "Mesa centro")
3. El precio de "Cómoda" aparece como 42.0 en lugar de 420.00 (error de decimal)

¿Qué otras inconsistencias encuentras?

### Enigma 8.4: Crea un catálogo para la feria

Crea una nueva hoja llamada "Feria_Madera". Copia los primeros 10 productos de tu catálogo ordenados por Calidad (A primero) y luego por Precio (mayor a menor). Agrega las columnas:

- **Código:** CAT-001, CAT-002, etc.
- **Precio Feria:** Precio normal con 10% de descuento (=Precio*0.90)
- **Disponibilidad:** "Inmediata" si Cantidad > 10, "Bajo pedido" si Cantidad <= 10

Pista: para la columna Disponibilidad, puedes usar la función SI que aprenderás más adelante, o hacerlo manualmente.

---

## Lo que aprendiste

- **Ordenar** datos organiza las filas según el valor de una o más columnas
- Puedes ordenar de forma **ascendente** (A-Z, menor-mayor) o **descendente** (Z-A, mayor-menor)
- El **orden por múltiples columnas** crea jerarquías de ordenamiento
- **Filtrar** oculta temporalmente filas que no cumplen condiciones
- Los filtros pueden ser por **valor**, **condición numérica** o **texto**
- Combinar ordenar y filtrar te permite encontrar información específica rápidamente
- Los datos deben ser **precisos y consistentes** para que el análisis sea confiable

---

El día de la Feria de la Madera, el stand de "Mendoza & Hijos" lucía impecable. Sofía había impreso el catálogo ordenado, con secciones claras y precios visibles. Cuando los clientes preguntaban por un producto específico, ella buscaba en su laptop y encontraba la información en segundos.

—¿Tienen mesas de comedor de cedro? —preguntó una señora elegante.

Sofía aplicó un filtro: Categoría = Comedor, Material = Cedro, Calidad = A. Encontró dos opciones en menos de cinco segundos.

—Sí, tenemos dos modelos —respondió con seguridad—. Le muestro las fotos y los precios.

Al final del día, Don Manuel se acercó con dos tazas de café.

—¿Sabes cuántos pedidos tomamos hoy? —preguntó.

—¿Cuántos?

Don Manuel mostró la libreta: doce pedidos. Más de los que Don Rafael solía tomar en un mes completo.

—Mija —dijo, con los ojos brillantes—, tu abuelo estaría orgulloso.

Sofía sonrió y miró el cielo anaranjado del atardecer. La Feria de la Madera había sido un éxito. Y el legado de su abuelo seguía vivo.
