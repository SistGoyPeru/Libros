# Capítulo 2: Conversando con los Datos

—De acuerdo, Copilot. Limpiemos estos datos.

Andrea aceptó la sugerencia de Copilot y comenzó el proceso de limpieza. Pero pronto se dio cuenta de que no bastaba con hacer clic en "Aceptar". Necesitaba aprender a comunicarse con la IA de manera efectiva.

El primer día fue frustrante. Andrea hacía preguntas vagas y obtenía respuestas igualmente vagas.

*"Muéstrame los datos importantes"* → Copilot le mostraba todo el archivo.

*"Dime qué está mal"* → Copilot le listaba decenas de problemas sin prioridad.

*"Arregla esto"* → Copilot no sabía a qué se refería "esto".

—Esto es como hablar con un becario muy inteligente pero sin experiencia —se quejó Andrea con Ricardo durante el almuerzo—. Sabe mucho, pero no entiende lo que necesito a menos que se lo explique con lujo de detalles.

—Pues explícaselo —respondió Ricardo, encogiéndose de hombros—. Para eso es la inteligencia artificial, no la telepatía.

Andrea se dio cuenta de que Ricardo tenía razón. Copilot no leía la mente. Necesitaba aprender a formular bien sus preguntas.

Al día siguiente, cambió su enfoque.

*"Copilot, necesito un análisis de los productos con mayor rotación en el último trimestre. Quiero saber: cuáles son los 10 productos más vendidos por cantidad, cuál es su margen de contribución, y si hay algún producto que no haya tenido ventas en los últimos 60 días."*

La respuesta fue radicalmente diferente.

*"He analizado los datos. Estos son los resultados:*

*TOP 10 PRODUCTOS MÁS VENDIDOS (Cantidad)*
*1. Laptop ProBook X1 — 1,234 unidades*
*2. Monitor UltraView 27" — 987 unidades*
*3. Teclado Mecánico RGB — 876 unidades*
*...*

*PRODUCTOS SIN VENTAS EN ÚLTIMOS 60 DÍAS*
*• Webcam HD-200 (stock: 45 unidades)*
*• Hub USB-C 7 puertos (stock: 123 unidades)*
*• Cargador Solar 20W (stock: 67 unidades)*
*...*

*Márgenes de contribución disponibles en la tabla adjunta.*

*¿Te gustaría que genere una alerta automática para los productos sin ventas?"*

Andrea sonrió. Eso era exactamente lo que necesitaba.

Esa semana aprendió una lección fundamental: Copilot no entiende lo que no le dices. Pero cuando le das el contexto adecuado y le preguntas con precisión, puede hacer cosas extraordinarias.

---

### Conceptos Clave: El Arte de Conversar con Copilot

La clave para aprovechar Copilot al máximo está en cómo formulas tus preguntas. A esto se le llama **ingeniería de prompts**.

#### Los 6 Componentes de un Buen Prompt

1. **Contexto**: Explica el escenario. ¿Qué estás analizando? ¿Para qué?
2. **Objetivo**: ¿Qué quieres lograr? Sé específico.
3. **Formato**: ¿Cómo quieres la respuesta? ¿Tabla? ¿Gráfico? ¿Lista?
4. **Detalles**: Columnas, filtros, condiciones, criterios.
5. **Ejemplo**: Si es posible, da un ejemplo de lo que esperas.
6. **Restricciones**: ¿Hay algo que debas evitar?

#### Ejemplos de Prompts

❌ *Débil:* "Analiza las ventas"
✅ *Fuerte:* "Analiza las ventas del último trimestre por región, mostrando solo las regiones que superaron los $100,000 en ventas totales. Ordena los resultados de mayor a menor."

❌ *Débil:* "Haz un gráfico"
✅ *Fuerte:* "Crea un gráfico de barras apiladas que muestre las ventas mensuales por categoría de producto para el año 2026. Incluye leyenda y títulos."

❌ *Débil:* "Busca errores"
✅ *Fuerte:* "Detecta valores atípicos en la columna 'Precio Unitario' usando el método de rango intercuartil (IQR). Muéstrame solo los valores que están por debajo del percentil 5 o por encima del percentil 95."

#### Verbos Útiles para Prompts

| Verbo | Uso | Ejemplo |
|-------|-----|---------|
| Analiza | Exploración general | "Analiza la tendencia de ventas" |
| Calcula | Operación numérica | "Calcula el promedio móvil de 30 días" |
| Muestra | Visualización | "Muestra los datos como tabla dinámica" |
| Compare | Comparación | "Compara el rendimiento Q2 vs Q3" |
| Detecta | Anomalías | "Detecta registros duplicados" |
| Genera | Creación | "Genera un dashboard de KPIs" |
| Explica | Interpretación | "Explica por qué bajaron las ventas en mayo" |
| Sugiere | Recomendación | "Sugiere mejoras para optimizar el inventario" |

---

### Ejercicio 2.1: Reformula tus Preguntas

Toma una pregunta vaga que le hayas hecho a Copilot y reformúlala usando los 6 componentes del prompt. Por ejemplo:

*Vaga:* "Muéstrame los datos de ventas"
*Mejorada:* "Contexto: Soy analista financiero. Objetivo: Necesito revisar las ventas del mes pasado. Formato: Tabla con columnas Producto, Cantidad, Precio, Total. Detalles: Solo incluir productos con más de 100 unidades vendidas. Orden: Por total de mayor a menor."

### Ejercicio 2.2: Prompt por Turnos

Copia este prompt y pruébalo con Copilot:

*"Eres un asistente de análisis de datos para el departamento financiero. Necesito un informe ejecutivo de las ventas del último trimestre. El informe debe incluir: (1) ventas totales por mes, (2) producto más vendido de cada mes, (3) comparación contra el trimestre anterior. Presenta los resultados en una tabla con formato claro."*

¿Obtuviste lo que esperabas? Ajusta el prompt y vuelve a intentarlo.
