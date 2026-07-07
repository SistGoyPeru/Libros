# Capítulo 1: Introducción al Business Intelligence

## ¿Qué es Business Intelligence?

**Business Intelligence (BI)** es el conjunto de estrategias, procesos, arquitecturas y tecnologías que transforman datos crudos en información significativa y útil para la toma de decisiones de negocio.

No es solo software. Es una disciplina que combina:
- **Datos**: fuentes internas y externas
- **Tecnología**: herramientas de extracción, transformación, carga y visualización
- **Procesos**: ETL, modelado, actualización, gobernanza
- **Personas**: analistas, arquitectos de BI, consumidores de datos

## BI vs Analytics

| | Business Intelligence | Data Analytics |
|---|---|---|
| **Enfoque** | Qué pasó y por qué | Qué pasará y cómo optimizar |
| **Horizonte** | Histórico y presente | Predictivo y prescriptivo |
| **Output** | Dashboards, reportes, KPIs | Modelos ML, experimentos, recomendaciones |
| **Usuario** | Ejecutivos, gerentes, analistas | Científicos de datos, ingenieros |
| **Pregunta** | ¿Cuánto vendimos este mes? | ¿Qué factores predicen la venta? |
| **Herramientas** | Power BI, Looker Studio, Tableau | Python, R, TensorFlow, BigQuery ML |

BI y Analytics no son opuestos: BI responde "qué pasó", Analytics responde "qué pasará". Ambos se complementan.

## Evolución histórica del BI

```
1980s ────── Sistemas de información ejecutiva (EIS)
   │           Reportes estáticos en mainframe
   ▼
1990s ────── Data Warehousing
   │           Inmon, Kimball, star schemas
   ▼
2000s ────── BI Tradicional
   │           Cognos, BusinessObjects, MicroStrategy
   ▼
2010s ────── Self-Service BI
   │           Tableau, Power BI, Qlik
   ▼
2020s ────── BI Cloud + AI
   │           Power BI Service, Looker, ThoughtSpot
```

## Roles en un equipo de BI

| Rol | Responsabilidad |
|-----|----------------|
| **Arquitecto de BI** | Diseña la arquitectura de datos, elige herramientas, define estándares |
| **Analista de BI** | Construye dashboards, define KPIs, interpreta datos |
| **Data Engineer** | Construye y mantiene pipelines ETL/ELT |
| **Consumidor de BI** | Usa dashboards para tomar decisiones |
| **Data Steward** | Asegura calidad, gobierno y documentación de datos |

En este libro te enfocarás en los roles de **Analista de BI** y **Arquitecto de BI**.

## El ciclo de vida del BI

```
1. Identificar necesidades de negocio
   └── ¿Qué decisiones necesitamos mejorar?
2. Definir KPIs y métricas
   └── ¿Qué medimos? ¿Cómo lo medimos?
3. Obtener y preparar datos
   └── ETL/ELT, limpieza, integración
4. Modelar los datos
   └── Star schema, tablas de hechos y dimensiones
5. Construir dashboards
   └── Visualizaciones, filtros, interactividad
6. Publicar y compartir
   └── Power BI Service, permisos, programación
7. Monitorizar y mejorar
   └── Feedback, nuevas métricas, optimización
```

## El desafío de TechStore

TechStore ha crecido. Ahora tienen:
- Datos en SQLite (transaccional)
- Algunos reportes en Excel
- Datos de ventas en BigQuery (del Libro 2)

Necesitan un **sistema de BI profesional** que unifique todas las fuentes y permita a la gerencia tomar decisiones en tiempo real.

Tu misión en este libro: diseñar, construir y publicar ese sistema.

## Ejercicios

1. ¿Cuál es la diferencia entre un reporte operativo y un dashboard estratégico?
2. Identifica 3 decisiones que la gerencia de TechStore podría mejorar con BI
3. ¿Qué perfil de BI eres tú actualmente? ¿A cuál quieres llegar?
4. Investiga: ¿qué es un data-driven organization?
5. ¿Por qué el self-service BI transformó la industria?
6. ¿Qué es un KPI? Nombra 3 ejemplos para TechStore
7. ¿Cuál es la diferencia entre BI tradicional y BI cloud?
8. ¿En qué etapa del ciclo de BI crees que hay más valor agregado?
9. ¿Qué herramientas de BI has usado? ¿Cuál te gustaría aprender?
10. Diseña un diagrama del ciclo de BI para TechStore
