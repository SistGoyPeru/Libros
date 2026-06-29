# Capítulo 5: Revelaciones

## Tema: Gráficos avanzados — combinados, minigráficos, de dispersión

---

—Los números me están dando dolor de cabeza —dijo Sofía, frotándose las sienes—. Tengo las tablas dinámicas, tengo los totales, pero no puedo ver el cuadro completo. Es como tener todas las piezas del rompecabezas pero no saber cómo encajan.

—Entonces es hora de **visualizar** —respondió Carlos—. El ojo humano procesa imágenes sesenta mil veces más rápido que el texto. Un buen gráfico puede revelar en segundos lo que una tabla no muestra en horas.

—Ya sé hacer gráficos básicos. Barras, líneas, pastel.

—Eso es el nivel principiante. Para este archivo necesitamos **gráficos avanzados**: combinados, minigráficos y de dispersión.

---

## Gráfico combinado: Dos historias en una

—Quiero ver la relación entre ingresos y egresos a lo largo del tiempo —dijo Sofía—. ¿Puedo poner ambas líneas en un mismo gráfico?

—Sí, pero si las escalas son muy diferentes, una línea se va a aplanar. La solución es un **gráfico combinado** que usa dos ejes Y: uno a la izquierda y otro a la derecha.

Carlos seleccionó los datos de la tabla dinámica por años: Año, Suma de Valor_A (ingresos), Suma de Valor_B (egresos).

—Paso 1: **Insertar > Gráfico combinado > Columna agrupada - Línea en eje secundario**.

Excel creó un gráfico con las columnas de ingresos y egresos, más una línea para la diferencia.

—No necesito la diferencia ahora —dijo Sofía—. Quiero que Valor_A sean columnas y Valor_B sea una línea.

—Personalicémoslo. Haz clic derecho sobre una de las series > **Cambiar tipo de gráfico de series**. Pon Valor_A como "Columna agrupada" y Valor_B como "Línea". Marca "Eje secundario" para Valor_B.

El gráfico se transformó. Ahora mostraba:

- Columnas azules para los ingresos (eje izquierdo, de 0 a 250,000)
- Línea naranja para los egresos (eje derecho, de 0 a 200,000)

—¡Ahora veo claramente la brecha entre ingresos y egresos! —exclamó Sofía.

—Y nota algo interesante —señaló Carlos—. En 2008, la línea de egresos casi toca el tope de las columnas de ingresos. El margen de ganancia fue casi cero.

—El año de la crisis. El abuelo sobrevivió por poco.

—Ahora cambiemos los colores para que sea más intuitivo: verde para ingresos, rojo para egresos.

---

## Formato de gráficos: el arte de comunicar

—Un gráfico feo puede arruinar un buen análisis —dijo Carlos—. Dedica tiempo al formato.

**Elementos esenciales de un gráfico:**

1. **Título del gráfico:** Debe ser descriptivo. En lugar de "Valor_A y Valor_B", pon "Ingresos vs Egresos (2005-2015)"
2. **Títulos de ejes:** Explica qué representan los números
3. **Leyenda:** Identifica cada serie
4. **Etiquetas de datos:** Muestran valores específicos (opcional, úsalo con moderación)
5. **Cuadrícula:** Ayuda a leer valores, pero no debe ser intrusiva

Para agregar/quitar elementos: haz clic en el ícono **+** junto al gráfico, o ve a **Diseño > Agregar elemento de gráfico**.

—¿Y esos colores predeterminados? —preguntó Sofía señalando el azul y naranja.

—Puedes cambiarlos. Doble clic en una serie > **Formato de serie de datos > Relleno**. Elige colores de la paleta del taller, por ejemplo.

—También puedes agregar **líneas de tendencia** —continuó Carlos—. Haz clic derecho sobre la serie de ingresos > **Agregar línea de tendencia**. Puedes elegir lineal, exponencial, polinómica, etc.

La línea de tendencia lineal mostró una pendiente positiva: los ingresos del taller estaban creciendo a lo largo de los años.

—El negocio crecía —dijo Sofía—. Entonces, ¿por qué el abuelo guardaba este archivo en secreto?

---

## Minigráficos: gráficos dentro de celdas

—A veces no necesitas un gráfico enorme —dijo Carlos—. A veces necesitas una **micro-visualización** dentro de una celda. Eso son los **minigráficos**.

—¿Gráficos dentro de celdas? ¿Como las barras de datos?

—Parecido, pero más versátiles. Las barras de datos solo muestran una barra proporcional. Los minigráficos muestran **tendencias**: líneas, columnas, ganancias/pérdidas.

—Selecciona una celda vacía, por ejemplo al lado de cada año en tu tabla resumen. Ve a **Insertar > Minigráfico > Línea**.

En el cuadro de diálogo, selecciona el rango de datos para ese año (los valores mensuales).

—Arrástralo hacia abajo para crear minigráficos para cada año.

El resultado fue una columna de pequeñas líneas que mostraban la tendencia mensual de cada año.

—¡Es como un electrocardiograma del negocio! —dijo Sofía—. Puedo ver los picos y valles de cada año en segundos.

—Exactamente. Y hay tres tipos:

| Tipo | Descripción | Mejor para |
|------|-------------|------------|
| **Línea** | Línea de tendencia | Mostrar evolución en el tiempo |
| **Columna** | Barras pequeñas | Comparar magnitudes entre períodos |
| **Ganancia/Pérdida** | Barras positivas/negativas | Mostrar resultados netos |

—Los minigráficos tienen opciones en la pestaña **Diseño de minigráfico**: puedes marcar el punto más alto, el más bajo, los puntos negativos, el primer y último punto.

Sofía marcó el punto más alto de cada año con un marcador rojo.

—¿Ves? —dijo—. En casi todos los años, el pico más alto es noviembre o diciembre. Excepto en 2008, donde el pico fue en marzo.

—¿Y qué pasó en marzo de 2008?

—No lo sé... pero puedo investigarlo.

---

## Gráfico de dispersión: la correlación inesperada

—Ahora vamos a hacer algo más avanzado —dijo Carlos—. Un **gráfico de dispersión** (XY). Este gráfico no muestra la evolución en el tiempo, sino la **relación entre dos variables**.

—¿Qué variables?

—Probemos Valor_A vs Valor_C. Si hay una correlación entre ellas, podría ser una pista importante.

Carlos seleccionó las columnas Valor_A y Valor_C del archivo original, y creó un gráfico de dispersión: **Insertar > Gráfico de dispersión > Solo con marcadores**.

Apareció una nube de puntos.

—No veo un patrón claro —dijo Sofía.

—Agrega una **línea de tendencia lineal**. Haz clic derecho sobre cualquier punto > **Agregar línea de tendencia**. Marca "Presentar ecuación en el gráfico" y "Presentar el valor R cuadrado en el gráfico".

La ecuación apareció: `y = 0.035x + 12.4`, con un `R² = 0.89`

—El R cuadrado es 0.89 —dijo Carlos—. Eso significa que hay una **correlación fuerte** entre Valor_A y Valor_C. El 89% de la variación de Valor_C se explica por Valor_A.

—¿Qué significa eso en términos prácticos?

—Que Valor_C no es independiente de Valor_A. Podría ser un cálculo basado en Valor_A: un porcentaje, un impuesto, una comisión.

Sofía calculó: `67 / 1450 = 0.0462`. Aproximadamente 4.6%.

Hizo la prueba con otros pares:

| Valor_A | Valor_C | Porcentaje |
|---------|---------|------------|
| 1450 | 67 | 4.62% |
| 890 | 12 | 1.35% |
| 2340 | 89 | 3.80% |
| 3450 | 23 | 0.67% |
| 5670 | 45 | 0.79% |

—No es un porcentaje constante —observó Sofía.

—Exacto. No es un impuesto fijo ni una comisión. Es otra cosa. Algo que cambia con el tiempo o con otra variable.

—Pero la correlación es fuerte... tal vez Valor_C es una variable dependiente de Valor_A pero con otro factor. Como un costo que depende del volumen pero con descuentos por cantidad.

—Exactamente. Ahora, prueba con Valor_B vs Valor_C.

Sofía creó otro gráfico de dispersión. El R² fue de 0.23 —correlación muy baja.

—Valor_C está relacionado con Valor_A, no con Valor_B —concluyó—. Eso es una pista importante. Significa que Valor_A y Valor_C miden aspectos del mismo fenómeno, mientras que Valor_B es independiente.

—Tal vez Valor_A y Valor_C son dos caras de la misma moneda —dijo Carlos—. Y Valor_B es otra cosa completamente diferente.

---

### Enigma 5.1: Crea un gráfico combinado

Usando los datos del archivo secreto, crea un gráfico combinado que muestre:
- Columnas para la suma de Valor_A por año
- Línea con eje secundario para la suma de Valor_B por año

Personaliza colores, agrega títulos y una línea de tendencia para la serie de Valor_A.

---

### Enigma 5.2: Minigráficos de tendencia

En una tabla resumen por año, agrega minigráficos de tipo línea para mostrar la tendencia mensual de Valor_A en cada año. Marca el punto máximo de cada minigráfico con un color diferente.

¿Qué año muestra la tendencia más volátil?

---

### Enigma 5.3: Dispersión reveladora

Crea un gráfico de dispersión entre Valor_A (eje X) y Valor_B (eje Y). Agrega línea de tendencia lineal y muestra el R².

¿Qué te dice este gráfico sobre la relación entre ingresos (Valor_A) y egresos (Valor_B)?

---

## Lo que aprendiste

- Los **gráficos combinados** permiten visualizar series con escalas diferentes usando ejes secundarios
- Las **líneas de tendencia** muestran la dirección general de los datos y permiten proyectar valores futuros
- Los **minigráficos** son micro-gráficos dentro de celdas que muestran tendencias de forma compacta
- Los **gráficos de dispersión** revelan correlaciones entre variables que no son obvias en tablas
- El **R² (coeficiente de determinación)** mide qué tan bien se ajusta un modelo a los datos (0=sin correlación, 1=correlación perfecta)

---

—La correlación entre Valor_A y Valor_C es la pista más importante hasta ahora —dijo Sofía—. Si descubro qué representa Valor_C, tendré la clave del archivo.

—Hay otro detalle —dijo Carlos—. En los comentarios que encontramos, uno decía "Verificar con cuaderno azul". ¿Revisaste si hay un cuaderno azul entre las cosas de tu abuelo?

—No... pero sé dónde podría estar. En el desván, detrás del archivador, hay una caja con sus cuadernos personales. No los revisé porque pensé que eran diarios personales.

—Tal vez sea momento de revisarlos.

Sofía sintió un escalofrío. El misterio se estaba volviendo más profundo. Pero también más claro. Como si cada herramienta de Excel que aprendía fuera una llave que abría una nueva puerta.

Y la siguiente puerta era el cuaderno azul de Don Rafael.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
