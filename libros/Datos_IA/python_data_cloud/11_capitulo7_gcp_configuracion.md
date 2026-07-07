# Capítulo 7: Google Cloud Platform — Configuración y Autenticación

## Crea tu cuenta de GCP

Para seguir este libro necesitas una cuenta de Google Cloud Platform. No te preocupes: BigQuery tiene un **free tier** generoso que cubre 10 GB de almacenamiento y 1 TB de consultas por mes.

### Paso 1: Crear cuenta

1. Ve a https://console.cloud.google.com
2. Inicia sesión con tu cuenta de Google (o crea una nueva)
3. Acepta los términos del servicio
4. Proporciona datos de facturación (te piden tarjeta, pero no te cobrarán mientras uses free tier)
5. Completa el registro

> **Importante**: GCP te da $300 en créditos gratis por 90 días al crear tu primera cuenta. Puedes usar esto para experimentar sin riesgo.

### Paso 2: Crear un proyecto

Un proyecto en GCP es el contenedor lógico que agrupa tus recursos, facturación y permisos.

```
1. En la consola, haz clic en el selector de proyectos (arriba a la izquierda)
2. Haz clic en "Nuevo proyecto"
3. Nombre: "techstore-analytics"
4. Ubicación: déjala por defecto (sin organización)
5. Haz clic en "Crear"
```

Anota el **Project ID** (suele ser `techstore-analytics-XXXXX`). Lo usarás en cada consulta.

### Paso 3: Habilitar APIs

Cada servicio en GCP requiere habilitar su API:

```
1. Ve a "APIs y servicios" → "Biblioteca"
2. Busca y habilita:
   - BigQuery API
   - Cloud Storage API
3. Espera 1-2 minutos a que se activen
```

## Autenticación: Service Accounts

Tu ordenador necesita identificarse ante Google Cloud para usar sus servicios. Hay dos formas principales:

| Método | Cuándo usarlo |
|--------|---------------|
| **gcloud CLI** | Desarrollo local, pruebas rápidas |
| **Service Account (JSON key)** | Código producción, automatización, scripts |

Usaremos **gcloud CLI** para desarrollo y **Service Account** para los scripts Python.

### Opción A: gcloud CLI (recomendada para desarrollo)

Instala Google Cloud SDK:

```
# Windows: descarga de https://cloud.google.com/sdk/docs/install
# O usa winget:
winget install Google.CloudSDK
```

Luego autentícate:

```bash
gcloud auth login
# Se abre tu navegador para autorizar
```

Configura tu proyecto activo:

```bash
gcloud config set project techstore-analytics-XXXXX
```

Verifica:

```bash
gcloud config list
gcloud auth list
```

### Opción B: Service Account (para código Python)

1. En la consola: IAM y Admin → Service Accounts
2. Haz clic en "Crear service account"
3. Nombre: `techstore-python`
4. Roles: BigQuery → BigQuery Admin, Storage → Storage Admin
5. Haz clic en "Hecho"
6. Selecciona la cuenta, ve a "Claves" → "Agregar clave" → JSON
7. Se descarga un archivo .json con las credenciales

Guarda este archivo de forma segura (nunca lo subas a GitHub). Lo cargarás en Python así:

```python
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "ruta/a/tu-archivo-credenciales.json"
)
cliente = bigquery.Client(credentials=credentials, project="techstore-analytics-XXXXX")
```

## IAM — Quién puede hacer qué

IAM (Identity and Access Management) es el sistema de permisos de GCP. Sus tres componentes:

- **Quién**: cuenta de Google, service account, grupo
- **Rol**: conjunto de permisos (BigQuery Admin, BigQuery Data Viewer, etc.)
- **Recurso**: proyecto, dataset, tabla

Principio de **mínimo privilegio**: asigna solo los roles necesarios.

| Rol BigQuery | Permisos |
|-------------|----------|
| `bigquery.user` | Ejecutar consultas, crear datasets |
| `bigquery.dataViewer` | Leer datos y metadatos |
| `bigquery.dataEditor` | Crear/modificar tablas |
| `bigquery.admin` | Control total |
| `bigquery.jobUser` | Ejecutar trabajos (consultas/cargas) |

Para este libro, asigna **BigQuery Admin** (es tu proyecto personal; en producción serías más restrictivo).

## gcloud CLI — Comandos esenciales

```bash
# Ver proyectos disponibles
gcloud projects list

# Ver datasets de BigQuery
bq ls

# Ejecutar consulta SQL directa desde terminal
bq query "SELECT 1 AS numero"

# Ver información de una tabla
bq show techstore:ventas

# Subir archivo a Cloud Storage
gcloud storage cp ventas.csv gs://techstore-datos/
```

## gcloud auth application-default

Para que tu código Python funcione sin cargar credenciales explícitamente:

```bash
gcloud auth application-default login
```

Esto crea credenciales por defecto que bibliotecas como `google-cloud-bigquery` usarán automáticamente.

```python
from google.cloud import bigquery

# Sin credenciales explícitas — usa ADCs (Application Default Credentials)
cliente = bigquery.Client()
```

## Ejercicios

1. Crea un proyecto en GCP llamado "techstore-analytics" y escribe aquí el Project ID
2. ¿Qué diferencia hay entre `gcloud auth login` y `gcloud auth application-default login`?
3. ¿Para qué sirve una service account? ¿Cuándo usarías una vs tu cuenta personal?
4. Habilita la API de BigQuery y la de Cloud Storage en tu proyecto
5. Instala gcloud CLI (o verifica que ya lo tienes con `gcloud --version`)
6. Enumera 5 roles de IAM en BigQuery y explica cada uno brevemente
7. ¿Qué significa "mínimo privilegio" en seguridad cloud?
8. Autentícate con `gcloud auth login` y configura tu proyecto activo
9. Explica por qué nunca debes subir un archivo JSON de service account a un repositorio público
10. Ejecuta `bq query "SELECT CURRENT_DATE() AS hoy"` desde tu terminal y pega el resultado
