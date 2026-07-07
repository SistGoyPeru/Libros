# Capítulo 6: SQL — Agrupando y Resumiendo Datos

## Funciones de agregación

Las funciones de agregación resumen múltiples filas en un solo resultado. Son la base del análisis de datos en SQL.

```sql
SELECT COUNT(*) AS total_pedidos,
       ROUND(SUM(total), 2) AS ingresos_totales,
       ROUND(AVG(total), 2) AS ticket_promedio,
       MIN(total) AS pedido_minimo,
       MAX(total) AS pedido_maximo
FROM orders;
```

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `COUNT(*)` | Cuenta filas | `COUNT(*)` = 6000 |
| `COUNT(columna)` | Cuenta valores no NULL | `COUNT(supplier)` |
| `SUM(columna)` | Suma de valores | `SUM(total)` |
| `AVG(columna)` | Promedio | `AVG(total)` |
| `MIN(columna)` | Valor mínimo | `MIN(total)` |
| `MAX(columna)` | Valor máximo | `MAX(total)` |

## GROUP BY: agrupar por categorías

`GROUP BY` agrupa filas que comparten un valor. Se usa con funciones de agregación.

```sql
SELECT status, COUNT(*) AS cantidad, ROUND(SUM(total), 2) AS total
FROM orders
GROUP BY status;
```

Resultado:

| status | cantidad | total |
|--------|----------|-------|
| Cancelado | 450 | 225,000 |
| Completado | 4,800 | 4,800,000 |
| Envío | 300 | 300,000 |
| Pendiente | 450 | 350,000 |

### GROUP BY con múltiples columnas

```sql
SELECT c.region, o.status,
       COUNT(*) AS pedidos,
       ROUND(SUM(o.total), 2) AS ingresos
FROM orders o
JOIN customers c ON o.customer_id = c.id
GROUP BY c.region, o.status
ORDER BY c.region, ingresos DESC;
```

## HAVING: filtrar grupos

`WHERE` filtra filas antes de agrupar. `HAVING` filtra grupos después de agrupar.

```sql
SELECT customer_id,
       COUNT(*) AS pedidos,
       ROUND(SUM(total), 2) AS gasto_total
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 10
ORDER BY gasto_total DESC;
```

Solo clientes con 10 o más pedidos aparecen en el resultado.

## Orden de ejecución en SQL

Es importante entender el orden en que SQL ejecuta las cláusulas:

1. `FROM` — Selecciona las tablas
2. `WHERE` — Filtra filas individuales
3. `GROUP BY` — Agrupa las filas
4. `HAVING` — Filtra los grupos
5. `SELECT` — Selecciona las columnas
6. `ORDER BY` — Ordena el resultado
7. `LIMIT` — Limita el número de filas

## Análisis práctico con TechStore

### Ventas por categoría de producto

```sql
SELECT c.name AS categoria,
       COUNT(DISTINCT oi.order_id) AS pedidos,
       SUM(oi.quantity) AS unidades_vendidas,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
FROM order_items oi
JOIN products p ON oi.product_id = p.id
JOIN categories c ON p.category_id = c.id
GROUP BY c.name
ORDER BY ingresos DESC;
```

### Ventas mensuales

```sql
SELECT strftime('%Y-%m', order_date) AS mes,
       COUNT(*) AS pedidos,
       ROUND(SUM(total), 2) AS ingresos
FROM orders
WHERE status = 'Completado'
GROUP BY mes
ORDER BY mes;
```

### Productos con mejor margen

```sql
SELECT p.name AS producto,
       p.price AS precio,
       p.cost AS coste,
       ROUND((p.price - p.cost) / p.price * 100, 1) AS margen_pct,
       SUM(oi.quantity) AS unidades_vendidas
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id
HAVING unidades_vendidas > 10
ORDER BY margen_pct DESC
LIMIT 10;
```

## Ejercicios del Capítulo 6

1. ¿Cuántos pedidos hay por cada estado (status)?
2. ¿Cuál es el total de ingresos por región?
3. ¿Cuántos productos hay en cada categoría? Muestra el nombre de la categoría y el conteo.
4. ¿Cuáles son las 5 ciudades con más clientes?
5. ¿Cuál es el ticket promedio por región?
6. ¿Cuántos pedidos ha hecho cada cliente? Muestra solo los que han hecho más de 5 pedidos.
7. ¿Cuál es el producto más vendido por unidades totales?
8. ¿Cuántos pedidos se hicieron cada mes en 2024?
9. ¿Cuál es el ingreso total generado por cada empleado (vendedor)?
10. ¿Qué categoría tiene el precio promedio más alto?

## Checklist de autoevaluación

- [ ] Sé usar funciones de agregación: COUNT, SUM, AVG, MIN, MAX
- [ ] Sé agrupar datos con GROUP BY
- [ ] Sé filtrar grupos con HAVING
- [ ] Entiendo la diferencia entre WHERE y HAVING
- [ ] Sé usar GROUP BY con múltiples columnas
- [ ] Entiendo el orden de ejecución de SQL
