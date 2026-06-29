## Módulo 1: El Lenguaje de los Datos

# El Ecosistema Matemático en Python

Python se ha convertido en el lenguaje dominante para el análisis de datos no por casualidad, sino por su ecosistema de librerías matemáticas. En este capítulo exploraremos las tres herramientas fundamentales que usarás a lo largo de todo el libro: NumPy, SciPy y SymPy.

## NumPy: El Corazón Numérico

NumPy (*Numerical Python*) es la librería fundamental para cómputo científico en Python. Su estructura principal, el `ndarray`, es un contenedor multidimensional homogéneo que permite operaciones vectorizadas de alto rendimiento.

### Arrays vs Listas de Python

La diferencia crucial entre una lista de Python y un array de NumPy es la eficiencia:

```python
import numpy as np
import time

# Lista de Python
lista = list(range(10_000_000))

# Array de NumPy
arr = np.arange(10_000_000)

# Multiplicación por 2 con listas
inicio = time.time()
resultado_lista = [x * 2 for x in lista]
print(f"Lista: {time.time() - inicio:.4f} segundos")

# Multiplicación por 2 con NumPy (vectorizada)
inicio = time.time()
resultado_arr = arr * 2
print(f"NumPy: {time.time() - inicio:.4f} segundos")
# Resultado: Lista: ~0.8s, NumPy: ~0.02s (40x más rápido)
```

Las operaciones vectorizadas ocurren en C, sin bucles Python. Esto permite trabajar con millones de datos sin sacrificar rendimiento.

### Creación de Arrays

```python
# Desde lista
a = np.array([1, 2, 3, 4, 5])

# Rangos
b = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
c = np.linspace(0, 1, 5)   # [0.0, 0.25, 0.5, 0.75, 1.0]

# Matrices especiales
d = np.zeros((3, 3))       # Matriz 3x3 de ceros
e = np.ones((2, 4))        # Matriz 2x4 de unos
f = np.eye(4)              # Matriz identidad 4x4
g = np.random.randn(1000)  # 1000 valores aleatorios N(0,1)
```

### Broadcasting

Una de las características más poderosas de NumPy es el *broadcasting*: operar arrays de diferentes formas sin necesidad de expansión explícita:

```python
# Broadcasting: sumar un escalar a cada elemento
arr = np.array([[1, 2, 3], [4, 5, 6]])
resultado = arr + 10
print(resultado)
# [[11 12 13]
#  [14 15 16]]

# Broadcasting con arrays de diferente forma
fila = np.array([1, 0, 1])
print(arr + fila)
# [[2 2 4]
#  [5 5 7]]
```

Las reglas del broadcasting: las dimensiones se comparan de derecha a izquierda. Son compatibles si son iguales o una es 1.

### Indexación y Cortes

```python
arr = np.arange(12).reshape(3, 4)
print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Indexación booleana
print(arr[arr > 5])
# [ 6  7  8  9 10 11]

# Indexación fancy
print(arr[[0, 2], :])
# [[ 0  1  2  3]
#  [ 8  9 10 11]]
```

## SciPy: Matemáticas Aplicadas

SciPy se construye sobre NumPy y añade algoritmos para optimización, integración, interpolación, álgebra lineal, procesamiento de señales y estadística.

```python
from scipy import optimize, stats, linalg, integrate
```

### Optimización

Encontrar el mínimo de una función es esencial en machine learning:

```python
from scipy import optimize

# Minimizar una función simple
def f(x):
    return x**2 + 5 * np.sin(x)

resultado = optimize.minimize_scalar(f)
print(f"Mínimo en x = {resultado.x:.4f}, f(x) = {resultado.fun:.4f}")
# Resultado: Mínimo en x = -1.1108, f(x) = -3.2464

# Encontrar raíces
raiz = optimize.root_scalar(lambda x: x**2 - 4, bracket=[0, 5])
print(f"Raíz en x = {raiz.root:.4f}")
# Resultado: Raíz en x = 2.0000
```

### Distribuciones Estadísticas

Acceso a más de 80 distribuciones de probabilidad:

```python
from scipy import stats

# Distribución normal estándar
z = stats.norm.ppf(0.975)  # Percentil 97.5% (para IC del 95%)
print(f"z(0.975) = {z:.4f}")
# Resultado: z(0.975) = 1.9600

# Función de densidad
pdf = stats.norm.pdf(0)
print(f"N(0,1) en x=0: {pdf:.4f}")
# Resultado: N(0,1) en x=0: 0.3989

# Valor p para un estadístico t
t_stat = 2.1
p_valor = stats.t.sf(t_stat, df=30) * 2  # Dos colas
print(f"Valor p: {p_valor:.4f}")
# Resultado: Valor p: 0.0441
```

## SymPy: Matemática Simbólica

SymPy permite hacer matemáticas con símbolos en lugar de números. Es como tener un CAS (Computer Algebra System) dentro de Python.

```python
import sympy as sp

# Definir símbolos
x, y = sp.symbols('x y')

# Expresiones simbólicas
expr = x**2 + 2*x + 1
print(sp.factor(expr))
# (x + 1)**2

# Límites
limite = sp.limit(sp.sin(x) / x, x, 0)
print(f"límite sin(x)/x cuando x→0: {limite}")
# límite sin(x)/x cuando x→0: 1

# Derivadas
derivada = sp.diff(x**3 * sp.sin(x), x)
print(f"derivada: {derivada}")
# derivada: x**3*cos(x) + 3*x**2*sin(x)

# Integrales
integral = sp.integrate(sp.exp(-x**2), (x, -sp.oo, sp.oo))
print(f"integral: {integral}")
# integral: sqrt(pi)
```

### Evaluación Numérica de Expresiones Simbólicas

```python
expr = sp.sin(x) / x
f_lambda = sp.lambdify(x, expr, 'numpy')
valores = f_lambda(np.array([0.1, 0.5, 1.0]))
print(valores)
# [0.99833417 0.95885108 0.84147098]
```

La función `lambdify` convierte una expresión simbólica en una función NumPy compilable, uniendo lo mejor de ambos mundos.

## ¿Cuándo usar cada una?

| Librería | Para qué | Ejemplo típico |
|----------|----------|----------------|
| NumPy | Manipulación numérica eficiente | Operaciones vectorizadas, álgebra lineal básica |
| SciPy | Algoritmos matemáticos avanzados | Optimización, tests estadísticos, señales |
| SymPy | Matemática simbólica | Derivar fórmulas, simplificar expresiones |

> **💡 Consejo del Analista:**
> Cuando empieces un proyecto nuevo, importa NumPy como `np` y SciPy como `sp` (o `scipy`). Es una convención universal que hará tu código legible para otros analistas.

En la práctica, trabajarás con NumPy a diario, SciPy semanalmente (para estadística y optimización) y SymPy ocasionalmente (para derivar ecuaciones o entender un algoritmo).

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Crea un array NumPy de 1000 elementos con `np.random.randn(1000)`. Multiplica cada elemento por 2 usando un bucle `for` y usando vectorización. Compara los tiempos de ejecución.
   - Pista: Usa `time.time()` antes y después de cada operación.

2. **Ejercicio 2:** Usando SciPy, encuentra el mínimo de la función f(x) = x⁴ - 3x² + 2x + 1 en el intervalo [-2, 2]. Grafica la función y marca el mínimo.

3. **Ejercicio 3:** Con SymPy, deriva la función f(x) = e^(x²) · sin(3x) y simplifica el resultado. Evalúa la derivada en x=2 usando `lambdify`.

4. **Ejercicio 4:** Demuestra el broadcasting: crea una matriz 4x3 y un vector fila de 3 elementos. Súmalos. Explica qué está sucediendo con las dimensiones.

## 📝 Resumen del Capítulo

- **NumPy** proporciona el `ndarray` para operaciones vectorizadas eficientes
- **SciPy** implementa algoritmos matemáticos y estadísticos sobre NumPy
- **SymPy** permite manipulación simbólica de expresiones matemáticas
- El **broadcasting** permite operaciones entre arrays de diferente forma
- Las tres librerías se complementan y son interoperables
- `lambdify` convierte expresiones simbólicas en funciones NumPy

**Conceptos clave aprendidos:** ndarray, broadcasting, vectorización, lambdify, SymPy, SciPy, optimización
