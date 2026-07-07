# Checkpoint 3: Análisis de Cohorte de Ventas

## Proyecto integrador del Proyecto 3

En este checkpoint vas a realizar un análisis de cohortes para entender el comportamiento de los clientes de TechStore a lo largo del tiempo.

## ¿Qué es un análisis de cohortes?

Un análisis de cohortes agrupa clientes por el período en que hicieron su primera compra y analiza su comportamiento en meses posteriores. Responde preguntas como:

- ¿Los clientes que se registraron en 2024 son más fieles que los de 2025?
- ¿Cuánto gastan los clientes en su segundo mes vs su primer mes?
- ¿Qué cohorte tiene mejor retención?

## Parte 1: SQL — Prepara los datos de cohortes

```sql
-- 3.1 Primera compra de cada cliente
WITH primera_compra AS (
    SELECT customer_id,
           MIN(order_date) AS fecha_primera_compra,
           strftime('%Y-%m', MIN(order_date)) AS cohorte
    FROM orders
    WHERE status = 'Completado'
    GROUP BY customer_id
),
-- 3.2 Compras por cliente y mes
compras_mensuales AS (
    SELECT o.customer_id,
           pc.cohorte,
           strftime('%Y-%m', o.order_date) AS mes_compra,
           (strftime('%Y', o.order_date) - strftime('%Y', pc.fecha_primera_compra)) * 12
           + (strftime('%m', o.order_date) - strftime('%m', pc.fecha_primera_compra)) AS mes_relativo,
           COUNT(DISTINCT o.id) AS pedidos,
           SUM(o.total) AS gasto
    FROM orders o
    JOIN primera_compra pc ON o.customer_id = pc.customer_id
    WHERE o.status = 'Completado'
    GROUP BY o.customer_id, pc.cohorte, mes_compra
)
-- 3.3 Tabla de cohortes
SELECT cohorte,
       mes_relativo,
       COUNT(DISTINCT customer_id) AS clientes_activos,
       ROUND(AVG(gasto), 2) AS gasto_promedio,
       ROUND(SUM(gasto), 2) AS gasto_total
FROM compras_mensuales
GROUP BY cohorte, mes_relativo
ORDER BY cohorte, mes_relativo;
```

```sql
-- 3.4 Ventas totales por mes
SELECT strftime('%Y-%m', order_date) AS mes,
       COUNT(*) AS pedidos,
       COUNT(DISTINCT customer_id) AS clientes,
       ROUND(SUM(total), 2) AS ingresos
FROM orders
WHERE status = 'Completado'
GROUP BY mes
ORDER BY mes;

-- 3.5 Distribución de valor de pedidos
SELECT CASE
           WHEN total < 50 THEN '< 50€'
           WHEN total < 100 THEN '50-100€'
           WHEN total < 200 THEN '100-200€'
           WHEN total < 500 THEN '200-500€'
           WHEN total < 1000 THEN '500-1000€'
           ELSE '+1000€'
       END AS rango,
       COUNT(*) AS pedidos,
       ROUND(SUM(total), 2) AS ingresos,
       ROUND(AVG(total), 2) AS ticket_promedio
FROM orders WHERE status = 'Completado'
GROUP BY rango
ORDER BY MIN(total);

-- 3.6 Frecuencia de compra por cliente
SELECT pedidos_realizados,
       COUNT(*) AS clientes
FROM (
    SELECT customer_id, COUNT(*) AS pedidos_realizados
    FROM orders WHERE status = 'Completado'
    GROUP BY customer_id
)
GROUP BY pedidos_realizados
ORDER BY pedidos_realizados;
```

## Parte 2: Excel — Power Query y tablas dinámicas

1. Carga `datos_detalles_ventas.csv` en Power Query
2. Realiza las siguientes transformaciones:
   - Cambia tipo de `order_date` a fecha
   - Filtra solo pedidos "Completado"
   - Agrupa por `customer_id` y mes (usa columna fecha agrupada)
   - Carga el resultado a una tabla
3. Crea una tabla dinámica con:
   - Filas: mes_relativo
   - Columnas: cohorte
   - Valores: clientes activos (conteo de customer_id)
4. Crea un gráfico de líneas para visualizar las cohortes
5. Utiliza formato condicional en la tabla dinámica para ver las cohortes con más actividad

## Parte 3: Python — Análisis de cohortes automatizado

```python
import csv
from datetime import datetime
from collections import defaultdict

def analisis_cohortes():
    # Leer ventas
    ventas = []
    with open("codigos/datos_ventas.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["status"] == "Completado":
                ventas.append({
                    "customer_id": int(row["customer_id"]),
                    "order_date": row["order_date"],
                    "total": float(row["total"]),
                    "region": row["region"]
                })
    
    # Encontrar primera compra de cada cliente
    primera_compra = {}
    for v in ventas:
        cid = v["customer_id"]
        fecha = v["order_date"][:7]  # YYYY-MM
        if cid not in primera_compra or fecha < primera_compra[cid]:
            primera_compra[cid] = fecha
    
    # Asignar cohorte a cada venta
    cohortes = defaultdict(lambda: defaultdict(lambda: {"clientes": set(), "gasto": 0.0, "pedidos": 0}))
    
    for v in ventas:
        cid = v["customer_id"]
        cohorte = primera_compra[cid]
        mes_compra = v["order_date"][:7]
        
        # Calcular mes relativo
        año_c, mes_c = int(cohorte[:4]), int(cohorte[5:7])
        año_v, mes_v = int(mes_compra[:4]), int(mes_compra[5:7])
        mes_rel = (año_v - año_c) * 12 + (mes_v - mes_c)
        
        cohortes[cohorte][mes_rel]["clientes"].add(cid)
        cohortes[cohorte][mes_rel]["gasto"] += v["total"]
        cohortes[cohorte][mes_rel]["pedidos"] += 1
    
    # Mostrar matriz de cohortes
    print("=== ANÁLISIS DE COHORTES ===\n")
    print("Clientes activos por mes relativo:\n")
    
    cohortes_ordenadas = sorted(cohortes.keys())
    meses_max = max(max(meses.keys()) for meses in cohortes.values())
    
    # Cabecera
    header = "Cohorte   "
    for m in range(meses_max + 1):
        header += f"  Mes {m:2d} "
    print(header)
    print("=" * len(header))
    
    for cohorte in cohortes_ordenadas:
        row = f"{cohorte}  "
        for m in range(meses_max + 1):
            num = len(cohortes[cohorte][m]["clientes"]) if m in cohortes[cohorte] else 0
            row += f"  {num:4d} "
        print(row)
    
    # Métricas de retención
    print("\n=== RETENCIÓN POR COHORTE ===\n")
    print(f"{'Cohorte':<10} {'Mes 0':>8} {'Mes 1':>8} {'Mes 3':>8} {'Mes 6':>8} {'Mes 12':>8}")
    print("=" * 55)
    
    for cohorte in cohortes_ordenadas:
        base = len(cohortes[cohorte][0]["clientes"])
        if base == 0:
            continue
        m0 = 100.0
        m1 = (len(cohortes[cohorte][1]["clientes"]) / base * 100) if 1 in cohortes[cohorte] else 0
        m3 = (len(cohortes[cohorte][3]["clientes"]) / base * 100) if 3 in cohortes[cohorte] else 0
        m6 = (len(cohortes[cohorte][6]["clientes"]) / base * 100) if 6 in cohortes[cohorte] else 0
        m12 = (len(cohortes[cohorte][12]["clientes"]) / base * 100) if 12 in cohortes[cohorte] else 0
        print(f"{cohorte:<10} {m0:>7.1f}% {m1:>7.1f}% {m3:>7.1f}% {m6:>7.1f}% {m12:>7.1f}%")
    
    # Métricas globales
    total_clientes = len(set(v["customer_id"] for v in ventas))
    total_ingresos = sum(v["total"] for v in ventas)
    
    print(f"\n=== RESUMEN ===")
    print(f"Total clientes activos: {total_clientes}")
    print(f"Total ingresos: {total_ingresos:,.2f}€")
    print(f"Ingreso por cliente: {total_ingresos/total_clientes:,.2f}€")
    
    # Distribución por frecuencia
    freq = defaultdict(int)
    for v in ventas:
        freq[v["customer_id"]] += 1
    
    unicos = set(v["customer_id"] for v in ventas)
    una_vez = sum(1 for c in unicos if freq[c] == 1)
    print(f"\nClientes que compraron solo una vez: {una_vez} ({una_vez/len(unicos)*100:.1f}%)")

analisis_cohortes()
```

## Parte 4: Preguntas de negocio

1. ¿Qué cohorte tiene mejor retención en el mes 3? ¿Por qué crees?
2. ¿Cuánto gastan los clientes en promedio en su primera compra vs la segunda?
3. ¿Hay estacionalidad en las ventas? ¿Qué meses venden más?
4. ¿Qué porcentaje de clientes compra más de una vez?
5. ¿Qué recomendarías al equipo de marketing basado en este análisis?

## Entregable

Guarda tu análisis en `proyecto_3/`:
- `analisis_cohortes.sql` — Consultas SQL
- `cohortes.xlsx` — Tabla dinámica con matriz de cohortes
- `analisis_cohortes.py` — Análisis Python automatizado
- `dashboard_cohortes.png` — Captura de tu dashboard

## Checklist de autoevaluación del Proyecto 3

- [ ] Sé usar subconsultas y CTEs para análisis complejos
- [ ] Sé usar funciones de ventana (ROW_NUMBER, LAG, NTILE)
- [ ] Sé usar Power Query para transformar datos
- [ ] Sé crear medidas DAX con CALCULATE y SUMX
- [ ] Sé crear funciones en Python y usar módulos
- [ ] Sé leer archivos CSV con Python
- [ ] Completé el análisis de cohortes en las 3 herramientas
