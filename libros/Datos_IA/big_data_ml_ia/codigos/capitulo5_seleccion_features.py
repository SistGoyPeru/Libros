"""Capítulo 5: Selección de features con SelectKBest e importancia del modelo"""

from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_parquet("data/silver/ventas/")
X = df.drop(["ingresos", "transaction_id", "timestamp"], axis=1)
y = df["ingresos"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Selección basada en correlación
selector = SelectKBest(score_func=f_regression, k=10)
X_selected = selector.fit_transform(X_train, y_train)
print(f"Features seleccionadas: {X_selected.shape[1]}")

# Importancia del modelo
# Nota: en un pipeline real usarías preprocessing antes
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train.select_dtypes(include=["number"]), y_train)

importancias = pd.DataFrame({
    "feature": X_train.select_dtypes(include=["number"]).columns,
    "importance": modelo.feature_importances_
}).sort_values("importance", ascending=False)

print(importancias.head(10))
