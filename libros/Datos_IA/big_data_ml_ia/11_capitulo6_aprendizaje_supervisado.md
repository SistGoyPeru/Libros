# Capítulo 6: Aprendizaje Supervisado

## 6.1 Regresión

### 6.1.1 Regresión Lineal

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Modelo base
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

print(f"R2: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: ${np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")

# Coeficientes (interpretabilidad)
coeficientes = pd.DataFrame({
    "feature": num_features,
    "coef": lr.coef_[:len(num_features)]
}).sort_values("coef", key=abs, ascending=False)

print("Features más importantes:")
print(coeficientes.head(5))

# Ridge (L2) vs Lasso (L1)
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.01)

ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

print(f"Ridge R2: {r2_score(y_test, ridge.predict(X_test)):.3f}")
print(f"Lasso R2: {r2_score(y_test, lasso.predict(X_test)):.3f}")
print(f"Features usadas por Lasso: {np.sum(lasso.coef_ != 0)}/{len(lasso.coef_)}")
```

### 6.1.2 Árboles de Decisión

```python
from sklearn.tree import DecisionTreeRegressor, plot_tree
import matplotlib.pyplot as plt

# Árbol simple (interpretable)
dt = DecisionTreeRegressor(max_depth=3, min_samples_leaf=50, random_state=42)
dt.fit(X_train, y_train)

print(f"R2 (train): {dt.score(X_train, y_train):.3f}")
print(f"R2 (test): {dt.score(X_test, y_test):.3f}")

# Visualizar el árbol
plt.figure(figsize=(20, 10))
plot_tree(dt, feature_names=X_train.columns, filled=True, fontsize=10)
plt.savefig("img/arbol_decision.png", dpi=150)

# Feature importance
importancias = pd.DataFrame({
    "feature": X_train.columns,
    "importance": dt.feature_importances_
}).sort_values("importance", ascending=False)
```

### 6.1.3 Random Forest

```python
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

# Random Forest
rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    min_samples_leaf=10,
    n_jobs=-1,
    random_state=42
)
rf.fit(X_train, y_train)

# Gradient Boosting
gbr = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
gbr.fit(X_train, y_train)

# XGBoost (el rey de los datos tabulares)
xgb = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=7,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
xgb.fit(X_train, y_train)

# Comparación
modelos = {
    "Random Forest": rf,
    "Gradient Boosting": gbr,
    "XGBoost": xgb
}

for nombre, modelo in modelos.items():
    y_pred = modelo.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"{nombre:20s} | RMSE: ${rmse:.2f} | R2: {r2:.3f}")
```

## 6.2 Clasificación

### 6.2.1 Regresión Logística

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Crear target binario: cliente premium (>$1000 gasto total)
df["es_premium"] = (df.groupby("customer_id")["amount"].transform("sum") > 1000).astype(int)

y_clf = df["es_premium"]
X_clf = df.drop(["es_premium", "transaction_id", "timestamp", "amount"], axis=1)

X_c_train, X_c_test, y_c_train, y_c_test = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42
)

# Regresión logística
log_reg = LogisticRegression(class_weight="balanced", max_iter=1000)
log_reg.fit(X_c_train, y_c_train)
y_c_pred = log_reg.predict(X_c_test)
y_c_proba = log_reg.predict_proba(X_c_test)[:, 1]

print(classification_report(y_c_test, y_c_pred))
print(f"AUC-ROC: {roc_auc_score(y_c_test, y_c_proba):.3f}")
```

### 6.2.2 Random Forest Classifier

```python
from sklearn.ensemble import RandomForestClassifier

rf_clf = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    class_weight="balanced",
    random_state=42
)
rf_clf.fit(X_c_train, y_c_train)
y_c_pred_rf = rf_clf.predict(X_c_test)

print("Random Forest Classifier:")
print(classification_report(y_c_test, y_c_pred_rf))

# Matriz de confusión
cm = confusion_matrix(y_c_test, y_c_pred_rf)
print(f"\nMatriz de Confusión:")
print(f"VN: {cm[0,0]:,} | FP: {cm[0,1]:,}")
print(f"FN: {cm[1,0]:,} | VP: {cm[1,1]:,}")
```

### 6.2.3 XGBoost Classifier

```python
from xgboost import XGBClassifier

xgb_clf = XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6,
    scale_pos_weight=(y_c_train == 0).sum() / (y_c_train == 1).sum(),
    random_state=42
)
xgb_clf.fit(X_c_train, y_c_train)

# Feature importance
importance_df = pd.DataFrame({
    "feature": X_c_train.columns,
    "importance": xgb_clf.feature_importances_
}).sort_values("importance", ascending=False)

print("Top 10 features predictivas:")
print(importance_df.head(10))
```

## 6.3 Ejercicios

1. **Regresión**: Predice el ticket promedio por cliente usando Random Forest y optimiza los hiperparámetros.
2. **Clasificación**: Crea un modelo que prediga si un producto será "top seller" (>100 unidades) usando XGBoost.
3. **Comparación**: Compara LinearRegression, Ridge, Lasso, Random Forest y XGBoost en el mismo dataset. ¿Cuál gana?
4. **Interpretación**: Usa SHAP para explicar las predicciones del mejor modelo de clasificación.
5. **Desequilibrio**: Crea un dataset desbalanceado (95% no-premium, 5% premium) y prueba técnicas de balanceo (SMOTE, class_weight).
