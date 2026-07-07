# Capítulo 8: La Regresión del Pasado

## Conceptos: Regresión lineal, recta de mejor ajuste, R², predicción

---

El viaje al Valle Sagrado tomó tres horas. Valeria y Marco alquilaron un auto y recorrieron la carretera que serpenteaba entre montañas. El paisaje era imponente: terrazas incas talladas en las laderas, nubes bajas que rozaban los picos, y el río Urubamba brillando al sol.

—¿Qué sabes de Sofía? —preguntó Valeria.

—Poco —dijo Marco—. Trabajaba con Kamila desde hacía dos años. Era su asistente de investigación. Muy callada, muy eficiente. Nunca llamaba la atención.

—Eso es sospechoso en sí mismo.

—¿Por qué?

—Porque en estadística, los valores atípicos son los más interesantes. Pero también lo son los valores que se esconden en la media. Los que nunca se desvían. Los que pasan desapercibidos.

Llegaron a un pequeño pueblo llamado Pachar. La dirección de Sofía era una casa de adobe al final de una calle empedrada. Valeria tocó la puerta.

Una mujer mayor abrió.

—¿Sofía? —preguntó Valeria.

—No está —respondió la mujer—. Se fue ayer. Dijo que tenía que regresar a la ciudad.

—¿Dijo algo más?

La mujer dudó. Luego sacó un sobre de su delantal.

—Dijo que si alguien venía preguntando por ella, les diera esto.

Valeria abrió el sobre. Dentro había una memoria USB y una nota que decía:

*"Lo siento. No sabía en lo que me estaba metiendo. Esto es lo que sé. — Sofía"*

---

## Los datos de Sofía

Valeria conectó la memoria USB a su laptop. Contenía un único archivo: `regresion_secreta.csv`.

—Son datos de ventas de un medicamento —dijo Valeria—. Pero no cualquier medicamento. Es el mismo del ensayo clínico manipulado.

—¿Qué muestra?

—Vamos a verlo con **regresión lineal**.

---

## Regresión lineal: encontrando la línea oculta

—La **regresión lineal** nos permite encontrar la relación entre una variable dependiente (Y) y una o más variables independientes (X). La idea es dibujar una línea recta que mejor se ajuste a los datos.

—La fórmula de una línea recta es:

$$Y = mX + b$$

Donde:
- **m** es la pendiente (cuánto cambia Y por cada unidad de X)
- **b** es el intercepto (el valor de Y cuando X = 0)

Valeria abrió Python:

```python
# Regresión lineal con Python

import numpy as np
import csv
import math

# Cargamos los datos de Sofía
datos_ventas = []
with open('regresion_secreta.csv', 'r') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        datos_ventas.append({
            'mes': int(fila['mes']),
            'gasto_publicidad': float(fila['gasto_publicidad']),
            'ventas': float(fila['ventas']),
            'pacientes': int(fila['pacientes'])
        })

print(f"Registros cargados: {len(datos_ventas)}")
print(f"Rango de meses: {datos_ventas[0]['mes']} - {datos_ventas[-1]['mes']}")
print()

# Extraemos variables
X = np.array([d['gasto_publicidad'] for d in datos_ventas])  # Gasto en publicidad
Y = np.array([d['ventas'] for d in datos_ventas])           # Ventas

# Calculamos la regresión lineal manualmente
n = len(X)
media_x = np.mean(X)
media_y = np.mean(Y)

# Pendiente (m)
numerador = sum((X[i] - media_x) * (Y[i] - media_y) for i in range(n))
denominador = sum((X[i] - media_x) ** 2 for i in range(n))
pendiente = numerador / denominador

# Intercepto (b)
intercepto = media_y - pendiente * media_x

print(f"=== REGRESIÓN LINEAL ===")
print(f"Ecuación: Ventas = {pendiente:.2f} × Publicidad + ({intercepto:.2f})")
print(f"Interpretación: por cada $1,000 en publicidad, las ventas aumentan en ${pendiente*1000:.0f}")
```

Resultado:

```
Registros cargados: 24
Rango de meses: 1 - 24

=== REGRESIÓN LINEAL ===
Ecuación: Ventas = 3.45 × Publicidad + (12.30)
Interpretación: por cada $1,000 en publicidad, las ventas aumentan en $3,450
```

—Pero hay algo raro —dijo Valeria—. La relación debería ser consistente. Veamos los residuos.

---

## Los residuos: lo que la línea no explica

—Los **residuos** son las diferencias entre los valores reales y los valores predichos por la línea de regresión. Si los residuos tienen un patrón, significa que la línea no está capturando toda la información.

```python
# Calculamos predicciones y residuos
predicciones = pendiente * X + intercepto
residuos = Y - predicciones

print(f"\n=== ANÁLISIS DE RESIDUOS ===")
print(f"{'Mes':<6} {'Real':<10} {'Predicho':<12} {'Residuo':<10}")
print("-" * 38)
for i in range(n):
    print(f"{datos_ventas[i]['mes']:<6} {Y[i]:<10.1f} {predicciones[i]:<12.1f} {residuos[i]:<10.1f}")

# Varianza de los residuos
var_residuos = np.var(residuos)
var_total = np.var(Y)
r_cuadrado = 1 - (var_residuos / var_total)

print(f"\nVarianza de residuos: {var_residuos:.2f}")
print(f"Varianza total: {var_total:.2f}")
print(f"R² (coeficiente de determinación): {r_cuadrado:.3f}")
print(f"Interpretación: el {r_cuadrado*100:.1f}% de la variación en ventas")
print(f"  es explicada por el gasto en publicidad")
```

Resultado:

```
=== ANÁLISIS DE RESIDUOS ===
Mes    Real       Predicho     Residuo   
------------------------------------------
1      50.0       48.9         1.1
2      52.0       52.4        -0.4
3      48.0       49.7        -1.7
4      55.0       53.2         1.8
5      51.0       50.1         0.9
...
23     78.0       68.0        10.0
24     82.0       69.3        12.7

Varianza de residuos: 5.82
Varianza total: 24.50
R² (coeficiente de determinación): 0.763
Interpretación: el 76.3% de la variación en ventas
  es explicada por el gasto en publicidad
```

—El R² de 0.763 es decente —dijo Valeria—. Pero mira los últimos meses: los residuos crecen. Mes 23: residuo de 10. Mes 24: residuo de 12.7.

—¿Qué significa?

—Que en los últimos meses, las ventas son mucho más altas de lo que la publicidad predeciría. Como si alguien estuviera inflando los números.

---

## Detectando la manipulación con regresión

Valeria dividió los datos en dos períodos: antes y después del mes 18.

```python
# Dividimos los datos
X_antes = X[:18]
Y_antes = Y[:18]
X_despues = X[18:]
Y_despues = Y[18:]

# Regresión para el período anterior
n_antes = len(X_antes)
media_x_antes = np.mean(X_antes)
media_y_antes = np.mean(Y_antes)
pendiente_antes = sum((X_antes[i] - media_x_antes) * (Y_antes[i] - media_y_antes) 
                       for i in range(n_antes)) / sum((X_antes[i] - media_x_antes) ** 2 
                       for i in range(n_antes))
intercepto_antes = media_y_antes - pendiente_antes * media_x_antes

# Regresión para el período posterior
n_despues = len(X_despues)
media_x_despues = np.mean(X_despues)
media_y_despues = np.mean(Y_despues)
pendiente_despues = sum((X_despues[i] - media_x_despues) * (Y_despues[i] - media_y_despues) 
                         for i in range(n_despues)) / sum((X_despues[i] - media_x_despues) ** 2 
                         for i in range(n_despues))
intercepto_despues = media_y_despues - pendiente_despues * media_x_despues

print("=== COMPARACIÓN DE PERÍODOS ===")
print(f"Período 1 (meses 1-18):")
print(f"  Ventas = {pendiente_antes:.2f} × Publicidad + ({intercepto_antes:.2f})")
print(f"  Pendiente: {pendiente_antes:.2f}")
print()
print(f"Período 2 (meses 19-24):")
print(f"  Ventas = {pendiente_despues:.2f} × Publicidad + ({intercepto_despues:.2f})")
print(f"  Pendiente: {pendiente_despues:.2f}")
print()

# Proyección: ¿qué ventas esperaríamos en los meses 19-24
# si el comportamiento hubiera sido el mismo que en los meses 1-18?
print("=== DETECCIÓN DE ANOMALÍAS ===")
print(f"{'Mes':<6} {'Real':<10} {'Esperado':<12} {'Diferencia':<12}")
print("-" * 40)
for i in range(n_despues):
    real = Y_despues[i]
    esperado = pendiente_antes * X_despues[i] + intercepto_antes
    diff = real - esperado
    print(f"{datos_ventas[18+i]['mes']:<6} {real:<10.1f} {esperado:<12.1f} {diff:<12.1f}")
```

Resultado:

```
=== COMPARACIÓN DE PERÍODOS ===
Período 1 (meses 1-18):
  Ventas = 2.80 × Publicidad + (14.20)
  Pendiente: 2.80

Período 2 (meses 19-24):
  Ventas = 4.90 × Publicidad + (8.50)
  Pendiente: 4.90

=== DETECCIÓN DE ANOMALÍAS ===
Mes    Real       Esperado     Diferencia   
--------------------------------------------
19     65.0       57.3         7.7
20     68.0       59.5         8.5
21     72.0       60.2         11.8
22     75.0       62.8         12.2
23     78.0       65.1         12.9
24     82.0       67.4         14.6
```

—La pendiente cambió de 2.80 a 4.90 —dijo Valeria—. Eso significa que, en los últimos 6 meses, cada dólar de publicidad generó casi el doble de ventas que antes. Eso no es crecimiento orgánico. Eso es manipulación.

—¿Y quién estuvo a cargo de los datos en esos meses?

—Según la nota de Sofía... ella misma.

---

## El R² y la calidad del modelo

—El **R²** (coeficiente de determinación) mide qué tan bien la línea de regresión se ajusta a los datos. Va de 0 a 1:

- **R² = 1**: el modelo predice perfectamente
- **R² = 0**: el modelo no predice nada

```python
# R² para ambos períodos
def calcular_r2(X, Y, pendiente, intercepto):
    predicciones = pendiente * X + intercepto
    residuos = Y - predicciones
    var_residuos = np.var(residuos)
    var_total = np.var(Y)
    return 1 - (var_residuos / var_total)

r2_antes = calcular_r2(X_antes, Y_antes, pendiente_antes, intercepto_antes)
r2_despues = calcular_r2(X_despues, Y_despues, pendiente_despues, intercepto_despues)

print(f"R² período 1: {r2_antes:.3f}")
print(f"R² período 2: {r2_despues:.3f}")
print()
print("Interpretación:")
if r2_despues > r2_antes:
    print("El R² aumentó: los datos del período 2 son 'demasiado perfectos'")
    print("→ Posible manipulación: los datos fueron ajustados para verse mejor")
else:
    print("El R² se mantuvo estable: los datos parecen consistentes")
```

Resultado:

```
R² período 1: 0.721
R² período 2: 0.958

Interpretación:
El R² aumentó: los datos del período 2 son 'demasiado perfectos'
→ Posible manipulación: los datos fueron ajustados para verse mejor
```

—Un R² de 0.958 en el segundo período significa que los datos se ajustan casi perfectamente a la línea —dijo Valeria—. En el mundo real, los datos nunca son tan perfectos. Alguien los fabricó.

—¿Sofía?

—O alguien usando sus credenciales.

---

## Enigmas

### Enigma 8.1: Calcula la regresión manual

Con estos datos de horas de estudio y notas:

```python
horas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas = [3.0, 4.0, 5.0, 5.5, 6.5, 7.0, 8.0, 8.5, 9.0, 9.5]
```

1. Calcula la pendiente y el intercepto
2. ¿Qué nota predecirías para 7.5 horas de estudio?
3. Calcula el R²

### Enigma 8.2: Detecta la manipulación

¿Cuál de estos conjuntos de datos parece manipulado? ¿Por qué?

```python
# Conjunto A
Xa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Ya = [15, 18, 20, 22, 25, 28, 30, 33, 35, 38]

# Conjunto B
Xb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Yb = [12, 25, 18, 30, 22, 35, 28, 40, 32, 45]
```

### Enigma 8.3: Predice el futuro

Usando la regresión del período 1 (Ventas = 2.80 × Publicidad + 14.20), predice las ventas para los meses 25 y 26 si el gasto en publicidad es de $15,000 y $16,000 respectivamente.

---

## Lo que aprendiste

- La **regresión lineal** encuentra la línea de mejor ajuste (Y = mX + b)
- La **pendiente (m)** mide el cambio en Y por unidad de cambio en X
- El **intercepto (b)** es el valor de Y cuando X = 0
- Los **residuos** son las diferencias entre valores reales y predichos
- El **R²** mide qué tan bien se ajusta el modelo (0 a 1)
- Residuos crecientes en el tiempo → posible manipulación

—Sofía nos dejó la evidencia, pero huyó —dijo Marco—. Eso la hace sospechosa.

—O la hace la próxima víctima —respondió Valeria—. Tenemos que encontrarla antes de que alguien más lo haga.

—¿Y cómo la encontramos?

Valeria miró los datos de la regresión.

—Usando el modelo. Si sabemos cómo se mueve, podemos predecir dónde estará.

