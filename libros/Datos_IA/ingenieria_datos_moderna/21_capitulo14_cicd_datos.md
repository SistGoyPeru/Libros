# Capítulo 14: CI/CD para Datos

## ¿Por qué CI/CD en datos?

El código de datos (dbt models, pipelines Python, DAGs de Airflow) debería tratarse como software: versionado, testeado y desplegado automáticamente.

```
Sin CI/CD:
  "Funciona en mi máquina" → push a main → todos los dashboards rotos

Con CI/CD:
  push → tests automáticos → deploy → pipelines verificados
```

### CI/CD vs Data CI/CD

| Aspecto | CI/CD tradicional | CI/CD para datos |
|---------|------------------|------------------|
| Testea | Código | Código + datos |
| Errores | Syntax, unit tests | Nulos, duplicados, freshness |
| Deploy | Nuevo código | Nuevos modelos + backfill |
| Rollback | git revert | dbt snapshot + rerun |

## GitHub Actions para dbt

```yaml
# .github/workflows/dbt_ci.yml
name: dbt CI

on:
  pull_request:
    branches: [main]
    paths:
      - 'dbt/**/*.sql'
      - 'dbt/**/*.yml'

jobs:
  dbt-test:
    runs-on: ubuntu-latest

    services:
      duckdb:
        image: ghcr.io/dbt-labs/dbt-duckdb:latest

    steps:
      - uses: actions/checkout@v4

      - name: Install dbt
        run: pip install dbt-core dbt-duckdb

      - name: dbt deps
        run: dbt deps
        working-directory: dbt/techstore_dbt

      - name: dbt compile
        run: dbt compile
        working-directory: dbt/techstore_dbt

      - name: dbt test (schema only)
        run: dbt test --select test_type:singular
        working-directory: dbt/techstore_dbt

      - name: dbt docs generate
        run: dbt docs generate
        working-directory: dbt/techstore_dbt

      - name: Upload docs artifact
        uses: actions/upload-artifact@v4
        with:
          name: dbt-docs
          path: dbt/techstore_dbt/target/
```

## GitHub Actions para pipelines Python

```yaml
# .github/workflows/pipeline_ci.yml
name: Pipeline CI

on:
  push:
    branches: [develop, main]
    paths:
      - 'pipelines/**'
      - 'config/**'
      - 'requirements.txt'

jobs:
  test-pipeline:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-mock

      - name: Run unit tests
        run: pytest tests/ -v

      - name: Lint with Ruff
        uses: astral-sh/ruff-action@v1
        with:
          src: "./pipelines"

      - name: Type check with mypy
        run: mypy pipelines/
```

## Tests para pipelines

```python
# tests/test_extract.py
import pytest
from pipelines.extract import extract_table
from pathlib import Path

def test_extract_orders_returns_parquet(tmp_path):
    """Extracción de orders debe generar un archivo Parquet válido."""
    result = extract_table("orders", tmp_path)
    assert result.exists()
    assert result.suffix == ".parquet"
    assert result.stat().st_size > 0

def test_extract_customers_columns(tmp_path):
    """Extracción de customers debe incluir columnas esperadas."""
    import pandas as pd
    result = extract_table("customers", tmp_path)
    df = pd.read_parquet(result)
    expected = {"customer_id", "name", "email", "city", "country"}
    assert expected.issubset(set(df.columns))

def test_extract_orders_no_negative_totals(tmp_path):
    """Ningún pedido debe tener total negativo."""
    import pandas as pd
    result = extract_table("orders", tmp_path)
    df = pd.read_parquet(result)
    assert (df["total"] >= 0).all()
```

## CI/CD para DAGs de Airflow

```yaml
# .github/workflows/airflow_ci.yml
name: Airflow DAG CI

on:
  pull_request:
    paths:
      - 'airflow/dags/**'

jobs:
  validate-dags:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Airflow
        run: |
          pip install apache-airflow==2.10.0
          pip install -r airflow/requirements.txt

      - name: Initialize Airflow DB
        run: airflow db init

      - name: Validate DAGs
        run: airflow dags list --output yaml
        working-directory: airflow

      - name: Test DAG integrity
        run: python -c "
from airflow.models import DagBag
dagbag = DagBag(dag_folder='dags')
assert len(dagbag.import_errors) == 0, f'DAG errors: {dagbag.import_errors}'
print(f'DAGs válidos: {len(dagbag.dags)}')
"
        working-directory: airflow
```

## dbt CI: pruebas en PRs

```yaml
# .github/workflows/dbt_pr.yml
name: dbt PR Checks

on:
  pull_request:
    paths:
      - 'dbt/**'

jobs:
  dbt-ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install dbt
        run: pip install dbt-core dbt-duckdb

      - name: dbt debug
        run: dbt debug
        working-directory: dbt/techstore_dbt

      - name: dbt deps
        run: dbt deps
        working-directory: dbt/techstore_dbt

      - name: dbt compile
        run: dbt compile --target ci
        working-directory: dbt/techstore_dbt

      - name: dbt run (limited)
        run: dbt run --select staging --target ci
        working-directory: dbt/techstore_dbt

      - name: dbt test
        run: dbt test --target ci
        working-directory: dbt/techstore_dbt

      - name: Comment PR on failure
        if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '❌ dbt tests failed. Check run: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}'
            })
```

## Deploy automatizado

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy-pipeline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t techstore-pipeline:latest .

      - name: Push to registry
        run: |
          docker tag techstore-pipeline:latest ghcr.io/${{ github.repository }}/pipeline:latest
          docker push ghcr.io/${{ github.repository }}/pipeline:latest

      - name: Deploy Airflow DAGs
        run: |
          rsync -avz airflow/dags/ airflow-server:/opt/airflow/dags/
          ssh airflow-server "airflow dags trigger techstore_complete"
```

## Buenas prácticas de CI/CD para datos

1. **Testea en PRs**: no esperes a main para descubrir errores
2. **Entorno CI efímero**: usa DuckDB o SQLite en CI (no dependas de infraestructura real)
3. **Testea datos + código**: schema tests + unit tests + integration tests
4. **Cachea dependencias**: `pip install` con cache para builds más rápidos
5. **Comentarios automáticos**: dbt test falla → comenta en el PR qué falló
6. **Deploy progresivo**: primero staging, luego producción

## Ejercicios

1. Crea un workflow de GitHub Actions que ejecute `dbt compile` en cada PR
2. Agrega un paso que ejecute `dbt test` solo en modelos modificados
3. Escribe tests unitarios para tu pipeline `extract_table`
4. Crea un workflow que valide que los DAGs de Airflow se importan correctamente
5. ¿Por qué es importante testear en PRs y no solo en main?
6. Implementa un step que comente el PR con el resultado de dbt test
7. ¿Qué ventaja tiene DuckDB como target de CI frente a una base real?
8. Configura Ruff (linter) en el workflow CI
9. Crea un deploy job que reconstruya la imagen Docker y la suba a un registry
10. ¿Cómo harías rollback de un modelo dbt desplegado con errores?
