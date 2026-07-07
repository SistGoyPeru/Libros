# Capítulo 13: LLMs e Inteligencia Artificial Generativa

## 13.1 Introducción a los LLMs

Los Large Language Models (LLMs) han revolucionado la IA. Modelos como GPT-4, Claude y Llama pueden entender y generar texto con una fluidez sin precedentes.

### 13.1.1 Arquitectura Transformer

```python
# Concepto: Attention is All You Need
conceptos_transformer = {
    "Self-Attention": "Cada palabra mira a todas las demás para entender contexto",
    "Multi-Head Attention": "Múltiples cabezas de atención en paralelo",
    "Positional Encoding": "Codificación de posición de palabras en la secuencia",
    "Feed Forward": "Red densa después de la atención",
    "Layer Norm": "Normalización para estabilidad del entrenamiento"
}
```

### 13.1.2 Modelos Disponibles

```python
modelos_llm = {
    "Propietarios": ["GPT-4 (OpenAI)", "Claude (Anthropic)", "Gemini (Google)"],
    "Open Source": ["Llama 3 (Meta)", "Mistral", "Falcon", "Phi-3 (Microsoft)"],
    "Cloud": ["Vertex AI (Gemini)", "Amazon Bedrock", "Azure OpenAI"]
}
```

## 13.2 LangChain: Orquestación de LLMs

### 13.2.1 Configuración

```python
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.chains import LLMChain, RetrievalQA, SimpleSequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.callbacks import StreamingStdOutCallbackHandler

# Opciones de LLM
llm_local = Ollama(model="llama3", temperature=0.7)
llm_cloud = ChatOpenAI(model="gpt-4", temperature=0.3)
llm_vertex = VertexAI(model="gemini-pro", temperature=0.5)
```

### 13.2.2 Prompts y Chains

```python
# Template básico
template_analista = """
Eres un asistente experto en datos de TechStore, una tienda de tecnología.
Responde la pregunta basándote en el contexto proporcionado.

Contexto: {contexto}

Pregunta: {pregunta}

Respuesta:
"""

prompt = PromptTemplate(
    template=template_analista,
    input_variables=["contexto", "pregunta"]
)

# Chain simple
chain = LLMChain(
    llm=llm_cloud,
    prompt=prompt,
    verbose=True
)

# Usar
respuesta = chain.invoke({
    "contexto": "TechStore vendió 10M en electrónicos en Q1 2025",
    "pregunta": "¿Cuánto vendió TechStore en electrónicos?"
})
print(respuesta["text"])
```

### 13.2.3 Memoria y Conversación

```python
from langchain.chains import ConversationChain

# Memoria conversacional
memory = ConversationBufferMemory()
conversacion = ConversationChain(
    llm=llm_cloud,
    memory=memory,
    verbose=True
)

# Chat continuo
resp1 = conversacion.predict(input="¿Cuáles son las categorías de TechStore?")
print(resp1)

resp2 = conversacion.predict(input="¿Cuál fue la más vendida en 2025?")
print(resp2)
# La memoria recuerda que hablamos de TechStore
```

## 13.3 RAG: Retrieval-Augmented Generation

RAG combina recuperación de información con generación de texto. Es la técnica clave para hacer que los LLMs trabajen con tus datos.

### 13.3.1 Vector Store

```python
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DataFrameLoader, TextLoader, DirectoryLoader

# Cargar documentos TechStore
loader = DirectoryLoader(
    "data/documentacion/",
    glob="**/*.md",
    loader_cls=TextLoader
)
documentos = loader.load()

print(f"Documentos cargados: {len(documentos)}")

# Dividir en chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
)
chunks = text_splitter.split_documents(documentos)
print(f"Chunks creados: {len(chunks)}")

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Vector store
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("data/vectorstore/techstore_docs")
```

### 13.3.2 RetrievalQA Chain

```python
from langchain.chains import RetrievalQA

# Crear retrievers
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# Chain QA con RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=llm_cloud,
    chain_type="stuff",  # 'stuff', 'map_reduce', 'refine', 'map_rerank'
    retriever=retriever,
    return_source_documents=True,
    verbose=True
)

# Preguntas sobre TechStore
preguntas = [
    "¿Cómo se calcula el CLV en TechStore?",
    "¿Qué productos tienen mayor rotación?",
    "¿Cuál es el perfil del cliente premium?"
]

for pregunta in preguntas:
    print(f"\nPregunta: {pregunta}")
    resultado = qa_chain.invoke({"query": pregunta})
    print(f"Respuesta: {resultado['result'][:200]}...")
    print(f"Fuentes: {len(resultado['source_documents'])} documentos")
```

### 13.3.3 RAG sobre TechStore Reviews

```python
# Crear RAG específico para reseñas
loader_reviews = DataFrameLoader(resenas, page_content_column="review_text")
docs_reviews = loader_reviews.load()
chunks_reviews = text_splitter.split_documents(docs_reviews)

vectorstore_reviews = FAISS.from_documents(chunks_reviews, embeddings)

qa_reviews = RetrievalQA.from_chain_type(
    llm=llm_cloud,
    chain_type="stuff",
    retriever=vectorstore_reviews.as_retriever(k=3)
)

# Consultas sobre reseñas
consultas = [
    "¿Qué dicen los clientes sobre el envío?",
    "¿Cuáles son las quejas más comunes sobre laptops?",
    "¿Qué productos tienen mejores reseñas?"
]

for consulta in consultas:
    print(f"\n--- {consulta} ---")
    print(qa_reviews.invoke({"query": consulta})["result"][:300])
```

## 13.4 Agentes con LangChain

```python
from langchain.agents import AgentExecutor, create_react_agent, Tool
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Herramientas personalizadas
@tool
def consultar_ventas(query: str) -> str:
    """Consulta métricas de ventas de TechStore"""
    df = pd.read_parquet("data/gold/ventas_diarias/")
    return f"Ventas totales: ${df['ingresos'].sum():,.2f}"

@tool
def buscar_producto(query: str) -> str:
    """Busca información de productos en TechStore"""
    df = pd.read_parquet("data/techstore_products/")
    resultado = df[df["product_name"].str.contains(query, case=False, na=False)]
    return resultado.to_string()

# Crear agente
tools = [consultar_ventas, buscar_producto]

prompt_agente = """
Eres un asistente de datos de TechStore. Tienes acceso a las siguientes herramientas:
{tools}

Usa las herramientas para responder preguntas sobre ventas y productos.

Pregunta: {input}

{agent_scratchpad}
"""

agente = create_react_agent(
    llm=llm_cloud,
    tools=tools,
    prompt=PromptTemplate.from_template(prompt_agente)
)

agent_executor = AgentExecutor(
    agent=agente,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

# Probar agente
respuesta = agent_executor.invoke({
    "input": "¿Cuánto vendió TechStore en total y qué productos son laptops?"
})
print(respuesta["output"])
```

## 13.5 Ejercicios

1. **Prompts**: Diseña 3 prompts diferentes para que un LLM analice datos de ventas de TechStore. Compara la calidad de las respuestas.
2. **RAG**: Construye un sistema RAG completo con documentación técnica de TechStore y prueba 5 preguntas de negocio.
3. **Vector Store**: Compara FAISS vs Chroma como vector store. ¿Cuál es más rápido? ¿Cuál escala mejor?
4. **Agentes**: Crea un agente con 3 herramientas personalizadas que pueda responder preguntas complejas sobre TechStore.
5. **Evaluación**: Diseña un conjunto de evaluación para medir la calidad de un sistema RAG (faithfulness, relevance, helpfulness).
