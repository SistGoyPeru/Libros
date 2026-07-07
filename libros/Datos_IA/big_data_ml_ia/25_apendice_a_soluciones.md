# Apéndice A: Soluciones a los Ejercicios

## Capítulo 1

### Ejercicio 1: Las 5 V del Big Data

**Volumen:** TechStore genera 10 millones de transacciones y 50 millones de eventos de navegación, demasiados para una sola máquina.

**Velocidad:** Los eventos de navegación llegan en tiempo real, requiriendo procesamiento streaming.

**Variedad:** Los datos incluyen transacciones estructuradas (CSV/Parquet), reseñas de texto no estructurado, eventos JSON semi-estructurados.

**Veracidad:** Reseñas con spam, datos incompletos, transacciones duplicadas requieren limpieza.

**Valor:** Predecir CLV, segmentar clientes, recomendar productos, analizar sentimiento.

### Ejercicio 4: Generar eventos de navegación

```python
eventos = spark.range(1_000_000) \
    .withColumn("user_id", (rand() * 100000).cast("int")) \
    .withColumn("page", when(rand() < 0.3, "home")
                .when(rand() < 0.6, "product")
                .when(rand() < 0.8, "cart")
                .otherwise("checkout")) \
    .withColumn("timestamp", expr("current_timestamp() - interval rand() * 30 days")) \
    .withColumn("duration_ms", (rand() * 30000 + 1000).cast("int"))
```

## Capítulo 5

### Ejercicio 1: Pipeline completo

```python
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression

modelos = [
    ("Linear Regression", LinearRegression()),
    ("Random Forest", RandomForestRegressor(n_estimators=100)),
    ("Gradient Boosting", GradientBoostingRegressor(n_estimators=100))
]

for nombre, modelo in modelos:
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", modelo)
    ])
    scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="r2")
    print(f"{nombre}: R2 CV = {scores.mean():.3f} ± {scores.std():.3f}")
```

## Capítulo 9

### Ejercicio 2: Regularización

La mejor combinación suele ser **L2 + Dropout**. L2 (weight decay) penaliza pesos grandes, Dropout apaga neuronas aleatoriamente durante training. Juntos previenen overfitting mejor que cada uno por separado.

```python
modelo_optimo = keras.Sequential([
    layers.Dense(128, activation="relu", kernel_regularizer=regularizers.l2(0.001)),
    layers.Dropout(0.3),
    layers.Dense(64, activation="relu", kernel_regularizer=regularizers.l2(0.001)),
    layers.Dropout(0.2),
    layers.Dense(1)
])
```

## Capítulo 13

### Ejercicio 2: Sistema RAG completo

```python
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

# Cargar documentación
loader = DirectoryLoader("docs/techstore/", glob="**/*.md", loader_cls=TextLoader)
docs = loader.load()

# Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embeddings y vector store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)

# QA Chain
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4", temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever(k=5),
    return_source_documents=True
)

# Preguntas de prueba
preguntas = [
    "¿Qué es el CLV y cómo se calcula?",
    "¿Cuáles son las categorías de productos?",
    "¿Cómo se segmentan los clientes?",
]
for p in preguntas:
    print(f"Q: {p}")
    print(f"A: {qa.invoke({'query': p})['result']}\n")
```
