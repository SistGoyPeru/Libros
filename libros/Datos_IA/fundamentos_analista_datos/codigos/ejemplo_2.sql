-- Ejemplo 2: Ventas por región
SELECT c.region, COUNT(DISTINCT o.id) AS pedidos, ROUND(SUM(o.total), 2) AS ingresos_totales, ROUND(AVG(o.total), 2) AS ticket_promedio
FROM orders o
JOIN customers c ON o.customer_id = c.id
GROUP BY c.region
ORDER BY ingresos_totales DESC;