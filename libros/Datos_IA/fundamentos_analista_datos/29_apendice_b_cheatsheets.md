# Apéndice B: Cheatsheets

## SQL Cheatsheet

### Consultas básicas
```sql
SELECT col1, col2 FROM tabla;
SELECT * FROM tabla LIMIT 10;
SELECT DISTINCT columna FROM tabla;
```

### Filtros
```sql
WHERE condicion
WHERE col > 100 AND col < 500
WHERE col IN ('A', 'B', 'C')
WHERE col BETWEEN 100 AND 500
WHERE col LIKE '%patron%'
WHERE col IS NULL
WHERE col IS NOT NULL
```

### Ordenación
```sql
ORDER BY col ASC    -- Ascendente (por defecto)
ORDER BY col DESC   -- Descendente
ORDER BY col1, col2 -- Múltiples columnas
```

### Agregación
```sql
GROUP BY col
HAVING condicion   -- Filtrar grupos
COUNT(*), SUM(col), AVG(col), MIN(col), MAX(col)
```

### JOINs
```sql
JOIN tabla2 ON t1.col = t2.col       -- INNER JOIN
LEFT JOIN tabla2 ON t1.col = t2.col  -- LEFT JOIN
RIGHT JOIN tabla2 ON t1.col = t2.col -- RIGHT JOIN
```

### Subconsultas y CTEs
```sql
SELECT * FROM tabla WHERE col IN (SELECT col FROM otra);
WITH cte AS (SELECT ...) SELECT * FROM cte;
```

### Window Functions
```sql
ROW_NUMBER() OVER (PARTITION BY col ORDER BY col)
RANK() OVER (ORDER BY col)
DENSE_RANK() OVER (ORDER BY col)
SUM(col) OVER (PARTITION BY col ORDER BY col)
LAG(col) OVER (ORDER BY col)
LEAD(col) OVER (ORDER BY col)
NTILE(n) OVER (ORDER BY col)
```

## Excel Cheatsheet

### Atajos de teclado
| Atajo | Acción |
|-------|--------|
| Ctrl+T | Crear tabla |
| Ctrl+Shift+L | Activar filtro |
| Ctrl+Shift+1 | Formato número |
| Ctrl+Shift+4 | Formato moneda |
| Ctrl+Shift+5 | Formato porcentaje |
| F4 | Repetir última acción |
| Ctrl+; | Fecha actual |
| Alt+= | Auto suma |

### Fórmulas esenciales
```excel
=SUMA(rango)
=PROMEDIO(rango)
=CONTAR(rango)
=CONTARA(rango)
=CONTAR.SI(rango; criterio)
=SUMAR.SI(rango_criterio; criterio; rango_suma)
=SI(condicion; valor_si; valor_no)
=BUSCARX(valor; rango_busqueda; rango_resultado)
```

### Power Query - Transformaciones
- Promover encabezados
- Cambiar tipo de datos
- Eliminar filas/columnas
- Reemplazar valores
- Dividir columna
- Combinar consultas (Merge)
- Agrupar por
- Columna personalizada

## Python Cheatsheet

### Tipos de datos
```python
int, float, str, bool, None, list, dict, tuple
```

### Operadores
```python
+ - * / // % **   # Aritméticos
== != > < >= <=   # Comparación
and or not         # Lógicos
```

### Strings
```python
f"texto {variable}"  # f-strings
len("texto")
"texto".upper(), .lower(), .strip()
```

### Listas
```python
lista = [1, 2, 3]
lista.append(4)
lista[0], lista[-1], lista[1:3]
len(lista), sum(lista), max(lista), min(lista)
[expr for item in lista if cond]  # List comprehension
```

### Diccionarios
```python
dic = {"clave": "valor"}
dic["clave"], dic.get("clave")
dic.keys(), dic.values(), dic.items()
for k, v in dic.items(): ...
```

### Control de flujo
```python
if cond: ... elif: ... else: ...
for item in lista: ...
for i in range(n): ...
while cond: ...
```

### pandas
```python
import pandas as pd
df = pd.read_csv("archivo.csv")
df = pd.read_sql("query", conn)
df.head(), df.shape, df.dtypes
df[df["col"] > 100]  # Filtro
df.groupby("col").agg({"val": "sum"})  # Agregación
df.sort_values("col", ascending=False)
df.to_excel("output.xlsx", index=False)
```

## Power Pivot / DAX Cheatsheet

```dax
-- Medidas básicas
Ventas = SUM(tabla[columna])
Pedidos = COUNTROWS(tabla)
Clientes = DISTINCTCOUNT(tabla[columna])
Promedio = AVERAGE(tabla[columna])

-- CALCULATE
CALCULATE(medida, condición)

-- Iteración
SUMX(tabla, expresión)
AVERAGEX(tabla, expresión)

-- Tiempo
TOTALYTD(medida, calendario[fecha])
SAMEPERIODLASTYEAR(calendario[fecha])
DIVIDE(numerador, denominador)
```
