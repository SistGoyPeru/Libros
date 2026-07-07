# Apéndice A: Soluciones a los Ejercicios

## Capítulo 1: Ecosistema del Analista

1. 5 tablas: customers, employees, orders, order_items, products
2. 509 productos
3. 250 clientes
4. id, customer_id, employee_id, order_date, status, total
5. Desde 2023-01-01 hasta 2026-06-30
6. 25 empleados
7. 15 categorías
8. 6000 filas
9. .db es una base de datos relacional (SQLite), .csv es un archivo de texto plano con valores separados por comas
10. SQLite está optimizado para consultas en millones de filas, utiliza índices y no carga todo en memoria

## Capítulo 2: SQL SELECT

1. `SELECT * FROM customers LIMIT 10;`
2. `SELECT first_name FROM customers;`
3. `SELECT name, price FROM products ORDER BY price DESC LIMIT 5;`
4. `SELECT COUNT(*) FROM products WHERE stock > 0;`
5. `SELECT name, price FROM products ORDER BY price ASC LIMIT 3;`
6. `SELECT first_name, last_name, position FROM employees ORDER BY hire_date;`
7. `SELECT name AS Producto, price AS Precio FROM products;`
8. `SELECT * FROM categories;`
9. `SELECT id, order_date, total FROM orders ORDER BY order_date DESC LIMIT 10;`
10. 21118 filas

## Capítulo 3: SQL WHERE

1. `SELECT * FROM products WHERE price > 1000;`
2. `SELECT COUNT(*) FROM products WHERE stock = 0;`
3. `SELECT * FROM products WHERE category_id = 4 AND price < 100;`
4. `SELECT * FROM customers WHERE region IN ('Madrid', 'Cataluña');`
5. `SELECT * FROM orders WHERE total BETWEEN 100 AND 500 ORDER BY total DESC;`
6. `SELECT COUNT(*) FROM orders WHERE status = 'Cancelado';` (Aprox 450)
7. `SELECT * FROM products WHERE name LIKE '%Ultra%';`
8. `SELECT * FROM employees WHERE hire_date > '2024-01-01';`
9. `SELECT COUNT(*) FROM products WHERE price IS NULL;` (0)
10. `SELECT name, price, stock FROM products WHERE stock > 0 ORDER BY price DESC LIMIT 10;`

## Capítulo 4: Excel Importar

1-10: Soluciones prácticas. Los valores numéricos dependen de los datos. Verificar con fórmulas:
- SUMA, PROMEDIO, CONTAR, CONTAR.SI, SUMAR.SI

## Capítulo 5: Python Variables

1. `nombre_tienda = "TechStore"; print(nombre_tienda)`
2. `ingresos = 1500000; gastos = 950000; print(f"Beneficio: {ingresos - gastos}€")`
3. `nombre = input("¿Cómo te llamas? "); print(f"Hola {nombre}")`
4. `precio = 499.99; print(f"Con IVA: {precio * 1.21:.2f}€")`
5. `precio = float("1299.99"); print(precio + 200)`
6. `from datetime import date; dias = (date.today() - date(2024, 1, 1)).days; print(dias)`
7. `stock = 50; stock -= 3; print(f"Stock restante: {stock}")`
8. `total = 25; mujeres = 12; print(f"Porcentaje: {mujeres/total*100:.1f}%")`
9. `a = float(input("Número 1: ")); b = float(input("Número 2: ")); print(a + b)`
10. `print(type(42), type(3.14), type("Hola"), type(True), type(None))`

## Capítulo 6: SQL GROUP BY

1. `SELECT status, COUNT(*) FROM orders GROUP BY status;`
2. `SELECT c.region, ROUND(SUM(o.total), 2) FROM orders o JOIN customers c ON o.customer_id = c.id GROUP BY c.region;`
3. `SELECT c.name, COUNT(*) FROM categories c JOIN products p ON c.id = p.category_id GROUP BY c.name;`
4. `SELECT city, COUNT(*) FROM customers GROUP BY city ORDER BY COUNT(*) DESC;`
5. `SELECT c.region, ROUND(AVG(o.total), 2) FROM orders o JOIN customers c ON o.customer_id = c.id GROUP BY c.region;`
6. `SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id HAVING COUNT(*) > 5;`
7. Ver consulta 3.1 del Checkpoint 2
8. `SELECT strftime('%Y-%m', order_date), COUNT(*) FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01' GROUP BY 1;`
9. `SELECT e.first_name || ' ' || e.last_name, ROUND(SUM(o.total), 2) FROM employees e JOIN orders o ON e.id = o.employee_id GROUP BY e.id ORDER BY 2 DESC;`
10. `SELECT c.name, ROUND(AVG(p.price), 2) FROM categories c JOIN products p ON c.id = p.category_id GROUP BY c.name ORDER BY 2 DESC;`

## Capítulo 7: SQL JOINs

1. `SELECT o.id, o.order_date, c.first_name || ' ' || c.last_name, c.region, o.total FROM orders o JOIN customers c ON o.customer_id = c.id ORDER BY o.order_date DESC LIMIT 10;`
2. `SELECT e.first_name || ' ' || e.last_name, COUNT(*) FROM employees e JOIN orders o ON e.id = o.employee_id GROUP BY e.id ORDER BY 2 DESC;`
3. `SELECT p.name, c.name AS categoria, p.price FROM products p JOIN categories c ON p.category_id = c.id ORDER BY p.price DESC;`
4. `SELECT c.first_name || ' ' || c.last_name, COUNT(o.id) FROM customers c JOIN orders o ON c.id = o.customer_id GROUP BY c.id ORDER BY 2 DESC;`
5. `SELECT p.name, ROUND(SUM(oi.quantity * oi.unit_price), 2) FROM products p JOIN order_items oi ON p.id = oi.product_id JOIN orders o ON oi.order_id = o.id WHERE o.status = 'Completado' GROUP BY p.id ORDER BY 2 DESC;`
6. `SELECT * FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.id IS NULL;`
7. `SELECT e.first_name || ' ' || e.last_name, ROUND(SUM(o.total), 2) FROM employees e JOIN orders o ON e.id = o.employee_id WHERE o.status = 'Completado' GROUP BY e.id ORDER BY 2 DESC;`
8. `SELECT c.name, MAX(p.price) AS caro, MIN(p.price) AS barato FROM categories c JOIN products p ON c.id = p.category_id GROUP BY c.name;`
9. Usar COUNT(DISTINCT oi.product_id) con JOINs
10. Ver Checkpoint 2

## Capítulo 8: Excel Tablas Dinámicas

Soluciones prácticas: crear tabla dinámica, arrastrar campos a filas/columnas/valores, cambiar tipo de cálculo.

## Capítulo 9: Python Estructuras

1. `productos = ["Portátil", "Smartphone", "Tablet", "Auriculares", "Ratón"]`
2. `productos.append("Teclado"); productos.append("Monitor"); productos.append("Altavoz")`
3. `cliente = {"nombre": "Ana", "email": "ana@email.com", "ciudad": "Madrid", "gasto_total": 1250.50}`
4. `cliente["gasto_total"] += 150`
5. `[round(p * 1.21, 2) for p in [299, 599, 899, 1299, 1999]]`
6. `cesta = [("Portátil", 1299.99), ("Ratón", 29.99), ("Teclado", 89.99)]; total = sum(p * c for _, p in cesta)`
7. `precios = [100, 500, 50, 1000, 200, 800]; [p for p in precios if p > 500]`
8. Usar diccionario y bucle para restar 1 a cada stock
9. `max(productos, key=lambda p: p["precio"])`
10. `def analisis(ventas): return {"promedio": sum(ventas)/len(ventas), "max": max(ventas), "min": min(ventas)}`

## Capítulo 10: Excel Gráficos

Soluciones prácticas: insertar gráfico, seleccionar datos, personalizar.

## Capítulo 11: SQL Subconsultas

1. `SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);`
2. `SELECT customer_id, SUM(total) FROM orders GROUP BY customer_id HAVING SUM(total) > (SELECT AVG(total) FROM orders);`
3. `SELECT *, ROUND(total / (SELECT SUM(total) FROM orders WHERE status = 'Completado') * 100, 2) FROM orders WHERE status = 'Completado';`
4. `WITH ventas_mes AS (SELECT strftime('%Y-%m', order_date) AS mes, SUM(total) AS ingresos FROM orders WHERE status = 'Completado' GROUP BY mes) SELECT * FROM ventas_mes WHERE ingresos > 100000;`
5. Crear CTEs y calcular porcentajes
6. `SELECT employee_id, COUNT(*) FROM orders GROUP BY employee_id HAVING COUNT(*) > (SELECT AVG(cnt) FROM (SELECT COUNT(*) AS cnt FROM orders GROUP BY employee_id));`
7. Con subconsulta correlacionada comparando stock con AVG(stock) de su categoría
8. CTE con ROW_NUMBER() PARTITION BY category_id
9. Crear CTEs para cada año y comparar
10. Con NOT EXISTS y subconsulta

## Capítulo 12: Window Functions

1. `SELECT name, price, ROW_NUMBER() OVER (ORDER BY price DESC) FROM products;`
2. `SELECT customer_id, gasto, NTILE(5) OVER (ORDER BY gasto) FROM (SELECT customer_id, SUM(total) AS gasto FROM orders GROUP BY customer_id);`
3. `SELECT mes, ingresos, SUM(ingresos) OVER (ORDER BY mes) FROM ventas_mensuales;`
4. Con FIRST_VALUE o MAX() OVER (PARTITION BY category_id)
5. `SELECT mes, ingresos, LAG(ingresos) OVER (ORDER BY mes) FROM ventas_mensuales;`
6. Con ROW_NUMBER() PARTITION BY category_id ORDER BY unidades DESC
7. Con AVG(total) OVER (ORDER BY fecha ROWS BETWEEN 29 PRECEDING AND CURRENT ROW)
8. `SELECT mes, ingresos, LEAD(ingresos) OVER (ORDER BY mes) FROM ventas_mensuales;`
9. `SELECT order_id, customer_id, total, ROUND(total / SUM(total) OVER (PARTITION BY customer_id), 4) FROM orders WHERE status = 'Completado';`
10. `SELECT *, price > AVG(price) OVER (PARTITION BY category_id) AS sobre_promedio FROM products;`

## Capítulo 13: Power Query

Soluciones prácticas en Power Query Editor.

## Capítulo 14: Python Funciones

1. `def calcular_iva(precio, tasa=0.21): return round(precio * (1 + tasa), 2)`
2-10: Ver archivos de soluciones en codigos/soluciones/

## Capítulo 15: DAX

Ver medidas DAX en el capítulo 17 para soluciones completas.
