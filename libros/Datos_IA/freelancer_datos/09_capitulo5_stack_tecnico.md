# Capítulo 5: Stack Técnico del Freelancer

## 5.1 El Stack Mínimo Viable

No necesitas 20 herramientas. Necesitas las correctas. Este es el stack que recomiendo para cualquier freelancer de datos:

### 5.1.1 Esenciales (empieza aquí)

Las herramientas esenciales para empezar como freelancer de datos incluyen SQL con DuckDB o PostgreSQL (no negociable), Python con pandas y matplotlib como navaja suiza, una herramienta de BI como Power BI o Tableau (elige una y domínala), Excel con Power Query para clientes pequeños, y Streamlit u Observable para prototipos y dashboards ligeros.

### 5.1.2 Stack intermedio (cuando crezcas)

Cuando crezcas como freelancer, incorpora herramientas intermedias: dbt para transformaciones ETL, Airflow solo si necesitas orquestación, BigQuery o Snowflake como data warehouse serverless, Jupyter y VS Code con extensiones para notebooks, Git con GitHub para control de versiones, y Ollama con modelos open source para IA local sin enviar datos a terceros.

## 5.2 Recomendaciones por Tipo de Proyecto

| Tipo de proyecto | Stack recomendado |
|------------------|-------------------|
| Dashboard simple | Power BI + Excel + SQL |
| Análisis exploratorio | Python (pandas) + Jupyter |
| ETL / limpieza | Python + dbt + BigQuery |
| Automatización de informes | Python + GitHub Actions + Streamlit |
| ML básico | scikit-learn + Python + MLflow |
| Consultoría estratégica | SQL + Excel + PowerPoint (los informes ejecutivos) |

## 5.3 Productividad para Freelancers

Las herramientas de productividad recomendadas incluyen Notion para gestión de proyectos, Toggl para time tracking, Calendly para agendar reuniones, Google Drive o OneDrive para compartir entregables, Slack o Discord para comunicación con clientes por canal, y Grammarly o LanguageTool como corrector para informes profesionales.

## 5.4 Hardware Recomendado

No necesitas un servidor. Necesitas:

- **Laptop**: 16 GB RAM mínimo, 32 GB ideal. Procesador i7 o Mx.
- **Pantalla externa**: 27" mínimo. Dos pantallas cambian tu productividad.
- **Buen internet**: Prioridad #1. Invierte en un plan estable, no en el más barato.
- **Nube**: Google Cloud / AWS (capa gratuita es suficiente para proyectos pequeños).

## 5.5 Plantilla de Análisis Rápido

Este script Python es tu plantilla para cualquier proyecto nuevo. Copia, pega y adapta:

Este script de plantilla realiza el flujo completo de análisis para un nuevo proyecto: carga un CSV, limpia datos eliminando nulos en columnas críticas, calcula métricas clave como ingresos totales y ticket promedio, agrupa por producto y exporta los resultados a Excel, y genera automáticamente un gráfico de barras con los 10 productos principales. Está diseñado para copiarse y adaptarse a cada proyecto cambiando el nombre del cliente y la ruta del archivo de datos.

Guarda esto como `template_analisis.py`. Lo usarás en cada proyecto nuevo.


