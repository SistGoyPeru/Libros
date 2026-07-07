# Capítulo 2: Arquitectura de Datos para BI

## De fuentes transaccionales a analíticas

Los sistemas transaccionales (OLTP) están optimizados para escribir y leer registros individuales rápidamente. Los sistemas analíticos (OLAP) están optimizados para leer grandes volúmenes de datos agregados.

| Característica | OLTP (Transaccional) | OLAP (Analítico) |
|---------------|---------------------|------------------|
| **Uso** | Operaciones diarias | Análisis y reporting |
| **Usuarios** | Clientes, cajeros, operadores | Ejecutivos, analistas |
| **Operaciones** | INSERT, UPDATE, DELETE | SELECT, agregaciones |
| **Datos** | Actuales, detallados | Históricos, agregados |
| **Modelo** | Normalizado (3NF) | Desnormalizado (Star Schema) |
| **Ejemplo** | SQLite de TechStore | Power BI, BigQuery |

## Arquitectura de BI en capas

```
┌──────────────────────────────────────────┐
│  Capa de Consumo (Reporting)             │
│  Power BI, Looker Studio, Excel          │
├──────────────────────────────────────────┤
│  Capa de Modelo Semántico                │
│  Tablas de hechos y dimensiones          │
│  Medidas DAX, KPIs, jerarquías           │
├──────────────────────────────────────────┤
│  Capa de Transformación (ETL/ELT)        │
│  Power Query, BigQuery, dbt             │
├──────────────────────────────────────────┤
│  Capa de Almacenamiento (Data Warehouse) │
│  BigQuery, SQL Server, Snowflake         │
├──────────────────────────────────────────┤
│  Capa de Fuentes (Orígenes de Datos)     │
│  SQLite, Excel, CSVs, APIs, CRM          │
└──────────────────────────────────────────┘
```

## Data Warehouse vs Data Mart

| | Data Warehouse | Data Mart |
|---|---|---|
| **Alcance** | Toda la organización | Un área o departamento |
| **Datos** | Integrados, corporativos | Subconjunto temático |
| **Tamaño** | Grande (TB–PB) | Pequeño (GB–TB) |
| **Tiempo** | Largo plazo (meses–años) | Corto plazo (semanas–meses) |
| **Ejemplo** | DWH corporativo de TechStore | Data Mart de Ventas |

**Estrategias de construcción:**
- **Top-Down (Inmon)**: Data Warehouse corporativo primero, luego Data Marts
- **Bottom-Up (Kimball)**: Data Marts departamentales primero, luego se integran

Para TechStore, usaremos el enfoque **Bottom-Up (Kimball)**: empezamos con un Data Mart de Ventas.

## Staging Area

Antes de cargar datos al Data Warehouse, necesitamos un área de staging:

```sql
-- Ejemplo: tabla staging en BigQuery
CREATE TABLE techstore_staging.orders_staging AS
SELECT * FROM techstore.orders
WHERE DATE(order_date) = CURRENT_DATE();
```

La staging area:
- Almacena datos crudos sin transformar
- Es temporal (se limpia después de procesar)
- Permite validar calidad antes de cargar al modelo final

## Esquema de estrella (Star Schema)

El **star schema** es el modelo de datos más usado en BI. Consiste en:

```
                    ┌─────────────┐
                    │   dim_date  │
                    │ (calendario) │
                    └──────┬──────┘
                           │
┌──────────────┐    ┌──────┴──────┐    ┌──────────────┐
│  dim_customer│◄───│  fact_orders│───►│  dim_product │
│  (clientes)   │    │  (pedidos)  │    │  (productos) │
└──────────────┘    └──────┬──────┘    └──────────────┘
                           │
                    ┌──────┴──────┐
                    │  dim_employee│
                    │ (vendedores) │
                    └─────────────┘
```

- **Tabla de hechos (fact)**: medidas numéricas (total, cantidad), foreign keys a dimensiones
- **Tablas de dimensión (dim)**: descriptivas (nombre, ciudad, categoría), texto

## Esquema de copo de nieve (Snowflake)

Variante del star schema donde las dimensiones están normalizadas:

```
dim_customer ─── dim_city ─── dim_country
dim_product  ─── dim_category
```

Ventaja: menos redundancia. Desventaja: consultas más lentas (más JOINs).

En Power BI y la mayoría de herramientas, **star schema es la recomendación estándar**.

## Tabla de calendario

Una tabla esencial en cualquier modelo de BI es la tabla de calendario (Date Dimension):

```sql
-- Generar calendario en SQL (BigQuery)
CREATE TABLE techstore.dim_date AS
SELECT
  fecha,
  EXTRACT(YEAR FROM fecha) AS anio,
  EXTRACT(MONTH FROM fecha) AS mes,
  FORMAT_DATE('%B', fecha) AS nombre_mes,
  EXTRACT(QUARTER FROM fecha) AS trimestre,
  CONCAT('Q', EXTRACT(QUARTER FROM fecha), ' ', EXTRACT(YEAR FROM fecha)) AS trimestre_nombre,
  EXTRACT(WEEK FROM fecha) AS semana,
  EXTRACT(DAYOFWEEK FROM fecha) AS dia_semana_num,
  FORMAT_DATE('%A', fecha) AS dia_semana,
  CASE WHEN EXTRACT(DAYOFWEEK FROM fecha) IN (1, 7) THEN TRUE ELSE FALSE END AS es_fin_semana
FROM UNNEST(
  GENERATE_DATE_ARRAY('2023-01-01', '2026-12-31', INTERVAL 1 DAY)
) AS fecha;
```

## Granularidad

La **granularidad** define el nivel de detalle de cada fila en la tabla de hechos. Para TechStore:

| Tabla de Hechos | Granularidad | Ejemplo |
|-----------------|-------------|---------|
| `fact_orders` | Un pedido | 1 fila = 1 pedido |
| `fact_order_items` | Un producto en un pedido | 1 fila = 1 línea de pedido |
| `fact_daily_sales` | Un día | 1 fila = 1 día de ventas |

Regla: define la granularidad antes de diseñar el modelo.

## Ejercicios

1. ¿Cuál es la diferencia entre OLTP y OLAP? Pon ejemplos de cada uno
2. Dibuja el star schema de TechStore con las 5 tablas originales
3. ¿Qué es un Data Mart? ¿Cuál sería el primer Data Mart de TechStore?
4. Explica la diferencia entre Inmon y Kimball en tus palabras
5. ¿Para qué sirve una staging area? ¿Qué datos pondrías ahí?
6. Genera la tabla dim_date en BigQuery (o SQLite) para el rango 2023-2026
7. ¿Cuál es la granularidad de la tabla order_items? ¿Y de orders?
8. ¿Por qué el star schema es recomendado para Power BI?
9. Investiga: ¿qué es un slowly changing dimension (SCD)?
10. Diseña un snowflake schema partiendo del star Schema de TechStore
