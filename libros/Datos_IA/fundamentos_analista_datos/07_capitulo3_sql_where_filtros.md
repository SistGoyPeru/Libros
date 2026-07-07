# Capítulo 3: SQL — Filtrando con Precisión

## El poder de WHERE

La cláusula `WHERE` filtra registros según una condición. Solo se devuelven las filas que cumplen la condición.

```sql
SELECT name, price, stock
FROM products
WHERE stock = 0;
```

Esta consulta encuentra todos los productos agotados.

### Operadores de comparación

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `=` | Igual a | `WHERE stock = 0` |
| `!=` o `<>` | Distinto de | `WHERE category_id <> 3` |
| `>` | Mayor que | `WHERE price > 500` |
| `<` | Menor que | `WHERE price < 50` |
| `>=` | Mayor o igual | `WHERE price >= 1000` |
| `<=` | Menor o igual | `WHERE stock <= 10` |

```sql
-- Productos con precio mayor a 500€
SELECT name, price FROM products WHERE price > 500;

-- Productos con stock bajo (10 o menos unidades)
SELECT name, stock FROM products WHERE stock <= 10;
```

## AND, OR, NOT: combinando condiciones

### AND: todas las condiciones deben cumplirse

```sql
-- Productos caros Y con buen stock
SELECT name, price, stock
FROM products
WHERE price > 300 AND stock > 50;
```

### OR: al menos una condición debe cumplirse

```sql
-- Productos de categoría 1 (Portátiles) o categoría 3 (Tablets)
SELECT name, category_id, price
FROM products
WHERE category_id = 1 OR category_id = 3;
```

### Combinando AND y OR

Usa paréntesis para agrupar condiciones, igual que en matemáticas:

```sql
-- Productos de categoría 1 o 2, con precio mayor a 500
SELECT name, category_id, price
FROM products
WHERE (category_id = 1 OR category_id = 2) AND price > 500;
```

### NOT: niega una condición

```sql
-- Productos que NO son de categoría 1
SELECT name, category_id FROM products WHERE NOT category_id = 1;
```

## IN: múltiples valores posibles

`IN` es una forma más limpia de escribir múltiples condiciones `OR`:

```sql
-- En lugar de: category_id = 1 OR category_id = 3 OR category_id = 5
SELECT name, category_id, price
FROM products
WHERE category_id IN (1, 3, 5);
```

## BETWEEN: rangos de valores

```sql
-- Productos entre 100 y 300 euros
SELECT name, price
FROM products
WHERE price BETWEEN 100 AND 300;
```

`BETWEEN` incluye los extremos. Es equivalente a `price >= 100 AND price <= 300`.

## LIKE: búsqueda de texto parcial

```sql
-- Productos que contienen "Pro" en el nombre
SELECT name FROM products WHERE name LIKE '%Pro%';
```

El símbolo `%` significa "cualquier secuencia de caracteres":

| Patrón | Significado |
|--------|-------------|
| `'Pro%'` | Empieza con "Pro" |
| `'%Pro'` | Termina con "Pro" |
| `'%Pro%'` | Contiene "Pro" en cualquier parte |
| `'Pro_'` | "Pro" seguido de exactamente 1 carácter |

## NULL: valores ausentes

`NULL` significa "valor desconocido" o "sin dato". No es lo mismo que 0 o cadena vacía.

No puedes usar `=` con NULL. Usa `IS NULL` o `IS NOT NULL`:

```sql
-- Productos sin proveedor asignado
SELECT name, supplier FROM products WHERE supplier IS NULL;

-- Productos con proveedor
SELECT name, supplier FROM products WHERE supplier IS NOT NULL;
```

## Combinando todo

```sql
-- Productos de categorías 1, 2 o 3, con precio entre 200 y 1000,
-- con stock disponible, ordenados por precio descendente
SELECT
    name AS producto,
    price AS precio,
    stock AS inventario
FROM products
WHERE category_id IN (1, 2, 3)
  AND price BETWEEN 200 AND 1000
  AND stock > 0
ORDER BY price DESC;
```

## Filtros en la tabla customers

```sql
-- Clientes de Madrid
SELECT first_name, last_name, city, region
FROM customers
WHERE city = 'Madrid';

-- Clientes de Andalucía o Cataluña
SELECT first_name, last_name, region
FROM customers
WHERE region IN ('Andalucía', 'Cataluña');

-- Clientes registrados después de 2025
SELECT first_name, last_name, registration_date
FROM customers
WHERE registration_date >= '2025-01-01';
```

## Ejercicios del Capítulo 3

1. Encuentra todos los productos con precio mayor a 1000€.
2. ¿Cuántos productos tienen stock igual a 0?
3. Muestra los productos de la categoría 4 (Auriculares) con precio menor a 100€.
4. Encuentra clientes de las regiones 'Madrid' o 'Cataluña'.
5. Muestra los pedidos con total entre 100 y 500€, ordenados por total descendente.
6. ¿Cuántos pedidos están cancelados (status = 'Cancelado')?
7. Encuentra productos cuyo nombre contiene "Ultra".
8. Muestra los empleados contratados después del 1 de enero de 2024.
9. ¿Cuántos productos tienen precio NULL? (ninguno, pero practica `IS NULL`)
10. Muestra los 10 productos más caros con stock disponible (stock > 0).

## Checklist de autoevaluación

- [ ] Sé usar `WHERE` con operadores de comparación
- [ ] Sé combinar condiciones con `AND`, `OR` y `NOT`
- [ ] Sé usar `IN` para múltiples valores
- [ ] Sé usar `BETWEEN` para rangos
- [ ] Sé usar `LIKE` para búsqueda por patrón
- [ ] Entiendo la diferencia entre `NULL` y otros valores
- [ ] Sé filtrar valores nulos con `IS NULL` / `IS NOT NULL`
