"""Capitulo 5: La Decision de la Ola
Conceptos: Condicionales if/elif/else, operadores logicos
"""

# ============================================
# EVALUANDO ESCENARIOS
# ============================================

altura_ola = 2.4
experiencia_surfista = 7  # anos

print("=== DECISION: TOMAMOS LA OLA? ===\n")

if altura_ola < 1.0:
    print("Ola muy pequena. No vale la pena.")
elif altura_ola <= 2.0:
    print("Ola moderada. Buena para practicar.")
elif altura_ola <= 3.5:
    if experiencia_surfista >= 5:
        print("Ola perfecta para surfista experimentado. A remar!")
    else:
        print("Ola grande para principiante. Mejor esperar.")
else:
    print("Ola peligrosa. No entrar al mar.")

# --- EVALUANDO IMPLICADOS ---

# Diccionario de implicados (del capitulo anterior)
implicados = {
    "Carlos Parra": {"edad": 45, "rol": "Ingeniero Naval", "involucrado": True, "nivel_sospecha": 8, "empresa": "OceanTech Peru", "evidencias": ["Diseno el generador", "Recibio transferencia de Soto"]},
    "Luisa Rivas": {"edad": 38, "rol": "Biologa Marina", "involucrado": False, "nivel_sospecha": 3, "empresa": "IMARPE", "evidencias": ["Denuncio ruido submarino", "Pidio investigacion"]},
    "Miguel Angel Soto": {"edad": 62, "rol": "Empresario", "involucrado": True, "nivel_sospecha": 9, "empresa": "Grupo Inmobiliario Costa Azul", "evidencias": ["Dueno del proyecto LOCUENTO", "Quiere construir en Ancon"]},
    "Capitan Paredes": {"edad": 55, "rol": "Capitan del Puerto", "involucrado": False, "nivel_sospecha": 5, "empresa": "Gobierno del Peru", "evidencias": ["Recibio quejas", "No investigo"]}
}

print("\n=== EVALUACION DE IMPLICADOS ===\n")

for nombre, datos in implicados.items():
    print(f"> {nombre}")

    if datos["nivel_sospecha"] >= 8:
        print(f"  ALTO: Sospechoso principal")
    elif datos["nivel_sospecha"] >= 5:
        print(f"  MEDIO: Requiere vigilancia")
    else:
        print(f"  BAJO: Probablemente inocente")

# --- ANALISIS MULTIFACTOR ---

for nombre, datos in implicados.items():
    print(f"\n> {nombre}")

    # and: ambas condiciones
    if datos["involucrado"] and datos["nivel_sospecha"] >= 7:
        print(f"  ! IMPLICADO DIRECTO: Involucrado y muy sospechoso")

    # or: al menos una
    if datos["nivel_sospecha"] >= 8 or "Soto" in datos.get("empresa", ""):
        print(f"  ! POSIBLE CABECILLA: Sospecha maxima o conexion con Soto")

    # not: negacion
    if not datos["involucrado"]:
        print(f"  OK Aparentemente limpio")

# --- SISTEMA DE DECISION PARA EL BUCEO ---

def evaluar_buceo(velocidad_viento, altura_ola, visibilidad, hay_luna):
    """Evalua si es seguro bucear hasta el generador."""

    print("\n=== EVALUACION DE BUCEO NOCTURNO ===")
    print(f"Viento: {velocidad_viento} nudos")
    print(f"Olas: {altura_ola}m")
    print(f"Visibilidad: {visibilidad}m")
    print(f"Luna: {'Si' if hay_luna else 'No'}")

    riesgos = 0

    if velocidad_viento > 15:
        print("  ! Viento fuerte")
        riesgos += 2
    if altura_ola > 1.5:
        print("  ! Olas grandes")
        riesgos += 2
    if visibilidad < 3:
        print("  ! Mala visibilidad")
        riesgos += 3
    if not hay_luna:
        print("  ! Sin luna (muy oscuro)")
        riesgos += 1

    print(f"\n  Total de riesgos: {riesgos}/10")

    if riesgos >= 7:
        return "NO RECOMENDADO: Condiciones peligrosas"
    elif riesgos >= 4:
        return "PRECAUCION: Posible pero con equipo adecuado"
    else:
        return "FAVORABLE: Condiciones seguras"

# Evaluar con condiciones actuales
resultado = evaluar_buceo(12, 1.2, 4, True)
print(f"\n  -> Resultado: {resultado}")

# --- PREPARANDO EL INTERROGATORIO ---

def analizar_respuesta(respuesta, evidencia_conocida):
    """Analiza si la respuesta coincide con la evidencia."""

    if respuesta == evidencia_conocida:
        return "VERDAD: Coincide con la evidencia"
    elif respuesta.lower() == "no se" or respuesta.lower() == "no recuerdo":
        return "EVASIVO: Podria estar ocultando algo"
    elif respuesta != evidencia_conocida:
        return f"MENTIRA: Dice '{respuesta}' pero la evidencia muestra '{evidencia_conocida}'"
    else:
        return "INDETERMINADO"

# Simular respuestas de Carlos Parra
preguntas = [
    ("Disenaste el generador submarino?", "Si, pero era para investigacion"),
    ("Sabes quien lo opera?", "No se"),
    ("Recibiste dinero de Miguel Angel Soto?", "No, fue una inversion legitima"),
]

evidencias = [
    "Si, diseno el generador",
    "Los registros muestran que si sabe",
    "Transferencia bancaria comprobada"
]

print("\n=== ANALISIS DE RESPUESTAS ===")
for (pregunta, respuesta), evidencia in zip(preguntas, evidencias):
    print(f"\nP: {pregunta}")
    print(f"R: '{respuesta}'")
    print(f"E: {evidencia}")
    print(f"-> {analizar_respuesta(respuesta, evidencia)}")

# --- ENIGMAS ---

print("\n=== ENIGMA 5.1: Evaluador de olas ===")
altura_prueba = 2.0  # valor harcodeado en lugar de input()
if altura_prueba < 1.0:
    print("Ola pequena")
elif 1.0 <= altura_prueba <= 2.5:
    print("Ola ideal para surf")
else:
    print("Ola peligrosa")

print("\n=== ENIGMA 5.2: Filtro de sospechosos ===")
print("Nivel de sospecha >= 7:")
for nombre, datos in implicados.items():
    if datos["nivel_sospecha"] >= 7:
        print(f"  * {nombre}")
print("Involucrados Y con evidencias:")
for nombre, datos in implicados.items():
    if datos["involucrado"] and datos["evidencias"]:
        print(f"  * {nombre}")
print("No involucrados PERO nivel_sospecha > 4:")
for nombre, datos in implicados.items():
    if not datos["involucrado"] and datos["nivel_sospecha"] > 4:
        print(f"  * {nombre}")

print("\n=== ENIGMA 5.3: Semaforo del mar ===")
temperatura = 18.0
if temperatura < 16:
    print("Agua muy fria, usa traje de neopreno")
elif temperatura <= 20:
    print("Agua templada, buenas condiciones")
else:
    print("Agua calida, ideal para todo el dia")
