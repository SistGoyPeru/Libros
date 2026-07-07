"""Capítulo 5: Pipeline básico de ML - Train/Test split con scikit-learn"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Cargar datos TechStore
df = pd.read_parquet("data/silver/ventas/")
print(f"Dataset: {df.shape[0]:,} registros, {df.shape[1]} features")

# Separar features y target
X = df.drop(["ingresos", "transaction_id", "timestamp"], axis=1)
y = df["ingresos"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Train: {len(X_train):,} | Test: {len(X_test):,}")
