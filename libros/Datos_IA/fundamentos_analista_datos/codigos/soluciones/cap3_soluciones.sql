-- Soluciones Capítulo 3: SQL WHERE

-- 1. Productos > 1000€
SELECT * FROM products WHERE price > 1000;

-- 2. Productos con stock = 0
SELECT COUNT(*) FROM products WHERE stock = 0;

-- 3. Productos categoría 4 (Auriculares), precio < 100
SELECT * FROM products WHERE category_id = 4 AND price < 100;

-- 4. Clientes de Madrid o Cataluña
SELECT * FROM customers WHERE region IN ('Madrid', 'Cataluña');

-- 5. Pedidos entre 100 y 500€, ordenados DESC
SELECT * FROM orders WHERE total BETWEEN 100 AND 500 ORDER BY total DESC;

-- 6. Pedidos cancelados
SELECT COUNT(*) FROM orders WHERE status = 'Cancelado';

-- 7. Productos cuyo nombre contiene "Ultra"
SELECT * FROM products WHERE name LIKE '%Ultra%';

-- 8. Empleados contratados después del 1 enero 2024
SELECT * FROM employees WHERE hire_date > '2024-01-01';

-- 9. Productos con precio NULL
SELECT COUNT(*) FROM products WHERE price IS NULL;

-- 10. 10 productos más caros con stock disponible
SELECT name, price, stock FROM products WHERE stock > 0 ORDER BY price DESC LIMIT 10;
