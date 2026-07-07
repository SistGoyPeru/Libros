# Capítulo 4: KPIs, Métricas y Cuadros de Mando

## Métricas vs KPIs

| | Métrica | KPI |
|---|---|---|
| **Definición** | Medición cuantitativa | Métrica ligada a un objetivo estratégico |
| **Propósito** | Monitorear | Evaluar desempeño vs meta |
| **Frecuencia** | Constante | Periódica (diaria, semanal, mensual) |
| **Ejemplo** | Número de pedidos | % de crecimiento vs mes anterior |
| **Meta** | No siempre tiene target | Siempre tiene un target |

**Todas las KPIs son métricas, pero no todas las métricas son KPIs.**

## Diseñando KPIs efectivos

### Framework SMART

| Criterio | Pregunta | Ejemplo |
|----------|----------|---------|
| **S**pecific | ¿Qué medimos exactamente? | Ingresos mensuales |
| **M**easurable | ¿Se puede cuantificar? | $, %, unidades |
| **A**chievable | ¿Es alcanzable? | +10% vs realista |
| **R**elevant | ¿Importa para el negocio? | Directamente ligado a ingresos |
| **T**ime-bound | ¿En qué período? | Este mes vs mes anterior |

### Jerarquía de KPIs

```
Nivel Estratégico (CEO, Dirección)
  └── Ingresos, Rentabilidad, Cuota de mercado
       │
Nivel Táctico (Gerentes)
  └── Ventas por región, Customer Lifetime Value, Rotación
       │
Nivel Operativo (Supervisores)
  └── Pedidos por hora, Tasa de cancelación, Stock crítico
```

## KPIs para TechStore

### Área de Ventas

| KPI | Fórmula | Frecuencia | Target |
|-----|---------|------------|--------|
| Ingresos Mensuales | SUM(total) | Mensual | $150,000 |
| Ticket Promedio | AVG(total) | Diario | $320 |
| Tasa de Conversión | Pedidos / Visitantes × 100 | Diario | 3.5% |
| Crecimiento vs mes anterior | (Mes actual - Mes anterior) / Mes anterior × 100 | Mensual | +5% |
| Ventas por empleado | SUM(total) / COUNT(employee) | Mensual | $25,000 |

### Área de Clientes

| KPI | Fórmula | Frecuencia | Target |
|-----|---------|------------|--------|
| Clientes Activos | COUNT(DISTINCT customer_id) | Mensual | +10% |
| Customer Lifetime Value | AVG(total_por_cliente) | Trimestral | $2,500 |
| Tasa de Retención | Clientes que repiten / Total clientes | Trimestral | 40% |
| NPS (Net Promoter Score) | Promotores - Detractores | Trimestral | +50 |

### Área de Operaciones

| KPI | Fórmula | Frecuencia | Target |
|-----|---------|------------|--------|
| Pedidos por día | COUNT(order_id) / COUNT(DISTINCT date) | Diario | 20 |
| Tasa de Cancelación | Pedidos cancelados / Total pedidos | Mensual | < 5% |
| Días entre pedidos (clientes) | AVG(días entre compras) | Mensual | < 60 |

## Cuadros de Mando (Scorecards)

Un **cuadro de mando** agrupa KPIs por perspectiva. El más famoso es el **Balanced Scorecard** (Kaplan & Norton):

| Perspectiva | Pregunta | KPIs TechStore |
|-------------|----------|----------------|
| **Financiera** | ¿Cómo nos ven los accionistas? | Ingresos, Margen, Rentabilidad |
| **Cliente** | ¿Cómo nos ven los clientes? | NPS, Retención, Satisfacción |
| **Interna** | ¿En qué debemos sobresalir? | Tasa cancelación, Calidad, Eficiencia |
| **Aprendizaje** | ¿Cómo mejoramos? | Capacitación, Rotación empleados |

## KPIs en SQL

```sql
-- Dashboard de KPIs para TechStore
SELECT
  -- Ingresos
  ROUND(SUM(total), 2) AS ingresos_totales,
  ROUND(AVG(total), 2) AS ticket_promedio,
  COUNT(*) AS total_pedidos,
  COUNT(DISTINCT customer_id) AS clientes_unicos,
  -- Métricas calculadas
  ROUND(SUM(total) / COUNT(*), 2) AS ingreso_por_pedido,
  ROUND(SUM(total) / COUNT(DISTINCT customer_id), 2) AS ingreso_por_cliente,
  ROUND(COUNT(*) / COUNT(DISTINCT customer_id), 1) AS pedidos_por_cliente,
  -- Métricas de cancelación
  SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS pedidos_cancelados,
  ROUND(
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
    2
  ) AS tasa_cancelacion_pct
FROM techstore.orders
WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY);
```

## KPIs en Power BI (DAX)

Estas medidas las implementaremos en el Proyecto 2:

```dax
Ingresos Totales = SUM(fact_orders[total])

Ticket Promedio = AVERAGE(fact_orders[total])

Total Pedidos = COUNTROWS(fact_orders)

Clientes Únicos = DISTINCTCOUNT(fact_orders[customer_id])

Crecimiento Mensual % = 
VAR mes_actual = SUM(fact_orders[total])
VAR mes_anterior = CALCULATE(SUM(fact_orders[total]), PREVIOUSMONTH(dim_date[full_date]))
RETURN DIVIDE(mes_actual - mes_anterior, mes_anterior, 0)
```

## Storytelling con KPIs

Un dashboard efectivo no solo muestra números. Cuenta una historia:

1. **Contexto**: ¿qué es normal? (promedio histórico, target)
2. **Tendencia**: ¿mejorando o empeorando? (vs periodo anterior)
3. **Desglose**: ¿qué impulsa el cambio? (por categoría, región)
4. **Acción**: ¿qué hacer? (recomendación basada en datos)

### Ejemplo de storytelling

> "Los ingresos de este mes son $142,000 — un 8% por debajo del target de $155,000. La caída se concentra en la categoría Portátiles (-15%) debido a problemas con el proveedor TechSupply. Recomendación: activar el proveedor alternativo e intensificar la promoción de Tablets que está 12% sobre target."

## Ejercicios

1. Define 5 KPIs para TechStore usando el framework SMART
2. ¿Cuál es la diferencia entre una métrica y un KPI?
3. Crea una consulta SQL que calcule los KPIs de ventas del último trimestre
4. Diseña un Balanced Scorecard para TechStore con 4 perspectivas
5. ¿Qué es el ticket promedio? ¿Cómo calcularlo en SQL? ¿En DAX?
6. Calcula la tasa de cancelación de TechStore en SQL
7. ¿Cuál es el KPI más importante para un CEO? ¿Y para un vendedor?
8. Escribe un storytelling de 3 párrafos basado en datos ficticios de TechStore
9. ¿Qué diferencia hay entre un dashboard y un scorecard?
10. Define un target SMART para el KPI "Clientes Activos"
