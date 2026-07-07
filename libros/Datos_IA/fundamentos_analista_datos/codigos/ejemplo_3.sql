-- Ejemplo 3: Clientes con mayor gasto
SELECT c.first_name || ' ' || c.last_name AS cliente, COUNT(o.id) AS pedidos, ROUND(SUM(o.total), 2) AS gasto_total
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id
HAVING gasto_total > 1000
ORDER BY gasto_total DESC;