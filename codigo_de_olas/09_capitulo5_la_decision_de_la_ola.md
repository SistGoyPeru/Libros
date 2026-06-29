# Capítulo 5: La Decisión de la Ola

## Conceptos: Condicionales `if/elif/else`, operadores lógicos

---

Mateo estaba en la orilla, mirando el mar. El generador submarino seguía activo. Las olas seguían siendo anómalas. Pero había decidido algo: esa noche iba a bucear hasta el generador para desactivarlo.

—Si vas solo, estás loco —dijo Rafa.

—Si no voy, el proyecto LOCUENTO sigue adelante y privatizan Ancón.

—¿Y si te atrapan?

—Entonces necesito un plan B.

Mateo abrió su laptop. Necesitaba evaluar escenarios. Y en Python, los escenarios se evalúan con **condicionales**.

## If/Elif/Else: La decisión del surfista

Los condicionales permiten que el código tome decisiones. Como un surfista decidiendo si tomar una ola o esperar la siguiente:

```python
# ============================================
# EVALUANDO ESCENARIOS
# ============================================

altura_ola = 2.4
experiencia_surfista = 7  # años

print("=== DECISIÓN: ¿TOMAMOS LA OLA? ===\n")

if altura_ola < 1.0:
    print("Ola muy pequeña. No vale la pena.")
elif altura_ola <= 2.0:
    print("Ola moderada. Buena para practicar.")
elif altura_ola <= 3.5:
    if experiencia_surfista >= 5:
        print("Ola perfecta para surfista experimentado. ¡A remar!")
    else:
        print("Ola grande para principiante. Mejor esperar.")
else:
    print("Ola peligrosa. No entrar al mar.")
```

### Operadores de comparación

| Operador | Significado |
|----------|-------------|
| `==` | Igual a |
| `!=` | Diferente de |
| `<` | Menor que |
| `>` | Mayor que |
| `<=` | Menor o igual |
| `>=` | Mayor o igual |

```python
# --- EVALUANDO IMPLICADOS ---

# Diccionario de implicados (del capítulo anterior)
implicados = {
    "Carlos Parra": {"edad": 45, "rol": "Ingeniero Naval", "involucrado": True, "nivel_sospecha": 8, "empresa": "OceanTech Perú", "evidencias": ["Diseñó el generador", "Recibió transferencia de Soto"]},
    "Luisa Rivas": {"edad": 38, "rol": "Bióloga Marina", "involucrado": False, "nivel_sospecha": 3, "empresa": "IMARPE", "evidencias": ["Denunció ruido submarino", "Pidió investigación"]},
    "Miguel Ángel Soto": {"edad": 62, "rol": "Empresario", "involucrado": True, "nivel_sospecha": 9, "empresa": "Grupo Inmobiliario Costa Azul", "evidencias": ["Dueño del proyecto LOCUENTO", "Quiere construir en Ancón"]},
    "Capitán Paredes": {"edad": 55, "rol": "Capitanía del Puerto", "involucrado": False, "nivel_sospecha": 5, "empresa": "Gobierno del Perú", "evidencias": ["Recibió quejas", "No investigó"]}
}

print("\n=== EVALUACIÓN DE IMPLICADOS ===\n")

for nombre, datos in implicados.items():
    print(f"▶ {nombre}")
    
    if datos["nivel_sospecha"] >= 8:
        print(f"  ALTO: Sospechoso principal")
    elif datos["nivel_sospecha"] >= 5:
        print(f"  MEDIO: Requiere vigilancia")
    else:
        print(f"  BAJO: Probablemente inocente")
```

### Operadores lógicos: and, or, not

Las decisiones reales usan múltiples condiciones:

```python
# --- ANÁLISIS MULTIFACTOR ---

for nombre, datos in implicados.items():
    print(f"\n▶ {nombre}")
    
    # and: ambas condiciones
    if datos["involucrado"] and datos["nivel_sospecha"] >= 7:
        print(f"  ⚠ IMPLICADO DIRECTO: Involucrado y muy sospechoso")
    
    # or: al menos una
    if datos["nivel_sospecha"] >= 8 or "Soto" in datos.get("empresa", ""):
        print(f"  ⚠ POSIBLE CABECILLA: Sospecha máxima o conexión con Soto")
    
    # not: negación
    if not datos["involucrado"]:
        print(f"  ✓ Aparentemente limpio")
```

## El plan de acción

Mateo escribió un sistema para decidir su plan según las condiciones del mar:

```python
# --- SISTEMA DE DECISIÓN PARA EL BUCEO ---

def evaluar_buceo(velocidad_viento, altura_ola, visibilidad, hay_luna):
    """Evalúa si es seguro bucear hasta el generador."""
    
    print("\n=== EVALUACIÓN DE BUCEO NOCTURNO ===")
    print(f"Viento: {velocidad_viento} nudos")
    print(f"Olas: {altura_ola}m")
    print(f"Visibilidad: {visibilidad}m")
    print(f"Luna: {'Sí' if hay_luna else 'No'}")
    
    riesgos = 0
    
    if velocidad_viento > 15:
        print("  ⚠ Viento fuerte")
        riesgos += 2
    if altura_ola > 1.5:
        print("  ⚠ Olas grandes")
        riesgos += 2
    if visibilidad < 3:
        print("  ⚠ Mala visibilidad")
        riesgos += 3
    if not hay_luna:
        print("  ⚠ Sin luna (muy oscuro)")
        riesgos += 1
    
    print(f"\n  Total de riesgos: {riesgos}/10")
    
    if riesgos >= 7:
        return "NO RECOMENDADO: Condiciones peligrosas"
    elif riesgos >= 4:
        return "PRECAUCIÓN: Posible pero con equipo adecuado"
    else:
        return "FAVORABLE: Condiciones seguras"

# Evaluar con condiciones actuales
resultado = evaluar_buceo(12, 1.2, 4, True)
print(f"\n  → Resultado: {resultado}")
```

## El interrogatorio digital

Mateo decidió que necesitaba hablar con Carlos Parra, el ingeniero naval. Pero antes quería preparar las preguntas basadas en los datos:

```python
# --- PREPARANDO EL INTERROGATORIO ---

def analizar_respuesta(respuesta, evidencia_conocida):
    """Analiza si la respuesta coincide con la evidencia."""
    
    if respuesta == evidencia_conocida:
        return "VERDAD: Coincide con la evidencia"
    elif respuesta.lower() == "no sé" or respuesta.lower() == "no recuerdo":
        return "EVASIVO: Podría estar ocultando algo"
    elif respuesta != evidencia_conocida:
        return f"MENTIRA: Dice '{respuesta}' pero la evidencia muestra '{evidencia_conocida}'"
    else:
        return "INDETERMINADO"

# Simular respuestas de Carlos Parra
preguntas = [
    ("¿Diseñaste el generador submarino?", "Sí, pero era para investigación"),
    ("¿Sabes quién lo opera?", "No sé"),
    ("¿Recibiste dinero de Miguel Ángel Soto?", "No, fue una inversión legítima"),
]

evidencias = [
    "Sí, diseñó el generador",
    "Los registros muestran que sí sabe",
    "Transferencia bancaria comprobada"
]

print("\n=== ANÁLISIS DE RESPUESTAS ===")
for (pregunta, respuesta), evidencia in zip(preguntas, evidencias):
    print(f"\nP: {pregunta}")
    print(f"R: '{respuesta}'")
    print(f"E: {evidencia}")
    print(f"→ {analizar_respuesta(respuesta, evidencia)}")
```

## Enigmas

### Enigma 5.1: Evaluador de olas

Pide al usuario la altura de una ola (con `input()`). Evalúa:
- Si es < 1m: "Ola pequeña"
- Si es entre 1 y 2.5m: "Ola ideal para surf"
- Si es > 2.5m: "Ola peligrosa"

### Enigma 5.2: Filtro de sospechosos

Del diccionario `implicados`, muestra solo los que:
- Tengan nivel_sospecha >= 7
- Estén involucrados Y tengan evidencias
- No estén involucrados PERO tengan nivel_sospecha > 4

### Enigma 5.3: El semáforo del mar

Escribe un programa que, dada la temperatura del agua, muestre:
- < 16°C: "Agua muy fría, usa traje de neopreno"
- 16-20°C: "Agua templada, buenas condiciones"
- > 20°C: "Agua cálida, ideal para todo el día"

---

## Lo que aprendiste

- `if`, `elif`, `else` ejecutan código según condiciones
- **Operadores de comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Operadores lógicos**: `and`, `or`, `not`
- Los condicionales pueden anidarse
- Las condiciones múltiples permiten análisis complejos

Mateo tenía su plan. Las condiciones del mar eran favorables. Iría esa noche.

Pero cuando se disponía a guardar su laptop, recibió un mensaje de texto de un número desconocido:

```
"Sabemos que estás investigando. 
No vayas al generador esta noche.
No es seguro.
— Alguien que quiere ayudarte."
```

Mateo miró el mensaje. ¿Era una advertencia real o una trampa?

—Si voy, puedo descubrir la verdad —dijo—. Si no voy, quizás pierdo la única oportunidad.

A veces, la decisión correcta no es la más obvia. A veces, hay que recorrer un **camino**, paso a paso, como un **bucle**.

---
