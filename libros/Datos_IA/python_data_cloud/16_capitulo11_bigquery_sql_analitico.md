# Capítulo 11: BigQuery — SQL Analítico y Nested Fields

## Más allá del SQL básico

En el Libro 1 dominaste SQLite con SELECT, JOIN, GROUP BY y funciones de ventana. BigQuery lleva el SQL analítico al siguiente nivel con tipos anidados, funciones de machine learning y capacidades geoespaciales.

En este capítulo explorarás las herramientas SQL que hacen de BigQuery un data warehouse analítico de clase mundial.

## Nested fields (STRUCT)

BigQuery permite columnas de tipo **STRUCT** (registros anidados). En lugar de tener tablas separadas unidas por JOIN, puedes incluir sub-registros dentro de una fila.

```sql
-- Crear tabla con columna anidada
CREATE TABLE techstore.orders_nested AS
SELECT
  o.order_id,
  o.order_date,
  o.total,
  o.status,
  STRUCT(
    c.customer_id,
    c.name,
    c.email,
    c.city
  ) AS customer,
  STRUCT(
    e.employee_id,
    e.name AS employee_name,
    e.position
  ) AS seller
FROM techstore.orders AS o
JOIN techstore.customers AS c ON o.customer_id = c.customer_id
JOIN techstore.employees AS e ON o.employee_id = e.employee_id;
```

### Consultar campos anidados

```sql
-- Acceder con punto (.)
SELECT
  order_id,
  customer.name AS cliente,
  customer.city AS ciudad,
  seller.employee_name AS vendedor
FROM techstore.orders_nested
LIMIT 10;
```

### Arrays dentro de STRUCTs

```sql
-- Crear tabla con ARRAY<STRUCT>
CREATE TABLE techstore.customer_summary AS
SELECT
  customer_id,
  name,
  email,
  ARRAY_AGG(
    STRUCT(
      order_id,
      order_date,
      total,
      status
    )
  ) AS orders
FROM techstore.orders_nested
GROUP BY customer_id, name, email;

-- Desanidar (UNNEST)
SELECT
  cs.name,
  order_details.order_id,
  order_details.total
FROM techstore.customer_summary AS cs,
UNNEST(cs.orders) AS order_details
WHERE order_details.total > 1000;
```

## Funciones analíticas avanzadas

### Percentiles y distribución

```sql
-- Percentiles del ticket promedio
SELECT
  ROUND(AVG(total), 2) AS promedio,
  APPROX_QUANTILES(total, 4)[OFFSET(1)] AS p25,
  APPROX_QUANTILES(total, 4)[OFFSET(2)] AS p50_mediana,
  APPROX_QUANTILES(total, 4)[OFFSET(3)] AS p75,
  MAX(total) AS maximo
FROM techstore.orders;
```

### Correlación

```sql
-- Correlación entre cantidad de productos y total del pedido
-- (necesitamos agregar por pedido)
WITH resumen AS (
  SELECT
    oi.order_id,
    SUM(oi.quantity) AS total_items,
    SUM(oi.quantity * oi.unit_price) AS total
  FROM techstore.order_items AS oi
  GROUP BY oi.order_id
)
SELECT
  CORR(total_items, total) AS correlacion_items_total
FROM resumen;
```

### Cohortes (análisis temporal)

```sql
-- Análisis de cohortes por mes de primera compra
WITH primera_compra AS (
  SELECT
    customer_id,
    DATE_TRUNC(MIN(order_date), MONTH) AS cohorte_mes
  FROM techstore.orders
  GROUP BY customer_id
),
actividad AS (
  SELECT
    pc.customer_id,
    pc.cohorte_mes,
    DATE_TRUNC(o.order_date, MONTH) AS mes_actividad,
    DATE_DIFF(
      DATE_TRUNC(o.order_date, MONTH),
      pc.cohorte_mes,
      MONTH
    ) AS mes_cohorte
  FROM techstore.orders AS o
  JOIN primera_compra AS pc ON o.customer_id = pc.customer_id
)
SELECT
  cohorte_mes,
  mes_cohorte,
  COUNT(DISTINCT customer_id) AS clientes_activos
FROM actividad
GROUP BY cohorte_mes, mes_cohorte
ORDER BY cohorte_mes, mes_cohorte;
```

## Window functions avanzadas

```sql
-- Diferencia mes a mes
WITH ventas_mensuales AS (
  SELECT
    DATE_TRUNC(order_date, MONTH) AS mes,
    ROUND(SUM(total), 2) AS ingresos
  FROM techstore.orders
  GROUP BY mes
)
SELECT
  mes,
  ingresos,
  LAG(ingresos) OVER (ORDER BY mes) AS mes_anterior,
  ROUND(ingresos - LAG(ingresos) OVER (ORDER BY mes), 2) AS variacion,
  ROUND(
    (ingresos - LAG(ingresos) OVER (ORDER BY mes))
    / LAG(ingresos) OVER (ORDER BY mes) * 100,
    2
  ) AS variacion_pct
FROM ventas_mensuales
ORDER BY mes;
```

```sql
-- Running total (acumulado)
WITH ventas_mensuales AS (
  SELECT
    DATE_TRUNC(order_date, MONTH) AS mes,
    ROUND(SUM(total), 2) AS ingresos
  FROM techstore.orders
  GROUP BY mes
)
SELECT
  mes,
  ingresos,
  ROUND(SUM(ingresos) OVER (ORDER BY mes), 2) AS acumulado,
  ROUND(AVG(ingresos) OVER (ORDER BY mes ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS media_movil_3m
FROM ventas_mensuales
ORDER BY mes;
```

## Expresiones regulares en BigQuery

```sql
-- Extraer dominio del email
SELECT
  email,
  REGEXP_EXTRACT(email, r'@(.+)') AS dominio,
  REGEXP_CONTAINS(email, r'gmail|hotmail|yahoo') AS es_correo_popular
FROM techstore.customers;

-- Validar formato de teléfono
SELECT
  name,
  phone,
  CASE
    WHEN REGEXP_CONTAINS(phone, r'^\+\d{2,3}\s?\d{9,10}$') THEN 'Formato válido'
    ELSE 'Formato inválido'
  END AS valido
FROM techstore.customers;
```

## Funciones de fecha avanzadas

```sql
-- Días entre pedidos por cliente
WITH pedidos_con_fechas AS (
  SELECT
    customer_id,
    order_date,
    LAG(order_date) OVER (
      PARTITION BY customer_id ORDER BY order_date
    ) AS fecha_anterior
  FROM techstore.orders
)
SELECT
  customer_id,
  order_date,
  fecha_anterior,
  DATE_DIFF(order_date, fecha_anterior, DAY) AS dias_entre_pedidos
FROM pedidos_con_fechas
WHERE fecha_anterior IS NOT NULL
ORDER BY dias_entre_pedidos DESC
LIMIT 10;
```

## Scripting en BigQuery

BigQuery soporta scripts con variables, bucles y condicionales:

```sql
-- Variables
DECLARE mes_inicio DATE DEFAULT '2024-01-01';
DECLARE mes_fin DATE DEFAULT '2024-06-30';

SELECT
  DATE_TRUNC(order_date, MONTH) AS mes,
  COUNT(*) AS pedidos
FROM techstore.orders
WHERE order_date BETWEEN mes_inicio AND mes_fin
GROUP BY mes
ORDER BY mes;
```

```sql
-- Bucle para crear tablas por mes (ejemplo conceptual)
DECLARE i INT64 DEFAULT 1;
DECLARE mes STRING;

WHILE i <= 12 DO
  SET mes = FORMAT('%04d-%02d', 2024, i);
  EXECUTE IMMEDIATE FORMAT("""
    CREATE OR REPLACE TABLE techstore.ventas_%s AS
    SELECT * FROM techstore.orders
    WHERE FORMAT_DATE('%%Y-%%m', order_date) = '%s'
  """, mes, mes);
  SET i = i + 1;
END WHILE;
```

## BQML: Machine Learning en SQL

BigQuery ML permite crear y ejecutar modelos de ML directamente con SQL:

```sql
-- Crear modelo de regresión lineal para predecir total del pedido
CREATE OR REPLACE MODEL techstore.modelo_ingresos
OPTIONS(model_type='linear_reg', input_label_cols=['total']) AS
SELECT
  o.total,
  EXTRACT(YEAR FROM o.order_date) AS anio,
  EXTRACT(MONTH FROM o.order_date) AS mes,
  EXTRACT(DAYOFWEEK FROM o.order_date) AS dia_semana,
  COUNT(DISTINCT oi.product_id) AS productos_distintos,
  SUM(oi.quantity) AS total_items
FROM techstore.orders AS o
JOIN techstore.order_items AS oi USING (order_id)
GROUP BY o.order_id, o.total, o.order_date;

-- Evaluar el modelo
SELECT * FROM ML.EVALUATE(MODEL techstore.modelo_ingresos);

-- Predecir
SELECT * FROM ML.PREDICT(
  MODEL techstore.modelo_ingresos,
  (
    SELECT
      1299.99 AS total,
      2025 AS anio,
      1 AS mes,
      2 AS dia_semana,
      3 AS productos_distintos,
      5 AS total_items
  )
);
```

## Ejercicios

1. Crea una tabla con STRUCT que combine orders y customers
2. Escribe una consulta que use UNNEST para desanidar un array
3. Calcula los percentiles 10, 50 y 90 del total de pedidos
4. ¿Qué hace APPROX_QUANTILES y por qué es útil?
5. Crea una consulta que calcule la media móvil de 3 meses de ingresos
6. Usa REGEXP_EXTRACT para extraer el nombre de usuario (antes de @) de los emails
7. ¿Qué diferencia hay entre STRUCT y ARRAY en BigQuery?
8. Escribe un script con variable para filtrar pedidos por año
9. Investiga: ¿qué otros modelos de ML soporta BQML además de regresión lineal?
10. Crea un análisis de cohortes mensual para los clientes de TechStore
