# Capítulo 8: DAX — El Lenguaje de las Fórmulas

## ¿Qué es DAX?

**DAX** (Data Analysis Expressions) es el lenguaje de fórmulas de Power BI, Power Pivot y Analysis Services. Es similar a las fórmulas de Excel, pero diseñado para trabajar con tablas relacionales.

```
Componentes de DAX:
- Funciones: SUM, COUNT, AVERAGE, CALCULATE
- Operadores: +, -, *, /, &&
- Referencias: Tablas[Columna], Medidas
- Contexto: Filtro, Fila
```

## Sintaxis básica

```dax
NombreMedida = FUNCIÓN(Tabla[Columna])
```

```dax
Ingresos Totales = SUM(fact_orders[total])
Total Pedidos = COUNTROWS(fact_orders)
Ticket Promedio = AVERAGE(fact_orders[total])
Cliente Máximo Pago = MAX(fact_orders[total])
Primer Pedido = MIN(fact_orders[order_id])
```

## Contexto de filtro

El **contexto de filtro** es el concepto más importante en DAX. Determina qué filas se usan para el cálculo.

```
Cuando seleccionas "Portátiles" en un slicer:
- El contexto de filtro incluye solo productos con category = "Portátiles"
- SUM(fact_orders[total]) suma solo pedidos de Portátiles
- Cada visual crea su propio contexto de filtro
```

```dax
-- Esta medida cambia según el contexto de filtro
Ingresos = SUM(fact_orders[total])

-- Misma medida, diferentes contextos:
-- Sin filtros: $2.45M
-- Filtro categoría = Portátiles: $980K
-- Filtro año = 2024: $820K
```

## Funciones básicas de agregación

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `SUM` | Suma de valores | `SUM(fact_orders[total])` |
| `AVERAGE` | Promedio | `AVERAGE(fact_orders[total])` |
| `COUNT` | Cuenta valores numéricos | `COUNT(fact_orders[total])` |
| `COUNTA` | Cuenta valores no vacíos | `COUNTA(dim_customer[name])` |
| `COUNTROWS` | Cuenta filas | `COUNTROWS(fact_orders)` |
| `DISTINCTCOUNT` | Cuenta valores únicos | `DISTINCTCOUNT(fact_orders[customer_sk])` |
| `MIN` / `MAX` | Mínimo/Máximo | `MIN(fact_orders[total])` |

## Funciones de conteo

```dax
Clientes Activos = DISTINCTCOUNT(fact_orders[customer_sk])

Pedidos con Descuento = 
COUNTROWS(FILTER(fact_orders, fact_orders[total] < fact_orders[total]))

Pedidos Premium = 
COUNTROWS(FILTER(fact_orders, fact_orders[total] >= 1000))
```

## FILTER y CALCULATE (introducción)

`CALCULATE` cambia el contexto de filtro de una medida. Es la función más poderosa de DAX.

```dax
-- Ventas de Portátiles
Ventas Portátiles = 
CALCULATE(
    SUM(fact_orders[total]),
    dim_product[category] = "Portátiles"
)

-- O usando FILTER (más explícito)
Ventas Portátiles v2 = 
CALCULATE(
    SUM(fact_orders[total]),
    FILTER(dim_product, dim_product[category] = "Portátiles")
)
```

## Funciones lógicas

```dax
-- IF (condición, resultado_si, resultado_no)
Margen Estimado = 
SUM(fact_orders[total]) * IF(
    HASONEVALUE(dim_product[category]),
    0.35,
    0.40
)

-- SWITCH (múltiples condiciones)
Categoría Ticket = 
SWITCH(
    TRUE(),
    AVERAGE(fact_orders[total]) >= 1000, "Premium",
    AVERAGE(fact_orders[total]) >= 500, "Alto",
    AVERAGE(fact_orders[total]) >= 200, "Medio",
    "Bajo"
)
```

## Funciones de fecha y hora

```dax
-- Año actual
Ventas Año Actual = 
CALCULATE(
    SUM(fact_orders[total]),
    dim_date[anio] = YEAR(TODAY())
)

-- Ventas del mes actual
Ventas Mes Actual = 
CALCULATE(
    SUM(fact_orders[total]),
    dim_date[mes] = MONTH(TODAY()),
    dim_date[anio] = YEAR(TODAY())
)
```

## Funciones de relación

```dax
-- RELATED: trae un valor de la dimensión al hecho
-- (solo se usa en columnas calculadas)
Producto Categoría = RELATED(dim_product[category])

-- RELATEDTABLE: trae datos del hecho a la dimensión
-- (solo se usa en columnas calculadas)
Pedidos del Cliente = COUNTROWS(RELATEDTABLE(fact_orders))
```

## Variables en DAX

Las variables hacen las medidas más legibles y eficientes:

```dax
Margen Neto = 
VAR ingresos = SUM(fact_orders[total])
VAR coste = ingresos * 0.6
VAR margen = ingresos - coste
VAR margen_pct = DIVIDE(margen, ingresos, 0)
RETURN margen_pct
```

```dax
Crecimiento vs Mes Anterior = 
VAR mes_actual = SUM(fact_orders[total])
VAR mes_anterior = 
    CALCULATE(
        SUM(fact_orders[total]),
        PREVIOUSMONTH(dim_date[full_date])
    )
VAR variacion = mes_actual - mes_anterior
VAR variacion_pct = DIVIDE(variacion, mes_anterior, 0)
RETURN variacion_pct
```

## DIVIDE vs división directa

```dax
-- MAL: división directa (error si denominador = 0)
Margen % = SUM(fact_orders[total]) * 0.4 / SUM(fact_orders[total])

-- BIEN: DIVIDE (maneja división por cero)
Margen % = DIVIDE(SUM(fact_orders[total]) * 0.4, SUM(fact_orders[total]), 0)
```

## Buenas prácticas en DAX

1. **Usa variables** para cálculos intermedios
2. **Prefiere medidas** sobre columnas calculadas (excepto para segmentaciones)
3. **Usa DIVIDE** en lugar de / (evita errores)
4. **Nombra claramente**: "Ingresos Totales", "% Crecimiento"
5. **Agrupa medidas** en carpetas lógicas
6. **Comenta fórmulas complejas** con // comentarios

## Ejercicios

1. Crea una medida de "Ingresos Totales" usando SUM
2. Crea "Ticket Promedio" usando AVERAGE
3. Crea "Clientes Activos" usando DISTINCTCOUNT
4. ¿Qué es el contexto de filtro? Explica con un ejemplo
5. Crea una medida "Ventas Portátiles" usando CALCULATE
6. Usa variables para crear "Margen Neto" (ingresos - coste estimado)
7. Crea una medida "Crecimiento %" vs año anterior (pista: SAMEPERIODLASTYEAR)
8. ¿Cuál es la diferencia entre FILTER y CALCULATE?
9. Crea un SWITCH que clasifique pedidos en 3 categorías
10. ¿Por qué deberías preferir DIVIDE sobre la división directa?
