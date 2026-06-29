# Capítulo 5: El Interrogatorio

## Conceptos: Condicionales `if/elif/else`, operadores de comparación, operadores lógicos

---

El sol se había alzado sobre Neo-Cusco cuando Wayra llegó a la comisaría. Raúl había conseguido acceso a las declaraciones oficiales de los sospechosos. Estaban sentados en una sala fría, con paredes de concreto y un espejo unidireccional.

—Van a interrogar a Lara primero —susurró Raúl—. Pero las declaraciones ya están aquí. Podemos analizarlas antes.

Wayra tomó los papeles. Había inconsistencias. Todas las declaraciones coincidían en los hechos generales, pero los detalles... los detalles no cuadraban.

—Necesito comparar estas declaraciones —dijo Wayra—. Encontrar las contradicciones. Y para eso necesito condicionales.

## If, elif, else: Las decisiones del quipucamayoc

Los **condicionales** son la forma en que Python toma decisiones. Al igual que un quipucamayoc decidía qué nudo usar según el tipo de información, Python decide qué código ejecutar según las condiciones que le das.

```python
# ============================================
# ANALIZANDO DECLARACIONES
# ============================================

# Declaración de Lara Mamani
declaracion_lara = {
    "nombre": "Lara Mamani",
    "hora_llegada": "08:00",
    "hora_salida": "18:00",
    "ultima_vez_vio_inti": "18:00",
    "relacion_con_inti": "Excelente, era como un padre",
    "sabe_de_amenazas": False,
    "acceso_a_yachay": True
}

# Análisis básico
print("=== ANÁLISIS DE DECLARACIÓN ===")

if declaracion_lara["acceso_a_yachay"]:
    print("Lara tenía acceso a Yachay.")
else:
    print("Lara NO tenía acceso a Yachay.")

if declaracion_lara["sabe_de_amenazas"]:
    print("Lara conocía amenazas contra Inti.")
else:
    print("Lara dice no conocer amenazas.")
```

—Pero esto es muy básico —dijo Wayra—. Necesito cruzar datos. Comparar declaraciones. Encontrar contradicciones.

### Operadores de comparación

Python tiene operadores para comparar valores:

| Operador | Significado |
|----------|-------------|
| `==` | Igual que |
| `!=` | Diferente de |
| `<` | Menor que |
| `>` | Mayor que |
| `<=` | Menor o igual que |
| `>=` | Mayor o igual que |

```python
# --- COMPARANDO DATOS ---

hora_muerte = "02:34"
hora_salida_lara = declaracion_lara["hora_salida"]

print(f"\nHora de la muerte: {hora_muerte}")
print(f"Lara dice que salió a las: {hora_salida_lara}")

if hora_salida_lara < hora_muerte:
    print("Lara se fue ANTES del crimen. Coartada posible.")
elif hora_salida_lara == hora_muerte:
    print("Lara salió EXACTAMENTE a la hora del crimen. Sospechoso.")
else:
    print("Lara se fue DESPUÉS del crimen. ¡Coartada falsa!")
```

### Múltiples condiciones: and, or, not

Las decisiones reales rara vez dependen de una sola condición. Python permite combinar condiciones con operadores lógicos:

```python
# --- CRUZANDO MÚLTIPLES FACTORES ---

# Datos de los sospechosos
sospechosos = [
    {"nombre": "Lara Mamani", "acceso": True, "coartada": False, "motivo": 7, "huellas": True},
    {"nombre": "Carlos Huamán", "acceso": True, "coartada": True, "motivo": 8, "huellas": False},
    {"nombre": "Sarah Chen", "acceso": True, "coartada": True, "motivo": 6, "huellas": False},
    {"nombre": "Rodrigo Mamani", "acceso": False, "coartada": True, "motivo": 9, "huellas": False},
    {"nombre": "Mama Killa", "acceso": True, "coartada": True, "motivo": 5, "huellas": True}
]

print("\n=== ANÁLISIS DE SOSPECHOSOS ===")

for s in sospechosos:
    # and: ambas condiciones deben ser True
    if s["acceso"] and not s["coartada"]:
        print(f"{s['nombre']}: ALTA PRIORIDAD - Acceso y sin coartada")
    
    # or: al menos una condición debe ser True
    elif s["motivo"] > 7 or s["huellas"]:
        print(f"{s['nombre']}: MEDIA PRIORIDAD - Motivo fuerte o huellas presentes")
    
    else:
        print(f"{s['nombre']": BAJA PRIORIDAD - Poco sospechoso")
```

### El interrogatorio completo

Wayra decidió construir un sistema de análisis más complejo:

```python
# ============================================
# SISTEMA DE ANÁLISIS DE DECLARACIONES
# ============================================

def analizar_declaracion(declaracion):
    """Analiza una declaración y devuelve un nivel de sospecha."""
    
    puntaje = 0
    razones = []
    
    # 1. ¿Tenía acceso?
    if declaracion["acceso"]:
        puntaje += 3
        razones.append("Tenía acceso al laboratorio")
    
    # 2. ¿Tiene coartada verificable?
    if not declaracion["coartada"]:
        puntaje += 4
        razones.append("NO tiene coartada")
    
    # 3. ¿Nivel de motivo?
    if declaracion["motivo"] >= 8:
        puntaje += 3
        razones.append("Motivo muy fuerte")
    elif declaracion["motivo"] >= 5:
        puntaje += 1
        razones.append("Motivo moderado")
    
    # 4. ¿Sus huellas están en la escena?
    if declaracion["huellas"]:
        puntaje += 1
        razones.append("Huellas en la escena")
    
    # 5. Evaluación final
    if puntaje >= 7:
        nivel = "CRÍTICO"
    elif puntaje >= 4:
        nivel = "ALTO"
    elif puntaje >= 2:
        nivel = "MODERADO"
    else:
        nivel = "BAJO"
    
    return puntaje, nivel, razones

# Analizar a cada sospechoso
print("\n=== RESULTADOS DEL ANÁLISIS ===\n")

for s in sospechosos:
    puntaje, nivel, razones = analizar_declaracion(s)
    print(f"{s['nombre']}:")
    print(f"  Puntaje: {puntaje}/10 | Nivel: {nivel}")
    print(f"  Razones: {', '.join(razones)}")
    print()
```

Los resultados fueron reveladores:

```
=== RESULTADOS DEL ANÁLISIS ===

Lara Mamani:
  Puntaje: 8/10 | Nivel: CRÍTICO
  Razones: Tenía acceso al laboratorio, NO tiene coartada, Huellas en la escena

Carlos Huamán:
  Puntaje: 5/10 | Nivel: ALTO
  Razones: Tenía acceso al laboratorio, Motivo muy fuerte

Sarah Chen:
  Puntaje: 4/10 | Nivel: ALTO
  Razones: Tenía acceso al laboratorio, Motivo moderado

Rodrigo Mamani:
  Puntaje: 3/10 | Nivel: MODERADO
  Razones: Motivo muy fuerte

Mama Killa:
  Puntaje: 5/10 | Nivel: ALTO
  Razones: Tenía acceso al laboratorio, Motivo moderado, Huellas en la escena
```

—Lara es la principal sospechosa —dijo Raúl—. Acceso, sin coartada, huellas en la escena...

—Sí —respondió Wayra, pero su tono no era de convencimiento—. Demasiado obvio. Es como si alguien hubiera querido que Lara pareciera culpable.

## El nudo condicional

Wayra recordó algo que su abuela le había enseñado sobre los quipus: "Cuando veas un nudo que parece obvio, busca el nudo invertido. El mensaje verdadero está en lo que no se ve a simple vista."

Aplicó esa lógica a los datos:

```python
# --- BUSCANDO LO NO OBVIO ---

# Si Lara es la culpable obvia, ¿quién se beneficia de eso?
print("=== ANÁLISIS DE BENEFICIARIO ===")

for s in sospechosos:
    # ¿Alguien que NO tiene acceso pero tiene motivo?
    if not s["acceso"] and s["motivo"] >= 8:
        print(f"{s['nombre']}: PODRÍA HABER MANIPULADO a Lara")
    
    # ¿Alguien que tiene acceso, coartada DÉBIL y motivo?
    if s["acceso"] and not s["coartada"] and s["motivo"] >= 5:
        print(f"{s['nombre']": SOSPECHOSO DIRECTO")
    
    # ¿Alguien con huellas PERO que dice no haber estado?
    if s["huellas"] and s["coartada"]:
        print(f"{s['nombre']}: CONTRADICCIÓN - Huellas pero dice no estar")

# Un caso especial: acceso sin motivo aparente
for s in sospechosos:
    if s["acceso"] and s["motivo"] < 5:
        print(f"{s['nombre']}: ¿POR QUÉ TENÍA ACCESO SI NO TENÍA MOTIVO?")
```

Wayra se detuvo en el último resultado.

—Mama Killa —murmuró—. Tenía acceso, motivo bajo, huellas en la escena, coartada. Es la hermana de Inti. ¿Por qué estaría involucrada?

—Quizás no lo está —dijo Raúl.

—O quizás su motivo no es económico —respondió Wayra—. Quizás su motivo es más antiguo. Más profundo. Algo que solo un hermano y una hermana comparten.

## Enigmas

### Enigma 5.1: Evaluador de coartadas

Escribe un programa que pida al usuario:
- Nombre del sospechoso
- Hora de la coartada (input)
- Hora del crimen (asumir 2:34)

Luego evalúe:
- Si la coartada es antes de las 2:00 → "Coartada sólida"
- Si es entre 2:00 y 2:34 → "Coartada débil"
- Si es después de 2:34 → "Coartada falsa"

### Enigma 5.2: El filtro de sospechosos

Dada la lista de sospechosos con sus datos, escribe un programa que:
1. Muestre solo los sospechosos con nivel de motivo >= 7
2. Muestre solo los que tienen acceso Y motivo >= 6
3. Muestre solo los que NO tienen coartada O tienen huellas

### Enigma 5.3: El juego de las contradicciones

Tres testigos dieron versiones diferentes:

- Testigo 1: "Vi a alguien salir del laboratorio a las 2:30"
- Testigo 2: "A las 2:30, el laboratorio estaba oscuro"
- Testigo 3: "Escuché una discusión a las 2:30"

Escribe condicionales que determinen si las versiones son compatibles entre sí. Si dos versiones se contradicen, muestra "CONTRADICCIÓN".

---

## Lo que aprendiste

- `if`, `elif`, `else` permiten ejecutar código condicionalmente
- **Operadores de comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Operadores lógicos**: `and`, `or`, `not`
- Los condicionales pueden anidarse y combinarse
- Los análisis complejos se construyen con múltiples condiciones
- La lógica condicional permite encontrar patrones y contradicciones

Wayra guardó el análisis. Los números señalaban a Lara, pero su instinto señalaba en otra dirección. Había demasiadas piezas perfectamente colocadas para apuntar a la asistente.

—Algo no cuadra —dijo, levantándose—. Necesito ver el laboratorio otra vez. Y necesito verlo sin la policía.

Raúl la miró, preocupado.

—Wayra, si te encuentran ahí...

—No me van a encontrar. Porque no voy a entrar por la puerta.

Salió de la comisaría con una determinación renovada. El quipus la había llevado hasta ahí, pero el siguiente paso requería algo más que condicionales. Requería un camino. Un recorrido. Un **bucle**.

---
