# Capítulo 11: Data Warehousing y Modelo Estrella en Power BI

## Del star schema al modelo semántico

El modelo estrella que construiste en el Proyecto 1 es la base. En Power BI, este modelo se convierte en un **modelo semántico** que define cómo los consumidores interactúan con los datos.

## Tablas de hechos: diseño fino

### Granularidad correcta

Elige la granularidad adecuada para cada tabla de hechos:

| Tabla | Granularidad | Medidas | Filas aprox |
|-------|-------------|---------|-------------|
| fact_orders | 1 fila = 1 pedido | total, item_count | 6,000 |
| fact_order_items | 1 fila = 1 línea de pedido | quantity, unit_price, line_total | ~15,000 |
| fact_daily_orders | 1 fila = 1 día | pedidos, ingresos | ~1,100 |
| fact_monthly_summary | 1 fila = 1 mes + 1 cat | ingresos, unidades | ~200 |

**NW**: no crees tablas de hechos resumidas si los datos caben en RAM. El motor de Power BI comprime muy bien los datos detallados.

### Medidas vs columnas en fact tables

```dax
-- Columna en fact_order_items (calculada en ETL)
line_total = [quantity] * [unit_price]

-- Medida en Power BI (calculada en consulta)
Ingresos por Producto = SUMX(fact_order_items, [quantity] * [unit_price])
```

**Recomendación**: calcula `line_total` en Power Query (columna) para velocidad, pero usa medidas para lógica de negocio compleja.

## Tablas de dimensión: enriquecimiento

### Añadir columnas derivadas

```dax
-- En dim_date (columnas calculadas)
Año-Mes = dim_date[anio] & "-" & FORMAT(dim_date[mes], "00")
Trimestre Nombre = "Q" & dim_date[trimestre] & " " & dim_date[anio]
Es Finde Semana = IF(dim_date[es_fin_semana] = 1, "Sí", "No")

-- En dim_customer
Segmento Cliente = 
SWITCH(
    TRUE(),
    dim_customer[city] IN ("New York", "Los Angeles", "Chicago"), "Metrópolis",
    dim_customer[city] IN ("Miami", "Houston", "Phoenix"), "Gran Ciudad",
    "Otras Ciudades"
)
```

### Dimensiones Role-Playing

Una misma dimensión puede cumplir múltiples roles. Ejemplo: `dim_date` usada como fecha de pedido, fecha de envío, fecha de pago.

En Power BI: crea copias de la tabla con diferentes nombres:

```dax
-- Crea una copia de dim_date (sin cargar datos duplicados)
dim_date_envío = dim_date  -- Role-playing dimension
dim_date_pago = dim_date   -- Role-playing dimension
```

Luego relaciona cada copia con la columna correspondiente en fact_orders.

## Tablas de calendario completas

Una buena tabla de calendario debe cubrir:

```sql
-- Calendario fiscal (para empresas con año fiscal no calendario)
-- Ejemplo: año fiscal de TechStore empieza en Octubre
SELECT
    full_date,
    anio,
    CASE WHEN mes >= 10 THEN anio + 1 ELSE anio END AS anio_fiscal,
    CASE WHEN mes >= 10 THEN mes - 9 ELSE mes + 3 END AS mes_fiscal,
    (CASE WHEN mes >= 10 THEN (mes - 10) / 3 + 1 ELSE (mes + 2) / 3 + 1 END) AS trimestre_fiscal,
    ...
FROM dim_date;
```

## Modelo de datos avanzado para TechStore

```
dim_date ──────┐
               │
dim_customer ──┼── fact_orders ──── fact_order_items ──── dim_product
               │                        │
dim_employee ──┘                        │
                                  dim_category (snowflake opcional)
```

### Agregar tablas auxiliares

```dax
-- Tabla de objetivos (importada de Excel)
Objetivos Mensuales =
  UNION(
    ROW("Año", 2024, "Mes", 1, "Objetivo", 130000),
    ROW("Año", 2024, "Mes", 2, "Objetivo", 135000),
    ...
  )

-- Medida: cumplimiento vs objetivo
% Cumplimiento =
DIVIDE(
    [Ingresos Totales],
    SUM(Objetivos_Mensuales[Objetivo]),
    0
)
```

## Rendimiento del modelo

### Estrategias de optimización

1. **Elimina columnas innecesarias** en Power Query
2. **Usa tipos de datos correctos** (entero vs decimal, fecha vs texto)
3. **Agrupa datos de alta cardinalidad** (ej: combinar ciudades pequeñas en "Otras")
4. **Deshabilita auto-date/time** (Archivo → Opciones → Carga de datos)
5. **Usa agregaciones precalculadas** para tablas muy grandes

### Cardinalidad y compresión

Power BI comprime mejor columnas con:
- **Baja cardinalidad**: categorías, estados (pocos valores únicos)
- **Datos ordenados**: ordena por la columna de alta cardinalidad
- **Enteros vs texto**: los enteros comprimen mejor

```powerquery
// En Power Query: ordenar por clave para mejor compresión
= Table.Sort(fact_orders, {{"date_sk", Order.Ascending}})
```

## Working with Multiple Fact Tables

A veces tienes múltiples tablas de hechos (ventas, inventario, marketing). Comparten dimensiones conformadas:

```
dim_date ──── fact_orders
dim_date ──── fact_inventory
dim_date ──── fact_marketing_spend

dim_product ── fact_order_items
dim_product ── fact_inventory
```

Las medidas de diferentes hechos se pueden combinar siempre que compartan dimensiones.

## Ejercicios

1. Agrega una columna "Año-Mes" (formato "2024-01") a dim_date
2. Crea una dimensión role-playing para fecha de envío
3. ¿Qué es una tabla de calendario fiscal? ¿Cómo la crearías?
4. Importa una tabla de objetivos mensuales desde Excel
5. Crea una medida de % Cumplimiento vs Objetivo
6. ¿Cómo optimizarías el rendimiento de un modelo con 50M de filas?
7. ¿Qué columnas eliminarías de fact_orders para mejorar compresión?
8. Crea una tabla de agregación mensual (fact_monthly_summary)
9. ¿Cuál es la ventaja de las dimensiones conformadas?
10. Diseña un modelo con 2 tablas de hechos (ventas + inventario)
