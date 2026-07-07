# Capítulo 5: Introducción a dbt

## ¿Qué es dbt?

**dbt** (data build tool) es una herramienta que permite a analistas e ingenieros transformar datos en su warehouse usando SQL, con buenas prácticas de software: testing, documentación, versionado y CI/CD.

```
Fuente: Tablas raw ──► dbt models (SQL) ──► Tablas transformadas
(SQLite, Parquet)       SELECT ...             (listas para BI)
```

dbt NO extrae ni carga datos. dbt SOLO transforma (la T de ELT).

### dbt Core vs dbt Cloud

| Característica | dbt Core | dbt Cloud |
|---------------|----------|-----------|
| Coste | Gratuito (open source) | Desde ~$100/mes |
| Instalación | pip install | SaaS |
| Entorno | CLI, local | Web + CLI |
| CI/CD | Manual | Integrado |
| Documentación | dbt docs generate | Hosteada |
| Ideal para | Aprendizaje, equipos pequeños | Equipos, empresas |

En este libro usamos **dbt Core** (gratuito, local).

## Instalación

```bash
pip install dbt-core dbt-duckdb
# dbt-duckdb: permite usar DuckDB como backend (perfecto para local)
```

## Crear un proyecto dbt

```bash
dbt init techstore_dbt
cd techstore_dbt
```

Estructura generada:

```
techstore_dbt/
├── models/
│   └── example/
│       ├── my_first_dbt_model.sql
│       └── my_second_dbt_model.sql
├── analyses/
├── tests/
├── seeds/
├── macros/
├── snapshots/
├── dbt_project.yml
└── profiles.yml          # Configuración de conexión
```

## Configuración de perfiles

```yaml
# profiles.yml
techstore_dbt:
  outputs:
    dev:
      type: duckdb
      path: /data/techstore_warehouse.duckdb
      schema: main
      threads: 4
  target: dev
```

## Primer modelo dbt

dbt transforma modelos SQL en tablas o vistas en tu base de datos.

```sql
-- models/staging/stg_orders.sql
-- Este modelo limpia orders: elimina nulos, estandariza fechas
SELECT
    order_id,
    customer_id,
    CAST(order_date AS DATE) AS order_date,
    ROUND(total, 2) AS total,
    COALESCE(status, 'unknown') AS status
FROM raw_orders
WHERE total > 0
```

### Materializaciones

dbt puede materializar modelos de 4 formas:

| Materialización | Descripción | Ideal para |
|----------------|-------------|------------|
| `view` | Vista SQL (default) | Transformaciones ligeras |
| `table` | Tabla física recreada cada run | Datos de tamaño medio |
| `incremental` | Solo inserta/actualiza nuevos registros | Grandes volúmenes |
| `ephemeral` | CTE reutilizable, no se materializa | Lógica compartida |

```sql
-- models/staging/stg_orders.sql
{{ config(materialized='view') }}

SELECT ... FROM raw_orders
```

```sql
-- models/marts/fact_orders.sql
{{ config(materialized='table') }}

SELECT ... FROM {{ ref('stg_orders') }}
```

## dbt_project.yml

```yaml
# dbt_project.yml
name: 'techstore_dbt'
version: '1.0.0'
config-version: 2

profile: 'techstore_dbt'

model-paths: ["models"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]

models:
  techstore_dbt:
    staging:
      +materialized: view
      +schema: staging
    marts:
      +materialized: table
      +schema: marts
```

## Comandos básicos

```bash
# Ejecutar todos los modelos
dbt run

# Ejecutar solo un modelo específico
dbt run --select stg_orders

# Ejecutar modelos y sus dependencias
dbt run --select stg_orders+

# Compilar SQL sin ejecutar
dbt compile

# Generar documentación
dbt docs generate
dbt docs serve    # Abre servidor web con docs
```

## Sources y ref

```sql
-- models/staging/stg_orders.sql
-- Usar source() en lugar de hardcodear nombres de tabla
{{ config(materialized='view') }}

SELECT
    order_id,
    customer_id,
    CAST(order_date AS DATE) AS order_date,
    ROUND(total, 2) AS total,
    COALESCE(status, 'unknown') AS status
FROM {{ source('techstore', 'orders') }}
WHERE total > 0
```

```yml
# models/sources.yml
version: 2

sources:
  - name: techstore
    database: main
    schema: main
    tables:
      - name: orders
      - name: customers
      - name: products
      - name: order_items
```

```sql
-- models/marts/fact_orders.sql
{{ config(materialized='table') }}

SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.total,
    o.status
FROM {{ ref('stg_orders') }} o
```

## Lineage (línea de datos)

dbt genera automáticamente el **lineage** de tus modelos:

```
stg_orders ──► fact_orders ──► dashboard_ventas
stg_customers ──► dim_customers ──► dashboard_ventas
                                      │
                                      ▼
                                    reporte_ejecutivo
```

```bash
dbt docs generate
dbt docs serve
# Abre http://localhost:8080 y haz clic en "View lineage graph"
```

## Ejercicios

1. Instala dbt-core y dbt-duckdb. Inicializa un proyecto `techstore_dbt`
2. Crea un modelo `stg_customers` que limpie nombres y emails
3. Configura `profiles.yml` para usar DuckDB como warehouse local
4. Define una source `techstore` con las 4 tablas principales
5. Crea un modelo `stg_order_items` que calcule `line_total = quantity * unit_price`
6. Ejecuta `dbt run` y verifica que se crearon las vistas
7. ¿Qué diferencia hay entre `source()` y `ref()` en dbt?
8. Genera la documentación con `dbt docs generate` y explora el lineage
9. ¿Por qué es útil tener staging models separados de marts models?
10. ¿Qué materialización usarías para una tabla de 10M filas que se actualiza diario?

