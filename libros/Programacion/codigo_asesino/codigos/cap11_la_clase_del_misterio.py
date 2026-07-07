"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 11 - La Clase del Misterio
Conceptos: POO, clases, objetos, atributos, métodos, __init__, self
Autor: Alex Goyzueta Delgado
"""

# ============================================
# MODELANDO EL MISTERIO CON CLASES
# ============================================

class QuipuDigital:
    """Representa un quipu digital."""
    
    def __init__(self, color, posiciones, significado=""):
        self.color = color
        self.posiciones = posiciones
        self.significado = significado
        self.descifrado = False
    
    def descifrar(self):
        mensaje = f"Quipu {self.color}: {len(self.posiciones)} nudos en posiciones {self.posiciones}"
        self.descifrado = True
        return mensaje
    
    def agregar_nudo(self, posicion):
        if posicion not in self.posiciones:
            self.posiciones.append(posicion)
            self.posiciones.sort()
            print(f"  ✓ Nudo agregado en posición {posicion}")
        else:
            print(f"  ✗ Ya existe un nudo en posición {posicion}")

quipu_rojo = QuipuDigital("rojo", [1, 4, 9], "conflicto")
quipu_blanco = QuipuDigital("blanco", [1, 3, 5, 7, 9], "verdad")

print("=== QUIPUS DIGITALES CREADOS ===")
print(f"Quipu rojo: {quipu_rojo.color} - {quipu_rojo.significado}")
print(f"Quipu blanco: {quipu_blanco.color} - {quipu_blanco.significado}")
print(f"\n{quipu_rojo.descifrar()}")
print(quipu_blanco.descifrar())
quipu_blanco.agregar_nudo(11)
quipu_blanco.agregar_nudo(5)

# --- CLASE SOSPECHOSO ---
class Sospechoso:
    """Representa un sospechoso en el caso."""
    
    def __init__(self, nombre, edad, rol, acceso=False):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
        self.acceso = acceso
        self.nivel_sospecha = 0
        self.coartada = ""
        self.evidencias = []
        self.interrogado = False
    
    def agregar_evidencia(self, evidencia):
        self.evidencias.append(evidencia)
        self.nivel_sospecha += 2
        print(f"  ⚠ Evidencia contra {self.nombre}: {evidencia}")
    
    def establecer_coartada(self, coartada):
        self.coartada = coartada
        print(f"  ✓ Coartada registrada: {coartada}")
    
    def interrogar(self):
        self.interrogado = True
        print(f"\n  === INTERROGANDO A {self.nombre.upper()} ===")
        print(f"  Edad: {self.edad}")
        print(f"  Rol: {self.rol}")
        print(f"  Acceso: {self.acceso}")
        print(f"  Coartada: {self.coartada or 'No proporcionada'}")
        print(f"  Evidencias: {len(self.evidencias)}")
        if self.nivel_sospecha >= 6:
            return f"  → {self.nombre} es ALTAMENTE SOSPECHOSO"
        elif self.nivel_sospecha >= 3:
            return f"  → {self.nombre} es MODERADAMENTE SOSPECHOSO"
        else:
            return f"  → {self.nombre} es POCO SOSPECHOSO"

lara = Sospechoso("Lara Mamani", 32, "Asistente", acceso=True)
carlos = Sospechoso("Dr. Carlos Huamán", 55, "Colega universitario", acceso=True)

print("\n=== SOSPECHOSOS CREADOS ===")
lara.agregar_evidencia("Registro de acceso a las 2:34")
lara.agregar_evidencia("Huellas en el teclado")
lara.establecer_coartada("Estaba en su departamento (sin verificar)")
carlos.agregar_evidencia("Discusión con Inti días antes")
carlos.establecer_coartada("Oficina universitaria")
print(lara.interrogar())
print(carlos.interrogar())

# --- ATRIBUTOS DE CLASE VS INSTANCIA ---
class Investigacion:
    nombre_del_caso = "El Asesinato del Dr. Inti Quispe"
    total_investigadores = 0
    
    def __init__(self, investigador_principal):
        self.investigador = investigador_principal
        self.sospechosos = []
        self.evidencias_encontradas = []
        self.estado = "abierta"
        Investigacion.total_investigadores += 1
    
    def agregar_sospechoso(self, sospechoso):
        self.sospechosos.append(sospechoso)
    
    def agregar_evidencia(self, evidencia):
        self.evidencias_encontradas.append(evidencia)
    
    def resumen(self):
        print(f"\n=== {self.nombre_del_caso} ===")
        print(f"Investigador: {self.investigador}")
        print(f"Estado: {self.estado}")
        print(f"Sospechosos: {len(self.sospechosos)}")
        print(f"Evidencias: {len(self.evidencias_encontradas)}")
        print(f"Total investigadores activos: {Investigacion.total_investigadores}")

caso = Investigacion("Wayra Condori")
caso.agregar_sospechoso(lara)
caso.agregar_sospechoso(carlos)
caso.agregar_evidencia("Quipu digital modificado")
caso.agregar_evidencia("Registro de acceso fraudulento")
caso.resumen()

# --- MODELO YACHAY ---
class PersonaYachay:
    def __init__(self, id_persona, nombre_real, rol_en_sistema, secreto=None,
                 lealtad="desconocida", nivel_acceso=0):
        self.id = id_persona
        self.nombre = nombre_real
        self.rol = rol_en_sistema
        self.secreto = secreto
        self.lealtad = lealtad
        self.nivel_acceso = nivel_acceso
        self._conexiones = []
    
    def revelar_secreto(self, clave_acceso):
        if clave_acceso == "YACHAY_ADMIN":
            return f"Secreto de {self.nombre}: {self.secreto}"
        return "Acceso denegado"
    
    def conectar_con(self, otra_persona):
        self._conexiones.append(otra_persona.id)
        print(f"  🔗 {self.nombre} → {otra_persona.nombre}")

print("\n=== PERSONAS EN EL SISTEMA YACHAY ===")
personas = [
    PersonaYachay("P001", "Inti Quispe", "Creador", "Llave... quipu blanco...", "Círculo del Sol", 10),
    PersonaYachay("P002", "Lara Mamani", "Asistente", "Hija de Rodrigo Mamani", "Dividida", 7),
    PersonaYachay("P003", "Carlos Huamán", "Colega", "Saboteó publicación de Inti", "Universidad", 5),
    PersonaYachay("P006", "Mama Killa", "Guardiana", "Sabe quién mató a Inti", "Círculo del Sol", 9),
    PersonaYachay("P007", "Wayra Condori", "Investigadora", "Nieta de Teodora", "En desarrollo", 1)
]
for p in personas:
    print(f"  [{p.id}] {p.nombre:25} | Rol: {p.rol:20} | Lealtad: {p.lealtad}")

print("\nSecretos:")
for p in personas:
    print(f"  {p.nombre}: {p.revelar_secreto('YACHAY_ADMIN')}")
