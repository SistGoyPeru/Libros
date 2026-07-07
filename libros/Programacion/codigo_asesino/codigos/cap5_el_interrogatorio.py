"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 5 - El Interrogatorio
Conceptos: Condicionales if/elif/else, operadores de comparación, operadores lógicos
Autor: Alex Goyzueta Delgado
"""

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

print("=== ANÁLISIS DE DECLARACIÓN ===")
if declaracion_lara["acceso_a_yachay"]:
    print("Lara tenía acceso a Yachay.")
else:
    print("Lara NO tenía acceso a Yachay.")

if declaracion_lara["sabe_de_amenazas"]:
    print("Lara conocía amenazas contra Inti.")
else:
    print("Lara dice no conocer amenazas.")

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

# --- CRUZANDO MÚLTIPLES FACTORES ---
sospechosos = [
    {"nombre": "Lara Mamani", "acceso": True, "coartada": False, "motivo": 7, "huellas": True},
    {"nombre": "Carlos Huamán", "acceso": True, "coartada": True, "motivo": 8, "huellas": False},
    {"nombre": "Sarah Chen", "acceso": True, "coartada": True, "motivo": 6, "huellas": False},
    {"nombre": "Rodrigo Mamani", "acceso": False, "coartada": True, "motivo": 9, "huellas": False},
    {"nombre": "Mama Killa", "acceso": True, "coartada": True, "motivo": 5, "huellas": True}
]

print("\n=== ANÁLISIS DE SOSPECHOSOS ===")
for s in sospechosos:
    if s["acceso"] and not s["coartada"]:
        print(f"{s['nombre']}: ALTA PRIORIDAD - Acceso y sin coartada")
    elif s["motivo"] > 7 or s["huellas"]:
        print(f"{s['nombre']}: MEDIA PRIORIDAD - Motivo fuerte o huellas presentes")
    else:
        print(f"{s['nombre']}: BAJA PRIORIDAD - Poco sospechoso")

# --- SISTEMA DE ANÁLISIS DE DECLARACIONES ---
def analizar_declaracion(declaracion):
    puntaje = 0
    razones = []

    if declaracion["acceso"]:
        puntaje += 3
        razones.append("Tenía acceso al laboratorio")

    if not declaracion["coartada"]:
        puntaje += 4
        razones.append("NO tiene coartada")

    if declaracion["motivo"] >= 8:
        puntaje += 3
        razones.append("Motivo muy fuerte")
    elif declaracion["motivo"] >= 5:
        puntaje += 1
        razones.append("Motivo moderado")

    if declaracion["huellas"]:
        puntaje += 1
        razones.append("Huellas en la escena")

    if puntaje >= 7:
        nivel = "CRÍTICO"
    elif puntaje >= 4:
        nivel = "ALTO"
    elif puntaje >= 2:
        nivel = "MODERADO"
    else:
        nivel = "BAJO"

    return puntaje, nivel, razones

print("\n=== RESULTADOS DEL ANÁLISIS ===")
for s in sospechosos:
    puntaje, nivel, razones = analizar_declaracion(s)
    print(f"\n{s['nombre']}:")
    print(f"  Puntaje: {puntaje}/10 | Nivel: {nivel}")
    print(f"  Razones: {', '.join(razones)}")

# --- BUSCANDO LO NO OBVIO ---
print("\n=== ANÁLISIS DE BENEFICIARIO ===")
for s in sospechosos:
    if not s["acceso"] and s["motivo"] >= 8:
        print(f"{s['nombre']}: PODRÍA HABER MANIPULADO a alguien")
    if s["acceso"] and not s["coartada"] and s["motivo"] >= 5:
        print(f"{s['nombre']}: SOSPECHOSO DIRECTO")
    if s["huellas"] and s["coartada"]:
        print(f"{s['nombre']}: CONTRADICCIÓN - Huellas pero dice no estar")
