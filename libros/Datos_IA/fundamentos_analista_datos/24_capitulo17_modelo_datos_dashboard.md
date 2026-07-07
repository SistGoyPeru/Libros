# Capítulo 17: Modelo de Datos y Dashboard Profesional

## Modelado dimensional

El modelado dimensional organiza los datos en **hechos** (métricas) y **dimensiones** (contexto). Es el estándar en business intelligence.

```
Dimensión Cliente ─────┐
                       │
Dimensión Fecha ───────┤─── Tabla de Hechos (Ventas) ──── Dashboard
                       │
Dimensión Producto ────┘
```

En Power Pivot / Power BI:
- **Tabla de hechos**: `ventas` (order_id, customer_id, product_id, date_id, cantidad, precio, total)
- **Dimensiones**: `clientes`, `productos`, `calendario`

## Construir el modelo en Power Pivot

1. Carga las siguientes tablas en Power Pivot:
   - `datos_detalles_ventas.csv` (hechos)
   - `datos_productos.csv` (dimensión)
   - `datos_clientes.csv` (dimensión)
   - Crea una tabla `calendario` con CALENDAR

2. Crea relaciones:

| Tabla origen | Columna | Tabla destino | Columna |
|-------------|---------|---------------|---------|
| detalles_ventas | customer_id | clientes | id |
| detalles_ventas | product_id | productos | id |
| detalles_ventas | order_date | calendario | fecha |

## Medidas DAX para el dashboard

```dax
-- KPIs principales
Ventas Totales = SUM(detalles_ventas[line_total])
Pedidos = DISTINCTCOUNT(detalles_ventas[order_id])
Clientes Activos = DISTINCTCOUNT(detalles_ventas[customer_id])
Productos Vendidos = DISTINCTCOUNT(detalles_ventas[product_name])
Ticket Promedio = DIVIDE([Ventas Totales], [Pedidos])
Unidades Vendidas = SUM(detalles_ventas[quantity])

-- Métricas de comparación
Ventas Año Anterior = CALCULATE(
    [Ventas Totales],
    SAMEPERIODLASTYEAR(calendario[fecha])
)
Crecimiento % = DIVIDE(
    [Ventas Totales] - [Ventas Año Anterior],
    [Ventas Año Anterior]
)

-- Ventas por categoría
Ventas Portátiles = CALCULATE(
    [Ventas Totales],
    productos[category_name] = "Portátiles"
)

-- Ranking de productos
Top Productos = TOPN(10, productos, [Ventas Totales])
```

## Diseño del dashboard profesional

Un dashboard debe responder 3 preguntas en 3 segundos:

1. **¿Cómo vamos?** (KPIs principales)
2. **¿Qué está pasando?** (tendencias, comparativas)
3. **¿Qué debo hacer?** (insights, alertas)

### Layout recomendado

```
┌─────────────────────────────────────────────────┐
│  TECHSTORE - DASHBOARD DE VENTAS                │
├──────────┬──────────┬──────────┬─────────────────┤
│ Ventas   │ Pedidos  │ Clientes │ Ticket Promedio │
│ €1.2M    │ 5,250    │ 245      │ €228           │
│ vs PY +12%│         │          │                 │
├──────────┴──────────┴──────────┴─────────────────┤
│  ┌──────────────────────┐  ┌──────────────────┐  │
│  │ Ventas por Región    │  │ Ventas Mensuales │  │
│  │ (Gráfico de barras)  │  │ (Gráfico línea)  │  │
│  └──────────────────────┘  └──────────────────┘  │
├──────────────────────────────────────────────────┤
│  ┌──────────────────────┐  ┌──────────────────┐  │
│  │ Top 5 Productos      │  │ Ventas por       │  │
│  │ (Gráfico barras)     │  │ Categoría (pastel)│  │
│  └──────────────────────┘  └──────────────────┘  │
└──────────────────────────────────────────────────┘
```

## Crear el dashboard paso a paso

1. En Power Pivot, crea las medidas del dashboard
2. Inserta tablas dinámicas y gráficos dinámicos
3. Conecta todos los elementos a los mismos segmentadores
4. Organiza en una hoja "Dashboard"

### Segmentadores compartidos

1. Crea un segmentador de año (de la tabla calendario)
2. Crea un segmentador de región (de la tabla clientes)
3. Conecta cada segmentador a todas las tablas dinámicas:
   - Haz clic derecho en el segmentador
   - "Conexiones de informes"
   - Selecciona todas las tablas dinámicas

## Formato profesional

### Tarjetas KPI

1. Crea una tabla dinámica con una sola celda para cada KPI
2. Formatea el número grande (18-24pt)
3. Añade la etiqueta debajo
4. Añade formato condicional: verde si crecimiento > 0, rojo si < 0

### Colores

```excel
KPI positivo: #00B050 (verde)
KPI negativo: #FF0000 (rojo)
Fondo dashboard: #F2F2F2 (gris claro)
Gráficos: paleta azul corporativo
```

### Reglas de diseño

1. **Máximo 5 KPIs** en la fila superior
2. **Máximo 4 gráficos** en el cuerpo
3. **Mismo tipo de gráfico** = mismo color
4. **Ordena los datos** de mayor a menor en barras
5. **Elimina leyendas** si solo hay una serie
6. **Títulos descriptivos**: "Ventas por Región (2025)" no "Gráfico 1"

## Validación del dashboard

Antes de compartir, pregúntate:

1. **Total correcto**: ¿Suma todas las regiones el total general?
2. **Filtros**: ¿Funcionan todos los segmentadores?
3. **Consistencia**: ¿Coinciden los números con los del reporte anterior?
4. **Rendimiento**: ¿Tarda mucho en actualizar?
5. **Claridad**: ¿Lo entendería alguien que no sabe de datos?

## Ejercicios del Capítulo 17

1. Carga las tablas en Power Pivot y crea las relaciones correctas.
2. Crea una tabla de calendario con CALENDAR para el rango 2023-2026.
3. Crea las medidas: Ventas Totales, Pedidos, Clientes Activos, Ticket Promedio.
4. Crea una medida de crecimiento interanual.
5. Diseña un layout de dashboard con 4 KPIs arriba y 4 gráficos abajo.
6. Crea un gráfico de ventas por región (barras) y otro de tendencia mensual (línea).
7. Conecta segmentadores de año y región a todos los elementos.
8. Aplica formato condicional a los KPIs (verde/rojo según crecimiento).
9. Añade una tabla de Top 10 productos más vendidos.
10. Valida el dashboard: comprueba que los totales coinciden con SQL.

## Checklist de autoevaluación

- [ ] Entiendo el modelo dimensional (hechos y dimensiones)
- [ ] Sé crear relaciones entre tablas en Power Pivot
- [ ] Sé crear medidas DAX para KPIs
- [ ] Sé diseñar un dashboard con layout profesional
- [ ] Sé conectar segmentadores a múltiples elementos
- [ ] Sé aplicar formato condicional y colores corporativos
- [ ] Sé validar un dashboard antes de compartirlo
