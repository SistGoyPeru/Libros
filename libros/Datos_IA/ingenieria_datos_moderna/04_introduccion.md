# Introducción

## Para quién es este libro

Este libro es para ti si:
- Eres analista de datos y quieres entender cómo funcionan los pipelines por debajo
- Has usado BigQuery, Power BI o dbt y quieres orquestar todo con Airflow
- Quieres aprender data engineering moderno con herramientas open source
- Tienes datos en archivos, bases de datos o APIs y necesitas construir tuberías confiables

## Lo que necesitas

- Python 3.10+ instalado
- Docker Desktop (para MinIO, Airflow, bases de datos)
- Git
- Un editor de código (VS Code recomendado)
- 8 GB+ de RAM (16 GB ideal para Airflow + Docker)

## El proyecto TechStore

TechStore evoluciona. En Libro 2 migró a BigQuery. En Libro 3 se modeló como star schema. Ahora TechStore tiene un **data lake** completo en MinIO (S3 local), transformaciones con dbt, orquestación con Airflow, y todo corre en contenedores.

```
TechStore Data Platform
├── Data Lake (MinIO) ──── Datos crudos en Parquet
├── dbt ─────────────────── Transformaciones (Bronze → Silver → Gold)
├── Airflow ─────────────── Orquestación y scheduling
├── Docker ──────────────── Contenedores y servicios
└── CI/CD ───────────────── Despliegue automatizado
```

## Estructura del libro

4 proyectos, 15 capítulos, 4 checkpoints:

**Proyecto 1: Fundamentos** — Conceptos, Python avanzado, formatos de datos, data lakes
**Proyecto 2: dbt** — Transformaciones, modelado, testing, documentación
**Proyecto 3: Airflow** — Orquestación, DAGs, integración, monitoreo
**Proyecto 4: Producción** — Docker, CI/CD, proyecto final

Cada capítulo termina con ejercicios. Los checkpoints integran todo lo aprendido.

## Convenciones

```
Código en este formato: comandos, SQL, Python, configuración
```

**Negrita**: términos importantes, nombres de archivos, herramientas

*Cursiva*: énfasis, términos en inglés

¡Al grano!
