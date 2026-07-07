# Capítulo 8: dbt Avanzado — Jinja, Macros y Paquetes

## Jinja en dbt

dbt usa **Jinja** (templating engine de Python) para hacer tus modelos SQL dinámicos y reutilizables.

```sql
-- Sin Jinja: hay que escribir cada columna manualmente
SELECT
    order_id,
    customer_id,
    order_date,
    total,
    status
FROM raw_orders
WHERE order_date >= '2024-01-01' AND order_date < '2024-02-01'

-- Con Jinja: parámetros y bucles
{% set start_date = '2024-01-01' %}
{% set end_date = '2024-02-01' %}

SELECT
    {% for col in ['order_id', 'customer_id', 'order_date', 'total', 'status'] %}
    {{ col }}{% if not loop.last %},{% endif %}
    {% endfor %}
FROM raw_orders
WHERE order_date >= '{{ start_date }}' AND order_date < '{{ end_date }}'
```

## Variables de configuración

```sql
-- dbt_project.yml
vars:
  start_date: '2024-01-01'
  end_date: '2024-12-31'
  revenue_target: 1000000
```

```sql
-- models/marts/report_dashboard.sql
SELECT
    DATE_TRUNC('month', order_date) AS mes,
    COUNT(*) AS pedidos,
    SUM(total) AS ingresos,
    SUM(total) / {{ var('revenue_target') }} * 100 AS pct_cumplimiento
FROM {{ ref('fact_orders') }}
WHERE order_date >= '{{ var('start_date') }}'
  AND order_date <= '{{ var('end_date') }}'
GROUP BY mes
```

## Macros (funciones reutilizables)

```sql
-- macros/dates.sql
{% macro date_range_sql(start_date, end_date) %}
  WHERE order_date >= '{{ start_date }}' AND order_date <= '{{ end_date }}'
{% endmacro %}

-- Uso
SELECT ... FROM {{ ref('fact_orders') }} {{ date_range_sql('2024-01-01', '2024-06-30') }}
```

### Macro para columnas comunes

```sql
-- macros/columns.sql
{% macro generate_surrogate_key(columns) %}
  MD5(CONCAT(
    {% for col in columns %}
      COALESCE(CAST({{ col }} AS VARCHAR), ''){% if not loop.last %} || '-' || {% endif %}
    {% endfor %}
  ))
{% endmacro %}

-- Uso
SELECT
    {{ generate_surrogate_key(['order_id', 'product_id']) }} AS order_item_sk,
    ...
FROM {{ ref('int_order_details') }}
```

### Macro de logging

```sql
-- macros/logging.sql
{% macro log_info(message) %}
  {{ log("[INFO] " ~ message, info=True) }}
{% endmacro %}

{% macro log_warning(message) %}
  {{ log("[WARN] " ~ message, info=True) }}
{% endmacro %}
```

## Hooks (eventos)

Los hooks ejecutan SQL antes o después de modelos:

```yaml
# dbt_project.yml
models:
  techstore_dbt:
    +pre-hook:
      - "DELETE FROM {{ this }} WHERE 1=0"  # Para cargas completas antes de insert
    +post-hook:
      - "INSERT INTO audit_log (model, run_at, rows_affected) VALUES ('{{ this.name }}', CURRENT_TIMESTAMP, (SELECT COUNT(*) FROM {{ this }}))"
```

## Paquetes (dbt packages)

Los paquetes son bibliotecas reutilizables de macros y modelos:

```yml
# packages.yml
packages:
  - package: dbt-labs/dbt_utils
    version: ">=1.0.0"
  - package: dbt-labs/codegen
    version: ">=0.12.0"
  - package: calogica/dbt_expectations
    version: ">=0.8.0"
```

```bash
dbt deps  # Instalar paquetes
```

### Ejemplos con dbt_utils

```sql
-- dbt_utils: pivot table
SELECT *
FROM {{ dbt_utils.pivot('status',
    dbt_utils.get_column_values(ref('stg_orders'), 'status'),
    agg='COUNT',
    prefix='orders_'
) }}

-- Equivalente a PIVOT en SQL dinámico
```

```sql
-- dbt_utils: surrogate key
SELECT
    {{ dbt_utils.generate_surrogate_key(['customer_id', 'order_date']) }} AS customer_day_sk,
    ...
```

### Codegen: generar modelos automáticamente

```bash
# Generar staging models desde una fuente existente
dbt run-operation generate_source --args '{"schema_name": "main", "database_name": "main"}'

# Generar documentación base
dbt run-operation generate_docs
```

## dbt Exposures

Los **exposures** documentan cómo se usan tus modelos downstream (BI tools, dashboards):

```yml
# models/exposures.yml
version: 2

exposures:
  - name: dashboard_ventas
    type: dashboard
    url: https://app.powerbi.com/...
    description: "Dashboard de ventas ejecutivo en Power BI"
    depends_on:
      - ref('fact_orders')
      - ref('dim_customers')
      - ref('report_sales_overview')
    owner:
      name: Alex Goyzueta
      email: alex@techstore.com

  - name: reporte_mensual
    type: analysis
    url: https://lookerstudio.google.com/...
    description: "Reporte mensual de KPIs"
    depends_on:
      - ref('report_sales_overview')
```

## dbt Snapshot (SCD Tipo 2)

Los snapshots capturan cambios históricos en dimensiones lentas (SCD2):

```sql
-- snapshots/customers_snapshot.sql
{% snapshot customers_snapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='customer_id',
        strategy='check',
        check_cols=['email', 'city', 'country'],
        invalidate_hard_deletes=True,
    )
}}

SELECT * FROM {{ source('techstore', 'customers') }}

{% endsnapshot %}
```

```bash
dbt snapshot  # Ejecuta los snapshots
```

## Buenas prácticas avanzadas

1. **Usa `dbt_utils`** para no reinventar la rueda
2. **Macros para lógica repetitiva**: no copies SQL, crea macros
3. **Variables para configuraciones**: fechas, umbrales, targets
4. **Hooks para auditoría**: registra cuándo se ejecutó cada modelo
5. **Snapshots para SCD2**: solo cuando necesites historia de cambios
6. **Exposures para documentar uso downstream**

## Ejercicios

1. Crea una macro `generate_timestamp_key` que genere una SK con timestamp + rand
2. Usa `dbt_utils.surrogate_key` para crear una SK en `fact_orders`
3. Instala el paquete `dbt_utils` y usa `dbt_utils.date_spine` para generar fechas
4. Crea un hook que registre en una tabla `audit_log` cada ejecución
5. Define una variable `revenue_target` y úsala en un modelo
6. Crea una exposure para tu dashboard Power BI
7. Usa `codegen` para generar un staging model automáticamente
8. ¿Qué ventaja tiene usar macros frente a SQL repetitivo?
9. Crea un snapshot SCD2 para `products`
10. ¿Por qué los packages son importantes en dbt?
