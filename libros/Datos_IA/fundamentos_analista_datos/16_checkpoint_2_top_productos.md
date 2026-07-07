# Checkpoint 2: Top 10 Productos Más Vendidos

## Proyecto integrador del Proyecto 2

En este checkpoint vas a combinar SQL, Excel y Python para identificar los productos más vendidos de TechStore y presentar un análisis completo.

## Parte 1: SQL — Identifica los top productos

```sql
-- 2.1 Top 10 productos más vendidos por unidades
SELECT p.name AS producto,
       c.name AS categoria,
       SUM(oi.quantity) AS unidades_vendidas,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos,
       ROUND(AVG(oi.unit_price), 2) AS precio_promedio
FROM order_items oi
JOIN products p ON oi.product_id = p.id
JOIN categories c ON p.category_id = c.id
GROUP BY p.id
ORDER BY unidades_vendidas DESC
LIMIT 10;

-- 2.2 Top 10 productos por ingresos generados
SELECT p.name AS producto,
       c.name AS categoria,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos,
       SUM(oi.quantity) AS unidades_vendidas
FROM order_items oi
JOIN products p ON oi.product_id = p.id
JOIN categories c ON p.category_id = c.id
GROUP BY p.id
ORDER BY ingresos DESC
LIMIT 10;

-- 2.3 Ventas por categoría
SELECT c.name AS categoria,
       COUNT(DISTINCT oi.order_id) AS pedidos,
       SUM(oi.quantity) AS unidades,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
FROM categories c
JOIN products p ON c.id = p.category_id
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'Completado'
GROUP BY c.name
ORDER BY ingresos DESC;

-- 2.4 ¿Qué cliente ha gastado más?
SELECT c.first_name || ' ' || c.last_name AS cliente,
       c.region,
       COUNT(o.id) AS pedidos,
       ROUND(SUM(o.total), 2) AS gasto_total
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.status = 'Completado'
GROUP BY c.id
ORDER BY gasto_total DESC
LIMIT 10;

-- 2.5 Ventas por región y categoría (cubo de datos)
SELECT c.region,
       cat.name AS categoria,
       COUNT(DISTINCT o.id) AS pedidos,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
JOIN categories cat ON p.category_id = cat.id
WHERE o.status = 'Completado'
GROUP BY c.region, cat.name
ORDER BY c.region, ingresos DESC;
```

## Parte 2: Excel — Visualiza los resultados

1. Exporta los resultados de la consulta 2.1 a CSV y cárgalos en Excel
2. Crea un gráfico de barras horizontales con el Top 10 productos
3. Crea una tabla dinámica con:
   - Filas: región
   - Columnas: categoría
   - Valores: ingresos
4. Crea un gráfico dinámico de columnas agrupadas
5. Aplica formato profesional:
   - Título descriptivo
   - Etiquetas de datos
   - Colores corporativos
   - Sin líneas de cuadrícula innecesarias

## Parte 3: Python — Análisis automatizado

```python
# Análisis de productos más vendidos
productos = [
    {"nombre": "Auriculares Ultra", "categoria": "Auriculares", "unidades": 245, "ingresos": 12250.00},
    {"nombre": "Smartphone Air", "categoria": "Smartphones", "unidades": 198, "ingresos": 178200.00},
    {"nombre": "Tablet Max", "categoria": "Tablets", "unidades": 167, "ingresos": 83500.00},
    {"nombre": "Portátil Pro", "categoria": "Portátiles", "unidades": 145, "ingresos": 188500.00},
    {"nombre": "Ratón Elite", "categoria": "Ratones", "unidades": 134, "ingresos": 5360.00},
    {"nombre": "Teclado Mecánico", "categoria": "Teclados", "unidades": 122, "ingresos": 10980.00},
    {"nombre": "Monitor UltraWide", "categoria": "Monitores", "unidades": 98, "ingresos": 49000.00},
    {"nombre": "Altavoz Portátil", "categoria": "Altavoces", "unidades": 87, "ingresos": 13050.00},
    {"nombre": "Disco SSD 1TB", "categoria": "Almacenamiento", "unidades": 82, "ingresos": 6560.00},
    {"nombre": "Cámara Web HD", "categoria": "Cámaras", "unidades": 76, "ingresos": 4560.00},
]

print("=== TOP 10 PRODUCTOS MÁS VENDIDOS ===\n")

# Métricas generales
total_unidades = sum(p["unidades"] for p in productos)
total_ingresos = sum(p["ingresos"] for p in productos)

print(f"Total unidades vendidas (top 10): {total_unidades}")
print(f"Total ingresos (top 10): {total_ingresos:,.2f}€\n")

# Análisis por producto
print(f"{'Producto':<25} {'Categoría':<15} {'Unidades':>10} {'Ingresos':>12} {'% Ingresos':>10}")
print("=" * 72)

for p in sorted(productos, key=lambda x: x["ingresos"], reverse=True):
    pct = (p["ingresos"] / total_ingresos) * 100
    print(f"{p['nombre']:<25} {p['categoria']:<15} {p['unidades']:>10} {p['ingresos']:>10,.2f}€ {pct:>8.1f}%")

# Concentración de ingresos
top_3_ingresos = sum(p["ingresos"] for p in sorted(productos, key=lambda x: x["ingresos"], reverse=True)[:3])
print(f"\nEl Top 3 productos concentra el {(top_3_ingresos/total_ingresos)*100:.1f}% de los ingresos")

# Recomendación
print("\n=== RECOMENDACIONES ===")
print("1. Los auriculares lideran en unidades pero no en ingresos")
print("2. Portátiles y smartphones generan más ingresos por unidad")
print("3. Considerar promociones cruzadas: portátil + ratón + teclado")
print("4. Evaluar si los productos baratos están canibalizando ventas de gama alta")
```

## Parte 4: Preguntas de negocio

1. ¿Hay diferencia entre los top productos por unidades y por ingresos?
2. ¿Qué categoría genera más ingresos totales?
3. ¿Qué región tiene el ticket promedio más alto?
4. ¿Hay algún producto que se venda mucho pero genere poco margen?
5. ¿Qué recomendarías al equipo de producto basado en este análisis?

## Entregable

Guarda tu análisis en `proyecto_2/`:
- `top_productos.sql` — Consultas SQL
- `analisis_ventas.xlsx` — Tablas dinámicas + gráficos
- `top_productos.py` — Análisis en Python
- `dashboard_proyecto_2.png` — Captura de tu dashboard

## Checklist de autoevaluación del Proyecto 2

- [ ] Sé usar funciones de agregación con GROUP BY
- [ ] Sé combinar múltiples tablas con JOINs
- [ ] Sé crear tablas dinámicas en Excel
- [ ] Sé crear gráficos profesionales
- [ ] Sé usar listas, diccionarios y bucles en Python
- [ ] Sé diseñar un dashboard básico
- [ ] Completé el análisis integrado en las 3 herramientas
