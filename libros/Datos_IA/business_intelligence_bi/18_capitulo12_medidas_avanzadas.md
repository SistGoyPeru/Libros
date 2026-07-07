# Capítulo 12: Medidas Avanzadas y KPIs Dinámicos

## KPIs dinámicos con segmentaciones

Los KPIs dinámicos cambian según la selección del usuario. Para lograrlo, necesitas tablas de parámetros y medidas inteligentes.

### Tabla de parámetros

Crea una tabla desconectada (no relacionada con el modelo):

```dax
Tabla KPIs = 
DATATABLE(
    "KPI", STRING,
    "Orden", INTEGER,
    "Descripción", STRING,
    {
        {"Ingresos Totales", 1, "Suma de todos los ingresos"},
        {"Total Pedidos", 2, "Número total de pedidos"},
        {"Ticket Promedio", 3, "Ingreso promedio por pedido"},
        {"Clientes Activos", 4, "Clientes que compraron"},
        {"Crecimiento %", 5, "Variación vs mes anterior"}
    }
)
```

### Medida genérica que cambia según selección

```dax
KPI Seleccionado = 
SWITCH(
    SELECTEDVALUE('Tabla KPIs'[KPI]),
    "Ingresos Totales", [Ingresos Totales],
    "Total Pedidos", [Total Pedidos],
    "Ticket Promedio", [Ticket Promedio],
    "Clientes Activos", [Clientes Activos],
    "Crecimiento %", [Crecimiento %],
    BLANK()
)
```

### Matriz dinámica con KPIs

Usa la tabla de parámetros como filas de una matriz y la medida genérica como valor:

```
Filas: Tabla KPIs[KPI]
Columnas: dim_date[anio], dim_date[mes]
Valores: [KPI Seleccionado]
```

El usuario ve todos los KPIs en una sola matriz sin necesidad de múltiples gráficos.

## Segmentación de fecha dinámica

```dax
Tabla Periodos = 
DATATABLE(
    "Periodo", STRING,
    "Días", INTEGER,
    {
        {"Últimos 7 días", -7},
        {"Últimos 30 días", -30},
        {"Últimos 90 días", -90},
        {"Últimos 12 meses", -365},
        {"Todo el histórico", -9999}
    }
)
```

```dax
Ventas Periodo Dinámico = 
VAR dias = SELECTEDVALUE('Tabla Periodos'[Días], -30)
RETURN
CALCULATE(
    [Ingresos Totales],
    DATESINPERIOD(
        dim_date[full_date],
        LASTDATE(dim_date[full_date]),
        dias,
        DAY
    )
)
```

## KPIs con formato condicional avanzado

```dax
-- Medida que devuelve el formato del semáforo
Formato KPI = 
SWITCH(
    TRUE(),
    [Crecimiento %] >= 0.05, "verde",
    [Crecimiento %] >= 0, "amarillo",
    "rojo"
)

-- En formato condicional, usas reglas basadas en campo
-- 1. Selecciona la medida
-- 2. Formato condicional → Color de fondo → Formato por: "Formato KPI"
```

## Forecasting con DAX

Power BI no tiene forecasting nativo en DAX, pero puedes simular tendencias:

```dax
-- Tendencia lineal simple
Pronóstico Próximo Mes = 
VAR ultimo_mes_con_datos = LASTNONBLANK(dim_date[full_date], [Ingresos Totales])
VAR ultimo_valor = CALCULATE([Ingresos Totales], ultimo_mes_con_datos)
VAR promedio_ultimos_3 = 
    CALCULATE(
        AVERAGEX(
            DATESINPERIOD(dim_date[full_date], ultimo_mes_con_datos, -3, MONTH),
            [Ingresos Totales]
        )
    )
VAR tendencia = ultimo_valor - promedio_ultimos_3
RETURN ultimo_valor + tendencia
```

## What-If Analysis

Power BI admite análisis What-If con parámetros:

1. "Modelado" → "Nuevo parámetro"
2. Nombre: "Descuento %", Tipo: Decimal, Rango: 0 a 0.5, Incremento: 0.05
3. Se crea una tabla `Descuento` y una medida `Descuento[Valor]`

```dax
Ingresos con Descuento = 
[Ingresos Totales] * (1 - [Valor Descuento])

Impacto Descuento = 
[Ingresos Totales] - [Ingresos con Descuento]
```

Agrega un slicer con el parámetro para que el usuario ajuste el descuento.

## Medidas de Pareto (80/20)

```dax
% Acumulado Producto = 
VAR total_general = CALCULATE([Ingresos Totales], ALL(dim_product))
VAR ingresos_producto = [Ingresos Totales]
VAR productos_mayores = 
    FILTER(
        ALL(dim_product),
        [Ingresos Totales] >= ingresos_producto
    )
VAR suma_mayores = 
    CALCULATE([Ingresos Totales], productos_mayores)
RETURN DIVIDE(suma_mayores, total_general, 0)

Es Pareto 80 = 
IF([% Acumulado Producto] <= 0.8, "80%", "20%")
```

## Medidas de cohortes

```dax
-- Primera compra del cliente
Primera Compra Cliente = 
CALCULATE(
    MIN(dim_date[full_date]),
    ALLEXCEPT(dim_customer, dim_customer[customer_sk])
)

-- Mes de cohorte (para análisis de cohortes)
Mes Cohorte = FORMAT([Primera Compra Cliente], "YYYY-MM")
```

## Tarjetas con indicadores

```dax
Tarjeta Ingresos con Indicador = 
VAR ingresos_actuales = [Ingresos Totales]
VAR ingresos_anteriores = [Ingresos Mes Anterior]
VAR variacion = ingresos_actuales - ingresos_anteriores
VAR icono = IF(variacion >= 0, UNICHAR(9650), UNICHAR(9660))  -- ▲ o ▼
VAR color = IF(variacion >= 0, "verde", "rojo")
RETURN
    ingresos_actuales & " " & icono & " " & FORMAT(variacion, "$#,##0")
```

## Biblioteca de medidas útiles

```dax
-- ===== Medidas para cualquier modelo BI =====

% Penetración = 
DIVIDE(
    DISTINCTCOUNT(fact_orders[customer_sk]),
    COUNTROWS(dim_customer),
    0
)

Frecuencia Compra = 
DIVIDE(
    [Total Pedidos],
    [Clientes Activos],
    0
)

Ticket por Cliente = 
DIVIDE(
    [Ingresos Totales],
    [Clientes Activos],
    0
)

Días Desde Última Venta = 
VAR ultima_venta = 
    CALCULATE(
        MAX(dim_date[full_date]),
        ALL(dim_date)
    )
RETURN DATEDIFF(ultima_venta, TODAY(), DAY)

Ingreso Promedio por Día = 
DIVIDE(
    [Ingresos Totales],
    COUNTROWS(dim_date),
    0
)
```

## Ejercicios

1. Crea una tabla de parámetros "KPIs" con 5 KPIs seleccionables
2. Crea una medida "KPI Seleccionado" que cambie según el parámetro
3. Implementa un análisis What-If con un parámetro de descuento
4. ¿Cómo harías un análisis de Pareto (80/20) en DAX?
5. Crea un indicador de tarjeta con ▲/▼ y color según tendencia
6. Crea una medida de cohorte (primera compra por cliente)
7. ¿Qué es una tabla desconectada? ¿Para qué sirve?
8. Implementa una segmentación de fecha dinámica (últimos 7, 30, 90 días)
9. Crea una medida de "Frecuencia de Compra" (pedidos / cliente)
10. Diseña una matriz dinámica que muestre todos los KPIs por mes
