# Regresión Logística para Clasificación

A pesar de su nombre, la regresión logística es un algoritmo de clasificación, no de regresión. Es el punto de partida para problemas de clasificación binaria: ¿un email es spam o no? ¿un cliente comprará o no? ¿un paciente tiene una enfermedad?

## De Regresión Lineal a Logística

La regresión lineal predice valores continuos. La logística predice probabilidades. La clave está en la *función sigmoide* (o logística):

```
σ(z) = 1 / (1 + e^(-z))
```

Esta función transforma cualquier valor real en una probabilidad entre 0 y 1.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, roc_auc_score, roc_curve
)

def sigmoide(z):
    """Función sigmoide: mapea cualquier real a [0, 1]"""
    return 1 / (1 + np.exp(-z))

# La sigmoide en acción
z = np.linspace(-10, 10, 100)
p = sigmoide(z)

print(f"z = -10 → p = {sigmoide(-10):.6f} (prácticamente 0)")
print(f"z = 0   → p = {sigmoide(0):.4f} (exactamente 0.5)")
print(f"z = 10  → p = {sigmoide(10):.6f} (prácticamente 1)")
# z = -10 → p = 0.000045
# z = 0   → p = 0.5000
# z = 10  → p = 0.999955
```

## Cómo Funciona la Regresión Logística

El modelo calcula una combinación lineal de los predictores (como en regresión lineal) y luego aplica la sigmoide:

```
P(Y=1 | X) = σ(β₀ + β₁X₁ + ... + βₚXₚ) = 1 / (1 + e^-(β₀ + β₁X₁ + ... + βₚXₚ))
```

```python
# Simular datos de clasificación
np.random.seed(42)
n = 200

# Dos variables predictoras
X = np.random.randn(n, 2)

# Probabilidad real (función logística)
z = -1 + 2 * X[:, 0] - 1.5 * X[:, 1]
p_real = sigmoide(z)
y = np.random.binomial(1, p_real)

print(f"Proporción de clase 1: {np.mean(y):.2%}")
```

## Entrenamiento con Scikit-learn

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Coeficientes
print(f"Intercepto (β₀): {modelo.intercept_[0]:.3f}")
print(f"Coeficientes (β₁, β₂): {modelo.coef_[0].round(3)}")
# Intercepto (β₀): -1.124
# Coeficientes (β₁, β₂): [2.031 -1.573]
```

## Interpretación de Coeficientes (Odds Ratio)

A diferencia de la regresión lineal, los coeficientes no se interpretan directamente como cambios en Y. Se interpretan en términos de *odds ratios*:

```python
# Odds = p / (1 - p)
# Log(Odds) = β₀ + β₁X₁ + ... + βₚXₚ
# Un cambio de 1 unidad en X₁ multiplica los odds por e^(β₁)

coef = modelo.coef_[0]
print("Interpretación (Odds Ratios):")
for i, c in enumerate(coef):
    or_valor = np.exp(c)
    print(f"  X{i+1}: OR = {or_valor:.3f}")
    print(f"       Por cada unidad más en X{i+1}, los odds se multiplican por {or_valor:.3f}")
```

## Probabilidades vs Clases

```python
# Probabilidades predichas
probs = modelo.predict_proba(X_test)
print("Probabilidades (primeras 5):")
print(f"  P(Y=0): {probs[:5, 0].round(3)}")
print(f"  P(Y=1): {probs[:5, 1].round(3)}")

# Clases predichas (umbral por defecto: 0.5)
predicciones = modelo.predict(X_test)
print(f"\nClases predichas: {predicciones[:10]}")
print(f"Clases reales:    {y_test[:10]}")
```

## Métricas de Clasificación

Accuracy es engañosa cuando las clases están desbalanceadas:

```python
def reporte_clasificacion(y_real, y_pred, y_prob=None):
    """Reporte completo de clasificación binaria"""
    tn, fp, fn, tp = confusion_matrix(y_real, y_pred).ravel()

    accuracy = accuracy_score(y_real, y_pred)
    precision = precision_score(y_real, y_pred)
    recall = recall_score(y_real, y_pred)
    f1 = f1_score(y_real, y_pred)

    print("=== Métricas de Clasificación ===")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f} (de los que predije 1, qué proporción es 1)")
    print(f"Recall:    {recall:.4f} (de los que son 1, qué proporción detecté)")
    print(f"F1-Score:  {f1:.4f} (media armónica de precisión y recall)")
    print(f"\nMatriz de confusión:")
    print(f"  [[{tn:3d} {fp:3d}]")
    print(f"   [{fn:3d} {tp:3d}]]")

    if y_prob is not None:
        auc = roc_auc_score(y_real, y_prob[:, 1])
        print(f"\nAUC-ROC:   {auc:.4f}")

    return {
        'accuracy': accuracy, 'precision': precision,
        'recall': recall, 'f1': f1
    }

y_prob = modelo.predict_proba(X_test)
reporte_clasificacion(y_test, predicciones, y_prob)
```

## La Matriz de Confusión Explicada

| | Predicho 0 | Predicho 1 |
|---|-----------|-----------|
| **Real 0** | TN (Verdadero Negativo) | FP (Falso Positivo) |
| **Real 1** | FN (Falso Negativo) | TP (Verdadero Positivo) |

```python
tn, fp, fn, tp = confusion_matrix(y_test, predicciones).ravel()

# Tasas derivadas
tpr = tp / (tp + fn)  # Recall / Sensibilidad
tnr = tn / (tn + fp)  # Especificidad
fpr = fp / (fp + tn)  # Tasa de falsos positivos

print(f"Sensibilidad (TPR): {tpr:.3f} - capacidad de detectar positivos")
print(f"Especificidad (TNR): {tnr:.3f} - capacidad de identificar negativos")
print(f"Tasa Falsos Pos (FPR): {fpr:.3f}")
```

## Curva ROC y AUC

La curva ROC muestra el trade-off entre sensibilidad y falsos positivos para diferentes umbrales:

```python
# Calcular curva ROC
fpr, tpr, umbrales = roc_curve(y_test, y_prob[:, 1])
auc = roc_auc_score(y_test, y_prob[:, 1])

print(f"AUC: {auc:.4f}")
print()
print(f"Umbral\tFPR\tTPR (Sensibilidad)")
for i in range(0, len(umbrales), len(umbrales)//5):
    print(f"{umbrales[i]:.2f}\t{fpr[i]:.3f}\t{tpr[i]:.3f}")

# AUC interpretación
# 0.50 = aleatorio
# 0.70-0.80 = aceptable
# 0.80-0.90 = excelente
# 0.90-1.00 = sobresaliente
```

## Balanceo de Clases

Cuando una clase es mucho más frecuente que la otra, las métricas como accuracy son engañosas:

```python
# Dataset desbalanceado
np.random.seed(42)
n = 1000
X_desb = np.random.randn(n, 2)
y_desb = np.random.binomial(1, 0.05, n)  # Solo 5% son clase 1

print(f"Proporción clase 1: {np.mean(y_desb):.2%}")

# Modelo ingenuo (predecir siempre 0)
y_ingenuo = np.zeros(n)
print(f"Accuracy del modelo ingenuo: {accuracy_score(y_desb, y_ingenuo):.4f}")
# 95%! Pero no detecta ningún positivo

# Estrategias para balancear:
# - class_weight='balanced' en sklearn
# - Sobremuestreo (SMOTE)
# - Submuestreo
# - Ajustar umbral de decisión

modelo_balanceado = LogisticRegression(class_weight='balanced')
modelo_balanceado.fit(X_train, y_train)

# Comparar umbrales
print("\nEfecto de ajustar umbral:")
for umbral in [0.3, 0.5, 0.7]:
    pred_umbral = (y_prob[:, 1] >= umbral).astype(int)
    prec = precision_score(y_test, pred_umbral)
    rec = recall_score(y_test, pred_umbral)
    print(f"  Umbral={umbral:.1f}: Precision={prec:.3f}, Recall={rec:.3f}")
```

## Regularización: Ridge y Lasso para Logística

```python
# Lasso (L1): selecciona variables (pone coeficientes a 0)
lasso = LogisticRegression(penalty='l1', solver='liblinear', C=1.0)
lasso.fit(X_train, y_train)
print(f"Coeficientes Lasso: {lasso.coef_[0].round(3)}")

# Ridge (L2): encoge coeficientes (nunca a 0)
ridge = LogisticRegression(penalty='l2', C=1.0)
ridge.fit(X_train, y_train)
print(f"Coeficientes Ridge: {ridge.coef_[0].round(3)}")

# C controla la fuerza de regularización (menor C = más regularización)
for C in [0.01, 0.1, 1, 10]:
    modelo_reg = LogisticRegression(C=C, penalty='l2')
    modelo_reg.fit(X_train, y_train)
    score = modelo_reg.score(X_test, y_test)
    print(f"C={C:5.2f}: Accuracy = {score:.4f}, ||β||² = {np.sum(modelo_reg.coef_**2):.4f}")
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Usando el dataset `load_breast_cancer` de sklearn, entrena un modelo de regresión logística. Reporta accuracy, precisión, recall, F1 y AUC. ¿Cuál es la métrica más importante para diagnóstico médico?

2. **Ejercicio 2:** Genera un dataset desbalanceado (95% clase 0, 5% clase 1). Compara un modelo con `class_weight=None` vs `class_weight='balanced'`. ¿Cómo cambian precisión y recall?

3. **Ejercicio 3:** Implementa la función sigmoide y la función de costo (log-loss) desde cero. Verifica que tu implementación de sklearn produce los mismos coeficientes.

4. **Ejercicio 4:** Simula datos donde la frontera de decisión no sea lineal. Compara la regresión logística lineal con una versión con términos polinomiales. ¿Cuál funciona mejor?

## 📝 Resumen del Capítulo

- La **regresión logística** modela la probabilidad de pertenencia a una clase
- La **función sigmoide** transforma combinaciones lineales en probabilidades [0, 1]
- Los **odds ratios** (e^β) interpretan el cambio en odds por unidad de predictor
- **Accuracy** es engañosa con clases desbalanceadas
- **Precision, Recall, F1** son mejores métricas para clasificación
- La **curva ROC** y el **AUC** evalúan el rendimiento en todos los umbrales
- La **matriz de confusión** desglosa aciertos y errores por clase
- El **balanceo de clases** es crítico; usa `class_weight` o remuestreo
- La **regularización** (L1/L2) previene sobreajuste

**Conceptos clave aprendidos:** sigmoide, odds ratio, log-loss, accuracy, precisión, recall, F1, matriz de confusión, ROC, AUC, balanceo de clases, regularización
