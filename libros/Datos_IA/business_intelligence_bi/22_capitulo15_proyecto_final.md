# Capítulo 15: Proyecto Final — Sistema de BI Completo

## El sistema completo

En los proyectos anteriores construiste:
1. **Modelo dimensional** (star schema)
2. **Dashboard interactivo** en Power BI Desktop
3. **Medidas DAX avanzadas** y KPIs dinámicos
4. **RLS** y seguridad

Ahora es momento de integrarlo todo en un **Sistema de BI Corporativo completo** para TechStore.

## Arquitectura del sistema

```
┌──────────────────────────────────────────────────────────────────┐
│                    POWER BI SERVICE                              │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  WORKSPACE: TechStore Analytics                            │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐   │ │
│  │  │ Dashboard    │ │ Reporte      │ │ Reporte          │   │ │
│  │  │ Ejecutivo    │ │ Ventas       │ │ RRHH             │   │ │
│  │  └──────────────┘ └──────────────┘ └──────────────────┘   │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │  Conjunto de Datos: TechStore Model (RLS aplicado)   │ │ │
│  │  │  Programación: Diaria 5:00 AM (Gateway)              │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
│  A P P   D E   T E C H S T O R E   A N A L Y T I C S          │
└──────────────────────────────────────────────────────────────────┘
          ▲                    ▲                    ▲
          │                    │                    │
    ┌─────┴─────┐      ┌──────┴──────┐      ┌─────┴─────┐
    │  CEO      │      │  Gerentes   │      │  Equipo   │
    │  (todo)   │      │  (su área)  │      │  Ventas   │
    │  RLS: -   │      │  RLS: área  │      │  RLS: self│
    └───────────┘      └─────────────┘      └───────────┘
```

## Paso 1: Refinar el modelo final

Asegúrate de que tu modelo tenga:

### Modelo completo

```dax
-- Tablas del modelo
Dimensiones: dim_date, dim_customer, dim_product, dim_employee
Hechos: fact_orders, fact_order_items
Auxiliares: Tabla KPIs, Tabla Periodos, Objetivos Mensuales, Seguridad

-- Relaciones
dim_date[date_sk] → fact_orders[date_sk] (*:1)
dim_customer[customer_sk] → fact_orders[customer_sk] (*:1)
dim_employee[employee_sk] → fact_orders[employee_sk] (*:1)
dim_product[product_sk] → fact_order_items[product_sk] (*:1)
fact_orders[order_sk] → fact_order_items[order_sk] (1:*)
```

### Biblioteca de medidas completa

```dax
-- ===== PROYECTO 1: Medidas Base =====
Ingresos Totales = SUM(fact_orders[total])
Total Pedidos = COUNTROWS(fact_orders)
Ticket Promedio = AVERAGE(fact_orders[total])
Clientes Activos = DISTINCTCOUNT(fact_orders[customer_sk])

-- ===== PROYECTO 2: Medidas de Tiempo =====
Ventas YTD = TOTALYTD([Ingresos Totales], dim_date[full_date])
Crecimiento % = DIVIDE([Ingresos Totales] - [Ingresos Mes Anterior], [Ingresos Mes Anterior], 0)
% vs Objetivo = DIVIDE([Ingresos Totales], SUM(Objetivos_Mensuales[Objetivo Ingresos]), 0)

-- ===== PROYECTO 3: Medidas Avanzadas =====
KPI Dinámico = SWITCH(...)
% Acumulado Pareto = ...
Ingresos con Descuento = ...

-- ===== PROYECTO 4: Seguridad =====
Rol Vendedor: [Vendedor Email] = USERPRINCIPALNAME()
```

## Paso 2: Crear la app de Power BI

La **App** es la puerta de entrada para los usuarios finales:

1. En el workspace "TechStore Analytics", crea una app
2. Configuración:
   - **Nombre**: "TechStore Analytics"
   - **Descripción**: "Sistema de BI Corporativo — Ventas, Clientes y KPIs"
   - **Logo**: logo de TechStore (opcional)
3. **Navegación**: incluye las páginas del dashboard como secciones
4. **Permisos**: "Toda la organización" o grupos específicos
5. "Publicar app"

## Paso 3: Configurar actualización automática

Para que el sistema funcione sin intervención:

### Opción 1: Gateway + SQLite (local)
1. Instala Power BI Gateway (modo personal)
2. Conecta la fuente SQLite
3. Programa actualización diaria

### Opción 2: Datos en BigQuery
1. Migra el star schema a BigQuery (como en Libro 2)
2. Conecta Power BI a BigQuery (DirectQuery o Import)
3. Programa actualización en BigQuery (Scheduled Queries)

### Opción 3: Pipeline Python
1. Script Python que actualiza el star schema
2. Exporta a CSV
3. Power BI lee los CSVs en cada actualización

## Paso 4: Documentación del sistema

### Ficha técnica del sistema

```markdown
# Sistema de BI TechStore

## Información General
- Sistema: TechStore Analytics
- Versión: 1.0
- Fecha: 2026
- Responsable: [Tu nombre]

## Componentes
- Fuente: SQLite (techstore_bi.db)
- ETL: Power Query (6 consultas)
- Modelo: Star Schema (6 tablas)
- Medidas: 25+ medidas DAX
- Dashboards: 1 app con 6 páginas
- Seguridad: RLS por rol (Vendedor, Gerente, Ejecutivo)
- Actualización: Diaria 5:00 AM (Gateway)

## KPIs Principales
1. Ingresos Totales — SUM(fact_orders[total])
2. Ticket Promedio — AVERAGE(fact_orders[total])
3. % Crecimiento — vs mes anterior
4. % Cumplimiento — vs objetivo mensual
5. Clientes Activos — DISTINCTCOUNT(customer_sk)
```

### Glosario de términos

| Término | Definición |
|---------|------------|
| Ingresos Totales | Suma de todos los pedidos confirmados |
| Ticket Promedio | Ingreso promedio por pedido |
| % Crecimiento | Variación porcentual vs mes anterior |
| Clientes Activos | Clientes con al menos 1 compra en el período |

## Paso 5: Capacitación de usuarios

Prepara una guía rápida para los consumidores del dashboard:

### Cómo usar el dashboard

1. **Navegación**: usa las pestañas en la parte inferior
2. **Filtros**: selecciona año, mes, categoría en los slicers
3. **Drill-down**: haz clic en un dato para ver detalle
4. **Exportar**: haz clic derecho en un gráfico → "Exportar datos"

### Preguntas frecuentes

```
Q: ¿Cada cuánto se actualizan los datos?
R: Diariamente a las 5:00 AM

Q: ¿Puedo ver datos de mi región?
R: Sí, si eres gerente regional, el RLS filtra automáticamente

Q: ¿Qué hago si veo un dato incorrecto?
R: Contacta al equipo de BI: bi@techstore.com
```

## Ejercicios

1. Refina tu modelo final con todas las tablas y relaciones correctas
2. Crea una app en Power BI Service con los dashboards
3. Escribe la ficha técnica completa del sistema
4. Documenta 10 medidas con nombre, fórmula y descripción
5. Prepara una guía rápida para usuarios finales
6. Configura la actualización automática del conjunto de datos
7. ¿Qué canal usarías para recibir feedback de los usuarios?
8. Diseña un plan de mantenimiento mensual del sistema
9. ¿Cómo escalarías este sistema a 100 usuarios?
10. Prepara una presentación ejecutiva de 5 slides sobre el sistema
