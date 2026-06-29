# Capítulo 2: La Probabilidad del Crimen

## Conceptos: Probabilidad básica, espacio muestral, eventos, regla de Laplace

---

Marco llevó a Valeria a la cafetería del ICD, un espacio abierto en el tercer piso con vistas a la cordillera. El sol de la mañana iluminaba los picos nevados mientras ellos se sentaban en una mesa apartada.

—Tengo que contarte algo —dijo Marco en voz baja—. La noche antes de morir, Kamila me envió un mensaje. Decía que había encontrado algo en los datos. Algo que no debía existir.

—¿Qué era?

—No lo sé. Dijo que era como... una irregularidad estadística. Una probabilidad imposible.

Valeria sacó su laptop.

—Dime exactamente lo que te dijo.

—Dijo: "La probabilidad de que esto ocurra al azar es una en un millón. Literalmente." Y luego me envió un archivo.

—¿Qué archivo?

—Este.

Marco le pasó una memoria USB. Valeria la conectó. Dentro había un solo archivo:

```
distribucion_sospechosa.csv
```

Valeria lo abrió. Eran 1000 registros con dos columnas: `tratamiento` y `resultado`.

—Son datos de un ensayo clínico —dijo Valeria—. Pero hay algo raro en la distribución.

---

## Probabilidad: el lenguaje del azar

Valeria abrió Python.

—Para entender qué vio Kamila, primero tenemos que entender la **probabilidad**. La probabilidad mide qué tan probable es que ocurra un evento. Va de 0 (imposible) a 1 (seguro).

—Eso lo sé —dijo Marco—. Como cuando la probabilidad de lluvia es del 30%.

—Exacto. Pero la forma correcta de calcularla es con la **regla de Laplace**:

$$P(evento) = \frac{\text{casos favorables}}{\text{casos posibles}}$$

—Por ejemplo, si lanzas una moneda, la probabilidad de que salga cara es 1/2 = 0.5. Si lanzas un dado, la probabilidad de que salga un 6 es 1/6 ≈ 0.1667.

Valeria escribió en Python:

```python
# Probabilidad básica con Python

import random

# Simular lanzamiento de una moneda
caras = 0
total_lanzamientos = 1000

for _ in range(total_lanzamientos):
    if random.random() < 0.5:  # 50% de probabilidad
        caras += 1

probabilidad_estimada = caras / total_lanzamientos
print(f"Lanzamientos: {total_lanzamientos}")
print(f"Caras obtenidas: {caras}")
print(f"Probabilidad estimada: {probabilidad_estimada:.4f}")
print(f"Probabilidad teórica: 0.5")
```

Resultado:

```
Lanzamientos: 1000
Caras obtenidas: 513
Probabilidad estimada: 0.5130
Probabilidad teórica: 0.5
```

—La probabilidad estimada se acerca a la teórica mientras más lanzamientos hagamos. Eso es la **ley de los grandes números**.

—Entonces, ¿qué vio Kamila en los datos del ensayo clínico?

---

## La distribución sospechosa

Valeria cargó el archivo en Python:

```python
import csv
from collections import Counter

datos_ensayo = []
with open('distribucion_sospechosa.csv', 'r') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        datos_ensayo.append(fila)

print(f"Total de pacientes: {len(datos_ensayo)}")

# Contar resultados por tratamiento
resultados = Counter()
for paciente in datos_ensayo:
    clave = (paciente['tratamiento'], paciente['resultado'])
    resultados[clave] += 1

print("\n=== RESULTADOS DEL ENSAYO ===")
for (tratamiento, resultado), conteo in sorted(resultados.items()):
    print(f"Tratamiento '{tratamiento}' - Resultado '{resultado}': {conteo}")
```

Resultado:

```
Total de pacientes: 1000

=== RESULTADOS DEL ENSAYO ===
Tratamiento 'A' - Resultado 'mejora': 470
Tratamiento 'A' - Resultado 'no_mejora': 30
Tratamiento 'B' - Resultado 'mejora': 240
Tratamiento 'B' - Resultado 'no_mejora': 260
```

—Mira esto —dijo Valeria—. Del grupo que recibió el tratamiento A, 470 de 500 pacientes mejoraron. Eso es una tasa de éxito del 94%. Del grupo B, solo 240 de 500 mejoraron: 48%.

—Entonces el tratamiento A funciona mucho mejor.

—Sí, pero la pregunta es: ¿cuál es la probabilidad de que esta diferencia se deba al azar?

Valeria continuó:

```python
total_pacientes = 1000

# Probabilidad de mejora con tratamiento A
p_A_mejora = 470 / 500
print(f"P(mejora | Tratamiento A) = {p_A_mejora:.3f}")

# Probabilidad de mejora con tratamiento B
p_B_mejora = 240 / 500
print(f"P(mejora | Tratamiento B) = {p_B_mejora:.3f}")

# Diferencia observada
diferencia = p_A_mejora - p_B_mejora
print(f"Diferencia observada: {diferencia:.3f}")

# ¿Cuál es la probabilidad general de mejora?
p_mejora_general = (470 + 240) / 1000
print(f"P(mejora general) = {p_mejora_general:.3f}")
```

Resultado:

```
P(mejora | Tratamiento A) = 0.940
P(mejora | Tratamiento B) = 0.480
Diferencia observada: 0.460
P(mejora general) = 0.710
```

—La diferencia es enorme: 46 puntos porcentuales. Kamila dijo que era una probabilidad en un millón. Vamos a comprobarlo.

```python
# Simulación: si el tratamiento no tuviera efecto,
# ¿con qué frecuencia veríamos una diferencia tan grande?

import random

simulaciones = 10000
diferencias_extremas = 0
resultados_totales = [1] * 710 + [0] * 290  # 710 mejoras, 290 no mejoras

for _ in range(simulaciones):
    random.shuffle(resultados_totales)
    grupo_A = resultados_totales[:500]
    grupo_B = resultados_totales[500:]
    
    p_A = sum(grupo_A) / 500
    p_B = sum(grupo_B) / 500
    diff = abs(p_A - p_B)
    
    if diff >= diferencia:
        diferencias_extremas += 1

probabilidad_azar = diferencias_extremas / simulaciones
print(f"Simulaciones: {simulaciones}")
print(f"Diferencias >= observada: {diferencias_extremas}")
print(f"Probabilidad de que sea azar: {probabilidad_azar:.6f}")
print(f"Equivale a 1 en {1/probabilidad_azar:.0f} aproximadamente")
```

Resultado:

```
Simulaciones: 10000
Diferencias >= observada: 0
Probabilidad de que sea azar: 0.000000
Equivale a 1 en infinito aproximadamente
```

—En 10,000 simulaciones —dijo Valeria—, nunca vimos una diferencia tan grande por puro azar. La probabilidad es esencialmente cero. Esto no fue un accidente estadístico.

—¿Qué significa?

—Significa que estos datos fueron manipulados. Alguien alteró los resultados del ensayo para que el tratamiento A pareciera milagroso. Y Kamila lo descubrió.

---

## La regla de la multiplicación

—Pero hay más —dijo Valeria—. Kamila también me enseñó sobre la probabilidad de eventos independientes.

—Por ejemplo, si la probabilidad de que una persona tenga una enfermedad es del 10% y la probabilidad de que un examen dé un falso positivo es del 5%, la probabilidad de que ambas cosas ocurran es:

$$P(A \cap B) = P(A) \times P(B) = 0.10 \times 0.05 = 0.005$$

—En términos simples, si tienes dos eventos independientes, la probabilidad de que ambos ocurran es el producto de sus probabilidades.

Valeria escribió:

```python
# Probabilidad de eventos independientes

p_enfermedad = 0.10
p_falso_positivo = 0.05

p_ambos = p_enfermedad * p_falso_positivo
print(f"P(enfermedad) = {p_enfermedad}")
print(f"P(falso positivo) = {p_falso_positivo}")
print(f"P(ambos) = {p_ambos}")
print(f"O 1 en {1/p_ambos:.0f}")
```

Resultado:

```
P(enfermedad) = 0.10
P(falso positivo) = 0.05
P(ambos) = 0.005
O 1 en 200
```

—Ahora, aplica esto al caso —dijo Valeria—. Si la probabilidad de que una persona específica estuviera en el ICD a las 3 a.m. es de 0.01 (1%), y la probabilidad de que esa persona tuviera acceso al laboratorio de Kamila es de 0.10 (10%), ¿cuál es la probabilidad de que ambas condiciones se cumplan?

```python
p_estar_en_icd = 0.01
p_tener_acceso = 0.10

p_ambas_condiciones = p_estar_en_icd * p_tener_acceso
print(f"Probabilidad de que una persona cumpla ambas: {p_ambas_condiciones:.4f}")
print(f"O 1 en {1/p_ambas_condiciones:.0f}")
```

—Las probabilidades son implacables —dijo Marco—. Alguien manipuló los datos y alguien estuvo allí esa noche. Y las dos cosas están conectadas.

---

## Enigmas

### Enigma 2.1: El dado cargado

Lanzas un dado 600 veces. Obtienes los siguientes resultados:

| Cara | Frecuencia |
|------|-----------|
| 1    | 120       |
| 2    | 115       |
| 3    | 108       |
| 4    | 95        |
| 5    | 90        |
| 6    | 72        |

1. ¿Cuál es la probabilidad teórica de cada cara?
2. Calcula la probabilidad observada de cada cara.
3. ¿Parece un dado cargado? ¿Por qué?

### Enigma 2.2: Probabilidad del sospechoso

En una lista de 8 sospechosos, 3 tienen acceso al laboratorio, 4 tenían motivos para querer muerta a Kamila, y 2 cumplen ambas condiciones.

1. Si elegimos un sospechoso al azar, ¿cuál es la probabilidad de que tenga acceso al laboratorio?
2. ¿Cuál es la probabilidad de que tenga motivo?
3. ¿Cuál es la probabilidad de que tenga ambos?

### Enigma 2.3: Simulación de la moneda

Escribe un programa en Python que simule 10,000 lanzamientos de una moneda y calcule la probabilidad estimada de obtener cara. ¿Qué tan cerca está del valor teórico de 0.5?

---

## Lo que aprendiste

- La **probabilidad** mide la posibilidad de que ocurra un evento (0 a 1)
- **Regla de Laplace**: P = casos favorables / casos posibles
- **Ley de los grandes números**: más repeticiones → estimaciones más precisas
- Eventos **independientes**: P(A y B) = P(A) × P(B)
- La **simulación** permite estimar probabilidades mediante repetición
- Una probabilidad extremadamente baja sugiere manipulación

Valeria guardó el análisis. Fuera, la noche había caído completamente sobre Barcelona.

—Hay alguien con quien necesito hablar —dijo Valeria—. El director del ICD. Si alguien sabía lo que Kamila estaba investigando, es él.

—No creo que sea buena idea —dijo Marco—. El director... es mi padre.

Valeria lo miró fijamente.

—Tu apellido es Tupac. El director es el Dr. Hugo Tupac.

Marco asintió.

—Y no tengo idea si él está involucrado. Pero tengo miedo de averiguarlo.

