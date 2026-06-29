"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 4 - El Diccionario de Inti
Conceptos: Diccionarios, sets, operaciones con sets
Autor: Alex Goyzueta Delgado
"""

# ============================================
# DICCIONARIO DEL CASO
# ============================================

caso = {
    "nombre": "El Asesinato del Dr. Inti Quispe",
    "fecha": "27 de junio, 2026",
    "lugar": "Templo del Sol (Coricancha)",
    "hora": "02:34 (acceso), 06:30 (descubrimiento)",
    "estado": "abierto",
    "analista": "Wayra Condori"
}

print("=== DATOS DEL CASO ===")
print(f"Nombre: {caso['nombre']}")
print(f"Lugar: {caso['lugar']}")
print(f"Analista: {caso['analista']}")

# --- Diccionario de un sospechoso ---
lara = {
    "nombre": "Lara Mamani",
    "edad": 32,
    "rol": "Asistente de laboratorio",
    "acceso": True,
    "nivel_sospecha": 7,
    "coartada": "Estaba en su departamento",
    "conexion_con_inti": "Trabajó junto a él por 3 años",
    "motivo": "Económico - ¿chantaje?"
}

print("\n=== FICHA DE LARA MAMANI ===")
for clave, valor in lara.items():
    print(f"{clave}: {valor}")

# --- Diccionarios anidados: todos los sospechosos ---
sospechosos = {
    "Lara Mamani": {
        "edad": 32,
        "rol": "Asistente",
        "acceso": True,
        "sospecha": 7,
        "coartada": "Departamento propio",
        "evidencias": ["huella digital en teclado", "registro de acceso falso"]
    },
    "Dr. Carlos Huamán": {
        "edad": 55,
        "rol": "Colega universitario",
        "acceso": True,
        "sospecha": 8,
        "coartada": "Oficina universitaria",
        "evidencias": ["discusión con Inti días antes", "publicaciones bloqueadas"]
    },
    "Dra. Sarah Chen": {
        "edad": 40,
        "rol": "Colaboradora MIT",
        "acceso": True,
        "sospecha": 6,
        "coartada": "Videollamada con MIT",
        "evidencias": ["presión del MIT por resultados", "visa próxima a vencer"]
    },
    "Rodrigo Mamani": {
        "edad": 60,
        "rol": "Empresario tecnológico",
        "acceso": False,
        "sospecha": 9,
        "coartada": "Cena de negocios",
        "evidencias": ["interés en comprar Yachay", "conexiones políticas"]
    },
    "Mama Killa": {
        "edad": 70,
        "rol": "Hermana",
        "acceso": True,
        "sospecha": 5,
        "coartada": "Dormía en su casa",
        "evidencias": ["herencia", "secretos familiares"]
    }
}

print(f"\nRol de Sarah: {sospechosos['Dra. Sarah Chen']['rol']}")
print(f"Evidencias contra Carlos: {sospechosos['Dr. Carlos Huamán']['evidencias']}")

sospechosos["Lara Mamani"]["sospecha"] = 9
print(f"Nuevo nivel de sospecha de Lara: {sospechosos['Lara Mamani']['sospecha']}/10")

# --- MÉTODOS DE DICCIONARIOS ---
print("\n=== TODOS LOS SOSPECHOSOS ===")
print(list(sospechosos.keys()))

print("\n=== NIVEL DE SOSPECHA ===")
for nombre, info in sospechosos.items():
    print(f"{nombre}: {info['sospecha']}/10")

if "Lara Mamani" in sospechosos:
    print("\nLara Mamani está en la base de datos")

acceso = sospechosos.get("Lara Mamani", {}).get("acceso", "No especificado")
print(f"Acceso de Lara: {acceso}")

# --- SETS: ELEMENTOS ÚNICOS ---
roles = set()
for info in sospechosos.values():
    roles.add(info["rol"])
print(f"\nRoles únicos: {roles}")

evidencias_totales = set()
for info in sospechosos.values():
    for evidencia in info["evidencias"]:
        evidencias_totales.add(evidencia)
print(f"\nEvidencias únicas:")
for e in evidencias_totales:
    print(f"  • {e}")

# --- OPERACIONES CON SETS ---
tienen_acceso = {nombre for nombre, info in sospechosos.items() if info["acceso"]}
alta_sospecha = {nombre for nombre, info in sospechosos.items() if info["sospecha"] > 7}

print(f"\nSospechosos con acceso: {tienen_acceso}")
print(f"Sospechosos con alta sospecha: {alta_sospecha}")
print(f"Intersección (acceso Y alta sospecha): {tienen_acceso & alta_sospecha}")
print(f"Unión (acceso O alta sospecha): {tienen_acceso | alta_sospecha}")
print(f"Diferencia (acceso - alta): {tienen_acceso - alta_sospecha}")

# --- MODELANDO EL QUIPU FÍSICO COMO DICCIONARIO ---
quipu_inti = {
    "cuerda_roja": {
        "significado": "guerra/conflicto",
        "nudos": [1, 4, 9],
        "tipo_nudo": "simple",
    },
    "cuerda_verde": {
        "significado": "agricultura/conocimiento",
        "nudos": [2, 5, 10],
        "tipo_nudo": "compuesto",
    },
    "cuerda_azul": {
        "significado": "religión/espiritualidad",
        "nudos": [1, 5, 9],
        "tipo_nudo": "simple",
    },
    "cuerda_amarilla": {
        "significado": "riqueza/poder",
        "nudos": [3, 7, 11],
        "tipo_nudo": "compuesto largo",
    },
    "cuerda_blanca": {
        "significado": "conexión espiritual/verdad",
        "nudos": [1, 3, 5, 7, 9, 11],
        "tipo_nudo": "binario intercalado",
    }
}

print("\n=== ANÁLISIS DEL QUIPU DE INTI ===")
for cuerda, info in quipu_inti.items():
    print(f"\n{cuerda.replace('_', ' ').title()}:")
    print(f"  Significado: {info['significado']}")
    print(f"  Nudos en posiciones: {info['nudos']}")
    print(f"  Tipo: {info['tipo_nudo']}")

# --- ENIGMA 4.3: Sets en acción ---
print("\n--- Enigma 4.3 ---")
acceso_lab = {"Lara", "Carlos", "Sarah", "Killa"}
coartada_debil = {"Lara", "Carlos", "Rodrigo"}
print(f"Intersección: {acceso_lab & coartada_debil}")
print(f"Unión: {acceso_lab | coartada_debil}")
print(f"Diferencia (acceso - debil): {acceso_lab - coartada_debil}")
print(f"Diferencia (debil - acceso): {coartada_debil - acceso_lab}")
