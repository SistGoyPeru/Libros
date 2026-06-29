"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 12 - La Herencia de los Incas
Conceptos: Herencia, polimorfismo, encapsulación, super()
Autor: Alex Goyzueta Delgado
"""

# ============================================
# HERENCIA: EL ÁRBOL DEL CONOCIMIENTO
# ============================================

class Persona:
    """Clase base para todas las personas en el sistema."""
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self._vivo = True
    
    def presentarse(self):
        return f"Soy {self.nombre}, de {self.edad} años."
    
    def esta_vivo(self):
        return self._vivo

class Sospechoso(Persona):
    """Un sospechoso es una Persona con características adicionales."""
    def __init__(self, nombre, edad, dni, motivo=""):
        super().__init__(nombre, edad, dni)
        self.motivo = motivo
        self.nivel_sospecha = 0
    
    def agregar_evidencia(self, peso):
        self.nivel_sospecha += peso
    
    def presentarse(self):
        return f"{super().presentarse()} | SOSPECHOSO - Motivo: {self.motivo}"

class Investigador(Persona):
    def __init__(self, nombre, edad, dni, placa, rango):
        super().__init__(nombre, edad, dni)
        self.placa = placa
        self.rango = rango
        self.casos_asignados = []
    
    def presentarse(self):
        return f"{super().presentarse()} | INVESTIGADOR - Placa: {self.placa}"

print("=== HERENCIA EN ACCIÓN ===\n")
sospechoso1 = Sospechoso("Lara Mamani", 32, "DNI-47291", "Económico/Emocional")
investigador1 = Investigador("Wayra Condori", 28, "DNI-83921", "PI-007", "Analista Senior")
print(sospechoso1.presentarse())
print(investigador1.presentarse())

# --- POLIMORFISMO ---
print("\n=== POLIMORFISMO ===")
personas = [
    Sospechoso("Carlos Huamán", 55, "DNI-56123", "Envidia profesional"),
    Investigador("Raúl Cusi", 35, "DNI-78234", "PER-023", "Periodista"),
    Sospechoso("Mama Killa", 70, "DNI-34567", "Secreto familiar"),
    Investigador("Wayra Condori", 28, "DNI-83921", "PI-007", "Analista Senior"),
]
for persona in personas:
    print(persona.presentarse())
    if isinstance(persona, Sospechoso):
        print(f"  → Nivel de sospecha: {persona.nivel_sospecha}")
    elif isinstance(persona, Investigador):
        print(f"  → Casos asignados: {len(persona.casos_asignados)}")

# --- HERENCIA MÚLTIPLE ---
class GuardianDeTradicion:
    def __init__(self, tradiciones_conocidas=None):
        self.tradiciones = tradiciones_conocidas or []
    def ensenar_tradicion(self):
        return f"Enseñando: {', '.join(self.tradiciones)}"

class ExpertoEnTecnologia:
    def __init__(self, tecnologias=None):
        self.tecnologias = tecnologias or []
    def programar(self, lenguaje):
        return f"Programando en {lenguaje}"

class QuipucamayocDigital(GuardianDeTradicion, ExpertoEnTecnologia):
    def __init__(self, nombre, tradiciones, tecnologias, nivel_maestria):
        GuardianDeTradicion.__init__(self, tradiciones)
        ExpertoEnTecnologia.__init__(self, tecnologias)
        self.nombre = nombre
        self.nivel_maestria = nivel_maestria
    def descifrar_quipu(self, quipu):
        return f"Descifrando {quipu} con sabiduría ancestral y tecnología moderna"

inti = QuipucamayocDigital(
    "Inti Quispe",
    ["quipus", "tejido andino", "medicina ancestral", "calendario inca"],
    ["Python", "Machine Learning", "Computación Cuántica", "Blockchain"],
    10
)
print(f"\n=== QUIPUCAMAYOC DIGITAL ===")
print(f"Nombre: {inti.nombre}")
print(f"Nivel de maestría: {inti.nivel_maestria}/10")
print(inti.ensenar_tradicion())
print(inti.programar("Python"))
print(inti.descifrar_quipu("BLANCO:1:3:5:7:9"))

# --- ENCAPSULACIÓN ---
class SecretoFamiliar:
    def __init__(self, contenido, nivel_clasificacion):
        self._contenido = contenido
        self.__nivel = nivel_clasificacion
        self.publico = True
    def obtener_secreto(self, clave):
        if clave == "YACHAY_ACCESS":
            return f"Secreto (nivel {self.__nivel}): {self._contenido}"
        return "🔒 Acceso denegado"

secreto = SecretoFamiliar("Lara es hija de Rodrigo Mamani", 7)
print(f"\n=== ENCAPSULACIÓN ===")
print(f"Atributo público: {secreto.publico}")
print(f"Atributo 'privado': {secreto._contenido}")
print(f"Name mangling: {secreto._SecretoFamiliar__nivel}")
print(secreto.obtener_secreto("clave_incorrecta"))
print(secreto.obtener_secreto("YACHAY_ACCESS"))

# --- MODELO COMPLETO ---
class EntidadYachay:
    def __init__(self, id_entidad):
        self.id = id_entidad

class Persona2(EntidadYachay):
    def __init__(self, id_entidad, nombre, edad):
        super().__init__(id_entidad)
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        return f"{self.nombre}, {self.edad} años"

class MiembroLaboratorio(Persona2):
    def __init__(self, id_entidad, nombre, edad, rol, nivel_acceso):
        super().__init__(id_entidad, nombre, edad)
        self.rol = rol
        self.nivel_acceso = nivel_acceso
        self.registros_acceso = []
    def registrar_acceso(self, hora, tipo):
        self.registros_acceso.append({"hora": hora, "tipo": tipo})
        print(f"  {self.nombre}: {tipo} a las {hora}")

class SospechosoCompleto(MiembroLaboratorio):
    def __init__(self, id_entidad, nombre, edad, rol, nivel_acceso, motivo):
        super().__init__(id_entidad, nombre, edad, rol, nivel_acceso)
        self.motivo = motivo
    def verificar_coartada(self):
        return f"Coartada de {self.nombre} verificada"

print("\n=== MODELO COMPLETO DEL CASO ===")
lara = SospechosoCompleto("P002", "Lara Mamani", 32, "Asistente", 7, "Hija de Rodrigo")
lara.registrar_acceso("08:15", "entrada")
lara.registrar_acceso("02:34", "entrada (fraudulenta)")
print(lara.presentarse())
