# Capítulo 7: Aprendizaje No Supervisado

## 7.1 Clustering con K-Means

### 7.1.1 Segmentación de Clientes

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Preparar datos de clientes TechStore
clientes = pd.read_parquet("data/silver/clientes/")

features_segmentacion = [
    "frecuencia_compra", "ticket_promedio", "gasto_total",
    "antiguedad_dias", "categorias_compradas", "dias_ultima_compra"
]

X_seg = clientes[features_segmentacion].dropna()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_seg)

# Encontrar K óptimo (método del codo)
inercias = []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inercias.append(km.inertia_)

# Gráfico del codo
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), inercias, "bo-")
plt.xlabel("K")
plt.ylabel("Inercia")
plt.title("Método del Codo para K-Means")
plt.savefig("img/codo_kmeans.png")
```

### 7.1.2 Interpretación de Clusters

```python
# Aplicar K-Means con K=4 (óptimo)
k = 4
km = KMeans(n_clusters=k, random_state=42, n_init=10)
clientes["cluster"] = km.fit_predict(X_scaled)

# Perfil de cada cluster
perfil = clientes.groupby("cluster")[features_segmentacion].mean()
perfil["count"] = clientes.groupby("cluster").size()
perfil["porcentaje"] = (perfil["count"] / len(clientes) * 100).round(1)

print("=== Perfil de Clusters ===")
for cluster in range(k):
    print(f"\nCluster {cluster} ({perfil.loc[cluster, 'porcentaje']:.1f}%)")
    for feat in features_segmentacion:
        val = perfil.loc[cluster, feat]
        print(f"  {feat}: {val:.2f}")

# Visualización 2D con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clientes["cluster"],
                      cmap="viridis", alpha=0.6)
plt.colorbar(scatter)
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.1%})")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.1%})")
plt.title("Segmentación de Clientes TechStore")
plt.savefig("img/segmentacion_clientes.png")

# Nombres de segmentos
segmentos = {
    0: "Premium Fieles - Alto gasto, alta frecuencia",
    1: "Compradores Ocasionales - Gasto medio, baja frecuencia",
    2: "Nuevos - Poca antigüedad, compras recientes",
    3: "En Riesgo - Alta antigüedad, sin compras recientes"
}
```

## 7.2 Sistemas de Recomendación

### 7.2.1 Filtrado Colaborativo

```python
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Matriz usuario-producto
matriz_compras = df.groupby(["customer_id", "product_id"])["amount"].sum().unstack(fill_value=0)
matriz_sparse = csr_matrix(matriz_compras.values)

# Similaridad entre usuarios
sim_usuarios = cosine_similarity(matriz_sparse)

# Sistema de recomendación simple
def recomendar_para_usuario(user_id, n_recomendaciones=5):
    idx = list(matriz_compras.index).index(user_id)
    similar_users = sim_usuarios[idx].argsort()[-6:-1][::-1]

    productos_comprados = set(matriz_compras.columns[matriz_compras.iloc[idx] > 0])
    recomendaciones = {}

    for sim_idx in similar_users:
        productos_vecino = matriz_compras.columns[matriz_compras.iloc[sim_idx] > 0]
        nuevos = set(productos_vecino) - productos_comprados
        for prod in nuevos:
            recomendaciones[prod] = recomendaciones.get(prod, 0) + sim_usuarios[idx][sim_idx]

    return sorted(recomendaciones.items(), key=lambda x: x[1], reverse=True)[:n_recomendaciones]

# Ejemplo
user_ejemplo = 42
recomendaciones = recomendar_para_usuario(user_ejemplo)
print(f"Recomendaciones para usuario {user_ejemplo}:")
for prod, score in recomendaciones:
    print(f"  → Producto {prod}: score {score:.3f}")
```

### 7.2.2 Filtrado Basado en Contenido

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Productos con descripciones
productos["descripcion_completa"] = (
    productos["product_name"] + " " +
    productos["category"] + " " +
    productos["description"] + " " +
    productos["keywords"]
)

# TF-IDF sobre descripciones
tfidf = TfidfVectorizer(max_features=1000, stop_words="spanish")
matriz_tfidf = tfidf.fit_transform(productos["descripcion_completa"])

# Similaridad entre productos
sim_productos = cosine_similarity(matriz_tfidf)

def recomendar_similares(producto_id, n=5):
    idx = productos[productos["product_id"] == producto_id].index[0]
    scores = list(enumerate(sim_productos[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]

    print(f"Producto: {productos.iloc[idx]['product_name']}")
    print("Productos similares:")
    for i, score in scores:
        p = productos.iloc[i]
        print(f"  → {p['product_name']} ({p['category']}) - {score:.2%} similitud")

recomendar_similares(1234)
```

## 7.3 Reducción de Dimensionalidad

```python
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# PCA para reducir dimensionalidad
pca = PCA(n_components=0.95)  # mantener 95% de varianza
X_pca = pca.fit_transform(X_scaled)

print(f"Dimensiones originales: {X_scaled.shape[1]}")
print(f"Dimensiones PCA (95% varianza): {X_pca.shape[1]}")
print(f"Varianza explicada por componente:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.1%}")

# t-SNE para visualización
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clientes["cluster"], cmap="viridis", alpha=0.6)
plt.title("PCA")

plt.subplot(1, 2, 2)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=clientes["cluster"], cmap="viridis", alpha=0.6)
plt.title("t-SNE")

plt.savefig("img/pca_vs_tsne.png")
```

## 7.4 Ejercicios

1. **Segmentación**: Aplica K-Means con K=3, 4, 5 a los clientes TechStore. ¿Cuál segmentación es más interpretable?
2. **Recomendación**: Implementa un sistema híbrido que combine filtrado colaborativo y basado en contenido.
3. **PCA**: Reduce las features de transacciones TechStore a 2 componentes y visualiza. ¿Se pierde mucha información?
4. **t-SNE**: Compara t-SNE con PCA para visualizar los clusters de clientes. ¿Cuál es mejor?
5. **DBSCAN**: Aplica DBSCAN a los datos de clientes y compara los clusters con K-Means. ¿Qué diferencias encuentras?
