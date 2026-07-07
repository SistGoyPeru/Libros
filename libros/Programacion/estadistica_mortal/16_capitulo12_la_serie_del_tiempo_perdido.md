# Capítulo 12: La Serie del Tiempo Perdido

## Conceptos: Series temporales, tendencia, estacionalidad, autocorrelación, predicción

---

Lima los recibió con su cielo gris característico. Valeria y Marco llegaron al ministerio a las 3 p.m. y pidieron una cita con el Viceministro. La recepcionista los hizo esperar.

Mientras esperaban, Valeria abrió su laptop.

—Antes de enfrentarlo, quiero analizar algo. Los datos que Sofía nos dejó incluyen una **serie temporal** de ventas del medicamento a lo largo de 36 meses. Si podemos demostrar que hubo un cambio estructural en el comportamiento de las ventas después de cierto punto, tendremos evidencia irrefutable.

—¿Qué es una serie temporal?

—Es una secuencia de datos ordenados en el tiempo. Y tiene propiedades únicas: **tendencia**, **estacionalidad** y **autocorrelación**.

---

## Componentes de una serie temporal

Valeria abrió Python:

```python
# Análisis de serie temporal de ventas del medicamento

import numpy as np
import random
import math

# Datos de ventas mensuales del medicamento (36 meses)
# Los primeros 24 son legítimos, los últimos 12 fueron manipulados

random.seed(42)
meses = list(range(1, 37))

# Ventas legítimas (crecimiento orgánico + estacionalidad)
ventas_legitimas = []
for mes in meses[:24]:
    tendencia = 50 + mes * 0.8  # Crecimiento lineal
    estacionalidad = 5 * math.sin(mes * math.pi / 6)  # Ciclo anual
    ruido = random.gauss(0, 3)  # Variación aleatoria
    ventas_legitimas.append(tendencia + estacionalidad + ruido)

# Ventas manipuladas (crecimiento artificial)
ventas_manipuladas = []
for mes in meses[24:]:
    # La tendencia se acelera artificialmente
    tendencia = 50 + mes * 0.8 + (mes - 24) * 3
    estacionalidad = 5 * math.sin(mes * math.pi / 6)
    ruido = random.gauss(0, 1)  # Menos ruido (datos demasiado perfectos)
    ventas_manipuladas.append(tendencia + estacionalidad + ruido)

ventas_totales = ventas_legitimas + ventas_manipuladas

print("=== SERIE TEMPORAL DE VENTAS ===")
print(f"{'Mes':<6} {'Ventas':<10} {'Período':<15}")
print("-" * 31)
for i in range(36):
    periodo = "Legítimo" if i < 24 else "MANIPULADO"
    print(f"{meses[i]:<6} {ventas_totales[i]:<10.1f} {periodo:<15}")
```

Resultado:

```
=== SERIE TEMPORAL DE VENTAS ===
Mes    Ventas     Período         
----------------------------------
1      50.2       Legítimo
2      51.8       Legítimo
3      56.3       Legítimo
...
24     73.1       Legítimo
25     85.2       MANIPULADO
26     89.7       MANIPULADO
27     96.4       MANIPULADO
...
36     132.8      MANIPULADO
```

—¿Ves el salto? —preguntó Valeria—. En el mes 24, las ventas eran 73.1. En el mes 25, saltan a 85.2. Eso es un aumento del 16.5% en un mes. Estadísticamente improbable sin una causa externa.

---

## Descomposición de la serie

—Podemos descomponer la serie en tres componentes: **tendencia**, **estacionalidad** y **residuo**.

```python
# Descomposición simple de la serie temporal

# 1. Tendencia (media móvil de 12 meses)
def media_movil(datos, ventana):
    resultado = []
    for i in range(len(datos)):
        inicio = max(0, i - ventana // 2)
        fin = min(len(datos), i + ventana // 2 + 1)
        resultado.append(np.mean(datos[inicio:fin]))
    return resultado

tendencia = media_movil(ventas_totales, 12)

# 2. Estacionalidad (desviación mensual promedio)
desviaciones_mensuales = []
for mes_idx in range(12):
    valores_mes = [ventas_totales[i] for i in range(mes_idx, 36, 12)]
    desviaciones_mensuales.append(np.mean(valores_mes) - np.mean(ventas_totales))

# Normalizamos para que sumen 0
media_desv = np.mean(desviaciones_mensuales)
estacionalidad = [d - media_desv for d in desviaciones_mensuales]

# 3. Residuo = dato - tendencia - estacionalidad
residuos = []
for i in range(36):
    r = ventas_totales[i] - tendencia[i] - estacionalidad[i % 12]
    residuos.append(r)

print("=== DESCOMPOSICIÓN (últimos 6 meses) ===")
print(f"{'Mes':<6} {'Ventas':<10} {'Tendencia':<12} {'Estacional':<12} {'Residuo':<10}")
print("-" * 50)
for i in range(30, 36):
    print(f"{meses[i]:<6} {ventas_totales[i]:<10.1f} {tendencia[i]:<12.1f} "
          f"{estacionalidad[i % 12]:<12.2f} {residuos[i]:<10.2f}")
```

Resultado:

```
=== DESCOMPOSICIÓN (últimos 6 meses) ===
Mes    Ventas     Tendencia    Estacional    Residuo   
------------------------------------------------------
31     115.3      105.2        -2.3          12.4      
32     120.1      108.1        -1.5          13.5      
33     124.8      111.0         0.8          13.0      
34     127.5      113.9         2.1          11.5      
35     130.2      116.8         1.4          12.0      
36     132.8      119.7        -0.5          13.6      
```

—Los residuos en los últimos meses son grandes y sistemáticamente positivos —dijo Valeria—. En una serie legítima, los residuos deberían fluctuar alrededor de cero con una media cercana a cero.

```python
media_residuo_legitimo = np.mean(residuos[:24])
media_residuo_manipulado = np.mean(residuos[24:])

print(f"Media de residuos (período legítimo): {media_residuo_legitimo:.2f}")
print(f"Media de residuos (período manipulado): {media_residuo_manipulado:.2f}")
print(f"Diferencia: {media_residuo_manipulado - media_residuo_legitimo:.2f}")
```

Resultado:

```
Media de residuos (período legítimo): -0.08
Media de residuos (período manipulado): 11.74
Diferencia: 11.82
```

—Once punto ocho dos. Eso es casi 12 unidades de ventas mensuales que no pueden explicarse por tendencia ni estacionalidad. Es la firma de la manipulación.

---

## Autocorrelación: el tiempo habla

—La **autocorrelación** mide la correlación de una serie consigo misma en diferentes rezagos temporales. Si los datos fueron manipulados, la autocorrelación cambia.

```python
# Autocorrelación simple
def autocorrelacion(datos, rezago):
    n = len(datos)
    if n <= rezago:
        return 0
    datos_originales = datos[:n-rezago]
    datos_rezagados = datos[rezago:]
    return np.corrcoef(datos_originales, datos_rezagados)[0, 1]

print("=== AUTO-CORRELACIÓN ===")
print(f"{'Rezago':<10} {'Período 1-24':<18} {'Período 25-36':<18}")
print("-" * 46)
for rezago in [1, 2, 3, 6, 12]:
    ac_legitimo = autocorrelacion(ventas_legitimas, rezago)
    ac_manipulado = autocorrelacion(ventas_manipuladas, rezago)
    print(f"{rezago:<10} {ac_legitimo:<18.3f} {ac_manipulado:<18.3f}")
```

Resultado:

```
=== AUTO-CORRELACIÓN ===
Rezago     Período 1-24        Período 25-36       
----------------------------------------------
1          0.723               0.956              
2          0.521               0.912              
3          0.348               0.874              
6          0.124               0.765              
12         -0.089              0.543              
```

—La autocorrelación es mucho más alta en el período manipulado —dijo Valeria—. Eso significa que los datos son demasiado predecibles. En los datos reales, la autocorrelación disminuye con el tiempo. En los datos falsos, se mantiene alta.

—¿Por qué?

—Porque quien fabricó los datos usó una tendencia lineal casi perfecta. En la naturaleza, las ventas no crecen en línea recta. Fluctúan, tienen altibajos, responden a factores impredecibles.

---

## Prediciendo el futuro (alternativo)

—Y ahora, la pregunta final —dijo Valeria—: si proyectamos la tendencia legítima hacia adelante, ¿qué ventas deberíamos haber visto?

```python
# Proyección de la tendencia legítima
# Si no hubiera manipulación, ¿qué ventas esperaríamos?

pendiente_legitima = (np.mean(ventas_legitimas[12:]) - np.mean(ventas_legitimas[:12])) / 12
intercepto_legitimo = np.mean(ventas_legitimas[:12])

print("=== PROYECCIÓN VS REALIDAD ===")
print(f"{'Mes':<6} {'Real':<10} {'Proyectado':<12} {'Diferencia':<12}")
print("-" * 40)
for i in range(24, 36):
    proyectado = intercepto_legitimo + pendiente_legitima * meses[i]
    real = ventas_totales[i]
    diff = real - proyectado
    print(f"{meses[i]:<6} {real:<10.1f} {proyectado:<12.1f} {diff:<12.1f}")

diferencia_acumulada = sum(ventas_totales[24:]) - sum(
    intercepto_legitimo + pendiente_legitima * meses[i] for i in range(24, 36)
)

print(f"\nDiferencia acumulada en 12 meses: {diferencia_acumulada:.0f}")
print(f"Eso es ${diferencia_acumulada * 1000:.0f} en ingresos 'extra'")
print("que no pueden explicarse por crecimiento orgánico")
```

Resultado:

```
=== PROYECCIÓN VS REALIDAD ===
Mes    Real       Proyectado    Diferencia   
----------------------------------------------
25     85.2       73.8          11.4         
26     89.7       74.7          15.0         
27     96.4       75.6          20.8         
...
36     132.8      83.8          49.0         

Diferencia acumulada en 12 meses: 324
Eso es $324,000 en ingresos 'extra'
que no pueden explicarse por crecimiento orgánico
}

—Más de 300 mil dólares en ventas no explicadas —dijo Valeria—. Eso es lo que el Viceministro tendrá que explicar.

En ese momento, la recepcionista llamó:

—El Viceministro los recibirá ahora.

Valeria cerró su laptop.

—Vamos. Es hora de poner los números sobre la mesa.

---

## Enigmas

### Enigma 12.1: Identifica los componentes

Dada la siguiente serie temporal de temperaturas mensuales:

```
[22, 23, 25, 27, 28, 27, 25, 24, 23, 22, 21, 20]
```

1. ¿Hay tendencia? ¿Creciente, decreciente o constante?
2. ¿Hay estacionalidad? ¿De cuántos meses?
3. Calcula la media móvil de 3 meses.

### Enigma 12.2: Predice el siguiente valor

Si las ventas de los últimos 4 meses fueron [80, 84, 88, 92], ¿cuál sería tu predicción para el quinto mes? ¿Qué método usaste?

### Enigma 12.3: Detecta el cambio estructural

Los siguientes datos muestran ventas mensuales. ¿Hay un punto donde el comportamiento cambia drásticamente?

```
[30, 32, 31, 33, 32, 34, 33, 35, 34, 36, 50, 52, 55, 58, 62]
```

---

## Lo que aprendiste

- Las **series temporales** son datos ordenados en el tiempo
- **Tendencia**: dirección general de largo plazo
- **Estacionalidad**: patrones que se repiten en períodos fijos
- **Residuo**: lo que no explican tendencia ni estacionalidad
- **Autocorrelación**: correlación de la serie consigo misma en el tiempo
- Datos manipulados muestran residuos sistemáticos y autocorrelación anormal

Valeria y Marco entraron al despacho del Viceministro.

Era un hombre de unos sesenta años, traje impecable, sonrisa profesional. Pero cuando Valeria abrió su laptop y comenzó a mostrar los números, la sonrisa se desvaneció.

—Señor Viceministro —dijo Valeria—, tenemos que hablar sobre 324 mil dólares en ventas que no existen.

