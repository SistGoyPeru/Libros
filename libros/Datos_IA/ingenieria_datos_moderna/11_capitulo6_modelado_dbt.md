# Capítulo 6: Modelado en dbt — Sources, Ref y Materializaciones

## El flujo de trabajo en dbt

```
Sources (tablas raw) ──► Staging (limpieza) ──► Intermediate (lógica) ──► Marts (negocio)
```

dbt fomenta un pipeline modular:

1. **Sources**: define las tablas de origen
2. **Staging**: modelos 1:1 con las fuentes — limpieza ligera
3. **Intermediate**: lógica de negocio, joins, agregaciones
4. **Marts**: tablas listas para BI (hechos y dimensiones)

## Staging models

Un staging model por cada tabla fuente. Limpieza mínima:

```sql
-- models/staging/stg_products.sql
{{ config(materialized='view') }}

SELECT
    product_id,
    TRIM(name) AS product_name,
    category,
    ROUND(unit_price, 2) AS unit_price,
    COALESCE(stock, 0) AS stock
FROM {{ source('techstore', 'products') }}
```

### Staging conventions

```sql
-- models/staging/stg_customers.sql
SELECT
    customer_id,
    TRIM(name) AS customer_name,
    LOWER(TRIM(email)) AS email,
    TRIM(city) AS city,
    TRIM(country) AS country,
    CAST(registration_date AS DATE) AS registration_date
FROM {{ source('techstore', 'customers') }}
```

## Intermediate models

Lógica de negocio y joins entre staging models:

```sql
-- models/intermediate/int_order_details.sql
{{ config(materialized='view') }}

SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.total,
    o.status,
    oi.product_id,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS line_total
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_order_items') }} oi ON o.order_id = oi.order_id
```

```sql
-- models/intermediate/int_customer_metrics.sql
{{ config(materialized='view') }}

SELECT
    o.customer_id,
    COUNT(DISTINCT o.order_id) AS total_pedidos,
    SUM(o.total) AS total_ingresos,
    AVG(o.total) AS ticket_promedio,
    MIN(o.order_date) AS primera_compra,
    MAX(o.order_date) AS ultima_compra,
    JULIANDAY(MAX(o.order_date)) - JULIANDAY(MIN(o.order_date)) AS dias_entre_compras
FROM {{ ref('stg_orders') }} o
GROUP BY o.customer_id
```

## Marts models (Hechos y Dimensiones)

### Tabla de hechos

```sql
-- models/marts/fact_orders.sql
{{ config(materialized='table') }}

SELECT
    order_id,
    customer_id,
    order_date,
    total,
    status,
    COUNT(DISTINCT product_id) AS productos_distintos,
    SUM(quantity) AS total_unidades,
    SUM(line_total) AS ingresos_brutos
FROM {{ ref('int_order_details') }}
GROUP BY 1, 2, 3, 4, 5
```

### Dimensiones

```sql
-- models/marts/dim_customers.sql
{{ config(materialized='table') }}

SELECT
    c.customer_id,
    c.customer_name,
    c.email,
    c.city,
    c.country,
    c.registration_date,
    COALESCE(m.total_pedidos, 0) AS total_pedidos,
    COALESCE(m.total_ingresos, 0) AS total_ingresos,
    COALESCE(m.ticket_promedio, 0) AS ticket_promedio
FROM {{ ref('stg_customers') }} c
LEFT JOIN {{ ref('int_customer_metrics') }} m ON c.customer_id = m.customer_id
```

```sql
-- models/marts/dim_products.sql
{{ config(materialized='table') }}

SELECT
    product_id,
    product_name,
    category,
    unit_price,
    stock
FROM {{ ref('stg_products') }}
```

### Mart analítico

```sql
-- models/marts/report_sales_overview.sql
{{ config(materialized='table') }}

SELECT
    DATE_TRUNC('month', o.order_date) AS mes,
    COUNT(DISTINCT o.order_id) AS pedidos,
    COUNT(DISTINCT o.customer_id) AS clientes_activos,
    SUM(o.total) AS ingresos,
    AVG(o.total) AS ticket_promedio,
    SUM(o.total_unidades) AS unidades_vendidas
FROM {{ ref('fact_orders') }} o
GROUP BY mes
ORDER BY mes
```

## Modelos incrementales

Para tablas grandes que se actualizan periódicamente:

```sql
-- models/marts/fact_orders_incremental.sql
{{ config(
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='merge'
) }}

SELECT
    order_id,
    customer_id,
    order_date,
    total,
    status
FROM {{ ref('stg_orders') }}

{% if is_incremental() %}
  WHERE order_date > (SELECT MAX(order_date) FROM {{ this }})
{% endif %}
```

## Dependencias y orden de ejecución

dbt resuelve el orden automáticamente según el lineage:

```
1. stg_orders, stg_customers, stg_products, stg_order_items
2. int_order_details, int_customer_metrics
3. fact_orders, dim_customers, dim_products
4. report_sales_overview
```

```bash
# Ver el DAG de dependencias
dbt run --select stg_orders+  # stg_orders + todo lo que depende de él

# Ejecutar solo marts
dbt run --select marts
```

## Schema naming

dbt puede organizar modelos en schemas separados:

```yaml
# dbt_project.yml
models:
  techstore_dbt:
    staging:
      +schema: staging
    intermediate:
      +schema: intermediate
    marts:
      +schema: marts
```

## Ejercicios

1. Crea el staging model para `stg_order_items` con `line_total` calculado
2. Crea un intermediate model `int_product_sales` que sume ventas por producto
3. Crea `dim_date` como un modelo que genere una tabla de fechas (2020-2026)
4. ¿Qué ventaja tienen los modelos incrementales frente a tablas completas?
5. Crea `fact_daily_orders` que agregue pedidos por día
6. Configura schemas separados para staging, intermediate y marts
7. Ejecuta `dbt run --select staging` y verifica que solo corre staging
8. ¿Por qué es buena práctica tener staging models 1:1 con las fuentes?
9. Crea un mart `report_top_products` con top 10 productos por ingresos
10. Usa `dbt run --select stg_orders+` y observa qué modelos se ejecutan
