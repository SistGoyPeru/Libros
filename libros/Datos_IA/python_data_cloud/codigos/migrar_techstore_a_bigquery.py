"""
migrar_techstore_a_bigquery.py
Migra la base de datos SQLite de TechStore a BigQuery.

Uso:
    python migrar_techstore_a_bigquery.py

Requisitos:
    - google-cloud-bigquery instalado
    - gcloud auth application-default login (o service account configurada)
    - Cambiar PROJECT por tu Project ID de GCP
"""

import sqlite3
import pandas as pd
from google.cloud import bigquery

# --- Configuración ---
SQLITE_PATH = "../codigos/techstore.db"
PROJECT = "techstore-analytics"  # CAMBIA por tu Project ID
DATASET = "techstore"

TABLAS = [
    "customers",
    "products",
    "orders",
    "order_items",
    "employees",
]

cliente = bigquery.Client(project=PROJECT)

# --- Crear dataset si no existe ---
dataset_ref = cliente.dataset(DATASET)
try:
    cliente.get_dataset(dataset_ref)
    print(f"Dataset {DATASET} ya existe")
except Exception:
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "us-central1"
    cliente.create_dataset(dataset)
    print(f"Dataset {DATASET} creado")

# --- Migrar cada tabla ---
conn = sqlite3.connect(SQLITE_PATH)

for tabla in TABLAS:
    print(f"Migrando {tabla}...")

    # Leer desde SQLite
    df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn)
    print(f"  Filas leídas: {len(df)}")

    # Cargar a BigQuery
    tabla_id = f"{DATASET}.{tabla}"
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    job = cliente.load_table_from_dataframe(df, tabla_id, job_config=job_config)
    job.result()

    # Verificar
    table = cliente.get_table(tabla_id)
    print(f"  Cargadas: {table.num_rows} filas, {table.num_bytes / 1e6:.2f} MB")

conn.close()
print("Migración completada.")
