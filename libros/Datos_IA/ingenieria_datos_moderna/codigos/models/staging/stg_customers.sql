-- Capítulo 5: Modelo staging de clientes
-- Limpia nombres y emails

{{ config(materialized='view') }}

SELECT
    customer_id,
    TRIM(name) AS name,
    LOWER(email) AS email,
    city,
    country,
    registration_date
FROM {{ source('techstore', 'customers') }}
WHERE email IS NOT NULL
