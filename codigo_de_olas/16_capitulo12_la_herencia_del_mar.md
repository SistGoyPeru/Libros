# Capítulo 12: La Herencia del Mar

## Conceptos: Herencia, polimorfismo, encapsulación, `super()`

---

Mateo descubrió que el código del generador usaba herencia de clases. Había una clase base `Dispositivo`, y de ella heredaban `GeneradorOlas`, `SensorMarino`, y `TransmisorMensajes`.

—Es como el océano —dijo—. El `Mar` es la clase base. De él heredan `Playa`, `Ola`, `Corriente`. Todos comparten atributos del mar, pero cada uno tiene sus propios métodos.

## Herencia: La familia del océano

```python
# ============================================
# HERENCIA EN EL OCÉANO DIGITAL
# ============================================

class Embarcacion:
    """Clase base para todas las embarcaciones."""
    
    def __init__(self, nombre, eslora, capacidad):
        self.nombre = nombre
        self.eslora = eslora  # metros
        self.capacidad = capacidad  # personas
        self._activo = True
    
    def zarpar(self):
        return f"⛵ {self.nombre} ha zarpado"
    
    def atracar(self):
        return f"⛵ {self.nombre} ha atracado"
    
    def info(self):
        return f"{self.nombre}: {self.eslora}m, {self.capacidad} pers."

class BarcoPesquero(Embarcacion):
    def __init__(self, nombre, eslora, capacidad, tipo_red):
        super().__init__(nombre, eslora, capacidad)
        self.tipo_red = tipo_red
        self.pescado = 0
    
    def pescar(self):
        self.pescado += 100
        return f"🎣 {self.nombre} pescó 100 kg con red {self.tipo_red}"
    
    def info(self):
        return f"{super().info()} | Pescador, red: {self.tipo_red}"

class YatePrivado(Embarcacion):
    def __init__(self, nombre, eslora, capacidad, dueno):
        super().__init__(nombre, eslora, capacidad)
        self.dueno = dueno
    
    def info(self):
        return f"{super().info()} | Yate de {self.dueno}"

print("=== EMBARCACIONES DE ANCÓN ===\n")
don_eulogio = BarcoPesquero("Don Eulogio", 8, 4, "enmalle")
costa_azul = YatePrivado("Costa Azul", 25, 12, "Miguel Ángel Soto")

print(don_eulogio.info())
print(costa_azul.info())
print(don_eulogio.zarpar())
print(don_eulogio.pescar())
```

### Polimorfismo: Mismo mensaje, diferente respuesta

```python
print("\n=== POLIMORFISMO: TODOS ZARPAN ===\n")
barcos = [
    BarcoPesquero("Mares del Sur", 12, 6, "arrastre"),
    YatePrivado("Costa Azul", 25, 12, "Soto"),
    BarcoPesquero("Ancón I", 7, 3, "cerco"),
]
for barco in barcos:
    print(barco.info())
    print(f"  → {barco.zarpar()}")
```

### Herencia múltiple

```python
class Capitan:
    def __init__(self, nombre, licencia):
        self.nombre_capitan = nombre
        self.licencia = licencia
    def dirigir(self):
        return f"Capitán {self.nombre_capitan} dirigiendo"

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
```

### Encapsulación: Secretos del mar

```python
class ProyectoSecreto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self._presupuesto = presupuesto
        self.__clave_acceso = "SOLO_INVESTIGACION"
    
    def obtener_presupuesto(self, nivel_acceso):
        if nivel_acceso >= 5:
            return f"Presupuesto: ${self._presupuesto:,}"
        return "🔒 Acceso denegado"

p = ProyectoSecreto("LOCUENTO", 2500000)
print(f"\nNombre: {p.nombre}")
print(p.obtener_presupuesto(3))
print(p.obtener_presupuesto(5))
```

## Enigmas

### Enigma 12.1: Jerarquía de playas

Crea: `ZonaCostera` → `PlayaPublica` → `PlayaPrivada`. Cada una agrega un atributo.

### Enigma 12.2: Polimorfismo con sonidos

Crea `SonidoMarino`, `Ola` hereda con `sonido()` → "¡Swish!", `Barco` → "¡Buuu!".

### Enigma 12.3: Encapsulación bancaria

Clase `CuentaMaritima` con `__saldo` privado. Métodos `depositar()` y `retirar()`.

---

## Lo que aprendiste

- **Herencia**: `class Hijo(Padre):`
- `super().__init__()` llama al constructor padre
- **Polimorfismo**: mismos métodos, diferentes comportamientos
- **Herencia múltiple**: varias clases padre
- **Encapsulación**: `_` y `__` protegen atributos

Mateo tenía todas las piezas del rompecabezas. Clases, herencia, encapsulación. Pero eran conceptos sueltos. Necesitaba unirlos en un solo programa que analizara las olas, detectara las artificiales, descifrara los mensajes y expusiera a los culpables.

Necesitaba un **proyecto integrador**.

---
