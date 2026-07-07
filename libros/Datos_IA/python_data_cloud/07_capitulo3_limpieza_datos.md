# Capítulo 3: Limpieza de Datos Reales

## El 80% del trabajo del analista

En el mundo real, los datos nunca llegan limpios. Vienen con:
- Valores nulos donde no debería haberlos
- Formatos inconsistentes (fechas, monedas, texto)
- Duplicados
- Valores atípicos (outliers)
- Errores de tipeo o carga

Este capítulo te enseña a detectar y solucionar cada problema.

## Cargar datos sucios

Vamos a crear un dataset con problemas reales para practicar:

```python
import pandas as pd
import numpy as np

# Dataset con problemas
data = {
    "cliente_id": [1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
    "nombre": ["Ana García", "Luis Pérez", "María López", "Juan Martínez",
               None, "Carlos Ruiz", "Elena Sánchez", "Pedro Gómez", None, "Sofía Díaz"],
    "email": ["ana@email.com", "luis@email", "maria@email.com", None,
              "carlos@email.com", "carlos@email.com", "elena@email.com",
              "pedro@email.com", None, "sofia@email.com"],
    "fecha_registro": ["2024-01-15", "2024/03/20", "15-01-2024", "2024-06-01",
                       "2024-07-01", "2024-07-01", "2024-08-15", "2024-09-01",
                       "enero 2025", "2024-11-15"],
    "gasto_total": [1250.50, 899.99, None, 450.00, 2300.00, 2300.00, -50.00, 999999, 350.00, 780.00],
    "edad": [32, 28, None, 45, 38, 38, 200, 29, 42, 31],
}

df = pd.DataFrame(data)
print("DATOS CRUDOS:")
print(df)
print(f"\nDimensiones: {df.shape}")
```

## 1. Valores nulos (missing data)

```python
# Detectar nulos
print("Nulos por columna:")
print(df.isnull().sum())
print(f"\nTotal nulos: {df.isnull().sum().sum()}")
print(f"% nulos por columna:\n{df.isnull().mean() * 100}")
```

### Estrategias para manejar nulos

```python
# 1. Eliminar filas con nulos (si son pocos)
df_sin_nulos = df.dropna()

# 2. Eliminar columnas con demasiados nulos
df = df.drop(columns=["nombre"])  # Si la columna no es crítica

# 3. Rellenar con un valor constante
df["nombre"] = df["nombre"].fillna("Cliente desconocido")
df["email"] = df["email"].fillna("sin-email@pendiente.com")

# 4. Rellenar con la media o mediana
df["gasto_total"] = df["gasto_total"].fillna(df["gasto_total"].median())

# 5. Rellenar con el valor anterior (forward fill)
df["edad"] = df["edad"].fillna(method="ffill")
```

## 2. Duplicados

```python
# Detectar duplicados
print(f"Filas duplicadas: {df.duplicated().sum()}")
print(f"Filas duplicadas (por cliente_id): {df.duplicated(subset=['cliente_id']).sum()}")

# Ver duplicados
print(df[df.duplicated(subset=["cliente_id"], keep=False)])

# Eliminar duplicados
df = df.drop_duplicates(subset=["cliente_id"], keep="first")
print(f"Después de limpiar duplicados: {len(df)} filas")
```

## 3. Formatos inconsistentes

### Fechas

```python
# Intentar convertir a datetime (detecta errores)
df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")
print("Fechas después de conversión:")
print(df["fecha_registro"].head(10))

# Las fechas que no pudo convertir se vuelven NaT (Not a Time)
print(f"Fechas inválidas: {df['fecha_registro'].isna().sum()}")
```

### Texto

```python
# Limpiar texto
df["nombre"] = df["nombre"].str.strip()  # Quitar espacios
df["email"] = df["email"].str.strip().str.lower()

# Validar emails (que contengan @ y .)
emails_validos = df["email"].str.contains(r"^[^@]+@[^@]+\.[^@]+$", na=False)
print(f"Emails inválidos: {(~emails_validos).sum()}")
df["email"] = df["email"].where(emails_validos, "email-invalido@corregir.com")
```

## 4. Valores atípicos (outliers)

```python
# Detectar outliers con el rango intercuartílico (IQR)
Q1 = df["gasto_total"].quantile(0.25)
Q3 = df["gasto_total"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Límite inferior: {limite_inferior:.2f}")
print(f"Límite superior: {limite_superior:.2f}")

outliers = df[(df["gasto_total"] < limite_inferior) | (df["gasto_total"] > limite_superior)]
print(f"Outliers detectados: {len(outliers)}")
print(outliers[["cliente_id", "gasto_total"]])

# Manejo de outliers:
# Opción 1: Eliminar
df = df[(df["gasto_total"] >= limite_inferior) & (df["gasto_total"] <= limite_superior)]

# Opción 2: Limitar (capping)
df["gasto_total"] = df["gasto_total"].clip(lower=0, upper=df["gasto_total"].quantile(0.95))

# Opción 3: Reemplazar con la mediana
mediana = df["gasto_total"].median()
df.loc[df["gasto_total"] > limite_superior, "gasto_total"] = mediana
```

## Pipeline de limpieza completo

```python
def limpiar_ventas(df):
    """Pipeline completo de limpieza"""
    df = df.copy()
    
    # 1. Eliminar duplicados
    df = df.drop_duplicates(subset=["order_id"])
    
    # 2. Convertir fechas
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    
    # 3. Eliminar filas con fecha inválida
    df = df.dropna(subset=["order_date"])
    
    # 4. Rellenar nulos en columnas de texto
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna("Sin dato")
    
    # 5. Rellenar nulos en columnas numéricas con la mediana
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())
    
    # 6. Eliminar outliers en total
    Q1 = df["total"].quantile(0.25)
    Q3 = df["total"].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df["total"] >= Q1 - 1.5 * IQR) & (df["total"] <= Q3 + 1.5 * IQR)]
    
    # 7. Estandarizar texto
    df["region"] = df["region"].str.strip().str.title()
    
    return df

# Aplicar pipeline
ventas_limpias = limpiar_ventas(pd.read_csv("codigos/datos_ventas.csv"))
print(f"Antes: 6000 filas | Después: {len(ventas_limpias)} filas")
```

## Ejercicios del Capítulo 3

1. Carga el dataset de ejemplo con problemas (data del inicio del capítulo).
2. Identifica cuántos valores nulos hay en cada columna.
3. Decide qué estrategia usarías para cada columna con nulos y aplícala.
4. Encuentra y elimina filas duplicadas por cliente_id.
5. Corrige las fechas con formato inconsistente.
6. Detecta outliers en gasto_total usando IQR y explícalos.
7. ¿Por qué una edad de 200 años es un outlier? ¿Qué harías con ella?
8. Crea una función `limpiar_clientes()` que limpie el dataset de clientes.
9. Aplica el pipeline de limpieza al archivo `datos_ventas.csv` real.
10. Guarda el resultado limpio en un nuevo archivo CSV.

## Checklist de autoevaluación

- [ ] Sé detectar y manejar valores nulos
- [ ] Sé identificar y eliminar duplicados
- [ ] Sé limpiar formatos inconsistentes (fechas, texto)
- [ ] Sé detectar outliers con IQR
- [ ] Sé crear un pipeline de limpieza reutilizable
- [ ] Entiendo que la limpieza es específica para cada dataset
