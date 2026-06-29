"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 13 - El Código Asesino — Primera Parte
Proyecto Integrador: Módulos de datos y modelos
Autor: Alex Goyzueta Delgado

NOTA: Este archivo contiene los módulos datos_caso.py y quipus.py
del proyecto integrador. Para ejecutar el proyecto completo,
use cap14_el_codigo_asesino_parte2.py y cap15_el_epilogo.py
"""

# ============================================
# MÓDULO: datos_caso.py
# ============================================

nombre_caso = "El Asesinato del Dr. Inti Quispe"
fecha_crimen = "27 de junio, 2026"
lugar_crimen = "Templo del Sol (Coricancha), Neo-Cusco"
hora_crimen = "02:34"
investigadora = "Wayra Condori"

quipus_del_caso = [
    {"id": "Q001", "color": "rojo", "nudos": [1, 4, 9], "significado": "conflicto/guerra"},
    {"id": "Q002", "color": "verde", "nudos": [2, 5, 10], "significado": "crecimiento/conocimiento"},
    {"id": "Q003", "color": "azul", "nudos": [1, 5, 9], "significado": "espiritualidad/religión"},
    {"id": "Q004", "color": "amarillo", "nudos": [3, 7, 11], "significado": "poder/riqueza"},
    {"id": "Q005", "color": "blanco", "nudos": [1, 3, 5, 7, 9, 11], "significado": "verdad/conexión espiritual"}
]

sospechosos_data = {
    "Lara Mamani": {
        "edad": 32, "rol": "Asistente de laboratorio",
        "acceso_lab": True, "nivel_acceso": 7,
        "coartada": "Departamento propio", "coartada_valida": False,
        "motivo": "Económico/Emocional (hija de Rodrigo)", "intensidad_motivo": 8,
        "huellas_escena": True,
        "evidencias": [
            "Registro de acceso a las 02:34", "Huellas en el teclado de Inti",
            "Hija secreta de Rodrigo Mamani", "Llamada perdida de Inti a las 02:30"
        ]
    },
    "Dr. Carlos Huamán": {
        "edad": 55, "rol": "Colega universitario",
        "acceso_lab": True, "nivel_acceso": 5,
        "coartada": "Oficina universitaria (no verificada)", "coartada_valida": False,
        "motivo": "Envidia profesional", "intensidad_motivo": 7,
        "huellas_escena": False,
        "evidencias": ["Discusión pública con Inti", "Publicación bloqueada por Inti"]
    },
    "Dra. Sarah Chen": {
        "edad": 40, "rol": "Colaboradora del MIT",
        "acceso_lab": True, "nivel_acceso": 6,
        "coartada": "Videollamada con MIT (02:00-03:30)", "coartada_valida": True,
        "motivo": "Presión académica", "intensidad_motivo": 5,
        "huellas_escena": False,
        "evidencias": ["Presión del MIT", "Visa próxima a vencer", "Oferta de NeuralCorp"]
    },
    "Rodrigo Mamani": {
        "edad": 60, "rol": "Empresario tecnológico",
        "acceso_lab": False, "nivel_acceso": 3,
        "coartada": "Cena de negocios (Hotel Monasterio)", "coartada_valida": True,
        "motivo": "Control de Yachay", "intensidad_motivo": 10,
        "huellas_escena": False,
        "evidencias": [
            "Líder de Los Herederos de Pizarro", "Padre secreto de Lara Mamani",
            "Ofertas de compra rechazadas por Inti"
        ]
    },
    "Mama Killa": {
        "edad": 70, "rol": "Hermana de Inti",
        "acceso_lab": True, "nivel_acceso": 9,
        "coartada": "Su casa en San Blas", "coartada_valida": False,
        "motivo": "Protección del legado familiar", "intensidad_motivo": 6,
        "huellas_escena": True,
        "evidencias": [
            "Miembro del Círculo del Sol", "Conocía el pasaje secreto",
            "Mensaje de Inti: 'Mama Killa sabe la verdad'"
        ]
    }
}

registro_accesos = [
    {"persona": "Lara", "hora": "08:15", "tipo": "entrada"},
    {"persona": "Inti", "hora": "08:30", "tipo": "entrada"},
    {"persona": "Carlos", "hora": "09:00", "tipo": "entrada"},
    {"persona": "Lara", "hora": "12:30", "tipo": "salida"},
    {"persona": "Lara", "hora": "13:30", "tipo": "entrada"},
    {"persona": "Carlos", "hora": "14:00", "tipo": "salida"},
    {"persona": "Sarah", "hora": "14:30", "tipo": "entrada"},
    {"persona": "Sarah", "hora": "16:00", "tipo": "salida"},
    {"persona": "Inti", "hora": "18:00", "tipo": "salida"},
    {"persona": "Inti", "hora": "22:00", "tipo": "entrada"},
    {"persona": "Lara", "hora": "02:34", "tipo": "entrada"},
    {"persona": "Lara", "hora": "02:45", "tipo": "salida"},
]

# ============================================
# MÓDULO: quipus.py
# ============================================

def decodificar_quipu(quipu):
    color = quipu["color"]
    nudos = quipu["nudos"]
    significado = quipu["significado"]
    
    if all(n % 2 == 1 for n in nudos):
        tipo = "PREGUNTA"
    elif all(n % 2 == 0 for n in nudos):
        tipo = "RESPUESTA"
    else:
        tipo = "MENSAJE MIXTO"
    
    if len(nudos) >= 2:
        diferencias = [nudos[i+1] - nudos[i] for i in range(len(nudos)-1)]
        patron = diferencias[0] if len(set(diferencias)) == 1 else "variable"
    else:
        patron = "único"
    
    return {
        "color": color, "significado": significado, "tipo": tipo,
        "total_nudos": len(nudos), "posiciones": nudos, "patron": patron,
        "mensaje_decodificado": f"{color.upper()}: {significado} ({tipo})"
    }

def decodificar_todos_los_quipus(lista_quipus):
    return [decodificar_quipu(q) for q in lista_quipus]

def buscar_quipu_por_color(lista_quipus, color):
    return [q for q in lista_quipus if q["color"] == color]

def quipu_a_string(quipu):
    return (f"  [{quipu['color'].upper():8}] {quipu['significado']:30} "
            f"| {quipu['tipo']:15} | {quipu['total_nudos']} nudos")

# --- DEMO ---
if __name__ == "__main__":
    print("=== MÓDULOS DEL PROYECTO CARGADOS ===")
    print(f"Caso: {nombre_caso}")
    print(f"Quipus registrados: {len(quipus_del_caso)}")
    print(f"Sospechosos registrados: {len(sospechosos_data)}")
    
    print("\n--- Decodificando quipus ---")
    for q in decodificar_todos_los_quipus(quipus_del_caso):
        print(quipu_a_string(q))
    
    blanco = buscar_quipu_por_color(quipus_del_caso, "blanco")
    if blanco:
        print(f"\nQuipu blanco: {blanco[0]['nudos']} → {len(blanco[0]['nudos'])} nudos (clave del caso)")
