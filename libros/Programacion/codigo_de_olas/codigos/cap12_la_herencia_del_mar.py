"""Capitulo 12: La Herencia del Mar
Conceptos: Herencia, polimorfismo, encapsulacion, super()
"""

# ============================================
# HERENCIA EN EL OCEANO DIGITAL
# ============================================

class Embarcacion:
    """Clase base para todas las embarcaciones."""

    def __init__(self, nombre, eslora, capacidad):
        self.nombre = nombre
        self.eslora = eslora  # metros
        self.capacidad = capacidad  # personas
        self._activo = True

    def zarpar(self):
        return f"Sail {self.nombre} ha zarpado"

    def atracar(self):
        return f"Sail {self.nombre} ha atracado"

    def info(self):
        return f"{self.nombre}: {self.eslora}m, {self.capacidad} pers."

class BarcoPesquero(Embarcacion):
    def __init__(self, nombre, eslora, capacidad, tipo_red):
        super().__init__(nombre, eslora, capacidad)
        self.tipo_red = tipo_red
        self.pescado = 0

    def pescar(self):
        self.pescado += 100
        return f"Fish {self.nombre} pesco 100 kg con red {self.tipo_red}"

    def info(self):
        return f"{super().info()} | Pescador, red: {self.tipo_red}"

class YatePrivado(Embarcacion):
    def __init__(self, nombre, eslora, capacidad, dueno):
        super().__init__(nombre, eslora, capacidad)
        self.dueno = dueno

    def info(self):
        return f"{super().info()} | Yate de {self.dueno}"

print("=== EMBARCACIONES DE ANCON ===\n")
don_eulogio = BarcoPesquero("Don Eulogio", 8, 4, "enmalle")
costa_azul = YatePrivado("Costa Azul", 25, 12, "Miguel Angel Soto")

print(don_eulogio.info())
print(costa_azul.info())
print(don_eulogio.zarpar())
print(don_eulogio.pescar())

# Polimorfismo: Mismo mensaje, diferente respuesta
print("\n=== POLIMORFISMO: TODOS ZARPAN ===\n")
barcos = [
    BarcoPesquero("Mares del Sur", 12, 6, "arrastre"),
    YatePrivado("Costa Azul", 25, 12, "Soto"),
    BarcoPesquero("Ancon I", 7, 3, "cerco"),
]
for barco in barcos:
    print(barco.info())
    print(f"  -> {barco.zarpar()}")

# Herencia multiple
class Capitan:
    def __init__(self, nombre, licencia):
        self.nombre_capitan = nombre
        self.licencia = licencia
    def dirigir(self):
        return f"Capitan {self.nombre_capitan} dirigiendo"

class Navegante:
    def __init__(self, sistema_gps):
        self.sistema_gps = sistema_gps
    def navegar(self, destino):
        return f"Navegando a {destino} con {self.sistema_gps}"

class BarcoModerno(Embarcacion, Capitan, Navegante):
    def __init__(self, nombre, eslora, capacidad, capitan, licencia, gps):
        Embarcacion.__init__(self, nombre, eslora, capacidad)
        Capitan.__init__(self, capitan, licencia)
        Navegante.__init__(self, gps)

print("\n=== BARCO MODERNO ===")
b = BarcoModerno("Investigador I", 20, 15, "Mateo", "CAP-001", "GPS Pro")
print(b.info())
print(b.dirigir())
print(b.navegar("Generador LOCUENTO"))

# Encapsulacion: Secretos del mar
class ProyectoSecreto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self._presupuesto = presupuesto
        self.__clave_acceso = "SOLO_INVESTIGACION"

    def obtener_presupuesto(self, nivel_acceso):
        if nivel_acceso >= 5:
            return f"Presupuesto: ${self._presupuesto:,}"
        return "Lock Acceso denegado"

p = ProyectoSecreto("LOCUENTO", 2500000)
print(f"\nNombre: {p.nombre}")
print(p.obtener_presupuesto(3))
print(p.obtener_presupuesto(5))

# --- ENIGMAS ---

print("\n=== ENIGMA 12.1: Jerarquia de playas ===")
class ZonaCostera:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

class PlayaPublica(ZonaCostera):
    def __init__(self, nombre, ubicacion, tiene_acceso_gratuito):
        super().__init__(nombre, ubicacion)
        self.tiene_acceso_gratuito = tiene_acceso_gratuito

class PlayaPrivada(ZonaCostera):
    def __init__(self, nombre, ubicacion, dueno):
        super().__init__(nombre, ubicacion)
        self.dueno = dueno

pub = PlayaPublica("Ancon", "Lima", True)
priv = PlayaPrivada("Costa Azul", "Lima", "Soto Holding")
print(f"Publica: {pub.nombre}, Gratuito: {pub.tiene_acceso_gratuito}")
print(f"Privada: {priv.nombre}, Dueno: {priv.dueno}")

print("\n=== ENIGMA 12.2: Polimorfismo con sonidos ===")
class SonidoMarino:
    def sonido(self):
        return "..."

class OlaMarina(SonidoMarino):
    def sonido(self):
        return "!Swish!"

class Barco(SonidoMarino):
    def sonido(self):
        return "!Buuu!"

for s in [OlaMarina(), Barco()]:
    print(f"{type(s).__name__}: {s.sonido()}")

print("\n=== ENIGMA 12.3: Encapsulacion bancaria ===")
class CuentaMaritima:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Depositado ${monto}. Nuevo saldo: ${self.__saldo}")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retirado ${monto}. Nuevo saldo: ${self.__saldo}")
        else:
            print("Fondos insuficientes")

cuenta = CuentaMaritima("Pescador Local", 500)
cuenta.depositar(200)
cuenta.retirar(100)
