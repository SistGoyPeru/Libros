# Capítulo 14: Python — Funciones y Módulos

## Funciones: reutilizar código

Una función es un bloque de código reutilizable. En lugar de escribir lo mismo varias veces, defines la función una vez y la llamas cuando la necesites.

```python
def calcular_ingresos(precio, cantidad):
    return precio * cantidad

# Usar la función
total = calcular_ingresos(1299.99, 3)
print(f"Ingresos: {total:.2f}€")
```

### Parámetros y argumentos

```python
def calcular_margen(precio_venta, precio_coste, iva=0.21):
    """
    Calcula el margen de beneficio de un producto.
    
    Args:
        precio_venta: Precio de venta sin IVA
        precio_coste: Coste del producto
        iva: Tasa de IVA (por defecto 21%)
    
    Returns:
        Diccionario con márgenes
    """
    precio_con_iva = precio_venta * (1 + iva)
    margen_bruto = precio_venta - precio_coste
    margen_porcentaje = (margen_bruto / precio_venta) * 100
    
    return {
        "precio_sin_iva": precio_venta,
        "precio_con_iva": round(precio_con_iva, 2),
        "coste": precio_coste,
        "margen_bruto": round(margen_bruto, 2),
        "margen_pct": round(margen_porcentaje, 1)
    }

# Llamar con argumentos posicionales
resultado = calcular_margen(1299.99, 850.00)
print(resultado)

# Llamar con argumentos nombrados (más legible)
resultado = calcular_margen(precio_venta=1299.99, precio_coste=850.00, iva=0.10)
```

### Parámetros por defecto y return múltiple

```python
def analizar_ventas(ingresos, gastos, impuestos=0.25):
    beneficio = ingresos - gastos
    beneficio_neto = beneficio * (1 - impuestos)
    margen = (beneficio / ingresos) * 100
    
    return beneficio, beneficio_neto, margen

b, bn, m = analizar_ventas(1250000, 875000)
print(f"Beneficio: {b:,.2f}€")
print(f"Beneficio neto: {bn:,.2f}€")
print(f"Margen: {m:.1f}%")
```

## Módulos: organizar el código

Un módulo es un archivo `.py` que contiene funciones y variables. Puedes importarlo desde otros archivos.

### Importar módulos

```python
# Importar un módulo completo
import math
print(math.sqrt(144))  # 12.0

# Importar funciones específicas
from math import sqrt, pi
print(sqrt(144))  # 12.0
print(pi)  # 3.14159...

# Importar con alias
import math as m
print(m.sqrt(144))
```

### Módulos útiles para análisis de datos

```python
import math      # Operaciones matemáticas
import random    # Números aleatorios
import datetime  # Fechas y horas
import csv       # Leer/escribir CSV
import json      # Leer/escribir JSON
import os        # Operaciones del sistema
```

## Trabajar con fechas (datetime)

```python
from datetime import datetime, date, timedelta

# Fecha actual
hoy = date.today()
print(f"Hoy: {hoy}")

# Fecha específica
inicio = date(2024, 1, 1)
print(f"Inicio: {inicio}")

# Diferencia entre fechas
dias_transcurridos = (hoy - inicio).days
print(f"Días desde inicio: {dias_transcurridos}")

# Sumar días
dentro_de_30 = hoy + timedelta(days=30)
print(f"Dentro de 30 días: {dentro_de_30}")

# Parsear strings a fechas
fecha_str = "2024-03-15"
fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
print(f"Parseada: {fecha}")

# Formatear fechas a strings
print(fecha.strftime("%d/%m/%Y"))  # 15/03/2024
print(fecha.strftime("%B %Y"))     # March 2024
```

## Trabajar con archivos

### Leer CSV manualmente

```python
import csv

with open("codigos/datos_ventas.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    ventas = list(reader)

print(f"Total registros: {len(ventas)}")
print(f"Primera venta: {ventas[0]}")

# Calcular total de ventas
total = sum(float(v["total"]) for v in ventas)
print(f"Total ventas: {total:,.2f}€")
```

### Escribir CSV

```python
with open("resumen.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto", "Unidades", "Ingresos"])
    writer.writerow(["Portátil Pro", 145, 188500])
    writer.writerow(["Smartphone Air", 198, 178200])
```

## Crear tu propio módulo

Crea un archivo `analizador.py`:

```python
# analizador.py
def calcular_ingresos(precio, cantidad):
    return precio * cantidad

def calcular_margen(venta, coste):
    return (venta - coste) / venta * 100

def clasificar_producto(precio):
    if precio > 1000:
        return "Gama alta"
    elif precio > 300:
        return "Gama media"
    else:
        return "Gama baja"
```

Luego úsalo desde otro archivo:

```python
from analizador import calcular_ingresos, clasificar_producto

ingresos = calcular_ingresos(1299.99, 5)
print(f"Ingresos: {ingresos:.2f}€")

gama = clasificar_producto(1299.99)
print(f"Clasificación: {gama}")
```

## Ejercicios del Capítulo 14

1. Crea una función `calcular_iva(precio, tasa=0.21)` que devuelva el precio con IVA.
2. Crea una función `resumen_ventas(ventas_lista)` que reciba una lista de totales y devuelva un diccionario con: total, promedio, máximo, mínimo, conteo.
3. Usa el módulo `datetime` para calcular cuántos días han pasado entre dos fechas.
4. Lee el archivo `datos_ventas.csv` y calcula las ventas totales por región usando un diccionario.
5. Crea tu propio módulo `metricas.py` con funciones de análisis (media, mediana, desviación).
6. Usa el módulo `random` para simular 10 ventas diarias de un producto.
7. Escribe un archivo CSV con los resultados del ejercicio 4.
8. Crea una función que reciba un nombre de archivo CSV y devuelva las primeras 5 filas.
9. Usa `datetime` para calcular la edad de un cliente basada en su fecha de registro.
10. Crea una función `generar_reporte(archivo_csv)` que lea un CSV, calcule métricas y las muestre formateadas.

## Checklist de autoevaluación

- [ ] Sé definir funciones con def
- [ ] Sé usar parámetros, argumentos y return
- [ ] Sé usar parámetros por defecto
- [ ] Sé importar módulos estándar (math, datetime, csv)
- [ ] Sé leer y escribir archivos CSV
- [ ] Sé crear y usar mis propios módulos
- [ ] Sé escribir docstrings para documentar funciones
