# Capítulo 11: La Prueba del Chi-Cuadrado

## Conceptos: Prueba de chi-cuadrado (χ²), tablas de contingencia, frecuencias observadas vs esperadas, independencia

---

Valeria recibió una llamada cuando salían de Andahuaylas. Era Ramiro.

—Encontré algo —dijo—. En los logs del ministerio. Hay un patrón de accesos que no habíamos visto.

—¿Qué tipo de patrón?

—Accesos desde una IP del Ministerio de Salud. Pero no desde una computadora cualquiera: desde el despacho del Viceministro.

—¿Del viceministro?

—Sí. Y los accesos coinciden exactamente con las fechas en que los datos fueron manipulados. La probabilidad de que sea una coincidencia es... calculémosla con chi-cuadrado.

---

## Chi-cuadrado: la prueba de independencia

—La **prueba de chi-cuadrado (χ²)** se usa para determinar si existe una asociación significativa entre dos variables categóricas. Es perfecta para nuestro caso: queremos saber si hay relación entre "persona" y "acceso nocturno".

—La fórmula es:

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

Donde:
- **O** = frecuencia observada
- **E** = frecuencia esperada (si no hubiera relación)

Valeria abrió Python cuando llegaron a un café con WiFi:

```python
# Prueba de chi-cuadrado para el caso

import numpy as np
import math
from collections import Counter

# TABLA DE CONTINGENCIA: Persona vs Acceso Nocturno
# Filas: personas (Hugo, Ramiro, Sofia, Viceministro, otros)
# Columnas: accesos nocturnos (Sí, No)

# Frecuencias observadas
# Extraído de los logs del ministerio
tabla_observada = np.array([
    [5,  73],    # Hugo: 5 accesos nocturnos, 73 diurnos
    [1,  45],    # Ramiro: 1 nocturno, 45 diurnos
    [3,  89],    # Sofia: 3 nocturnos, 89 diurnos
    [12, 28],    # Viceministro: 12 nocturnos, 28 diurnos
    [8,  736]    # Otros: 8 nocturnos, 736 diurnos
])

personas = ['Hugo', 'Ramiro', 'Sofia', 'Viceministro', 'Otros']
total_observado = np.sum(tabla_observada)

print("=== TABLA DE CONTINGENCIA ===")
print(f"{'Persona':<18} {'Nocturnos':<12} {'Diurnos':<12} {'Total':<12}")
print("-" * 54)
for i, persona in enumerate(personas):
    nocturnos = tabla_observada[i, 0]
    diurnos = tabla_observada[i, 1]
    total = nocturnos + diurnos
    print(f"{persona:<18} {nocturnos:<12} {diurnos:<12} {total:<12}")
print("-" * 54)
totales_columna = np.sum(tabla_observada, axis=0)
print(f"{'Total':<18} {totales_columna[0]:<12} {totales_columna[1]:<12} {total_observado:<12}")
```

Resultado:

```
=== TABLA DE CONTINGENCIA ===
Persona            Nocturnos     Diurnos       Total         
------------------------------------------------------
Hugo               5             73            78            
Ramiro             1             45            46            
Sofia              3             89            92            
Viceministro       12            28            40            
Otros              8             736           744           
------------------------------------------------------
Total              29            971           1000          
```

—Ahora calculamos las frecuencias **esperadas**. Si no hubiera relación entre la persona y los accesos nocturnos, la proporción de accesos nocturnos sería la misma para todos: 29/1000 = 2.9%.

```python
# Frecuencias esperadas (bajo la hipótesis de independencia)
proporcion_nocturna = totales_columna[0] / total_observado
print(f"\nProporción general de accesos nocturnos: {proporcion_nocturna:.4f} ({proporcion_nocturna*100:.1f}%)")

# Frecuencias esperadas para cada celda
# E = (total_fila * total_columna) / total_general
tabla_esperada = np.zeros_like(tabla_observada, dtype=float)
for i in range(len(personas)):
    total_fila = np.sum(tabla_observada[i, :])
    for j in range(2):
        tabla_esperada[i, j] = (total_fila * totales_columna[j]) / total_observado

print(f"\n=== FRECUENCIAS ESPERADAS ===")
print(f"{'Persona':<18} {'Nocturnos (esp)':<18} {'Diurnos (esp)':<18}")
print("-" * 54)
for i, persona in enumerate(personas):
    print(f"{persona:<18} {tabla_esperada[i, 0]:<18.1f} {tabla_esperada[i, 1]:<18.1f}")
```

Resultado:

```
Proporción general de accesos nocturnos: 0.0290 (2.9%)

=== FRECUENCIAS ESPERADAS ===
Persona            Nocturnos (esp)   Diurnos (esp)    
------------------------------------------------------
Hugo               2.3               75.7             
Ramiro             1.3               44.7             
Sofia              2.7               89.3             
Viceministro       1.2               38.8             
Otros              21.6              722.4            
```

—Y ahora calculamos el chi-cuadrado:

```python
# Cálculo del chi-cuadrado
chi_cuadrado = 0
for i in range(len(personas)):
    for j in range(2):
        o = tabla_observada[i, j]
        e = tabla_esperada[i, j]
        contribucion = (o - e) ** 2 / e
        chi_cuadrado += contribucion
        if contribucion > 1:
            print(f"  {personas[i]}: contribución significativa = {contribucion:.2f}")

print(f"\n=== RESULTADO CHI-CUADRADO ===")
print(f"χ² = {chi_cuadrado:.2f}")

# Grados de libertad = (filas - 1) * (columnas - 1) = (5-1)*(2-1) = 4
gl = (len(personas) - 1) * (2 - 1)
print(f"Grados de libertad: {gl}")

# Valor crítico para α = 0.05 con 4 gl ≈ 9.49
valor_critico = 9.49
print(f"Valor crítico (α=0.05): {valor_critico}")

if chi_cuadrado > valor_critico:
    print(f"→ χ² ({chi_cuadrado:.2f}) > valor crítico ({valor_critico})")
    print(f"→ RECHAZAMOS H₀: existe relación significativa entre")
    print(f"  la persona y los accesos nocturnos")
else:
    print(f"→ No hay evidencia suficiente para rechazar H₀")
```

Resultado:

```
Hugo: contribución significativa = 3.37
Viceministro: contribución significativa = 103.20
Otros: contribución significativa = 8.81

=== RESULTADO CHI-CUADRADO ===
χ² = 117.82
Grados de libertad: 4
Valor crítico (α=0.05): 9.49
→ χ² (117.82) > valor crítico (9.49)
→ RECHAZAMOS H₀: existe relación significativa entre
  la persona y los accesos nocturnos
```

—El chi-cuadrado es 117.82 —dijo Valeria—. El valor crítico para 95% de confianza es 9.49. Esto es más de 10 veces el valor crítico.

—¿Y qué significa eso exactamente?

—Que la probabilidad de que esta distribución sea producto del azar es esencialmente cero. El Viceministro tiene una cantidad anormal de accesos nocturnos. Y la contribución al chi-cuadrado del Viceministro es de 103.20 de 117.82 totales. Es decir, el 87.6% de la señal viene de él.

—El Viceministro es nuestro hombre —dijo Marco.

—Estadísticamente, sí. Ahora necesitamos la prueba directa.

---

## La prueba de bondad de ajuste

—Hay otra forma de usar chi-cuadrado —dijo Valeria—: la **prueba de bondad de ajuste**. Sirve para ver si una distribución observada coincide con una distribución esperada.

—Por ejemplo, si los datos del ensayo clínico siguieran una distribución normal, las frecuencias deberían distribuirse de cierta manera.

```python
# Prueba de bondad de ajuste para los datos del ensayo

# Datos observados del ensayo (tratamiento A)
mejora_observada = 470
no_mejora_observada = 30

# Frecuencias esperadas bajo H₀ (sin efecto del tratamiento)
# Si el tratamiento no tuviera efecto, esperaríamos la misma
# proporción de mejora que en el grupo de control (48%)
tasa_control = 0.48
mejora_esperada = 500 * tasa_control
no_mejora_esperada = 500 * (1 - tasa_control)

print("=== PRUEBA DE BONDAD DE AJUSTE ===")
print(f"{'':<20} {'Observado':<15} {'Esperado':<15} {'(O-E)²/E':<15}")
print("-" * 65)
for categoria, obs, esp in [("Mejora", mejora_observada, mejora_esperada),
                              ("No mejora", no_mejora_observada, no_mejora_esperada)]:
    contrib = (obs - esp) ** 2 / esp
    print(f"{categoria:<20} {obs:<15} {esp:<15.1f} {contrib:<15.2f}")

chi2_bondad = (mejora_observada - mejora_esperada)**2 / mejora_esperada + \
              (no_mejora_observada - no_mejora_esperada)**2 / no_mejora_esperada

print(f"\nχ² (bondad de ajuste) = {chi2_bondad:.2f}")
print(f"Grados de libertad: 1")
print(f"Valor crítico (α=0.05): 3.84")
print(f"→ {'RECHAZAMOS' if chi2_bondad > 3.84 else 'NO RECHAZAMOS'} H₀")
print(f"→ Los datos NO siguen la distribución esperada")
print(f"→ El tratamiento A tiene un efecto estadísticamente")
print(f"  significativo... pero es DEMASIADO significativo")
```

Resultado:

```
=== PRUEBA DE BONDAD DE AJUSTE ===
                     Observado        Esperado         (O-E)²/E         
-----------------------------------------------------------------
Mejora               470              240.0            220.42           
No mejora            30               260.0            203.46           

χ² (bondad de ajuste) = 423.88
Grados de libertad: 1
Valor crítico (α=0.05): 3.84
→ RECHAZAMOS H₀
→ Los datos NO siguen la distribución esperada
→ El tratamiento A tiene un efecto estadísticamente
  significativo... pero es DEMASIADO significativo
```

—423.88 —dijo Valeria—. Para que te des una idea, un chi-cuadrado de 10 ya es extremadamente significativo. Esto es 40 veces más. Es como lanzar una moneda y obtener cara 100 veces seguidas.

—No hay duda —dijo Marco—. Los datos fueron fabricados.

—Y el Viceministro es el responsable estadístico. Pero la estadística no es una condena judicial. Necesitamos la evidencia física.

---

## El veredicto estadístico

—En estadística —dijo Valeria—, nunca decimos "esto es cierto". Decimos "rechazamos la hipótesis nula con un nivel de confianza del 95%". Pero en este caso, los números hablan por sí solos.

```python
# Resumen de toda la evidencia estadística
print("=== RESUMEN DE EVIDENCIA ESTADÍSTICA ===")
print()

evidencia = [
    ("Manipulación de datos del ensayo", "Z-score = 11.5", "Extremadamente significativo"),
    ("Accesos nocturnos del Viceministro", f"χ² = {chi_cuadrado:.1f} (gl=4)", "p < 0.00001"),
    ("Reducción artificial de varianza", "CV: 2.96% → 0.56%", "Firma de manipulación"),
    ("Correlación IP-nocturna", "r = 0.87", "Correlación muy fuerte"),
    ("Regresión inconsistente", "R²: 0.72 → 0.96", "Datos 'demasiado perfectos'"),
    ("Desaparición de Ramiro y Sofía", "Bayes: P(culpable|evidencia) = 0.85", "Probabilidad alta"),
]

print(f"{'Evidencia':<45} {'Estadístico':<35} {'Conclusión':<35}")
print("-" * 115)
for item in evidencia:
    print(f"{item[0]:<45} {item[1]:<35} {item[2]:<35}")
print()
print("→ La evidencia estadística apunta al Viceministro de Salud")
print("→ Pero necesitamos la prueba definitiva")
```

—¿Y cuál es la prueba definitiva? —preguntó Marco.

—Una confesión. O un documento que lo vincule directamente.

—¿Y cómo conseguimos eso?

Valeria guardó su laptop.

—Hablando con la única persona que puede dártelo: el propio Viceministro.

---

## Enigmas

### Enigma 11.1: Calcula chi-cuadrado

Tienes una encuesta sobre preferencia política por género:

|        | Hombre | Mujer |
|--------|--------|-------|
| Partido A | 120 | 80 |
| Partido B | 90 | 110 |

1. Calcula las frecuencias esperadas
2. Calcula el chi-cuadrado
3. ¿Hay relación entre género y preferencia política?

### Enigma 11.2: Bondad de ajuste

Un dado se lanza 120 veces con estos resultados:

| Cara | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| Frecuencia | 25 | 18 | 22 | 20 | 15 | 20 |

¿El dado está cargado? Usa chi-cuadrado con α = 0.05.

### Enigma 11.3: Aplica al caso

Si agregamos una nueva fila a la tabla de contingencia con los datos de un nuevo sospechoso llamado "Ministro" que tiene 8 accesos nocturnos y 12 diurnos, ¿cómo cambia el chi-cuadrado? ¿Es más o menos sospechoso que el Viceministro?

---

## Lo que aprendiste

- La **prueba de chi-cuadrado (χ²)** evalúa la relación entre variables categóricas
- χ² = Σ((O - E)² / E)
- **Tablas de contingencia**: organizan frecuencias observadas
- **Frecuencias esperadas**: las que esperaríamos si no hubiera relación
- **Bondad de ajuste**: compara una distribución observada con una esperada
- Un χ² alto sugiere que los datos NO son producto del azar

—Vamos a Lima —dijo Valeria—. Vamos a hablar con el Viceministro.

—¿Y si es peligroso?

—Lo es. Pero Kamila merece justicia. Y los números no mienten.

Marco arrancó el auto.

—Entonces vamos.

