# Checkpoint 2: Dashboard de Ventas TechStore

## Objetivo

Has aprendido Power BI Desktop, modelado de datos, visualizaciones y DAX. Ahora es momento de integrar todo: **construir un dashboard profesional de ventas para TechStore** con KPIs, gráficos interactivos y formato condicional.

## Requisitos

- Power BI Desktop instalado
- Star schema de TechStore conectado (techstore_bi.db o CSVs)
- Modelo con relaciones creadas
- Medidas DAX básicas definidas

## Paso 1: Modelo y relaciones

Verifica que tu modelo tenga:
- `dim_date` conectada a `fact_orders` por `date_sk` (*:1)
- `dim_customer` conectada a `fact_orders` por `customer_sk` (*:1)
- `dim_employee` conectada a `fact_orders` por `employee_sk` (*:1)
- `dim_product` conectada a `fact_order_items` por `product_sk` (*:1)
- `fact_orders` conectada a `fact_order_items` por `order_sk` (1:*)
- Jerarquía en dim_date: Año → Trimestre → Mes → Fecha

## Paso 2: Medidas DAX

Crea estas medidas en una carpeta "KPIs":

```dax
-- ===== KPIs Principales =====

Ingresos Totales = SUM(fact_orders[total])
Total Pedidos = COUNTROWS(fact_orders)
Ticket Promedio = AVERAGE(fact_orders[total])
Clientes Activos = DISTINCTCOUNT(fact_orders[customer_sk])

Ingresos Mes Anterior = 
CALCULATE(
    [Ingresos Totales],
    PREVIOUSMONTH(dim_date[full_date])
)

Crecimiento % = 
DIVIDE(
    [Ingresos Totales] - [Ingresos Mes Anterior],
    [Ingresos Mes Anterior],
    0
)

% vs Target = 
DIVIDE([Ingresos Totales], 150000, 0)

-- ===== KPIs de Producto =====

Unidades Vendidas = SUM(fact_order_items[quantity])
Productos Distintos = DISTINCTCOUNT(fact_order_items[product_sk])
Ingresos por Producto = SUM(fact_order_items[line_total])

-- ===== KPIs de Cliente =====

Ticket Promedio por Cliente = 
DIVIDE([Ingresos Totales], [Clientes Activos], 0)

Pedidos por Cliente = 
DIVIDE([Total Pedidos], [Clientes Activos], 0)

-- ===== KPIs de Tiempo =====

Ingresos YTD = 
TOTALYTD([Ingresos Totales], dim_date[full_date])

Ingresos por Trimestre = 
CALCULATE(
    [Ingresos Totales],
    DATESQTD(dim_date[full_date])
)

-- ===== Medidas de Formato =====

Semáforo Crecimiento = 
SWITCH(
    TRUE(),
    [Crecimiento %] >= 0.05, 1,
    [Crecimiento %] >= 0, 2,
    3
)
```

## Paso 3: Páginas del dashboard

### Página 1: Resumen Ejecutivo

Diseño:

```
┌──────────────────────────────────────────────────────────────┐
│  TechStore Analytics    Última actualización: [fecha]        │
├────────────┬────────────┬────────────┬────────────┬──────────┤
│  Tarjeta   │  Tarjeta   │  Tarjeta   │  Tarjeta   │ Medidor  │
│  Ingresos  │  Pedidos   │  Ticket    │  Clientes  │ vs Target│
│  $2.45M    │  7,850     │  $312      │  1,250     │ 98%      │
├────────────┴────────────┴────────────┴────────────┴──────────┤
│ ┌───────────────────────────────────┐  ┌──────────────────┐  │
│ │ Ingresos Mensuales (líneas)       │  │ Ventas por       │  │
│ │ (línea con pronóstico)            │  │ Categoría (torta)│  │
│ └───────────────────────────────────┘  └──────────────────┘  │
│ ┌───────────────────────────────────┐  ┌──────────────────┐  │
│ │ Top 10 Productos (barras horiz.)  │  │ Ventas por       │  │
│ │                                   │  │ Empleado (barra) │  │
│ └───────────────────────────────────┘  └──────────────────┘  │
├──────────────────────────────────────────────────────────────┤
│  [Slicer Año]  [Slicer Trimestre]  [Slicer Categoría]        │
└──────────────────────────────────────────────────────────────┘
```

### Página 2: Detalle de Ventas

- Matriz: Categoría × Mes (con formato condicional)
- Tabla: Top 20 productos (con barra de progreso)
- Gráfico de dispersión: Precio vs Cantidad vendida
- Mapa: Ventas por ciudad (si tienes datos de ubicación)

### Página 3: KPIs por Empleado

- Gráfico de barras: Ingresos por empleado
- Tabla: métricas detalladas por empleado
- Segmentación por empleado (desplegable)
- Tarjetas: Top performer, promedio del equipo

## Paso 4: Formato y estilo

1. Tema: utiliza la paleta de colores estándar
2. Títulos descriptivos en cada visual
3. Formato condicional en la matriz (colores de fondo)
4. Tooltips personalizados
5. Marca de agua o logo de TechStore

## Paso 5: Interactividad

1. Todas las segmentaciones deben afectar a todos los gráficos
2. Al hacer clic en una categoría en la torta, se filtran los demás gráficos
3. Drill-through desde el Top 10 al detalle del producto
4. Botones para navegar entre páginas

## Entregables del Checkpoint 2

- [ ] Archivo TechStore_BI.pbix con 3 páginas de dashboard
- [ ] Mínimo 12 medidas DAX creadas y funcionando
- [ ] Modelo con relaciones correctas (star schema)
- [ ] Formato condicional en matriz
- [ ] Segmentaciones interactivas
- [ ] Tooltips personalizados
- [ ] Drill-through configurado
- [ ] KPIs principales visibles en la página de resumen

## Preguntas de reflexión

1. ¿Qué KPI crees que es más útil para la gerencia de TechStore?
2. ¿Qué filtros (slicers) son imprescindibles en un dashboard de ventas?
3. ¿Cómo mejorarías este dashboard con datos adicionales?
4. ¿Qué medida DAX fue la más compleja de implementar?

¡Felicidades! Has construido tu primer dashboard profesional en Power BI. En el Proyecto 3 profundizarás en DAX avanzado y Power Query.
