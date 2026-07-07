# Capítulo 4: El Rompecabezas Financiero

## Tema: Tablas dinámicas

---

—Ya clasifiqué los códigos del archivo secreto —dijo Sofía cuando Carlos llegó al taller—. AX son ingresos, BX son egresos, CX son transferencias entre cuentas. Pero hay más de 800 transacciones en 10 años. No puedo analizar eso fila por fila.

—Es como tener 800 piezas de un rompecabezas esparcidas en la mesa —dijo Carlos—. No puedes ver la imagen completa hasta que las organizas.

—¿Y cómo las organizo?

—Con una **tabla dinámica**. Es la herramienta más poderosa de Excel para resumir, analizar y explorar grandes volúmenes de datos.

---

## ¿Qué es una tabla dinámica?

—Una tabla dinámica no es una tabla cualquiera —explicó Carlos—. Es un **motor de análisis interactivo**. Tomas tus datos, los arrastras a diferentes áreas, y Excel los resume automáticamente.

—¿Como si hiciera los totales por mí?

—Mucho más que eso. Puedes agrupar, filtrar, cambiar filas a columnas, y ver los datos desde cualquier ángulo. Se llama "dinámica" porque puedes rotar los campos para ver la información desde diferentes perspectivas.

Carlos abrió el archivo secreto y seleccionó todo el rango de datos.

—Paso 1: Convierte los datos en **Tabla de Excel**. Selecciona el rango y presiona **Ctrl+T**. Asegúrate de que "Mi tabla tiene encabezados" esté marcado.

—¿Por qué convertirla en tabla?

—Porque si después agregas más filas, la tabla dinámica las incluirá automáticamente. Es más fácil de mantener.

Sofía lo hizo. El rango se transformó en una tabla con formato y filtros automáticos.

—Paso 2: Con el cursor dentro de la tabla, ve a **Insertar > Tabla dinámica**. Acepta el rango predeterminado y elige "Nueva hoja de cálculo".

Apareció un lienzo vacío: la **Lista de campos de tabla dinámica**.

---

## Construyendo la tabla dinámica

—Este es el corazón del asunto —dijo Carlos—. La lista de campos tiene cuatro áreas:

1. **Filtros:** Filtran toda la tabla dinámica
2. **Columnas:** Van como encabezados de columna
3. **Filas:** Van como encabezados de fila
4. **Valores:** Los datos que se van a resumir (sumar, contar, promediar, etc.)

—Arrastra "Fecha" a **Filas**, "Código" a **Columnas**, y "Valor_A" a **Valores**.

Sofía lo hizo. Inmediatamente, la tabla dinámica mostró un resumen de los valores por fecha y código.

—Pero esto sigue siendo confuso —dijo Sofía—. Hay demasiadas fechas.

—Por eso puedes **agrupar**. Haz clic derecho sobre cualquier fecha > **Agrupar**. Puedes agrupar por meses, trimestres, años.

Sofía agrupó por meses y años. La tabla se volvió mucho más clara:

| Año | Mes | AX (Ingresos) | BX (Egresos) | CX (Transferencias) |
|-----|-----|---------------|--------------|---------------------|
| 2005 | Ene | 12,450 | 8,200 | 2,000 |
| 2005 | Feb | 11,800 | 7,900 | 1,500 |
| 2005 | Mar | 13,200 | 8,500 | 2,200 |
| ... | ... | ... | ... | ... |

—Ahora veo los patrones mensuales —dijo Sofía—. Los ingresos son consistentes, alrededor de 12,000 mensuales. Pero hay meses con picos.

—¿Qué meses?

Sofía aplicó un filtro para ver solo los meses donde la suma de AX superaba 15,000. Usó el filtro de etiquetas de fila: **Filtros de etiquetas > Mayor que... > 15000**.

—Noviembre y diciembre de cada año —respondió—. Como si hubiera compras estacionales.

—O ventas estacionales. Pero recuerda que esto son ingresos, no ventas. ¿Qué más ves?

—Los egresos (BX) son ligeramente menores a los ingresos en la mayoría de meses... excepto en 2008. Mira.

Sofía señaló la pantalla. En 2008, los egresos superaban a los ingresos durante seis meses consecutivos.

—2008 fue un año difícil —dijo Carlos—. La crisis económica global. Tu abuelo me contó que estuvo a punto de cerrar el taller.

—Pero no cerró —dijo Sofía—. El archivo muestra que después de 2008, los números se recuperan.

—Exacto. Y las transferencias (CX) tienen un patrón interesante: aumentan justo antes de los meses de crisis.

---

## Segmentadores de datos

—Para hacer la tabla dinámica más interactiva, podemos agregar **segmentadores de datos** —dijo Carlos—. Son botones visuales que filtran la tabla con un solo clic.

1. Selecciona la tabla dinámica
2. Ve a **Análisis de tabla dinámica > Insertar segmentador**
3. Elige los campos que quieres como filtros: "Mes", "Año", "Código"

Aparecieron paneles con botones para cada año y mes.

—Es como un control remoto para la tabla dinámica —dijo Sofía, haciendo clic en "2008". La tabla se actualizó instantáneamente, mostrando solo ese año.

—Ahora veamos los totales generales —dijo Carlos—. Arrastra "Valor_B" y "Valor_C" también al área de Valores. Excel los agregará como nuevas columnas de resumen.

La tabla ahora mostraba:

| Año | Suma de Valor_A | Suma de Valor_B | Suma de Valor_C |
|-----|----------------|-----------------|-----------------|
| 2005 | 156,780 | 102,400 | 8,450 |
| 2006 | 168,200 | 110,500 | 9,120 |
| ... | ... | ... | ... |
| **Total general** | **1,856,400** | **1,234,500** | **98,700** |

—Un millón ochocientos mil soles en ingresos en 10 años —murmuró Sofía—. Eso es mucho más de lo que el taller facturaba.

—Exacto —dijo Carlos en voz baja—. Esto no es el taller. Es otra cosa.

---

## Más herramientas de tabla dinámica

—Las tablas dinámicas tienen muchas opciones más —continuó Carlos—:

**Cambiar el tipo de cálculo:** Haz clic derecho sobre un valor > **Configuración de campo de valor**. Puedes cambiar de SUMA a CONTAR, PROMEDIO, MAX, MIN, etc.

**Mostrar como %:** En la misma configuración, ve a la pestaña **Mostrar valores como**. Puedes mostrar el valor como porcentaje del total, porcentaje del subtotal, diferencia respecto a un período anterior, etc.

—Prueba "Mostrar valores como % del total de la fila" para ver qué porcentaje de cada año corresponde a cada tipo de código.

**Ordenar:** Haz clic derecho sobre cualquier etiqueta > **Ordenar**. Puedes ordenar por valor ascendente/descendente, no solo alfabéticamente.

**Actualizar:** Si los datos fuente cambian, la tabla dinámica **no se actualiza automáticamente**. Debes hacer clic derecho > **Actualizar**, o usar **Datos > Actualizar todo**.

---

## Tablas dinámicas con múltiples rangos

—¿Y si los datos están en diferentes hojas? —preguntó Sofía.

—Hay una función avanzada que permite combinar múltiples rangos en una sola tabla dinámica. Pero requiere usar el **Asistente para tablas dinámicas y gráficos dinámicos**, que no está visible por defecto.

Para acceder a él:
1. Presiona **Alt + D + P** (en Windows)
2. Selecciona "Varios rangos de consolidación"
3. Sigue el asistente

—Este método es útil cuando tienes datos similares en diferentes hojas o archivos —explicó Carlos—. Pero no es tan flexible como una tabla dinámica normal. Te sugiero que primero combines los datos con Power Query o consolidándolos manualmente.

---

### Enigma 4.1: Crea tu primera tabla dinámica

Usando el archivo secreto, crea una tabla dinámica que muestre:
- **Filas:** Código (AX, BX, CX, DX)
- **Valores:** Suma de Valor_A y Suma de Valor_B

¿Qué tipo de código tiene el valor total más alto? ¿Cuál tiene más registros (usa CONTAR en lugar de SUMA)?

---

### Enigma 4.2: Análisis temporal

Agrupa la tabla dinámica por trimestres y años. ¿En qué trimestre de qué año hubo más movimiento (suma de Valor_A)?

Usa la función **Agrupar** selección > **Trimestres** y **Años**.

---

### Enigma 4.3: Los valores sospechosos

Usando un segmentador de datos para el campo "Fecha", filtra solo los meses donde la suma de Valor_A sea mayor que el promedio general. ¿Cuántos meses cumplen esta condición?

Pista: usa el filtro de etiquetas de fila > Filtros de valor > Mayor que, y escribe la fórmula =PROMEDIO(tu_rango) para calcular el promedio.

---

## Lo que aprendiste

- Las **tablas dinámicas** resumen grandes volúmenes de datos en segundos
- Tienen cuatro áreas: **Filtros, Columnas, Filas, Valores**
- Se pueden **agrupar** por fechas (días, meses, trimestres, años)
- Los **segmentadores de datos** son filtros visuales interactivos
- Puedes cambiar el **tipo de cálculo** (SUMA, CONTAR, PROMEDIO, etc.)
- La opción **Mostrar valores como** permite ver porcentajes, diferencias, etc.
- Las tablas dinámicas **no se actualizan automáticamente** al cambiar los datos fuente

---

—Ya tengo una imagen más clara —dijo Sofía, mirando la tabla dinámica terminada—. Hay tres tipos de movimientos claramente diferenciados. Y una cantidad de dinero que no cuadra con la contabilidad del taller.

—¿Qué crees que sea?

—No estoy segura. Pero si el abuelo manejaba tanto dinero, tenía que haber un registro oficial en algún lado. Tal vez una cuenta bancaria que no conocíamos.

—O tal vez —dijo Carlos en voz baja— algo que no debía estar en los libros oficiales.

Sofía lo miró. —¿Qué sugieres?

—Nada todavía. Pero mañana vamos a visualizar estos datos con gráficos. Tal vez los números nos cuenten una historia que las tablas no pueden mostrar.

Mientras guardaba el archivo, Sofía notó que su mano temblaba ligeramente. El misterio se estaba volviendo más grande de lo que había imaginado. Pero también más emocionante.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
