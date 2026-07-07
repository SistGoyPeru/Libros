# Capítulo 10: Excel — Visualización con Gráficos

## Por qué visualizar datos

Un gráfico bien diseñado comunica en segundos lo que una tabla tarda minutos en explicar. Como analista, tu trabajo no termina con los números; terminas cuando comunicas el mensaje.

## Gráfico de columnas: comparar categorías

Ideal para comparar valores entre categorías.

1. Crea una tabla dinámica con ventas por región
2. Selecciona los datos
3. "Insertar" > "Gráfico de columnas"
4. Elige "Columna agrupada 2D"

```excel
Tip: ordena los datos de mayor a menor antes de graficar
```

### Personalizar el gráfico

1. **Título**: haz doble clic y escribe "Ventas por Región 2025"
2. **Colores**: "Formato" > "Relleno de forma" > elige un color corporativo
3. **Etiquetas de datos**: haz clic derecho > "Agregar etiquetas de datos"
4. **Eje vertical**: ajusta el mínimo si es necesario

## Gráfico de líneas: mostrar tendencias

Perfecto para evolución temporal.

1. Crea una tabla dinámica con ventas por mes
2. "Insertar" > "Gráfico de líneas"
3. Elige "Línea 2D con marcadores"

```excel
Línea con marcadores: muestra puntos de datos + línea de tendencia
```

### Añadir línea de tendencia

1. Haz clic derecho en la línea
2. "Agregar línea de tendencia"
3. Elige "Lineal" o "Media móvil"
4. Muestra la ecuación R² si quieres

## Gráfico circular: mostrar proporciones

Usa con moderación. Solo para mostrar partes de un todo (máximo 5-6 categorías).

1. Crea una tabla dinámica con ventas por categoría
2. "Insertar" > "Gráfico circular"
3. Elige "Circular 2D"

```excel
Tip: usa "Explosión" para destacar una categoría
```

## Gráfico de barras: comparar horizontalmente

Cuando las etiquetas son largas, las barras horizontales son más legibles.

1. Crea una tabla dinámica con productos y ventas
2. "Insertar" > "Gráfico de barras"
3. Ordena de mayor a menor para mejor legibilidad

## Combinar gráficos: dos ejes

Cuando tienes dos métricas con escalas diferentes (ej: ingresos en € y número de pedidos):

1. Selecciona los datos (ingresos y pedidos por mes)
2. "Insertar" > "Gráfico de columnas"
3. Haz clic derecho en la serie de pedidos > "Cambiar tipo de gráfico" > "Línea"
4. Marca "Eje secundario" para la línea

## Gráficos desde una tabla dinámica

Los gráficos dinámicos se actualizan automáticamente cuando filtras:

1. Selecciona cualquier celda de la tabla dinámica
2. "Insertar" > "Gráfico dinámico"
3. Los segmentadores afectan tanto a la tabla como al gráfico

## Formato profesional de gráficos

### Colores corporativos

```excel
Azul oscuro: #1F4E79
Azul medio: #2E75B6
Azul claro: #9DC3E6
Naranja: #ED7D31
Gris: #A5A5A5
```

### Consejos de diseño

1. **Elimina el ruido visual**: quita líneas de cuadrícula si no son necesarias
2. **Usa etiquetas directas**: mejor que leyendas si hay pocos datos
3. **Consistencia de color**: mismo color = misma categoría en todos los gráficos
4. **Título descriptivo**: "Ventas por Región (2025)" no "Gráfico 1"
5. **Fuente legible**: mantén el tamaño mínimo en 10pt

## Dashboard en una hoja

Combina varios gráficos en una sola hoja para crear un dashboard:

1. Crea 3-4 tablas dinámicas en hojas separadas
2. Crea gráficos para cada una
3. Copia los gráficos a una hoja nueva llamada "Dashboard"
4. Conecta todos a los mismos segmentadores
5. Organiza visualmente: KPIs arriba, gráficos principales al centro

## Ejercicios del Capítulo 10

Usa `datos_ventas.csv` para todos los ejercicios.

1. Crea un gráfico de columnas con ventas totales por región.
2. Crea un gráfico de líneas con la evolución mensual de ventas (agrupa por fecha).
3. Crea un gráfico circular con la distribución de pedidos por estado.
4. Crea un gráfico de barras con las 10 ciudades con más ventas.
5. Combina ingresos y número de pedidos en un gráfico de doble eje.
6. Añade una línea de tendencia al gráfico de ventas mensuales.
7. Personaliza los colores de un gráfico con la paleta corporativa sugerida.
8. Crea un gráfico dinámico conectado a una tabla dinámica con segmentador de región.
9. Diseña un dashboard en una hoja con: ingresos por región (columnas), tendencia mensual (líneas), y distribución por estado (circular).
10. Exporta un gráfico como imagen (clic derecho > "Guardar como imagen").

## Checklist de autoevaluación

- [ ] Sé crear gráficos de columnas, líneas, circulares y barras
- [ ] Sé personalizar títulos, colores y etiquetas
- [ ] Sé añadir líneas de tendencia
- [ ] Sé crear gráficos de doble eje
- [ ] Sé crear gráficos dinámicos conectados a tablas dinámicas
- [ ] Sé diseñar un dashboard básico con múltiples gráficos
- [ ] Aplico principios de diseño profesional a mis gráficos
