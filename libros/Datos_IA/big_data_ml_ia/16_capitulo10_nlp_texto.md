# Capítulo 10: Procesamiento de Lenguaje Natural

## 10.1 NLP con Python

### 10.1.1 Preprocesamiento de Texto

```python
import re
import nltk
import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

# Descargar recursos de NLTK
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

stemmer = SnowballStemmer("spanish")
stop_words = set(stopwords.words("spanish"))

def preprocesar_texto(texto):
    if not isinstance(texto, str):
        return ""

    # Minúsculas
    texto = texto.lower()

    # Eliminar URLs
    texto = re.sub(r"http\S+|www\S+|https\S+", "", texto)

    # Eliminar signos de puntuación (mantener letras, números y espacios)
    texto = re.sub(r"[^\w\sáéíóúüñ]", " ", texto)

    # Eliminar números
    texto = re.sub(r"\d+", "", texto)

    # Tokenizar
    tokens = word_tokenize(texto, language="spanish")

    # Eliminar stopwords y palabras cortas
    tokens = [t for t in tokens if t not in stop_words and len(t) > 2]

    # Stemming
    tokens = [stemmer.stem(t) for t in tokens]

    return " ".join(tokens)

# Cargar reseñas TechStore
resenas = pd.read_parquet("data/techstore_reviews/")
resenas["texto_limpio"] = resenas["review_text"].apply(preprocesar_texto)

print("Ejemplo de preprocesamiento:")
print(f"Original: {resenas['review_text'].iloc[0][:200]}")
print(f"Limpio:   {resenas['texto_limpio'].iloc[0][:200]}")
```

### 10.1.2 Visualización de Texto

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Nube de palabras para reseñas positivas y negativas
positivas = resenas[resenas["rating"] >= 4]["texto_limpio"]
negativas = resenas[resenas["rating"] <= 2]["texto_limpio"]

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

texto_pos = " ".join(positivas.dropna())
wc_pos = WordCloud(width=800, height=400, background_color="white",
                   colormap="Greens", max_words=100).generate(texto_pos)
axes[0].imshow(wc_pos, interpolation="bilinear")
axes[0].axis("off")
axes[0].set_title("Reseñas Positivas (4-5 estrellas)")

texto_neg = " ".join(negativas.dropna())
wc_neg = WordCloud(width=800, height=400, background_color="white",
                   colormap="Reds", max_words=100).generate(texto_neg)
axes[1].imshow(wc_neg, interpolation="bilinear")
axes[1].axis("off")
axes[1].set_title("Reseñas Negativas (1-2 estrellas)")

plt.savefig("img/wordcloud_reviews.png")
```

## 10.2 Vectorización de Texto

### 10.2.1 Bag of Words y TF-IDF

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Bag of Words
bow = CountVectorizer(max_features=1000, ngram_range=(1, 2))
X_bow = bow.fit_transform(resenas["texto_limpio"])

# TF-IDF
tfidf = TfidfVectorizer(max_features=2000, ngram_range=(1, 3), min_df=5)
X_tfidf = tfidf.fit_transform(resenas["texto_limpio"])

print(f"BoW shape: {X_bow.shape}")
print(f"TF-IDF shape: {X_tfidf.shape}")
print(f"Vocabulario TF-IDF: {len(tfidf.get_feature_names_out()):,} términos")

# Clasificación de sentimiento
y_rating = (resenas["rating"] >= 4).astype(int)  # 1=positivo, 0=negativo

X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y_rating, test_size=0.2, random_state=42
)

nb = MultinomialNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

print("\nClasificación de Sentimiento (TF-IDF + Naive Bayes):")
print(classification_report(y_test, y_pred))

# Palabras más informativas para cada clase
log_prob = nb.feature_log_prob_
palabras_pos = tfidf.get_feature_names_out()[np.argsort(log_prob[1])[-20:]]
palabras_neg = tfidf.get_feature_names_out()[np.argsort(log_prob[0])[-20:]]

print(f"\nTop palabras positivas: {', '.join(palabras_pos[::-1])}")
print(f"Top palabras negativas: {', '.join(palabras_neg[::-1])}")
```

### 10.2.2 Word Embeddings

```python
from gensim.models import Word2Vec
from sklearn.decomposition import PCA

# Tokenizar reseñas
tokens = [texto.split() for texto in resenas["texto_limpio"].dropna()]

# Entrenar Word2Vec
w2v = Word2Vec(
    sentences=tokens,
    vector_size=100,
    window=5,
    min_count=5,
    workers=4,
    epochs=30
)

# Palabras similares
print("Palabras similares a 'producto':")
for palabra, sim in w2v.wv.most_similar("producto", topn=10):
    print(f"  {palabra}: {sim:.3f}")

# Embeddings promedio para clasificación
def document_vector(doc_tokens):
    vectors = [w2v.wv[word] for word in doc_tokens if word in w2v.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(w2v.vector_size)

X_w2v = np.array([document_vector(t) for t in tokens])

print(f"\nEmbeddings shape: {X_w2v.shape}")

# Clasificar con embeddings
X_train_w2v, X_test_w2v = train_test_split(
    range(len(X_w2v)), test_size=0.2, random_state=42
)
```

## 10.3 Análisis de Sentimiento con Deep Learning

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Bidirectional, GlobalMaxPooling1D

# Tokenización Keras
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(resenas["texto_limpio"])

sequences = tokenizer.texts_to_sequences(resenas["texto_limpio"])
X_seq = pad_sequences(sequences, maxlen=100, padding="post", truncating="post")

print(f"Secuencias shape: {X_seq.shape}")

# LSTM para clasificación
modelo_lstm = keras.Sequential([
    Embedding(5000, 128, input_length=100),
    Bidirectional(LSTM(64, return_sequences=True)),
    GlobalMaxPooling1D(),
    layers.Dense(32, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(1, activation="sigmoid")
])

modelo_lstm.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

modelo_lstm.summary()

# Entrenar
X_seq_train, X_seq_test, y_seq_train, y_seq_test = train_test_split(
    X_seq, y_rating, test_size=0.2, random_state=42
)

hist_lstm = modelo_lstm.fit(
    X_seq_train, y_seq_train,
    epochs=10,
    batch_size=64,
    validation_split=0.2,
    callbacks=[EarlyStopping(patience=3)]
)

# Evaluar
loss, acc = modelo_lstm.evaluate(X_seq_test, y_seq_test)
print(f"Test Accuracy (LSTM): {acc:.3f}")
```

## 10.4 Ejercicios

1. **Preprocesamiento**: Crea una función de preprocesamiento mejorada que maneje emojis, hashtags y menciones.
2. **TF-IDF**: Clasifica reseñas en 3 niveles (positivo, neutral, negativo) usando TF-IDF + Logistic Regression.
3. **Word2Vec**: Entrena Word2Vec con las reseñas y encuentra las 10 palabras más similares a "envío", "calidad" y "precio".
4. **LSTM**: Compara el rendimiento de LSTM unidireccional vs bidireccional para análisis de sentimiento.
5. **Visualización**: Genera wordclouds separadas para cada categoría de producto y analiza las diferencias.
