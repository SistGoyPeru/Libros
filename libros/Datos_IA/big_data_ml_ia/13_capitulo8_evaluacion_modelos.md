# Capítulo 8: Evaluación y Optimización de Modelos

## 8.1 Métricas de Evaluación

### 8.1.1 Para Regresión

```python
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    mean_absolute_percentage_error, explained_variance_score
)

def evaluar_regresion(y_true, y_pred, nombre="Modelo"):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred) * 100
    r2 = r2_score(y_true, y_pred)
    ev = explained_variance_score(y_true, y_pred)

    print(f"=== {nombre} ===")
    print(f"RMSE:  ${rmse:.2f}")
    print(f"MAE:   ${mae:.2f}")
    print(f"MAPE:  {mape:.1f}%")
    print(f"R2:    {r2:.3f}")
    print(f"EV:    {ev:.3f}")

    return {"RMSE": rmse, "MAE": mae, "MAPE": mape, "R2": r2}
```

### 8.1.2 Para Clasificación

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_curve, auc, roc_auc_score, confusion_matrix,
    classification_report, log_loss
)

def evaluar_clasificacion(y_true, y_pred, y_proba=None, nombre="Modelo"):
    print(f"=== {nombre} ===")

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print(f"Accuracy:  {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall:    {recall:.3f}")
    print(f"F1-Score:  {f1:.3f}")

    if y_proba is not None:
        auc = roc_auc_score(y_true, y_proba)
        print(f"AUC-ROC:   {auc:.3f}")

    # Matriz de confusión
    cm = confusion_matrix(y_true, y_pred)
    print(f"\nMatriz de Confusión:")
    print(f"  VP: {cm[1,1]:,}  FP: {cm[0,1]:,}")
    print(f"  FN: {cm[1,0]:,}  VN: {cm[0,0]:,}")

    return {"accuracy": accuracy, "precision": precision,
            "recall": recall, "f1": f1}
```

## 8.2 Validación Cruzada

```python
from sklearn.model_selection import (
    cross_val_score, cross_validate, KFold, StratifiedKFold,
    learning_curve, validation_curve
)
import matplotlib.pyplot as plt

# K-Fold para regresión
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(rf, X_train, y_train, cv=kf, scoring="r2")
print(f"R2 por fold: {scores}")
print(f"R2 promedio: {scores.mean():.3f} ± {scores.std():.3f}")

# Cross-validate completa
cv_results = cross_validate(
    rf, X_train, y_train,
    cv=5,
    scoring=["r2", "neg_mean_squared_error", "neg_mean_absolute_error"],
    return_train_score=True
)

print(f"Train R2: {cv_results['train_r2'].mean():.3f}")
print(f"Test R2:  {cv_results['test_r2'].mean():.3f}")

# Curvas de aprendizaje
train_sizes, train_scores, test_scores = learning_curve(
    rf, X_train, y_train,
    cv=5, n_jobs=-1,
    train_sizes=np.linspace(0.1, 1.0, 10)
)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores.mean(axis=1), "o-", label="Train")
plt.plot(train_sizes, test_scores.mean(axis=1), "o-", label="Validation")
plt.xlabel("Training examples")
plt.ylabel("R2 Score")
plt.legend()
plt.title("Learning Curve - Random Forest")
plt.savefig("img/learning_curve.png")
```

## 8.3 Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import randint, uniform
import time

# Grid Search (exhaustivo)
param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [10, 15, 20, None],
    "min_samples_leaf": [1, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1,
    verbose=1
)

t0 = time.time()
grid_search.fit(X_train, y_train)
print(f"Grid Search: {time.time() - t0:.1f}s")

print(f"Mejores parámetros: {grid_search.best_params_}")
print(f"Mejor R2 (CV): {grid_search.best_score_:.3f}")

# Random Search (más eficiente)
param_dist = {
    "n_estimators": randint(100, 500),
    "max_depth": randint(5, 30),
    "min_samples_leaf": randint(1, 20),
    "max_features": ["sqrt", "log2", None],
    "bootstrap": [True, False]
}

random_search = RandomizedSearchCV(
    RandomForestRegressor(random_state=42),
    param_dist,
    n_iter=50,
    cv=3,
    scoring="r2",
    n_jobs=-1,
    random_state=42
)

t0 = time.time()
random_search.fit(X_train, y_train)
print(f"\nRandom Search: {time.time() - t0:.1f}s")

print(f"Mejores parámetros: {random_search.best_params_}")
print(f"Mejor R2 (CV): {random_search.best_score_:.3f}")
```

## 8.4 Overfitting y Underfitting

```python
# Detectar overfitting
def detectar_overfitting(modelo, X_train, y_train, X_test, y_test):
    train_score = modelo.score(X_train, y_train)
    test_score = modelo.score(X_test, y_test)
    diff = train_score - test_score

    print(f"Train R2: {train_score:.3f}")
    print(f"Test R2:  {test_score:.3f}")
    print(f"Diferencia: {diff:.3f}")

    if diff > 0.1:
        print("⚠️ Posible OVERFITTING (diferencia > 0.1)")
    elif diff < -0.05:
        print("⚠️ Posible UNDERFITTING (test > train)")
    else:
        print("✅ Modelo balanceado")

# Regularización para combatir overfitting
print("\n=== Sin regularización ===")
dt_deep = DecisionTreeRegressor(max_depth=None, random_state=42)
dt_deep.fit(X_train, y_train)
detectar_overfitting(dt_deep, X_train, y_train, X_test, y_test)

print("\n=== Con regularización ===")
dt_reg = DecisionTreeRegressor(max_depth=8, min_samples_leaf=20, random_state=42)
dt_reg.fit(X_train, y_train)
detectar_overfitting(dt_reg, X_train, y_train, X_test, y_test)

# Curva de validación para max_depth
param_range = range(1, 21)
train_scores, test_scores = validation_curve(
    DecisionTreeRegressor(random_state=42),
    X_train, y_train,
    param_name="max_depth",
    param_range=param_range,
    cv=5, scoring="r2"
)

plt.figure(figsize=(10, 6))
plt.plot(param_range, train_scores.mean(axis=1), "o-", label="Train")
plt.plot(param_range, test_scores.mean(axis=1), "o-", label="Validation")
plt.axvline(x=8, color="r", linestyle="--", label="Optimal depth")
plt.xlabel("max_depth")
plt.ylabel("R2 Score")
plt.legend()
plt.title("Validation Curve - max_depth")
plt.savefig("img/validation_curve.png")
```

## 8.5 Ejercicios

1. **Grid Search**: Optimiza un XGBoost con GridSearch sobre learning_rate, n_estimators y max_depth.
2. **Curvas de Aprendizaje**: Genera curvas de aprendizaje para Random Forest con diferentes tamaños de dataset. ¿Cuándo deja de mejorar?
3. **Overfitting**: Entrena un modelo sin regularización y otro con regularización fuerte. Compara train/test scores.
4. **Validación Cruzada**: Implementa StratifiedKFold para clasificación y explica por qué es mejor que KFold simple.
5. **Métricas**: Para un problema de detección de fraude (1% de casos), ¿qué métrica es más importante? Justifica.
