# Capítulo 1: Repaso Rápido — Python y pandas para Análisis

## De Python básico a pandas

En el Libro 1 aprendiste Python básico: variables, tipos, listas, diccionarios, funciones y bucles. Ahora vamos a dar el salto a **pandas**, la biblioteca más importante para análisis de datos en Python.

Si necesitas repasar Python básico, revisa el Apéndice B al final de este libro.

## ¿Qué es pandas?

pandas es una biblioteca que proporciona estructuras de datos rápidas y flexibles para trabajar con datos "relacionales" o "etiquetados". Sus dos estructuras principales son:

- **Series**: una columna de datos (como una lista con índice)
- **DataFrame**: una tabla completa (como una hoja de Excel o una tabla SQL)

```python
import pandas as pd
import numpy as np

print(f"pandas versión: {pd.__version__}")
print(f"numpy versión: {np.__version__}")
```

## Tu primer DataFrame

```python
import pandas as pd

# Desde un diccionario
data = {
    "producto": ["Portátil Pro", "Smartphone Air", "Tablet Max"],
    "precio": [1299.99, 899.99, 499.99],
    "stock": [50, 120, 80],
    "categoria": ["Portátiles", "Smartphones", "Tablets"],
}
df = pd.DataFrame(data)
print(df)
```

```
       producto   precio  stock     categoria
0  Portátil Pro  1299.99     50    Portátiles
1  Smartphone Air  899.99    120  Smartphones
2     Tablet Max  499.99     80       Tablets
```

### Desde CSV

```python
df = pd.read_csv("codigos/datos_ventas.csv")
print(df.head())  # Primeras 5 filas
```

## Exploración rápida de un DataFrame

```python
# Dimensiones
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

# Información de columnas y tipos
print(df.info())

# Estadísticas descriptivas
print(df.describe())

# Nombres de columnas
print(df.columns.tolist())

# Valores únicos en una columna
print(df["region"].unique())
print(df["region"].value_counts())
```

## Selección de datos

```python
# Seleccionar una columna (devuelve una Serie)
totales = df["total"]

# Seleccionar múltiples columnas
df[["order_id", "total", "region"]]

# Filtrar filas
df[df["total"] > 1000]
df[df["region"] == "Madrid"]
df[(df["total"] > 500) & (df["region"] == "Cataluña")]

# Seleccionar por posición: .iloc
df.iloc[0]        # Primera fila
df.iloc[1:5]      # Filas 1 a 4
df.iloc[:, 0:3]   # Columnas 0 a 2

# Seleccionar por etiqueta: .loc
df.loc[df["region"] == "Madrid", ["order_id", "total"]]
```

## Trabajar con columnas

```python
# Crear nueva columna
df["año"] = pd.to_datetime(df["order_date"]).dt.year
df["mes"] = pd.to_datetime(df["order_date"]).dt.month
df["ingreso_con_iva"] = df["total"] * 1.21

# Renombrar columnas
df = df.rename(columns={"total": "importe_total"})

# Eliminar columnas
df.drop(columns=["customer_name"], inplace=True)

# Reordenar columnas
df = df[["order_id", "order_date", "region", "total"]]
```

## Valores nulos

```python
# Detectar nulos
print(df.isnull().sum())

# Eliminar filas con nulos
df_sin_nulos = df.dropna()

# Rellenar nulos
df["employee_name"] = df["employee_name"].fillna("Sin asignar")
df["total"] = df["total"].fillna(0)
```

## Guardar datos

```python
# A CSV
df.to_csv("datos_limpios.csv", index=False)

# A Excel
df.to_excel("datos_limpios.xlsx", index=False, sheet_name="Ventas")

# A JSON
df.to_json("datos_limpios.json", orient="records")
```

## Ejercicios del Capítulo 1

1. Importa pandas y numpy. Lee `datos_ventas.csv` en un DataFrame.
2. Muestra las primeras 10 filas, la información del DataFrame y las estadísticas descriptivas.
3. ¿Cuántas filas y columnas tiene el DataFrame?
4. Filtra solo los pedidos de la región "Madrid" con total > 500.
5. Crea una columna "año" a partir de "order_date".
6. ¿Cuántos valores nulos hay en cada columna?
7. Agrupa por región y calcula el total de ventas (usa `groupby`).
8. Ordena el DataFrame por total descendente.
9. Guarda los pedidos completados en un archivo CSV separado.
10. Calcula el precio promedio por región usando `groupby`.

## Checklist de autoevaluación

- [ ] Sé crear un DataFrame desde un diccionario y desde CSV
- [ ] Sé explorar un DataFrame con head, info, describe
- [ ] Sé seleccionar columnas y filtrar filas
- [ ] Sé crear y eliminar columnas
- [ ] Sé manejar valores nulos
- [ ] Sé guardar datos a CSV, Excel y JSON
