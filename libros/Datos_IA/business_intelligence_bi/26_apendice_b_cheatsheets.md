# Apéndice B: Cheatsheets

## DAX — Medidas

```dax
// ===== Agregaciones =====
SUM(tabla[columna])
AVERAGE(tabla[columna])
COUNTROWS(tabla)
DISTINCTCOUNT(tabla[columna])
MIN(tabla[columna])
MAX(tabla[columna])

// ===== Filtros =====
CALCULATE(medida, filtro1, filtro2, ...)
FILTER(tabla, condición)
ALL(tabla)          // Quita todos los filtros
ALLEXCEPT(tabla, col)  // Quita todos excepto col
ALLSELECTED(tabla)  // Quita filtros excepto externos
KEEPFILTERS(tabla)  // Intersecta filtros
REMOVEFILTERS(tabla)    // Elimina filtros

// ===== Time Intelligence =====
TOTALYTD(medida, fecha)
TOTALQTD(medida, fecha)
TOTALMTD(medida, fecha)
SAMEPERIODLASTYEAR(fecha)
DATEADD(fecha, -1, YEAR)
DATESINPERIOD(fecha, fin, -30, DAY)
DATESMTD(fecha)
DATESQTD(fecha)
DATESYTD(fecha)
PREVIOUSMONTH(fecha)
PREVIOUSQUARTER(fecha)
PREVIOUSYEAR(fecha)
PARALLELPERIOD(fecha, -1, MONTH)

// ===== Lógica =====
IF(condición, valor_sí, valor_no)
SWITCH(expr, val1, res1, val2, res2, ... default)
SWITCH(TRUE(), cond1, res1, cond2, res2, ... default)
AND(a, b)
OR(a, b)
NOT(condición)

// ===== Iteradores =====
SUMX(tabla, expresión)
AVERAGEX(tabla, expresión)
COUNTX(tabla, expresión)
MAXX(tabla, expresión)
MINX(tabla, expresión)
RANKX(tabla, medida)
FILTER(tabla, condición)  // Filtra filas
ADDCOLUMNS(tabla, "col", expr)  // Agrega columna

// ===== Variables =====
VAR nombre = expresión
RETURN resultado

// ===== Relaciones =====
RELATED(dim[col])     // Desde tabla actual a dimensión
RELATEDTABLE(hecho)   // Desde dimensión a hecho
USERELATIONSHIP(dim[col], hecho[col])  // Relación inactiva

// ===== Valores =====
SELECTEDVALUE(dim[col], default)
VALUES(dim[col])
DISTINCT(dim[col])
HASONEVALUE(dim[col])
ISFILTERED(dim[col])
ISCROSSFILTERED(dim[col])

// ===== Seguridad =====
USERNAME()
USERPRINCIPALNAME()
```

## Power Query M

```powerquery
// ===== Conexión =====
let
    Origen = Sql.Database("server", "db_name"),
    Tabla = Origen{[Schema="schema",Item="table"]}[Data],
    CSV = Csv.Document(File.Contents("archivo.csv"), [Delimiter=","]),
    Excel = Excel.Workbook(File.Contents("archivo.xlsx"), null, true),
    Folder = Folder.Files("C:\datos\")
in
    Tabla

// ===== Transformación =====
Table.SelectRows(tabla, each [columna] > 100)
Table.RemoveColumns(tabla, {"col1", "col2"})
Table.RenameColumns(tabla, {{"old", "new"}})
Table.TransformColumnTypes(tabla, {{"col", type number}})
Table.Sort(tabla, {{"col", Order.Descending}})
Table.Distinct(tabla)
Table.AddColumn(tabla, "nueva", each [a] * [b])
Table.ReplaceValue(tabla, "old", "new", Replacer.ReplaceText, {"col"})
Table.FillDown(tabla, {"col"})

// ===== Merge =====
Table.NestedJoin(t1, {"key"}, t2, {"key"}, "new_col", JoinKind.LeftOuter)
Table.ExpandTableColumn(tabla, "col", {"sub1", "sub2"}, {"sub1", "sub2"})
Table.Combine({t1, t2})  // Append

// ===== Fechas =====
Date.Year([fecha])
Date.Month([fecha])
Date.MonthName([fecha])
Date.Quarter([fecha])
Date.DayOfWeek([fecha])
Date.DayOfWeekName([fecha])
Date.StartOfMonth([fecha])
Date.EndOfMonth([fecha])
Date.AddDays([fecha], 30)
Duration.Days([fecha_fin] - [fecha_ini])

// ===== Texto =====
Text.Trim([col])
Text.Lower([col])
Text.Upper([col])
Text.Proper([col])
Text.Replace([col], "a", "b")
Text.Start([col], 5)
Text.End([col], 3)

// ===== Números =====
Number.Round([col], 2)
Number.Abs([col])
Number.IntegerDivide([a], [b])
Number.Mod([a], [b])
```

## SQL para BI

```sql
-- Dimensiones
SELECT DISTINCT customer_id, name, email, city
FROM customers;

-- Hechos con dimensiones
SELECT
    o.order_id,
    o.order_date,
    c.name AS customer,
    c.city,
    p.name AS product,
    p.category,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price AS line_total,
    o.total
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;

-- Agregaciones
SELECT
    c.city,
    COUNT(DISTINCT o.order_id) AS pedidos,
    SUM(o.total) AS ingresos,
    AVG(o.total) AS ticket_promedio
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY ingresos DESC;

-- Ventas por período
SELECT
    strftime('%Y', o.order_date) AS anno,
    strftime('%m', o.order_date) AS mes,
    COUNT(*) AS pedidos,
    SUM(o.total) AS ingresos
FROM orders o
GROUP BY anno, mes
ORDER BY anno, mes;
```

## Modelado Dimensional

```text
// Star Schema
┌──────────────────┐
│    dim_date      │
│ date_sk (PK)     │──┐
│ full_date        │  │
│ year, month      │  │
│ quarter, week    │  │
└──────────────────┘  │
                      │
┌──────────────────┐  │  ┌──────────────────────┐
│   dim_customer   │  │  │    fact_orders       │
│ customer_sk (PK) │──┼─►│ order_sk (PK)        │
│ name, email, city│  │  │ date_sk (FK)         │
│ country, segment │  │  │ customer_sk (FK)     │
└──────────────────┘  │  │ employee_sk (FK)     │
                      │  │ total, status        │
┌──────────────────┐  │  └──────────┬───────────┘
│   dim_employee   │  │             │
│ employee_sk (PK) │──┘             │ 1:*
│ name, region     │                │
│ role, email      │           ┌────┴──────────────────┐
└──────────────────┘           │    fact_order_items   │
                               │ item_sk (PK)          │
┌──────────────────┐           │ order_sk (FK)         │
│   dim_product    │           │ product_sk (FK)       │
│ product_sk (PK)  │──┐       │ quantity, unit_price  │
│ name, category   │  │       └───────────────────────┘
│ unit_price       │  │
└──────────────────┘  │
                      │
                      └──► Corazón del modelo
```

## Power BI Service

```text
// Publicar
Desktop → Publicar → Service

// Workspaces crean app
Workspace → Crear App → Publicar → Consumidores

// Roles en workspace
Admin:    todo
Member:   editar + publicar
Viewer:   solo ver

// RLS
Desktop:  Modelado → Administrar roles → DAX
Service:  Dataset → Seguridad nivel fila → Asignar

// Actualización
Dataset → Programar actualización → Frecuencia diaria

// Suscripciones
Informe → Suscribirse → Email + PDF adjunto
```

## Conceptos clave de BI

| Concepto | Definición |
|----------|------------|
| Star schema | Tabla de hechos + dimensiones alrededor |
| Snowflake schema | Dimensiones normalizadas en varias tablas |
| Grano | Nivel de detalle de una tabla de hechos |
| Cardinalidad | Tipo de relación (1:*, 1:1, *:*) |
| SCD | Dimensiones de cambio lento (Tipo 1, 2, 3) |
| ETL | Extract → Transform → Load |
| ELT | Extract → Load → Transform |
| MOLAP | Cubo multidimensional precalculado |
| ROLAP | Consultas directas a base relacional |
| DirectQuery | Power BI consulta origen en tiempo real |
| Import | Power BI carga datos en memoria (columna) |
| Composite | Mezcla DirectQuery + Import |
| Data Gateway | Puente entre Power BI Service y datos on-prem |
| Workspace | Contenedor de informes/datasets en Service |
| App | Pack de contenido publicado para consumidores |
