# Apéndice A: Instalación y Configuración del Entorno Python

## Instalación de Python

### Opción 1: Python Oficial

1. Descarga Python 3.12+ desde [python.org](https://python.org)
2. Durante la instalación, marca **"Add Python to PATH"**
3. Verifica la instalación:

```bash
python --version
# Python 3.12.x
```

### Opción 2: Anaconda (Recomendada para Análisis de Datos)

1. Descarga Anaconda desde [anaconda.com](https://anaconda.com)
2. Incluye la mayoría de librerías preinstaladas
3. Usa `conda` para gestionar entornos:

```bash
conda create --name motor_cuantitativo python=3.12
conda activate motor_cuantitativo
```

## Instalación de Librerías

### Con pip

```bash
pip install numpy scipy sympy pandas scikit-learn matplotlib seaborn statsmodels
```

### Con conda

```bash
conda install numpy scipy sympy pandas scikit-learn matplotlib seaborn statsmodels
```

### Versiones Mínimas Recomendadas

```python
# Verificar versiones instaladas
import numpy as np
import scipy as sp
import sympy as sym
import pandas as pd
import sklearn as sk
import matplotlib as mpl
import seaborn as sns
import statsmodels as sm

print(f"NumPy:        {np.__version__}")
print(f"SciPy:        {sp.__version__}")
print(f"SymPy:        {sym.__version__}")
print(f"pandas:       {pd.__version__}")
print(f"scikit-learn: {sk.__version__}")
print(f"matplotlib:   {mpl.__version__}")
print(f"seaborn:      {sns.__version__}")
print(f"statsmodels:  {sm.__version__}")
```

## Entornos Virtuales

### Con venv (Librería estándar)

```bash
# Crear entorno
python -m venv motor_cuantitativo

# Activar (Windows)
motor_cuantitativo\Scripts\activate

# Activar (Mac/Linux)
source motor_cuantitativo/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### requirements.txt

Crea este archivo en la raíz de tu proyecto:

```
numpy>=1.24.0
scipy>=1.11.0
sympy>=1.12.0
pandas>=2.0.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
statsmodels>=0.14.0
jupyter>=1.0.0
```

## Configuración de Jupyter

### Instalación

```bash
pip install jupyter
# o
conda install jupyter
```

### Ejecutar

```bash
jupyter notebook
# o
jupyter lab
```

### Extensiones Útiles

```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

## Verificación Completa

Ejecuta este script para verificar que todo funciona correctamente:

```python
# test_setup.py
import numpy as np
from scipy import stats
import sympy as sp
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

print("✅ Todas las librerías se importaron correctamente")

# Prueba NumPy
a = np.array([1, 2, 3])
assert a.sum() == 6
print("✅ NumPy funciona")

# Prueba SciPy
z = stats.norm.ppf(0.975)
assert abs(z - 1.96) < 0.01
print("✅ SciPy funciona")

# Prueba SymPy
x = sp.symbols('x')
assert sp.diff(x**2, x) == 2*x
print("✅ SymPy funciona")

# Prueba pandas
df = pd.DataFrame({'a': [1, 2, 3]})
assert df['a'].sum() == 6
print("✅ pandas funciona")

# Prueba sklearn
X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
model = LinearRegression().fit(X, y)
assert abs(model.coef_[0] - 2.0) < 0.01
print("✅ scikit-learn funciona")

# Prueba matplotlib
fig, ax = plt.subplots()
ax.plot([1, 2, 3])
plt.close()
print("✅ matplotlib funciona")

print("\n🎉 Todo listo para empezar con El Motor Cuantitativo")
```

## Solución de Problemas Comunes

| Problema | Solución |
|----------|----------|
| `pip` no encontrado | Asegúrate de que Python está en el PATH |
| Error de permisos | Usa `pip install --user` o activa el entorno virtual |
| Conflicto de versiones | Usa entornos virtuales |
| `numpy` no encuentra BLAS | Instala desde conda: `conda install numpy` |
| Gráficos matplotlib no se muestran | Ejecuta `plt.show()` en scripts, o usa `%matplotlib inline` en Jupyter |
