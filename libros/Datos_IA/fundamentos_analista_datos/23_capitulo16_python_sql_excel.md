# Capítulo 16: Python + SQL + Excel — La Integración Total

## El flujo completo del analista

En proyectos reales, un analista combina las tres herramientas en un flujo de trabajo:

```
SQL  ─── Extraer datos de la base de datos
  │
  ▼
Python ── Limpiar, transformar y analizar
  │
  ▼
Excel ─── Visualizar y presentar resultados
```

En este capítulo aprenderás a conectar estas herramientas.

## Conectar Python con SQLite

```python
import sqlite3
import csv
from datetime import datetime

# Conectar a la base de datos
conn = sqlite3.connect("codigos/techstore.db")
conn.row_factory = sqlite3.Row  # Permite acceder por nombre de columna

# Ejecutar consulta
cursor = conn.execute("""
    SELECT c.region,
           strftime('%Y-%m', o.order_date) AS mes,
           COUNT(DISTINCT o.id) AS pedidos,
           ROUND(SUM(o.total), 2) AS ingresos
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    WHERE o.status = 'Completado'
    GROUP BY c.region, mes
    ORDER BY c.region, mes
""")

# Leer resultados
filas = cursor.fetchall()
print(f"Total filas: {len(filas)}")
print(f"Columnas: {[desc[0] for desc in cursor.description]}")

# Convertir a lista de diccionarios
resultados = [dict(fila) for fila in filas]

# Mostrar primeras 5
for r in resultados[:5]:
    print(r)

conn.close()
```

## pandas: la biblioteca estrella

pandas es la biblioteca más importante para análisis de datos en Python. Trabaja con DataFrames (tablas en memoria).

```python
# pip install pandas
import pandas as pd

# Leer CSV directamente
df = pd.read_csv("codigos/datos_ventas.csv")
print(df.head())        # Primeras 5 filas
print(df.shape)         # Dimensiones (filas, columnas)
print(df.dtypes)        # Tipos de datos

# Leer SQL directamente
conn = sqlite3.connect("codigos/techstore.db")
df_ventas = pd.read_sql("""
    SELECT o.*, c.region, c.city
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
""", conn)
conn.close()

print(df_ventas.head())
```

### Operaciones básicas con pandas

```python
# Filtros
df_madrid = df_ventas[df_ventas["region"] == "Madrid"]
df_caros = df_ventas[df_ventas["total"] > 1000]

# Agrupación
resumen = df_ventas.groupby("region").agg(
    pedidos=("id", "count"),
    ingresos=("total", "sum"),
    ticket_promedio=("total", "mean")
).reset_index()

print(resumen)

# Ordenar
resumen = resumen.sort_values("ingresos", ascending=False)

# Añadir columna calculada
df_ventas["año"] = pd.to_datetime(df_ventas["order_date"]).dt.year
df_ventas["mes"] = pd.to_datetime(df_ventas["order_date"]).dt.month
```

## Exportar de Python a Excel

```python
# Crear un archivo Excel con múltiples hojas
with pd.ExcelWriter("reporte_techstore.xlsx", engine="openpyxl") as writer:
    # Hoja 1: Resumen por región
    resumen.to_excel(writer, sheet_name="Resumen Regiones", index=False)
    
    # Hoja 2: Top productos
    df_detalles = pd.read_csv("codigos/datos_detalles_ventas.csv")
    top_productos = df_detalles.groupby("product_name").agg(
        unidades=("quantity", "sum"),
        ingresos=("line_total", "sum")
    ).sort_values("unidades", ascending=False).head(20).reset_index()
    top_productos.to_excel(writer, sheet_name="Top Productos", index=False)
    
    # Hoja 3: Ventas mensuales
    df_ventas["order_date"] = pd.to_datetime(df_ventas["order_date"])
    df_ventas["mes"] = df_ventas["order_date"].dt.to_period("M")
    mensual = df_ventas.groupby("mes").agg(
        pedidos=("id", "count"),
        ingresos=("total", "sum")
    ).reset_index()
    mensual["mes"] = mensual["mes"].astype(str)
    mensual.to_excel(writer, sheet_name="Ventas Mensuales", index=False)

print("Reporte Excel generado: reporte_techstore.xlsx")
```

## Script completo: pipeline automatizado

```python
"""
pipeline_analisis.py
Pipeline completo de análisis: SQL → pandas → Excel
"""
import sqlite3
import pandas as pd
from datetime import datetime

def extraer_datos(db_path):
    """Extraer datos de SQLite"""
    conn = sqlite3.connect(db_path)
    
    query = """
        SELECT o.id AS order_id, o.order_date, o.status, o.total,
               c.first_name || ' ' || c.last_name AS cliente,
               c.region, c.city,
               e.first_name || ' ' || e.last_name AS vendedor
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        JOIN employees e ON o.employee_id = e.id
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def transformar_datos(df):
    """Limpiar y transformar"""
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["año"] = df["order_date"].dt.year
    df["mes"] = df["order_date"].dt.month
    df["día_semana"] = df["order_date"].dt.day_name()
    return df

def generar_reportes(df, output_path):
    """Generar reportes Excel"""
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        # Ventas por región
        df[df["status"] == "Completado"].groupby("region").agg(
            pedidos=("order_id", "count"),
            ingresos=("total", "sum"),
            ticket_promedio=("total", "mean")
        ).sort_values("ingresos", ascending=False).to_excel(
            writer, sheet_name="Por Región", index=True
        )
        
        # Ventas por año-mes
        df[df["status"] == "Completado"].groupby(
            df["order_date"].dt.to_period("M")
        ).agg(
            pedidos=("order_id", "count"),
            ingresos=("total", "sum")
        ).to_excel(writer, sheet_name="Tendencia Mensual", index=True)
        
        # Top 10 vendedores
        df[df["status"] == "Completado"].groupby("vendedor").agg(
            pedidos=("order_id", "count"),
            ingresos=("total", "sum")
        ).sort_values("ingresos", ascending=False).head(10).to_excel(
            writer, sheet_name="Top Vendedores", index=True
        )

if __name__ == "__main__":
    print("=== Pipeline de Análisis TechStore ===")
    print("Extrayendo datos...")
    df = extraer_datos("codigos/techstore.db")
    print(f"  {len(df)} registros extraídos")
    
    print("Transformando datos...")
    df = transformar_datos(df)
    
    print("Generando reportes...")
    output = f"reporte_techstore_{datetime.now().strftime('%Y%m%d')}.xlsx"
    generar_reportes(df, output)
    print(f"  Reporte generado: {output}")
    print("¡Pipeline completado!")
```

## Ejercicios del Capítulo 16

1. Conecta Python a la base de datos TechStore y extrae todos los clientes.
2. Usa pandas para leer `datos_ventas.csv` y muestra las primeras 10 filas.
3. Calcula el total de ventas por región usando pandas groupby.
4. Exporta el resultado del ejercicio 3 a un archivo Excel.
5. Crea un script que lea datos de SQLite, los transforme y los guarde en Excel.
6. Usa pandas para filtrar pedidos con total > 500 y cuenta cuántos hay.
7. Añade una columna "trimestre" a un DataFrame de ventas.
8. Exporta un Excel con 3 hojas: resumen general, top clientes, y ventas mensuales.
9. Crea una función que reciba una consulta SQL y devuelva un DataFrame.
10. Combina datos de ventas y productos usando pandas merge (equivalente a JOIN).

## Checklist de autoevaluación

- [ ] Sé conectar Python con SQLite usando sqlite3
- [ ] Sé usar pandas para leer CSV y SQL
- [ ] Sé filtrar, agrupar y ordenar con pandas
- [ ] Sé exportar DataFrames a Excel con múltiples hojas
- [ ] Sé crear un pipeline automatizado SQL → pandas → Excel
- [ ] Entiendo el flujo de trabajo completo del analista
