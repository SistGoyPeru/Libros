# Capítulo 2: SQL — SELECT y tus Primeros Datos

## ¿Qué es SQL?

SQL (Structured Query Language) es el lenguaje universal para hablar con bases de datos. Con SQL puedes:

- Extraer datos específicos
- Filtrar registros
- Combinar tablas
- Calcular métricas
- Insertar, actualizar y eliminar datos

Todo analista de datos debe saber SQL. Es la habilidad más demandada en ofertas de empleo de datos.

## Tu primera consulta SQL

La sentencia más básica es `SELECT`. Sirve para extraer datos de una tabla.

```sql
SELECT * FROM products;
```

Esta consulta dice: "dame todas las columnas (`*`) de la tabla `products`".

**Pruébalo**: Abre DB Browser, ve a la pestaña "Execute SQL", escribe la consulta y haz clic en "Run".

### LIMIT: controla cuántos resultados ves

Las tablas pueden tener miles de filas. Usa `LIMIT` para ver solo las primeras:

```sql
SELECT * FROM products LIMIT 10;
```

### Seleccionar columnas específicas

En lugar de `*`, nombra las columnas que quieres:

```sql
SELECT name, price, stock FROM products LIMIT 10;
```

## ORDER BY: ordena los resultados

```sql
SELECT name, price FROM products ORDER BY price DESC LIMIT 10;
```

`DESC` ordena descendente. `ASC` (o nada) ordena ascendente.

```sql
SELECT name, price FROM products ORDER BY price ASC LIMIT 10;
```

### Ordenar por múltiples columnas

```sql
SELECT name, category_id, price
FROM products
ORDER BY category_id ASC, price DESC
LIMIT 20;
```

Esto ordena primero por categoría, y dentro de cada categoría, por precio descendente.

## Comentarios en SQL

```sql
-- Esto es un comentario de una línea
SELECT name, price FROM products;  -- también al final de una línea

/* Esto es un
   comentario
   de varias líneas */
SELECT * FROM customers;
```

## Alias con AS

Usa `AS` para renombrar columnas en los resultados:

```sql
SELECT
    name AS producto,
    price AS precio,
    stock AS inventario
FROM products
LIMIT 10;
```

Esto hace que los resultados sean más legibles.

## Explorando las tablas de TechStore

Prueba estas consultas para familiarizarte con los datos:

```sql
-- Todos los productos
SELECT * FROM products LIMIT 20;

-- Todos los clientes (solo nombre y ciudad)
SELECT first_name, last_name, city FROM customers LIMIT 20;

-- Todos los pedidos, ordenados del más reciente al más antiguo
SELECT id, customer_id, order_date, total
FROM orders
ORDER BY order_date DESC
LIMIT 20;

-- Los 5 productos más caros
SELECT name, price FROM products ORDER BY price DESC LIMIT 5;

-- Los 5 productos más baratos
SELECT name, price FROM products ORDER BY price ASC LIMIT 5;
```

## Buenas prácticas

1. **Usa mayúsculas para palabras clave SQL**: `SELECT`, `FROM`, `WHERE`
2. **Termina cada consulta con punto y coma** (`;`)
3. **Usa nombres descriptivos para los alias**
4. **Comienza simple y ve añadiendo complejidad**

## Ejercicios del Capítulo 2

Usando DB Browser for SQLite y la base de datos TechStore:

1. Escribe una consulta que muestre todas las columnas de la tabla `customers` limitada a 10 filas.
2. Muestra solo los nombres (`first_name`) de los clientes.
3. Muestra el nombre y el precio de los productos, ordenados por precio de mayor a menor, limitado a 5.
4. ¿Cuántos productos hay con stock mayor que 0? (pista: `SELECT COUNT(*) FROM products WHERE stock > 0`)
5. Muestra los 3 productos más baratos con nombre y precio.
6. Muestra los nombres de los empleados y su puesto, ordenados por fecha de contratación.
7. Usa alias para mostrar el nombre del producto como "Producto" y el precio como "Precio".
8. ¿Qué categorías existen? Consulta la tabla `categories`.
9. Muestra los 10 pedidos más recientes con su fecha y total.
10. ¿Cuántas filas tiene la tabla `order_items`?

## Checklist de autoevaluación

- [ ] Entiendo qué es SQL y para qué sirve
- [ ] Sé escribir `SELECT` con columnas específicas
- [ ] Sé usar `LIMIT` para controlar resultados
- [ ] Sé ordenar resultados con `ORDER BY` y `DESC`/`ASC`
- [ ] Sé usar `AS` para crear alias
- [ ] Sé escribir comentarios en SQL
