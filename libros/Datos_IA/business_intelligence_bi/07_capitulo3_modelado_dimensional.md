# Capítulo 3: Modelado Dimensional — Hechos y Dimensiones

## La teoría de Kimball

Ralph Kimball definió el modelado dimensional como una aproximación para diseñar bases de datos analíticas. Sus principios:

1. **Granularidad**: define el nivel de detalle de cada fila
2. **Dimensiones**: el contexto (quién, qué, cuándo, dónde)
3. **Hechos**: las medidas (cuánto, cuántos)
4. **Hechos atómicos**: almacena al máximo detalle, agrega después

## Tablas de hechos (Fact Tables)

Contienen las **métricas** del negocio. Cada fila representa un evento.

```sql
-- Tabla de hechos: pedidos
CREATE TABLE techstore_bi.fact_orders (
  order_sk INTEGER PRIMARY KEY,  -- Surrogate Key
  order_date_sk INTEGER,         -- FK a dim_date
  customer_sk INTEGER,           -- FK a dim_customer
  employee_sk INTEGER,           -- FK a dim_employee
  order_id INTEGER,              -- Natural Key (original)
  total NUMERIC(10,2),           -- Medida
  item_count INTEGER,            -- Medida (derivada)
  status VARCHAR(20)             -- Atributo degenerado
);
```

### Tipos de hechos

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Aditivo** | Se puede sumar en todas las dimensiones | total, cantidad |
| **Semi-aditivo** | Se suma en algunas dimensiones, no en todas | saldo (no suma en tiempo) |
| **No aditivo** | No se puede sumar | precio unitario, porcentaje |

Para TechStore:
- `total` → aditivo (suma en tiempo, cliente, producto)
- `quantity` → aditivo
- `unit_price` → no aditivo (promedio, no suma)

### Surrogate Keys

En BI se usan **surrogate keys** (SK o ID artificial) en lugar de las claves naturales:

```sql
-- En lugar de usar customer_id directamente
customer_sk INTEGER REFERENCES dim_customer(customer_sk)

-- Ventajas:
-- - Independencia del sistema fuente
-- - Manejo de cambios lentos (SCD)
-- - Mejor rendimiento en JOINs
```

## Tablas de dimensión (Dimension Tables)

Contienen el **contexto** descriptivo. Son tablas anchas con muchas columnas textuales.

```sql
CREATE TABLE techstore_bi.dim_customer (
  customer_sk INTEGER PRIMARY KEY,
  customer_id INTEGER,           -- Natural Key
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(20),
  city VARCHAR(50),
  country VARCHAR(50),
  registration_date DATE,
  valid_from DATE,               -- Para SCD Tipo 2
  valid_to DATE,
  is_current BOOLEAN
);

CREATE TABLE techstore_bi.dim_date (
  date_sk INTEGER PRIMARY KEY,   -- Formato: 20240115
  full_date DATE,
  anio INTEGER,
  mes INTEGER,
  mes_nombre VARCHAR(20),
  trimestre INTEGER,
  semana INTEGER,
  dia_semana_num INTEGER,
  dia_semana_nombre VARCHAR(20),
  es_fin_semana BOOLEAN
);

CREATE TABLE techstore_bi.dim_product (
  product_sk INTEGER PRIMARY KEY,
  product_id INTEGER,
  name VARCHAR(200),
  category VARCHAR(50),
  supplier VARCHAR(100),
  price NUMERIC(10,2)
);

CREATE TABLE techstore_bi.dim_employee (
  employee_sk INTEGER PRIMARY KEY,
  employee_id INTEGER,
  name VARCHAR(100),
  position VARCHAR(50),
  hire_date DATE,
  salary NUMERIC(10,2)
);
```

## Dimensiones conformadas

Una **dimensión conformada** es una dimensión que se comparte entre múltiples tablas de hechos. Por ejemplo, `dim_date` se usa en fact_orders y fact_inventory.

En TechStore:
- `dim_date` se comparte entre todas las fact tables
- `dim_customer` se comparte entre ventas, devoluciones, marketing

## Atributos degenerados

Son atributos de la tabla de hechos que no encajan en una dimensión separada. Ejemplo: `status` o `order_number`.

Se quedan en la fact table porque:
- Tienen alta cardinalidad (muchos valores únicos)
- No comparten contexto entre hechos
- Son referencias operacionales

## Hechos sin medidas (Factless Fact Tables)

A veces necesitas una tabla de hechos sin medidas numéricas, solo con foreign keys:

```sql
-- Evento: cliente visita página web
CREATE TABLE techstore_bi.fact_pageviews (
  date_sk INTEGER,
  customer_sk INTEGER,
  page_sk INTEGER,
  session_id VARCHAR(50),
  PRIMARY KEY (date_sk, customer_sk, page_sk, session_id)
);
```

## Diseñando el star schema de TechStore

```
dim_date ◄─────────── fact_orders ───────────► dim_customer
                           │
                           ├──────────────────► dim_employee
                           │
                    fact_order_items
                           │
                           └──────────────────► dim_product
```

Estructura final:

```sql
-- Tabla de hechos: pedidos (granularidad: 1 fila = 1 pedido)
CREATE TABLE techstore_bi.fact_orders (
  order_sk INTEGER PRIMARY KEY,
  date_sk INTEGER NOT NULL,
  customer_sk INTEGER NOT NULL,
  employee_sk INTEGER NOT NULL,
  order_id INTEGER,
  total NUMERIC(10,2),
  item_count INTEGER,
  status VARCHAR(20)
);

-- Tabla de hechos: líneas de pedido (granularidad: 1 fila = 1 producto en 1 pedido)
CREATE TABLE techstore_bi.fact_order_items (
  order_item_sk INTEGER PRIMARY KEY,
  order_sk INTEGER NOT NULL,
  product_sk INTEGER NOT NULL,
  quantity INTEGER,
  unit_price NUMERIC(10,2),
  line_total NUMERIC(10,2)
);
```

## Ejercicios

1. Crea la tabla dim_date en SQLite o BigQuery para el rango 2023-2026
2. ¿Cuál es la diferencia entre natural key y surrogate key?
3. Diseña la tabla dim_product con 6 atributos descriptivos
4. ¿Qué es un hecho aditivo? Da 2 ejemplos de TechStore
5. ¿Por qué status es un atributo degenerado?
6. Convierte la tabla orders de SQLite a star schema (fact + dims)
7. ¿Qué es una dimensión conformada? ¿Cuál usarías en TechStore?
8. Investiga SCD Tipo 1, 2 y 3. ¿Cuál usarías para dim_customer?
9. Diseña una factless fact table para seguimiento de campañas de marketing
10. Crea el diagrama completo del star schema de TechStore con todas las tablas
