# Cálculo Diferencial Básico: Tasas de Cambio y Optimización

El cálculo diferencial es la matemática del cambio. En análisis de datos lo usamos constantemente: cada vez que un modelo "aprende" ajustando sus parámetros, está haciendo cálculo diferencial. Este capítulo te dará la intuición y las herramientas para entender ese proceso.

## Derivadas: La Tasa de Cambio Instantánea

La derivada de una función f(x) en un punto x₀ mide cómo cambia f cuando x cambia infinitesimalmente:

```
f'(x₀) = límite cuando h→0 de (f(x₀ + h) - f(x₀)) / h
```

### Derivada Numérica

```python
import numpy as np
import matplotlib.pyplot as plt

def derivada_numerica(f, x, h=1e-7):
    """Aproximación de la derivada por diferencias finitas"""
    return (f(x + h) - f(x - h)) / (2 * h)

# Función cuadrática
def f(x):
    return x**2

# Derivada analítica: f'(x) = 2x
for x in [0, 1, 2, 3]:
    num = derivada_numerica(f, x)
    print(f"f'({x}) ≈ {num:.6f} (analítica: {2*x})")
# f'(0) ≈ 0.000000 (analítica: 0)
# f'(1) ≈ 2.000000 (analítica: 2)
# f'(2) ≈ 4.000000 (analítica: 4)
# f'(3) ≈ 6.000000 (analítica: 6)
```

> **💡 Consejo del Analista:**
> Siempre que puedas, deriva analíticamente con SymPy y luego convierte a NumPy con `lambdify`. Es más preciso que la diferenciación numérica y solo un poco más lento en tiempo de desarrollo.

### Derivadas con SymPy (Analíticas)

```python
import sympy as sp

x = sp.symbols('x')
f = x**3 * sp.exp(x)
derivada = sp.diff(f, x)
print(f"f'(x) = {derivada}")
# f'(x) = x**3*exp(x) + 3*x**2*exp(x)

# Evaluación numérica
f_prime = sp.lambdify(x, derivada, 'numpy')
print(f"f'(2) = {f_prime(2):.4f}")
# f'(2) = 59.1124
```

## Gradiente: La Derivada en Múltiples Dimensiones

Cuando tenemos múltiples variables, la derivada se convierte en gradiente: un vector de derivadas parciales.

```python
import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + y**2 + 3*x*y

# Gradiente (vector de derivadas parciales)
grad = [sp.diff(f, var) for var in [x, y]]
print(f"Gradiente: ∂f/∂x = {grad[0]}, ∂f/∂y = {grad[1]}")
# Gradiente: ∂f/∂x = 2*x + 3*y, ∂f/∂y = 2*y + 3*x
```

El gradiente apunta en la dirección de máximo crecimiento de la función. Por eso el *descenso de gradiente* se mueve en dirección opuesta al gradiente para minimizar.

## Descenso de Gradiente: Cómo Aprenden los Modelos

El descenso de gradiente es el algoritmo de optimización más importante en machine learning. Ajusta iterativamente los parámetros de un modelo para minimizar el error.

### Implementación desde Cero

```python
import numpy as np

def descenso_gradiente(grad_f, x0, lr=0.1, n_iter=100):
    """
    grad_f: función que calcula el gradiente en un punto
    x0: punto inicial
    lr: learning rate (tasa de aprendizaje)
    n_iter: número de iteraciones
    """
    x = np.array(x0, dtype=float)
    trayectoria = [x.copy()]

    for i in range(n_iter):
        grad = grad_f(x)
        x = x - lr * grad
        trayectoria.append(x.copy())

    return x, trayectoria

# Minimizar f(x, y) = x^2 + y^2 (mínimo en (0,0))
def grad_f(p):
    x, y = p
    return np.array([2*x, 2*y])

minimo, trayectoria = descenso_gradiente(grad_f, [5.0, 5.0], lr=0.1, n_iter=20)
print(f"Mínimo encontrado: {np.round(minimo, 6)}")
# Mínimo encontrado: [0.135335 0.135335]

# Error cuadrático medio (función de pérdida típica)
def grad_mse(X, y, beta):
    """Gradiente del MSE para regresión lineal"""
    n = len(y)
    error = X @ beta - y
    return (2/n) * X.T @ error

# Regresión lineal con descenso de gradiente
np.random.seed(42)
X = np.random.randn(100, 2)
y = 3 + 2*X[:, 0] - 1.5*X[:, 1] + np.random.randn(100)*0.3

# Añadir columna de 1s
X_b = np.column_stack([np.ones(100), X])
beta = np.zeros(3)

for _ in range(1000):
    beta = beta - 0.01 * grad_mse(X_b, y, beta)

print(f"β = {np.round(beta, 3)}")
# β ≈ [3.0  2.0  -1.5]
```

> **⚠️ Advertencia:**
> Un learning rate mal ajustado es la causa más común de fallo en el entrenamiento de modelos. Monitorea siempre la función de pérdida durante el entrenamiento: si oscila o diverge, reduce el learning rate. Si converge muy lento, auméntalo.

### El Problema del Learning Rate

La tasa de aprendizaje (learning rate) es crítica:

- **Demasiado grande:** el algoritmo diverge (no converge)
- **Demasiado pequeño:** converge muy lentamente
- **Bien ajustado:** converge eficientemente

```python
# Demostración de learning rate
def grad_f_simple(x):
    return 2 * x  # Derivada de x²

for lr in [0.01, 0.1, 1.0]:
    x = 10.0
    for _ in range(10):
        x = x - lr * grad_f_simple(x)
    print(f"LR={lr:.2f}: x final = {x:.6f}")
# LR=0.01: x final = 8.170730
# LR=0.10: x final = 1.073742
# LR=1.00: x final = 10.000000 (oscila sin converger)
```

## Regla de la Cadena y Retropropagación

La regla de la cadena es fundamental para entender cómo se entrenan las redes neuronales:

```
∂z/∂x = (∂z/∂y) * (∂y/∂x)
```

```python
import sympy as sp

x = sp.symbols('x')
y = x**2 + 3*x      # y = g(x)
z = sp.sin(y)        # z = f(y)

# Regla de la cadena: dz/dx = dz/dy * dy/dx
dz_dy = sp.diff(z, y)
dy_dx = sp.diff(y, x)
dz_dx = dz_dy * dy_dx

print(f"dz/dx = {dz_dx}")
# dz/dx = (2*x + 3)*cos(x**2 + 3*x)

# Verificación directa
print(f"Directa: {sp.diff(z, x)}")
# Directa: (2*x + 3)*cos(x**2 + 3*x)
```

## Jacobiano y Hessiano

### Matriz Jacobiana

Cuando una función tiene múltiples entradas y múltiples salidas, el gradiente se generaliza a la matriz Jacobiana:

```python
import sympy as sp

x, y = sp.symbols('x y')
f1 = x**2 + y**2
f2 = x*y

# Jacobiana
J = sp.Matrix([f1, f2]).jacobian([x, y])
print(f"Jacobiana:\n{J}")
# [[2*x, 2*y],
#  [  y,   x]]
```

### Matriz Hessiana

La Hessiana contiene las segundas derivadas parciales. Determina si un punto crítico es mínimo, máximo o punto de silla:

```python
f = x**3 - 3*x*y**2  # Función de ejemplo

# Hessiana
H = sp.hessian(f, (x, y))
print(f"Hessiana:\n{H}")
# [[6*x, -6*y],
#  [-6*y, -6*x]]
```

## Aplicación Práctica: Optimización de una Función de Costo

```python
from scipy import optimize

# Función de costo tipo Rosenbrock
def costo(params):
    x, y = params
    return (1 - x)**2 + 100 * (y - x**2)**2

# Gradiente de la función de costo
def grad_costo(params):
    x, y = params
    dx = -2*(1 - x) - 400*x*(y - x**2)
    dy = 200*(y - x**2)
    return np.array([dx, dy])

# Mínimo en (1, 1)
resultado = optimize.minimize(costo, [0, 0], method='BFGS', jac=grad_costo)
print(f"Mínimo: {np.round(resultado.x, 6)}")
# Mínimo: [1. 1.]
print(f"Valor: {resultado.fun:.2e}")
# Valor: 0.00e+00
```

Las funciones de pérdida en machine learning (MSE, cross-entropy, etc.) son versiones a gran escala de este mismo problema.

## Derivadas Parciales en la Práctica

Entender derivadas parciales te permite interpretar coeficientes de modelos:

```python
# En regresión lineal: y = β₀ + β₁x₁ + β₂x₂
# ∂y/∂x₁ = β₁ → "cambio en y por unidad de cambio en x₁"
```

Cada coeficiente en una regresión es una derivada parcial: mide la sensibilidad de la salida ante cambios en esa variable.

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Calcula la derivada numérica de f(x) = sin(x²) en x=2 usando diferencias finitas con h=0.1, 0.01, 0.001, 0.0001. Compara con el valor analítico. ¿Qué h da mejor resultado?
   - Pista: f'(x) = (f(x+h) - f(x-h)) / (2h)

2. **Ejercicio 2:** Implementa el descenso de gradiente para minimizar f(x,y) = x² + 2y² + xy. Parte de (3, 3) con learning rate 0.1. ¿En cuántas iteraciones converge?

3. **Ejercicio 3:** Usando SymPy, calcula el gradiente y la matriz Hessiana de f(x,y,z) = x²y + y²z + z²x. Evalúa en el punto (1, -1, 0).

4. **Ejercicio 4:** Explica con tus palabras la relación entre la regla de la cadena y la retropropagación en redes neuronales. ¿Por qué es importante poder descomponer la derivada de una función compuesta?

## 📝 Resumen del Capítulo

- La **derivada** mide la tasa de cambio instantánea de una función
- El **gradiente** generaliza la derivada a múltiples dimensiones (vector de derivadas parciales)
- El **descenso de gradiente** minimiza funciones moviéndose en dirección opuesta al gradiente
- El **learning rate** controla el tamaño del paso; muy grande diverge, muy pequeño es lento
- La **regla de la cadena** permite descomponer derivadas de funciones compuestas (base de la retropropagación)
- El **Jacobiano** generaliza el gradiente para funciones vectoriales
- El **Hessiano** contiene las segundas derivadas; determina si un punto crítico es mínimo o máximo

**Conceptos clave aprendidos:** derivada, gradiente, descenso de gradiente, learning rate, regla de la cadena, Jacobiano, Hessiano, optimización
