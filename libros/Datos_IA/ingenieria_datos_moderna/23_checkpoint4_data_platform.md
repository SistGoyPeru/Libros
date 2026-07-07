# Checkpoint 4: Data Platform Corporativa

## Objetivo

Integrar todos los componentes en una **Data Platform corporativa** completa con CI/CD, documentación y runbook de operaciones.

## Requisitos

- Docker Desktop
- Python 3.10+
- Git + GitHub (o GitHub alternativo)
- Proyectos de los Checkpoints 1-3 funcionando

## Paso 1: Repositorio completo

```bash
mkdir -p techstore-data-platform && cd techstore-data-platform
git init
```

Copia y organiza los archivos de los checkpoints anteriores en la estructura del Capítulo 15.

## Paso 2: Configurar CI/CD

```yaml
# .github/workflows/ci.yml
name: TechStore Data Platform CI

on:
  pull_request:
    branches: [main]

jobs:
  test-extract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v

  validate-dbt:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install dbt-core dbt-duckdb
      - run: dbt deps && dbt compile
        working-directory: dbt/techstore_dbt

  validate-airflow:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install apache-airflow==2.10.0
      - run: airflow db init && python -c "
from airflow.models import DagBag
dag = DagBag(dag_folder='airflow/dags')
assert not dag.import_errors, f'Errors: {dag.import_errors}'
print(f'{len(dag.dags)} DAGs OK')
"
```

## Paso 3: Ficha técnica del sistema

```markdown
# Ficha Técnica — TechStore Data Platform

## Información General
- Sistema: TechStore Data Platform
- Versión: 1.0
- Fecha: 2026
- Responsable: [Tu nombre]

## Componentes
- Fuente: SQLite (techstore.db)
- Data Lake: MinIO (S3-compatible)
- Formato: Parquet (columnar, comprimido)
- Transformación: dbt (DuckDB)
- Orquestación: Apache Airflow 2.10
- Contenedores: Docker Compose
- CI/CD: GitHub Actions
- Documentación: dbt docs + README

## Pipeline (diario 6:00 AM)
| Paso | Duración estimada |
|------|-------------------|
| Extract | 2 min |
| Load to Bronze | 1 min |
| dbt Run | 5 min |
| dbt Test | 2 min |
| dbt Docs | 1 min |
| **Total** | **~11 min** |

## Estructura del Data Lake
- Bronze: datos crudos en Parquet (schema-on-read)
- Silver: datos limpios y validados
- Gold: datos modelados para BI (DuckDB)

## Servicios
| Servicio | Puerto | Credenciales |
|----------|--------|-------------|
| Airflow | 8080 | admin / admin |
| MinIO API | 9000 | minioadmin / minioadmin123 |
| MinIO Console | 9001 | minioadmin / minioadmin123 |
```

## Paso 4: Verificación final

```bash
# 1. Verificar servicios
docker compose ps
# Todos deben mostrar "Up"

# 2. Verificar DAGs en Airflow
curl http://localhost:8080/api/v1/dags -u admin:admin

# 3. Verificar datos en MinIO
curl http://localhost:9001/api/v1/buckets -u minioadmin:minioadmin123

# 4. Ejecutar pipeline manual
# Airflow UI → DAG → Trigger DAG

# 5. Verificar logs
# Airflow → DAG → ultima run → logs

# 6. Verificar dbt docs
# ls dbt/techstore_dbt/target/
```

## Paso 5: Onboarding document

```markdown
## Onboarding: Nuevo miembro del equipo TechStore Data

### Día 1
1. Clonar repo: `git clone https://github.com/techstore/data-platform`
2. Copiar `.env.example` → `.env` y configurar
3. `docker compose up -d`
4. Verificar Airflow: http://localhost:8080 (admin/admin)

### Día 2
1. Explorar DAGs existentes en Airflow
2. Leer modelos dbt en `dbt/techstore_dbt/models/`
3. Ejecutar `dbt docs serve` y explorar lineage

### Día 3
1. Hacer un cambio pequeño en un modelo dbt
2. Crear PR → esperar CI → mergear
3. Verificar deploy en Airflow

### Semana 1
1. Entender el pipeline completo
2. Hacer un backfill de un mes de datos
3. Agregar un test nuevo a un modelo existente
```

## Entregables del Checkpoint 4

- [ ] Repositorio completo con estructura estándar
- [ ] CI/CD funcionando (GitHub Actions)
- [ ] Docker Compose con todos los servicios
- [ ] Pipeline orquestado en Airflow
- [ ] dbt models con tests y documentación
- [ ] Datos accesibles desde BI (Power BI / Looker)
- [ ] Ficha técnica del sistema documentada
- [ ] Onboarding document para nuevos miembros
- [ ] Runbook de operaciones

## Checklist de calidad

| Aspecto | Verificación |
|---------|-------------|
| Datos correctos | dbt tests pasan (0 fallos) |
| Pipeline corre | Airflow muestra última run exitosa |
| CI/CD activo | GitHub Actions último PR verde |
| Docker | Todos los servicios "Up" |
| Documentación | dbt docs serve funcionando |
| Extract OK | Parquet en MinIO bronze |
| Transform OK | Gold accesible desde DuckDB |
| Reproducible | `git clone && docker compose up` funciona |

## Próximos pasos

1. **Conecta fuentes reales**: reemplaza SQLite por PostgreSQL, APIs, o streaming (Kafka)
2. **Escala a cloud**: migra MinIO a S3/GCS, DuckDB a Snowflake/BigQuery
3. **Agrega calidad**: Great Expectations para validación avanzada
4. **Real-time**: Kafka + Spark Streaming para datos en tiempo real
5. **Data Mesh**: distribuye la propiedad de datos entre equipos
6. **ML Pipeline**: agrega feature store y modelos ML orquestados

¡Felicidades! Has construido una Data Platform corporativa completa desde cero. Esto es lo que las empresas modernas usan para mover, transformar y orquestar datos a escala.

La colección **Data & Analytics Mastery** continúa:
**Libro 5**: Big Data, ML e IA: Especialización Avanzada
