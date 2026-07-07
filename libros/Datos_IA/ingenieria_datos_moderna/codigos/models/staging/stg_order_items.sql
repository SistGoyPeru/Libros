-- Capítulo 5: Modelo staging de items de órdenes
-- Calcula line_total a partir de quantity y unit_price

{{ config(materialized='view') }}

SELECT
    order_id,
    product_id,
    quantity,
    unit_price,
    ROUND(quantity * unit_price, 2) AS line_total
FROM {{ source('techstore', 'order_items') }}
