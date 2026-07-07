# Introducción

## De local a cloud: el salto del analista

En el Libro 1 trabajaste con datos locales: SQLite, Excel y Python en tu ordenador. En el mundo real, los datos empresariales no están en SQLite. Están en data warehouses cloud como BigQuery, Snowflake o Redshift.

Este libro te lleva de **analista local** a **analista cloud**.

## Tecnologías que usarás

| Tecnología | Propósito |
|------------|-----------|
| **Python + pandas** | Análisis y transformación de datos |
| **Matplotlib / Seaborn** | Visualización de datos |
| **Google Cloud Platform** | Infraestructura cloud |
| **BigQuery** | Data warehouse serverless |
| **Looker Studio** | Dashboards cloud |
| **Cloud Functions** | Automatización serverless |

## El proyecto central: TechStore Cloud

Seguimos con TechStore, pero ahora migrado a la nube. Trabajarás con datasets más grandes, consultas más rápidas y dashboards compartidos.

## Instalación inicial

```bash
pip install pandas numpy matplotlib seaborn pandas-gbq
```

Para BigQuery necesitarás:
1. Una cuenta de Google (gmail)
2. Un proyecto en Google Cloud Console
3. Facturación habilitada (usarás el tier gratuito)

El Apéndice C cubre la configuración paso a paso.

## Sobre el tier gratuito de GCP

Google Cloud ofrece:
- **$300 USD** en créditos gratuitos por 90 días
- **BigQuery**: 10 GB de almacenamiento y 1 TB de consultas por mes gratis
- **Cloud Functions**: 2 millones de invocaciones gratis

Puedes completar todo el libro sin gastar dinero.
