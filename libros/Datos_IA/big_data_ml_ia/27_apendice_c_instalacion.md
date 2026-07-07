# Apéndice C: Guía de Instalación y Configuración

## C.1 Python y Entorno Virtual

```bash
# Python 3.10+ requerido
python --version

# Crear entorno virtual
python -m venv .venv

# Activar
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Actualizar pip
pip install --upgrade pip
```

## C.2 Instalación de Librerías

### C.2.1 Data Science Base

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### C.2.2 Big Data

```bash
pip install pyspark
# Opcional: conectar con Hadoop
# pip install找到hadoop找到找到找到找到找到找到
```

### C.2.3 Machine Learning

```bash
pip install xgboost lightgbm
pip install scikit-learn  # ya incluido arriba
```

### C.2.4 Deep Learning

```bash
pip install tensorflow
# Para GPU:
# pip install tensorflow[and-cuda]
```

### C.2.5 NLP

```bash
pip install nltk wordcloud gensim

# Descargar recursos NLTK
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### C.2.6 Series Temporales

```bash
pip install prophet statsmodels
```

### C.2.7 MLOps

```bash
pip install mlflow
```

### C.2.8 IA Generativa

```bash
pip install langchain langchain-community langchain-openai
pip install langchain-google-vertexai
pip install chromadb faiss-cpu
pip install huggingface-hub sentence-transformers
```

### C.2.9 Producción y API

```bash
pip install fastapi uvicorn streamlit
pip install google-cloud-aiplatform google-cloud-bigquery
```

### C.2.10 Instalación Completa

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
pyspark>=3.5.0
xgboost>=2.0.0
lightgbm>=4.0.0
tensorflow>=2.15.0
nltk>=3.8.0
wordcloud>=1.9.0
gensim>=4.3.0
prophet>=1.1.0
statsmodels>=0.14.0
mlflow>=2.10.0
langchain>=0.1.0
langchain-community>=0.0.10
langchain-openai>=0.0.2
chromadb>=0.4.0
faiss-cpu>=1.7.0
sentence-transformers>=2.2.0
fastapi>=0.109.0
uvicorn>=0.27.0
streamlit>=1.30.0
google-cloud-aiplatform>=1.38.0
google-cloud-bigquery>=3.14.0
```

## C.3 Configuración de PySpark

```python
import os

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

# Para Windows:
os.environ["HADOOP_HOME"] = "C:\\hadoop"
# Descargar winutils.exe de https://github.com/steveloughran/winutils
```

## C.4 Configuración de APIs

### C.4.1 OpenAI

```bash
export OPENAI_API_KEY="sk-..."
# O crear .env:
echo "OPENAI_API_KEY=sk-..." > .env
```

### C.4.2 Google Cloud

```bash
# Instalar gcloud CLI
gcloud auth application-default login
gcloud config set project techstore-analytics

# O usar service account
export GOOGLE_APPLICATION_CREDENTIALS="service-account.json"
```

## C.5 Docker

```bash
# Instalar Docker Desktop desde https://www.docker.com/products/docker-desktop/

# Verificar
docker --version
docker-compose --version

# Comandos básicos
docker pull apache/spark:latest
docker pull minio/minio
docker pull apache/airflow:latest
```

## C.6 Verificación de Instalación

```python
# scripts/verify_install.py
import sys
import importlib

librerias = [
    "pandas", "numpy", "sklearn", "pyspark", "xgboost",
    "tensorflow", "nltk", "prophet", "mlflow", "langchain",
    "fastapi", "uvicorn", "streamlit"
]

print(f"Python {sys.version}\n")
print("=== Verificación de Librerías ===")

for lib in librerias:
    try:
        importlib.import_module(lib)
        print(f"  ✅ {lib}")
    except ImportError:
        print(f"  ❌ {lib}")

print("\n¡Listo para comenzar!")
```

## C.7 Troubleshooting

| Problema | Solución |
|----------|----------|
| PySpark no encuentra Hadoop | Descargar winutils.exe o instalar en WSL |
| TensorFlow GPU no detecta | `pip install tensorflow[and-cuda]` |
| Prophet falla en Windows | Usar WSL o conda install |
| mlflow no conecta | Verificar `mlflow.set_tracking_uri()` |
| LangChain OpenAI sin API key | Configurar OPENAI_API_KEY en .env |
| Streamlit no muestra gráficos | `pip install --upgrade plotly` |
| FAISS no se instala | Usar `pip install faiss-cpu` (no faiss) |
