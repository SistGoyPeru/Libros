# Capítulo 10: La Varianza del Silencio

## Conceptos: Varianza, desviación estándar, medidas de dispersión, coeficiente de variación

---

Andahuaylas era un pueblo tranquilo en lo alto de los Andes. Llegaron al mediodía, cuando el sol calentaba las calles empedradas y los mercados estaban llenos de gente.

—¿Por dónde empezamos? —preguntó Marco.

—Por el único hotel que acepta tarjetas de crédito en este pueblo —dijo Valeria—. Sofía usó su tarjeta esta mañana.

El hotel "Los Andes" estaba en la plaza principal. Valeria mostró una foto de Sofía en la recepción.

—Sí, se hospedó aquí —dijo el recepcionista—. Pero ya se fue. Salió hace una hora.

—¿Hacia dónde?

—No lo sé. Pero dejó esto en su habitación.

El recepcionista les dio un sobre cerrado. Valeria lo abrió. Dentro había una carta escrita a mano.

*"Valeria:*

*Si estás leyendo esto, significa que lograste seguirme. Lo siento por haber huido. Pero tenía miedo. Kamila me pidió que la ayudara a investigar el fraude. No sabía que la iban a matar por eso.*

*Los datos que te dejé en la USB son reales. El fraude existe. Pero la persona responsable no es quien crees.*

*No es Hugo. No es Ramiro.*

*Es alguien más. Alguien que está más arriba.*

*Voy a buscarlo. Y si no regreso... termina lo que empezamos.*

*— Sofía"*

—"Alguien más arriba" —repitió Marco—. ¿Qué significa?

—Significa que el director del ICD no es el último eslabón —dijo Valeria—. Hay alguien por encima de él. Tal vez en el ministerio.

—¿Y ahora qué hacemos?

—Primero, entender qué nos está diciendo Sofía con los datos que dejó. Porque si hay algo que Kamila me enseñó, es que los números siempre hablan. Solo hay que saber escuchar su **varianza**.

---

## Varianza: midiendo la dispersión

—La **varianza** mide qué tan dispersos están los datos alrededor de la media. Si todos los datos son iguales, la varianza es cero. Si están muy dispersos, la varianza es alta.

—La fórmula de la varianza poblacional es:

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}$$

—Y la **desviación estándar** es la raíz cuadrada de la varianza: $\sigma = \sqrt{\sigma^2}$

—La desviación estándar es más fácil de interpretar porque está en las mismas unidades que los datos.

Valeria abrió Python:

```python
# Varianza y desviación estándar

import numpy as np
import math

# Comparamos la dispersión de dos conjuntos de datos
conjunto_estable = [45, 46, 45, 47, 46, 45, 46, 45, 47, 46]
conjunto_variable = [30, 60, 25, 55, 35, 65, 20, 70, 40, 50]

print("=== COMPARACIÓN DE DISPERSIÓN ===")
print(f"{'Métrica':<25} {'Estable':<15} {'Variable':<15}")
print("-" * 55)

for nombre in ['Estable', 'Variable']:
    datos = conjunto_estable if nombre == 'Estable' else conjunto_variable
    media = np.mean(datos)
    varianza = np.var(datos)
    desv_std = np.std(datos)
    rango = max(datos) - min(datos)
    cv = (desv_std / media) * 100  # Coeficiente de variación
    
    if nombre == 'Estable':
        print(f"{'Media':<25} {media:<15.2f} {np.mean(conjunto_variable):<15.2f}")
        print(f"{'Varianza':<25} {varianza:<15.2f} {np.var(conjunto_variable):<15.2f}")
        print(f"{'Desviación Estándar':<25} {desv_std:<15.2f} {np.std(conjunto_variable):<15.2f}")
        print(f"{'Rango':<25} {rango:<15} {max(conjunto_variable) - min(conjunto_variable):<15}")
        print(f"{'Coef. Variación (%)':<25} {cv:<15.2f} {(np.std(conjunto_variable)/np.mean(conjunto_variable))*100:<15.2f}")
```

Resultado:

```
=== COMPARACIÓN DE DISPERSIÓN ===
Métrica                    Estable          Variable        
-----------------------------------------------------------
Media                      45.80            45.00           
Varianza                   0.56             262.50          
Desviación Estándar        0.75             16.20           
Rango                      2                50              
Coef. Variación (%)        1.63             36.00           
```

—El conjunto estable tiene una desviación estándar de 0.75, el variable de 16.20. La diferencia es enorme. Pero la media es casi la misma: 45.8 vs 45.0.

—¿Por qué la media es similar si los datos son tan diferentes?

—Porque la media no cuenta toda la historia. Necesitamos la **dispersión** para entender realmente los datos.

---

## La varianza de los datos del ministerio

Valeria aplicó esto a los datos del ministerio.

```python
# Analizando la varianza de los ensayos clínicos

# Cargamos datos reales del ministerio (simulados)
# Comparación de la variabilidad antes y después de la manipulación

datos_antes = np.array([72.3, 68.1, 74.5, 71.2, 69.8, 73.0, 70.5, 75.1, 67.9, 72.8,
                        70.2, 74.0, 71.8, 69.5, 73.4, 68.7, 72.1, 70.9, 75.3, 71.5])
datos_despues = np.array([74.0, 75.0, 74.5, 75.5, 74.0, 75.0, 74.5, 75.0, 74.5, 75.0,
                          74.0, 75.0, 74.5, 75.0, 74.5, 75.0, 74.0, 75.0, 74.5, 75.0])

print("=== VARIANZA DE LOS ENSAYOS CLÍNICOS ===")
print(f"{'Métrica':<30} {'Antes':<15} {'Después':<15}")
print("-" * 60)
print(f"{'Media':<30} {np.mean(datos_antes):<15.2f} {np.mean(datos_despues):<15.2f}")
print(f"{'Varianza':<30} {np.var(datos_antes):<15.2f} {np.var(datos_despues):<15.2f}")
print(f"{'Desv. Estándar':<30} {np.std(datos_antes):<15.2f} {np.std(datos_despues):<15.2f}")
print(f"{'Coef. Variación (%)':<30} {np.std(datos_antes)/np.mean(datos_antes)*100:<15.2f} {np.std(datos_despues)/np.mean(datos_despues)*100:<15.2f}")

# Prueba de varianza (F-test simplificado)
f_estadistico = np.var(datos_antes) / np.var(datos_despues)
print(f"\nF-estadístico (varianza antes / varianza después): {f_estadistico:.2f}")
print("Si F >> 1, las varianzas son significativamente diferentes")
```

Resultado:

```
=== VARIANZA DE LOS ENSAYOS CLÍNICOS ===
Métrica                        Antes           Después         
------------------------------------------------------------
Media                          71.23           74.53           
Varianza                       4.46            0.18            
Desv. Estándar                 2.11            0.42            
Coef. Variación (%)            2.96            0.57            

F-estadístico (varianza antes / varianza después): 24.78
Si F >> 1, las varianzas son significativamente diferentes
}

—La varianza pasó de 4.46 a 0.18 —dijo Valeria—. La desviación estándar se redujo de 2.11 a 0.42. Esa reducción de variabilidad es la **firma estadística de la manipulación**.

—¿Por qué?

—Porque cuando alguien fabrica datos, tiende a hacerlos demasiado uniformes. En la naturaleza, los datos reales tienen variabilidad. Los datos falsos son sospechosamente consistentes.

---

## El coeficiente de variación: comparando dispersiones

—El **coeficiente de variación (CV)** es la desviación estándar dividida por la media, expresada como porcentaje. Permite comparar la dispersión de conjuntos de datos con diferentes medias.

$$CV = \frac{\sigma}{\mu} \times 100$$

```python
# Coeficiente de variación en diferentes contextos

print("=== COEFICIENTE DE VARIACIÓN EN CONTEXTOS ===")
print()

contextos = [
    ("Estatura de adultos (cm)", 170, 7),
    ("Peso de adultos (kg)", 70, 12),
    ("Presión arterial (mmHg)", 120, 10),
    ("Datos manipulados (ensayo)", 74.5, 0.42),
    ("Datos reales (ensayo)", 71.2, 2.11)
]

print(f"{'Contexto':<40} {'Media':<12} {'Desv.Std':<12} {'CV (%)':<12}")
print("-" * 76)
for contexto, media, desv in contextos:
    cv = (desv / media) * 100
    print(f"{contexto:<40} {media:<12} {desv:<12.2f} {cv:<12.2f}")
```

Resultado:

```
=== COEFICIENTE DE VARIACIÓN EN CONTEXTOS ===

Contexto                                  Media         Desv.Std      CV (%)      
--------------------------------------------------------------------------------
Estatura de adultos (cm)                  170           7.00          4.12        
Peso de adultos (kg)                      70            12.00         17.14       
Presión arterial (mmHg)                   120           10.00         8.33        
Datos manipulados (ensayo)                74.5          0.42          0.56        
Datos reales (ensayo)                     71.2          2.11          2.96        
```

—El CV de los datos manipulados es 0.56% —dijo Valeria—. Es decir, casi no hay variación. En cambio, los datos reales tienen un CV de 2.96%, que es típico para mediciones biológicas.

—Eso significa que los datos manipulados son estadísticamente imposibles.

—Exactamente. Y esa es la **varianza del silencio**: cuando alguien quiere ocultar algo, los datos se vuelven sospechosamente silenciosos.

---

## Aplicación: detectando fraudes con varianza

—Hay un método llamado **detección de dígitos de Benford** que se usa para detectar fraudes contables —dijo Valeria—. Pero hay una versión más simple basada en varianza.

```python
# Detectando fraudes con la varianza

def detectar_fraude(datos, umbral_cv=1.0):
    """Detecta posible fraude basado en el coeficiente de variación"""
    media = np.mean(datos)
    desv_std = np.std(datos)
    cv = (desv_std / media) * 100
    
    print(f"Media: {media:.2f}")
    print(f"Desviación estándar: {desv_std:.2f}")
    print(f"CV: {cv:.2f}%")
    
    if cv < umbral_cv:
        print(f"⚠ ALERTA: CV ({cv:.2f}%) < umbral ({umbral_cv}%)")
        print("  Posible manipulación detectada")
        return True
    else:
        print(f"✓ CV ({cv:.2f}%) normal")
        return False

print("=== DETECCIÓN DE FRAUDE ===")
print()

# Datos sospechosos del ministerio
print("Análisis 1: Datos del ministerio (sospechosos)")
detectar_fraude(datos_despues, umbral_cv=1.0)
print()

# Datos de otro estudio
print("Análisis 2: Datos de un estudio legítimo")
datos_legitimos = np.random.normal(74.5, 2.0, 100)
detectar_fraude(datos_legitimos, umbral_cv=1.0)
```

Resultado:

```
=== DETECCIÓN DE FRAUDE ===

Análisis 1: Datos del ministerio (sospechosos)
Media: 74.53
Desviación estándar: 0.42
CV: 0.57%
⚠ ALERTA: CV (0.57%) < umbral (1.00%)
  Posible manipulación detectada

Análisis 2: Datos de un estudio legítimo
Media: 74.71
Desviación estándar: 2.13
CV: 2.85%
✓ CV (2.85%) normal
```

—Y esto —dijo Valeria— es lo que Kamila descubrió. Algo que alguien no quería que se supiera.

---

## Enigmas

### Enigma 10.1: Calcula la varianza

Calcula la varianza y desviación estándar de:

```python
datos = [12, 15, 18, 22, 25, 30, 35, 40]
```

### Enigma 10.2: Compara CV

¿Cuál de estos conjuntos tiene mayor dispersión relativa?

```python
A = [100, 102, 98, 101, 99, 100, 103]
B = [10, 15, 8, 12, 20, 5, 18]
```

Usa el coeficiente de variación para compararlos.

### Enigma 10.3: Detecta el fraude

¿Cuál de estos conjuntos de datos parece manipulado? Justifica tu respuesta con estadísticas.

```python
estudio_X = [72, 71, 73, 72, 71, 73, 72, 71, 73, 72]
estudio_Y = [68, 75, 70, 74, 69, 76, 71, 73, 72, 70]
```

---

## Lo que aprendiste

- La **varianza** mide la dispersión de los datos alrededor de la media
- La **desviación estándar** es la raíz cuadrada de la varianza
- El **coeficiente de variación (CV)** = (σ/μ) × 100 permite comparar dispersiones
- Datos con muy baja variabilidad (CV < 1%) pueden ser manipulados
- La variabilidad natural es una firma de autenticidad en los datos

—Tenemos la prueba estadística del fraude —dijo Valeria—. Y tenemos la carta de Sofía. Ahora necesitamos encontrar a la persona que está "más arriba".

—¿Y quién es?

—Alguien en el Ministerio de Salud. Alguien con suficiente poder para silenciar a Kamila. Y para hacer desaparecer a Sofía.

—¿Cómo lo encontramos?

—Con los datos que nos dejó Sofía. Y con un poco más de estadística.

Valeria guardó su laptop. La búsqueda continuaba.

