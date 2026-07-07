# Apéndice C: Costes, Licencias y Recursos de Power BI

## Planes y Costes de Power BI

| Plan | Coste | Ideal para |
|------|-------|------------|
| **Gratuito** | $0 | Aprendizaje, crear informes para uno mismo |
| **Pro** | ~$10 USD/usuario/mes | Compartir informes, colaborar, workspaces |
| **Premium Per User** | ~$20 USD/usuario/mes | IA, paginados, mayor capacidad |
| **Premium Capacity** | Desde $4,995 USD/mes | Empresas con >500 usuarios |

### ¿Qué necesitas para este libro?

- Las **licencias gratuitas** bastan para aprender Power BI Desktop
- Para **publicar y compartir** en el servicio, necesitas al menos **Pro**
- Microsoft ofrece **cuenta de prueba gratuita por 60 días** de Power BI Pro

### Free vs Pro vs Premium

| Característica | Gratis | Pro | PPU |
|----------------|--------|-----|-----|
| Power BI Desktop | ✓ | ✓ | ✓ |
| Publicar en Service | Solo Mi área | ✓ | ✓ |
| Compartir informes | ✗ | ✓ | ✓ |
| Workspaces | ✗ | ✓ | ✓ |
| Apps | ✗ | ✓ | ✓ |
| RLS | ✓ (crear) | ✓ (asignar) | ✓ |
| Actualización programada | ✗ | 8/día | 48/día |
| XMLA endpoints | ✗ | ✗ | ✓ |
| AI visuals | ✗ | ✗ | ✓ |
| Paginados | ✗ | ✗ | ✓ |
| Capacidad | 1 GB | 1 GB | 100 TB |

## Configuración de Power BI Service

### Paso 1: Crear cuenta Microsoft

1. Ve a `https://powerbi.microsoft.com`
2. "Comenzar gratis" → usa tu email personal o corporativo
3. Completa el registro

### Paso 2: Iniciar prueba Pro

1. En Power BI Service: icono de perfil → "Iniciar prueba Pro"
2. 60 días gratis, sin necesidad de tarjeta

### Paso 3: Instalar Power BI Desktop

1. Descarga de `https://powerbi.microsoft.com/desktop`
2. Instalador (~400 MB) — Windows 10+
3. Power BI Desktop se actualiza mensualmente

## Power BI Gateway

**Necesario cuando:** tus datos están en local (SQLite, Excel, SQL Server local) y quieres actualizarlos automáticamente en Power BI Service.

### Instalación

1. Descarga de `https://powerbi.microsoft.com/gateway`
2. Elige **modo personal** (para un solo usuario)
3. Registra con tu cuenta de Power BI
4. Conecta tus fuentes de datos locales

### Alternativas para evitar Gateway

1. **Migrar a BigQuery** (como en Libro 2) — Power BI se conecta directo a BigQuery
2. **Usar OneDrive/SharePoint** — Power BI Service puede leer archivos Excel/CSV desde ahí
3. **Power BI Dataflows** — ETL en la nube, sin gateway

## Troubleshooting común

### Error: "No se pudo cargar el modelo"

- Solución: reduce el tamaño del modelo, elimina tablas innecesarias
- Límite Pro: 1 GB por dataset

### Error: "RLS no funciona en el servicio"

- Solución: verifica que asignaste usuarios a los roles en "Seguridad a nivel de fila"
- Prueba con "Ver como" en el servicio

### Error: "Actualización falló"

- Solución: verifica credenciales del gateway, conectividad SQLite, ruta de archivo
- Revisa el historial de actualización para ver el error específico

### Error: "No tienes permiso para ver este informe"

- Solución: el informe está en un workspace. Pide acceso al admin
- O comparte el informe directamente desde el workspace

### Error: "USERNAME() devuelve null"

- Solución: USERNAME() funciona en el servicio, no siempre en Desktop
- Para pruebas en Desktop, usa un valor fijo temporal

## Recursos adicionales

- **Power BI Desktop (descarga)**: https://powerbi.microsoft.com/desktop
- **Power BI Service**: https://app.powerbi.com
- **Documentación oficial**: https://learn.microsoft.com/power-bi
- **Galería de informes**: https://community.powerbi.com (ver ejemplos)
- **DAX Guide**: https://dax.guide (referencia completa de funciones)
- **DAX Patterns**: https://www.daxpatterns.com (patrones de medidas)
- **Power Query M Reference**: https://learn.microsoft.com/powerquery-m
- **Comunidad Power BI**: https://community.fabric.microsoft.com
- **YouTube oficial**: Microsoft Power BI (canal oficial)
- **SQLBI**: https://www.sqlbi.com (cursos avanzados de DAX — Alberto Ferrari y Marco Russo)

## Plantilla de proyecto BI

Puedes descargar la plantilla del proyecto TechStore y adaptarla a tus datos:

1. **Archivo**: TechStore_BI.pbix (lo creaste durante el libro)
2. **Modelo**: star schema con 6 tablas
3. **Medidas**: 25+ medidas DAX documentadas
4. **RLS**: 3 roles configurados

Para usar la plantilla con tus datos:
1. Reemplaza las fuentes de datos (Power Query)
2. Ajusta las relaciones si cambian los nombres
3. Actualiza las medidas según tus KPIs
4. Configura RLS con tus usuarios y regiones
