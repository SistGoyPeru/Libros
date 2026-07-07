# Apéndice A: Soluciones a los Ejercicios

## Capítulo 1: Introducción al BI

**Ejercicio 10 — Definiciones clave:**

1. **Business Intelligence**: disciplina que combina herramientas, procesos y tecnologías para transformar datos brutos en información útil para la toma de decisiones empresariales.
2. **OLTP**: sistemas transaccionales optimizados para escritura (ej: ERP). **OLAP**: sistemas analíticos optimizados para consultas complejas (ej: Power BI).
3. **Modelo dimensional**: técnica de modelado que organiza datos en tablas de hechos (métricas) y dimensiones (contexto), optimizada para consultas analíticas.

## Capítulo 2: Arquitectura de Datos

**Ejercicio 8 — Componentes de la arquitectura TechStore:**

| Componente | Herramienta | Propósito |
|------------|------------|-----------|
| Fuente transaccional | SQLite | Datos operacionales |
| ETL/ELT | Power Query | Limpieza y transformación |
| Data Warehouse | Star schema (SQLite) | Modelo dimensional analítico |
| BI | Power BI Desktop | Modelado y visualización |
| Distribución | Power BI Service | Portal corporativo cloud |

## Capítulo 3: Modelado Dimensional

**Ejercicio 8 — Identificar grano de las tablas:**

```sql
-- Grano: 1 fila = 1 pedido
SELECT order_id, COUNT(*) FROM orders GROUP BY order_id;

-- Grano: 1 fila = 1 línea de pedido
SELECT order_id, product_id, COUNT(*)
FROM order_items GROUP BY order_id, product_id;
```

**Ejercicio 9 — Modelo estrella SQL:**

```sql
CREATE TABLE dim_date (
    date_sk INTEGER PRIMARY KEY,
    full_date DATE NOT NULL,
    year INTEGER,
    month INTEGER,
    month_name TEXT,
    quarter INTEGER,
    day_of_week INTEGER
);

CREATE TABLE dim_customer (
    customer_sk INTEGER PRIMARY KEY,
    customer_id INTEGER,
    name TEXT,
    email TEXT,
    city TEXT,
    country TEXT,
    registration_date DATE
);

CREATE TABLE dim_product (
    product_sk INTEGER PRIMARY KEY,
    product_id INTEGER,
    name TEXT,
    category TEXT,
    unit_price REAL
);

CREATE TABLE dim_employee (
    employee_sk INTEGER PRIMARY KEY,
    employee_id INTEGER,
    name TEXT,
    email TEXT,
    region TEXT,
    role TEXT
);

CREATE TABLE fact_orders (
    order_sk INTEGER PRIMARY KEY,
    order_id INTEGER,
    date_sk INTEGER,
    customer_sk INTEGER,
    employee_sk INTEGER,
    total REAL,
    status TEXT,
    FOREIGN KEY (date_sk) REFERENCES dim_date(date_sk),
    FOREIGN KEY (customer_sk) REFERENCES dim_customer(customer_sk),
    FOREIGN KEY (employee_sk) REFERENCES dim_employee(employee_sk)
);

CREATE TABLE fact_order_items (
    item_sk INTEGER PRIMARY KEY,
    order_sk INTEGER,
    product_sk INTEGER,
    quantity INTEGER,
    unit_price REAL,
    FOREIGN KEY (order_sk) REFERENCES fact_orders(order_sk),
    FOREIGN KEY (product_sk) REFERENCES dim_product(product_sk)
);
```

## Capítulo 4: KPIs y Métricas

**Ejercicio 1 — KPI vs métrica:**
- **KPI**: métrica crítica vinculada a un objetivo estratégico (ej: "% Crecimiento de ingresos" con objetivo > 10%)
- **Métrica**: medida cuantitativa sin objetivo estratégico directo (ej: "Total de pedidos del mes")
- **Diferencia**: un KPI tiene un objetivo y una decisión asociada

**Ejercicio 5 — Ficha técnica KPI:**

```markdown
# Ficha Técnica: Ticket Promedio
Nombre: Ticket Promedio
Fórmula: AVERAGE(fact_orders[total])
Frecuencia: Mensual
Responsable: Analista BI
Objetivo: > $300
Fuente: fact_orders
```

## Capítulo 5: Power BI — Primeros Pasos

**Ejercicio 7 — Consulta SQL de conexión:**

```sql
SELECT
  o.order_id,
  o.order_date,
  o.total,
  o.status,
  c.name AS customer_name,
  c.email,
  c.city,
  c.country
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2024-01-01';
```

## Capítulo 6: Modelado en Power BI

**Ejercicio 6 — Cardinalidades:**
- `dim_product` → `fact_order_items`: 1:* (un producto aparece en muchas líneas)
- `dim_customer` → `fact_orders`: 1:* (un cliente hace muchos pedidos)
- Dirección del filtro: de dimensión a hecho (única)

## Capítulo 7: Visualizaciones en Power BI

**Ejercicio 8 — Gráfico de barras apiladas:**
1. Eje X: `dim_product[category]`
2. Eje Y: `SUM(fact_orders[total])`
3. Leyenda: `dim_date[year]`
4. Ordenar: `category` ascendente

## Capítulo 8: DAX Básico

**Ejercicio 5 — Medidas:**

```dax
-- Medida: Margen Bruto
Margen Bruto = SUM(fact_orders[total]) - SUM(fact_order_items[total_cost])

-- Medida: % Margen
% Margen = DIVIDE([Margen Bruto], SUM(fact_orders[total]), 0)

-- Medida con condición
Pedidos Altos =
CALCULATE(
    COUNTROWS(fact_orders),
    fact_orders[total] > 500
)
```

## Capítulo 9: DAX Avanzado

**Ejercicio 7 — CALCULATE + time intelligence:**

```dax
-- Ventas mismo trimestre año anterior
Ventas Mismo Trimestre Año Anterior =
CALCULATE(
    [Ingresos Totales],
    SAMEPERIODLASTYEAR(dim_date[full_date])
)

-- Crecimiento trimestral YoY
Crecimiento YoY Trimestral =
VAR ventas_actual = [Ingresos Totales]
VAR ventas_anterior = [Ventas Mismo Trimestre Año Anterior]
RETURN DIVIDE(ventas_actual - ventas_anterior, ventas_anterior, 0)
```

## Capítulo 10: Power Query ETL

**Ejercicio 6 — Merge en Power Query M:**

```powerquery
let
    Origen = Sql.Database("localhost", "techstore_bi"),
    Orders = Origen{[Schema="main",Item="orders"]}[Data],
    Customers = Origen{[Schema="main",Item="customers"]}[Data],
    Merge = Table.NestedJoin(
        Orders, {"customer_id"},
        Customers, {"customer_id"},
        "Customers", JoinKind.LeftOuter
    ),
    Expand = Table.ExpandRecordColumn(
        Merge, "Customers",
        {"name", "email", "city"},
        {"customer_name", "email", "city"}
    )
in
    Expand
```

## Capítulo 11: Data Warehousing

**Ejercicio 5 — SCD Tipo 2:**

```sql
-- Insertar nueva versión (SCD Tipo 2)
UPDATE dim_customer
SET valid_to = CURRENT_DATE,
    is_current = 0
WHERE customer_id = 123 AND is_current = 1;

INSERT INTO dim_customer (
    customer_sk, customer_id, name, email,
    city, valid_from, valid_to, is_current
) VALUES (
    (SELECT COALESCE(MAX(customer_sk), 0) + 1 FROM dim_customer),
    123, 'Alex Goyzueta', 'alex@nuevoemail.com',
    'Lima', CURRENT_DATE, '9999-12-31', 1
);
```

## Capítulo 12: Medidas Avanzadas

**Ejercicio 8 — Matriz semáforo formato condicional:**

```dax
-- Regla de formato condicional (color de fondo)
Color Semáforo =
SWITCH(
    TRUE(),
    [% Cumplimiento Ingresos] >= 1, "Green",
    [% Cumplimiento Ingresos] >= 0.8, "Yellow",
    "Red"
)
```

## Capítulo 13: Power BI Service

**Ejercicio 4 — Informe vs Panel:**
- **Informe**: vista interactiva con múltiples páginas, filtros compartidos, drill-down
- **Panel**: vista resumen con KPIs fijos (pin de un informe), sin filtros interactivos

## Capítulo 14: Seguridad RLS

**Ejercicio 5 — RLS vs OLS:**
- **RLS (Row-Level Security)**: filtra filas completas según el usuario
- **OLS (Object-Level Security)**: oculta columnas o tablas enteras
- OLS requiere **Premium** o **Premium Per User**

## Capítulo 15: Proyecto Final

**Ejercicio 8 — Plan de mantenimiento mensual:**

1. **Semana 1**: verificar actualizaciones automáticas, revisar logs
2. **Semana 2**: validar calidad de datos (nulos, duplicados, outliers)
3. **Semana 3**: recoger feedback de usuarios, priorizar mejoras
4. **Semana 4**: implementar cambios, documentar, desplegar
