# Capítulo 11: La Clase del Surfista

## Conceptos: POO, clases, objetos, atributos, métodos

---

Mateo había descargado todo el código del proyecto LOCUENTO. Pero el código no solo tenía funciones: tenía **clases**. Alguien había modelado el proyecto como un sistema de objetos.

—El mar no es solo datos —dijo—. El mar es un objeto. Una ola es un objeto. Un surfista es un objeto. Todo en el mar puede representarse como una clase.

## Clases: El molde del surfista

Una **clase** es un molde para crear objetos. Como un molde de tabla de surf: defines la forma, y luego creas tablas (objetos) a partir de ella.

```python
# ============================================
# MODELANDO EL OCÉANO CON CLASES
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
        return f"🌊 ¡Ola de {self.altura}m rompiendo!"
    
    def es_surfeable(self):
        return 0.8 <= self.altura <= 3.0
    
    def info(self):
        return f"Ola: {self.altura}m, cada {self.frecuencia}s, dirección {self.direccion}"

ola_1 = Ola(1.8, 12, "SO")
ola_2 = Ola(2.4, 8, "O")
ola_3 = Ola(0.5, 20, "NO")

print("=== OLAS CREADAS ===")
print(ola_1.info())
print(ola_2.info())
print(ola_3.info())

print(f"\n¿Ola 1 surfeable? {ola_1.es_surfeable()}")
print(f"¿Ola 3 surfeable? {ola_3.es_surfeable()}")

print(f"\n{ola_2.romper()}")
```

### La clase Implicado

Mateo modeló a los implicados como objetos:

```python
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
        print(f"  ⚠ Evidencia contra {self.nombre}: {evidencia}")
    
    def interrogar(self):
        self.interrogado = True
        print(f"\n  ▶ INTERROGANDO A {self.nombre.upper()}")
        print(f"    Rol: {self.rol}")
        print(f"    Riesgo: {self.nivel_riesgo}/10")
        print(f"    Evidencias: {len(self.evidencias)}")
        if self.nivel_riesgo >= 7:
            return f"    → {self.nombre} es ALTAMENTE SOSPECHOSO"
        elif self.nivel_riesgo >= 4:
            return f"    → {self.nombre} requiere vigilancia"
        return f"    → {self.nombre} tiene perfil bajo"

carlos = Implicado("Carlos Parra", "Ingeniero Naval", 8)
luisa = Implicado("Luisa Rivas", "Bióloga Marina", 3)
soto = Implicado("Miguel Ángel Soto", "Empresario", 9)

print("\n=== IMPLICADOS CREADOS ===")
carlos.agregar_evidencia("Diseñó el generador")
soto.agregar_evidencia("Financia el proyecto")
soto.agregar_evidencia("Dueño del terreno")
print(carlos.interrogar())
print(soto.interrogar())
```

### Atributos de clase

```python
class Investigacion:
    nombre_caso = "Operación LOCUENTO - Contaminación de Olas"
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

caso = Investigacion("Mateo Sánchez")
caso.agregar_implicado(carlos)
caso.agregar_implicado(soto)
caso.evidencias.append("Firmware del generador")
caso.evidencias.append("Registro de activaciones")
caso.resumen()
```

## Enigmas

### Enigma 11.1: Clase TablaDeSurf

Crea una clase `TablaDeSurf` con: `marca`, `longitud`, `material`. Método `remar()` que muestre "Remando en [marca]".

### Enigma 11.2: Clase con contador

Modifica `Ola` para que cuente cuántas olas se han creado en total.

### Enigma 11.3: Sistema de playas

Crea una clase `Playa` con atributos `nombre`, `ubicacion`, `tiene_muelle`. Método `info()`. Crea 3 playas.

---

## Lo que aprendiste

- Una **clase** define un molde para objetos
- `__init__()` es el constructor
- `self` se refiere al propio objeto
- **Atributos de clase** son compartidos
- Los **métodos** son funciones del objeto

Mateo había modelado a los implicados como objetos. Pero notó que algunos compartían características: Soto y Parra tenían acceso al generador, ambos tenían altos niveles de riesgo. En cambio, Luisa Rivas era un caso distinto.

—Los implicados no son todos iguales —dijo Mateo—. Hay una jerarquía. Algunos heredan características de otros. Como las clases en Python.

Estaba a punto de descubrir la **herencia**.

---
