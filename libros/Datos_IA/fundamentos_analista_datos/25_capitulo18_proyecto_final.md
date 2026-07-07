# Capítulo 18: Proyecto Integrador Final

## El desafío completo

Has llegado al final. Este proyecto integra todo lo aprendido en los 17 capítulos anteriores. Vas a construir un pipeline completo de análisis que va desde la base de datos hasta un dashboard profesional.

## Escenario

La dirección de TechStore quiere un **sistema de reporting automatizado** que:

1. Se actualice automáticamente con nuevos datos
2. Proporcione una visión general del negocio
3. Identifique tendencias y anomalías
4. Sea fácil de compartir con el equipo

## Fase 1: Extracción con SQL

Crea un archivo `consultas_finales.sql` con estas consultas:

```sql
-- 1.1 Resumen general del negocio
SELECT 'Total Ventas' AS metrica, ROUND(SUM(total), 2) AS valor FROM orders WHERE status = 'Completado'
UNION ALL
SELECT 'Total Pedidos', CAST(COUNT(*) AS REAL) FROM orders WHERE status = 'Completado'
UNION ALL
SELECT 'Clientes Únicos', CAST(COUNT(DISTINCT customer_id) AS REAL) FROM orders WHERE status = 'Completado'
UNION ALL
SELECT 'Ticket Promedio', ROUND(AVG(total), 2) FROM orders WHERE status = 'Completado'
UNION ALL
SELECT 'Productos Vendidos', CAST(SUM(oi.quantity) AS REAL)
FROM order_items oi JOIN orders o ON oi.order_id = o.id WHERE o.status = 'Completado'
UNION ALL
SELECT 'Tasa Cancelación', ROUND(
    CAST(SUM(CASE WHEN status = 'Cancelado' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 1
) FROM orders;

-- 1.2 Ventas por región y categoría
SELECT c.region, cat.name AS categoria,
       COUNT(DISTINCT o.id) AS pedidos,
       SUM(oi.quantity) AS unidades,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
JOIN categories cat ON p.category_id = cat.id
WHERE o.status = 'Completado'
GROUP BY c.region, cat.name
ORDER BY c.region, ingresos DESC;

-- 1.3 Top 20 productos
SELECT p.name AS producto, cat.name AS categoria,
       SUM(oi.quantity) AS unidades,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
FROM products p
JOIN categories cat ON p.category_id = cat.id
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'Completado'
GROUP BY p.id
ORDER BY ingresos DESC
LIMIT 20;

-- 1.4 Rendimiento de vendedores
SELECT e.first_name || ' ' || e.last_name AS vendedor,
       e.position AS cargo,
       COUNT(DISTINCT o.id) AS pedidos,
       ROUND(SUM(o.total), 2) AS ingresos,
       ROUND(AVG(o.total), 2) AS ticket_promedio
FROM employees e
JOIN orders o ON e.id = o.employee_id
WHERE o.status = 'Completado'
GROUP BY e.id
ORDER BY ingresos DESC;

-- 1.5 Evolución mensual (2024-2026)
SELECT strftime('%Y-%m', order_date) AS mes,
       COUNT(*) AS pedidos,
       COUNT(DISTINCT customer_id) AS clientes,
       ROUND(SUM(total), 2) AS ingresos
FROM orders
WHERE status = 'Completado'
GROUP BY mes
ORDER BY mes;
```

## Fase 2: Pipeline Python

Crea `pipeline_final.py`:

```python
"""
pipeline_final.py
Pipeline automatizado TechStore
SQL → pandas → Excel → Dashboard
"""
import sqlite3
import pandas as pd
from datetime import datetime
import os

def conectar_bd(ruta="codigos/techstore.db"):
    return sqlite3.connect(ruta)

def extraer_metricas(conn):
    return pd.read_sql("""
        SELECT 'Ventas Totales' AS metrica, ROUND(SUM(total), 2) AS valor
        FROM orders WHERE status = 'Completado'
    """, conn)

def extraer_ventas_mensuales(conn):
    return pd.read_sql("""
        SELECT strftime('%Y-%m', order_date) AS mes,
               COUNT(*) AS pedidos,
               COUNT(DISTINCT customer_id) AS clientes,
               ROUND(SUM(total), 2) AS ingresos
        FROM orders WHERE status = 'Completado'
        GROUP BY mes ORDER BY mes
    """, conn)

def extraer_top_productos(conn):
    return pd.read_sql("""
        SELECT p.name AS producto, SUM(oi.quantity) AS unidades,
               ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
        FROM products p
        JOIN order_items oi ON p.id = oi.product_id
        JOIN orders o ON oi.order_id = o.id
        WHERE o.status = 'Completado'
        GROUP BY p.id ORDER BY ingresos DESC LIMIT 10
    """, conn)

def generar_excel(conn, output="reporte_final_techstore.xlsx"):
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        extraer_ventas_mensuales(conn).to_excel(writer, sheet_name="Tendencia", index=False)
        extraer_top_productos(conn).to_excel(writer, sheet_name="Top Productos", index=False)
        
        region_cat = pd.read_sql("""
            SELECT c.region, cat.name AS categoria,
                   COUNT(DISTINCT o.id) AS pedidos,
                   ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
            FROM customers c JOIN orders o ON c.id = o.customer_id
            JOIN order_items oi ON o.id = oi.order_id
            JOIN products p ON oi.product_id = p.id
            JOIN categories cat ON p.category_id = cat.id
            WHERE o.status = 'Completado'
            GROUP BY c.region, cat.name
        """, conn)
        region_cat.to_excel(writer, sheet_name="Región-Categoría", index=False)
        
        pd.read_sql("SELECT * FROM products ORDER BY price DESC LIMIT 10", conn).to_excel(
            writer, sheet_name="Productos Caros", index=False)
    
    print(f"Reporte Excel generado: {output}")
    return output

def main():
    print("=" * 50)
    print("PIPELINE FINAL - TECHSTORE")
    print("=" * 50)
    
    conn = conectar_bd()
    
    print("\n1. Extrayendo métricas...")
    generar_excel(conn)
    
    print("\n2. Resumen de ejecución:")
    print(f"   Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"   Base datos: techstore.db")
    print(f"   Reporte: reporte_final_techstore.xlsx")
    
    conn.close()
    print("\n¡Pipeline completado exitosamente!")

if __name__ == "__main__":
    main()
```

## Fase 3: Dashboard en Excel

Crea un dashboard profesional en Excel con:

1. **Hoja "Dashboard"** con:
   - 4 tarjetas KPI: Ventas, Pedidos, Clientes, Ticket Promedio
   - Gráfico de tendencia mensual (líneas)
   - Gráfico de ventas por región (barras)
   - Gráfico de Top 10 productos (barras horizontales)
   - Gráfico de distribución por categoría (circular)
   - Segmentadores de año y región

2. **Hoja "Datos"** con los resultados de tus consultas SQL

3. **Hoja "Metodología"** explicando el análisis

## Fase 4: Presentación ejecutiva

Prepara un resumen ejecutivo (5 diapositivas máximo) con:

1. **Resumen**: métricas principales del negocio
2. **Regiones**: qué regiones rinden mejor
3. **Productos**: qué productos destacan
4. **Tendencias**: evolución mensual y estacionalidad
5. **Recomendaciones**: 3 acciones concretas para el negocio

## Criterios de evaluación

Tu proyecto final debe demostrar:

- [ ] **SQL**: Consultas correctas con JOINs, agregaciones y filtros
- [ ] **Python**: Script funcional que genera reportes automáticamente
- [ ] **Excel**: Dashboard profesional con KPIs, gráficos y segmentadores
- [ ] **Modelado**: Relaciones correctas entre tablas
- [ ] **DAX**: Medidas correctas para KPIs
- [ ] **Calidad**: Datos validados y consistentes
- [ ] **Presentación**: Dashboard claro y profesional

## Checklist de autoevaluación final

- [ ] Completé las 5 consultas SQL del proyecto final
- [ ] El pipeline Python se ejecuta sin errores
- [ ] El reporte Excel contiene todas las hojas requeridas
- [ ] El dashboard tiene 4 KPIs correctamente calculados
- [ ] Los gráficos muestran la información claramente
- [ ] Los segmentadores filtran correctamente
- [ ] Validé que los totales del dashboard coinciden con SQL
- [ ] Preparé la presentación ejecutiva
- [ ] Guardé todo en la carpeta `proyecto_final/`
