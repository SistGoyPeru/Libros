# Capítulo 7: Visualización de Datos

## Una imagen vale 50,000 filas

—El mejor análisis del mundo —dijo Valeria— no sirve de nada si no lo comunicas bien. Y la mejor forma de comunicar datos es con gráficos.

### Principios de visualización

—Antes de hacer un gráfico —dijo Valeria—, pregúntate:

```
1. ¿Qué historia quiero contar?
2. ¿Quién va a leer esto?
3. ¿Qué acción quiero provocar?
```

### Gráfico correcto para cada análisis

| Objetivo | Tipo de gráfico |
|----------|----------------|
| Comparar categorías | Barras, columnas |
| Mostrar tendencia | Líneas |
| Composición | Pastel, anillo, apilado |
| Relación | Dispersión (XY) |
| Distribución | Histograma, caja |
| Ranking | Barras horizontales |

### Gráficos combinados

—Para mostrar dos escalas diferentes:

```
Insertar > Gráfico combinado
Serie 1: Ventas (columna, eje primario)
Serie 2: % Crecimiento (línea, eje secundario)
```

—Ideal para mostrar valor absoluto y variación.

### Líneas de referencia

—Agrega contexto a tus gráficos:

```
Clic derecho en gráfico > Agregar línea de tendencia
Clic derecho > Agregar línea de promedio
```

**Línea de meta o presupuesto:**
```
Agregar serie: Meta mensual
Formato: Línea punteada, color diferente
```

### Formato condicional en gráficos

—Resalta puntos importantes:

```
Formato del punto de datos > Relleno
Criterio: Si valor > meta -> verde, si no -> rojo
```

—O usa colores por categoría.

### Gráficos dinámicos

—Los gráficos dinámicos se actualizan con la tabla dinámica:

```
Insertar > Gráfico dinámico
Se conecta automáticamente a los segmentadores
```

### Dashboard en una hoja

—Valeria mostró cómo construir un dashboard compacto:

```
Diseño:
  [Filtros]       [KPI 1] [KPI 2] [KPI 3]
  [Gráfico Evolución]     [Gráfico Pareto]
  [Tabla Top 10]         [Minigráficos]
```

**Elementos de un dashboard analítico:**

1. **KPI principales**: 3-4 tarjetas con valor, variación y tendencia
2. **Gráfico de evolución**: Ventas, gastos o usuarios en el tiempo
3. **Gráfico de composición**: Distribución por categoría
4. **Tabla de detalle**: Top N o Bottom N
5. **Segmentadores**: Filtros interactivos

### Minigráficos avanzados

—Los minigráficos en celdas individuales:

```
Insertar > Minigráficos
Tipo: Ganancia/pérdida (muestra pérdidas en rojo)
```

—Perfecto para tablas de KPIs donde cada fila tiene su tendencia.

### Gráfico de velas (Para analistas financieros)

—Muestra apertura, cierre, máximo y mínimo:

```
Insertar > Gráfico de cotizaciones
Datos: Fecha, Máximo, Mínimo, Apertura, Cierre
```

### Enigma #7

En `codigos/c07_visualizacion/datos_visualizacion.xlsx` tienes datos de ventas, gastos y KPIs.

**Tu misión:**
1. Crea un gráfico combinado: columnas de ventas + línea de % crecimiento
2. Agrega una línea de referencia para la meta anual
3. Crea un gráfico de Pareto para los productos (barras + línea acumulada)
4. Diseña un dashboard de una hoja con: 4 KPIs, gráfico de evolución, segmentador por trimestre
5. Agrega minigráficos de tendencia en cada fila de la tabla de productos
6. El dashboard debe ser imprimible en A4