-- Capítulo 5: Modelo staging de órdenes
-- Limpia orders: elimina nulos, estandariza fechas

{{ config(materialized='view') }}

SELECT
    order_id,
    customer_id,
    CAST(order_date AS DATE) AS order_date,
    ROUND(total, 2) AS total,
    COALESCE(status, 'unknown') AS status
FROM {{ source('techstore', 'orders') }}
WHERE total > 0
