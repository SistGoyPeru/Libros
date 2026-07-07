"""Capítulo 5: Train/Test/Validation split y Cross-Validation"""

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

df = pd.read_parquet("data/silver/ventas/")
X = df.drop(["ingresos", "transaction_id", "timestamp"], axis=1)
y = df["ingresos"]

X = X.select_dtypes(include=["number"])

# Split triple para modelos complejos
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

print(f"Train: {len(X_train):,} | Val: {len(X_val):,} | Test: {len(X_test):,}")

# Cross-validation
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
scores = cross_val_score(modelo, X_train, y_train, cv=5, scoring="r2")
print(f"CV R2: {scores.mean():.3f} +/- {scores.std():.3f}")
