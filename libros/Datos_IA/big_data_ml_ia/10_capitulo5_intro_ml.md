# Capítulo 5: Introducción al Machine Learning

## 5.1 El Pipeline de ML

El machine learning no es magia; es un proceso estructurado. El pipeline clásico consta de:

```mermaid
graph LR
    A[Datos] --> B[Preprocesamiento]
    B --> C[Train/Test Split]
    C --> D[Entrenamiento]
    D --> E[Evaluación]
    E --> F[Despliegue]
    F --> G[Monitoreo]
    G --> A
```

### 5.1.1 Tipos de Aprendizaje

```python
tipos = {
    "Supervisado": "Etiquetas conocidas (regresión, clasificación)",
    "No supervisado": "Sin etiquetas (clustering, reducción de dimensionalidad)",
    "Semi-supervisado": "Pocas etiquetas, muchos datos sin etiquetar",
    "Refuerzo": "Agente aprende por recompensas (RL)"
}
```

## 5.2 Scikit-learn: La Biblioteca Esencial

### 5.2.1 API Consistente

```python
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
```

### 5.2.2 Preprocesamiento

```python
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
```

## 5.3 Feature Engineering

### 5.3.1 Creación de Features

```python
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
```

### 5.3.2 Selección de Features

```python
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression

# Selección basada en correlación
selector = SelectKBest(score_func=f_regression, k=10)
X_selected = selector.fit_transform(X_train, y_train)

# Importancia del modelo
modelo.fit(X_train, y_train)
importancias = pd.DataFrame({
    "feature": X_train.columns,
    "importance": modelo.named_steps["regressor"].feature_importances_
}).sort_values("importance", ascending=False)

print(importancias.head(10))
```

## 5.4 Train/Test/Validation Split

```python
from sklearn.model_selection import train_test_split, cross_val_score

# Split triple para modelos complejos
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

print(f"Train: {len(X_train):,} | Val: {len(X_val):,} | Test: {len(X_test):,}")

# Cross-validation
scores = cross_val_score(modelo, X_train, y_train, cv=5, scoring="r2")
print(f"CV R2: {scores.mean():.3f} +/- {scores.std():.3f}")
```

## 5.5 Métricas Fundamentales

```python
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

# Para regresión: predicción de ingresos
metricas_regresion = {
    "MSE": mean_squared_error(y_test, y_pred),
    "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
    "MAE": mean_absolute_error(y_test, y_pred),
    "R2": r2_score(y_test, y_pred),
    "MAPE": np.mean(np.abs((y_test - y_pred) / y_test)) * 100
}
```

## 5.6 Ejercicios

1. **Pipeline**: Construye un pipeline completo para predecir ingresos de TechStore con preprocessing y 3 modelos diferentes.
2. **Feature Engineering**: Crea 5 features nuevas a partir de los datos de TechStore y mide su impacto en R2.
3. **Cross-Validation**: Compara CV=5 vs CV=10 en términos de tiempo y estabilidad de métricas.
4. **Métricas**: Para un modelo de clasificación (cliente premium vs básico), calcula precisión, recall y F1.
5. **Overfitting**: Demuestra overfitting entrenando un árbol de decisión sin limitar profundidad vs con max_depth=5.
