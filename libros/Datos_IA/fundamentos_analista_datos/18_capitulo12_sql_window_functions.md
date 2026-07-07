# Capítulo 12: SQL — Funciones de Ventana (Window Functions)

## ¿Qué son las funciones de ventana?

Las funciones de ventana realizan cálculos a través de un conjunto de filas relacionadas con la fila actual. A diferencia de GROUP BY, no colapsan las filas: cada fila conserva su identidad.

```sql
-- GROUP BY: colapsa (1 fila por grupo)
SELECT category_id, AVG(price) FROM products GROUP BY category_id;

-- Window function: no colapsa (cada fila conserva su precio + el promedio)
SELECT name, price, category_id,
       AVG(price) OVER (PARTITION BY category_id) AS promedio_categoria
FROM products
LIMIT 10;
```

## Sintaxis básica

```sql
funcion() OVER (
    PARTITION BY columna   -- grupos (opcional)
    ORDER BY columna       -- orden dentro del grupo (opcional)
    frame_specification    -- ventana móvil (opcional)
)
```

## ROW_NUMBER, RANK, DENSE_RANK

### ROW_NUMBER: número único de fila

```sql
SELECT name, price, category_id,
       ROW_NUMBER() OVER (ORDER BY price DESC) AS posicion_global
FROM products
LIMIT 10;
```

### Particionado: reiniciar el contador

```sql
SELECT name, price, category_id,
       ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY price DESC) AS pos_en_categoria
FROM products
LIMIT 20;
```

### RANK vs DENSE_RANK

```sql
SELECT name, price,
       RANK() OVER (ORDER BY price DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY price DESC) AS dense_rank
FROM products
WHERE price > 1500
ORDER BY price DESC;
```

| name | price | rank | dense_rank |
|------|-------|------|------------|
| Producto A | 1999.99 | 1 | 1 |
| Producto B | 1999.99 | 1 | 1 |
| Producto C | 1899.99 | 3 | 2 |
| Producto D | 1799.99 | 4 | 3 |

Diferencia: RANK salta números en empates, DENSE_RANK no.

## Funciones de agregación como ventanas

Puedes usar SUM, AVG, COUNT como ventanas:

```sql
SELECT o.id AS pedido,
       o.order_date,
       o.total,
       SUM(o.total) OVER (ORDER BY o.order_date) AS acumulado,
       AVG(o.total) OVER (ORDER BY o.order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS media_movil_7d
FROM orders o
WHERE o.status = 'Completado'
ORDER BY o.order_date
LIMIT 20;
```

## NTILE: dividir en grupos

```sql
-- Dividir productos en 4 cuartiles por precio
SELECT name, price,
       NTILE(4) OVER (ORDER BY price DESC) AS cuartil
FROM products
LIMIT 20;
```

## LAG y LEAD: acceder a filas anteriores/siguientes

```sql
-- Comparar ventas con el mes anterior
WITH ventas_mensuales AS (
    SELECT strftime('%Y-%m', order_date) AS mes,
           ROUND(SUM(total), 2) AS ingresos
    FROM orders
    WHERE status = 'Completado'
    GROUP BY mes
)
SELECT mes, ingresos,
       LAG(ingresos, 1) OVER (ORDER BY mes) AS mes_anterior,
       ROUND(ingresos - LAG(ingresos, 1) OVER (ORDER BY mes), 2) AS variacion,
       ROUND((ingresos - LAG(ingresos, 1) OVER (ORDER BY mes)) / LAG(ingresos, 1) OVER (ORDER BY mes) * 100, 1) AS crecimiento_pct
FROM ventas_mensuales
ORDER BY mes;
```

## Frame specification (ventana móvil)

Controla exactamente qué filas incluir:

```sql
-- ROWS BETWEEN inicio AND fin
-- PRECEDING: filas anteriores
-- FOLLOWING: filas posteriores
-- CURRENT ROW: fila actual
-- UNBOUNDED PRECEDING: desde el inicio del grupo
-- UNBOUNDED FOLLOWING: hasta el final del grupo

-- Media móvil de 3 días
AVG(total) OVER (ORDER BY order_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)

-- Total acumulado desde el inicio
SUM(total) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)

-- Total del grupo completo (todas las filas)
SUM(total) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
```

## FIRST_VALUE y LAST_VALUE

```sql
-- Comparar cada producto con el más caro de su categoría
SELECT p.name, p.price, p.category_id,
       FIRST_VALUE(p.name) OVER (PARTITION BY p.category_id ORDER BY p.price DESC) AS mas_caro_categoria,
       FIRST_VALUE(p.price) OVER (PARTITION BY p.category_id ORDER BY p.price DESC) AS precio_mas_caro,
       ROUND(p.price / FIRST_VALUE(p.price) OVER (PARTITION BY p.category_id ORDER BY p.price DESC) * 100, 1) AS porcentaje
FROM products p
LIMIT 20;
```

## Análisis práctico: ranking de productos

```sql
-- Top 3 productos más vendidos por categoría
WITH ranking AS (
    SELECT c.name AS categoria,
           p.name AS producto,
           SUM(oi.quantity) AS unidades,
           ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS posicion
    FROM categories c
    JOIN products p ON c.id = p.category_id
    JOIN order_items oi ON p.id = oi.product_id
    GROUP BY c.id, p.id
)
SELECT categoria, producto, unidades
FROM ranking
WHERE posicion <= 3
ORDER BY categoria, posicion;
```

## Ejercicios del Capítulo 12

1. Asigna un número de fila único a todos los productos ordenados por precio descendente.
2. Divide los clientes en 5 quintiles según su gasto total.
3. Calcula el total acumulado de ventas por mes (acumulado año corrido).
4. Para cada producto, muestra cuánto representa su precio respecto al más caro de su categoría.
5. Calcula la diferencia de ventas entre cada mes y el mes anterior usando LAG.
6. Encuentra el top 3 de productos más vendidos en cada categoría (usa ROW_NUMBER con PARTITION BY).
7. Calcula una media móvil de 30 días para las ventas diarias.
8. Usa LEAD para mostrar las ventas del próximo mes junto a las del mes actual.
9. Para cada pedido, muestra qué porcentaje representa respecto al total del cliente.
10. Encuentra productos cuyo precio está por encima del promedio de su categoría (usa AVG como ventana).

## Checklist de autoevaluación

- [ ] Entiendo qué son las funciones de ventana y cómo se diferencian de GROUP BY
- [ ] Sé usar ROW_NUMBER, RANK y DENSE_RANK
- [ ] Sé usar PARTITION BY para agrupar cálculos
- [ ] Sé usar funciones de agregación como ventanas
- [ ] Sé usar LAG y LEAD para acceder a filas adyacentes
- [ ] Sé usar frames (ROWS BETWEEN) para ventanas móviles
- [ ] Sé usar NTILE para dividir en grupos percentiles
