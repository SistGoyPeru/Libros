# Checkpoint 3: Dashboard Cloud de Ventas TechStore

## Objetivo

Has aprendido SQL analítico en BigQuery, data pipelines con Python y Looker Studio. Ahora es momento de integrar todo: **crear un dashboard profesional en Looker Studio** conectado a BigQuery, con múltiples páginas, filtros interactivos y campos calculados.

## Requisitos

- Dataset `techstore` migrado a BigQuery (Checkpoint 2 completado)
- Cuenta de Looker Studio (lookerstudio.google.com)
- Conexión a BigQuery configurada

## Paso 1: Preparar las consultas base

Crea una **consulta personalizada** en Looker Studio que sirva como fuente principal del dashboard. Esta consulta debe devolver datos limpios y enriquecidos:

```sql
-- Vista principal del dashboard
SELECT
  o.order_id,
  o.order_date,
  o.status,
  o.total,
  EXTRACT(YEAR FROM o.order_date) AS anio,
  EXTRACT(MONTH FROM o.order_date) AS mes,
  FORMAT_DATE('%Y-%m', o.order_date) AS anio_mes,
  EXTRACT(QUARTER FROM o.order_date) AS trimestre,
  EXTRACT(DAYOFWEEK FROM o.order_date) AS dia_semana,
  FORMAT_DATE('%A', o.order_date) AS nombre_dia_semana,
  c.customer_id,
  c.name AS customer_name,
  c.city,
  c.country,
  c.email,
  e.employee_id,
  e.name AS employee_name,
  e.position AS employee_position
FROM techstore.orders AS o
JOIN techstore.customers AS c ON o.customer_id = c.customer_id
JOIN techstore.employees AS e ON o.employee_id = e.employee_id
WHERE o.order_date >= '2023-01-01'
```

Además, crea una segunda consulta para el detalle de productos:

```sql
-- Vista de productos por pedido
SELECT
  oi.order_id,
  oi.product_id,
  p.name AS product_name,
  p.category,
  p.supplier,
  oi.quantity,
  oi.unit_price,
  (oi.quantity * oi.unit_price) AS line_total,
  o.order_date,
  o.customer_id
FROM techstore.order_items AS oi
JOIN techstore.products AS p ON oi.product_id = p.product_id
JOIN techstore.orders AS o ON oi.order_id = o.order_id
WHERE o.order_date >= '2023-01-01'
```

## Paso 2: Diseñar la estructura del dashboard

Crea un informe con **4 páginas**:

### Página 1: Resumen Ejecutivo
- **Título**: "TechStore — Panel de Ventas"
- **KPIs** (tarjetas de puntuación): Ingresos totales, Pedidos, Ticket promedio, Clientes únicos
- **Gráfico**: Serie temporal de ingresos mensuales
- **Gráfico**: Top 10 productos más vendidos (barras horizontales)
- **Filtro**: Selector de fecha (a nivel de informe)

### Página 2: Análisis Geográfico
- **Gráfico**: Mapa de ventas por ciudad
- **Gráfico**: Barras con top 10 ciudades
- **Tabla**: Detalle de ventas por país/ciudad
- **Filtro**: Desplegable de país

### Página 3: Rendimiento por Vendedor
- **Gráfico**: Barras apiladas de ingresos por vendedor
- **Gráfico**: Evolución mensual por vendedor (líneas múltiples)
- **Tabla**: Rankings de vendedores
- **Filtro**: Desplegable de vendedor

### Página 4: Detalle de Productos
- **Gráfico**: Torta de ingresos por categoría
- **Tabla pivotante**: Categoría × Mes (ingresos)
- **Gráfico**: Dispersión (precio unitario vs cantidad vendida)
- **Campo calculado**: Margen estimado (precio * 0.4) como columna adicional

## Paso 3: Implementar campos calculados

Crea estos campos calculados en tu fuente de datos:

```text
// Ticket promedio (manual)
Ingreso por pedido
SUM(total)

// Día de la semana (texto)
FORMAT_DATETIME('%A', order_date)

// Mes (texto corto)
FORMAT_DATETIME('%b %Y', order_date)

// Categoría de ticket
CASE
  WHEN total >= 1000 THEN 'Alto'
  WHEN total >= 500 THEN 'Medio'
  ELSE 'Bajo'
END

// Trimestre fiscal
CONCAT('Q', CAST(EXTRACT(QUARTER FROM order_date) AS TEXT), ' - ', CAST(EXTRACT(YEAR FROM order_date) AS TEXT))
```

## Paso 4: Añadir interactividad

1. **Selector de fecha** en todas las páginas (control de rango)
2. **Desplegable de categoría** para filtrar productos
3. **Desplegable de vendedor** en página 3
4. **Filtro cruzado**: al hacer clic en un gráfico, se filtran los demás
5. **Parámetro "Objetivo mensual"** con valor por defecto $50,000
   - Campo calculado: `SUM(total) / objetivo_mensual * 100`

## Paso 5: Personalizar apariencia

1. Tema de colores corporativo (azul oscuro + naranja)
2. Logo de TechStore (opcional — puedes usar un icono)
3. Títulos descriptivos en cada gráfico
4. Formato de moneda ($) en todas las métricas de ingresos
5. Fondo blanco/límpio, sin elementos distractores

## Paso 6: Compartir y programar

1. Comparte el informe con "Cualquiera con el enlace puede ver"
2. Programa la actualización de la fuente de datos BigQuery (diaria a las 6 AM)
3. Descarga el informe como PDF

## Entregables del Checkpoint 3

Al completar este checkpoint deberías tener:

- [ ] Informe en Looker Studio con 4 páginas
- [ ] Conexión a BigQuery con 2 consultas personalizadas
- [ ] KPIs principales en la página de resumen
- [ ] Mapa geográfico funcionando
- [ ] Análisis por vendedor
- [ ] Detalle de productos con tabla pivotante
- [ ] Mínimo 3 campos calculados
- [ ] Filtros interactivos (fecha, categoría, vendedor)
- [ ] Parámetro de objetivo mensual
- [ ] Informe compartido (enlace de solo lectura)

## Preguntas de reflexión

1. ¿Cuánto tiempo te tomó crear el dashboard? ¿Qué fue lo más complejo?
2. ¿Qué información nueva descubriste sobre TechStore al ver los datos visualmente?
3. ¿Qué ventaja tiene un dashboard interactivo frente a un informe PDF estático?
4. Si tuvieras que presentar este dashboard a la dirección, ¿qué página mostrarías primero?
5. ¿Cómo mejorarías este dashboard con datos adicionales (ej: inventario, costes, devoluciones)?

¡Felicidades! Has creado tu primer dashboard cloud conectado a BigQuery. En el próximo proyecto automatizarás todo el pipeline para que se actualice sin intervención manual.
