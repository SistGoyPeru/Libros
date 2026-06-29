"""Capitulo 11: La Clase del Surfista
Conceptos: POO, clases, objetos, atributos, metodos
"""

# ============================================
# MODELANDO EL OCEANO CON CLASES
# ============================================

class Ola:
    """Representa una ola del mar."""

    def __init__(self, altura, frecuencia, direccion):
        self.altura = altura
        self.frecuencia = frecuencia
        self.direccion = direccion
        self.rota = False

    def romper(self):
        """La ola rompe en la orilla."""
        self.rota = True
        return f"~ !Ola de {self.altura}m rompiendo!"

    def es_surfeable(self):
        return 0.8 <= self.altura <= 3.0

    def info(self):
        return f"Ola: {self.altura}m, cada {self.frecuencia}s, direccion {self.direccion}"

ola_1 = Ola(1.8, 12, "SO")
ola_2 = Ola(2.4, 8, "O")
ola_3 = Ola(0.5, 20, "NO")

print("=== OLAS CREADAS ===")
print(ola_1.info())
print(ola_2.info())
print(ola_3.info())

print(f"\nOla 1 surfeable? {ola_1.es_surfeable()}")
print(f"Ola 3 surfeable? {ola_3.es_surfeable()}")

print(f"\n{ola_2.romper()}")

# La clase Implicado
class Implicado:
    """Persona involucrada en el proyecto LOCUENTO."""

    def __init__(self, nombre, rol, nivel_riesgo=5):
        self.nombre = nombre
        self.rol = rol
        self.nivel_riesgo = nivel_riesgo
        self.evidencias = []
        self.interrogado = False

    def agregar_evidencia(self, evidencia):
        self.evidencias.append(evidencia)
        self.nivel_riesgo += 1
        print(f"  ! Evidencia contra {self.nombre}: {evidencia}")

    def interrogar(self):
        self.interrogado = True
        print(f"\n  > INTERROGANDO A {self.nombre.upper()}")
        print(f"    Rol: {self.rol}")
        print(f"    Riesgo: {self.nivel_riesgo}/10")
        print(f"    Evidencias: {len(self.evidencias)}")
        if self.nivel_riesgo >= 7:
            return f"    -> {self.nombre} es ALTAMENTE SOSPECHOSO"
        elif self.nivel_riesgo >= 4:
            return f"    -> {self.nombre} requiere vigilancia"
        return f"    -> {self.nombre} tiene perfil bajo"

carlos = Implicado("Carlos Parra", "Ingeniero Naval", 8)
luisa = Implicado("Luisa Rivas", "Biologa Marina", 3)
soto = Implicado("Miguel Angel Soto", "Empresario", 9)

print("\n=== IMPLICADOS CREADOS ===")
carlos.agregar_evidencia("Diseno el generador")
soto.agregar_evidencia("Financia el proyecto")
soto.agregar_evidencia("Dueno del terreno")
print(carlos.interrogar())
print(soto.interrogar())

# Atributos de clase
class Investigacion:
    nombre_caso = "Operacion LOCUENTO - Contaminacion de Olas"
    total_investigadores = 0

    def __init__(self, investigador):
        self.investigador = investigador
        self.implicados = []
        self.evidencias = []
        self.estado = "abierta"
        Investigacion.total_investigadores += 1

    def agregar_implicado(self, implicado):
        self.implicados.append(implicado)

    def resumen(self):
        print(f"\n=== {self.nombre_caso} ===")
        print(f"Investigador: {self.investigador}")
        print(f"Implicados: {len(self.implicados)}")
        print(f"Evidencias: {len(self.evidencias)}")
        print(f"Investigadores activos: {Investigacion.total_investigadores}")

caso = Investigacion("Mateo Sanchez")
caso.agregar_implicado(carlos)
caso.agregar_implicado(soto)
caso.evidencias.append("Firmware del generador")
caso.evidencias.append("Registro de activaciones")
caso.resumen()

# --- ENIGMAS ---

print("\n=== ENIGMA 11.1: Clase TablaDeSurf ===")
class TablaDeSurf:
    def __init__(self, marca, longitud, material):
        self.marca = marca
        self.longitud = longitud
        self.material = material

    def remar(self):
        print(f"Remando en {self.marca}")

tabla = TablaDeSurf("OceanRider", 6.2, "fibra de vidrio")
tabla.remar()

print("\n=== ENIGMA 11.2: Clase con contador ===")
class OlaConContador:
    total_olas = 0

    def __init__(self, altura, frecuencia, direccion):
        self.altura = altura
        self.frecuencia = frecuencia
        self.direccion = direccion
        OlaConContador.total_olas += 1

    @classmethod
    def cuantas_olas(cls):
        return cls.total_olas

o1 = OlaConContador(1.5, 12, "SO")
o2 = OlaConContador(2.0, 8, "O")
print(f"Total de olas creadas: {OlaConContador.cuantas_olas()}")

print("\n=== ENIGMA 11.3: Sistema de playas ===")
class Playa:
    def __init__(self, nombre, ubicacion, tiene_muelle):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tiene_muelle = tiene_muelle

    def info(self):
        muelle_str = "si" if self.tiene_muelle else "no"
        return f"Playa {self.nombre} en {self.ubicacion} (muelle: {muelle_str})"

playa1 = Playa("Ancon", "Lima", True)
playa2 = Playa("Miraflores", "Lima", True)
playa3 = Playa("Punta Hermosa", "Lima Sur", False)

for p in [playa1, playa2, playa3]:
    print(p.info())
