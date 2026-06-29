## Módulo 7: Casos de Uso Reales

# Flujo de Trabajo de un Proyecto Cuantitativo

Este capítulo unifica todo lo aprendido en un flujo de trabajo completo y reproducible. Seguirás un caso real de principio a fin: desde la pregunta de negocio hasta la presentación de resultados.

## El Pipeline Completo

```python
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
```

### Fase 1: Definición del Problema

> **Pregunta de negocio:** ¿Podemos predecir qué clientes dejarán nuestro servicio (churn) en los próximos 30 días, basándonos en su comportamiento histórico?

```python
# Criterios de éxito: AUC > 0.75 en datos de prueba
# Restricciones: el modelo debe ser interpretable (regresión logística)
# Acción: enviar un descuento personalizado a clientes con >60% de riesgo
```

### Fase 2: Obtención y Exploración de Datos

```python
np.random.seed(42)
n = 5000

# Simular datos de clientes
df = pd.DataFrame({
    'cliente_id': range(1, n + 1),
    'antiguedad_meses': np.random.exponential(24, n).clip(1, 120).astype(int),
    'num_llamadas_soporte': np.random.poisson(2, n),
    'monto_mensual': np.random.lognormal(4.5, 0.5, n),
    'contrato_mensual': np.random.binomial(1, 0.4, n),  # 1 = mensual, 0 = anual
    'pago_electronico': np.random.binomial(1, 0.6, n),
    'quejas_30_dias': np.random.poisson(0.5, n),
    'uso_servicio': np.random.uniform(0, 100, n),  # % de uso del servicio contratado
})

# Generar churn basado en un modelo subyacente
z = (-2
     - 0.02 * df['antiguedad_meses']
     + 0.3 * df['num_llamadas_soporte']
     - 0.01 * df['monto_mensual']
     + 0.8 * df['contrato_mensual']
     - 0.5 * df['pago_electronico']
     + 0.7 * df['quejas_30_dias']
     - 0.03 * df['uso_servicio']
     + np.random.normal(0, 1, n))

p_churn = 1 / (1 + np.exp(-z))
df['churn'] = np.random.binomial(1, p_churn)

print(f"Tasa de churn: {df['churn'].mean():.2%}")
print(f"\nPrimeras filas:")
print(df.head())
```

### Fase 3: Análisis Exploratorio (EDA)

```python
def exploratory_analysis(df, target='churn'):
    """Análisis exploratorio completo"""
    print("=== 1. Estructura del Dataset ===")
    print(f"  Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    print(f"  Valores faltantes: {df.isna().sum().sum()}")
    print(f"  Tipos de datos:\n{df.dtypes.value_counts()}")

    print("\n=== 2. Estadísticas Descriptivas ===")
    print(df.describe().round(2))

    print("\n=== 3. Análisis Univariante (por variable vs target) ===")
    for col in df.select_dtypes(include=[np.number]).columns:
        if col != target and col != 'cliente_id':
            churn_1 = df[df[target] == 1][col]
            churn_0 = df[df[target] == 0][col]
            stat, p = stats.ttest_ind(churn_0, churn_1, equal_var=False)
            print(f"  {col:25s}: media(churn=0)={churn_0.mean():.2f}, media(churn=1)={churn_1.mean():.2f}, p={p:.4f}")

exploratory_analysis(df)
```

### Fase 4: Preprocesamiento

```python
# Separar predictores y target
features = ['antiguedad_meses', 'num_llamadas_soporte', 'monto_mensual',
            'contrato_mensual', 'pago_electronico', 'quejas_30_dias', 'uso_servicio']
X = df[features]
y = df['churn']

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"Train: {X_train.shape[0]} muestras ({y_train.mean():.2%} churn)")
print(f"Test:  {X_test.shape[0]} muestras ({y_test.mean():.2%} churn)")

# Estandarizar variables numéricas
num_features = ['antiguedad_meses', 'num_llamadas_soporte',
                'monto_mensual', 'quejas_30_dias', 'uso_servicio']
scaler = StandardScaler()
X_train[num_features] = scaler.fit_transform(X_train[num_features])
X_test[num_features] = scaler.transform(X_test[num_features])
```

### Fase 5: Modelado

```python
# Modelo base: regresión logística
modelo = LogisticRegression(class_weight='balanced', random_state=42)
modelo.fit(X_train, y_train)

# Evaluación
y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

print("=== Evaluación del Modelo ===")
print(classification_report(y_test, y_pred))
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob):.4f}")

# Interpretación de coeficientes
coef_df = pd.DataFrame({
    'feature': features,
    'coef': modelo.coef_[0],
    'odds_ratio': np.exp(modelo.coef_[0])
}).sort_values('odds_ratio', ascending=False)

print("\n=== Importancia de Variables (Odds Ratios) ===")
print(coef_df.round(3))
```

### Fase 6: Validación Cruzada

```python
scores = cross_val_score(modelo, X_train, y_train, cv=5, scoring='roc_auc')
print(f"Validación Cruzada (5 folds):")
print(f"  AUC promedio: {scores.mean():.4f} ± {scores.std():.4f}")
```

### Fase 7: Optimización de Umbral

```python
# Encontrar el umbral óptimo para maximizar F1
from sklearn.metrics import f1_score

umbrales = np.linspace(0.1, 0.9, 50)
f1_scores = []

for umbral in umbrales:
    pred_umbral = (y_prob >= umbral).astype(int)
    f1_scores.append(f1_score(y_test, pred_umbral))

umbral_optimo = umbrales[np.argmax(f1_scores)]
print(f"Umbral óptimo (máximo F1): {umbral_optimo:.2f}")
print(f"F1 en umbral óptimo: {max(f1_scores):.4f}")

# Decisión de negocio: enviar descuento si riesgo > 60%
umbral_negocio = 0.60
clientes_riesgo = X_test[y_prob >= umbral_negocio]
print(f"\nClientes con >60% de riesgo: {len(clientes_riesgo)} ({len(clientes_riesgo)/len(X_test):.1%})")
```

### Fase 8: Documentación y Comunicación

```python
def resumen_ejecutivo(modelo, metricas, umbral_negocio, df_test, y_prob):
    """Genera un resumen ejecutivo del proyecto"""
    print("=" * 60)
    print("RESUMEN EJECUTIVO: Modelo de Predicción de Churn")
    print("=" * 60)
    print(f"\nObjetivo: Identificar clientes con alto riesgo de abandono")

    print(f"\nRendimiento del modelo:")
    print(f"  AUC-ROC: {metricas['auc']:.3f}")
    print(f"  Precision: {metricas['precision']:.3f}")
    print(f"  Recall: {metricas['recall']:.3f}")

    print(f"\nImpacto en negocio:")
    n_clientes_riesgo = int((y_prob >= umbral_negocio).sum())
    print(f"  Clientes identificados como alto riesgo: {n_clientes_riesgo}")
    print(f"  Tasa de retención esperada (estimación): +15-25%")

    print(f"\nVariables más influyentes:")
    for _, row in coef_df.head(3).iterrows():
        print(f"  {row['feature']}: OR = {row['odds_ratio']:.2f}")

    print(f"\nRecomendación:")
    print(f"  Implementar campaña de retención dirigida a los {n_clientes_riesgo} clientes identificados.")
    print(f"  Costo estimado: ${n_clientes_riesgo * 5:.0f} (descuento de $5 por cliente)")
    print(f"  ROI estimado: 3.5x (basado en LTV promedio de $500)")

metricas = {
    'auc': roc_auc_score(y_test, y_prob),
    'precision': __import__('sklearn').metrics.precision_score(y_test, y_pred),
    'recall': __import__('sklearn').metrics.recall_score(y_test, y_pred)
}

resumen_ejecutivo(modelo, metricas, 0.60, X_test, y_prob)
```

## Checklist de un Proyecto Cuantitativo

| Fase | Actividades clave | Entregable |
|------|-------------------|------------|
| 1. Definición | Pregunta, criterios de éxito, restricciones | Documento de alcance |
| 2. Datos | Fuentes, calidad, integración | Dataset limpio |
| 3. EDA | Estadísticas, visualizaciones, hipótesis | Reporte exploratorio |
| 4. Preprocesamiento | Limpieza, transformaciones, división | Datos listos para modelar |
| 5. Modelado | Selección, entrenamiento, tuning | Modelo entrenado |
| 6. Validación | CV, métricas, interpretación | Evaluación del modelo |
| 7. Despliegue | Implementación, monitoreo | API/Informe |
| 8. Comunicación | Visualización, storytelling, acción | Resumen ejecutivo |

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Aplica este flujo de trabajo completo a un dataset de tu elección (puede ser de Kaggle, UCI o sklearn). Documenta cada fase.

2. **Ejercicio 2:** Modifica el flujo para incluir un segundo modelo (Random Forest) y compáralo con la regresión logística. ¿Cuál prefieres? ¿Por qué?

3. **Ejercicio 3:** Crea un dashboard en matplotlib/seaborn que muestre las métricas clave del proyecto: distribución del target, matriz de correlación, importancia de variables y curva ROC.

4. **Ejercicio 4:** Escribe un resumen ejecutivo de una página (en markdown) explicando los resultados a un director de marketing. No uses jerga técnica.

## 📝 Resumen del Capítulo

- Un proyecto cuantitativo sigue un **flujo estructurado** de 8 fases
- La **definición del problema** guía todas las decisiones posteriores
- El **EDA** revela patrones, anomalías y relaciones
- El **preprocesamiento** incluye escalado, división y manejo de faltantes
- El **modelado** combina selección, entrenamiento y validación
- La **optimización de umbral** alinea la estadística con el negocio
- La **comunicación** debe traducir hallazgos técnicos en acciones de negocio
- Documenta cada paso para garantizar **reproducibilidad**

**Conceptos clave aprendidos:** pipeline, EDA, preprocesamiento, modelado, validación, umbral de decisión, ROI, resumen ejecutivo, reproducibilidad
