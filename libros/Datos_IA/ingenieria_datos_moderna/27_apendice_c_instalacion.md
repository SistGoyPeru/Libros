# Apéndice C: Instalación y Configuración — Docker, Airflow, dbt

## Instalación de Docker

Docker es requisito para MinIO, Airflow, y los pipelines.

### Windows

1. Descarga Docker Desktop de https://www.docker.com/products/docker-desktop
2. Requisitos: WSL 2 habilitado, virtualización activada en BIOS
3. Instala y reinicia
4. Verifica:
```bash
docker --version
docker compose version
```

### macOS

```bash
brew install --cask docker
# O descargar de https://www.docker.com/products/docker-desktop
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install docker.io docker-compose-v2
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar
docker --version
```

## Instalación de Python y dependencias

```bash
# Verificar versión
python --version   # Debe ser 3.10+

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate   # Linux/macOS
.\venv\Scripts\activate     # Windows

# Instalar dependencias del proyecto
pip install -r requirements.txt
```

```txt
# requirements.txt (completo del libro)
pandas>=2.0
pyarrow>=15.0
boto3>=1.34
pyyaml>=6.0
dbt-core>=1.8
dbt-duckdb>=1.8
duckdb>=1.0
apache-airflow>=2.10
pytest>=8.0
ruff>=0.5
mypy>=1.10
slack-sdk>=3.27
```

## Instalación de dbt

```bash
pip install dbt-core dbt-duckdb

# Verificar
dbt --version
# core: 1.8.x, duckdb: 1.8.x

# Iniciar proyecto
dbt init techstore_dbt
```

### Configuración DuckDB

```yml
# ~/.dbt/profiles.yml
techstore_dbt:
  outputs:
    dev:
      type: duckdb
      path: /data/techstore_gold.duckdb
      schema: main
      threads: 4
    ci:
      type: duckdb
      path: /tmp/techstore_ci.duckdb
      schema: main
      threads: 2
    prod:
      type: duckdb
      path: /data/techstore_gold.duckdb
      schema: main
      threads: 8
  target: dev
```

## Levantar Airflow con Docker

```bash
# Descargar docker-compose.yaml oficial
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.0/docker-compose.yaml'

# Crear directorios necesarios
mkdir -p dags logs plugins config

# Inicializar base de datos
docker compose up airflow-init

# Iniciar Airflow
docker compose up -d

# Acceder
# http://localhost:8080 (airflow/airflow)
```

### Configuración personalizada

```yaml
# docker-compose.override.yml
services:
  airflow-webserver:
    ports:
      - "8080:8080"
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
      - ./dbt:/opt/airflow/dbt
  airflow-scheduler:
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
      - ./dbt:/opt/airflow/dbt
```

## Troubleshooting

### Docker: "Cannot connect to the Docker daemon"
- Windows: asegúrate que Docker Desktop esté corriendo
- Linux: `sudo systemctl start docker`
- Verificar: `docker ps`

### MinIO: "Access Denied"
- Verificar credenciales (MINIO_ROOT_USER / MINIO_ROOT_PASSWORD)
- Verificar signature_version: "s4v4"
- MinIO requiere firma v4

### dbt: "Could not find profile"
- Verificar que `profiles.yml` existe en `~/.dbt/` o `DBT_PROFILES_DIR`
- Ejecutar `dbt debug` para diagnosticar

### Airflow: "DAG import errors"
- Verificar sintaxis del DAG: `python dags/mi_dag.py`
- Verificar dependencias instaladas en el contenedor
- Revisar logs del scheduler

### Airflow: ModuleNotFoundError
- Los operadores adicionales requieren `pip install apache-airflow-providers-*`
- Ej: `apache-airflow-providers-slack`, `apache-airflow-providers-docker`

### GitHub Actions: "dbt not found"
- Agregar `pip install dbt-core dbt-duckdb` en el workflow
- O usar `dbt-labs/dbt-action@v1`

## Recursos adicionales

- **Docker**: https://docs.docker.com
- **MinIO**: https://min.io/docs/minio/container/index.html
- **dbt**: https://docs.getdbt.com
- **dbt Package Hub**: https://hub.getdbt.com
- **Airflow**: https://airflow.apache.org/docs
- **Airflow Providers**: https://registry.astronomer.io
- **DuckDB**: https://duckdb.org/docs
- **Parquet**: https://parquet.apache.org/docs
- **GitHub Actions**: https://docs.github.com/actions
- **Great Expectations**: https://greatexpectations.io (para calidad de datos)
- **Data Engineering Cookbook**: https://github.com/andkret/Cookbook
