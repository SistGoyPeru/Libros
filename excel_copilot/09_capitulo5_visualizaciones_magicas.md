# Capítulo 5: Visualizaciones Mágicas

La presentación ante la junta directiva fue un éxito. Diego Ventura felicitó a Andrea frente a todos.

—Andrea nos ha presentado el análisis más completo que hemos tenido en años —dijo, mostrando las tablas y gráficos que ella había preparado—. Y lo hizo en 24 horas.

Los directivos asintieron, impresionados. Pero Andrea sabía que el mérito no era solo suyo.

Después de la reunión, Ricardo se acercó.

—¿Cómo hiciste los gráficos tan rápido? El de barras apiladas, el de tendencia... parecen hechos por un diseñador profesional.

Andrea sonrió.

—Se los pedí a Copilot.

—¿En serio? —Ricardo levantó una ceja—. ¿Así nomás?

—Así nomás.

---

### La Conversación

Andrea le mostró a Ricardo cómo había funcionado:

*"Copilot, quiero crear un dashboard visual para la reunión de junta. Necesito:*

1. *Un gráfico de barras apiladas que muestre ventas por línea de producto y por mes (enero a septiembre 2026)*
2. *Un gráfico de líneas que muestre la tendencia del margen bruto mensual*
3. *Un gráfico de pastel (o anillo) con la distribución de ventas por línea*
4. *Formato condicional en la tabla de rentabilidad: verde para márgenes >25%, amarillo para 15-25%, rojo para <15%*

*Colores corporativos: azul oscuro (#1A3A5C) y celeste (#4A90D9)."*

Copilot no solo generó los gráficos. También los formateó con los colores corporativos, agregó etiquetas de datos, títulos descriptivos y una leyenda clara.

Cuando terminó, Andrea tenía un dashboard completo en menos de 15 minutos.

---

### Conceptos Clave: Visualizaciones con Copilot

Copilot puede crear prácticamente cualquier tipo de gráfico en Excel. Pero la calidad del resultado depende de la claridad de tus instrucciones.

#### Tipos de Gráficos que Copilot Puede Generar

| Tipo | Cuándo Usarlo | Prompt Ejemplo |
|------|--------------|----------------|
| Barras / Columnas | Comparar categorías | "Gráfico de barras agrupadas: ventas por región" |
| Líneas | Mostrar tendencias en el tiempo | "Gráfico de líneas: ingresos mensuales 2026" |
| Pastel / Anillo | Mostrar proporciones | "Gráfico de pastel:市场份额 por producto" |
| Barras apiladas | Mostrar composición + total | "Barras apiladas: ventas por línea y mes" |
| Dispersión | Correlación entre variables | "Dispersión: precio vs cantidad vendida" |
| Cascada | Desglose de un total | "Cascada: utilidad neta paso a paso" |
| Combinado | Dos escalas diferentes | "Combinado: barras para ventas, línea para margen%" |

#### Elementos de un Buen Prompt de Visualización

1. **Tipo de gráfico**: "Gráfico de barras apiladas"
2. **Datos a incluir**: "Columnas Mes, Línea, Ventas"
3. **Ejes**: "Eje X = Mes, Eje Y = Ventas, Leyenda = Línea"
4. **Formato**: "Colores corporativos, etiquetas, título"
5. **Filtros**: "Solo 2026, excluir devoluciones"

#### Formato Condicional con Copilot

El formato condicional es una de las características más potentes de Excel, y Copilot lo simplifica enormemente:

- *"Aplica formato condicional: colores de semáforo a la columna de margen (verde >25%, amarillo 15-25%, rojo <15%)"*
- *"Resalta en rojo las filas donde las ventas están por debajo del objetivo"*
- *"Aplica barras de datos a la columna de cantidad vendida"*
- *"Usa iconos (flechas) para mostrar la tendencia vs mes anterior"*

#### Personalización Avanzada

Puedes refinar los gráficos con instrucciones adicionales:

- *"Cambia el título a 'Ventas 2026 por Línea de Producto'"*
- *"Agrega etiquetas de datos en la parte superior de cada barra"*
- *"Mueve la leyenda a la parte inferior"*
- *"Cambia el color de la serie Laptops a naranja"*
- *"Agrega una línea de tendencia al gráfico de líneas"*

---

### Ejercicio 5.1: Crea tu Primer Dashboard

Usando un archivo con datos de ventas mensuales por categoría, pídele a Copilot:

*"Crea un dashboard con 3 gráficos:*
1. *Barras apiladas: ventas por categoría y mes*
2. *Líneas: tendencia de ventas totales mensuales*
3. *Pastel: distribución de ventas por categoría*

*Usa una combinación de colores profesional. Agrega títulos a cada gráfico. Organiza los gráficos en una sola hoja."*

### Ejercicio 5.2: Formato Condicional Narrativo

Pídele a Copilot:

*"Aplica formato condicional a la tabla de ventas:*
- *Si la venta es > $10,000, fondo verde claro*
- *Si la venta es entre $5,000 y $10,000, fondo amarillo claro*
- *Si la venta es < $5,000, fondo rojo claro*
- *Agrega barras de datos proporcionales en la columna de cantidad"*
