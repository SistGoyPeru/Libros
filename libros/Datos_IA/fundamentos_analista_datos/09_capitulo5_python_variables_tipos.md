# Capítulo 5: Python — Variables y Tipos de Datos

## ¿Por qué Python?

Python es el lenguaje más popular en análisis de datos por tres razones:

1. **Sintaxis simple**: Se lee como inglés
2. **Ecosistema increíble**: Pandas, NumPy, Matplotlib
3. **Comunidad masiva**: Siempre encuentras ayuda

No necesitas ser programador. Python para análisis de datos se aprende haciendo.

## Tu primer programa

Abre VS Code, crea un archivo `hola_analista.py` y escribe:

```python
print("¡Hola, analista de datos!")
```

Ejecuta con: botón derecho > "Run Python" o en terminal: `python hola_analista.py`

## Variables: guardar información

Una variable es como una caja donde guardas un valor:

```python
nombre = "TechStore"
año_fundacion = 2018
ventas_totales = 1250000.50
tiene_tienda_online = True
```

### Reglas para nombres de variables

- Usa letras, números y guiones bajos
- No empieces con número
- No uses palabras reservadas (`if`, `for`, `while`, etc.)
- Usa `snake_case`: `ventas_totales`, `nombre_producto`

## Tipos de datos básicos

```python
# Texto (string)
nombre = "TechStore"
mensaje = 'Bienvenidos'

# Números enteros (int)
empleados = 25
productos = 509

# Números decimales (float)
precio = 1299.99
iva = 0.21

# Booleanos (bool)
activo = True
en_oferta = False

# Tipo de dato None (nulo)
descuento = None
```

Puedes saber el tipo de cualquier valor con `type()`:

```python
print(type(nombre))    # <class 'str'>
print(type(empleados)) # <class 'int'>
print(type(precio))    # <class 'float'>
print(type(activo))    # <class 'bool'>
```

## Conversión entre tipos

```python
precio_str = "1299.99"
precio_num = float(precio_str)   # Convierte texto a número
print(precio_num + 100)          # 1399.99

empleados = 25
print("Tenemos " + str(empleados) + " empleados")  # Convierte número a texto
```

### F-strings (la forma moderna)

```python
nombre = "TechStore"
empleados = 25
print(f"{nombre} tiene {empleados} empleados")
# TechStore tiene 25 empleados
```

## Operadores básicos

### Aritméticos

```python
a = 10
b = 3

print(a + b)   # 13  (suma)
print(a - b)   # 7   (resta)
print(a * b)   # 30  (multiplicación)
print(a / b)   # 3.33 (división real)
print(a // b)  # 3   (división entera)
print(a % b)   # 1   (módulo / resto)
print(a ** b)  # 1000 (potencia)
```

### Comparación

```python
print(10 > 5)    # True
print(10 == 5)   # False
print(10 != 5)   # True
print(10 >= 10)  # True
```

## Input del usuario

```python
nombre = input("¿Cómo te llamas? ")
print(f"Bienvenido al análisis de datos, {nombre}")
```

## Un ejemplo con datos de TechStore

```python
# Calcular precio con IVA
precio_sin_iva = 1299.99
iva = 0.21
precio_con_iva = precio_sin_iva * (1 + iva)
print(f"Precio sin IVA: {precio_sin_iva}€")
print(f"Precio con IVA: {precio_con_iva:.2f}€")

# Calcular margen de beneficio
coste = 850.00
margen = precio_sin_iva - coste
porcentaje_margen = (margen / precio_sin_iva) * 100
print(f"Margen: {margen:.2f}€ ({porcentaje_margen:.1f}%)")

# Valor del inventario
unidades = 150
valor_inventario = precio_sin_iva * unidades
print(f"Valor inventario: {valor_inventario:,.2f}€")
```

## Errores comunes (y cómo solucionarlos)

```python
# Error: mezclar tipos
precio = "1299.99"
# print(precio + 100)  # TypeError: can only concatenate str to str

# Solución: convertir
print(float(precio) + 100)  # 1399.99

# Error: variable no definida
# print(ventas_2026)  # NameError

# Solución: definir la variable primero
ventas_2026 = 1500000
print(ventas_2026)
```

## Ejercicios del Capítulo 5

Escribe y ejecuta cada ejercicio en VS Code.

1. Crea una variable `nombre_tienda` con valor "TechStore" y muéstrala.
2. Crea variables `ingresos` (1500000) y `gastos` (950000). Calcula y muestra el beneficio.
3. Pide al usuario su nombre y muestra un saludo personalizado con f-string.
4. Calcula el precio con IVA (21%) de un producto que cuesta 499.99€.
5. Convierte el string "1299.99" a float y súmale 200. Muestra el resultado.
6. Calcula cuántos días han pasado desde el 1 de enero de 2024 hasta hoy. Usa `from datetime import date` y haz la resta.
7. Crea una variable `stock` con valor 50. Simula una venta de 3 unidades y muestra el stock restante usando f-string.
8. Calcula el porcentaje de mujeres en una empresa: de 25 empleados, 12 son mujeres.
9. Pide al usuario dos números, súmalos y muestra el resultado (recuerda convertir el input).
10. Usa `type()` para verificar los tipos de: 42, 3.14, "Hola", True, None.

## Proyecto rápido: Calculadora de métricas TechStore

```python
# Calculadora rápida de métricas
print("=== TechStore - Calculadora de Métricas ===")

ingresos = float(input("Ingresos totales: "))
gastos = float(input("Gastos totales: "))
clientes = int(input("Número de clientes: "))

beneficio = ingresos - gastos
margen = (beneficio / ingresos) * 100
ingreso_por_cliente = ingresos / clientes

print(f"\n=== Resumen ===")
print(f"Beneficio: {beneficio:,.2f}€")
print(f"Margen: {margen:.1f}%")
print(f"Ingreso por cliente: {ingreso_por_cliente:.2f}€")
```

## Checklist de autoevaluación

- [ ] Sé crear y ejecutar un archivo Python
- [ ] Sé crear variables con nombres descriptivos
- [ ] Conozco los tipos básicos: int, float, str, bool, None
- [ ] Sé convertir entre tipos (int a str, str a float)
- [ ] Sé usar f-strings para formatear texto
- [ ] Sé usar operadores aritméticos y de comparación
- [ ] Sé obtener input del usuario con input()
