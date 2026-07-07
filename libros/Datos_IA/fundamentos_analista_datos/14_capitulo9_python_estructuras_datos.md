# Capítulo 9: Python — Estructuras de Datos y Control de Flujo

## Listas: colecciones ordenadas

Una lista es una secuencia ordenada de elementos. Se crea con corchetes `[]`.

```python
# Lista de productos
productos = ["Portátil Pro", "Smartphone Air", "Tablet Max", "Auriculares Ultra"]
print(productos[0])    # Portátil Pro (índice 0)
print(productos[-1])   # Auriculares Ultra (último)
print(productos[1:3])  # ["Smartphone Air", "Tablet Max"] (slicing)
```

### Operaciones con listas

```python
ventas_mensuales = [45000, 52000, 48000, 55000, 61000, 58000]

# Añadir elementos
ventas_mensuales.append(62000)

# Insertar en posición específica
ventas_mensuales.insert(0, 43000)  # Insertar al inicio

# Eliminar elementos
ventas_mensuales.remove(48000)  # Eliminar por valor
ultimo = ventas_mensuales.pop()  # Eliminar y devolver el último

# Longitud
print(len(ventas_mensuales))

# Suma, máximo, mínimo
print(sum(ventas_mensuales))
print(max(ventas_mensuales))
print(min(ventas_mensuales))

# Ordenar
ventas_mensuales.sort(reverse=True)  # Descendente
```

## Diccionarios: pares clave-valor

Un diccionario almacena datos en pares `clave: valor`. Se crea con llaves `{}`.

```python
# Diccionario de un producto
producto = {
    "nombre": "Portátil Pro",
    "precio": 1299.99,
    "stock": 50,
    "categoria": "Portátiles"
}

# Acceder a valores
print(producto["nombre"])   # Portátil Pro
print(producto.get("precio"))  # 1299.99 (seguro, no da error si falta)

# Modificar valores
producto["precio"] = 1199.99
producto["stock"] -= 1  # Vender una unidad

# Añadir nuevas claves
producto["proveedor"] = "TechSupply S.L."

# Recorrer diccionario
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
```

### Lista de diccionarios (estructura típica de datos)

```python
productos = [
    {"nombre": "Portátil Pro", "precio": 1299.99, "stock": 50},
    {"nombre": "Smartphone Air", "precio": 899.99, "stock": 120},
    {"nombre": "Tablet Max", "precio": 499.99, "stock": 80},
]

# Calcular valor total del inventario
valor_total = 0
for p in productos:
    valor_total += p["precio"] * p["stock"]
print(f"Valor inventario: {valor_total:,.2f}€")
```

## Condicionales: if/elif/else

```python
stock = 5

if stock == 0:
    print("Producto agotado")
elif stock <= 10:
    print(f"Stock bajo: {stock} unidades")
elif stock <= 50:
    print(f"Stock normal: {stock} unidades")
else:
    print(f"Stock alto: {stock} unidades")
```

## Bucles: for y while

### for: iterar sobre colecciones

```python
productos = ["Portátil", "Smartphone", "Tablet"]
precios = [1299.99, 899.99, 499.99]

for i in range(len(productos)):
    print(f"{productos[i]}: {precios[i]}€")

# Más pythonico: zip
for producto, precio in zip(productos, precios):
    print(f"{producto}: {precio}€")
```

### while: repetir mientras se cumpla una condición

```python
stock = 50
while stock > 0:
    # Simular venta
    stock -= 1
    print(f"Vendido. Stock restante: {stock}")

print("Producto agotado")
```

## Comprensión de listas (list comprehension)

Forma concisa de crear listas:

```python
# Duplicar precios (versión normal)
precios = [100, 200, 300]
precios_doble = []
for p in precios:
    precios_doble.append(p * 2)

# Mismo resultado con comprensión de listas
precios_doble = [p * 2 for p in precios]

# Filtrar productos caros
precios = [100, 500, 50, 1000, 200, 800]
caros = [p for p in precios if p > 500]
print(caros)  # [1000, 800]
```

## Análisis práctico

```python
# Analítica rápida de ventas
ventas_diarias = [1200, 3400, 2800, 4100, 3900, 4500, 3200,
                  3800, 5100, 4700, 5300, 4900, 5200, 5800]

# Métricas básicas
total = sum(ventas_diarias)
promedio = total / len(ventas_diarias)
max_venta = max(ventas_diarias)
min_venta = min(ventas_diarias)

print(f"Total: {total:,.2f}€")
print(f"Promedio diario: {promedio:,.2f}€")
print(f"Mejor día: {max_venta:,.2f}€")
print(f"Peor día: {min_venta:,.2f}€")

# Días por encima del promedio
dias_sobre_promedio = [v for v in ventas_diarias if v > promedio]
print(f"Días sobre promedio: {len(dias_sobre_promedio)} de {len(ventas_diarias)}")

# Crecimiento vs día anterior
for i in range(1, len(ventas_diarias)):
    cambio = ventas_diarias[i] - ventas_diarias[i-1]
    signo = "+" if cambio > 0 else ""
    print(f"Día {i+1}: {signo}{cambio:,.2f}€")
```

## Ejercicios del Capítulo 9

1. Crea una lista con los nombres de 5 productos de TechStore.
2. Añade 3 productos más a la lista con `append()`.
3. Crea un diccionario para un cliente con: nombre, email, ciudad, gasto_total.
4. Actualiza el gasto_total del cliente sumando 150€.
5. Dada una lista de precios `[299, 599, 899, 1299, 1999]`, crea una nueva lista con los precios con IVA (x1.21).
6. Usa un bucle for para calcular el total de una cesta de la compra: `[("Portátil", 1299.99), ("Ratón", 29.99), ("Teclado", 89.99)]`.
7. Filtra una lista de precios para mostrar solo los mayores de 500€.
8. Simula un inventario: crea un diccionario con 5 productos y sus stocks. Usa un bucle para vender 1 unidad de cada uno.
9. Encuentra el producto más caro en una lista de diccionarios de productos.
10. Crea una función que reciba una lista de ventas diarias y devuelva el promedio, máximo y mínimo.

## Checklist de autoevaluación

- [ ] Sé crear y manipular listas
- [ ] Sé crear y manipular diccionarios
- [ ] Sé usar condicionales if/elif/else
- [ ] Sé usar bucles for para iterar colecciones
- [ ] Sé usar while para repeticiones condicionales
- [ ] Sé usar comprensión de listas
- [ ] Entiendo la estructura lista-de-diccionarios
