"""
consultas_bigquery_ejemplo.py
Ejemplos de consultas a BigQuery desde Python.

Uso:
    python consultas_bigquery_ejemplo.py

Requisitos:
    - google-cloud-bigquery instalado
    - Dataset techstore migrado en BigQuery
"""

from google.cloud import bigquery
import pandas as pd

PROJECT = "techstore-analytics"  # CAMBIA por tu Project ID
DATASET = "techstore"

cliente = bigquery.Client(project=PROJECT)


def consultar(query, descripcion=""):
    if descripcion:
        print(f"\n=== {descripcion} ===")
    df = cliente.query(query).to_dataframe()
    print(df.to_string(index=False))
    print(f"Filas: {len(df)}")
    return df


# 1. Ventas por mes
consultar(f"""
    SELECT
        DATE_TRUNC(order_date, MONTH) AS mes,
        COUNT(*) AS pedidos,
        ROUND(SUM(total), 2) AS ingresos
    FROM {DATASET}.orders
    GROUP BY mes
    ORDER BY mes
""", "Ventas por mes")

# 2. Top 10 clientes
consultar(f"""
    SELECT
        c.name,
        c.city,
        COUNT(o.order_id) AS pedidos,
        ROUND(SUM(o.total), 2) AS gasto_total
    FROM {DATASET}.orders AS o
    JOIN {DATASET}.customers AS c ON o.customer_id = c.customer_id
    GROUP BY c.name, c.city
    ORDER BY gasto_total DESC
    LIMIT 10
""", "Top 10 clientes por gasto")

# 3. Productos más vendidos
consultar(f"""
    SELECT
        p.name,
        p.category,
        COUNT(oi.order_id) AS veces_vendido,
        ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos
    FROM {DATASET}.order_items AS oi
    JOIN {DATASET}.products AS p ON oi.product_id = p.product_id
    GROUP BY p.name, p.category
    ORDER BY veces_vendido DESC
    LIMIT 10
""", "Top 10 productos mas vendidos")

# 4. Métricas generales
consultar(f"""
    SELECT
        ROUND(SUM(total), 2) AS ingresos_totales,
        COUNT(*) AS total_pedidos,
        ROUND(AVG(total), 2) AS ticket_promedio,
        COUNT(DISTINCT customer_id) AS clientes_unicos
    FROM {DATASET}.orders
""", "Metricas generales")

# 5. Dry run - estimación de coste
print("\n=== Dry run: SELECT * FROM orders ===")
job_config = bigquery.QueryJobConfig(dry_run=True)
job = cliente.query(f"SELECT * FROM {DATASET}.orders", job_config=job_config)
bytes_escaneados = job.total_bytes_processed
print(f"Bytes a escanear: {bytes_escaneados:,}")
print(f"GB a escanear: {bytes_escaneados / 1e9:.2f}")
print(f"Costo estimado (on-demand): ${bytes_escaneados / 1e12 * 5:.4f} USD")

print("\nEjemplos completados.")
