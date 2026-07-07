# Capítulo 7: Testing y Documentación en dbt

## Por qué testear datos

Los datos tienen errores. Siempre. dbt te permite detectarlos automáticamente:

```
Errores típicos:
- Valores nulos en columnas que no deberían ser nulas
- IDs duplicados en tablas que deben ser únicas
- Valores fuera de rango (totales negativos, fechas futuras)
- Relaciones que no se cumplen (customer_id sin customer)
```

## Schema tests (tests declarativos)

Los schema tests se definen en archivos YAML:

```yml
# models/schema.yml
version: 2

models:
  - name: stg_orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: total
        tests:
          - not_null
          - accepted_values:
              values: ["> 0"]  # Test personalizado
      - name: status
        tests:
          - accepted_values:
              values: ['completed', 'pending', 'cancelled', 'refunded']
```

### Tests integrados

```yml
# models/marts/schema.yml
version: 2

models:
  - name: fact_orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_customers')
              field: customer_id
      - name: order_date
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: "order_date <= CURRENT_DATE"

  - name: dim_customers
    columns:
      - name: customer_id
        tests:
          - unique
          - not_null
      - name: email
        tests:
          - not_null
          - unique
```

## Generic tests (tests parametrizables)

Puedes crear tus propios tests reutilizables:

```sql
-- tests/generic/test_positive_values.sql
{% test positive_values(model, column_name) %}

SELECT *
FROM {{ model }}
WHERE {{ column_name }} <= 0

{% endtest %}
```

```yml
# models/schema.yml
models:
  - name: stg_orders
    columns:
      - name: total
        tests:
          - positive_values
```

### Otros tests genéricos

```sql
-- tests/generic/test_date_in_past.sql
{% test date_in_past(model, column_name) %}

SELECT *
FROM {{ model }}
WHERE {{ column_name }} > CURRENT_DATE

{% endtest %}
```

```yml
# models/schema.yml
  - name: fact_orders
    columns:
      - name: order_date
        tests:
          - date_in_past
```

## Data tests (tests SQL personalizados)

Para lógica más compleja:

```sql
-- tests/assert_order_total_is_correct.sql
-- Verifica que el total de orders = suma de line_totals en order_items
SELECT
    o.order_id,
    o.total AS order_total,
    SUM(oi.quantity * oi.unit_price) AS calculated_total
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_order_items') }} oi ON o.order_id = oi.order_id
GROUP BY o.order_id, o.total
HAVING ABS(o.total - SUM(oi.quantity * oi.unit_price)) > 0.01
```

```sql
-- tests/assert_no_future_orders.sql
SELECT order_id, order_date
FROM {{ ref('fact_orders') }}
WHERE order_date > CURRENT_DATE
```

## Ejecutar tests

```bash
# Ejecutar todos los tests
dbt test

# Tests de un modelo específico
dbt test --select stg_orders

# Tests solo de un tipo
dbt test --select test_type:unique

# Ver resultados
dbt test --select stg_orders --store_failures
```

### Almacenar fallos

```bash
dbt test --store-failures
# Crea tablas con los registros que fallaron
# Útil para debugging y auditoría
```

## Documentación en dbt

dbt genera documentación automática a partir de descripciones en YAML:

```yml
# models/marts/schema.yml
version: 2

models:
  - name: fact_orders
    description: "Tabla de hechos de pedidos. Cada fila es un pedido con métricas agregadas."
    columns:
      - name: order_id
        description: "Identificador único del pedido (PK)"
        tests:
          - unique
          - not_null
      - name: total
        description: "Monto total del pedido en USD. Incluye impuestos."
      - name: status
        description: "Estado del pedido: completed, pending, cancelled, refunded"

  - name: dim_customers
    description: "Dimensión de clientes con métricas de comportamiento."
    columns:
      - name: customer_id
        description: "Identificador único del cliente (PK)"
      - name: total_pedidos
        description: "Número total de pedidos realizados por el cliente"
      - name: ticket_promedio
        description: "Gasto promedio por pedido del cliente"
```

### Generar y servir documentación

```bash
dbt docs generate
dbt docs serve
# Abre http://localhost:8080
# Incluye: descripciones, columnas, tests, lineage, SQL de cada modelo
```

## dbt Project Evaluator

dbt tiene un paquete que evalúa la calidad de tu proyecto:

```yml
# packages.yml
packages:
  - package: dbt-labs/dbt_project_evaluator
    version: ">=0.1.0"
```

```bash
dbt deps    # Instalar paquetes
dbt run --select package:dbt_project_evaluator
dbt test --select package:dbt_project_evaluator
```

## Buenas prácticas de testing

1. **Siempre testea PKs**: `unique` + `not_null` en cada staging model
2. **Testea relaciones**: cada FK debe tener un test `relationships`
3. **Testea rangos**: fechas futuras, valores negativos, outliers
4. **Documenta mientras construyes**: la documentación es parte del código
5. **Falla rápido**: corre tests en cada `dbt run`

## Ejercicios

1. Agrega tests `unique` y `not_null` a `order_id` en `stg_orders`
2. Crea un test `relationships` entre `stg_orders.customer_id` y `stg_customers.customer_id`
3. Escribe un data test que verifique que no hay pedidos con total negativo
4. Crea un test genérico `not_empty_string` para columnas de texto
5. Documenta 3 modelos con descripciones y columnas
6. Genera la documentación con `dbt docs generate`
7. Ejecuta `dbt test` y corrige cualquier fallo
8. ¿Por qué es importante testear relaciones entre tablas?
9. Crea un test que verifique que `order_items.quantity > 0`
10. ¿Qué ventaja tiene `dbt test --store-failures`?
