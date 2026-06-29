# Capítulo 6: El Viaje de Mateo

## Conceptos: Bucles `for`/`while`, `range()`, `enumerate()`, `break`/`continue`

---

Eran las 11:00 p.m. cuando Mateo llegó al muelle de Ancón. La luna estaba alta. El mar estaba tranquilo. Pero en el horizonte, unas luces parpadeaban.

—Es el generador —dijo Rafa, que lo acompañaba—. Está a 500 metros mar adentro. 

—Necesito llegar hasta él. Pero no en línea recta. Hay boyas de monitoreo. Si paso cerca de ellas, activo una alarma.

—¿Cómo piensas llegar entonces?

Mateo señaló un patrón en el agua.

—Las olas van en una dirección. El generador está en otra. Pero hay un camino. Como un bucle en Python: paso a paso, evitando los obstáculos.

## For: Navegando entre olas

El bucle `for` recorre una secuencia de elementos. Como navegar de boya en boya:

```python
# ============================================
# RUTA HACIA EL GENERADOR
# ============================================

# Puntos de referencia en el mar (boyas)
puntos_ruta = [
    "Muelle de Ancón",
    "Boya Roja #1",
    "Roca del Norte",
    "Boya Verde #2",
    "Banco de Arena",
    "Generador Submarino"
]

print("=== RUTA HACIA EL GENERADOR ===\n")
print("Recorriendo puntos de navegación:\n")

for punto in puntos_ruta:
    print(f"  → Avanzando hacia: {punto}")
    if punto == "Generador Submarino":
        print(f"  ★ ¡Destino alcanzado!")
```

### range(): Distancias numéricas

A veces necesitas contar. Como los metros que nada Mateo:

```python
print("\n=== CONTANDO METROS NADADOS ===\n")

for metro in range(1, 11):
    print(f"  Metro {metro}: braceo...")
    
print("  ¡Descanso! Llegué a los 10 metros.")
```

### enumerate(): Posición y valor

`enumerate()` da el índice y el valor al mismo tiempo:

```python
print("\n=== BOYAS CON SUS COORDENADAS ===\n")

boyas = [
    "Boya Roja (inicio)",
    "Boya Azul (norte)",
    "Boya Verde (este)",
    "Boya Amarilla (generador)"
]

for indice, boya in enumerate(boyas):
    print(f"  Boya [{indice}]: {boya}")
```

## While: Hasta encontrar el generador

El bucle `while` se ejecuta mientras una condición sea verdadera. Como Mateo nadando hasta alcanzar el generador:

```python
print("\n=== NADANDO HACIA EL GENERADOR ===\n")

distancia = 500  # metros
metros_nadados = 0

while metros_nadados < distancia:
    metros_nadados += 25  # brazadas de 25 metros
    progreso = (metros_nadados / distancia) * 100
    print(f"  Progreso: {metros_nadados}/{distancia}m ({progreso:.0f}%)")
    time.sleep(0.2)

print(f"\n  ★ ¡Generador alcanzado después de nadar {metros_nadados} metros!")
```

### break: Evadiendo la patrulla

De repente, Mateo vio luces. Una patrulla de la Capitanía se acercaba. Necesitaba salir del bucle:

```python
print("\n=== EVADIENDO A LA PATRULLA ===\n")

ruta_segura = ["bajo el muelle", "detrás de la roca", "zona de boyas", "junto al generador"]
patrulla_cerca = False

for zona in ruta_segura:
    if patrulla_cerca:
        print(f"  ⚠ Patrulla detectada en {zona}. ¡BREAK! Ocultándose...")
        break
    
    print(f"  → Avanzando por {zona}...")
    
    # Simular detección de patrulla en la tercera zona
    if zona == "zona de boyas":
        print(f"  ⚠ ¡Luces de patrulla a lo lejos!")
        patrulla_cerca = True
        print(f"  → Rompiendo ruta. Parando en {zona}.")
        break

print(f"\n  → Búsqueda {'interrumpida por patrulla' if patrulla_cerca else 'completada'}.")
```

### continue: Ignorando obstáculos menores

Algunos obstáculos no requieren detenerse, solo evitarlos:

```python
print("\n=== SORTEANDO OBSTÁCULOS MENORES ===\n")

obstaculos = ["alga", "medusa", "roca", "red", "plástico", "generador"]

for obstaculo in obstaculos:
    if obstaculo in ["alga", "medusa", "plástico"]:
        print(f"  → {obstaculo} detectado. Esquivando (continue)...")
        continue
    
    print(f"  → {obstaculo}: Bajando a revisar...")
    
    if obstaculo == "generador":
        print(f"  ★ ¡GENERADOR ENCONTRADO!")
        break
```

## El registro de activaciones

Mateo llegó al generador y encontró una pequeña computadora sellada en una caja estanca. Descargó el registro de activaciones para analizarlo después:

```python
# --- REGISTRO DE ACTIVACIONES DEL GENERADOR ---

print("\n=== REGISTRO DE ACTIVACIONES ===\n")

activaciones = [
    {"fecha": "01-06", "hora": "06:00", "duracion": 15},
    {"fecha": "01-06", "hora": "09:00", "duracion": 15},
    {"fecha": "01-06", "hora": "12:00", "duracion": 15},
    {"fecha": "01-06", "hora": "15:00", "duracion": 15},
    {"fecha": "01-06", "hora": "18:00", "duracion": 15},
    {"fecha": "01-06", "hora": "21:00", "duracion": 15},
    {"fecha": "01-06", "hora": "00:00", "duracion": 30},
    {"fecha": "02-06", "hora": "03:00", "duracion": 30},
]

print("Activaciones registradas:")
for act in activaciones:
    print(f"  {act['fecha']} | {act['hora']} | {act['duracion']} min")

# Análisis: buscar patrones en las activaciones
print("\n=== ANÁLISIS DE PATRONES ===\n")

for i, act in enumerate(activaciones):
    if i > 0:
        anterior = activaciones[i-1]
        if act["duracion"] != anterior["duracion"]:
            print(f"  ⚠ Cambio de duración: {anterior['duracion']} → {act['duracion']} min a las {act['hora']}")

# ¿Cuánto tiempo total de activación?
total_minutos = sum(act["duracion"] for act in activaciones)
print(f"\n  Tiempo total activado: {total_minutos} minutos")
print(f"  Equivalente a: {total_minutos // 60}h {total_minutos % 60}m")
```

El patrón era claro: activaciones cada 3 horas, con duraciones que variaban. Como un programa con diferentes configuraciones.

## Enigmas

### Enigma 6.1: Recorrido de playas

Dada la lista `playas = ["Ancón", "Miraflores", "Barranco", "Costa Verde"]`, usa `for` para mostrar cada playa con su número (usando `enumerate`).

### Enigma 6.2: Búsqueda del generador

Usando `while`, simula una búsqueda del generador. Parte de 0 metros, avanza de 10 en 10, y cuando llegues a 100 metros, muestra "GENERADOR ENCONTRADO".

### Enigma 6.3: Filtro de datos erróneos

Dada la lista de temperaturas del mar: `[18.2, 19.0, -5, 18.5, 500, 19.1]`, usa `continue` para saltar los valores imposibles (negativos o > 50). Muestra solo los válidos.

### Enigma 6.4: Pirámide de olas

Usando `range()` y bucles anidados, crea:

```
*
**
***
****
```

---

## Lo que aprendiste

- `for elemento in coleccion:` recorre una secuencia
- `range(n)` genera números de 0 a n-1
- `enumerate()` da índice y valor
- `while condicion:` itera mientras se cumpla la condición
- `break` sale del bucle
- `continue` salta a la siguiente iteración

Mateo tenía el registro de activaciones. Ahora sabía que el generador no solo creaba olas anómalas: también transmitía datos. Cada activación era una función del programa principal.

—El generador no es solo una máquina —dijo—. Es un programa ejecutándose en el mar. Y cada función del programa hace algo diferente. Necesito entender esas **funciones**.

---
