"""Capítulo 5: Métricas de regresión y clasificación"""

from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
import numpy as np

# ─── Métricas de regresión ───
# Simular predicciones para el ejemplo
y_test = np.array([100, 200, 150, 300, 250])
y_pred = np.array([110, 190, 145, 310, 240])

metricas_regresion = {
    "MSE": mean_squared_error(y_test, y_pred),
    "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
    "MAE": mean_absolute_error(y_test, y_pred),
    "R2": r2_score(y_test, y_pred),
    "MAPE": np.mean(np.abs((y_test - y_pred) / y_test)) * 100
}

print("📊 Métricas de regresión:")
for k, v in metricas_regresion.items():
    print(f"  {k}: {v:.2f}")

# ─── Métricas de clasificación ───
y_true_clf = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred_clf = np.array([1, 0, 1, 0, 0, 1, 0, 1, 1, 0])

print("\n📊 Métricas de clasificación:")
print(f"  Accuracy: {accuracy_score(y_true_clf, y_pred_clf):.2f}")
print(f"  Precision: {precision_score(y_true_clf, y_pred_clf):.2f}")
print(f"  Recall: {recall_score(y_true_clf, y_pred_clf):.2f}")
print(f"  F1: {f1_score(y_true_clf, y_pred_clf):.2f}")
print(f"\nMatriz de confusión:\n{confusion_matrix(y_true_clf, y_pred_clf)}")
