-- Soluciones Capítulo 2: SQL SELECT

-- 1. Todas las columnas de customers, 10 filas
SELECT * FROM customers LIMIT 10;

-- 2. Solo nombres de clientes
SELECT first_name FROM customers;

-- 3. Nombre y precio, ordenado por precio DESC, 5 resultados
SELECT name, price FROM products ORDER BY price DESC LIMIT 5;

-- 4. Productos con stock > 0
SELECT COUNT(*) FROM products WHERE stock > 0;

-- 5. 3 productos más baratos
SELECT name, price FROM products ORDER BY price ASC LIMIT 3;

-- 6. Empleados: nombre y puesto, ordenado por fecha contratación
SELECT first_name, last_name, position FROM employees ORDER BY hire_date;

-- 7. Alias: Producto, Precio
SELECT name AS Producto, price AS Precio FROM products;

-- 8. Categorías existentes
SELECT * FROM categories;

-- 9. 10 pedidos más recientes
SELECT id, order_date, total FROM orders ORDER BY order_date DESC LIMIT 10;

-- 10. Filas en order_items
SELECT COUNT(*) FROM order_items;
