# Capítulo 12: MLOps: Machine Learning en Producción

## 12.1 Introducción a MLOps

MLOps es el conjunto de prácticas que unen el desarrollo de ML con las operaciones de producción. Es la respuesta a: "funciona en mi Jupyter, pero ¿cómo lo llevo a producción?"

```python
pilares_mlops = {
    "Experimentación": "Seguimiento de parámetros, métricas, artefactos",
    "Reproducibilidad": "Versionado de datos, código, modelos, entorno",
    "Despliegue": "APIs, batch inference, edge deployment",
    "Monitoreo": "Data drift, model decay, alertas automáticas",
    "Gobernanza": "Auditoría, explicabilidad, fairness, compliance"
}
```

## 12.2 MLflow: Experiment Tracking

### 12.2.1 Configuración Inicial

```python
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient

# Configurar MLflow
mlflow.set_tracking_uri("http://localhost:5000")  # o "file:./mlruns"
mlflow.set_experiment("techstore-clv-prediction")

# O usar tracking local
# mlflow.set_tracking_uri("./mlruns")
```

### 12.2.2 Registro de Experimentos

```python
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

# Experimentar con diferentes modelos
modelos_exp = {
    "RandomForest": {
        "modelo": RandomForestRegressor(n_estimators=200, random_state=42),
        "params": {"n_estimators": 200, "max_depth": "default"}
    },
    "XGBoost": {
        "modelo": XGBRegressor(n_estimators=200, learning_rate=0.05, random_state=42),
        "params": {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 6}
    },
    "GradientBoosting": {
        "modelo": GradientBoostingRegressor(n_estimators=100, random_state=42),
        "params": {"n_estimators": 100, "learning_rate": 0.1}
    }
}

for nombre, config in modelos_exp.items():
    with mlflow.start_run(run_name=nombre):
        # Log parámetros
        for key, value in config["params"].items():
            mlflow.log_param(key, value)

        # Entrenar
        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("regressor", config["modelo"])
        ])
        pipeline.fit(X_train, y_train)

        # Predecir
        y_pred = pipeline.predict(X_test)

        # Log métricas
        mlflow.log_metric("rmse", np.sqrt(mean_squared_error(y_test, y_pred)))
        mlflow.log_metric("mae", mean_absolute_error(y_test, y_pred))
        mlflow.log_metric("r2", r2_score(y_test, y_pred))

        # Log modelo
        mlflow.sklearn.log_model(pipeline, f"model_{nombre}")

        # Log artefactos adicionales
        mlflow.log_artifact("img/feature_importance_clv.png")
        mlflow.log_artifact("img/analisis_errores_clv.png")

        print(f"Run {nombre} completado: R2={r2_score(y_test, y_pred):.3f}")
```

### 12.2.3 Comparación de Runs

```python
# Cargar experimentos
client = MlflowClient()
experiment = client.get_experiment_by_name("techstore-clv-prediction")

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.r2 DESC"],
    max_results=5
)

print("=== Top 5 Runs ===")
for run in runs:
    print(f"  {run.data.tags.get('mlflow.runName', 'unknown'):20s} "
          f"| R2: {run.data.metrics.get('r2', 0):.3f} "
          f"| RMSE: ${run.data.metrics.get('rmse', 0):.2f}")

# Obtener mejor modelo
best_run = runs[0]
best_model_uri = f"runs:/{best_run.info.run_id}/model_XGBoost"
best_model = mlflow.sklearn.load_model(best_model_uri)

print(f"\nMejor modelo cargado desde: {best_model_uri}")
```

### 12.2.4 Model Registry

```python
# Registrar modelo en MLflow Model Registry
result = mlflow.register_model(
    model_uri=best_model_uri,
    name="TechStore_CLV_Model"
)

# Transicionar a diferentes stages
client.transition_model_version_stage(
    name="TechStore_CLV_Model",
    version=result.version,
    stage="Staging"
)

# Promover a producción
client.transition_model_version_stage(
    name="TechStore_CLV_Model",
    version=result.version,
    stage="Production"
)

# Listar versiones
for mv in client.search_model_versions("name='TechStore_CLV_Model'"):
    print(f"Versión {mv.version}: stage={mv.current_stage}, "
          f"run_id={mv.run_id[:8]}...")
```

## 12.3 Versionado de Modelos

```python
# Versionado manual con DVC (Data Version Control)
# dvc init
# dvc add data/
# dvc add models/

# Versionado automático con MLflow
import joblib
from datetime import datetime

def guardar_modelo_versionado(modelo, metricas, nombre="modelo_clv"):
    version = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"models/{nombre}_{version}.pkl"

    # Guardar modelo
    joblib.dump(modelo, path)

    # Guardar metadata
    metadata = {
        "version": version,
        "fecha": datetime.now().isoformat(),
        "metricas": metricas,
        "features": X_train.columns.tolist()
    }
    joblib.dump(metadata, f"models/{nombre}_{version}_metadata.pkl")

    print(f"Modelo guardado: {path}")
    return version

# Ejemplo de uso
metricas = {"rmse": rmse, "r2": r2, "mae": mae}
version = guardar_modelo_versionado(best_model, metricas)

# Cargar modelo específico
def cargar_modelo_version(version):
    return joblib.load(f"models/modelo_clv_{version}.pkl")
```

## 12.4 Monitoreo de Modelos en Producción

### 12.4.1 Data Drift Detection

```python
from scipy.stats import ks_2samp
import warnings
warnings.filterwarnings("ignore")

def detectar_data_drift(datos_referencia, datos_nuevos, features, threshold=0.05):
    """
    Detectar drift entre datos de entrenamiento y nuevos datos
    usando Kolmogorov-Smirnov test
    """
    drifts = []
    for feature in features:
        stat, p_value = ks_2samp(datos_referencia[feature], datos_nuevos[feature])
        if p_value < threshold:
            drifts.append({
                "feature": feature,
                "statistic": stat,
                "p_value": p_value,
                "drift": True
            })

    return pd.DataFrame(drifts)

# Simular datos nuevos con drift
datos_nuevos = X_test.copy()
datos_nuevos["freq_total"] = datos_nuevos["freq_total"] * 1.5  # drift artificial

drift_result = detectar_data_drift(
    X_train, datos_nuevos,
    features=num_features
)

print(f"Features con drift detectado: {len(drift_result)}")
if len(drift_result) > 0:
    print(drift_result[["feature", "p_value"]].to_string(index=False))
```

### 12.4.2 Performance Monitoring

```python
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("model_monitor")

# Configuración de alertas
config_monitoreo = {
    "rmse_threshold": 50.0,
    "mae_threshold": 35.0,
    "min_predicciones": 100,
    "ventana_drift": "7d",
    "alertas_email": ["data-team@techstore.com"]
}

def evaluar_modelo_produccion():
    """Evaluar rendimiento del modelo en producción"""
    ventana = datetime.now() - timedelta(days=7)
    datos_recientes = obtener_datos_desde(ventana)

    if len(datos_recientes) < config_monitoreo["min_predicciones"]:
        logger.warning(f"Datos insuficientes: {len(datos_recientes)}")
        return

    # Predecir y evaluar
    X_reciente = datos_recientes.drop(["customer_id", "monto_total"], axis=1)
    y_reciente = datos_recientes["monto_total"]
    y_pred = best_model.predict(X_reciente)

    rmse_actual = np.sqrt(mean_squared_error(y_reciente, y_pred))
    mae_actual = mean_absolute_error(y_reciente, y_pred)

    logger.info(f"RMSE actual: ${rmse_actual:.2f}")
    logger.info(f"MAE actual: ${mae_actual:.2f}")

    # Alertas
    if rmse_actual > config_monitoreo["rmse_threshold"]:
        logger.error(f"⚠️ RMSE excedió umbral: ${rmse_actual:.2f}")
        enviar_alerta(f"RMSE crítico: ${rmse_actual:.2f}")

    return {"rmse": rmse_actual, "mae": mae_actual, "fecha": datetime.now()}
```

## 12.5 Ejercicios

1. **MLflow Setup**: Configura MLflow (local o cloud) y registra 3 experimentos con diferentes modelos de TechStore.
2. **Model Registry**: Promueve un modelo de Staging a Production y demuestra cómo cargar cada versión.
3. **Data Drift**: Implementa detección de drift para las features numéricas del modelo CLV. Simula 3 escenarios de drift.
4. **Dashboard de Monitoreo**: Crea un dashboard en Streamlit que muestre métricas en tiempo real del modelo en producción.
5. **Pipeline MLOps**: Diseña un pipeline completo: entrenamiento → registro → staging → production → monitoreo → alertas.
