# Capítulo 9: El Presupuesto Final

## Configuración de Impresión, Diseño de Página y Vista Previa

---

La Feria de la Madera fue un punto de inflexión. Los doce pedidos que Sofía consiguió significaban trabajo para los siguientes dos meses. Pero también significaban algo más: clientes que esperaban facturas, presupuestos formales y documentos profesionales.

—Don Manuel —dijo Sofía una tarde—, necesito imprimir los presupuestos para los clientes. Pero cuando imprimo, los bordes se cortan, las columnas no encajan, y todo se ve... amateur.

Don Manuel rió.

—Tu abuelo siempre decía que un presupuesto mal presentado es como un mueble sin lijar: la gente no confía en él.

Sofía suspiró. Había dominado las fórmulas, los formatos, los gráficos y los filtros. Pero la impresión era su talón de Aquiles.

---

## Configuración de página

La pestaña **Diseño de Página** en la cinta de opciones contiene todas las herramientas para controlar cómo se verá tu hoja al imprimirse.

### Márgenes

Los márgenes son los espacios en blanco alrededor del contenido impreso.

1. Ve a **Diseño de Página > Márgenes**
2. Opciones predefinidas: Normal, Ancho, Estrecho
3. O **Márgenes personalizados...** para configurar manualmente

Sofía eligió **Estrecho** para aprovechar mejor el espacio:

| Margen | Valor |
|--------|-------|
| Superior | 1.5 cm |
| Inferior | 1.5 cm |
| Izquierdo | 1.5 cm |
| Derecho | 1.5 cm |

### Orientación

- **Vertical:** Más alto que ancho (ideal para listas)
- **Horizontal:** Más ancho que alto (ideal para tablas con muchas columnas)

La tabla de presupuesto de Sofía tenía 8 columnas, así que eligió **Horizontal**.

### Tamaño de papel

- **Carta (21.59 x 27.94 cm):** Estándar en América
- **A4 (21.0 x 29.7 cm):** Estándar en Europa y otros países
- **Oficio:** Más largo que Carta

Para clientes peruanos, Sofía usó **A4**.

---

## Área de impresión

A veces no quieres imprimir toda la hoja, solo una parte. El **Área de impresión** define qué celdas se imprimirán.

1. Selecciona el rango que quieres imprimir (ej: A1:H25)
2. Ve a **Diseño de Página > Área de impresión > Establecer área de impresión**

Sofía seleccionó solo la tabla del presupuesto, excluyendo las notas de trabajo y cálculos auxiliares que tenía en la misma hoja.

Para borrar el área de impresión: **Diseño de Página > Área de impresión > Borrar área de impresión**

---

## Saltos de página

Cuando una tabla es muy larga, Excel la divide automáticamente en varias páginas. Puedes controlar dónde ocurren los saltos:

1. Ve a **Vista > Vista previa de salto de página**
2. Verás líneas azules que indican dónde se divide la página
3. Arrastra las líneas azules para ajustar los saltos

Sofía ajustó los saltos para que cada categoría de producto (Dormitorio, Sala, Comedor) quedara completa en una sola página.

---

## Encabezados y pies de página

Los encabezados y pies de página son textos que aparecen en todas las páginas impresas. Son ideales para:

- **Encabezado:** Nombre del taller, título del documento
- **Pie de página:** Número de página, fecha, nombre del autor

1. Ve a **Insertar > Encabezado y pie de página**
2. Excel cambia a la vista **Diseño** con tres secciones: izquierda, centro, derecha

Sofía configuró:

**Encabezado (izquierda):** Mendoza & Hijos - Carpintería Fina
**Encabezado (derecha):** Presupuesto
**Pie de página (centro):** Página &[Página] de &[Páginas]
**Pie de página (derecha):** &[Fecha]

Los códigos &[Página], &[Páginas] y &[Fecha] son **variables** que Excel reemplaza automáticamente con los valores correctos.

---

## Vista previa de impresión

Antes de imprimir, siempre debes usar la **Vista previa**:

1. **Archivo > Imprimir** (o Ctrl + P)
2. En el panel derecho, ves exactamente cómo se verá la hoja impresa
3. Puedes navegar entre páginas con las flechas
4. Ajusta la configuración si es necesario

En la vista previa, Sofía notó que su tabla tenía una columna que se salía del borde derecho. Ajustó la escala:

**Configuración > Sin escala > Escalar para ajustar > Ancho de página.**

Esto redujo ligeramente el tamaño para que todo cupiera en una página horizontal.

---

## El presupuesto perfecto

Sofía creó un presupuesto modelo para el cliente más importante de la feria: la Sra. María Fernanda, que quería amueblar toda su casa.

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| **Código** | **Producto** | **Cant.** | **P. Unit.** | **Subtotal** | **Descuento** | **Total** |
| DORM-01 | Cama king cedro | 2 | 680 | 1360 | 10% | 1224 |
| DORM-02 | Mesa de noche | 4 | 120 | 480 | 10% | 432 |
| DORM-03 | Cómoda | 2 | 420 | 840 | 10% | 756 |
| SALA-01 | Sillón | 3 | 520 | 1560 | 5% | 1482 |
| SALA-02 | Mesa de centro | 1 | 250 | 250 | 5% | 237.5 |
| COMED-01 | Mesa comedor | 1 | 520 | 520 | 0% | 520 |
| COMED-02 | Silla comedor | 8 | 150 | 1200 | 0% | 1200 |

**TOTAL GENERAL:** S/ 5,851.50

Sofía configuró la impresión:

1. **Orientación:** Horizontal
2. **Márgenes:** 1.5 cm todos
3. **Área de impresión:** A1:G10 (la tabla completa más el total)
4. **Encabezado:** "Mendoza & Hijos - Presupuesto para Sra. María Fernanda"
5. **Pie de página:** "Página 1 de 1" + fecha
6. **Escala:** Ajustar a 1 página de ancho

La vista previa mostraba un documento limpio, profesional, listo para entregar.

—Esto se ve mejor que los presupuestos que me daban en las tiendas grandes —dijo Sofía orgullosa.

---

## Otros ajustes importantes

### Ajustar escala

- **Escalar para ajustar:** Reduce el tamaño para que quepa en un número específico de páginas
- **Alto:** Especifica el número de páginas de alto
- **Ancho:** Especifica el número de páginas de ancho
- **Porcentaje de escala normal:** Reduce o aumenta manualmente (100% = tamaño normal)

### Opciones de hoja

En **Diseño de Página > Opciones de hoja**:

- **Líneas de cuadrícula (imprimir):** Muestra las líneas entre celdas
- **Encabezados (imprimir):** Muestra las letras de columna y números de fila

Para un presupuesto profesional, Sofía activó las líneas de cuadrícula (para que se vean los bordes de la tabla) y desactivó los encabezados.

### Imprimir títulos

Si tu tabla ocupa varias páginas, puedes repetir las filas de encabezado en cada página:

1. **Diseño de Página > Imprimir títulos**
2. En **Filas para repetir en el extremo superior**, selecciona la fila de encabezados
3. Así, en cada página impresa aparecerán los títulos de las columnas

---

## Enigmas del Capítulo 9

### Enigma 9.1: Configura un presupuesto profesional

Crea un presupuesto para un cliente (puede ser ficticio) con al menos 8 productos. Configura la impresión así:

1. Orientación horizontal
2. Márgenes estrechos
3. Encabezado: "Taller Mendoza & Hijos" (izquierda) y tu nombre (derecha)
4. Pie de página: "Presupuesto válido por 15 días" (centro) y la fecha (derecha)
5. Escala: Ajustar a 1 página de ancho
6. Líneas de cuadrícula activadas para impresión
7. Títulos de columna repetidos en todas las páginas (si aplica)

### Enigma 9.2: Vista previa y ajustes

Toma la tabla que creaste en el Enigma 9.1 y:

1. Revisa la vista previa de impresión (Ctrl + P)
2. ¿La tabla se ve completa o está cortada?
3. Si está cortada, ajusta la escala hasta que quepa en una página
4. Prueba con orientación vertical vs horizontal. ¿Cuál funciona mejor para tu tabla?
5. Cambia los márgenes de "Normal" a "Estrecho". ¿Notas la diferencia?

### Enigma 9.3: Encabezados y pies creativos

Configura el encabezado y pie de página con la siguiente información:

**Encabezado:**
- Izquierda: "Mendoza & Hijos"
- Centro: "EXCEL BÁSICO - Ejercicio Práctico"
- Derecha: "Cliente: [nombre del cliente]"

**Pie de página:**
- Izquierda: "Página &[Página]"
- Centro: "Documento generado electrónicamente"
- Derecha: "&[Fecha] &[Hora]"

Observa cómo Excel reemplaza &[Página], &[Fecha] y &[Hora] con valores reales.

### Enigma 9.4: El presupuesto definitivo

Combina todo lo aprendido en el libro hasta ahora:

1. Crea una hoja con el inventario de materiales (del Capítulo 1)
2. Agrega fórmulas para calcular el costo total (Capítulo 3)
3. Agrega el IVA con referencia absoluta (Capítulo 4)
4. Aplica formato de moneda y colores (Capítulo 5)
5. Agrega funciones SUM y AVERAGE para totales (Capítulo 6)
6. Configura la impresión profesional (Capítulo 9)

Imprime o exporta a PDF. El resultado debe verse como un documento empresarial real.

---

## Lo que aprendiste

- La pestaña **Diseño de Página** controla la apariencia al imprimir
- Los **márgenes** definen el espacio en blanco alrededor del contenido
- La **orientación** puede ser vertical u horizontal
- El **área de impresión** define qué parte de la hoja se imprime
- Los **encabezados y pies de página** agregan información consistente a todas las páginas
- La **vista previa** (Ctrl + P) muestra el resultado antes de imprimir
- **Escalar** ajusta el tamaño para que quepa en el número deseado de páginas
- Un documento bien presentado genera confianza en los clientes

---

Sofía imprimió el presupuesto para la Sra. María Fernanda y lo puso en un folder de cartulina color marfil, con el logo del taller.

—Don Manuel —dijo—, ¿sabe qué es lo mejor de todo?

—¿Qué, mija?

—Que cuando la Sra. María Fernanda vea este presupuesto, no va a pensar que se lo hizo una diseñadora gráfica que aprendió Excel hace dos meses. Va a pensar que se lo hizo una profesional.

Don Manuel sonrió, y sus ojos se humedecieron ligeramente.

—Tu abuelo no solo te dejó un taller. Te dejó las herramientas para ser lo que tú quieras ser.

Sofía guardó el presupuesto en su bolso. Al día siguiente lo entregaría personalmente. Pero esa noche, al cerrar la computadora, sintió que había cruzado una línea invisible. Ya no era una principiante asustada frente a una hoja de cálculo. Ahora sabía lo que hacía.

Y el taller de su abuelo estaba en las mejores manos posibles.
