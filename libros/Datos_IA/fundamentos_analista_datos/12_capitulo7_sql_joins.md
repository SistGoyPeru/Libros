# Capítulo 7: SQL — Conectando Tablas con JOINs

## ¿Por qué necesitamos JOINs?

Los datos en una base de datos relacional están distribuidos en varias tablas. Para responder preguntas de negocio, necesitas combinarlas.

```sql
-- Sin JOIN: solo ves IDs, no nombres
SELECT customer_id, total FROM orders LIMIT 5;

-- Con JOIN: ves el nombre del cliente
SELECT o.id, c.first_name, c.last_name, o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id
LIMIT 5;
```

## INNER JOIN: solo registros que coinciden

`INNER JOIN` devuelve solo las filas donde hay correspondencia en ambas tablas.

```sql
SELECT o.id AS pedido,
       c.first_name || ' ' || c.last_name AS cliente,
       o.order_date, o.total
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
LIMIT 10;
```

```
Pedido | Cliente           | Fecha      | Total
1      | Ana García        | 2024-03-15 | 1250.50
2      | Luis Pérez        | 2024-03-15 | 89.99
...
```

## LEFT JOIN: todo de la izquierda, coincidencias de la derecha

`LEFT JOIN` devuelve todas las filas de la tabla izquierda. Si no hay coincidencia, las columnas de la derecha son NULL.

```sql
SELECT p.name AS producto, oi.order_id, oi.quantity
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.order_id IS NULL;
```

Esto encuentra productos que nunca se han vendido.

## JOIN con múltiples tablas

Los datos de TechStore requieren unir varias tablas para obtener información completa:

```sql
SELECT o.id AS pedido,
       c.first_name || ' ' || c.last_name AS cliente,
       c.region,
       e.first_name || ' ' || e.last_name AS vendedor,
       o.order_date, o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN employees e ON o.employee_id = e.id
WHERE o.status = 'Completado'
ORDER BY o.total DESC
LIMIT 10;
```

## JOIN con agregación

```sql
SELECT c.name AS categoria,
       COUNT(DISTINCT o.id) AS pedidos,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
FROM categories c
JOIN products p ON c.id = p.category_id
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'Completado'
GROUP BY c.name
ORDER BY ingresos DESC;
```

## Alias de tablas

Usa alias cortos para simplificar consultas con muchos JOINs:

```sql
-- Sin alias
SELECT orders.id, customers.first_name, products.name
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN order_items ON orders.id = order_items.order_id
JOIN products ON order_items.product_id = products.id;

-- Con alias
SELECT o.id, c.first_name, p.name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

## Uniendo una tabla consigo misma (Self JOIN)

A veces necesitas comparar filas dentro de la misma tabla:

```sql
-- Productos en la misma categoría con precio similar
SELECT a.name AS producto_a,
       b.name AS producto_b,
       a.category_id, a.price
FROM products a
JOIN products b ON a.category_id = b.category_id
                AND a.id < b.id
                AND ABS(a.price - b.price) < 10
LIMIT 20;
```

## Ejercicios del Capítulo 7

1. Muestra los 10 pedidos más recientes con nombre del cliente y región.
2. ¿Qué empleado ha gestionado más pedidos? Muestra su nombre y conteo.
3. Lista los productos con su nombre de categoría, ordenados por precio descendente.
4. ¿Cuántos pedidos ha hecho cada cliente? Muestra nombre y conteo, ordenado de mayor a menor.
5. ¿Qué producto ha generado más ingresos? Necesitas joins con order_items y products.
6. Muestra todos los clientes que NO han hecho ningún pedido (usa LEFT JOIN y IS NULL).
7. ¿Qué vendedor ha generado más ingresos? Muestra su nombre y el total.
8. Para cada categoría, muestra el producto más caro y el más barato.
9. ¿Cuántos productos diferentes compró cada cliente? Muestra cliente y conteo de productos distintos.
10. Muestra el top 5 de productos más vendidos con su nombre de categoría y unidades vendidas.

## Checklist de autoevaluación

- [ ] Entiendo qué son los JOINs y por qué son necesarios
- [ ] Sé usar INNER JOIN para combinar tablas
- [ ] Sé usar LEFT JOIN para incluir registros sin coincidencia
- [ ] Sé unir más de 2 tablas en una consulta
- [ ] Sé usar alias de tablas
- [ ] Entiendo la diferencia entre INNER y LEFT JOIN
