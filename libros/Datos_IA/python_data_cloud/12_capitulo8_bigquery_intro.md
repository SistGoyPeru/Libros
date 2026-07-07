# Capítulo 8: BigQuery — Tu Primer Data Warehouse en la Nube

## ¿Qué es BigQuery?

BigQuery es un **data warehouse** serverless y altamente escalable de Google Cloud. "Serverless" significa que no hay servidores que gestionar: Google aprovisiona, escala y mantiene la infraestructura por ti.

Características clave:
- **SQL estándar**: consultas con dialecto ANSI 2011 plus funciones propias
- **Escalado automático**: desde 1 fila hasta petabytes
- **Pago por uso**: pagas por almacenamiento + consultas ejecutadas
- **Streaming**: puedes insertar datos en tiempo real
- **Separación storage/compute**: almacenar es barato, consultar cuesta según datos escaneados

## Arquitectura de BigQuery

```
Proyecto (techstore-analytics)
  └── Dataset (techstore)
        ├── Tabla: customers
        ├── Tabla: products
        ├── Tabla: orders
        ├── Tabla: order_items
        └── Tabla: employees
```

- **Dataset**: contenedor de tablas (similar a una base de datos SQLite)
- **Tabla**: filas y columnas, como en SQL (pero almacenada en columnar format — Capacitor/ColumnIO)
- **Job**: cada consulta, carga o exportación que ejecutas

## Tu primer dataset en BigQuery

Desde la consola web:

```
1. Ve a BigQuery → console.cloud.google.com/bigquery
2. En el explorador, haz clic en los tres puntos junto a tu proyecto
3. "Crear dataset"
4. Dataset ID: techstore
5. Región: us-central1 (o la más cercana a ti)
6. "Crear dataset"
```

Desde CLI:
```bash
bq mk --dataset --location=us-central1 techstore-analytics:techstore
```

## Tu primera tabla

Puedes crear tablas de varias formas:

### Opción 1: Desde CSV en Cloud Storage

```sql
-- Esta es una consulta de carga (LOAD), no SELECT
-- Se ejecuta desde consola o bq CLI
LOAD DATA INTO techstore.customers
FROM FILES (
  format = 'CSV',
  uris = ['gs://techstore-datos/customers.csv']
)
OPTIONS (
  skip_leading_rows = 1,
  field_delimiter = ','
);
```

### Opción 2: Desde consulta SQL

```sql
CREATE TABLE techstore.ventas_resumen AS
SELECT
  categoria,
  COUNT(*) AS total_ventas,
  ROUND(SUM(total), 2) AS ingresos_totales
FROM techstore.orders
GROUP BY categoria;
```

### Opción 3: Crear tabla vacía con esquema

```sql
CREATE TABLE techstore.employees (
  employee_id INT64 NOT NULL,
  name STRING(100),
  position STRING(50),
  hire_date DATE,
  salary FLOAT64
);
```

## Tipos de datos en BigQuery

| Tipo BigQuery | Equivalente SQLite | Notas |
|-------------|-------------------|-------|
| `INT64` | `INTEGER` | Entero de 64 bits |
| `FLOAT64` | `REAL` | Coma flotante |
| `STRING` | `TEXT` | Unicode |
| `BOOL` | `INTEGER` (0/1) | Booleano |
| `DATE` | `TEXT` (formato) | Fecha sin hora |
| `DATETIME` | `TEXT` (formato) | Fecha + hora |
| `TIMESTAMP` | — | Momento exacto (con zona horaria) |
| `NUMERIC` | — | Decimal exacto de alta precisión |
| `BYTES` | `BLOB` | Datos binarios |
| `ARRAY<TIPO>` | — | Array repetido |
| `STRUCT<...>` | — | Registro anidado |

## SQL en BigQuery: diferencias con SQLite

```sql
-- SQLite
SELECT datetime('now');

-- BigQuery
SELECT CURRENT_DATETIME();
SELECT CURRENT_TIMESTAMP();

-- SQLite
SELECT * FROM orders LIMIT 10;

-- BigQuery (igual)
SELECT * FROM orders LIMIT 10;

-- BigQuery: nombre completo con proyecto.dataset.tabla
SELECT * FROM techstore-analytics.techstore.orders LIMIT 10;

-- O con backticks
SELECT * FROM `techstore-analytics.techstore.orders` LIMIT 10;

-- Puedes omitir proyecto y dataset si es el activo
SELECT * FROM orders LIMIT 10;
```

## Funciones útiles de BigQuery

```sql
-- Fechas
SELECT
  EXTRACT(YEAR FROM order_date) AS anio,
  EXTRACT(MONTH FROM order_date) AS mes,
  DATE_TRUNC(order_date, MONTH) AS mes_inicio,
  FORMAT_DATE('%Y-%m', order_date) AS anio_mes
FROM orders;

-- Strings
SELECT
  UPPER(name) AS nombre_mayus,
  LOWER(email) AS email_minus,
  CONCAT(first_name, ' ', last_name) AS nombre_completo,
  SPLIT(email, '@')[OFFSET(0)] AS usuario,
  LENGTH(name) AS longitud
FROM customers;

-- NULLs
SELECT
  COALESCE(phone, 'NO TIENE') AS telefono,
  IFNULL(email, 'sin_email@email.com') AS email
FROM customers;

-- Ventanas
SELECT
  order_id, customer_id, total,
  ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total DESC) AS rn,
  RANK() OVER (ORDER BY total DESC) AS ranking_global,
  SUM(total) OVER (PARTITION BY customer_id) AS total_cliente
FROM orders;
```

## Consultas prácticas en BigQuery

```sql
-- ¿Cuánto almacenamiento usa cada tabla?
SELECT
  table_name,
  ROUND(size_bytes / POW(1024, 3), 2) AS size_gb,
  row_count
FROM `techstore.INFORMATION_SCHEMA.TABLES`;

-- Consulta que escanea menos datos
SELECT
  DATE_TRUNC(order_date, MONTH) AS mes,
  COUNT(*) AS pedidos
FROM orders
WHERE order_date >= '2024-01-01'  -- Filtro por partición
GROUP BY mes;

-- JOINs funcionan igual que en SQLite
SELECT
  c.name,
  COUNT(o.order_id) AS num_pedidos,
  ROUND(SUM(o.total), 2) AS gasto_total
FROM orders AS o
JOIN customers AS c USING (customer_id)
GROUP BY c.name
ORDER BY gasto_total DESC;
```

## Estimación de costes antes de ejecutar

BigQuery te dice cuántos GB escaneará tu consulta **antes de ejecutarla**:

```bash
# CLI: --dry_run estima el coste sin ejecutar
bq query --dry_run "SELECT * FROM techstore.orders"

# Consola: aparece "Bytes que se leerán" arriba del botón Ejecutar
# Python: job_config.dry_run = True
```

> **Regla de oro**: 1 TB escaneado ≈ $5 USD (a precio estándar). Siempre prefiltra y selecciona solo columnas necesarias.

## Ejercicios

1. Crea el dataset `techstore` en BigQuery desde la consola web
2. ¿Cuál es la diferencia entre un dataset en BigQuery y una base de datos en SQLite?
3. Ejecuta `SELECT CURRENT_DATE() AS hoy, CURRENT_TIMESTAMP() AS ahora` en BigQuery
4. ¿Qué significa que BigQuery sea "serverless"? Nombra dos ventajas
5. Crea una tabla llamada `test` con columnas `id INT64, nombre STRING, fecha DATE`
6. Inserta 3 registros en `test` usando INSERT INTO
7. Elimina la tabla `test` con DROP TABLE
8. ¿Para qué sirve `SELECT ... FROM tabla WHERE ... LIMIT 0`? (pista: estimación de costes)
9. Usa INFORMATION_SCHEMA para listar todas las tablas de tu dataset techstore
10. Explica qué función cumple `DATE_TRUNC` y escribe un ejemplo
