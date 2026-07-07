# Checkpoint 2: Pipeline dbt de TechStore

## Objetivo

Construir un pipeline completo de transformación con dbt que tome los datos del data lake (bronze) y los transforme en un modelo analítico listo para BI (gold).

## Requisitos

- dbt-core + dbt-duckdb instalados (Capítulo 5)
- Data Lake con datos en bronze (Checkpoint 1)
- DuckDB como warehouse local

## Paso 1: Configurar proyecto dbt

```bash
dbt init techstore_dbt
cd techstore_dbt
```

```yml
# profiles.yml
techstore_dbt:
  outputs:
    dev:
      type: duckdb
      path: /data/techstore_gold.duckdb
      schema: main
      threads: 4
  target: dev
```

## Paso 2: Definir sources

```yml
# models/sources.yml
version: 2

sources:
  - name: bronze
    database: main
    schema: main
    tables:
      - name: orders
      - name: customers
      - name: products
      - name: order_items
```

Los datos se cargan desde Parquet usando DuckDB:

```sql
-- models/staging/stg_orders.sql
{{ config(materialized='view') }}

SELECT *
FROM read_parquet('data/bronze/orders/*.parquet')
```

## Paso 3: Staging models

```sql
-- models/staging/stg_customers.sql
{{ config(materialized='view') }}

SELECT
    customer_id,
    TRIM(name) AS customer_name,
    LOWER(TRIM(email)) AS email,
    TRIM(city) AS city,
    TRIM(country) AS country,
    CAST(registration_date AS DATE) AS registration_date
FROM read_parquet('data/bronze/customers/*.parquet')
```

```sql
-- models/staging/stg_products.sql
{{ config(materialized='view') }}

SELECT
    product_id,
    TRIM(name) AS product_name,
    category,
    ROUND(unit_price, 2) AS unit_price,
    COALESCE(stock, 0) AS stock
FROM read_parquet('data/bronze/products/*.parquet')
```

```sql
-- models/staging/stg_order_items.sql
{{ config(materialized='view') }}

SELECT
    order_id,
    product_id,
    quantity,
    unit_price,
    (quantity * unit_price) AS line_total
FROM read_parquet('data/bronze/order_items/*.parquet')
```

## Paso 4: Intermediate models

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
    oi.line_total
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_order_items') }} oi ON o.order_id = oi.order_id
```

## Paso 5: Marts models (Gold)

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

```sql
-- models/marts/dim_customers.sql
{{ config(materialized='table') }}

SELECT * FROM {{ ref('stg_customers') }}
```

```sql
-- models/marts/report_sales_daily.sql
{{ config(materialized='table') }}

SELECT
    order_date,
    COUNT(DISTINCT order_id) AS pedidos,
    COUNT(DISTINCT customer_id) AS clientes_activos,
    SUM(total) AS ingresos,
    AVG(total) AS ticket_promedio
FROM {{ ref('fact_orders') }}
GROUP BY order_date
ORDER BY order_date
```

## Paso 6: Tests

```yml
# models/schema.yml
version: 2

models:
  - name: stg_orders
    description: "Orders desde el data lake bronze"
    columns:
      - name: order_id
        tests: [unique, not_null]
      - name: total
        tests: [not_null]
      - name: status
        tests:
          - accepted_values:
              values: ['completed', 'pending', 'cancelled', 'refunded']

  - name: fact_orders
    description: "Hechos de pedidos agregados"
    columns:
      - name: order_id
        tests: [unique, not_null]
      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_customers')
              field: customer_id
```

## Paso 7: Ejecutar

```bash
# Instalar paquetes (opcional)
dbt deps

# Ejecutar todos los modelos
dbt run

# Ejecutar tests
dbt test

# Generar documentación
dbt docs generate
dbt docs serve
```

## Entregables del Checkpoint 2

- [ ] Proyecto dbt configurado con profiles.yml
- [ ] Sources definidas para datos bronze
- [ ] 4 staging models (orders, customers, products, order_items)
- [ ] 1 intermediate model (int_order_details)
- [ ] 3 marts models (fact_orders, dim_customers, report_sales_daily)
- [ ] Tests para PKs, FKs y valores aceptados
- [ ] Documentación generada (dbt docs serve)
- [ ] duckdb generado con datos gold

## Preguntas de reflexión

1. ¿Qué capa de la medallion architecture corresponde a marts? ¿Por qué?
2. ¿Cómo cambiaría el pipeline si tuviéramos 50 tablas fuente en lugar de 4?
3. ¿Qué tests adicionales agregarías para garantizar calidad de datos?
4. ¿Cómo conectarías estos datos gold a Power BI o Looker Studio?
