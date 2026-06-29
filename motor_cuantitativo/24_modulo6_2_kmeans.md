# Análisis de Conglomerados (K-Means)

El clustering (agrupamiento) es una técnica de aprendizaje no supervisado que encuentra grupos naturales en los datos sin etiquetas previas. K-Means es el algoritmo de clustering más conocido y utilizado.

## ¿Qué es K-Means?

K-Means particiona n observaciones en k grupos, donde cada observación pertenece al grupo con la media (centroide) más cercana.

### El Algoritmo

1. Seleccionar k centroides iniciales (aleatorios)
2. Asignar cada punto al centroide más cercano
3. Recalcular centroides como la media de los puntos asignados
4. Repetir pasos 2-3 hasta convergencia

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs
from scipy.spatial.distance import cdist

np.random.seed(42)

# Generar datos agrupados
X, y_real = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.5,
    random_state=42
)

print(f"Shape: {X.shape}")
print(f"Centros reales: 4 grupos")
```

### Implementación desde Cero

```python
def kmeans_desde_cero(X, k, max_iter=100, tol=1e-4):
    """K-Means implementado desde cero"""
    n, m = X.shape

    # 1. Inicializar centroides (elegir k puntos aleatorios)
    idx = np.random.choice(n, k, replace=False)
    centroides = X[idx]

    for iteracion in range(max_iter):
        # 2. Asignar cada punto al centroide más cercano
        distancias = cdist(X, centroides, metric='euclidean')
        etiquetas = np.argmin(distancias, axis=1)

        # 3. Recalcular centroides
        nuevos_centroides = np.array([
            X[etiquetas == i].mean(axis=0) for i in range(k)
        ])

        # 4. Verificar convergencia
        cambio = np.linalg.norm(nuevos_centroides - centroides)
        centroides = nuevos_centroides

        if cambio < tol:
            print(f"Convergió en {iteracion + 1} iteraciones")
            break

    return etiquetas, centroides

etiquetas_manual, centroides_manual = kmeans_desde_cero(X, k=4)
```

### Con Scikit-learn

```python
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
kmeans.fit(X)

etiquetas = kmeans.labels_
centroides = kmeans.cluster_centers_

print(f"Inercia (suma de distancias al cuadrado): {kmeans.inertia_:.2f}")
print(f"Número de iteraciones: {kmeans.n_iter_}")

# Comparar con implementación manual
print(f"¿Coinciden las etiquetas? {np.array_equal(etiquetas, etiquetas_manual)}")
# Pueden diferir por la inicialización aleatoria
```

## Cómo Elegir k: El Método del Codo

No hay una respuesta única para k. El método del codo busca el punto donde agregar más clusters deja de dar mejoras significativas:

```python
def metodo_codo(X, k_max=10):
    """Calcula inercia para diferentes valores de k"""
    inercias = []
    for k in range(1, k_max + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
        kmeans.fit(X)
        inercias.append(kmeans.inertia_)

    # Tasa de mejora
    mejoras = []
    for i in range(1, len(inercias)):
        mejora = (inercias[i-1] - inercias[i]) / inercias[i-1]
        mejoras.append(mejora)

    print("k\tInercia\t\tMejora")
    for i, (inercia, mejora) in enumerate(zip(inercias, [0] + mejoras)):
        print(f"{i+1}\t{inercia:.2f}\t{mejora:.4f}" if i > 0 else f"{i+1}\t{inercia:.2f}\t-")

metodo_codo(X, k_max=8)
# k=1: 2500.00  -
# k=2: 1200.00  0.5200
# k=3: 700.00   0.4167
# k=4: 350.00   0.5000  ← codo
# k=5: 320.00   0.0857  ← mejora mucho menor
# k=6: 300.00   0.0625
```

## Coeficiente de Silueta

Una métrica formal para evaluar la calidad del clustering:

```python
for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    etiquetas_k = kmeans.fit_predict(X)
    silueta = silhouette_score(X, etiquetas_k)
    print(f"k={k}: Silueta = {silueta:.4f}")
# k=2: Silueta = 0.5812
# k=3: Silueta = 0.6421
# k=4: Silueta = 0.6810  ← mejor
# k=5: Silueta = 0.5304
# k=6: Silueta = 0.4893
```

> **💡 Consejo del Analista:**
> El coeficiente de silueta varía de -1 a 1. >0.5 indica buena separación entre clusters. Combínalo con el método del codo para elegir k.

## Limitaciones de K-Means

### 1. Sensible a la Inicialización

```python
# Diferentes inicializaciones pueden dar diferentes resultados
resultados = []
for semilla in range(10):
    kmeans = KMeans(n_clusters=4, random_state=semilla, n_init=1)
    kmeans.fit(X)
    resultados.append(kmeans.inertia_)

print(f"Inercias para 10 inicializaciones:")
print(f"  Min: {min(resultados):.2f}")
print(f"  Max: {max(resultados):.2f}")
print(f"  Diferencia: {max(resultados) - min(resultados):.2f}")
```

### 2. Asume Clusters Esféricos

```python
# K-Means falla con formas no esféricas
from sklearn.datasets import make_moons

X_moons, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
kmeans_moons = KMeans(n_clusters=2, random_state=42, n_init='auto')
etiquetas_moons = kmeans_moons.fit_predict(X_moons)
silueta_moons = silhouette_score(X_moons, etiquetas_moons)

print(f"Silueta para datos de luna (K-Means): {silueta_moons:.4f}")
# K-Means no captura bien formas no convexas
```

### 3. Sensible a Outliers

```python
# Añadir un outlier
X_con_outlier = np.vstack([X, [20, 20]])
kmeans_outlier = KMeans(n_clusters=4, random_state=42, n_init='auto')
etiquetas_outlier = kmeans_outlier.fit_predict(X_con_outlier)

# El outlier distorsiona los centroides
print(f"Centroides sin outlier:\n{np.round(centroides, 2)}")
print(f"Centroides con outlier:\n{np.round(kmeans_outlier.cluster_centers_, 2)}")
```

## Alternativas a K-Means

| Algoritmo | Ventajas | Desventajas |
|-----------|----------|-------------|
| **K-Means** | Rápido, escalable | Clusters esféricos, sensible a inicialización |
| **DBSCAN** | Detecta outliers, formas arbitrarias | Sensible a parámetros ε y minPts |
| **Hierarchical (Agglomerative)** | Dendrograma, no requiere k | Lento para grandes datos |
| **Gaussian Mixture** | Clusters con forma de elipse, probabilístico | Más parámetros |

```python
from sklearn.cluster import DBSCAN

# DBSCAN para formas no convexas
dbscan = DBSCAN(eps=0.2, min_samples=5)
etiquetas_dbscan = dbscan.fit_predict(X_moons)
n_clusters_dbscan = len(set(etiquetas_dbscan)) - (1 if -1 in etiquetas_dbscan else 0)

print(f"DBSCAN en datos de luna:")
print(f"  Clusters encontrados: {n_clusters_dbscan}")
print(f"  Puntos de ruido: {np.sum(etiquetas_dbscan == -1)}")
```

## Aplicación: Segmentación de Clientes

```python
# Simular datos de clientes
np.random.seed(42)
n_clientes = 500

clientes = np.column_stack([
    np.random.normal(5, 2, n_clientes),       # Frecuencia de compra
    np.random.normal(100, 40, n_clientes),     # Gasto promedio
    np.random.exponential(3, n_clientes),      # Antigüedad (años)
])

from sklearn.preprocessing import StandardScaler
clientes_scaled = StandardScaler().fit_transform(clientes)

# Encontrar segmentos
kmeans_clientes = KMeans(n_clusters=3, random_state=42, n_init='auto')
segmentos = kmeans_clientes.fit_predict(clientes_scaled)

# Caracterizar segmentos (en escala original)
for i in range(3):
    mascara = segmentos == i
    print(f"\nSegmento {i+1} (n={mascara.sum()}):")
    print(f"  Frecuencia: {np.mean(clientes[mascara, 0]):.1f}")
    print(f"  Gasto: ${np.mean(clientes[mascara, 1]):.1f}")
    print(f"  Antigüedad: {np.mean(clientes[mascara, 2]):.1f} años")
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Genera datos con 3 clusters de diferentes densidades. Aplica K-Means con k=3. ¿El algoritmo encuentra los clusters correctamente? ¿Qué pasa si las densidades son muy diferentes?

2. **Ejercicio 2:** Usando el método del codo y el coeficiente de silueta, determina el k óptimo para el dataset Iris (solo las características, sin las etiquetas). ¿Coincide con el número de especies?

3. **Ejercicio 3:** Compara K-Means con DBSCAN en el dataset `make_circles` de sklearn (círculos concéntricos). ¿Cuál algoritmo captura mejor la estructura?

4. **Ejercicio 4:** Implementa una función que calcule el centroide más cercano para un nuevo punto después de entrenar K-Means. Úsala para clasificar 5 nuevos clientes en los segmentos existentes.

## 📝 Resumen del Capítulo

- **K-Means** agrupa datos en k clusters basados en distancia al centroide
- El **método del codo** y el **coeficiente de silueta** guían la elección de k
- K-Means asume clusters **esféricos** y de **tamaño similar**
- Es **sensible a la inicialización** (usa k-means++ o n_init)
- Los **outliers** distorsionan los centroides
- **DBSCAN** y **clustering jerárquico** son alternativas para formas complejas
- El **escalado** de variables es crítico (la distancia se ve afectada por la escala)
- La **segmentación de clientes** es una aplicación clásica

**Conceptos clave aprendidos:** clustering, centroide, inercia, método del codo, silueta, K-Means++, DBSCAN, segmentación, aprendizaje no supervisado
