# Capítulo 10: Visualizaciones que Impactan

## 10.1 El Problema de los Malos Gráficos

El 90% de los dashboards que veo son decorativos, no funcionales. Tienen colores bonitos pero no responden preguntas de negocio.

**Un buen gráfico responde una pregunta específica en menos de 3 segundos.**

## 10.2 Principios de Visualización Efectiva

### 10.2.1 Menos es más

Las reglas de visualización efectiva son: elimina todo lo que no aporte información (gridlines, fondos, 3D, sombras); reduce la paleta de colores (máximo 6 colores, usa escalas secuenciales); un gráfico, una historia (no mezcles 3 métricas en un solo chart); etiqueta directamente sobre los datos, no en leyendas separadas; y ordena los datos (el ojo lee de arriba a abajo, de izquierda a derecha).

### 10.2.2 El tipo de gráfico correcto

| Qué quieres mostrar | Gráfico recomendado |
|---------------------|---------------------|
| Comparación entre categorías | Barras |
| Tendencia en el tiempo | Líneas |
| Composición del total | Barras apiladas (no pie charts) |
| Correlación entre dos variables | Scatter plot |
| Distribución de una variable | Histograma |
| Ranking | Barras horizontales ordenadas |
| Parte del todo (>4 categorías) | Treemap (no pie charts) |
| Evolución + comparación | Líneas + barras combinado |

## 10.3 Colores que Funcionan

### 10.3.1 Paletas recomendadas

Se recomiendan tres paletas de colores: **corporativa** (azul, verde, rojo, amarillo, cian, morado); **segura** (verde oscuro, turquesa, amarillo, naranja, terracota); y **accesible para daltónicos** (azul, celeste, naranja, rojo, verde azulado).

### 10.3.2 Nunca uses

- Gráficos 3D
- Pie charts (con más de 3 categorías)
- Colores neón o brillantes
- Fondo oscuro (excepto para presentaciones en escenario)
- Más de 6 colores en un solo gráfico

## 10.4 Visualizaciones que Impactan

### 10.4.1 El dashboard que vende

Un dashboard que tus clientes amen tiene:

1. **Título claro**: "Dashboard de Ventas 2025" no. "¿Estamos cumpliendo el presupuesto?" sí.
2. **Jerarquía visual**: Lo más importante primero, grande, arriba a la izquierda.
3. **Contexto**: Comparativas con período anterior, targets, benchmarks.
4. **Interactividad**: Filtros, drill-down, tooltips informativos.
5. **Llamado a la acción**: ¿Qué debe hacer el cliente al ver esto?

### 10.4.2 Anotaciones que marcan la diferencia

Las anotaciones efectivas incluyen: flecha con texto en el punto más alto (ej. "Máximo histórico"); línea vertical en una fecha clave (ej. "Lanzamiento de campaña"); círculo en una anomalía (ej. "Posible error en datos"); y texto explicativo junto al gráfico, no en una nota al pie.

## 10.5 Herramientas de Visualización

| Herramienta | Mejor para | Precio freelancer |
|-------------|------------|-------------------|
| **Power BI** | Dashboards interactivos | Gratuito Desktop |
| **Tableau** | Visualizaciones avanzadas | 75$/mes (Tableau Creator) |
| **Python (matplotlib/seaborn)** | Gráficos estáticos para informes | Gratuito |
| **Streamlit** | Dashboards con Python interactivo | Gratuito |
| **Observable (D3.js)** | Visualizaciones custom | Gratuito (community) |
| **Datawrapper** | Gráficos para web embedidos | Gratuito |
| **Flourish** | Visualizaciones animadas | Gratuito (públicas) |


