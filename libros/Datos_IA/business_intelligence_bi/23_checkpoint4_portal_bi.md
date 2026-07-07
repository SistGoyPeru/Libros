# Checkpoint 4: Portal BI Corporativo

## Objetivo

Has llegado al final del libro. Este checkpoint integra todo: **publicar un portal BI corporativo completo** con Power BI Service, RLS, actualización automática y documentación.

## Requisitos

- Power BI Desktop con el modelo completo
- Cuenta de Power BI Service (gratuita o Pro)
- Modelo con medidas de Proyectos 1-3

## Paso 1: Publicar el informe final

1. Abre tu archivo TechStore_BI.pbix final
2. Verifica:
   - [ ] Todas las relaciones son correctas
   - [ ] Todas las medidas funcionan
   - [ ] Los 3 roles RLS están creados
   - [ ] Tablas auxiliares creadas (KPIs, Periodos, Seguridad)
3. Publica en Power BI Service

## Paso 2: Configurar RLS en el servicio

1. "Conjunto de datos" → tu modelo
2. "Seguridad a nivel de fila"
3. Asigna miembros a cada rol:
   - **Vendedor**: ventas@techstore.com, vendedor1@techstore.com
   - **Gerente**: gerente@techstore.com
   - **Ejecutivo**: ceo@techstore.com
4. "Guardar"
5. Prueba con "Ver como" para cada rol

## Paso 3: Crear el workspace

1. Crea workspace: "TechStore BI Corporativo"
2. Agrega miembros (simulado):
   - Tú: Admin
   - Analistas: Member
   - Gerentes: Viewer
3. Mueve el informe publicado a este workspace

## Paso 4: Crear la app

1. "Crear app" en el workspace
2. Nombre: "TechStore Analytics"
3. Descripción: "Portal de Business Intelligence de TechStore"
4. Páginas incluidas: todas
5. Tema: colores corporativos
6. "Publicar app"

## Paso 5: Configurar actualización

1. "Conjunto de datos" → "Actualizar programado"
2. Frecuencia: Diaria
3. Hora: 5:00 AM
4. Zona horaria: (tu zona)
5. Enviar notificación de fallo a tu email

## Paso 6: Documentar el sistema

Completa la ficha técnica:

```markdown
# Sistema de BI Corporativo — TechStore

## Arquitectura
- Fuente: SQLite (techstore_bi.db) / Power Query
- Modelo: Star Schema (6 tablas, 25+ medidas DAX)
- Publicación: Power BI Service (workspace corporativo)
- Seguridad: RLS (3 roles)
- Actualización: Diaria 5:00 AM

## Contenido
- 6 páginas de dashboard
- KPIs dinámicos con tabla de parámetros
- Análisis What-If (descuento)
- Matriz de Pareto (80/20)
- Cumplimiento vs objetivos

## Roles de Seguridad
- Ejecutivo: acceso total
- Gerente: filtra por región
- Vendedor: solo sus ventas

## KPIs Principales
1. Ingresos Totales: $2.45M
2. Ticket Promedio: $312
3. Clientes Activos: 1,250
4. % Crecimiento: +5.2%
5. % Cumplimiento: 98%
```

## Entregables del Checkpoint 4

- [ ] Informe publicado en Power BI Service
- [ ] Workspace "TechStore BI Corporativo" creado
- [ ] Roles RLS configurados y probados
- [ ] App "TechStore Analytics" publicada
- [ ] Actualización automática programada
- [ ] Ficha técnica del sistema documentada
- [ ] Guía rápida para usuarios

## Checklist de calidad

Antes de finalizar, verifica:

| Aspecto | Verificación |
|---------|-------------|
| Datos correctos | SUM de ingresos coincide con SQLite |
| Medidas precisas | KPIs sin errores (DIVIDE maneja cero) |
| Filtros funcionan | Slicers afectan a todos los gráficos |
| RLS aplica | Cada rol ve solo sus datos |
| Actualización OK | Gateway conectado y programado |
| App publicada | Usuarios pueden acceder |
| Documentación | Ficha técnica completa |

## Próximos pasos tras el libro

1. **Conecta fuentes reales**: reemplaza SQLite por datos reales de tu empresa
2. **Expande el modelo**: agrega más tablas de hechos (inventario, marketing)
3. **Automatiza ETL**: pipeline Python completo (Libro 2) que alimente el star schema
4. **Crea más apps**: dashboards por departamento (RRHH, Finanzas, Operaciones)
5. **Implementa alertas**: usando Power Automate + Power BI
6. **Forma usuarios**: capacita al equipo para usar los dashboards

¡Felicidades! Has completado **Business Intelligence y Modelado de Datos**. Construiste un sistema de BI corporativo completo desde cero: desde el modelo dimensional hasta la publicación en la nube con seguridad y actualización automática.

La colección **Data & Analytics Mastery** continúa:
4. Ingeniería de Datos Moderna
5. Big Data, ML e IA: Especialización Avanzada
