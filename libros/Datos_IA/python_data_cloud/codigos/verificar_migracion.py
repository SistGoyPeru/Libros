"""
verificar_migracion.py
Verifica que la migración a BigQuery sea correcta.
Compara totales entre SQLite y BigQuery.

Uso:
    python verificar_migracion.py
"""

import sqlite3
from google.cloud import bigquery

SQLITE_PATH = "../codigos/techstore.db"
PROJECT = "techstore-analytics"  # CAMBIA por tu Project ID
DATASET = "techstore"

conexion_bq = bigquery.Client(project=PROJECT)
conexion_sqlite = sqlite3.connect(SQLITE_PATH)

TABLAS = ["customers", "products", "orders", "order_items", "employees"]

print("Comparacion de filas por tabla:")
print(f"{'Tabla':<15} {'SQLite':<10} {'BigQuery':<10} {'Coinciden':<10}")
print("-" * 50)

for tabla in TABLAS:
    cursor = conexion_sqlite.execute(f"SELECT COUNT(*) FROM {tabla}")
    count_sqlite = cursor.fetchone()[0]

    query = f"SELECT COUNT(*) AS cnt FROM {DATASET}.{tabla}"
    rows = conexion_bq.query(query).result()
    count_bq = list(rows)[0].cnt

    coincide = "OK" if count_sqlite == count_bq else "ERROR"
    print(f"{tabla:<15} {count_sqlite:<10} {count_bq:<10} {coincide:<10}")

conexion_sqlite.close()
print("Verificacion completada.")
