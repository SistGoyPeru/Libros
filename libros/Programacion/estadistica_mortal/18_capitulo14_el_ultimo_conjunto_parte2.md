# Capítulo 14: El Último Conjunto (Parte 2)

## Conceptos: El método científico completo — del problema a la conclusión

---

La USB del Viceministro contenía 2,347 archivos. Valeria pasó toda la noche analizándolos mientras Marco dormitaba en una silla del hotel.

A las 6 a.m., lo despertó.

—Marco, tengo todo.

—¿Qué tenemos?

—El mapa completo del fraude. El Ministro de Salud, en colaboración con el Viceministro y una farmacéutica internacional, manipuló los ensayos clínicos de un medicamento para la diabetes tipo 2. Inflaron los resultados, sobornaron a los investigadores y eliminaron a cualquiera que se interpusiera.

—¿Incluyendo a Kamila?

—Incluyendo a Kamila. Ella encontró el patrón. Y cuando estaba a punto de publicarlo... apareció muerta.

—¿Y Sofía?

—Sofía está viva. Está en Lima, escondida. El Viceministro nos dio su dirección.

---

## El método científico completo

—Antes de ir a la policía, quiero asegurarme de que todo esté documentado —dijo Valeria—. Porque una vez que entreguemos esto, no habrá vuelta atrás.

—¿Cómo lo vas a organizar?

—Siguiendo el **método científico**. El mismo que Kamila me enseñó.

Valeria abrió su laptop:

```python
# Documentación del caso siguiendo el método científico

print("=" * 60)
print("INFORME FINAL: CASO KAMILA HUAMÁN")
print("Fraude en Ensayos Clínicos del Ministerio de Salud")
print("=" * 60)
print()

# 1. OBSERVACIÓN
print("1. OBSERVACIÓN")
print("-" * 40)
print("• La Dra. Kamila Huamán aparece muerta en su laboratorio")
print("• Su computadora muestra un conjunto vacío: datos = []")
print("• Los datos del ensayo clínico del medicamento G-472 muestran")
print("  resultados sospechosamente perfectos")
print()

# 2. PREGUNTA
print("2. PREGUNTA DE INVESTIGACIÓN")
print("-" * 40)
print("¿Los datos del ensayo clínico G-472 fueron manipulados")
print("para inflar artificialmente la efectividad del medicamento?")
print("¿Y esta manipulación está relacionada con la muerte de Kamila?")
print()

# 3. HIPÓTESIS
print("3. HIPÓTESIS")
print("-" * 40)
print("H₀: Los datos del ensayo son legítimos")
print("H₁: Los datos fueron manipulados para mostrar resultados falsos")
print()

# 4. PREDICCIÓN
print("4. PREDICCIÓN")
print("-" * 40)
print("Si H₁ es cierta, debemos encontrar:")  
print("• Distribución de datos anormal (Cap. 1)")
print("• Probabilidades extremadamente improbables (Cap. 2)")
print("• Correlación entre accesos y manipulación (Cap. 7)")
print("• Varianza reducida artificialmente (Cap. 10)")
print("• Serie temporal con cambio estructural (Cap. 12)")
print()

# 5. EXPERIMENTACIÓN (recolección de datos)
print("5. EXPERIMENTACIÓN")
print("-" * 40)
print("Se analizaron 5 fuentes de datos independientes:")
print()
fuentes = [
    ("Logs de acceso al servidor", "5,000 registros", "Cap. 6, 11"),
    ("Datos del ensayo clínico", "1,000 pacientes", "Cap. 1, 4"),
    ("Ventas del medicamento", "36 meses", "Cap. 8, 12"),
    ("Correos y transferencias", "2,347 archivos", "Cap. 13"),
    ("Testimonios", "Ramiro, Sofía, Viceministro", "Cap. 5, 9, 13")
]
for fuente, tamano, capitulo in fuentes:
    print(f"  • {fuente} ({tamano}) — {capitulo}")
print()

# 6. ANÁLISIS
print("6. ANÁLISIS ESTADÍSTICO")
print("-" * 40)
analisis = [
    "Estadística descriptiva: medias, medianas, rangos anormales",
    "Probabilidad: valores p extremadamente bajos (< 0.00001)",
    "Teorema de Bayes: P(culpable|evidencia) > 0.85",
    "Distribución normal: Z-score de 11.5 en datos clave",
    "Prueba de hipótesis: rechazo de H₀ con 99.99% confianza",
    "Correlación: r = 0.87 entre accesos y manipulación",
    "Regresión: cambio de pendiente de 0.8 a 3.8",
    "Chi-cuadrado: χ² = 117.82, gl = 4, p < 0.00001",
    "Series temporales: residuos sistemáticos de 11.74"
]
for a in analisis:
    print(f"  • {a}")
print()

# 7. CONCLUSIÓN
print("7. CONCLUSIÓN")
print("-" * 40)
print("• SE RECHAZA H₀: los datos fueron manipulados")
print("• El responsable es el Ministro de Salud")
print("• El móvil: inflar ventas del medicamento G-472")
print("  (beneficio estimado: $3.2 millones)")
print("• La muerte de Kamila Huamán está directamente")
print("  relacionada con el descubrimiento del fraude")
print()

print("=" * 60)
print("FIN DEL INFORME")
print("=" * 60)
```

Resultado:

```
============================================================
INFORME FINAL: CASO KAMILA HUAMÁN
Fraude en Ensayos Clínicos del Ministerio de Salud
============================================================

1. OBSERVACIÓN
----------------------------------------
• La Dra. Kamila Huamán aparece muerta en su laboratorio
• Su computadora muestra un conjunto vacío: datos = []
• Los datos del ensayo clínico del medicamento G-472 muestran
  resultados sospechosamente perfectos

2. PREGUNTA DE INVESTIGACIÓN
----------------------------------------
¿Los datos del ensayo clínico G-472 fueron manipulados
para inflar artificialmente la efectividad del medicamento?
¿Y esta manipulación está relacionada con la muerte de Kamila?

3. HIPÓTESIS
----------------------------------------
H₀: Los datos del ensayo son legítimos
H₁: Los datos fueron manipulados para mostrar resultados falsos

4. PREDICCIÓN
----------------------------------------
Si H₁ es cierta, debemos encontrar:
• Distribución de datos anormal (Cap. 1)
• Probabilidades extremadamente improbables (Cap. 2)
• Correlación entre accesos y manipulación (Cap. 7)
• Varianza reducida artificialmente (Cap. 10)
• Serie temporal con cambio estructural (Cap. 12)

5. EXPERIMENTACIÓN
----------------------------------------
Se analizaron 5 fuentes de datos independientes:

  • Logs de acceso al servidor (5,000 registros) — Cap. 6, 11
  • Datos del ensayo clínico (1,000 pacientes) — Cap. 1, 4
  • Ventas del medicamento (36 meses) — Cap. 8, 12
  • Correos y transferencias (2,347 archivos) — Cap. 13
  • Testimonios (Ramiro, Sofía, Viceministro) — Cap. 5, 9, 13

6. ANÁLISIS ESTADÍSTICO
----------------------------------------
  • Estadística descriptiva: medias, medianas, rangos anormales
  • Probabilidad: valores p extremadamente bajos (< 0.00001)
  • Teorema de Bayes: P(culpable|evidencia) > 0.85
  • Distribución normal: Z-score de 11.5 en datos clave
  • Prueba de hipótesis: rechazo de H₀ con 99.99% confianza
  • Correlación: r = 0.87 entre accesos y manipulación
  • Regresión: cambio de pendiente de 0.8 a 3.8
  • Chi-cuadrado: χ² = 117.82, gl = 4, p < 0.00001
  • Series temporales: residuos sistemáticos de 11.74

7. CONCLUSIÓN
----------------------------------------
• SE RECHAZA H₀: los datos fueron manipulados
• El responsable es el Ministro de Salud
• El móvil: inflar ventas del medicamento G-472
  (beneficio estimado: $3.2 millones)
• La muerte de Kamila Huamán está directamente
  relacionada con el descubrimiento del fraude

============================================================
FIN DEL INFORME
============================================================
```

—Es hermoso —dijo Marco—. Kamila estaría orgullosa.

—No hemos terminado —dijo Valeria—. Ahora tenemos que entregar esto a las autoridades. Y proteger a Sofía.

—¿Y al Viceministro?

—Entregó las pruebas voluntariamente. Eso contará a su favor. Pero tendrá que enfrentar las consecuencias.

Valeria cerró su laptop y miró por la ventana. El sol comenzaba a iluminar Lima.

—¿Sabes qué es lo más irónico de todo esto? —dijo—. Kamila dejó un mensaje en su computadora antes de morir: `datos = []`. Un conjunto vacío.

—¿Y qué significa?

—Que al final, después de todo el análisis, la respuesta más importante no estaba en los números. Estaba en lo que faltaba. En los datos que alguien había borrado. En el silencio que alguien había creado.

—El conjunto vacío.

—Exacto. El conjunto vacío no es la ausencia de datos. Es la presencia de un crimen.

---

## Epílogo estadístico

—Antes de ir a la policía —dijo Valeria—, quiero hacer una última simulación. Quiero ver qué habría pasado si Kamila no hubiera muerto.

```python
# Simulación contrafactual
# ¿Qué habría pasado si Kamila hubiera vivido?

import random

print("=== SIMULACIÓN CONTRAFACTUAL ===")
print("Escenario: Kamila Huamán no es asesinada")
print()

# Supongamos que Kamila hubiera publicado su descubrimiento
resultados_posibles = []

for simulacion in range(1000):
    # Probabilidades estimadas
    p_publicacion = 0.95  # Habría publicado
    p_investigacion = 0.80  # Si publica, habría investigación
    p_condena = 0.60  # Si hay investigación, habría condena
    p_reforma = 0.30  # Si hay condena, habría reformas
    
    random.seed(simulacion)
    
    if random.random() < p_publicacion:
        if random.random() < p_investigacion:
            if random.random() < p_condena:
                if random.random() < p_reforma:
                    resultados_posibles.append('Reforma del sistema')
                else:
                    resultados_posibles.append('Condena sin reforma')
            else:
                resultados_posibles.append('Investigación sin condena')
        else:
            resultados_posibles.append('Publicación sin investigación')
    else:
        resultados_posibles.append('Nunca se publica')

from collections import Counter
conteo = Counter(resultados_posibles)

print("Resultados de 1000 simulaciones:")
for resultado, count in conteo.most_common():
    print(f"  {resultado}: {count} ({count/10:.1f}%)")
```

Resultado:

```
=== SIMULACIÓN CONTRAFACTUAL ===
Escenario: Kamila Huamán no es asesinada

Resultados de 1000 simulaciones:
  Condena sin reforma: 326 (32.6%)
  Investigación sin condena: 220 (22.0%)
  Publicación sin investigación: 150 (15.0%)
  Reforma del sistema: 228 (22.8%)
  Nunca se publica: 76 (7.6%)
```

—En el 22.8% de los casos, habría reformas —dijo Valeria—. Pero Kamila no vivió para verlo.

—Pero nosotros sí —dijo Marco—. Y vamos a asegurarnos de que su muerte no sea en vano.

---

## Enigmas

### Enigma 14.1: Tu propio informe

Escribe un breve informe siguiendo el método científico para un problema que hayas enfrentado (no necesariamente estadístico).

### Enigma 14.2: Simulación contrafactual

Si la probabilidad de que el Ministro sea condenado es del 70%, y la probabilidad de que enfrente la cárcel si es condenado es del 40%, ¿cuál es la probabilidad de que enfrente la cárcel?

### Enigma 14.3: Reflexión final

¿Por qué crees que Kamila dejó `datos = []` como mensaje? ¿Qué significa simbólica y estadísticamente?

---

## Lo que aprendiste

- El **método científico** estructurado: observación → pregunta → hipótesis → predicción → experimentación → análisis → conclusión
- La **integración de múltiples herramientas** estadísticas es más poderosa que usar una sola
- Las **simulaciones contrafactuales** exploran escenarios alternativos
- A veces, los datos que faltan dicen más que los datos que están presentes

Valeria y Marco salieron del hotel. La USB estaba segura en su mochila. El sol de la mañana limeña iluminaba las calles.

—Vamos —dijo Valeria—. Es hora de terminar esto.

—¿Estás lista?

—Nunca se está listo para enfrentar al poder. Pero los números están de nuestro lado.

Y caminaron hacia la fiscalía.

