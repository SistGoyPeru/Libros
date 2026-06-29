"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 14 - El Código Asesino — Segunda Parte
Proyecto Integrador: Motor de análisis forense digital
Autor: Alex Goyzueta Delgado

Requiere: cap13_el_codigo_asesino_parte1.py (importa datos_caso y quipus)
"""

# ============================================
# MÓDULO: sospechosos.py (POO)
# ============================================

class Persona:
    def __init__(self, nombre, edad, rol):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
    def presentarse(self):
        return f"{self.nombre} ({self.edad}), {self.rol}"

class Sospechoso(Persona):
    def __init__(self, nombre, edad, rol, datos):
        super().__init__(nombre, edad, rol)
        self.acceso_lab = datos.get("acceso_lab", False)
        self.nivel_acceso = datos.get("nivel_acceso", 0)
        self.coartada = datos.get("coartada", "")
        self.coartada_valida = datos.get("coartada_valida", False)
        self.motivo = datos.get("motivo", "")
        self.intensidad_motivo = datos.get("intensidad_motivo", 0)
        self.huellas_escena = datos.get("huellas_escena", False)
        self.evidencias = datos.get("evidencias", [])
        self._puntaje_sospecha = 0
    
    def calcular_puntaje(self):
        puntaje = 0
        if self.acceso_lab:
            puntaje += 3 * (self.nivel_acceso / 10)
        if not self.coartada_valida:
            puntaje += 4
        puntaje += self.intensidad_motivo * 0.5
        if self.huellas_escena:
            puntaje += 2
        puntaje += len(self.evidencias) * 0.5
        self._puntaje_sospecha = min(puntaje, 10)
        return self._puntaje_sospecha
    
    def obtener_categoria(self):
        if self._puntaje_sospecha >= 8:
            return "CRÍTICO"
        elif self._puntaje_sospecha >= 6:
            return "ALTO"
        elif self._puntaje_sospecha >= 4:
            return "MODERADO"
        else:
            return "BAJO"
    
    def reporte(self):
        self.calcular_puntaje()
        return {
            "nombre": self.nombre,
            "puntaje": self._puntaje_sospecha,
            "categoria": self.obtener_categoria(),
            "evidencias": self.evidencias,
            "motivo": self.motivo
        }

# ============================================
# MÓDULO: analisis.py (Motor de análisis)
# ============================================

# Importar datos (simulado - en proyecto real iría en otro archivo)
# from datos_caso import *
# from quipus import *

# Datos inline para que este archivo sea autónomo
nombre_caso = "El Asesinato del Dr. Inti Quispe"
fecha_crimen = "27 de junio, 2026"
investigadora = "Wayra Condori"
hora_crimen = "02:34"

sospechosos_data = {
    "Lara Mamani": {
        "edad": 32, "rol": "Asistente de laboratorio",
        "acceso_lab": True, "nivel_acceso": 7,
        "coartada": "Departamento propio", "coartada_valida": False,
        "motivo": "Económico/Emocional (hija de Rodrigo)", "intensidad_motivo": 8,
        "huellas_escena": True,
        "evidencias": ["Registro de acceso a las 02:34", "Huellas en el teclado de Inti",
                       "Hija secreta de Rodrigo Mamani", "Llamada perdida de Inti a las 02:30"]
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
        "evidencias": ["Presión del MIT", "Visa próxima a vencer"]
    },
    "Rodrigo Mamani": {
        "edad": 60, "rol": "Empresario tecnológico",
        "acceso_lab": False, "nivel_acceso": 3,
        "coartada": "Cena de negocios (Hotel Monasterio)", "coartada_valida": True,
        "motivo": "Control de Yachay", "intensidad_motivo": 10,
        "huellas_escena": False,
        "evidencias": ["Líder de Los Herederos de Pizarro", "Padre secreto de Lara Mamani"]
    },
    "Mama Killa": {
        "edad": 70, "rol": "Hermana de Inti",
        "acceso_lab": True, "nivel_acceso": 9,
        "coartada": "Su casa en San Blas", "coartada_valida": False,
        "motivo": "Protección del legado familiar", "intensidad_motivo": 6,
        "huellas_escena": True,
        "evidencias": ["Miembro del Círculo del Sol", "Conocía el pasaje secreto"]
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


def analizar_quipus_completo():
    print("=" * 65)
    print("  ANÁLISIS DE QUIPUS DIGITALES")
    print("=" * 65)
    print("  (Simulación - datos de quipus no cargados)")
    print("  Quipus disponibles en cap13_el_codigo_asesino_parte1.py")

def crear_sospechosos():
    objetos = []
    for nombre, datos in sospechosos_data.items():
        s = Sospechoso(nombre, datos["edad"], datos["rol"], datos)
        objetos.append(s)
    return objetos

def verificar_coartadas(registros, hora_crimen):
    print("\n  ► Verificación de coartadas:")
    print(f"    Hora del crimen: {hora_crimen}")
    h_c, m_c = map(int, hora_crimen.split(":"))
    min_crimen = h_c * 60 + m_c
    estado = {}
    for reg in registros:
        h, m = map(int, reg["hora"].split(":"))
        mins = h * 60 + m
        if reg["tipo"] == "entrada":
            estado[reg["persona"]] = mins
        elif reg["tipo"] == "salida" and reg["persona"] in estado:
            del estado[reg["persona"]]
    print("    Personas dentro del lab a las 02:34:")
    for p, m in estado.items():
        if m <= min_crimen:
            print(f"      • {p}")

def analizar_evidencias(sospechosos_objetos):
    print("\n  ► Resumen de evidencias:")
    for s in sospechosos_objetos:
        print(f"    • {s.nombre}")
        for ev in s.evidencias:
            print(f"      - {ev}")

def calcular_puntajes(sospechosos_objetos):
    print("\n  ► Puntajes de sospecha:\n")
    resultados = []
    for s in sospechosos_objetos:
        r = s.reporte()
        resultados.append(r)
        barra = "█" * int(r["puntaje"]) + "░" * (10 - int(r["puntaje"]))
        print(f"    {r['nombre']:25} [{barra}] {r['puntaje']:.1f}/10 ({r['categoria']})")
    return resultados

def determinar_culpable(resultados):
    print("\n" + "=" * 65)
    print("  VEREDICTO DEL ANÁLISIS FORENSE DIGITAL")
    print("=" * 65)
    resultados.sort(key=lambda r: r["puntaje"], reverse=True)
    for i, r in enumerate(resultados, 1):
        print(f"  {i}. {r['nombre']:25} - {r['puntaje']:.1f}/10")
    principal = resultados[0]
    print(f"\n  ► SOSPECHOSO PRINCIPAL: {principal['nombre']}")
    print(f"    Puntaje: {principal['puntaje']:.1f}/10")
    print(f"    Motivo: {principal['motivo']}")
    print(f"    Evidencias: {len(principal['evidencias'])}")
    print(f"\n  Conclusión: {principal['nombre'].upper()}")
    return principal

def generar_informe(resultados, culpable):
    with open("informe_final_caso.txt", "w", encoding="utf-8") as f:
        f.write(f"INFORME FINAL: {nombre_caso}\n")
        f.write(f"Investigadora: {investigadora}\n\n")
        f.write("--- PUNTAJES ---\n")
        for r in sorted(resultados, key=lambda r: r["puntaje"], reverse=True):
            f.write(f"  {r['nombre']:25} {r['puntaje']:.1f}/10 ({r['categoria']})\n")
        f.write(f"\n--- CULPABLE ---\n")
        f.write(f"  {culpable['nombre']}\n")
        for ev in culpable['evidencias']:
            f.write(f"    - {ev}\n")
    print(f"\n  ► Informe generado: informe_final_caso.txt")

def main():
    print("\n  ╔═════════════════════════════════════════╗")
    print("  ║    CÓDIGO ASESINO - ANÁLISIS FORENSE   ║")
    print("  ╚═════════════════════════════════════════╝")
    print(f"\n  Caso: {nombre_caso}")
    print(f"  Investigadora: {investigadora}\n")
    
    sospechosos = crear_sospechosos()
    verificar_coartadas(registro_accesos, hora_crimen)
    analizar_evidencias(sospechosos)
    resultados = calcular_puntajes(sospechosos)
    input("\n  Presiona Enter para revelar el veredicto...\n")
    culpable = determinar_culpable(resultados)
    generar_informe(resultados, culpable)
    print("\n" + "=" * 65)
    print("  ANÁLISIS COMPLETADO")
    print("=" * 65)

if __name__ == "__main__":
    main()
