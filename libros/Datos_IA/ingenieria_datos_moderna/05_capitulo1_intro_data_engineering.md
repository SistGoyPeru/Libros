# Capítulo 1: Introducción al Data Engineering

## ¿Qué es Data Engineering?

**Data Engineering** es la disciplina que diseña, construye y mantiene la infraestructura y los pipelines que transforman datos crudos en datos listos para análisis.

```
Datos Crudos ──► Pipeline ──► Datos Listos ──► Analistas / BI / ML
  (fuentes)       (DE)         (confiables)     (consumidores)
```

### Data Engineering vs Data Science vs Data Analysis

| Rol | ¿Qué hace? | Herramientas |
|-----|------------|-------------|
| **Data Engineer** | Construye pipelines, orquesta, garantiza calidad | Python, SQL, Airflow, dbt, Docker |
| **Data Analyst** | Explora, visualiza, genera insights | SQL, Excel, Power BI, Looker |
| **Data Scientist** | Modela, predice, experimenta | Python, ML, estadística, Jupyter |
| **Analytics Engineer** | Puente entre DE y DA: transforma datos con dbt | SQL, dbt, Python |

## El stack moderno de Data Engineering

En 2026, el stack moderno se ve así:

```
┌──────────────────────────────────────────────────┐
│                 Consumidores                      │
│  (BI Tools, ML Models, Dashboards, APIs)         │
└────────────────────┬─────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────┐
│           Data Warehouse / Lakehouse              │
│  (BigQuery, Snowflake, DuckDB, Spark)             │
└────────────────────┬─────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────┐
│           Transformación (dbt)                    │
│  Modelos, tests, documentación, lineages          │
└────────────────────┬─────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────┐
│           Orquestación (Airflow)                  │
│  DAGs, scheduling, monitoreo, alertas             │
└────────────────────┬─────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────┐
│           Data Lake / Object Storage              │
│  (MinIO, S3, GCS, ADLS) — Parquet, Avro          │
└────────────────────┬─────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────┐
│           Fuentes de Datos                        │
│  (Bases SQL, APIs, logs, archivos, streaming)    │
└──────────────────────────────────────────────────┘
```

### Herramientas de este libro

| Herramienta | Propósito |
|------------|-----------|
| **Python** | Lenguaje principal para pipelines y scripts |
| **SQL** | Consultas, transformaciones, dbt models |
| **MinIO** | Data Lake local compatible con S3 API |
| **Parquet / Avro** | Formatos columnar/binario eficientes |
| **dbt** | Transformaciones, testing, documentación |
| **Airflow** | Orquestación, scheduling, monitoreo |
| **Docker** | Contenedores para entornos reproducibles |
| **Git + GitHub Actions** | CI/CD para pipelines de datos |

## La medallion architecture (Bronze → Silver → Gold)

El patrón más usado hoy para organizar datos en un data lake:

```
Bronze ──► Silver ──► Gold
(crudo)    (limpio)   (analítico)
```

| Capa | Descripción | Formato | Dueño |
|------|-------------|---------|-------|
| **Bronze** | Datos tal cual llegan de la fuente | Parquet (crudo) | Data Engineer |
| **Silver** | Datos limpios, validados, deduplicados | Parquet (particionado) | Data Engineer |
| **Gold** | Datos agregados, modelados para negocio | Tablas SQL / vistas | Analytics Engineer |

### Ejemplo TechStore

```
Bronze:  orders_2024-01-01.parquet (crudo desde API)
Silver: orders_clean.parquet (nulos manejados, formatos estandarizados)
Gold:   fact_orders (tabla agregada por día, lista para Power BI)
```

## Pipelines: batch vs streaming

| Característica | Batch | Streaming |
|---------------|-------|-----------|
| Frecuencia | Diaria, horaria | Tiempo real (segundos) |
| Volumen | Alto por lote | Continuo, menor por unidad |
| Complejidad | Baja-media | Alta |
| Herramientas | Airflow, dbt | Kafka, Flink, Spark Streaming |
| Uso en TechStore | Reportes diarios | No aplica (por ahora) |

En este libro trabajamos con **batch** (el 90% de los casos reales).

## El pipeline de TechStore en este libro

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Extract  │───►│  Bronze  │───►│  Silver  │───►│   Gold   │
│ (Python) │    │ (MinIO)  │    │  (dbt)   │    │  (dbt)   │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │                                              │
     │ Airflow orquesta todo                        ▼
     └──────────────────────────────────────► Power BI / Análisis
```

## Ejercicios

1. ¿Cuál es la diferencia entre Data Engineer y Data Analyst?
2. ¿Qué capa de la medallion architecture contiene datos crudos?
3. ¿Por qué Parquet es mejor que CSV para un data lake?
4. Investiga qué es DuckDB y cómo se compara con SQLite
5. ¿En qué casos usarías streaming en lugar de batch?
6. ¿Qué rol juega dbt en el stack moderno?
7. ¿Qué es un pipeline de datos? Define sus 3 etapas principales
8. ¿Cuál es la ventaja de la medallion architecture frente a un solo contenedor de datos?
9. ¿Cómo encaja Airflow en el stack de TechStore?
10. ¿Qué herramienta de este libro usas ya? ¿Cuál te gustaría aprender más?
