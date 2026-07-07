# Capítulo 7: Visualizaciones y Diseño de Dashboards

## Principios de diseño de dashboards

Un buen dashboard no es solo gráficos bonitos. Es comunicación efectiva.

### Los 5 principios de Tufte

| Principio | Aplicación en Power BI |
|-----------|----------------------|
| **Integridad** | Los datos deben hablar, no decorar |
| **Contexto** | Compara con target, histórico, benchmark |
| **Proporción** | Escalas correctas (no distorsionar) |
| **Simplicidad** | Menos ink = más información |
| **Enfoque** | Un dashboard, una historia |

### Jerarquía visual

```
Arriba ─ Izquierda: KPIs principales (lo más importante)
Arriba ─ Derecha: KPIs secundarios
Centro: Tendencia principal
Abajo: Detalles y desgloses
```

## Tipos de visualización y cuándo usarlas

### KPIs y métricas únicas

| Visual | Uso | Ejemplo TechStore |
|--------|-----|-------------------|
| **Tarjeta** | Un solo número | Ingresos totales: $2.5M |
| **Tarjeta múltiple** | Varios KPIs | Ingresos, Pedidos, Clientes |
| **Medidor (Gauge)** | vs objetivo | Ingresos vs target $150K |

### Comparaciones

| Visual | Uso | Ejemplo TechStore |
|--------|-----|-------------------|
| **Barra** | Comparar categorías | Ventas por categoría |
| **Barra apilada** | Composición + comparación | Ventas por categoría y mes |
| **Columna** | Evolución temporal | Pedidos por mes |
| **Torta/Donut** | Proporciones (máx 5 categorías) | % ventas por categoría |

### Tendencias

| Visual | Uso | Ejemplo TechStore |
|--------|-----|-------------------|
| **Líneas** | Evolución temporal | Ingresos mensuales 12 meses |
| **Área** | Volumen + tendencia | Volumen de ventas acumulado |
| **Líneas múltiples** | Comparar tendencias | Ventas por categoría en el tiempo |

### Detalle y análisis

| Visual | Uso | Ejemplo TechStore |
|--------|-----|-------------------|
| **Tabla** | Datos detallados | Top 10 productos |
| **Matriz** | Resumen por 2+ dimensiones | Ventas por categoría y mes |
| **Mapa** | Datos geográficos | Ventas por ciudad |
| **Gráfico de dispersión** | Correlación | Precio vs cantidad vendida |

## Diseñando el dashboard de TechStore

### Página 1: Resumen Ejecutivo

```
┌──────────────────────────────────────────────────────────┐
│  TechStore — Panel de Ventas                [Filtro fecha] │
├─────────┬──────────┬──────────┬──────────┬───────────────┤
│ $2.45M  │  7,850   │   $312   │  1,250   │ Ingresos vs   │
│ Ingresos│ Pedidos  │ Ticket   │ Clientes │ target: 98%   │
├─────────┴──────────┴──────────┴──────────┴───────────────┤
│ ┌──────────────────────────────────┐  ┌────────────────┐ │
│ │  Ingresos Mensuales             │  │ Ventas por     │ │
│ │  (línea, 12 meses)              │  │ Categoría      │ │
│ │                                 │  │ (barra, top 5) │ │
│ └──────────────────────────────────┘  └────────────────┘ │
├──────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────┐  ┌────────────────┐ │
│ │  Top 10 Productos               │  │ Ventas por     │ │
│ │  (barras horizontales)           │  │ Empleado       │ │
│ │                                 │  │ (tabla)        │ │
│ └──────────────────────────────────┘  └────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

### Formato y estilo

**Paleta de colores recomendada**:
- Principal: Azul oscuro (#1B2A4A)
- Secundario: Azul medio (#2E86AB)
- Acento: Naranja (#E67E22)
- Éxito: Verde (#27AE60)
- Alerta: Rojo (#E74C3C)
- Fondo: Blanco/Gris claro (#F8F9FA)

**Tipografía**: Segoe UI (estándar Power BI), títulos en bold

## Formato condicional

Power BI permite colorear celdas según su valor:

1. En una tabla/matriz, selecciona la columna
2. "Formato condicional" → "Color de fondo"
3. Reglas:
   - Ingresos > $100K → verde
   - Ingresos entre $50K y $100K → amarillo
   - Ingresos < $50K → rojo

### Reglas de formato

```dax
-- Medida para formato condicional de semáforo
Semáforo Crecimiento = 
VAR crecimiento = [Crecimiento %]
RETURN SWITCH(
    TRUE(),
    crecimiento >= 0.05, 1,  -- Verde
    crecimiento >= 0,    2,  -- Amarillo
    3                       -- Rojo
)
```

## Segmentaciones (Slicers)

Las segmentaciones permiten a los usuarios filtrar interactivamente:

| Tipo | Cuándo usarlo |
|------|---------------|
| **Lista** | Pocos valores (categorías, empleados) |
| **Desplegable** | Muchos valores (productos, ciudades) |
| **Control deslizante** | Rangos numéricos (precio, total) |
| **Selector de fecha** | Rangos de fecha |
| **Jerarquía** | Drill-down (año → trimestre → mes) |

## Interacciones entre visuales

Por defecto, al seleccionar un elemento en un gráfico se filtran los demás. Puedes personalizar esto:

1. Selecciona un visual
2. "Formato" → "Editar interacciones"
3. Elige para cada otro visual: **Filtrar** o **No afectar**

## Drill-through y tooltips

### Drill-through

Permite navegar de un resumen a un detalle:

1. Crea una página de "Detalle de Categoría"
2. Arrastra `dim_product[category]` al panel "Drill-through"
3. Desde la página principal, haz clic derecho en una categoría → "Ver detalles"

### Tooltips personalizados

1. Crea una página de tooltip (tamaño: 300×150)
2. Arrastra `dim_product[category]` al panel "Tooltip"
3. En la página principal, asigna este tooltip al gráfico

## Marcadores (Bookmarks)

Los marcadores guardan el estado del dashboard:

1. Configura filtros, segmentaciones, página
2. "Ver" → "Panel de marcadores" → "Agregar"
3. Asigna botones para cambiar entre estados

## Ejercicios

1. Crea una página de resumen ejecutivo con 4 tarjetas KPI
2. Agrega un gráfico de líneas con ingresos mensuales
3. Crea un gráfico de barras con ventas por categoría
4. Agrega una segmentación de fecha (range slicer)
5. ¿Cuál es el principio más importante de Tufte para dashboards?
6. Agrega formato condicional a una tabla (por color)
7. Configura drill-through para ver detalle de una categoría
8. Crea un tooltip personalizado para el gráfico de ventas
9. Usa marcadores para alternar entre dos vistas del dashboard
10. ¿Qué tipo de gráfico usarías para mostrar la correlación entre precio y cantidad?
