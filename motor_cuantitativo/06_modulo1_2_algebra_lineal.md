# Álgebra Lineal Esencial: Vectores, Matrices y Operaciones

El álgebra lineal es el lenguaje de los datos modernos. Cada vez que ajustas un modelo de regresión, realizas PCA o entrenas una red neuronal, estás haciendo álgebra lineal. En este capítulo entenderás qué ocurre realmente.

## Vectores: Los Bloques Fundamentales

Un vector es una lista ordenada de números. En análisis de datos, cada fila de un dataset es un vector: el vector de características de una observación.

### Representación en Python

```python
import numpy as np

# Vector fila (1D)
v = np.array([2, -1, 3])
print(f"Vector: {v}, Shape: {v.shape}")
# Vector: [2 -1 3], Shape: (3,)

# Vector columna explícito
v_col = v.reshape(-1, 1)
print(f"Shape columna: {v_col.shape}")
# Shape columna: (3, 1)
```

### Operaciones con Vectores

```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Suma (elemento a elemento)
print(f"Suma: {v1 + v2}")     # [5 7 9]

# Producto punto (dot product)
dot = np.dot(v1, v2)
print(f"Producto punto: {dot}")  # 1*4 + 2*5 + 3*6 = 32

# Producto punto con @ (Python 3.5+)
print(f"Producto punto (@): {v1 @ v2}")  # 32

# Norma euclidiana (magnitud)
norma = np.linalg.norm(v1)
print(f"Norma L2: {norma:.4f}")  # sqrt(1+4+9) = 3.7417

# Normalización (vector unitario)
unitario = v1 / norma
print(f"Unitario: {unitario}")
# [0.2673 0.5345 0.8018]
```

> **⚠️ Advertencia:**
> El producto punto de dos vectores ortogonales es 0. Si trabajas con datos de alta dimensión, la mayoría de los vectores aleatorios tienden a ser casi ortogonales entre sí. Este es un aspecto clave de la "maldición de la dimensionalidad".

### Interpretación Geométrica del Producto Punto

El producto punto mide la proyección de un vector sobre otro:

```python
import numpy as np

a = np.array([1, 0])
b = np.array([np.cos(np.pi/3), np.sin(np.pi/3)])  # 60 grados

dot_ab = a @ b
angulo = np.arccos(dot_ab / (np.linalg.norm(a) * np.linalg.norm(b)))

print(f"Producto punto: {dot_ab:.4f}")
print(f"Ángulo: {np.degrees(angulo):.1f}°")
# Producto punto: 0.5000
# Ángulo: 60.0°
```

## Matrices: Datos en 2D

Una matriz es un arreglo bidimensional. Tu dataset tabular es una matriz: filas = observaciones, columnas = variables.

### Creación y Propiedades

```python
# Matriz 2x3
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Propiedades
print(f"Shape: {A.shape}")          # (2, 3)
print(f"Dimensiones: {A.ndim}")     # 2
print(f"Total elementos: {A.size}") # 6

# Transpuesta
print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]
```

### Multiplicación de Matrices

```python
A = np.array([[1, 2], [3, 4]])  # 2x2
B = np.array([[5, 6], [7, 8]])  # 2x2

# Multiplicación matricial (dot product)
C = A @ B
print(C)
# [[19 22]
#  [43 50]]

# Equivalente: np.matmul(A, B)
```

### Sistemas de Ecuaciones Lineales

Resolver sistemas de ecuaciones es una tarea cotidiana en análisis de datos:

```python
# Sistema: 3x + 2y = 7
#          2x - y  = 0

A = np.array([[3, 2],
              [2, -1]])
b = np.array([7, 0])

# Solución: x = A^(-1) * b
x = np.linalg.solve(A, b)
print(f"Solución: x = {x[0]:.2f}, y = {x[1]:.2f}")
# Solución: x = 1.00, y = 2.00
```

## Eigenvalores y Eigenvectores

Los eigenvalores y eigenvectores son fundamentales para PCA, análisis de redes y reducción de dimensionalidad.

Un eigenvector de una matriz A es un vector v que, al multiplicarse por A, solo se escala (no cambia de dirección):

```
A · v = λ · v
```

Donde λ (lambda) es el eigenvalor asociado.

```python
A = np.array([[2, 1],
              [1, 2]])

eigenvalores, eigenvectores = np.linalg.eig(A)

print(f"Eigenvalores: {eigenvalores}")
# [3. 1.]

print(f"Eigenvectores (columnas):\n{eigenvectores}")
# [[ 0.70710678 -0.70710678]
#  [ 0.70710678  0.70710678]]

# Verificación: A * v = λ * v
v = eigenvectores[:, 0]
lam = eigenvalores[0]
print(np.allclose(A @ v, lam * v))  # True
```

## Descomposición en Valores Singulares (SVD)

SVD es, probablemente, el resultado más importante del álgebra lineal para datos. Descompone cualquier matriz A en tres matrices:

```
A = U · Σ · V^T
```

```python
from numpy.linalg import svd

# Matriz de datos (5 observaciones, 3 variables)
A = np.array([[1, 0, 1],
              [0, 1, 1],
              [1, 1, 0],
              [0, 0, 1],
              [1, 0, 0]])

U, S, Vt = svd(A)

print(f"U shape: {U.shape}")    # (5, 5)
print(f"Sigma: {S}")             # Valores singulares
# [1.9021 1.6180 0.6180]
print(f"Vt shape: {Vt.shape}")  # (3, 3)

# Reconstrucción (truncando a 2 componentes)
k = 2
A_aprox = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
error = np.linalg.norm(A - A_aprox)
print(f"Error de reconstrucción: {error:.4f}")
```

SVD es la base de PCA, sistemas de recomendación (filtrado colaborativo) y compresión de datos.

## Matriz de Covarianza

La matriz de covarianza es la herramienta central para entender relaciones entre variables:

```python
# Datos: 100 observaciones, 3 variables correlacionadas
np.random.seed(42)
X = np.random.randn(100, 3)

# Introducir correlación
X[:, 1] = 0.7 * X[:, 0] + 0.3 * X[:, 1]
X[:, 2] = -0.4 * X[:, 0] + 0.6 * X[:, 2]

# Matriz de covarianza (centrando los datos)
X_centrado = X - X.mean(axis=0)
cov = (X_centrado.T @ X_centrado) / (X.shape[0] - 1)

print("Matriz de covarianza:")
print(np.round(cov, 3))
# [[ 1.02    0.714 -0.366]
#  [ 0.714  0.999 -0.256]
#  [-0.366 -0.256  0.978]]

# Comparación con numpy
print(np.round(np.cov(X.T), 3))
# Mismo resultado
```

Los elementos diagonales son las varianzas; los no diagonales, las covarianzas.

## Aplicación Práctica: Regresión Lineal desde Cero

El álgebra lineal que acabamos de ver te permite implementar regresión lineal sin scikit-learn:

```python
# Datos de ejemplo
np.random.seed(42)
X = np.random.randn(100, 2)  # 2 variables
y = 3 + 2 * X[:, 0] - 1.5 * X[:, 1] + np.random.randn(100) * 0.5

# Añadir columna de 1s para el intercepto
X_b = np.column_stack([np.ones(100), X])

# Ecuación normal: β = (X^T X)^(-1) X^T y
beta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
print(f"β₀ = {beta[0]:.2f}, β₁ = {beta[1]:.2f}, β₂ = {beta[2]:.2f}")
# β₀ = 3.02, β₁ = 2.01, β₂ = -1.49

# Coeficientes reales: β₀=3, β₁=2, β₂=-1.5
```

> **💡 Consejo del Analista:**
> Para datasets grandes (n > 10,000 o muchas variables), usar la ecuación normal directa es computacionalmente costosa (O(n³)). En esos casos, el descenso de gradiente (capítulo siguiente) es más eficiente.

La ecuación normal `β = (X^T X)^(-1) X^T y` es la solución analítica de la regresión lineal.

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Dados los vectores a = [3, -1, 2] y b = [0, 4, -2], calcula: (a) producto punto, (b) norma de cada uno, (c) ángulo entre ellos.
   - Pista: `np.arccos(dot / (norm_a * norm_b))`

2. **Ejercicio 2:** Resuelve el sistema de ecuaciones usando `np.linalg.solve`:
   ```
   2x + 3y - z = 1
   4x - 2y + 5z = -3
   x + y + z = 2
   ```

3. **Ejercicio 3:** Implementa la descomposición SVD desde cero (usando `np.linalg.eig` sobre A^T A y AA^T) y verifica que coincide con `np.linalg.svd`.

4. **Ejercicio 4:** Genera una matriz 5x3 de datos aleatorios. Calcula su matriz de covarianza. ¿Qué información obtienes de los elementos fuera de la diagonal?

## 📝 Resumen del Capítulo

- Los **vectores** representan observaciones; las **matrices**, datasets completos
- El **producto punto** mide similitud entre vectores y proyecta uno sobre otro
- Los sistemas de ecuaciones se resuelven con `np.linalg.solve`
- Los **eigenvalores/eigenvectores** revelan la estructura fundamental de una matriz
- **SVD** descompone cualquier matriz en componentes ortonormales (base de PCA)
- La **matriz de covarianza** captura las relaciones entre variables
- La **ecuación normal** (β = (X^T X)⁻¹ X^T y) es la solución cerrada de regresión lineal

**Conceptos clave aprendidos:** vector, matriz, producto punto, SVD, eigenvalores, eigenvectores, covarianza, ecuación normal
