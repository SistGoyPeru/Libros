# Capítulo 9: BigQuery Avanzado — Particiones, Clustering y Optimización

## El problema del full scan

Cuando ejecutas `SELECT * FROM orders`, BigQuery escanea **todas las filas de la tabla**, aunque solo necesites un mes de datos. Si la tabla tiene 10 TB, pagas por escanear 10 TB cada vez.

BigQuery ofrece dos mecanismos para evitar esto: **particiones** y **clustering**.

## Particionamiento (Partitioning)

Una tabla particionada divide los datos en segmentos basados en una columna (normalmente fecha). Al consultar con un filtro en esa columna, BigQuery solo lee las particiones relevantes.

### Tipos de particionamiento

| Tipo | Columna | Ejemplo |
|------|---------|---------|
| Por tiempo (ingesta) | `_PARTITIONTIME` | Datos del día X |
| Por columna DATE/DATETIME | Una columna date | `order_date` |
| Por entero (rango) | Columna INT64 | `customer_id` RANGE BETWEEN 1 AND 100000 |

### Crear tabla particionada

```sql
-- Particionada por order_date (costo mensual)
CREATE TABLE techstore.orders_partitioned
PARTITION BY DATE_TRUNC(order_date, MONTH)
AS
SELECT * FROM techstore.orders;

-- Particionada por día (más granular)
CREATE TABLE techstore.orders_daily
PARTITION BY order_date
OPTIONS (
  partition_expiration_days = 365  -- Borra particiones > 1 año
) AS
SELECT * FROM techstore.orders;

-- Con entero (por rango de customer_id)
CREATE TABLE techstore.customers_partitioned
PARTITION BY RANGE_BUCKET(customer_id, GENERATE_ARRAY(0, 250001, 50000))
AS
SELECT * FROM techstore.customers;
```

### Consultas en tablas particionadas

```sql
-- BigQuery solo escanea las particiones de 2024
SELECT
  DATE_TRUNC(order_date, MONTH) AS mes,
  COUNT(*) AS pedidos,
  ROUND(SUM(total), 2) AS ingresos
FROM techstore.orders_partitioned
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY mes;

-- Pseudocolumna _PARTITIONTIME (para particiones por ingesta)
SELECT DISTINCT _PARTITIONTIME FROM techstore.orders_partitioned;
```

> **Beneficio**: si tienes 5 años de datos pero filtras por 1 mes, BigQuery escanea solo ese mes (~1/60 de los datos). **Ahorro: ~98% del coste**.

## Clustering

Clustering ordena físicamente los datos dentro de cada partición según una o más columnas. No reduce el escaneo como las particiones, pero acelera las consultas con filtros en esas columnas.

### Crear tabla con clustering

```sql
CREATE TABLE techstore.orders_clustered
PARTITION BY DATE_TRUNC(order_date, MONTH)
CLUSTER BY customer_id, category
AS
SELECT * FROM techstore.orders;
```

### ¿Cuándo usar clustering?

| Situación | Recomendación |
|-----------|---------------|
| Filtros frecuentes por columna X | Clustering por X |
| Columnas con alta cardinalidad (muchos valores únicos) | Buen candidato a clustering |
| Columnas con baja cardinalidad (pocos valores, ej: categorías) | Buen candidato a clustering |
| Tablas < 1 GB | No vale la pena (overhead) |
| Consultas sin filtro | No beneficia |

**Límite**: hasta 4 columnas de clustering. El orden importa: pon primero la columna más usada en filtros.

### Clustering con múltiples columnas

```sql
CREATE TABLE techstore.orders_clustered_v2
PARTITION BY DATE_TRUNC(order_date, MONTH)
CLUSTER BY category, customer_id, status
AS
SELECT * FROM techstore.orders;
```

En este caso, las consultas que filtren por `category` serán más rápidas. Las que filtren por `status` sin `category` se beneficiarán menos.

## Buenas prácticas de optimización

### 1. Selecciona solo las columnas necesarias

```sql
-- MAL: escanea todas las columnas
SELECT * FROM orders;

-- BIEN: escanea solo 3 columnas
SELECT order_date, customer_id, total FROM orders;
```

### 2. Prefiltra antes de JOIN

```sql
-- MAL: JOIN primero, filtro después
SELECT c.name, o.total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= '2024-01-01';

-- BIEN: filtra primero, JOIN después (BigQuery lo optimiza, pero es buena práctica)
-- Usa subquery o CTE para filtrar datos antes del JOIN
WITH orders_2024 AS (
  SELECT * FROM orders WHERE order_date >= '2024-01-01'
)
SELECT c.name, o.total
FROM customers c
JOIN orders_2024 o ON c.customer_id = o.customer_id;
```

### 3. Usa LIMIT 0 para estimar coste

```sql
-- Muestra el tamaño de datos a escanear sin ejecutar realmente
SELECT * FROM techstore.orders LIMIT 0;
```

En la consola verás "Bytes que se leerán: 1.2 GB" — eso es lo que costaría un `SELECT *`.

### 4. Evita SELECT DISTINCT en columnas grandes

```sql
-- En lugar de DISTINCT sobre columna larga
SELECT DISTINCT description FROM products;

-- Considera agregar una tabla de dimensiones
-- o usar GROUP BY si necesitas agregaciones
```

### 5. Usa aproximaciones cuando sea aceptable

```sql
-- Exacto (lento en tablas enormes)
SELECT COUNT(DISTINCT customer_id) FROM orders;

-- Aproximado (rápido, margen de error ~1%)
SELECT APPROX_COUNT_DISTINCT(customer_id) FROM orders;
```

### 6. Materializa resultados intermedios

```sql
-- Si usas la misma subconsulta múltiples veces, créala como tabla
CREATE TABLE techstore.ventas_2024 AS
SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
```

## Slot-based architecture

BigQuery ejecuta consultas usando **slots** (unidades de procesamiento). Cada slot equivale aproximadamente a un core de CPU con memoria.

- **On-demand**: hasta 2000 slots simultáneos (compartidos con otros usuarios)
- **Flat-rate**: compras slots fijos (rendimiento predecible, mejor para producción)

La mayoría de usuarios empezamos con **on-demand**. Si tus consultas se vuelven lentas, puedes considerar flat-rate.

## INFORMATION_SCHEMA para monitorización

```sql
-- Consultas ejecutadas hoy
SELECT
  query,
  ROUND(total_bytes_processed / POW(1024, 3), 2) AS gb_procesados,
  total_slot_ms / 1000 AS segundos_slot,
  TIMESTAMP_DIFF(end_time, start_time, SECOND) AS duracion_seg
FROM `region-us.INFORMATION_SCHEMA.JOBS`
WHERE EXTRACT(DATE FROM creation_time) = CURRENT_DATE()
  AND job_type = 'QUERY'
ORDER BY total_bytes_processed DESC;
```

## Ejercicios

1. Crea una tabla particionada por mes con los datos de orders
2. Explica con tus palabras la diferencia entre partitioning y clustering
3. ¿Cuántas columnas de clustering puedes definir como máximo?
4. Crea una tabla clustered por `category` y `customer_id`
5. Ejecuta una consulta con y sin partición: ¿cuántos GB escanea cada una?
6. ¿Qué es un slot en BigQuery? ¿Para qué sirve?
7. Usa INFORMATION_SCHEMA.JOBS para listar las 3 consultas más caras de hoy
8. ¿Por qué SELECT * es una mala práctica en BigQuery? ¿En qué casos se justifica?
9. ¿Cuándo NO usarías particionamiento? Plantea un ejemplo
10. Crea una tabla con `partition_expiration_days = 90` y explica qué hace ese parámetro
