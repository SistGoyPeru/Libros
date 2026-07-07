-- Ejemplo 1: Top 10 productos más vendidos
SELECT p.name AS producto, SUM(oi.quantity) AS unidades_vendidas, ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
FROM order_items oi
JOIN products p ON oi.product_id = p.id
GROUP BY p.name
ORDER BY unidades_vendidas DESC
LIMIT 10;