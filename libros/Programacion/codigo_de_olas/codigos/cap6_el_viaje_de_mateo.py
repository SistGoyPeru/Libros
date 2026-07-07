"""Capitulo 6: El Viaje de Mateo
Conceptos: Bucles for/while, range(), enumerate(), break/continue
"""

import time

# ============================================
# RUTA HACIA EL GENERADOR
# ============================================

# Puntos de referencia en el mar (boyas)
puntos_ruta = [
    "Muelle de Ancon",
    "Boya Roja #1",
    "Roca del Norte",
    "Boya Verde #2",
    "Banco de Arena",
    "Generador Submarino"
]

print("=== RUTA HACIA EL GENERADOR ===\n")
print("Recorriendo puntos de navegacion:\n")

for punto in puntos_ruta:
    print(f"  -> Avanzando hacia: {punto}")
    if punto == "Generador Submarino":
        print(f"  * !Destino alcanzado!")

# range(): Distancias numericas
print("\n=== CONTANDO METROS NADADOS ===\n")

for metro in range(1, 11):
    print(f"  Metro {metro}: braceo...")

print("  !Descanso! Llegue a los 10 metros.")

# enumerate(): Posicion y valor
print("\n=== BOYAS CON SUS COORDENADAS ===\n")

boyas = [
    "Boya Roja (inicio)",
    "Boya Azul (norte)",
    "Boya Verde (este)",
    "Boya Amarilla (generador)"
]

for indice, boya in enumerate(boyas):
    print(f"  Boya [{indice}]: {boya}")

# While: Hasta encontrar el generador
print("\n=== NADANDO HACIA EL GENERADOR ===\n")

distancia = 500  # metros
metros_nadados = 0

while metros_nadados < distancia:
    metros_nadados += 25  # brazadas de 25 metros
    progreso = (metros_nadados / distancia) * 100
    print(f"  Progreso: {metros_nadados}/{distancia}m ({progreso:.0f}%)")
    time.sleep(0.2)

print(f"\n  * !Generador alcanzado despues de nadar {metros_nadados} metros!")

# break: Evadiendo la patrulla
print("\n=== EVADIENDO A LA PATRULLA ===\n")

ruta_segura = ["bajo el muelle", "detras de la roca", "zona de boyas", "junto al generador"]
patrulla_cerca = False

for zona in ruta_segura:
    if patrulla_cerca:
        print(f"  ! Patrulla detectada en {zona}. !BREAK! Ocultandose...")
        break

    print(f"  -> Avanzando por {zona}...")

    # Simular deteccion de patrulla en la tercera zona
    if zona == "zona de boyas":
        print(f"  ! !Luces de patrulla a lo lejos!")
        patrulla_cerca = True
        print(f"  -> Rompiendo ruta. Parando en {zona}.")
        break

print(f"\n  -> Busqueda {'interrumpida por patrulla' if patrulla_cerca else 'completada'}.")

# continue: Ignorando obstaculos menores
print("\n=== SORTEANDO OBSTACULOS MENORES ===\n")

obstaculos = ["alga", "medusa", "roca", "red", "plastico", "generador"]

for obstaculo in obstaculos:
    if obstaculo in ["alga", "medusa", "plastico"]:
        print(f"  -> {obstaculo} detectado. Esquivando (continue)...")
        continue

    print(f"  -> {obstaculo}: Bajando a revisar...")

    if obstaculo == "generador":
        print(f"  * !GENERADOR ENCONTRADO!")
        break

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

# Analisis: buscar patrones en las activaciones
print("\n=== ANALISIS DE PATRONES ===\n")

for i, act in enumerate(activaciones):
    if i > 0:
        anterior = activaciones[i-1]
        if act["duracion"] != anterior["duracion"]:
            print(f"  ! Cambio de duracion: {anterior['duracion']} -> {act['duracion']} min a las {act['hora']}")

# Cuanto tiempo total de activacion?
total_minutos = sum(act["duracion"] for act in activaciones)
print(f"\n  Tiempo total activado: {total_minutos} minutos")
print(f"  Equivalente a: {total_minutos // 60}h {total_minutos % 60}m")

# --- ENIGMAS ---

print("\n=== ENIGMA 6.1: Recorrido de playas ===")
playas = ["Ancon", "Miraflores", "Barranco", "Costa Verde"]
for i, playa in enumerate(playas):
    print(f"  {i+1}. {playa}")

print("\n=== ENIGMA 6.2: Busqueda del generador ===")
dist = 0
while dist < 100:
    dist += 10
    print(f"  Avanzando... {dist}m")
print("  !GENERADOR ENCONTRADO!")

print("\n=== ENIGMA 6.3: Filtro de datos erroneos ===")
temperaturas = [18.2, 19.0, -5, 18.5, 500, 19.1]
print("Temperaturas validas:")
for t in temperaturas:
    if t < 0 or t > 50:
        continue
    print(f"  {t}C")

print("\n=== ENIGMA 6.4: Piramide de olas ===")
for i in range(1, 5):
    print("*" * i)
