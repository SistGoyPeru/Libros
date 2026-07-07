# Capítulo 14: Looker Studio Avanzado — Parámetros, Cálculos y Filtros

## Campos calculados

Los **campos calculados** te permiten crear nuevas métricas o dimensiones usando fórmulas, sin modificar los datos en BigQuery.

### Crear un campo calculado

1. En la fuente de datos, haz clic en "Añadir un campo"
2. Escribe el nombre y la fórmula
3. El campo estará disponible en todos los gráficos

### Fórmulas básicas

```text
// Margen de beneficio (asumiendo 40% de coste)
(SUM(total) * 0.4) / SUM(total) * 100

// Ticket promedio manual
SUM(total) / COUNT(order_id)

// Descuento aplicado (si precio_original > total)
(SUM(precio_original) - SUM(total)) / SUM(precio_original) * 100

// Edad del cliente a partir de fecha
DATE_DIFF(CURRENT_DATE(), fecha_nacimiento, YEAR)

// Día de la semana
FORMAT_DATETIME('%A', order_date)

// Categorización manual
CASE
  WHEN SUM(total) >= 1000 THEN 'Alto'
  WHEN SUM(total) >= 500 THEN 'Medio'
  ELSE 'Bajo'
END
```

### Fórmulas de agregación

```text
// Promedio móvil (7 días)
SUM(SUM(total)) OVER (ORDER BY order_date ROWS 6 PRECEDING) / 7

// Diferencia vs mes anterior
SUM(total) - SUM(SUM(total)) OVER (ORDER BY order_date ROWS 1 PRECEDING)

// Porcentaje del total
SUM(total) / SUM(SUM(total)) OVER () * 100
```

## Parámetros

Los **parámetros** permiten que el usuario controle aspectos del dashboard sin modificar filtros manualmente.

### Usar parámetros para objetivos

1. "Añadir un control" → "Parámetro de entrada"
2. Nombre: `objetivo_ingresos`
3. Tipo: Número
4. Valor por defecto: `100000`

Luego crea un campo calculado que use el parámetro:

```text
// Porcentaje de cumplimiento
SUM(total) / objetivo_ingresos * 100
```

### Parámetro para top N

1. Crea un parámetro: `top_n` → Número → Valor: 10
2. En un campo calculado:

```text
// Ranking por ingresos
RANK() OVER (ORDER BY SUM(total) DESC) <= top_n
```

3. Usa este campo como filtro booleano en el gráfico

## Blending de datos

El **blending** combina datos de múltiples fuentes sin JOINs en SQL, similar a un VLOOKUP de Excel:

1. "Añadir datos" → "Combinar datos" (Blend)
2. Selecciona la fuente izquierda (ej: orders)
3. "Añadir otra fuente" (ej: customers)
4. Define la clave de unión: `customer_id`
5. Selecciona las métricas y dimensiones de cada fuente

### Blending vs JOIN en BigQuery

| Blending | JOIN SQL |
|----------|----------|
| Se configura en UI | Se escribe en SQL |
| Menos flexible | Totalmente flexible |
| Bueno para uniones simples | Necesario para transformaciones complejas |
| Limitado a 5 fuentes | Sin límite práctico |

## Filtros avanzados

### Filtros con expresiones regulares

```
REGEXP_MATCH(customer.email, '.*@gmail\\.com$')
```

### Filtros por rango dinámico

```text
// Productos con precio sobre el promedio
unit_price > AVG(unit_price)
```

### Filtros entre dashboards

Puedes pasar filtros entre páginas de un mismo informe:
1. Añade un control desplegable en la página 1
2. En la página 2, el filtro se aplica automáticamente (misma fuente de datos)

## Comunidad de conectores y visualizaciones

Looker Studio tiene una **galería de socios** con visualizaciones adicionales:

- **Gantt Chart**: cronogramas
- **Word Cloud**: nubes de palabras
- **Heatmap Calendar**: calendario de calor
- **Sankey Diagram**: flujos
- **Bullet Chart**: barras con objetivo

Para instalarlos:
1. En el informe, "Editar" → "Administrar visualizaciones adicionales"
2. Explora la galería
3. Añade las que necesites

## Optimización de dashboards con BigQuery

### Cache

Looker Studio cachea resultados de BigQuery por 12 horas por defecto. Puedes ajustar esto en la configuración de la fuente de datos.

### Consultas eficientes

- Usa agregaciones precalculadas (tablas materializadas)
- Limita el rango de fechas por defecto
- Evita conexiones directas a tablas sin resumir
- Programa actualizaciones en horas de menor coste

### Programación de informes

1. En la fuente de datos, "Programación de actualización"
2. Frecuencia: cada 4 horas, diario, semanal
3. Configura la hora para evitar picos de coste

## Ejemplo: Dashboard de rendimiento de ventas

Crea un dashboard completo con:

### Página 1: Resumen ejecutivo
- 4 tarjetas KPI (ingresos, pedidos, ticket promedio, clientes activos)
- Serie temporal de ingresos vs mes anterior
- Tabla con top 10 productos
- Mapa de ventas por ciudad

### Página 2: Análisis detallado
- Tabla pivotante (categoría × mes)
- Filtro por vendedor (empleado)
- Gráfico de barras apiladas (categoría por mes)
- Parámetro para ajustar el objetivo de ingresos

### Página 3: Cohortes y retención
- Heatmap de cohortes mensuales
- Curva de retención (clientes que repiten)
- Filtro de fecha para seleccionar período

## Ejercicios

1. Crea un campo calculado que categorice pedidos como "Pequeño", "Mediano", "Grande" según el total
2. Añade un parámetro numérico para ajustar el objetivo de ingresos
3. Usa un filtro REGEXP_MATCH para mostrar solo clientes con email corporativo
4. Crea un blend entre orders y employees para mostrar ventas por vendedor
5. ¿Qué diferencia hay entre un filtro y un parámetro en Looker Studio?
6. Añade una visualización de terceros (ej: Word Cloud o Sankey)
7. Programa la actualización diaria de tu fuente de datos BigQuery
8. Crea un campo calculado con CASE para clasificar ciudades por región
9. Usa un parámetro para que el usuario seleccione el TOP N de productos
10. Crea un dashboard de 2 páginas con filtro cruzado entre ellas
