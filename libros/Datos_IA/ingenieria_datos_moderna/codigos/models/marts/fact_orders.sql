-- Capítulo 5: Modelo marts de órdenes
-- Tabla física para BI y reportes

{{ config(materialized='table') }}

SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.total,
    o.status
FROM {{ ref('stg_orders') }} o
