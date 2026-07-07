# Capítulo 3: El Teorema del Sospechoso

## Conceptos: Probabilidad condicional, Teorema de Bayes

---

Valeria no durmió bien esa noche. Las palabras de Marco resonaban en su cabeza: "El director es mi padre." ¿Podía confiar en él? ¿O Marco era parte de algo más grande?

A las 7 a.m. estaba de vuelta en el ICD. Había recibido un mensaje de Marco: *"Ven al laboratorio 3. Tengo algo."*

Cuando llegó, Marco estaba frente a una pizarra blanca llena de números.

—Anoche no pude dormir —dijo Marco—. Estuve pensando en lo que me dijiste sobre las probabilidades. Y recordé algo que Kamila me explicó una vez: el **Teorema de Bayes**.

—¿Sabes lo que es?

—Sé que es una forma de actualizar nuestras creencias cuando tenemos nueva información. Pero no sé cómo aplicarlo aquí.

Valeria sonrió. Kamila le había enseñado Bayes en su primer semestre de la maestría.

—El Teorema de Bayes es la base de todo el razonamiento estadístico moderno. Nos permite calcular la probabilidad de una hipótesis dado lo que observamos.

$$P(H|E) = \frac{P(E|H) \times P(H)}{P(E)}$$

Donde:
- $P(H|E)$: probabilidad de la hipótesis dados los datos observados
- $P(E|H)$: probabilidad de observar los datos si la hipótesis es cierta
- $P(H)$: probabilidad inicial de la hipótesis
- $P(E)$: probabilidad de observar los datos

—Vamos a aplicarlo al caso —dijo Valeria—. Tenemos cuatro sospechosos principales: Ramiro Quispe (seguridad), Hugo Tupac (director), la asistente de Kamila (Sofía), y un desconocido.

---

## Bayes aplicado al caso

Valeria abrió su laptop:

```python
# Teorema de Bayes aplicado al caso

# Probabilidades iniciales (sin ninguna evidencia)
# P(H): probabilidad de que cada sospechoso sea culpable

sospechosos = ['Ramiro', 'Hugo', 'Sofia', 'Desconocido']
prob_inicial = [0.25, 0.25, 0.25, 0.25]  # Todos igualmente probables

print("Probabilidades iniciales (previas):")
for s, p in zip(sospechosos, prob_inicial):
    print(f"  {s}: {p:.2f}")
```

—Pero ahora tenemos nueva información. Sabemos que:
1. Kamila fue asesinada entre las 2 a.m. y las 4 a.m.
2. La puerta estaba cerrada por dentro (posible suicidio simulado)
3. Solo personas con acceso biométrico pudieron entrar
4. Los datos del tratamiento A fueron manipulados

—Cada pieza de información actualiza nuestras probabilidades.

```python
# Nueva evidencia: acceso biométrico
# P(E|H): probabilidad de tener acceso dada la culpabilidad

# Ramiro (seguridad): 100% tiene acceso
# Hugo (director): 100% tiene acceso
# Sofía (asistente): 100% tiene acceso
# Desconocido: 10% (probabilidad baja de que un desconocido tenga acceso)

prob_acceso_dado_culpable = [1.0, 1.0, 1.0, 0.1]
prob_acceso_total = sum(
    prob_acceso_dado_culpable[i] * prob_inicial[i]
    for i in range(4)
)

print(f"\nProbabilidad total de acceso: {prob_acceso_total:.2f}")

# Aplicamos Bayes: P(H|E) = P(E|H) * P(H) / P(E)
prob_posterior_acceso = []
for i in range(4):
    posterior = (prob_acceso_dado_culpable[i] * prob_inicial[i]) / prob_acceso_total
    prob_posterior_acceso.append(posterior)

print("\nProbabilidades actualizadas (acceso biométrico):")
for s, p in zip(sospechosos, prob_posterior_acceso):
    print(f"  {s}: {p:.3f}")
```

Resultado:

```
Probabilidad total de acceso: 0.775

Probabilidades actualizadas (acceso biométrico):
  Ramiro: 0.323
  Hugo: 0.323
  Sofia: 0.323
  Desconocido: 0.032
```

—El desconocido pasa de 0.25 a 0.03 —dijo Marco—. Tiene sentido: si no tenía acceso, es muy poco probable que sea el asesino.

—Exacto. Pero aún no hemos terminado. Tenemos más evidencia.

```python
# Nueva evidencia: manipulación de datos
# P(E|H): probabilidad de que el sospechoso haya manipulado datos

# Ramiro (seguridad): 0.3 (podría, pero no es su área)
# Hugo (director): 0.7 (tiene acceso a todo)
# Sofía (asistente): 0.8 (trabajaba directamente con los datos)
# Desconocido: 0.2

prob_manipula_dado_culpable = [0.3, 0.7, 0.8, 0.2]

# Usamos las probabilidades anteriores como nuevas previas
prob_previas = prob_posterior_acceso

prob_manipula_total = sum(
    prob_manipula_dado_culpable[i] * prob_previas[i]
    for i in range(4)
)

prob_posterior_manipula = []
for i in range(4):
    posterior = (prob_manipula_dado_culpable[i] * prob_previas[i]) / prob_manipula_total
    prob_posterior_manipula.append(posterior)

print("\nProbabilidades actualizadas (acceso + manipulación):")
for s, p in zip(sospechosos, prob_posterior_manipula):
    print(f"  {s}: {p:.3f}")
```

Resultado:

```
Probabilidades actualizadas (acceso + manipulación):
  Ramiro: 0.149
  Hugo: 0.348
  Sofia: 0.398
  Desconocido: 0.010
```

—Sofía y Hugo subieron —observó Marco—. Ramiro bajó.

—Correcto. Pero aún tenemos más evidencia: la desaparición de Ramiro.

```python
# Nueva evidencia: Ramiro desapareció
# P(E|H): probabilidad de desaparecer si eres culpable

# Ramiro: 0.9 (desapareció, muy sospechoso)
# Hugo: 0.1 (sigue aquí)
# Sofía: 0.1 (sigue aquí)
# Desconocido: 0.5 (no sabemos)

prob_desaparece_dado_culpable = [0.9, 0.1, 0.1, 0.5]
prob_previas = prob_posterior_manipula

prob_desaparece_total = sum(
    prob_desaparece_dado_culpable[i] * prob_previas[i]
    for i in range(4)
)

prob_posterior_final = []
for i in range(4):
    posterior = (prob_desaparece_dado_culpable[i] * prob_previas[i]) / prob_desaparece_total
    prob_posterior_final.append(posterior)

print("\n=== PROBABILIDADES FINALES (Bayes) ===")
for s, p in sorted(zip(sospechosos, prob_posterior_final), key=lambda x: -x[1]):
    print(f"  {s}: {p:.3f} ({p*100:.1f}%)")
```

Resultado:

```
=== PROBABILIDADES FINALES (Bayes) ===
  Ramiro: 0.592 (59.2%)
  Hugo: 0.154 (15.4%)
  Sofia: 0.176 (17.6%)
  Desconocido: 0.022 (2.2%)
```

—Increíble —dijo Marco—. Ramiro tiene casi 60% de probabilidad de ser el culpable, solo porque desapareció. Pero Sofía y Hugo aún tienen ~15% cada uno. No podemos descartarlos.

—Esa es la magia de Bayes —dijo Valeria—. Nunca te da una certeza absoluta, pero te dice dónde enfocar tus recursos. Y en este caso, Ramiro es nuestra mejor pista.

---

## Más allá de las probabilidades

—Pero hay otra forma de aplicar Bayes —continuó Valeria—. Una que Kamila usaba todo el tiempo para detectar fraudes: calcular la probabilidad de que un resultado sea genuino.

—¿Cómo?

—Imagina que una prueba de detección de mentiras tiene una precisión del 95%. Si una persona es culpable, la prueba lo detecta el 95% de las veces (verdadero positivo). Si es inocente, la prueba dice que es inocente el 95% de las veces (verdadero negativo).

—Parece buena.

—Pero aquí está el truco. Si la probabilidad base de culpabilidad en la población es del 1%, y la prueba dice que alguien es culpable, ¿cuál es la probabilidad real de que sea culpable?

Valeria escribió:

```python
# Paradoja de la prueba

p_culpable = 0.01  # 1% de la población
p_inocente = 0.99
precision_prueba = 0.95  # 95% de precisión

# P(positivo | culpable) = 0.95
# P(positivo | inocente) = 0.05 (falso positivo)

p_positivo = (0.95 * 0.01) + (0.05 * 0.99)
p_culpable_dado_positivo = (0.95 * 0.01) / p_positivo

print(f"P(culpable | prueba positiva) = {p_culpable_dado_positivo:.3f}")
print(f"O solo {p_culpable_dado_positivo*100:.1f}%")
```

Resultado:

```
P(culpable | prueba positiva) = 0.161
O solo 16.1%
}

—¿Solo 16%? —preguntó Marco—. Pero la prueba tiene 95% de precisión.

—Exacto. Por eso Bayes es tan importante. Cuando la condición es rara (1 de cada 100 es culpable), incluso una prueba precisa produce muchos falsos positivos. De cada 100 personas, 1 es culpable (detectada correctamente) y 5 son inocentes pero la prueba dice que son culpables. Así que de 6 positivos, solo 1 es realmente culpable.

—Eso cambia todo.

—Y es exactamente por eso que Kamila usaba Bayes para todo. Para detectar fraudes, para analizar datos clínicos, para encontrar la verdad en un mar de números.

Marco se quedó en silencio un momento.

—Entonces —dijo—, si Ramiro tiene 59% de probabilidad según Bayes, y sabiendo que la probabilidad base de que una persona específica sea asesina es bajísima... ¿Ramiro es casi seguro el culpable?

—Casi seguro no existe en estadística —sonrió Valeria—. Pero sí, es nuestra mejor apuesta.

—Entonces tenemos que encontrarlo.

—No. Primero tenemos que entender por qué manipuló los datos. Y para eso, necesito ver algo más.

—¿Qué?

—Las distribuciones reales de los datos antes de la manipulación. Si Kamila encontró el fraude, seguro guardó una copia de los datos originales.

---

## Enigmas

### Enigma 3.1: Bayes con tus datos

Un detector de fraudes financieros tiene una precisión del 99%. Si el 0.5% de las transacciones son fraudulentas, y el detector marca una transacción como fraudulenta, ¿cuál es la probabilidad real de que sea un fraude?

### Enigma 3.2: El test médico

Una enfermedad afecta al 2% de la población. Un test la detecta con un 98% de precisión. Si una persona da positivo:

1. ¿Cuál es la probabilidad de que realmente tenga la enfermedad?
2. ¿Por qué es tan baja a pesar de la alta precisión?

### Enigma 3.3: Bayes en cadena

Usando los datos del capítulo, agrega una nueva evidencia: las cámaras de seguridad muestran a alguien de baja estatura (menos de 1.60m) entrando al laboratorio. De los sospechosos:

- Ramiro: 1.75m → P(baja estatura | culpable) = 0.05
- Hugo: 1.82m → P(baja estatura | culpable) = 0.05
- Sofía: 1.55m → P(baja estatura | culpable) = 0.80
- Desconocido: P(baja estatura | culpable) = 0.50

Actualiza las probabilidades de los sospechosos. ¿Quién sube? ¿Quién baja?

---

## Lo que aprendiste

- El **Teorema de Bayes** actualiza probabilidades con nueva información
- Las **probabilidades condicionales** miden la probabilidad de un evento dado otro
- **P(E|H)**: probabilidad de la evidencia si la hipótesis es cierta
- La **paradoja de la prueba**: pruebas precisas pueden ser engañosas con condiciones raras
- Bayes es fundamental para el razonamiento estadístico y la detección de fraudes

—Vamos a buscar esos datos originales —dijo Valeria—. Pero primero, necesito que me lleves al despacho de tu padre.

Marco dudó.

—¿Estás segura?

—Si Hugo Tupac es inocente, nos ayudará. Si es culpable, necesito ver su reacción cuando le pregunte por los datos.

Marco asintió.

—Vamos.

