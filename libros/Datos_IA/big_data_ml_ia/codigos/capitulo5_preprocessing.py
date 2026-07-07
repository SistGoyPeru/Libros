"""Capítulo 5: Preprocesamiento con ColumnTransformer y Pipeline"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

df = pd.read_parquet("data/silver/ventas/")
X = df.drop(["ingresos", "transaction_id", "timestamp"], axis=1)
y = df["ingresos"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Definir tipos de columnas
num_features = ["precio_unitario", "cantidad", "descuento", "edad_cliente"]
cat_features = ["categoria", "region", "segmento", "metodo_pago"]

# Transformadores
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_features)
    ]
)

# Pipeline completo
modelo = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Entrenar
modelo.fit(X_train, y_train)
print("Modelo entrenado correctamente")
