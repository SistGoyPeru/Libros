# Capítulo 9: El Intervalo de Confianza

## Conceptos: Intervalo de confianza, nivel de confianza, margen de error, distribución muestral

---

Sofía no estaba en Pachar. La mujer de la casa dijo que había tomado un bus hacia Ollantaytambo temprano esa mañana. Valeria y Marco abordaron su auto y continuaron la persecución.

—¿Cómo sabemos que vamos en la dirección correcta? —preguntó Marco.

—No lo sabemos —admitió Valeria—. Pero podemos estimarlo.

—¿Estimarlo?

—Con un **intervalo de confianza**.

---

## El intervalo de confianza

—Un **intervalo de confianza** es un rango de valores dentro del cual esperamos que se encuentre el valor real de un parámetro, con cierto nivel de confianza.

—Por ejemplo, si decimos "el 95% de los peruanos tiene entre 25 y 35 años", ese es un intervalo de confianza del 95%.

—Pero no significa que haya un 95% de probabilidad de que la media esté en ese intervalo. Significa que, si repitiéramos el estudio muchas veces, el 95% de los intervalos contendrían la media real.

Valeria abrió Python:

```python
# Intervalo de confianza

import numpy as np
import random
import math

# EJEMPLO: Estimando la edad promedio de los estudiantes del ICD

# Tomamos una muestra de 50 estudiantes
random.seed(42)
muestra_edades = [random.gauss(25, 5) for _ in range(50)]
edad_media_muestral = np.mean(muestra_edades)
desv_std_muestral = np.std(muestra_edades, ddof=1)  # ddof=1 para muestra
n = len(muestra_edades)

print("=== INTERVALO DE CONFIANZA ===")
print(f"Tamaño de muestra: {n}")
print(f"Media muestral: {edad_media_muestral:.2f} años")
print(f"Desviación estándar muestral: {desv_std_muestral:.2f} años")
print()

# Para un intervalo de confianza del 95%:
# IC = media ± (valor_crítico × error_estándar)
# error_estándar = desv_std / sqrt(n)
# valor_crítico para 95% ≈ 1.96 (distribución normal)

nivel_confianza = 0.95
valor_critico = 1.96
error_estandar = desv_std_muestral / math.sqrt(n)
margen_error = valor_critico * error_estandar

ic_inferior = edad_media_muestral - margen_error
ic_superior = edad_media_muestral + margen_error

print(f"Intervalo de confianza del {nivel_confianza*100:.0f}%:")
print(f"  [{ic_inferior:.2f}, {ic_superior:.2f}]")
print(f"  Margen de error: ±{margen_error:.2f}")
print()
print("Interpretación: tenemos un 95% de confianza")
print("de que la media real de la población está entre")
print(f"{ic_inferior:.2f} y {ic_superior:.2f} años.")
```

Resultado:

```
=== INTERVALO DE CONFIANZA ===
Tamaño de muestra: 50
Media muestral: 24.87 años
Desviación estándar muestral: 4.83 años

Intervalo de confianza del 95%:
  [23.53, 26.21]
  Margen de error: ±1.34

Interpretación: tenemos un 95% de confianza
de que la media real de la población está entre
23.53 y 26.21 años.
```

—Ahora —dijo Valeria—, apliquemos esto a nuestra búsqueda de Sofía.

---

## Buscando a Sofía con intervalos

Valeria abrió los registros de su teléfono.

—Sofía usó su tarjeta de crédito tres veces después de desaparecer: una en una gasolinera en Chinchero, otra en un restaurante en Urubamba, y otra en un hotel en Ollantaytambo.

—Está yendo hacia Machu Picchu —dijo Marco.

—O está yendo a la frontera. Pero podemos calcular un intervalo de confianza para su ubicación actual.

```python
# Estimando la ubicación de Sofía

# Distancias desde Pachar (km)
pachar = 0
chinchero = 15
urubamba = 35
ollantaytambo = 60
aguas_calientes = 85  # Machu Picchu
frontera = 200  # Frontera con Bolivia

# Tiempos desde su desaparición (horas)
horas_desde_desaparicion = 18

# Velocidad promedio de viaje (km/h)
# Estimación: entre 30 y 60 km/h (transporte público en la región)
velocidad_min = 30
velocidad_max = 60

# Distancia mínima y máxima recorrida
distancia_min = velocidad_min * horas_desde_desaparicion
distancia_max = velocidad_max * horas_desde_desaparicion

print("=== ESTIMACIÓN DE UBICACIÓN ===")
print(f"Horas desde desaparición: {horas_desde_desaparicion}")
print(f"Velocidad estimada: {velocidad_min}-{velocidad_max} km/h")
print(f"Distancia recorrida: {distancia_min}-{distancia_max} km")
print()

# Radio de búsqueda desde el último punto conocido (Ollantaytambo)
ultima_ubicacion = ollantaytambo
radio_busqueda_min = distancia_min - (ollantaytambo - pachar)
radio_busqueda_max = distancia_max - (ollantaytambo - pachar)

print(f"Última ubicación conocida: Ollantaytambo (km {ultima_ubicacion})")
print(f"Radio de búsqueda: {radio_busqueda_min:.0f}-{radio_busqueda_max:.0f} km desde Ollantaytambo")
print()

# Probabilidad estimada por destino
destinos = {
    'Aguas Calientes (MP)': 85,
    'Cusco': 60,
    'Frontera Bolivia': 200,
    'Selva (Malvinas)': 150
}

print("Probabilidad estimada por destino (basada en distancia):")
for destino, distancia in destinos.items():
    if distancia_min <= distancia <= distancia_max:
        print(f"  {destino}: DENTRO del intervalo de confianza")
    elif distancia < distancia_min:
        print(f"  {destino}: demasiado cerca (ya debería haber llegado)")
    else:
        print(f"  {destino}: demasiado lejos (no le alcanza el tiempo)")
```

Resultado:

```
=== ESTIMACIÓN DE UBICACIÓN ===
Horas desde desaparición: 18
Velocidad estimada: 30-60 km/h
Distancia recorrida: 540-1080 km

Última ubicación conocida: Ollantaytambo (km 60)
Radio de búsqueda: 480-1020 km desde Ollantaytambo
```

—Con ese radio, podría estar en casi cualquier parte del sur del Perú —dijo Marco.

—Por eso necesitamos más datos. Los intervalos de confianza se estrechan cuando tenemos más información.

---

## Estrechando el intervalo

Valeria revisó los registros telefónicos de Sofía.

—Su teléfono hizo una llamada a las 6 a.m. de hoy. Duró 30 segundos. La torre que la registró está en la carretera hacia Abancay.

```python
# Nueva información: llamada registrada en Abancay
# Abancay está a 150 km de Ollantaytambo

torre_abancay = 150  # km desde Pachar
hora_llamada = 6  # a.m.
hora_actual = 11  # a.m.

# Con esta información, ajustamos el intervalo
# Sabemos que hace 5 horas estaba en Abancay (km 150)
distancia_desde_abancay_min = velocidad_min * (hora_actual - hora_llamada)
distancia_desde_abancay_max = velocidad_max * (hora_actual - hora_llamada)

print("=== INTERVALO ACTUALIZADO ===")
print(f"Última ubicación confirmada: Abancay (km 150) a las 6 a.m.")
print(f"Tiempo desde entonces: {hora_actual - hora_llamada} horas")
print(f"Distancia desde Abancay: {distancia_desde_abancay_min:.0f}-{distancia_desde_abancay_max:.0f} km")
print()

# Nuevos destinos probables
destinos_actualizados = {
    'Abancay': 150,
    'Andahuaylas': 220,
    'Ayacucho': 350,
    'Nazca': 500,
    'Arequipa': 550,
    'Cusco (retorno)': 60
}

print("Destinos probables (actualizado):")
for destino, distancia in sorted(destinos_actualizados.items(), key=lambda x: x[1]):
    if distancia_desde_abancay_min <= distancia <= distancia_desde_abancay_max:
        prob = "ALTA"
    elif abs(distancia - distancia_desde_abancay_min) < 50 or abs(distancia - distancia_desde_abancay_max) < 50:
        prob = "MEDIA"
    else:
        prob = "BAJA"
    print(f"  {destino} ({distancia} km): {prob}")
```

Resultado:

```
=== INTERVALO ACTUALIZADO ===
Última ubicación confirmada: Abancay (km 150) a las 6 a.m.
Tiempo desde entonces: 5 horas
Distancia desde Abancay: 150-300 km

Destinos probables (actualizado):
  Abancay (150 km): ALTA
  Andahuaylas (220 km): ALTA
  Ayacucho (350 km): MEDIA
  Cusco (retorno) (60 km): BAJA
  Nazca (500 km): BAJA
  Arequipa (550 km): BAJA
}

—Andahuaylas o Ayacucho —dijo Valeria—. Está yendo hacia la sierra sur.

—¿Y por qué iría allí?

—Tal vez porque allí hay alguien que puede ayudarla. O tal vez porque allí puede desaparecer para siempre.

---

## El error estándar y la precisión

—La precisión de nuestras estimaciones depende del **error estándar**:

$$EE = \frac{\sigma}{\sqrt{n}}$$

—Cuanto mayor sea la muestra (n), menor será el error estándar y más preciso será nuestro intervalo.

```python
# Cómo el tamaño de la muestra afecta el intervalo de confianza

print("=== EFECTO DEL TAMAÑO DE MUESTRA ===")
print(f"{'n':<10} {'Error Estándar':<18} {'Margen Error (95%)':<20} {'IC'}")
print("-" * 70)

desv_std_ejemplo = 5  # Desviación estándar típica
for n in [10, 30, 50, 100, 500, 1000]:
    error_estandar = desv_std_ejemplo / math.sqrt(n)
    margen = 1.96 * error_estandar
    print(f"{n:<10} {error_estandar:<18.3f} ±{margen:<18.2f} [{25-margen:.1f}, {25+margen:.1f}]")
```

Resultado:

```
=== EFECTO DEL TAMAÑO DE MUESTRA ===
n          Error Estándar    Margen Error (95%)   IC
----------------------------------------------------------------------
10         1.581             ±3.10                [21.9, 28.1]
30         0.913             ±1.79                [23.2, 26.8]
50         0.707             ±1.39                [23.6, 26.4]
100        0.500             ±0.98                [24.0, 26.0]
500        0.224             ±0.44                [24.6, 25.4]
1000       0.158             ±0.31                [24.7, 25.3]
```

—Cuantos más datos tenemos, más preciso es nuestro intervalo. Pero la precisión aumenta con la raíz cuadrada de n. Para duplicar la precisión, necesitamos cuadruplicar la muestra.

—Como en la investigación —dijo Marco—. Cada nueva pista nos da más precisión, pero nunca certeza absoluta.

—Exactamente. Y ahora, nuestra mejor estimación dice que Sofía va hacia Andahuaylas. Vamos.

---

## Enigmas

### Enigma 9.1: Calcula el intervalo

Una muestra de 100 personas tiene una media de ingresos de S/2,500 con una desviación estándar de S/800.

1. Calcula el error estándar
2. Calcula el intervalo de confianza del 95%
3. Interpreta el resultado

### Enigma 9.2: El tamaño importa

¿Qué tamaño de muestra necesitarías para tener un margen de error de ±S/100 con 95% de confianza, si la desviación estándar es S/800?

### Enigma 9.3: Aplica al caso

Si Sofía fue vista en Andahuaylas a las 8 a.m. (a 220 km de Pachar) y ahora son las 2 p.m., ¿cuál es tu intervalo de confianza para su ubicación actual? Usa velocidades de 30-60 km/h.

---

## Lo que aprendiste

- El **intervalo de confianza** da un rango para el valor real de un parámetro
- El **nivel de confianza** (95%) indica qué tan seguros estamos
- El **margen de error** depende del error estándar y del nivel de confianza
- El **error estándar** = σ / √n
- Mayor muestra → menor error → intervalo más preciso
- Nunca hay certeza absoluta, solo intervalos de confianza

Valeria aceleró en la carretera hacia Andahuaylas. El intervalo de confianza decía que Sofía estaba allí. Pero los intervalos de confianza no siempre aciertan.

Y ella lo sabía.

