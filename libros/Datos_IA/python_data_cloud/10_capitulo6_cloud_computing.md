# Capítulo 6: Cloud Computing — Conceptos Fundamentales

## Del escritorio a la nube

Hasta ahora hemos trabajado con Python, SQL y pandas en tu máquina local. Todo corre en tu CPU, usa tu RAM y guarda archivos en tu disco duro. Esto funciona bien con datasets pequeños (TechStore: ~6000 pedidos, ~500 productos), pero ¿qué pasa cuando tienes millones de filas, terabytes de datos, o necesitas compartir resultados con tu equipo en tiempo real?

Ahí entra la **nube** (cloud computing).

En este proyecto vas a migrar TechStore desde tu SQLite local a **BigQuery**, el data warehouse en la nube de Google Cloud Platform. Pero antes de escribir consultas, necesitas entender cómo piensa la nube.

## ¿Qué es cloud computing?

Cloud computing es la entrega de recursos informáticos (servidores, almacenamiento, bases de datos, redes, software) a través de internet, bajo demanda y con pago por uso.

En lugar de comprar y mantener tus propios servidores, alquilas lo que necesitas de un proveedor como Google Cloud, AWS o Azure.

### Modelo de responsabilidad compartida

```
Tú eres responsable de:     El proveedor es responsable de:
─────────────────────────   ───────────────────────────────
Tus datos                    Hardware físico
Tu código                    Redes
Configuraciones de seguridad Virtualización
IAM (accesos)                Electricidad y refrigeración
                             Seguridad física del datacenter
```

## Tipos de servicio en la nube

| Modelo | Siglas | Ejemplo | Tú gestionas |
|--------|--------|---------|--------------|
| Infrastructure as a Service | IaaS | Compute Engine (VM) | SO, runtime, datos |
| Platform as a Service | PaaS | BigQuery, App Engine | Solo datos y código |
| Software as a Service | SaaS | Gmail, Looker Studio | Solo usar la app |
| Function as a Service | FaaS | Cloud Functions | Solo una función |

BigQuery es **PaaS**: no gestionas servidores ni discos. Solo subes datos y escribes SQL. Google se encarga del escalado y mantenimiento.

## Ventajas clave de la nube

1. **Escalado elástico**: de 0 a miles de servidores en segundos
2. **Pago por uso**: solo pagas lo que usas (storage + compute separados)
3. **Disponibilidad global**: datacenters en todo el mundo
4. **Mantenimiento cero**: el proveedor actualiza parches y hardware
5. **Seguridad**: inversión masiva en certificaciones y protecciones

## Desventajas y consideraciones

- **Costes impredecibles** si no monitorizas
- **Dependencia de internet**: sin conexión, sin acceso
- **Vendor lock-in**: migrar entre proveedores es complejo
- **Privacidad de datos**: según la legislación del país del datacenter

> **Regla práctica**: usa la nube cuando necesites escalar, compartir, o procesar datos que no caben en tu máquina. Para proyectos personales pequeños, local sigue siendo una opción válida.

## Almacenamiento en la nube: Object Storage vs Data Warehouse vs Data Lake

| Tipo | Uso | Ejemplo GCP |
|------|-----|-------------|
| Object Storage | Archivos sin procesar (CSVs, JSONs, imágenes) | Cloud Storage (GCS) |
| Data Warehouse | Datos estructurados para análisis y reporting | BigQuery |
| Data Lake | Datos brutos en formato nativo (estructurados y no) | Dataproc / GCS |
| Database | Transacciones OLTP (insert/update/delete rápidos) | Cloud SQL, Firestore |

TechStore empezó como SQLite (database local). Ahora lo moverás a BigQuery (data warehouse cloud) para análisis escalable.

## Cloud Storage (GCS) — El sistema de archivos de la nube

Antes de BigQuery, necesitas un lugar para subir tus archivos. Cloud Storage organiza los datos en **buckets** (contenedores con nombre único global).

```python
# Pseudocódigo: subir un CSV a GCS
# from google.cloud import storage
#
# cliente = storage.Client()
# bucket = cliente.get_bucket("techstore-datos")
# blob = bucket.blob("ventas/ventas_2024.csv")
# blob.upload_from_filename("ventas_2024.csv")
# print(f"Archivo subido a gs://techstore-datos/ventas/ventas_2024.csv")
```

Los buckets tienen URLs tipo `gs://techstore-datos/ventas/ventas_2024.csv` (gs = Google Storage).

## Regiones y multi-regiones

GCP organiza sus datacenters en:
- **Regiones**: `us-central1`, `europe-west1`, `southamerica-east1`
- **Multi-regiones**: `US`, `EU` (abarcan varios datacenters de un continente)
- **Dual-region**: dos regiones específicas para alta disponibilidad

Elegir región:
- Más cercana a tus usuarios → menor latencia
- Más cercana a ti → menor coste
- Considera requisitos legales de residencia de datos

## Costes en la nube: Compute vs Storage

En BigQuery (y muchos servicios cloud) pagas por separado:
- **Storage**: $ por GB/mes por datos almacenados
- **Compute**: $ por TB procesado por cada consulta

Esto cambia tu mentalidad:
- En local: preocuparte por RAM y CPU
- En BigQuery: preocuparte por cuántos GB escanea cada SELECT
- **Siempre usa SELECT \`project.dataset.table\`.columnas, no SELECT \** (esto escanea menos datos)

## Ejercicios

1. Busca tres ventajas de usar BigQuery frente a SQLite para un dataset de 10 millones de filas
2. Investiga cuánto cuesta almacenar 1 GB en BigQuery (región US) y cuánto cuesta consultar 1 TB
3. ¿Qué modelo de servicio (IaaS, PaaS, SaaS) es Cloud Storage? ¿Y Looker Studio?
4. Explica con tus palabras qué significa "pago por uso" en cloud computing
5. ¿Por qué SELECT * puede ser peligroso en un data warehouse? ¿Y en SQLite?
6. Crea una tabla comparativa: SQLite vs BigQuery (5 criterios)
7. ¿Qué es un bucket? ¿Para qué sirve en el contexto de data analytics?
8. Investiga qué es "egress" en cloud y por qué puede encarecer tu factura
9. ¿Cuándo NO deberías migrar una base de datos a la nube?
10. Busca qué es el free tier de Google Cloud y qué incluye BigQuery
