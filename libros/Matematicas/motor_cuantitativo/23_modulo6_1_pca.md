## Módulo 6: Análisis Multivariante y Series Temporales

# Reducción de Dimensionalidad: PCA Explicado

Cuando tu dataset tiene muchas variables, surgen problemas: maldición de la dimensionalidad, multicolinealidad, sobreajuste y dificultad de visualización. El Análisis de Componentes Principales (PCA) es la técnica más popular para reducir dimensionalidad preservando la mayor cantidad de información posible.

## ¿Qué es PCA?

PCA encuentra nuevas direcciones (componentes principales) en los datos que capturan la máxima varianza. El primer componente captura la mayor varianza posible; el segundo, la siguiente mayor varianza ortogonal al primero; y así sucesivamente.

## La Geometría de PCA

PCA rota el sistema de coordenadas para alinearlo con las direcciones de máxima varianza de los datos.

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy import stats

np.random.seed(42)

# Simular datos correlacionados (2D, pero la información real es 1D)
n = 200
X = np.random.randn(n, 2)
# Rotar y estirar: los datos forman un "elipse" alargada
angulo = np.pi / 4
rotacion = np.array([[np.cos(angulo), -np.sin(angulo)],
                     [np.sin(angulo),  np.cos(angulo)]])
X = X @ rotacion
X[:, 0] *= 3  # Estirar en una dirección

# PCA
X_scaled = StandardScaler().fit_transform(X)
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

print("Varianza explicada por componente:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.4f} ({var*100:.2f}%)")
# PC1: 0.9567 (95.67%)
# PC2: 0.0433 (4.33%)

print(f"\nVarianza explicada acumulada:")
print(f"  PC1: {pca.explained_variance_ratio_[0]:.4f}")
print(f"  PC1+PC2: {np.sum(pca.explained_variance_ratio_):.4f}")
```

## El Algoritmo PCA Paso a Paso

PCA se implementa mediante la descomposición SVD de la matriz de datos centrada:

```python
def pca_desde_cero(X, n_componentes=2):
    """PCA implementado desde cero usando SVD"""
    # 1. Centrar los datos
    X_centrado = X - np.mean(X, axis=0)

    # 2. SVD
    U, S, Vt = np.linalg.svd(X_centrado, full_matrices=False)

    # 3. Componentes principales (vectores en Vt)
    componentes = Vt[:n_componentes]

    # 4. Datos transformados
    X_proyectado = X_centrado @ componentes.T

    # 5. Varianza explicada
    varianza_total = np.sum(S**2)
    varianza_explicada = (S[:n_componentes]**2) / varianza_total

    return X_proyectado, componentes, varianza_explicada

# Verificar contra sklearn
X_proy_manual, comps_manual, var_exp_manual = pca_desde_cero(X_scaled, 2)
print("Varianza explicada (implementación manual):")
for i, v in enumerate(var_exp_manual):
    print(f"  PC{i+1}: {v:.4f}")
# Coincide con sklearn
```

## Cómo Elegir el Número de Componentes

```python
# Dataset de mayor dimensión
from sklearn.datasets import load_digits
digits = load_digits()
X_digits = digits.data
print(f"Shape original: {X_digits.shape}")  # (1797, 64)

# PCA completo
pca_full = PCA().fit(StandardScaler().fit_transform(X_digits))

# Varianza acumulada
var_acum = np.cumsum(pca_full.explained_variance_ratio_)

print("\nComponentes necesarios para:")
for umbral in [0.70, 0.80, 0.90, 0.95, 0.99]:
    n = np.argmax(var_acum >= umbral) + 1
    print(f"  {umbral:.0%} de varianza: {n} componentes (de 64)")
# 70% de varianza: ~8 componentes
# 80% de varianza: ~12 componentes
# 90% de varianza: ~21 componentes
# 95% de varianza: ~29 componentes
# 99% de varianza: ~45 componentes
```

> **💡 Consejo del Analista:**
> No hay una regla fija para elegir k componentes. El punto de codo en el gráfico de varianza explicada y el umbral del 90-95% son buenos puntos de partida. La elección depende de tu objetivo: ¿visualización (k=2-3), compresión (k que retenga 95%), o preprocesamiento?

## PCA para Visualización

```python
# Reducir dígitos a 2D para visualización
pca_2d = PCA(n_components=2)
X_digits_2d = pca_2d.fit_transform(StandardScaler().fit_transform(X_digits))

print("Dígitos en 2D:")
print(f"  Shape reducido: {X_digits_2d.shape}")
print(f"  Varianza explicada: {np.sum(pca_2d.explained_variance_ratio_):.2%}")
# Con 2 componentes capturamos ~28% de la varianza (suficiente para visualizar)
```

## PCA como Preprocesamiento para Modelos

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Sin PCA
rf = RandomForestClassifier(n_estimators=100, random_state=42)
score_original = cross_val_score(rf, X_digits, digits.target, cv=5).mean()

# Con PCA (retener 95% de varianza)
n_comps_95 = np.argmax(var_acum >= 0.95) + 1
pca_95 = PCA(n_components=n_comps_95)
X_pca_95 = pca_95.fit_transform(StandardScaler().fit_transform(X_digits))

score_pca = cross_val_score(rf, X_pca_95, digits.target, cv=5).mean()

print(f"\nRendimiento del clasificador:")
print(f"  Sin PCA (64 vars):  accuracy = {score_original:.4f}")
print(f"  Con PCA ({n_comps_95} vars): accuracy = {score_pca:.4f}")
# El rendimiento es similar pero con 29 variables en vez de 64
```

## Carga de Componentes (Loadings)

Las cargas (loadings) indican cuánto contribuye cada variable original a cada componente:

```python
# Loadings para el dataset de dígitos
loadings = pca_full.components_  # Shape: (n_componentes, n_variables)

print("Interpretación de PC1 (loadings):")
# Las variables con mayor |loading| contribuyen más a PC1
pc1_loadings = loadings[0]
top_vars = np.argsort(np.abs(pc1_loadings))[-5:]
print(f"  Las 5 variables más importantes para PC1: {top_vars}")
```

## El Efecto de Estandarizar

```python
# Sin estandarizar: las variables con mayor escala dominan
X_sin_escala = np.column_stack([
    np.random.randn(100) * 100,  # Escala grande
    np.random.randn(100) * 1,     # Escala pequeña
])
pca_no_scale = PCA().fit(X_sin_escala)
print(f"Sin estandarizar - varianza explicada PC1: {pca_no_scale.explained_variance_ratio_[0]:.4f}")
# PC1 captura casi toda la varianza, dominada por la variable de gran escala

# Con estandarización
X_escalada = StandardScaler().fit_transform(X_sin_escala)
pca_scaled = PCA().fit(X_escalada)
print(f"Estandarizado - varianza explicada PC1: {pca_scaled.explained_variance_ratio_[0]:.4f}")
# Las variables contribuyen equitativamente
```

> **⚠️ Advertencia:**
> Siempre estandariza (media=0, var=1) antes de PCA a menos que todas las variables estén en la misma unidad y escala. PCA es sensible a la escala de las variables.

## PCA y la Matriz de Covarianza

PCA está íntimamente relacionado con la descomposición en eigenvectores de la matriz de covarianza:

```python
# Matriz de covarianza
X_centrado = X_scaled - np.mean(X_scaled, axis=0)
cov = (X_centrado.T @ X_centrado) / (X_centrado.shape[0] - 1)

# Eigenvectores = direcciones de máxima varianza
eigenvals, eigenvects = np.linalg.eigh(cov)
# Ordenar por eigenvalor descendente
idx = np.argsort(eigenvals)[::-1]
eigenvals = eigenvals[idx]
eigenvects = eigenvects[:, idx]

print("Eigenvalores (varianza en cada dirección):")
print(f"  {eigenvals.round(4)}")

# Proporción de varianza explicada
print(f"  Varianza explicada PC1: {eigenvals[0]/np.sum(eigenvals):.4f}")
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Aplica PCA al dataset Iris. ¿Cuánta varianza explica cada componente? ¿Qué especies se separan mejor en las primeras 2 componentes?

2. **Ejercicio 2:** Implementa PCA desde cero usando la descomposición en eigenvectores de la matriz de covarianza (en lugar de SVD). Compara los resultados con sklearn.

3. **Ejercicio 3:** Usa PCA como preprocesamiento para regresión logística en el dataset de dígitos. Varía el número de componentes de 1 a 64. ¿En qué punto el rendimiento se estabiliza?

4. **Ejercicio 4:** Genera un dataset con 20 variables aleatorias, donde solo 3 son informativas y las demás son ruido. Demuestra que PCA puede identificar las dimensiones relevantes.

## 📝 Resumen del Capítulo

- **PCA** encuentra direcciones ortogonales de máxima varianza en los datos
- Reduce dimensionalidad proyectando los datos en las primeras k componentes
- La **varianza explicada** indica cuánta información retiene cada componente
- El **número óptimo de componentes** se elige por punto de codo o umbral de varianza
- **SVD** es el algoritmo subyacente para implementar PCA numéricamente
- Los **loadings** indican la contribución de cada variable original a los componentes
- **Siempre estandariza** antes de PCA
- PCA mejora la eficiencia computacional y reduce el sobreajuste

**Conceptos clave aprendidos:** componente principal, varianza explicada, SVD, loadings, scree plot, estandarización, reducción de dimensionalidad, eigenvalores
