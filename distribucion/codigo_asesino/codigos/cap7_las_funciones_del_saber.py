"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 7 - Las Funciones del Saber Ancestral
Conceptos: Funciones, parámetros, return, alcance de variables, docstrings
Autor: Alex Goyzueta Delgado
"""

# ============================================
# FUNCIONES DEL SABER ANCESTRAL
# ============================================

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida del laboratorio."""
    print("=" * 50)
    print("LABORATORIO YACHAY - Conocimiento Ancestral Digital")
    print("=" * 50)

mostrar_bienvenida()

# --- FUNCIÓN CON PARÁMETROS ---
def crear_ficha(nombre, edad, rol, nivel_sospecha):
    """Crea una ficha formateada de un sospechoso."""
    print(f"\n■ {nombre.upper()}")
    print(f"  Edad: {edad}")
    print(f"  Rol: {rol}")
    print(f"  Nivel de sospecha: {nivel_sospecha}/10")

crear_ficha("Lara Mamani", 32, "Asistente", 7)
crear_ficha("Dr. Carlos Huamán", 55, "Colega", 8)
crear_ficha("Mama Killa", 70, "Hermana", 5)

# --- PARÁMETROS POR DEFECTO ---
def crear_ficha_avanzada(nombre, edad, rol, nivel_sospecha=5, acceso=False):
    print(f"\n■ {nombre}")
    print(f"  Edad: {edad} | Rol: {rol}")
    print(f"  Sospecha: {nivel_sospecha}/10 | Acceso: {acceso}")

crear_ficha_avanzada("Rodrigo Mamani", 60, "Empresario", 9)
crear_ficha_avanzada("Sarah Chen", 40, "Colaboradora")
crear_ficha_avanzada("Visitante Desconocido", 0, "Desconocido")

# --- FUNCIÓN CON RETURN ---
def calcular_nivel_sospecha(acceso, coartada, motivo, huellas):
    """Calcula un nivel de sospecha basado en múltiples factores."""
    puntaje = 0
    if acceso:
        puntaje += 3
    if not coartada:
        puntaje += 4
    if motivo >= 7:
        puntaje += 3
    elif motivo >= 4:
        puntaje += 1
    if huellas:
        puntaje += 1
    return min(puntaje, 10)

nivel_lara = calcular_nivel_sospecha(True, False, 7, True)
nivel_carlos = calcular_nivel_sospecha(True, True, 8, False)
print(f"\nNivel de sospecha de Lara: {nivel_lara}/10")
print(f"Nivel de sospecha de Carlos: {nivel_carlos}/10")

# --- MÚLTIPLES VALORES DE RETORNO ---
def analizar_sospechoso_completo(nombre, acceso, coartada, motivo, huellas):
    nivel = calcular_nivel_sospecha(acceso, coartada, motivo, huellas)
    if nivel >= 8:
        categoria = "CRÍTICO"
        accion = "Interrogar inmediatamente"
    elif nivel >= 5:
        categoria = "ALTO"
        accion = "Vigilancia continua"
    elif nivel >= 3:
        categoria = "MODERADO"
        accion = "Mantener en observación"
    else:
        categoria = "BAJO"
        accion = "Sin acción requerida"
    return nivel, categoria, accion

nombre = "Lara Mamani"
nivel, categoria, accion = analizar_sospechoso_completo(nombre, True, False, 7, True)
print(f"\n=== RESULTADO: {nombre} ===")
print(f"Nivel: {nivel}/10")
print(f"Categoría: {categoria}")
print(f"Acción recomendada: {accion}")

# --- ALCANCE DE VARIABLES (SCOPE) ---
laboratorio = "Coricancha"
investigadora = "Wayra Condori"

def mostrar_caso():
    nombre_caso = "El Asesinato del Dr. Inti Quispe"
    print(f"\nCaso: {nombre_caso}")
    print(f"Lugar: {laboratorio}")
    print(f"Investigadora: {investigadora}")

mostrar_caso()

def cambiar_laboratorio():
    global laboratorio
    laboratorio = "Laboratorio Secreto del Qhapaq Ñan"
    print(f"Laboratorio cambiado a: {laboratorio}")

cambiar_laboratorio()
print(f"Laboratorio ahora es: {laboratorio}")

# --- DESCRIPCIÓN DEL QUIPU ---
def descifrar_quipu_digital(quipu_codificado):
    """Descifra un quipu digital y devuelve el mensaje oculto."""
    partes = quipu_codificado.split(":")
    tipo = partes[0]
    posiciones = [int(p) for p in partes[1:]]
    return {"tipo": tipo, "posiciones": posiciones, "mensaje": f"Decodificado: {tipo} - {posiciones}"}

quipu1 = descifrar_quipu_digital("ROJO:1:4:9")
quipu2 = descifrar_quipu_digital("BLANCO:1:3:5:7:9")
print(f"\nQuipu 1: {quipu1}")
print(f"Quipu 2: {quipu2}")

# --- SISTEMA COMPLETO DE ANÁLISIS ---
def generar_informe(sospechosos_analizados):
    print("\n" + "=" * 60)
    print("INFORME FORENSE DIGITAL - CASO INTI QUISPE")
    print("=" * 60)
    for nombre, datos in sospechosos_analizados.items():
        print(f"\n▶ {nombre}")
        print(f"  Nivel de sospecha: {datos['nivel']}/10")
        print(f"  Categoría: {datos['categoria']}")
        print(f"  Acción: {datos['accion']}")
    print("\n" + "=" * 60)
    print("FIN DEL INFORME")
    print("=" * 60)

sospechosos_data = {
    "Lara Mamani": {"acceso": True, "coartada": False, "motivo": 7, "huellas": True},
    "Carlos Huamán": {"acceso": True, "coartada": True, "motivo": 8, "huellas": False},
    "Sarah Chen": {"acceso": True, "coartada": True, "motivo": 6, "huellas": False},
    "Rodrigo Mamani": {"acceso": False, "coartada": True, "motivo": 9, "huellas": False},
    "Mama Killa": {"acceso": True, "coartada": True, "motivo": 5, "huellas": True}
}

resultados = {}
for nombre, datos in sospechosos_data.items():
    nivel, categoria, accion = analizar_sospechoso_completo(
        nombre, datos["acceso"], datos["coartada"], datos["motivo"], datos["huellas"])
    resultados[nombre] = {"nivel": nivel, "categoria": categoria, "accion": accion}

generar_informe(resultados)
