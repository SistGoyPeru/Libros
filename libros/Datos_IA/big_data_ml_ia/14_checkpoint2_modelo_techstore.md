# Checkpoint 2: Modelo Predictivo para TechStore

## Objetivo

Construir, evaluar y optimizar un modelo de machine learning que prediga el valor de vida del cliente (CLV) en TechStore.

## Dataset

Usa los datos procesados del Checkpoint 1 (capa Silver) y enriquece con features de clientes.

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
ventas = pd.read_parquet("data/silver/ventas/")
clientes = pd.read_parquet("data/silver/clientes/")
```

## Feature Engineering

```python
# Agregar features por cliente
clv_features = ventas.groupby("customer_id").agg(
    freq_total=("transaction_id", "count"),
    monto_total=("amount", "sum"),
    ticket_promedio=("amount", "mean"),
    ticket_max=("amount", "max"),
    ticket_std=("amount", "std"),
    antiguedad_dias=("timestamp", lambda x: (x.max() - x.min()).days),
    dias_ultima_compra=("timestamp", lambda x: (pd.Timestamp("2025-12-31") - x.max()).days),
    categorias_distintas=("category", "nunique"),
    productos_distintos=("product_id", "nunique"),
    devoluciones=("es_devolucion", "sum"),
    metodo_pago_frecuente=("metodo_pago", lambda x: x.mode().iloc[0] if not x.mode().empty else "unknown")
).reset_index()

# Merge con datos demográficos
clv = clv_features.merge(clientes, on="customer_id", how="left")

# Target: CLV = monto_total (valor de vida del cliente)
y = clv["monto_total"]
X = clv.drop(["customer_id", "monto_total"], axis=1)

# Separar numéricas y categóricas
num_features = X.select_dtypes(include=[np.number]).columns.tolist()
cat_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

print(f"Features numéricas: {len(num_features)}")
print(f"Features categóricas: {len(cat_features)}")
print(f"Dataset: {len(X):,} clientes")
```

## Pipeline de Modelado

```python
# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_features)
    ]
)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelos a probar
modelos = {
    "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=200, learning_rate=0.05, random_state=42)
}

resultados = []

for nombre, modelo in modelos.items():
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", modelo)
    ])

    # Cross-validation
    scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="r2")

    # Entrenar
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    resultados.append({
        "modelo": nombre,
        "R2_CV": scores.mean(),
        "R2_CV_std": scores.std(),
        "R2_Test": r2_score(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "MAE": mean_absolute_error(y_test, y_pred)
    })

resultados_df = pd.DataFrame(resultados).sort_values("R2_Test", ascending=False)
print(resultados_df.to_string(index=False))
```

## Optimización del Mejor Modelo

```python
# Optimizar XGBoost
param_grid = {
    "regressor__n_estimators": [100, 200, 300],
    "regressor__learning_rate": [0.01, 0.05, 0.1],
    "regressor__max_depth": [4, 6, 8],
    "regressor__subsample": [0.7, 0.8, 1.0],
    "regressor__colsample_bytree": [0.7, 0.8, 1.0]
}

pipeline_xgb = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", XGBRegressor(random_state=42))
])

grid = GridSearchCV(
    pipeline_xgb,
    param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1,
    verbose=1
)

grid.fit(X_train, y_train)

print(f"Mejores parámetros: {grid.best_params_}")
print(f"Mejor R2 (CV): {grid.best_score_:.3f}")
print(f"R2 (Test): {r2_score(y_test, grid.predict(X_test)):.3f}")

# Feature importance
best_model = grid.best_estimator_
importancias = pd.DataFrame({
    "feature": num_features,
    "importance": best_model.named_steps["regressor"].feature_importances_[:len(num_features)]
}).sort_values("importance", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=importancias.head(15), x="importance", y="feature")
plt.title("Top 15 Features para Predicción de CLV")
plt.tight_layout()
plt.savefig("img/feature_importance_clv.png")
```

## Análisis de Errores

```python
# Análisis de residuos
y_pred_best = best_model.predict(X_test)
residuos = y_test - y_pred_best

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.scatter(y_pred_best, y_test, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
plt.xlabel("Predicho")
plt.ylabel("Real")
plt.title("Predicho vs Real")

plt.subplot(1, 3, 2)
plt.scatter(y_pred_best, residuos, alpha=0.5)
plt.axhline(y=0, color="r", linestyle="--")
plt.xlabel("Predicho")
plt.ylabel("Residuo")
plt.title("Residuos")

plt.subplot(1, 3, 3)
plt.hist(residuos, bins=50, edgecolor="black")
plt.xlabel("Error ($)")
plt.title("Distribución de Errores")

plt.tight_layout()
plt.savefig("img/analisis_errores_clv.png")
```

## Entregables

1. Pipeline completo con preprocesamiento y 3 modelos
2. Grid Search con el mejor modelo optimizado
3. Feature importance plot
4. Análisis de errores (predicho vs real, residuos)
5. Modelo final serializado (`modelo_clv.pkl`)

## Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Feature engineering completo | 20 |
| Pipeline con 3+ modelos | 20 |
| Optimización de hiperparámetros | 20 |
| Análisis de errores | 20 |
| Feature importance interpretable | 10 |
| Modelo serializado | 10 |

¡Has construido un modelo predictivo de CLV listo para producción!
