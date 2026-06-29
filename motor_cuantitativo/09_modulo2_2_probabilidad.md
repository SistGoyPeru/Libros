# Teoría de la Probabilidad y Teorema de Bayes

La probabilidad es el lenguaje de la incertidumbre. En análisis de datos, cada predicción, cada intervalo de confianza y cada decisión basada en datos es una declaración probabilística. Este capítulo te da las bases para entender y cuantificar la incertidumbre.

## Conceptos Fundamentales

### Espacio Muestral y Eventos

El *espacio muestral* (Ω) es el conjunto de todos los resultados posibles. Un *evento* es un subconjunto del espacio muestral.

```python
import numpy as np
from itertools import product

# Espacio muestral: lanzar dos dados
omega = list(product(range(1, 7), repeat=2))
print(f"Espacio muestral: {len(omega)} resultados posibles")
# Espacio muestral: 36 resultados posibles

# Evento A: suma = 7
evento_A = [resultado for resultado in omega if sum(resultado) == 7]
print(f"P(A) = {len(evento_A)}/{len(omega)} = {len(evento_A)/len(omega):.4f}")
# P(A) = 6/36 = 0.1667

# Evento B: ambos dados pares
evento_B = [r for r in omega if r[0] % 2 == 0 and r[1] % 2 == 0]
print(f"P(B) = {len(evento_B)}/{len(omega)} = {len(evento_B)/len(omega):.4f}")
# P(B) = 9/36 = 0.2500
```

### Axiomas de Probabilidad

1. **No negatividad:** P(A) ≥ 0
2. **Normalización:** P(Ω) = 1
3. **Aditividad:** Si A y B son mutuamente excluyentes, P(A ∪ B) = P(A) + P(B)

## Probabilidad Condicional e Independencia

La probabilidad condicional responde a: "¿cómo cambia la probabilidad de A si sabemos que B ocurrió?"

```
P(A|B) = P(A ∩ B) / P(B)
```

```python
# Probabilidad condicional: dado que la suma es 7,
# ¿cuál es la probabilidad de que el primer dado sea 3?
evento_A = [(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)]
evento_B = [(3,4), (3,5), (3,6), (3,1), (3,2), (3,3)]

# Esto no es correcto porque los eventos no están
# definidos sobre el espacio muestral completo.
# Mejor:

omega = list(product(range(1, 7), repeat=2))

# A: suma = 7
A = {r for r in omega if sum(r) == 7}
# B: primer dado = 3
B = {r for r in omega if r[0] == 3}

# P(A|B) = P(A ∩ B) / P(B)
A_int_B = A & B
p_A_dado_B = len(A_int_B) / len(B)
print(f"P(A|B) = {p_A_dado_B:.4f}")
# P(A|B) = 0.1667 (de 6 resultados con primer dado=3, solo 1 suma 7)
```

### Independencia

Dos eventos son independientes si P(A|B) = P(A), o equivalentemente P(A ∩ B) = P(A) · P(B):

```python
# ¿Son independientes "primer dado = 3" y "suma = 7"?
p_A = len(A) / len(omega)
p_B = len(B) / len(omega)
p_A_int_B = len(A_int_B) / len(omega)

print(f"P(A)·P(B) = {p_A * p_B:.4f}")
print(f"P(A∩B) = {p_A_int_B:.4f}")
print(f"¿Independientes? {np.isclose(p_A * p_B, p_A_int_B)}")
# P(A)·P(B) = 0.0463
# P(A∩B) = 0.0278
# ¿Independientes? False
```

## Teorema de Probabilidad Total

Para un conjunto de eventos {Bᵢ} que particionan el espacio muestral:

```
P(A) = Σ P(A|Bᵢ) · P(Bᵢ)
```

```python
# Ejemplo: tres urnas con bolas
# Urna 1: 3 rojas, 7 azules (P=0.5)
# Urna 2: 5 rojas, 5 azules (P=0.3)
# Urna 3: 8 rojas, 2 azules (P=0.2)

p_urna = [0.5, 0.3, 0.2]
p_roja_dada_urna = [3/10, 5/10, 8/10]

p_roja = sum(p * pr for p, pr in zip(p_urna, p_roja_dada_urna))
print(f"P(Roja) = {p_roja:.4f}")
# P(Roja) = 0.4600
```

## Teorema de Bayes

Bayes es el teorema más importante que aprenderás como analista. Permite actualizar creencias (probabilidades) a la luz de nueva evidencia:

```
P(A|B) = P(B|A) · P(A) / P(B)
```

Donde:
- P(A): *probabilidad a priori* (antes de ver los datos)
- P(B|A): *verosimilitud* (likelihood)
- P(A|B): *probabilidad a posteriori* (después de ver los datos)

### Ejemplo Clásico: Prueba Médica

```python
# Supongamos:
# - Enfermedad rara: P(E) = 0.01 (1% de la población)
# - Prueba detecta 95% de enfermos: P(+|E) = 0.95 (sensibilidad)
# - Prueba da falso positivo en 5%: P(+|no E) = 0.05 (1 - especificidad)

# Pregunta: si una persona da positivo, ¿cuál es la probabilidad
# de que realmente tenga la enfermedad?

p_enfermedad = 0.01
p_positivo_dado_enfermo = 0.95
p_positivo_dado_sano = 0.05

# Probabilidad total de positivo
p_positivo = (p_positivo_dado_enfermo * p_enfermedad +
              p_positivo_dado_sano * (1 - p_enfermedad))

# Teorema de Bayes
p_enfermedad_dado_positivo = (p_positivo_dado_enfermo * p_enfermedad) / p_positivo

print(f"P(Enfermo | +) = {p_enfermedad_dado_positivo:.4f} ({p_enfermedad_dado_positivo*100:.1f}%)")
# P(Enfermo | +) = 0.1610 (16.1%)
```

> **⚠️ Advertencia:**
> Aunque la prueba parece confiable (95% de sensibilidad), la baja prevalencia (1%) hace que la mayoría de positivos sean falsos. Este es un error clásico de interpretación incluso entre médicos.

### Implementación General de Bayes

```python
def teorema_bayes(p_hipotesis, p_evidencia_dado_hipotesis, p_evidencia_dado_no_hipotesis):
    """
    Calcula P(Hipótesis | Evidencia)

    Parámetros:
    - p_hipotesis: P(H), probabilidad a priori
    - p_evidencia_dado_hipotesis: P(E|H), verosimilitud
    - p_evidencia_dado_no_hipotesis: P(E|¬H)
    """
    p_evidencia = (p_evidencia_dado_hipotesis * p_hipotesis +
                   p_evidencia_dado_no_hipotesis * (1 - p_hipotesis))
    return (p_evidencia_dado_hipotesis * p_hipotesis) / p_evidencia

# Aplicación a detección de spam
# - 20% de los emails son spam: P(Spam) = 0.20
# - 90% de los spams contienen "oferta": P("oferta"|Spam) = 0.90
# - 10% de los emails legítimos contienen "oferta": P("oferta"|NoSpam) = 0.10

p_spam_dado_oferta = teorema_bayes(0.20, 0.90, 0.10)
print(f"P(Spam | 'oferta') = {p_spam_dado_oferta:.4f} ({p_spam_dado_oferta*100:.1f}%)")
# P(Spam | 'oferta') = 0.6923 (69.2%)
```

## Bayes Múltiple: Actualización Secuencial

El poder de Bayes está en la actualización iterativa: la *posterior* de hoy es la *prior* de mañana:

```python
def actualizar_bayes(p_prior, verosimilitud_positivo, verosimilitud_negativo, datos):
    """
    Actualiza secuencialmente P(H) con múltiples observaciones

    datos: lista de 'positivo' o 'negativo'
    """
    p = p_prior
    historial = [p]

    for resultado in datos:
        if resultado == 'positivo':
            p = teorema_bayes(p, verosimilitud_positivo, 1 - verosimilitud_positivo)
        else:
            p = teorema_bayes(p, 1 - verosimilitud_negativo, verosimilitud_negativo)
        historial.append(p)

    return p, historial

# Diagnosticar enfermedad con 3 pruebas
# Supongamos P(E)=0.5 (inciertos), prueba tiene 90% sensibilidad y 90% especificidad
p_final, hist = actualizar_bayes(
    p_prior=0.5,
    verosimilitud_positivo=0.9,
    verosimilitud_negativo=0.1,  # 1 - especificidad
    datos=['positivo', 'positivo', 'negativo']
)

for i, p in enumerate(hist):
    print(f"Después de observación {i}: P(E) = {p:.4f}")
# Después de observación 0: P(E) = 0.5000 (prior)
# Después de observación 1: P(E) = 0.9000
# Después de observación 2: P(E) = 0.9878
# Después de observación 3: P(E) = 0.9000 (una negativa reduce la certeza)
```

## Aplicación en Machine Learning: Naive Bayes

El clasificador *Naive Bayes* aplica el teorema de Bayes con el supuesto (ingenuo) de independencia entre características:

```python
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Cargar datos
iris = load_iris()
X, y = iris.data, iris.target

# Dividir
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Entrenar Naive Bayes
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_test)
precision = np.mean(y_pred == y_test)
print(f"Precisión: {precision:.2%}")
# Precisión: ~96%

# Probabilidades a posteriori (esto es Bayes puro)
probabilidades = modelo.predict_proba(X_test[:3])
print("Probabilidades a posteriori para 3 muestras:")
print(np.round(probabilidades, 3))
# [[1.000 0.000 0.000]   -> 100% clase 0
#  [0.000 0.999 0.001]   -> 99.9% clase 1
#  [0.000 0.015 0.985]]  -> 98.5% clase 2
```

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Escribe una función que simule el lanzamiento de una moneda 1000 veces y compare la frecuencia relativa de caras con la probabilidad teórica (0.5). ¿Qué observas al aumentar el número de lanzamientos?

2. **Ejercicio 2:** Un test detecta una condición con 99% de sensibilidad y 95% de especificidad. Si la condición afecta al 0.5% de la población, ¿cuál es la probabilidad de tener la condición si el test da positivo?

3. **Ejercicio 3:** Implementa un clasificador Naive Bayes desde cero (sin scikit-learn) para el dataset Iris y compáralo con el de sklearn. Usa el teorema de Bayes con el supuesto de normalidad de las características.

## 📝 Resumen del Capítulo

- La **probabilidad** cuantifica la incertidumbre entre 0 y 1
- La **probabilidad condicional** P(A|B) actualiza la creencia en A dado que B ocurrió
- Dos eventos son **independientes** si P(A∩B) = P(A)·P(B)
- El **Teorema de Probabilidad Total** descompone una probabilidad en casos
- El **Teorema de Bayes** es el mecanismo formal para actualizar creencias con datos
- La **prior** se actualiza a **posterior** mediante la **verosimilitud**
- **Naive Bayes** aplica Bayes con independencia condicional entre características
- La actualización secuencial permite incorporar nueva evidencia progresivamente

**Conceptos clave aprendidos:** espacio muestral, evento, probabilidad condicional, independencia, Teorema de Probabilidad Total, Teorema de Bayes, prior, verosimilitud, posterior, Naive Bayes
