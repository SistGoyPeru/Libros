# Capítulo 11: SQL — Subconsultas y CTEs

## Subconsultas: consultas dentro de consultas

Una subconsulta es una consulta SQL dentro de otra consulta. Se usa para calcular valores intermedios.

### Subconsulta en WHERE

```sql
-- Productos con precio superior al promedio
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;
```

La subconsulta `(SELECT AVG(price) FROM products)` se ejecuta primero y devuelve un solo valor.

### Subconsulta con IN

```sql
-- Clientes que han comprado productos de la categoría "Portátiles"
SELECT first_name, last_name, email
FROM customers
WHERE id IN (
    SELECT DISTINCT o.customer_id
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE p.category_id = 1
);
```

### Subconsulta en SELECT

```sql
-- Porcentaje que representa cada categoría sobre el total
SELECT c.name AS categoria,
       ROUND(AVG(p.price), 2) AS precio_promedio,
       ROUND((SELECT AVG(price) FROM products), 2) AS precio_global,
       ROUND(AVG(p.price) / (SELECT AVG(price) FROM products) * 100, 1) AS porcentaje
FROM categories c
JOIN products p ON c.id = p.category_id
GROUP BY c.name
ORDER BY porcentaje DESC;
```

### Subconsulta correlacionada

Una subconsulta correlacionada referencia columnas de la consulta externa.

```sql
-- Productos cuyo precio es mayor que el promedio de su categoría
SELECT p.name, p.price, p.category_id,
       (SELECT ROUND(AVG(p2.price), 2)
        FROM products p2
        WHERE p2.category_id = p.category_id) AS promedio_categoria
FROM products p
WHERE p.price > (SELECT AVG(p2.price)
                 FROM products p2
                 WHERE p2.category_id = p.category_id)
LIMIT 20;
```

## CTEs (Common Table Expressions) con WITH

Una CTE es como una vista temporal que existe solo durante tu consulta. Hace el SQL más legible.

```sql
-- CTE simple
WITH ventas_por_categoria AS (
    SELECT c.name AS categoria,
           SUM(oi.quantity * oi.unit_price) AS ingresos
    FROM categories c
    JOIN products p ON c.id = p.category_id
    JOIN order_items oi ON p.id = oi.product_id
    GROUP BY c.name
)
SELECT categoria, ROUND(ingresos, 2) AS ingresos
FROM ventas_por_categoria
ORDER BY ingresos DESC;
```

### Múltiples CTEs

```sql
WITH
clientes_top AS (
    SELECT customer_id, COUNT(*) AS pedidos, SUM(total) AS gasto
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(*) > 5
),
ventas_region AS (
    SELECT c.region, SUM(o.total) AS ingresos
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    WHERE o.customer_id IN (SELECT customer_id FROM clientes_top)
    GROUP BY c.region
)
SELECT region, ROUND(ingresos, 2) AS ingresos
FROM ventas_region
ORDER BY ingresos DESC;
```

### CTE recursiva

Útil para datos jerárquicos como categorías o fechas:

```sql
-- Generar una serie de meses
WITH RECURSIVE meses AS (
    SELECT DATE('2024-01-01') AS mes
    UNION ALL
    SELECT DATE(mes, '+1 month')
    FROM meses
    WHERE mes < DATE('2025-12-01')
)
SELECT strftime('%Y-%m', mes) AS mes
FROM meses;
```

## Subconsulta vs CTE vs JOIN

| Situación | Recomendación |
|-----------|---------------|
| Valor único para comparación | Subconsulta en WHERE |
| Necesitas reutilizar la misma subconsulta | CTE |
| Relacionar dos tablas | JOIN |
| Consulta anidada compleja | CTE (más legible) |
| Filtrar por agregación | HAVING o subconsulta en WHERE |

## Análisis práctico

```sql
-- Clientes con gasto superior al promedio de su región
WITH gasto_region AS (
    SELECT c.region, AVG(o.total) AS avg_gasto_region
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    GROUP BY c.region
)
SELECT c.first_name || ' ' || c.last_name AS cliente,
       c.region,
       ROUND(SUM(o.total), 2) AS gasto_total,
       ROUND(g.avg_gasto_region, 2) AS promedio_region
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN gasto_region g ON c.region = g.region
GROUP BY c.id
HAVING SUM(o.total) > g.avg_gasto_region
ORDER BY gasto_total DESC;
```

## Ejercicios del Capítulo 11

1. Encuentra los productos con precio superior al promedio general.
2. ¿Qué clientes han gastado más que el promedio de todos los clientes?
3. Usa una subconsulta en SELECT para mostrar cada pedido y el % que representa sobre el total.
4. Crea una CTE que calcule las ventas por mes, y luego consulta los meses con ventas superiores a 100,000€.
5. Usa múltiples CTEs para: (1) calcular ventas por categoría, (2) calcular ventas totales, (3) mostrar el % de cada categoría.
6. Encuentra empleados que han gestionado más pedidos que el promedio.
7. Usa una subconsulta correlacionada para mostrar productos cuyo stock está por debajo del promedio de su categoría.
8. Crea una CTE para encontrar el producto más vendido de cada categoría.
9. ¿Qué productos se han vendido más en 2025 que en 2024? (Usa dos CTEs y compáralas).
10. Encuentra clientes que han pedido productos de todas las categorías (usa subconsultas con NOT EXISTS).

## Checklist de autoevaluación

- [ ] Sé escribir subconsultas en WHERE, SELECT y FROM
- [ ] Entiendo las subconsultas correlacionadas
- [ ] Sé crear CTEs con WITH
- [ ] Sé usar múltiples CTEs en una consulta
- [ ] Sé cuándo usar subconsulta vs CTE vs JOIN
- [ ] Entiendo las ventajas de legibilidad de las CTEs
