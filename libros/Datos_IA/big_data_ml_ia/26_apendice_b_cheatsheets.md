# Apéndice B: Cheatsheets y Referencias Rápidas

## PySpark

```python
# SparkSession
spark = SparkSession.builder.appName("App").getOrCreate()

# Leer/Escribir
spark.read.parquet("path/")           # Parquet
spark.read.csv("path/", header=True)  # CSV con cabecera
df.write.mode("overwrite").parquet("path/")
df.write.partitionBy("col").parquet("path/")

# Transformaciones
df.select("col1", "col2")
df.filter(col("col") > 100)
df.withColumn("new_col", expr("col * 2"))
df.groupBy("col").agg(sum("val"), avg("val"), count("*"))
df.join(other_df, "key", "left")
df.orderBy(col("val").desc())
df.dropDuplicates(["col"])
df.repartition(8, "key")

# SQL
df.createOrReplaceTempView("vista")
spark.sql("SELECT * FROM vista WHERE col > 100")

# Streaming
df_stream = spark.readStream.format("parquet").load("path/")
query = df_stream.writeStream \
    .format("console") \
    .trigger(processingTime="10 seconds") \
    .start()
query.awaitTermination()
```

## Scikit-learn

```python
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Pipeline
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(), cat_cols)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("clf", RandomForestClassifier())
])

# Entrenar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)

# Evaluar
score = model.score(X_test, y_test)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring="f1")

# Grid Search
GridSearchCV(model, param_grid, cv=3, scoring="roc_auc")
```

## TensorFlow/Keras

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# MLP
model = keras.Sequential([
    layers.Dense(128, activation="relu", input_shape=(n_features,)),
    layers.Dropout(0.3),
    layers.Dense(64, activation="relu"),
    layers.Dense(1)  # regresión
    # layers.Dense(1, activation="sigmoid")  # clasificación binaria
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])
model.fit(X_train, y_train, epochs=100, validation_split=0.2,
          callbacks=[EarlyStopping(patience=5)])
model.evaluate(X_test, y_test)
model.predict(X_test)

# LSTM
layers.LSTM(64, return_sequences=True)
layers.Bidirectional(LSTM(64))
```

## MLflow

```python
import mlflow

mlflow.set_experiment("experimento")

with mlflow.start_run():
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("plot.png")
    mlflow.sklearn.log_model(model, "model")

# Cargar modelo
model = mlflow.sklearn.load_model("runs:/run_id/model")

# Model Registry
mlflow.register_model("runs:/run_id/model", "ModelName")
```

## LangChain

```python
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

# RAG
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4"),
    chain_type="stuff",
    retriever=vectorstore.as_retriever(k=5)
)
qa.invoke({"query": "pregunta"})
```

## Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "api:app", "--host", "0.0.0.0"]
```

```bash
docker build -t techstore-ai .
docker run -p 8000:8000 techstore-ai
docker-compose up -d
docker-compose down
```
