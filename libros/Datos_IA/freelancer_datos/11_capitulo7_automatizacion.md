# Capítulo 7: Automatización de Informes

## 7.1 ¿Por qué Automatizar?

El tiempo es tu recurso más escaso. Cada hora que pasas haciendo manualmente lo que una máquina podría hacer es una hora que no dedicas a conseguir clientes, mejorar tu producto o descansar.

## 7.2 Plantillas de Informes

### 7.2.1 Estructura de informe que funciona

La estructura de informe que funciona consta de cinco secciones: resumen ejecutivo de un párrafo que el cliente entienda en 30 segundos; KPIs principales con 3 a 5 métricas clave y su variación respecto al período anterior; análisis detallado con gráficos e interpretación donde cada gráfico tiene su conclusión; recomendaciones con 3 a 5 acciones concretas del tipo "haz X para lograr Y"; y anexos opcionales con datos crudos, metodología y glosario.

### 7.2.2 Plantillas de dashboards que venden

Las plantillas de dashboard se dividen en tres tipos: ejecutivo, con 3 a 5 KPIs grandes, tendencia y alertas para decisiones rápidas; operativo, con tablas detalladas, filtros y drill-down para el equipo; y analítico, con segmentaciones, correlaciones y distribuciones para insights profundos.

## 7.3 Automatización con Python

### 7.3.1 Script para generar informes automáticos

Este script genera informes automáticos con Python: carga los datos desde un CSV, calcula métricas clave sumando las columnas indicadas, genera gráficos de tendencia y comparativa, crea un informe en HTML usando Jinja2 con los resultados y la imagen incrustada, y prepara el envío por email adjuntando la imagen con codificación base64. Incluye comentados los pasos de conexión SMTP para enviar el correo. Es una plantilla reutilizable para cualquier cliente.

### 7.3.2 Pipelines ligeros para freelancers

Para automatizar informes semanales, puedes usar GitHub Actions con un workflow programado que se ejecute cada lunes a las 8am. El workflow checkout el repositorio, configura Python 3.11, instala las dependencias, ejecuta el script generador de informes y sube el resultado como artefacto descargable. También permite ejecución manual con workflow_dispatch.

## 7.4 Herramientas No-Code para Automatización

No todo es código. Estas herramientas pueden reemplazar scripts simples:

| Herramienta | Para qué | Precio |
|-------------|----------|--------|
| **Zapier / Make** | Conectar apps (Google Sheets -> Gmail -> Slack) | Gratis - 20€/mes |
| **Google Apps Script** | Automatizar Google Sheets, Gmail, Calendar | Gratis |
| **Power Automate** | Automatización Microsoft (Excel, Outlook, Teams) | Gratis con Office |
| **Datawrapper** | Visualizaciones embedidas, auto-actualizables | Gratis - 50€/mes |


