# Capítulo 9: DAX Avanzado — Time Intelligence y CALCULATE

## CALCULATE en profundidad

`CALCULATE` es la función más importante de DAX. Cambia el contexto de filtro de una expresión.

```dax
CALCULATE(
    expresión,       -- La medida o agregación a calcular
    filtro1,         -- Nuevo filtro a aplicar
    filtro2,         -- (Opcional) más filtros
    ...
)
```

### CALCULATE con filtros simples

```dax
Ventas Portátiles = 
CALCULATE(
    [Ingresos Totales],
    dim_product[category] = "Portátiles"
)

Ventas 2024 = 
CALCULATE(
    [Ingresos Totales],
    dim_date[anio] = 2024
)

Ventas Altas = 
CALCULATE(
    [Ingresos Totales],
    fact_orders[total] >= 500
)
```

### CALCULATE con múltiples filtros

```dax
Ventas Portátiles 2024 USA = 
CALCULATE(
    [Ingresos Totales],
    dim_product[category] = "Portátiles",
    dim_date[anio] = 2024,
    dim_customer[country] = "USA"
)
```

### CALCULATE + FILTER

`FILTER` da control total sobre el filtro:

```dax
-- Top 10% de pedidos más caros
Ventas Top10 = 
CALCULATE(
    [Ingresos Totales],
    FILTER(
        fact_orders,
        fact_orders[total] >= PERCENTILE.INC(fact_orders[total], 0.9)
    )
)
```

## Funciones de Time Intelligence

### Acumulados

```dax
-- Year to Date (desde inicio del año hasta la fecha actual)
Ventas YTD = 
TOTALYTD([Ingresos Totales], dim_date[full_date])

-- Quarter to Date
Ventas QTD = 
TOTALQTD([Ingresos Totales], dim_date[full_date])

-- Month to Date
Ventas MTD = 
TOTALMTD([Ingresos Totales], dim_date[full_date])
```

### Comparación con periodos anteriores

```dax
-- Mes anterior
Ventas Mes Anterior = 
CALCULATE(
    [Ingresos Totales],
    PREVIOUSMONTH(dim_date[full_date])
)

-- Mismo mes del año anterior
Ventas Mismo Mes Año Anterior = 
CALCULATE(
    [Ingresos Totales],
    SAMEPERIODLASTYEAR(dim_date[full_date])
)

-- Fecha equivalente del periodo anterior
Ventas Periodo Anterior = 
CALCULATE(
    [Ingresos Totales],
    DATEADD(dim_date[full_date], -1, MONTH)
)
```

### Promedios móviles

```dax
-- Promedio móvil de 3 meses
Ventas Promedio 3M = 
CALCULATE(
    AVERAGEX(
        DATESINPERIOD(
            dim_date[full_date],
            LASTDATE(dim_date[full_date]),
            -3,
            MONTH
        ),
        [Ingresos Totales]
    )
)

-- O más simple con DATESINPERIOD
Ventas Promedio Móvil 3M = 
CALCULATE(
    [Ingresos Totales],
    DATESINPERIOD(dim_date[full_date], LASTDATE(dim_date[full_date]), -3, MONTH)
) / 3
```

### Periodo vs Periodo Anterior

```dax
Variación vs Año Anterior = 
[Ingresos Totales] - [Ventas Mismo Mes Año Anterior]

% Crecimiento Anual = 
DIVIDE(
    [Variación vs Año Anterior],
    [Ventas Mismo Mes Año Anterior],
    0
)
```

## Funciones de inteligencia de tiempo avanzadas

```dax
-- Primer y último día del mes
Primer Día Mes = STARTOFMONTH(dim_date[full_date])
Último Día Mes = ENDOFMONTH(dim_date[full_date])

-- Fechas hasta la fecha actual
Ventas Hasta Hoy = 
CALCULATE(
    [Ingresos Totales],
    DATESBETWEEN(
        dim_date[full_date],
        BLANK(),
        TODAY()
    )
)

-- Próximo periodo (para pronóstico)
Ventas Próximo Mes = 
CALCULATE(
    [Ingresos Totales],
    NEXTMONTH(dim_date[full_date])
)
```

## Context Transition

**Context Transition** ocurre cuando una medida calculada en contexto de fila se evalua en contexto de filtro. Pasa automáticamente al usar agregaciones dentro de FILTER o en columnas calculadas.

```dax
-- En columna calculada (contexto de fila)
Cada Fila = [Ingresos Totales]  
-- MAL: No funciona (medida no se puede usar en contexto de fila)

Cada Fila Correcto = 
CALCULATE([Ingresos Totales])  
-- BIEN: CALCULATE fuerza la transición de contexto
```

## ALL, ALLEXCEPT y REMOVEFILTERS

Estas funciones **eliminan** filtros del contexto.

```dax
-- Porcentaje del total general
% del Total = 
DIVIDE(
    [Ingresos Totales],
    CALCULATE([Ingresos Totales], ALL(dim_product))
)

-- Lo mismo, pero respetando filtros de fecha
% del Total (por fecha) = 
DIVIDE(
    [Ingresos Totales],
    CALCULATE([Ingresos Totales], ALLEXCEPT(dim_product, dim_date))
)

-- Cambiar el contexto de filtro
Ventas sin Filtro Fecha = 
CALCULATE([Ingresos Totales], REMOVEFILTERS(dim_date))
```

## Funciones de ranking

```dax
-- Ranking de productos por ingresos (en una tabla)
Ranking Producto = 
RANKX(
    ALL(dim_product),
    [Ingresos Totales],
    ,
    DESC,
    Dense
)

-- Top N productos
Top 5 Productos = 
CALCULATE(
    [Ingresos Totales],
    TOPN(5, ALL(dim_product), [Ingresos Totales])
)
```

## Funciones de evaluación (ITERATE)

Estas funciones operan fila por fila:

```dax
-- SUMX: suma de una expresión evaluada por fila
Ingresos por Item = 
SUMX(
    fact_order_items,
    fact_order_items[quantity] * fact_order_items[unit_price]
)

-- AVERAGEX: promedio de una expresión por fila
Ticket Promedio por Día = 
AVERAGEX(
    VALUES(dim_date[full_date]),
    [Ingresos Totales]
)

-- MAXX / MINX: encontrar máximo/mínimo por fila
Mejor Día de Ventas = 
MAXX(
    VALUES(dim_date[full_date]),
    [Ingresos Totales]
)
```

## Ejercicios

1. Usa CALCULATE para crear "Ventas de Smartphones" filtrando por categoría
2. Crea una medida YTD (Year to Date) de ingresos
3. ¿Qué hace SAMEPERIODLASTYEAR? Escribe un ejemplo
4. Crea un promedio móvil de 3 meses de ingresos
5. Usa ALL para calcular el % de cada producto sobre el total
6. Crea un ranking de categorías usando RANKX
7. ¿Qué es context transition? ¿Cuándo ocurre?
8. Usa SUMX para calcular ingresos totales desde fact_order_items
9. Crea una medida que muestre el crecimiento vs el mismo mes del año anterior
10. Usa TOPN para mostrar solo los 5 productos más vendidos
