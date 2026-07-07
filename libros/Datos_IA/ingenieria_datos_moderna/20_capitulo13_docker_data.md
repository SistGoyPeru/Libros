# Capítulo 13: Docker para Data Engineering

## ¿Por qué Docker?

Los pipelines de datos dependen de múltiples servicios: bases de datos, object storage, orquestadores, herramientas de transformación. Docker permite empaquetar cada servicio en un contenedor reproducible.

```
Sin Docker:
  "En mi máquina funciona" → 3 días configurando dependencias

Con Docker:
  docker compose up → Todo funcionando en 30 segundos
```

## Conceptos clave

```
Imagen ──► Plantilla (read-only)
  └── docker build -t techstore-pipeline .

Contenedor ──► Instancia en ejecución de una imagen
  └── docker run techstore-pipeline

Dockerfile ──► Receta para construir la imagen

Docker Compose ──► Orquestación de múltiples contenedores
```

## Dockerfile para un pipeline Python

```dockerfile
# Dockerfile.pipeline
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY pipelines/ ./pipelines/
COPY config/ ./config/
COPY run_pipeline.py .

# Ejecutar pipeline
CMD ["python", "run_pipeline.py"]
```

```txt
# requirements.txt
pandas==2.2.0
pyarrow==15.0.0
boto3==1.34.0
pyyaml==6.0.1
sqlite3-helper==1.0.0
```

### Build y ejecución

```bash
docker build -t techstore-pipeline -f Dockerfile.pipeline .
docker run --rm -v data:/app/data techstore-pipeline
```

## Docker Compose para el stack TechStore

```yaml
# docker-compose.yml
services:
  # ── Data Lake ──
  minio:
    image: minio/minio:latest
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"
    volumes:
      - minio_data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ── Base de datos fuente ──
  sqlite:
    image: nouchka/sqlite3:latest
    volumes:
      - ./data:/data
    stdin_open: true
    tty: true

  # ── Pipeline de extracción ──
  extract:
    build:
      context: .
      dockerfile: Dockerfile.extract
    volumes:
      - ./data:/app/data
      - ./config:/app/config
    depends_on:
      minio:
        condition: service_healthy

  # ── dbt ──
  dbt:
    image: ghcr.io/dbt-labs/dbt-duckdb:latest
    volumes:
      - ./dbt:/usr/app
      - ./data:/data
    working_dir: /usr/app
    command: ["run"]

volumes:
  minio_data:
```

## Docker networks

Los contenedores se comunican entre sí a través de redes Docker:

```yaml
services:
  minio:
    networks:
      - techstore_net

  airflow:
    networks:
      - techstore_net

networks:
  techstore_net:
    driver: bridge
```

Dentro de la red, los contenedores se resuelven por nombre de servicio:

```python
# Desde el contenedor extract
s3_client = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",  # Nombre del servicio, no localhost
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin123",
)
```

## Volúmenes y persistencia

```yaml
services:
  minio:
    volumes:
      - minio_data:/data          # Volumen nombrado (persiste)
      - ./backup:/backup          # Bind mount (comparte con host)

volumes:
  minio_data:                     # Se crea automáticamente
```

## Multi-stage build para imágenes más pequeñas

```dockerfile
# Stage 1: Build
FROM python:3.11-slim AS builder
COPY requirements.txt .
RUN pip install --user --no-warn-script-location -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
COPY --from=builder /root/.local /root/.local
COPY pipelines/ ./pipelines/
COPY run_pipeline.py .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "run_pipeline.py"]

# Imagen final: ~200 MB vs ~1 GB sin multi-stage
```

## Buenas prácticas Docker para datos

1. **Imágenes pequeñas**: usa `python:3.11-slim`, no `python:3.11`
2. **Capas**: ordena las capas de menos a más cambiantes (requirements antes que código)
3. **.dockerignore**: excluye `__pycache__`, `.git`, `.env`, `data/`
4. **Healthchecks**: verifica que servicios como MinIO estén listos
5. **No correr como root**: usa `USER airflow` en imágenes de Airflow
6. **Logs a stdout**: los logs deben ir a stdout/stderr, no a archivos

```dockerfile
# Buenas prácticas
FROM python:3.11-slim

RUN addgroup --system app && adduser --system --group app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER app

CMD ["python", "run_pipeline.py"]
```

```gitignore
# .dockerignore
__pycache__/
*.pyc
.git/
.env
data/
*.md
tests/
```

## Ejercicios

1. Crea un Dockerfile para un pipeline Python que extraiga datos de SQLite
2. Construye la imagen y ejecútala con `docker run`
3. Usa Docker Compose para levantar MinIO + tu pipeline
4. Configura un healthcheck para MinIO
5. ¿Por qué es importante el orden de las capas en un Dockerfile?
6. Crea un multi-stage build para reducir el tamaño de tu imagen
7. Usa un volumen para persistir los datos de MinIO
8. ¿Cómo se comunican dos contenedores en la misma red Docker?
9. Agrega `.dockerignore` a tu proyecto
10. ¿Qué ventaja tiene usar `python:3.11-slim` en lugar de `python:3.11`?
