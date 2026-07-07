# Checkpoint 3: Pipeline de ML Completo

## Objetivo

Construir un pipeline de machine learning completo que integre experimentación (MLflow), forecasting (Prophet/LSTM), NLP (análisis de sentimiento de reseñas) y MLOps con monitoreo de drift.

## Dataset

- `techstore_transactions.parquet` — para modelo de ventas
- `techstore_reviews.parquet` — para NLP
- `techstore_customers.parquet` — para features

## Pipeline

### Fase 1: Experimentación con MLflow

```python
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib

mlflow.set_experiment("techstore-ml-pipeline")

df = pd.read_parquet("data/silver/ventas/")
y = df["amount"]
X = df.drop(["amount", "transaction_id", "timestamp"], axis=1)

num_features = X.select_dtypes(include=[np.number]).columns.tolist()
cat_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_features),
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_features)
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelos = {
    "RF": RandomForestRegressor(n_estimators=200, random_state=42),
    "GB": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "XGB": XGBRegressor(n_estimators=200, learning_rate=0.05, random_state=42),
    "Ensemble": VotingRegressor([
        ("rf", RandomForestRegressor(n_estimators=100, random_state=42)),
        ("xgb", XGBRegressor(n_estimators=100, learning_rate=0.05, random_state=42))
    ])
}

mejor_modelo = None
mejor_r2 = -np.inf

for nombre, modelo in modelos.items():
    with mlflow.start_run(run_name=nombre):
        pipeline = Pipeline([("preprocessor", preprocessor), ("model", modelo)])
        cv_scores = cross_val_score(pipeline, X_train, y_train, cv=3, scoring="r2")

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)

        mlflow.log_param("model_type", nombre)
        mlflow.log_metric("cv_r2_mean", cv_scores.mean())
        mlflow.log_metric("test_r2", r2)
        mlflow.log_metric("test_rmse", rmse)
        mlflow.log_metric("test_mae", mae)
        mlflow.sklearn.log_model(pipeline, f"model_{nombre}")

        print(f"{nombre}: R2={r2:.3f}, RMSE=${rmse:.2f}, CV={cv_scores.mean():.3f}")

        if r2 > mejor_r2:
            mejor_r2 = r2
            mejor_modelo = pipeline

# Registrar mejor modelo
mlflow.register_model(
    f"runs:/{mlflow.active_run().info.run_id}/model_XGB",
    "TechStore_Predictor"
)
```

### Fase 2: Forecast de Ventas (Prophet + LSTM)

```python
from prophet import Prophet
from tensorflow import keras
from tensorflow.keras import layers

# Prophet
ventas_diarias = pd.read_parquet("data/silver/ventas_diarias/")
df_prophet = ventas_diarias.reset_index()[["fecha", "ingresos"]]
df_prophet.columns = ["ds", "y"]

modelo_prophet = Prophet(weekly_seasonality=True, seasonality_mode="multiplicative")
modelo_prophet.fit(df_prophet)
future = modelo_prophet.make_future_dataframe(periods=14)
forecast = modelo_prophet.predict(future)

# Guardar forecast
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].to_csv("data/gold/forecast_14d.csv", index=False)
print("Forecast generado: data/gold/forecast_14d.csv")
```

### Fase 3: Análisis de Sentimiento de Reseñas

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline as SkPipeline
import joblib

resenas = pd.read_parquet("data/techstore_reviews/")
resenas["sentimiento"] = (resenas["rating"] >= 4).astype(int)

pipeline_nlp = SkPipeline([
    ("tfidf", TfidfVectorizer(max_features=2000, ngram_range=(1, 2), min_df=5)),
    ("clf", LogisticRegression(class_weight="balanced"))
])

X_nlp_train, X_nlp_test, y_nlp_train, y_nlp_test = train_test_split(
    resenas["review_text"], resenas["sentimiento"],
    test_size=0.2, random_state=42
)

pipeline_nlp.fit(X_nlp_train, y_nlp_train)
acc = pipeline_nlp.score(X_nlp_test, y_nlp_test)
print(f"Sentiment Accuracy: {acc:.3f}")

joblib.dump(pipeline_nlp, "models/sentiment_model.pkl")
```

### Fase 4: Monitoreo MLOps

```python
def verificar_salud_modelos():
    from scipy.stats import ks_2samp

    reporte = {
        "fecha": pd.Timestamp.now().isoformat(),
        "modelo_principal": "TechStore_Predictor (XGBoost)",
        "r2_ultimo_test": mejor_r2,
        "forecast_disponible": True,
        "sentiment_accuracy": acc
    }

    # Detectar drift en datos nuevos simulados
    datos_recientes = df.sample(frac=0.1)
    drift_features = []

    for col in num_features[:5]:
        stat, p = ks_2samp(X_train[col], datos_recientes[col])
        if p < 0.05:
            drift_features.append(col)

    reporte["data_drift"] = len(drift_features) == 0
    reporte["features_con_drift"] = drift_features

    return pd.Series(reporte)

print("=== Reporte de Salud MLOps ===")
print(verificar_salud_modelos())
```

## Entregables

1. Pipeline ML con experiment tracking (MLflow)
2. Modelo registrado en Model Registry
3. Forecast de ventas a 14 días
4. Modelo de sentimiento para reseñas
5. Reporte de monitoreo MLOps

## Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Experiment tracking completo | 20 |
| Mejor modelo registrado | 15 |
| Forecast funcional | 15 |
| NLP pipeline funcional | 15 |
| Monitoreo y drift detection | 15 |
| Integración de todos los componentes | 20 |

¡Has construido un pipeline ML completo que integra experimentación, forecasting y MLOps!
