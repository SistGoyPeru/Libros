# Capítulo 13: Power BI Service — Publicación y Colaboración

## ¿Qué es Power BI Service?

Power BI Service es la plataforma cloud donde publicas, compartes y colaboras con tus dashboards.

```
Power BI Desktop ──► Power BI Service ──► Consumidores
(crear modelo)        (publicar)           (ver dashboards)
```

### Planes de Power BI Service

| Plan | Coste | Características |
|------|-------|-----------------|
| **Gratuito** | $0 | Solo ver contenido propio. No compartir |
| **Pro** | ~$10 USD/usuario/mes | Compartir, colaborar, workspaces |
| **Premium Per User** | ~$20 USD/usuario/mes | AI, paginados, mayores límites |
| **Premium Capacity** | Desde $5K USD/mes | Dedicado, sin licencias por usuario |

Para este libro, usaremos la **versión gratuita** para publicar y la **versión Pro** para compartir.

## Publicar desde Power BI Desktop

1. En Power BI Desktop: "Publicar" (cinta Inicio)
2. Inicia sesión con tu cuenta Microsoft (gratuita)
3. Selecciona el espacio de trabajo:
   - "Mi área de trabajo" (personal, gratuito)
   - Un workspace compartido (requiere Pro)
4. Haz clic en "Seleccionar"

El informe se publica como:
- **Informe**: las visualizaciones con filtros interactivos
- **Conjunto de datos**: el modelo de datos (tablas, medidas, relaciones)
- **Panel**: (opcional) puedes crear un panel con KPIs fijos

## Workspaces

Los **workspaces** son contenedores lógicos para organizar informes:

```
Workspace: "TechStore BI"
  ├── Informe: Resumen Ejecutivo
  ├── Informe: Ventas por Producto
  ├── Informe: KPIs Gerenciales
  ├── Conjunto de datos: TechStore Modelo
  └── Panel: KPIs TechStore
```

### Crear un workspace

1. En Power BI Service: "Workspaces" → "Crear workspace"
2. Nombre: "TechStore Analytics"
3. Descripción: "Dashboards de ventas TechStore"
4. Configura:
   - **Tipo de workspace**: Workspace clásico o basado en app
   - **Contacto**: tu email
5. "Guardar"

### Roles en workspaces

| Rol | Permisos |
|-----|----------|
| **Admin** | Todo: editar, compartir, agregar miembros |
| **Member** | Publicar, editar, compartir contenido |
| **Contributor** | Publicar y editar contenido |
| **Viewer** | Solo ver contenido |

## Compartir informes

### Opción 1: Compartir directamente

1. Abre el informe en Power BI Service
2. "Compartir" (arriba a la derecha)
3. Ingresa emails de los destinatarios
4. Permisos: "Permitir que los destinatarios compartan" (opcional)
5. "Compartir"

### Opción 2: Publicar en toda la organización

1. "Archivo" → "Publicar en la web" (público — cuidado con datos sensibles)
2. O "Incrustar" en SharePoint o sitio web corporativo

### Opción 3: Apps de Power BI

1. En el workspace, "Crear app"
2. Selecciona los informes y paneles a incluir
3. Configura navegación, colores, logo
4. Publica la app para los usuarios

## Programación de actualización

Los datos locales (SQLite, Excel) no se actualizan automáticamente en la nube. Necesitas:

### Gateway de datos (on-premises)

1. Descarga e instala **Power BI Gateway** (modo personal)
2. Configura la conexión a tu archivo SQLite/CSV
3. En Power BI Service:
   - Configuración del conjunto de datos → "Gateway"
   - Conecta al gateway instalado
   - Programa actualización: diaria, horaria

### Gateway para SQLite

Power BI Service no tiene conector nativo a SQLite. Alternativas:
1. Migra datos a BigQuery (ya lo hiciste en Libro 2)
2. Usa Excel como intermediario (exporta SQLite → Excel → Power BI)
3. Configura un pipeline Python que actualice CSVs y Power BI los lea

### Programar actualización

1. En Power BI Service: "Conjuntos de datos" → tu dataset
2. "Actualizar programado"
3. Frecuencia: Diario
4. Zona horaria: (tu zona)
5. Hora: 5:00 AM

## Suscripciones a informes

Power BI permite enviar informes por email automáticamente:

1. Abre el informe
2. "Suscribirse" → "Agregar suscripción"
3. Configura:
   - Frecuencia: Diaria, semanal, mensual
   - Hora de envío
   - Asunto del email
   - Destinatarios
4. "Guardar"

Los suscriptores reciben el informe como PDF adjunto.

## Métricas de uso

Power BI Service proporciona analytics de uso:

1. "Configuración" → "Métricas de uso"
2. Verás:
   - Vistas por informe
   - Usuarios únicos
   - Compartidos
   - Tendencias de uso

## Ejercicios

1. Publica tu informe TechStore_BI.pbix en Power BI Service
2. Crea un workspace llamado "TechStore Analytics"
3. Comparte tu informe con un compañero (o con tu otro email)
4. ¿Cuál es la diferencia entre Informe y Panel en Power BI Service?
5. Programa una actualización diaria de tu conjunto de datos
6. Crea una suscripción semanal para recibir el informe por email
7. ¿Qué es Power BI Gateway y cuándo se necesita?
8. ¿Qué plan de Power BI necesitas para compartir informes?
9. Explora las métricas de uso de tu informe publicado
10. ¿Cómo manejarías datos sensibles al publicar en la web?
