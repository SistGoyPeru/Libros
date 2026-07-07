# Capítulo 15: Excel — DAX y Power Pivot

## ¿Qué es DAX?

DAX (Data Analysis Expressions) es el lenguaje de fórmulas de Power Pivot, Power BI y Analysis Services. Es como las fórmulas de Excel pero mucho más potente.

Mientras que las fórmulas de Excel trabajan celda por celda, DAX trabaja sobre tablas enteras y relaciones.

## Power Pivot: el motor de análisis

Power Pivot es un motor de análisis en memoria que permite trabajar con millones de filas de múltiples orígenes.

1. "Datos" > "Administrar modelo de datos" (o "Power Pivot" > "Administrar")
2. Si no ves la pestaña Power Pivot: "Archivo" > "Opciones" > "Complementos" > Activar Power Pivot

### Cargar datos en Power Pivot

1. En Power Pivot, "Inicio" > "Obtener datos"
2. Carga `datos_ventas.csv` y `datos_productos.csv`
3. Crea relaciones entre tablas:
   - Power Pivot > "Diseño" > "Crear relación"
   - Tabla1: `ventas[product_id]`, Tabla2: `productos[id]`

## DAX vs Excel: diferencias clave

| Concepto | Excel | DAX |
|----------|-------|-----|
| Contexto | Celda actual | Fila actual + filtros |
| Tablas | Rangos de celdas | Tablas con relaciones |
| Filtros | Manual | Automático por contexto |
| Resultado | Una celda | Puede ser una tabla |

## Medidas vs Columnas calculadas

### Columna calculada: evaluada fila por fila

Se crea en Power Pivot > "Agregar columna". Se guarda en la tabla.

```dax
= ventas[cantidad] * ventas[precio_unitario]
```

### Medida: calculada en contexto de filtro

Se crea en Power Pivot > "Nueva medida". Solo existe como agregación.

```dax
Ingresos Totales = SUMX(ventas, ventas[cantidad] * ventas[precio_unitario])
```

**Regla general**: usa columnas calculadas para valores por fila, medidas para agregaciones.

## Medidas DAX básicas

```dax
-- Medidas básicas
Total Pedidos = COUNTROWS(ventas)
Total Ingresos = SUM(ventas[total])
Ticket Promedio = AVERAGE(ventas[total])
Pedido Máximo = MAX(ventas[total])
Pedido Mínimo = MIN(ventas[total])

-- Conteo de valores distintos
Clientes Activos = DISTINCTCOUNT(ventas[customer_id])
Productos Vendidos = DISTINCTCOUNT(ventas[product_id])
```

## CALCULATE: la función más importante

`CALCULATE` cambia el contexto de filtro de una medida. Es la función más potente de DAX.

```dax
-- Ventas totales (sin filtro)
Ventas Totales = SUM(ventas[total])

-- Ventas solo de Madrid
Ventas Madrid = CALCULATE(
    SUM(ventas[total]),
    clientes[region] = "Madrid"
)

-- Ventas de productos caros (> 500€)
Ventas Productos Caros = CALCULATE(
    SUM(ventas[total]),
    productos[precio] > 500
)

-- Ventas del año 2025
Ventas 2025 = CALCULATE(
    SUM(ventas[total]),
    YEAR(ventas[fecha]) = 2025
)
```

### Múltiples filtros en CALCULATE

```dax
-- Ventas de Madrid en 2025 de productos caros
Ventas Madrid Premium = CALCULATE(
    SUM(ventas[total]),
    clientes[region] = "Madrid",
    YEAR(ventas[fecha]) = 2025,
    productos[precio] > 500
)
```

## Funciones de iteración (X functions)

SUMX, AVERAGEX, COUNTX, etc. iteran fila por fila:

```dax
-- SUMX: suma fila por fila
Margen Total = SUMX(
    ventas,
    ventas[cantidad] * (ventas[precio_unitario] - RELATED(productos[coste]))
)

-- AVERAGEX: promedio fila por fila
Ticket Promedio con Detalle = AVERAGEX(
    ventas,
    ventas[cantidad] * ventas[precio_unitario]
)
```

## Funciones de fecha y tiempo

```dax
-- Ventas del período actual
Ventas YTD = TOTALYTD(SUM(ventas[total]), calendario[fecha])
Ventas QTD = TOTALQTD(SUM(ventas[total]), calendario[fecha])
Ventas MTD = TOTALMTD(SUM(ventas[total]), calendario[fecha])

-- Ventas del mismo período año anterior
Ventas Año Anterior = CALCULATE(
    SUM(ventas[total]),
    SAMEPERIODLASTYEAR(calendario[fecha])
)

-- Crecimiento interanual
Crecimiento YoY = 
    DIVIDE(
        SUM(ventas[total]) - [Ventas Año Anterior],
        [Ventas Año Anterior]
    )
```

## RELATED: navegar relaciones

Similar a BUSCARV en Excel:

```dax
-- Acceder al precio del producto desde la tabla ventas
Precio Producto = RELATED(productos[precio])

-- Margen por línea de venta
Margen Línea = ventas[cantidad] * (ventas[precio_unitario] - RELATED(productos[coste]))
```

## Tabla de calendario

Para análisis temporales, necesitas una tabla de calendario:

```dax
Calendario = CALENDAR(
    DATE(2023, 1, 1),
    DATE(2026, 12, 31)
)
```

Luego añade columnas:

```dax
Año = YEAR(calendario[fecha])
Mes = FORMAT(calendario[fecha], "MMMM")
Mes Número = MONTH(calendario[fecha])
Trimestre = "Q" & QUARTER(calendario[fecha])
Año-Mes = FORMAT(calendario[fecha], "YYYY-MM")
```

## Medida de ejemplo: dashboard completo

```dax
-- KPIs principales
Ventas Totales = SUM(ventas[total])
Pedidos = COUNTROWS(ventas)
Ticket Promedio = AVERAGE(ventas[total])
Clientes = DISTINCTCOUNT(ventas[customer_id])

-- Ventas por región
Ventas Madrid = CALCULATE([Ventas Totales], clientes[region] = "Madrid")
% Madrid = DIVIDE([Ventas Madrid], [Ventas Totales])

-- Crecimiento
Ventas Año Anterior = CALCULATE([Ventas Totales], SAMEPERIODLASTYEAR(calendario[fecha]))
Crecimiento vs Año Ant = DIVIDE([Ventas Totales] - [Ventas Año Anterior], [Ventas Año Anterior])
```

## Ejercicios del Capítulo 15

1. Carga `datos_ventas.csv` en Power Pivot y crea una medida `Total Ventas` que sume `total`.
2. Crea una medida `Total Pedidos` que cuente filas de la tabla ventas.
3. Crea una medida `Ventas Cataluña` que calcule ventas solo de Cataluña.
4. Carga `datos_productos.csv` y relaciónala con ventas por `product_id`.
5. Crea una medida `Margen Total` usando SUMX y RELATED para obtener el coste.
6. Crea una tabla de calendario con CALENDAR para el rango 2023-2026.
7. Crea medidas de Ventas YTD y compáralas con el año anterior.
8. Crea una medida de crecimiento interanual como porcentaje.
9. Diseña un KPI card en Power Pivot o Power BI con: ventas totales, pedidos, ticket promedio.
10. Crea una medida que calcule el % de ventas de cada región sobre el total.

## Checklist de autoevaluación

- [ ] Sé cargar datos en Power Pivot
- [ ] Sé crear relaciones entre tablas
- [ ] Entiendo la diferencia entre medidas y columnas calculadas
- [ ] Sé escribir medidas DAX básicas (SUM, COUNT, AVERAGE)
- [ ] Sé usar CALCULATE para modificar contexto
- [ ] Sé usar SUMX y otras funciones de iteración
- [ ] Sé usar funciones de fecha y tiempo (YTD, SAMEPERIODLASTYEAR)
- [ ] Sé crear una tabla de calendario
