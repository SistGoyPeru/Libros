"""Capítulo 5: Feature Engineering - creación de features temporales y agregadas"""

import pandas as pd
import numpy as np

df = pd.read_parquet("data/silver/ventas/")

# Features temporales
df["hora"] = pd.to_datetime(df["timestamp"]).dt.hour
df["dia_semana"] = pd.to_datetime(df["timestamp"]).dt.dayofweek
df["es_fin_semana"] = df["dia_semana"].isin([5, 6]).astype(int)
df["mes"] = pd.to_datetime(df["timestamp"]).dt.month

# Features agregadas por cliente
features_cliente = df.groupby("customer_id").agg(
    freq_compra=("transaction_id", "count"),
    ticket_avg=("amount", "mean"),
    ticket_max=("amount", "max"),
    antiguedad_dias=("timestamp", lambda x: (x.max() - x.min()).days)
).reset_index()

# Features de producto
features_producto = df.groupby("product_id").agg(
    ventas_totales=("amount", "sum"),
    veces_vendido=("transaction_id", "count"),
    precio_promedio=("amount", "mean")
).reset_index()

print(f"Features por cliente: {features_cliente.shape}")
print(features_cliente.head())
print(f"\nFeatures por producto: {features_producto.shape}")
print(features_producto.head())
