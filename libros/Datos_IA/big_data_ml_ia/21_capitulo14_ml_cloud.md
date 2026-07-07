# Capítulo 14: Machine Learning en la Nube

## 14.1 BigQuery ML

BigQuery ML permite crear y ejecutar modelos de ML directamente con SQL, sin mover datos.

### 14.1.1 Configuración

```python
from google.cloud import bigquery
from google.cloud import aiplatform
import pandas as pd

# Cliente BigQuery
client = bigquery.Client(project="techstore-analytics")

# Verificar datasets
datasets = list(client.list_datasets())
print("Datasets disponibles:")
for ds in datasets:
    print(f"  {ds.dataset_id}")
```

### 14.1.2 Modelos con SQL

```sql
-- Modelo de regresión lineal para predecir CLV
CREATE OR REPLACE MODEL `techstore.clv_model`
OPTIONS(
    model_type='linear_reg',
    input_label_cols=['total_spent'],
    l1_reg=0.01,
    l2_reg=0.01,
    max_iterations=50
) AS
SELECT
    customer_id,
    visit_count,
    avg_session_duration,
    categories_viewed,
    days_since_last_visit,
    total_spent
FROM `techstore.features.train_data`
```

```python
# Evaluar modelo
query_eval = """
SELECT
    *
FROM ML.EVALUATE(MODEL `techstore.clv_model`,
    TABLE `techstore.features.eval_data`)
"""
eval_result = client.query(query_eval).to_dataframe()
print(eval_result)

# Predecir
query_pred = """
SELECT
    customer_id,
    predicted_total_spent AS predicted_clv
FROM ML.PREDICT(MODEL `techstore.clv_model`,
    TABLE `techstore.features.new_customers`)
ORDER BY predicted_clv DESC
LIMIT 10
"""
predicciones = client.query(query_pred).to_dataframe()
print(predicciones)
```

### 14.1.3 XGBoost en BigQuery

```sql
-- Modelo XGBoost para clasificación de clientes premium
CREATE OR REPLACE MODEL `techstore.premium_classifier`
OPTIONS(
    model_type='boosted_tree_classifier',
    input_label_cols=['is_premium'],
    l1_reg=0.01,
    l2_reg=0.01,
    num_parallel_tree=8,
    max_tree_depth=6,
    subsample=0.8,
    learn_rate=0.1,
    min_tree_child_weight=5,
    early_stop=True
) AS
SELECT
    visit_count,
    avg_session_duration,
    categories_viewed,
    products_viewed,
    days_since_last_visit,
    is_premium
FROM `techstore.features.train_data`
```

```python
# Feature importance
query_importance = """
SELECT
    input,
    weight
FROM ML.FEATURE_IMPORTANCE(MODEL `techstore.premium_classifier`)
ORDER BY weight DESC
"""
importance = client.query(query_importance).to_dataframe()
print("Feature Importance (BigQuery ML):")
print(importance)
```

## 14.2 Vertex AI

### 14.2.1 Custom Training

```python
from google.cloud.aiplatform import CustomTrainingJob
from google.cloud.aiplatform import hyperparameter_tuning as hp

# Configurar Vertex AI
aiplatform.init(
    project="techstore-analytics",
    location="us-central1",
    staging_bucket="gs://techstore-ml-staging"
)

# Job de entrenamiento personalizado
job = CustomTrainingJob(
    display_name="techstore-xgboost-training",
    script_path="trainers/train_xgboost.py",
    container_uri="us-docker.pkg.dev/vertex-ai/training/xgboost-cpu.1-1:latest",
    requirements=["pandas", "scikit-learn", "cloudml-hypertune"],
    model_serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.1-1:latest"
)

# Ejecutar
model = job.run(
    model_display_name="techstore-clv-predictor",
    replica_count=1,
    machine_type="n1-standard-4",
    args=["--data-dir=gs://techstore-ml-staging/data"]
)
```

### 14.2.2 AutoML

```python
from google.cloud.aiplatform import AutoMLTabularTrainingJob

# AutoML para clasificación
automl_job = AutoMLTabularTrainingJob(
    display_name="techstore-automl-premium",
    optimization_prediction_type="classification",
    optimization_objective="maximize-au-roc"
)

# Dataset
dataset = aiplatform.TabularDataset.create(
    display_name="techstore-customers",
    gcs_source=["gs://techstore-ml-staging/data/customers_for_automl.csv"]
)

# Entrenar
model_automl = automl_job.run(
    dataset=dataset,
    target_column="is_premium",
    budget_milli_node_hours=1000,
    model_display_name="techstore-automl-premium-model"
)

# Evaluar
evaluation = model_automl.evaluate()
print(f"AutoML AUC-ROC: {evaluation.metrics['auRoc']:.3f}")
```

### 14.2.3 Endpoint y Predicciones

```python
# Desplegar modelo
endpoint = model.deploy(
    machine_type="n1-standard-2",
    min_replica_count=1,
    max_replica_count=3,
    traffic_split={"0": 100}
)

# Predicción batch
batch_prediction_job = model.batch_predict(
    job_display_name="techstore-batch-prediction",
    gcs_source="gs://techstore-ml-staging/data/to_predict.csv",
    gcs_destination_prefix="gs://techstore-ml-staging/predictions/",
    machine_type="n1-standard-4"
)

# Predicción online
instances = [
    {"visit_count": 15, "avg_session_duration": 300, "categories_viewed": 5}
]
prediction = endpoint.predict(instances=instances)
print(f"Predicción CLV: ${prediction.predictions[0]:.2f}")
```

## 14.3 Pipelines Serverless

```python
from google.cloud.aiplatform import PipelineJob

# Pipeline de ML completo
pipeline_definition = """
apiVersion: argoproj.io/v1alpha1
kind: Workflow
spec:
  entrypoint: ml-pipeline
  templates:
    - name: ml-pipeline
      dag:
        tasks:
          - name: data-preparation
            template: data-prep
          - name: model-training
            template: training
            dependsOn: data-preparation
          - name: model-evaluation
            template: evaluation
            dependsOn: model-training
          - name: model-deployment
            template: deployment
            dependsOn: model-evaluation
"""

# Ejecutar pipeline
pipeline = PipelineJob(
    display_name="techstore-ml-pipeline",
    template_path="pipeline.yaml",
    pipeline_root="gs://techstore-ml-staging/pipelines",
    parameter_values={
        "project": "techstore-analytics",
        "data_path": "gs://techstore-ml-staging/data"
    }
)

pipeline.run(sync=False)
print(f"Pipeline Job ID: {pipeline.resource_name}")
```

## 14.4 Ejercicios

1. **BigQuery ML**: Crea un modelo de regresión logística en BigQuery ML para predecir churn de clientes.
2. **Vertex AI AutoML**: Entrena un modelo de clasificación con AutoML y compáralo con un modelo custom de XGBoost.
3. **Endpoint**: Despliega un modelo en Vertex AI Endpoint y haz 10 predicciones online.
4. **Batch Prediction**: Configura una predicción batch para 100,000 clientes y mide el tiempo de ejecución.
5. **Pipeline**: Diseña un pipeline de Vertex AI Pipelines que incluya: data validation → training → evaluation → deployment.
