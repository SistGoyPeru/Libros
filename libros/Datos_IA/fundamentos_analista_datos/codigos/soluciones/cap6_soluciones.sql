-- Soluciones Capítulo 6: SQL GROUP BY

-- 1. Pedidos por estado
SELECT status, COUNT(*) FROM orders GROUP BY status;

-- 2. Ingresos por región
SELECT c.region, ROUND(SUM(o.total), 2) AS ingresos
FROM orders o JOIN customers c ON o.customer_id = c.id
GROUP BY c.region;

-- 3. Productos por categoría
SELECT c.name, COUNT(*) AS cantidad
FROM categories c JOIN products p ON c.id = p.category_id
GROUP BY c.name;

-- 4. Ciudades con más clientes
SELECT city, COUNT(*) AS cantidad
FROM customers
GROUP BY city ORDER BY cantidad DESC;

-- 5. Ticket promedio por región
SELECT c.region, ROUND(AVG(o.total), 2) AS ticket_promedio
FROM orders o JOIN customers c ON o.customer_id = c.id
GROUP BY c.region;

-- 6. Clientes con más de 5 pedidos
SELECT customer_id, COUNT(*) AS pedidos
FROM orders GROUP BY customer_id HAVING pedidos > 5;

-- 7. Producto más vendido
SELECT p.name, SUM(oi.quantity) AS unidades
FROM products p JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id ORDER BY unidades DESC LIMIT 1;

-- 8. Pedidos por mes en 2024
SELECT strftime('%Y-%m', order_date) AS mes, COUNT(*) AS pedidos
FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'
GROUP BY mes ORDER BY mes;

-- 9. Ingresos por empleado
SELECT e.first_name || ' ' || e.last_name AS empleado,
       ROUND(SUM(o.total), 2) AS ingresos
FROM employees e JOIN orders o ON e.id = o.employee_id
GROUP BY e.id ORDER BY ingresos DESC;

-- 10. Precio promedio por categoría
SELECT c.name, ROUND(AVG(p.price), 2) AS precio_promedio
FROM categories c JOIN products p ON c.id = p.category_id
GROUP BY c.name ORDER BY precio_promedio DESC;
