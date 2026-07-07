# Checkpoint 3: Modelo Semántico y KPIs Avanzados

## Objetivo

Has aprendido DAX avanzado, Power Query y modelado de datos. Ahora es momento de llevar tu modelo Power BI al siguiente nivel: **crear un modelo semántico profesional con KPIs dinámicos, análisis What-If y segmentaciones inteligentes**.

## Requisitos

- Archivo TechStore_BI.pbix del Checkpoint 2
- Modelo star schema conectado y validado
- Medidas DAX básicas funcionando

## Paso 1: Tablas auxiliares (desconectadas)

Crea estas tablas usando "Introducir datos" en Power BI:

### Tabla KPIs

```dax
Tabla KPIs = 
DATATABLE(
    "KPI", STRING,
    "Orden", INTEGER,
    "Descripción", STRING,
    {
        {"Ingresos Totales", 1, "Suma de ingresos"},
        {"Total Pedidos", 2, "Número de pedidos"},
        {"Ticket Promedio", 3, "Ingreso promedio por pedido"},
        {"Clientes Activos", 4, "Clientes únicos que compraron"},
        {"Crecimiento %", 5, "Variación vs mes anterior"}
    }
)
```

### Tabla Periodos

```dax
Tabla Periodos = 
DATATABLE(
    "Periodo", STRING,
    "Días", INTEGER,
    "Orden", INTEGER,
    {
        {"Últimos 7 días", -7, 1},
        {"Últimos 30 días", -30, 2},
        {"Últimos 90 días", -90, 3},
        {"Últimos 12 meses", -365, 4},
        {"Todo el histórico", -9999, 5}
    }
)
```

### Tabla Objetivos (simulada)

```dax
Objetivos Mensuales = 
DATATABLE(
    "Año", INTEGER,
    "Mes", INTEGER,
    "Objetivo Ingresos", CURRENCY,
    "Objetivo Pedidos", INTEGER,
    {
        {2024, 1, 130000, 400},
        {2024, 2, 135000, 410},
        {2024, 3, 140000, 420},
        {2024, 4, 145000, 430},
        {2024, 5, 150000, 440},
        {2024, 6, 155000, 450},
        {2024, 7, 160000, 460},
        {2024, 8, 165000, 470},
        {2024, 9, 170000, 480},
        {2024, 10, 175000, 490},
        {2024, 11, 180000, 500},
        {2024, 12, 200000, 550}
    }
)
```

## Paso 2: Medidas avanzadas

Agrega estas medidas a tu modelo:

```dax
-- ===== KPIs Dinámicos =====

KPI Seleccionado = 
SWITCH(
    SELECTEDVALUE('Tabla KPIs'[KPI]),
    "Ingresos Totales", [Ingresos Totales],
    "Total Pedidos", [Total Pedidos],
    "Ticket Promedio", [Ticket Promedio],
    "Clientes Activos", [Clientes Activos],
    "Crecimiento %", [Crecimiento %],
    BLANK()
)

Ventas Periodo Dinámico = 
VAR dias = SELECTEDVALUE('Tabla Periodos'[Días], -30)
RETURN
CALCULATE(
    [Ingresos Totales],
    DATESINPERIOD(
        dim_date[full_date],
        LASTDATE(dim_date[full_date]),
        dias,
        DAY
    )
)

-- ===== Cumplimiento vs Objetivo =====

% Cumplimiento Ingresos = 
DIVIDE(
    [Ingresos Totales],
    SUM(Objetivos_Mensuales[Objetivo Ingresos]),
    0
)

% Cumplimiento Pedidos = 
DIVIDE(
    [Total Pedidos] * 1.0,
    SUM(Objetivos_Mensuales[Objetivo Pedidos]),
    0
)

-- ===== Análisis What-If =====

Ingresos con Descuento = 
[Ingresos Totales] * (1 - [Valor Descuento])

Impacto Descuento = 
[Ingresos Totales] - [Ingresos con Descuento]

-- ===== Pareto =====

% Acumulado = 
VAR total_general = CALCULATE([Ingresos Totales], ALL(dim_product))
VAR ingresos_actual = [Ingresos Totales]
VAR productos_superiores = 
    FILTER(
        ALL(dim_product),
        [Ingresos Totales] >= ingresos_actual
    )
RETURN
DIVIDE(
    CALCULATE([Ingresos Totales], productos_superiores),
    total_general
)

Es Pareto = IF([% Acumulado] <= 0.8, "80%", "20%")

-- ===== Indicadores de Tarjeta =====

Variación vs Mes Anterior = 
[Ingresos Totales] - [Ingresos Mes Anterior]

Tendencia = 
IF([Variación vs Mes Anterior] >= 0, "▲", "▼")

Color Tendencia = 
IF([Variación vs Mes Anterior] >= 0, "verde", "rojo")
```

## Paso 3: Páginas nuevas

### Página 4: KPIs Dinámicos

- Un slicer con la tabla "Tabla KPIs" (lista)
- Una tarjeta que muestre "KPI Seleccionado"
- Matriz: Tabla KPIs[KPI] en filas, dim_date[anio] y [mes] en columnas

### Página 5: What-If

- Slicer del parámetro "Descuento" (control deslizante)
- Tarjetas: Ingresos Originales, Ingresos con Descuento, Impacto
- Gráfico de líneas: comparando ingresos con/sin descuento por mes

### Página 6: Análisis Avanzado

- Gráfico de Pareto (barras + línea acumulada)
- Matriz con formato condicional por semáforo
- Tabla de cohortes (opcional)

## Paso 4: Formato y estilo avanzado

1. Formato condicional en matriz (color de fondo según valor)
2. Iconos en tarjetas (▲/▼ según tendencia)
3. Tooltips personalizados para KPIs
4. Marcadores para cambiar entre vistas de KPIs

## Entregables del Checkpoint 3

- [ ] Tablas auxiliares creadas (KPIs, Periodos, Objetivos)
- [ ] Medida "KPI Seleccionado" funcionando con parámetro
- [ ] Análisis What-If con parámetro de descuento
- [ ] Matriz dinámica con KPIs seleccionables
- [ ] % Cumplimiento vs Objetivo
- [ ] Análisis de Pareto (80/20)
- [ ] Tarjetas con indicadores de tendencia
- [ ] Página de KPIs dinámicos
- [ ] Página de What-If

## Preguntas de reflexión

1. ¿Qué ventaja tiene un KPI dinámico frente a tarjetas estáticas?
2. ¿Cómo usarías el What-If Analysis en una reunión con la gerencia?
3. ¿Qué insights te da el análisis de Pareto para TechStore?
4. ¿Qué otros parámetros What-If serían útiles para TechStore?

¡Felicidades! Tu modelo semántico es ahora profesional y flexible. En el Proyecto 4 lo publicarás en Power BI Service para compartirlo con tu organización.
