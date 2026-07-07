# Capítulo 7: La Correlación del Secreto

## Conceptos: Correlación, coeficiente de Pearson, causalidad vs correlación, matriz de correlación

---

El Dr. Hugo Tupac los recibió en su despacho con una expresión que Valeria no supo interpretar. ¿Era preocupación? ¿Enojo? ¿Miedo?

—Me dijeron que estaban investigando por su cuenta —dijo el director—. ¿Qué han encontrado?

Valeria colocó su laptop sobre la mesa y mostró los logs de acceso.

—Esto —dijo—. Accesos nocturnos desde la IP de su despacho al servidor del ministerio. La misma noche en que Kamila murió.

El Dr. Tupac observó la pantalla en silencio.

—No fui yo —dijo finalmente—. Esa noche estaba en una cena con el ministro. Tengo testigos.

—¿Alguien más tiene acceso a su computadora?

—Solo yo. Pero... la puerta de mi despacho no tiene llave física. Es biométrica. Cualquiera con acceso al octavo piso pudo entrar.

—¿Quién tiene acceso al octavo piso?

—Mi asistente. El personal de limpieza. Y... Kamila.

—¿Kamila?

—Sí. Ella venía a verme a menudo. Y a veces, cuando yo no estaba, dejaba documentos en mi escritorio.

Valeria procesó la información. ¿Era posible que Kamila misma hubiera accedido al servidor desde el despacho de Hugo? ¿O que alguien estuviera usando la ausencia de Hugo para incriminarlo?

—Necesito ver algo —dijo Valeria—. Las bitácoras de entrada al octavo piso.

—Puedo conseguírtelas —dijo Hugo—. Pero me vas a tener que explicar qué estás buscando.

—Estoy buscando **correlaciones**.

---

## Correlación: la danza de los números

—La **correlación** mide la relación entre dos variables. Si una aumenta y la otra también, tienen correlación positiva. Si una aumenta y la otra disminuye, tienen correlación negativa. Si no hay patrón, no hay correlación.

—El coeficiente de correlación de Pearson (r) va de -1 a +1:

- **r = +1**: correlación positiva perfecta
- **r = 0**: sin correlación
- **r = -1**: correlación negativa perfecta

Valeria abrió Python:

```python
# Correlación en Python

import numpy as np
import random
import math

# Ejemplos de correlación

# 1. Correlación positiva perfecta (r ≈ 1)
horas_estudio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas_examen = [2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 9.0, 10.0]

r_positivo = np.corrcoef(horas_estudio, notas_examen)[0, 1]
print(f"Correlación (horas estudio vs nota): {r_positivo:.3f}")

# 2. Correlación negativa perfecta (r ≈ -1)
edad_auto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
precio_auto = [30000, 27000, 24000, 21000, 18000, 15000, 12000, 9000, 6000, 3000]

r_negativo = np.corrcoef(edad_auto, precio_auto)[0, 1]
print(f"Correlación (edad del auto vs precio): {r_negativo:.3f}")

# 3. Sin correlación (r ≈ 0)
random.seed(42)
x_aleatorio = [random.gauss(0, 1) for _ in range(50)]
y_aleatorio = [random.gauss(0, 1) for _ in range(50)]

r_cero = np.corrcoef(x_aleatorio, y_aleatorio)[0, 1]
print(f"Correlación (datos aleatorios): {r_cero:.3f}")
```

Resultado:

```
Correlación (horas estudio vs nota): 0.976
Correlación (edad del auto vs precio): -0.997
Correlación (datos aleatorios): 0.042
```

---

## El problema: correlación no es causalidad

—Pero aquí está el error más común en estadística —dijo Valeria—: confundir **correlación con causalidad**.

—¿Qué significa eso?

—Que porque dos cosas estén correlacionadas, no significa que una cause la otra.

Valeria escribió:

```python
# Ejemplos de correlaciones falsas

# Ejemplo 1: Ventas de helados y ahogados
meses = list(range(1, 13))
ventas_helados = [10, 12, 15, 25, 40, 55, 60, 58, 45, 30, 18, 12]
ahogados_playa = [2, 3, 4, 8, 15, 22, 25, 24, 16, 9, 5, 3]

r_helados_ahogados = np.corrcoef(ventas_helados, ahogados_playa)[0, 1]
print(f"Correlación (helados vs ahogados): {r_helados_ahogados:.3f}")
print("¿Los helados causan ahogados? ¡NO!")
print("Variable oculta: el CALOR (en verano se venden más helados y más gente va a la playa)")
print()

# Ejemplo 2: Número de iglesias y crímenes
# (Datos ficticios para ilustrar)
ciudades = ['A', 'B', 'C', 'D', 'E']
iglesias = [5, 10, 15, 20, 25]
tasa_crimen = [20, 35, 45, 55, 70]

r_iglesias_crimen = np.corrcoef(iglesias, tasa_crimen)[0, 1]
print(f"Correlación (iglesias vs crímenes): {r_iglesias_crimen:.3f}")
print("¿Las iglesias causan crímenes? ¡NO!")
print("Variable oculta: POBLACIÓN (ciudades más grandes tienen más iglesias y más crímenes)")
```

Resultado:

```
Correlación (helados vs ahogados): 0.987
¿Los helados causan ahogados? ¡NO!
Variable oculta: el CALOR (en verano se venden más helados y más gente va a la playa)

Correlación (iglesias vs crímenes): 0.993
¿Las iglesias causan crímenes? ¡NO!
Variable oculta: POBLACIÓN (ciudades más grandes tienen más iglesias y más crímenes)
```

—En nuestro caso —dijo Valeria—, tenemos una correlación entre la IP de Hugo y los accesos nocturnos. Pero eso no significa que Hugo sea el culpable. Podría haber una **variable oculta**.

—¿Como qué?

—Como que alguien más usó su computadora. O que Kamila misma accedió desde allí para investigar. O que el sistema de logs fue manipulado.

---

## Matriz de correlación del caso

Valeria cargó los datos completos.

```python
# Matriz de correlación de las variables del caso

import pandas as pd

# Datos simulados del caso
datos_caso = pd.DataFrame({
    'sospechoso': ['Ramiro', 'Hugo', 'Sofia', 'Proveedor', 'Consultor'],
    'acceso_fisico': [1, 1, 1, 0, 1],        # 1 = tiene acceso
    'acceso_datos': [0.7, 0.9, 0.8, 0.1, 1],  # 0-1 nivel de acceso
    'motivo': [0.5, 0.3, 0.2, 0.8, 0.6],      # 0-1 nivel de motivo
    'coartada': [0.1, 0.7, 0.5, 0.3, 0.4],    # 0-1 solidez de coartada
    'desaparicion': [1, 0, 0, 0, 0],           # 1 = desapareció
    'ip_nocturna': [0, 1, 0.2, 0, 0.3],        # 0-1 frecuencia en logs nocturnos
    'manipulacion': [0.3, 0.7, 0.8, 0.2, 0.6]  # 0-1 evidencia de manipulación
})

# Calculamos la matriz de correlación
matriz_correlacion = datos_caso.select_dtypes(include=[np.number]).corr()

print("=== MATRIZ DE CORRELACIÓN ===")
print(matriz_correlacion.round(3))
print()

# Extraemos las correlaciones con 'manipulacion'
print("=== CORRELACIONES CON 'MANIPULACION' ===")
correlaciones_con_manipulacion = matriz_correlacion['manipulacion'].sort_values(ascending=False)
print(correlaciones_con_manipulacion.round(3))
```

Resultado:

```
=== MATRIZ DE CORRELACIÓN ===
                acceso_fisico  acceso_datos   motivo  coartada  desaparicion  ip_nocturna  manipulacion
acceso_fisico          1.000         0.707   -0.707    -0.000        -0.707        0.000         0.000
acceso_datos           0.707         1.000   -0.677     0.632        -0.535        0.574         0.707
motivo                -0.707        -0.677    1.000    -0.535         0.189       -0.542        -0.394
coartada              -0.000         0.632   -0.535     1.000        -0.632        0.316         0.316
desaparicion          -0.707        -0.535    0.189    -0.632         1.000       -0.189        -0.189
ip_nocturna            0.000         0.574   -0.542     0.316        -0.189        1.000         0.872
manipulacion           0.000         0.707   -0.394     0.316        -0.189        0.872         1.000

=== CORRELACIONES CON 'MANIPULACION' ===
manipulacion     1.000
ip_nocturna      0.872
acceso_datos     0.707
coartada         0.316
motivo          -0.394
desaparicion    -0.189
acceso_fisico    0.000
```

—Mira esto —dijo Valeria—. La variable con mayor correlación con `manipulacion` es `ip_nocturna` (0.872). Eso significa que quien tenga accesos nocturnos desde su IP tiene alta probabilidad de haber manipulado datos. Y Hugo es quien tiene el valor más alto en `ip_nocturna`.

—Pero —interrumpió Marco— también dijiste que correlación no es causalidad.

—Correcto. Y por eso necesitamos la siguiente pieza del rompecabezas.

---

## El diagrama de dispersión

Valeria creó un gráfico:

```python
# Diagrama de dispersión: acceso a datos vs manipulación
import matplotlib.pyplot as plt

datos_grafico = {
    'Ramiro': (0.7, 0.3),
    'Hugo': (0.9, 0.7),
    'Sofia': (0.8, 0.8),
    'Proveedor': (0.1, 0.2),
    'Consultor': (1.0, 0.6)
}

nombres = list(datos_grafico.keys())
accesos = [datos_grafico[n][0] for n in nombres]
manipulaciones = [datos_grafico[n][1] for n in nombres]

plt.figure(figsize=(8, 6))
plt.scatter(accesos, manipulaciones, s=100)

for i, nombre in enumerate(nombres):
    plt.annotate(nombre, (accesos[i], manipulaciones[i]),
                 xytext=(5, 5), textcoords='offset points')

plt.xlabel('Nivel de Acceso a Datos')
plt.ylabel('Evidencia de Manipulación')
plt.title('Acceso a Datos vs Manipulación')
plt.grid(True, alpha=0.3)

# Línea de tendencia
z = np.polyfit(accesos, manipulaciones, 1)
p = np.poly1d(z)
x_line = np.linspace(0, 1, 100)
plt.plot(x_line, p(x_line), 'r--', alpha=0.7)

plt.show()
```

—Sofía y Hugo están en la zona de alta correlación —dijo Valeria—. Pero Sofía tiene más evidencia de manipulación (0.8) que Hugo (0.7). Y tiene menos acceso que Hugo...

—¿Entonces podría ser Sofía? —preguntó Marco.

—O podría ser que Hugo y Sofía estén trabajando juntos. O que uno esté incriminando al otro.

---

## Enigmas

### Enigma 7.1: Calcula la correlación

Dados los siguientes datos de publicidad vs ventas:

```python
publicidad = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ventas = [12, 15, 18, 20, 22, 25, 28, 30, 32, 35]
```

1. Calcula el coeficiente de correlación de Pearson
2. Interpreta el resultado

### Enigma 7.2: Correlación falsa

Propón tres ejemplos de correlaciones falsas (donde dos variables están correlacionadas pero no hay relación causal). Para cada una, identifica la variable oculta.

### Enigma 7.3: Matriz del caso

Agrega un nuevo sospechoso a la matriz: la asistente de Kamila, llamada "Lidia", con estos valores:

- acceso_fisico: 0
- acceso_datos: 0.6
- motivo: 0.4
- coartada: 0.8
- desaparicion: 0
- ip_nocturna: 0.5
- manipulacion: 0.4

Recalcula la matriz de correlación. ¿Cambia la interpretación?

---

## Lo que aprendiste

- La **correlación** mide la relación entre dos variables (-1 a +1)
- **Pearson (r)**: mide correlación lineal
- **r ≈ 0**: sin correlación
- **Correlación no implica causalidad**: puede haber variables ocultas
- La **matriz de correlación** muestra relaciones entre múltiples variables
- Los **diagramas de dispersión** visualizan correlaciones

—Sofía —dijo Valeria—. Necesito hablar con Sofía.

—No vas a poder —dijo Hugo—. Tomó una semana de vacaciones. Justo después de la muerte de Kamila.

Valeria sintió que las piezas comenzaban a encajar.

—¿Dónde se fue?

—No lo dijo. Pero tengo su dirección de emergencia. Un pueblo en el Valle Sagrado.

—Entonces —dijo Valeria levantándose—, creo que es hora de hacer un viaje.

