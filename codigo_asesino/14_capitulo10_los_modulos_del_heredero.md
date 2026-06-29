# Capítulo 10: Los Módulos del Heredero

## Conceptos: Módulos, paquetes, `import`, `__name__`, `if __name__ == "__main__"`

---

Eran las 3:00 a.m. cuando Wayra encontró el acceso al módulo `circulo_del_sol.py`. Pero no podía abrirlo directamente. El archivo estaba protegido por un sistema de autenticación que requería una clave.

—No necesito la clave —dijo Wayra—. Necesito entender cómo Inti estructuró Yachay. Porque si entiendo la estructura, puedo encontrar el acceso sin la clave.

En Python, la forma de organizar código en archivos separados es mediante **módulos** y **paquetes**. Yachay no era un solo archivo: era un conjunto de módulos que trabajaban juntos.

## Import: Tejiendo los hilos del conocimiento

Cuando usas `import` en Python, estás trayendo código de otro archivo al actual. Como tomar una cuerda de quipu de un estante y agregarla a tu tejido:

```python
# ============================================
# EXPLORANDO LOS MÓDULOS DE YACHAY
# ============================================

# Creando los módulos de Yachay (simulados)

# --- módulo: yachay/quipus.py ---
contenido_quipus = '''
"""Módulo para la lectura y procesamiento de quipus digitales."""

def leer_quipu(ruta):
    """Lee un quipu digital desde un archivo."""
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def contar_nudos(quipu):
    """Cuenta los nudos en un quipu."""
    if ":" in quipu:
        partes = quipu.split(":")
        # Los nudos son los números después del color
        nudos = [p for p in partes[1:] if p.isdigit()]
        return len(nudos)
    return 0

def colores_del_quipu(quipu):
    """Extrae los colores de un quipu."""
    if ":" in quipu:
        return quipu.split(":")[0]
    return "desconocido"

VERSION = "1.0"
AUTOR = "Inti Quispe"
'''

# Guardar como módulo simulado
with open("yachay_quipus.py", "w", encoding="utf-8") as f:
    f.write(contenido_quipus)

# --- AHORA IMPORTAMOS Y USAMOS EL MÓDULO ---

print("=== IMPORTANDO MÓDULOS DE YACHAY ===\n")

# Importar el módulo completo
import yachay_quipus

# Usar funciones del módulo
quipu_ejemplo = "ROJO:1:4:9"
nudos = yachay_quipus.contar_nudos(quipu_ejemplo)
color = yachay_quipus.colores_del_quipu(quipu_ejemplo)

print(f"Quipu: {quipu_ejemplo}")
print(f"Nudos encontrados: {nudos}")
print(f"Color: {color}")
print(f"Versión del módulo: {yachay_quipus.VERSION}")
```

### Import selectivo

No siempre necesitas todo un módulo. A veces solo necesitas una función:

```python
# Importar solo funciones específicas
from yachay_quipus import contar_nudos, colores_del_quipu

print("\n=== IMPORT SELECTIVO ===\n")
print(f"Nudos: {contar_nudos('VERDE:2:5:10')}")
print(f"Color: {colores_del_quipo('VERDE:2:5:10')}")
```

### Import con alias

Los nombres largos pueden acortarse:

```python
# Import con alias
import yachay_quipus as yq

print("\n=== IMPORT CON ALIAS ===\n")
print(f"Nudos: {yq.contar_nudos('AZUL:1:5:9')}")
```

## El módulo `circulo_del_sol`

Wayra encontró que el módulo `circulo_del_sol` estaba en un archivo separado pero era importado por Yachay:

```python
# --- Creando el módulo circulo_del_sol ---

contenido_circulo = '''
"""Módulo del Círculo del Sol - Acceso restringido."""

__clave_acceso = "YACHAY_SUN_CIRCLE_2026"

def verificar_acceso(usuario, clave):
    """Verifica si un usuario tiene acceso al Círculo del Sol."""
    if clave == __clave_acceso:
        return True
    return False

def obtener_miembros():
    """Devuelve la lista de miembros del Círculo del Sol."""
    return ["Inti Quispe", "Mama Killa", "Wayra Condori (potencial)"]

class Mision:
    """Representa una misión del Círculo del Sol."""
    def __init__(self, nombre, objetivo):
        self.nombre = nombre
        self.objetivo = objetivo
        self.completada = False
'''

with open("yachay_circulo.py", "w", encoding="utf-8") as f:
    f.write(contenido_circulo)

# --- INTENTANDO ACCEDER ---

import yachay_circulo as circulo

print("\n=== ACCEDIENDO AL CÍRCULO DEL SOL ===\n")

# Intentar verificar acceso con clave incorrecta
acceso = circulo.verificar_acceso("Wayra", "clave_incorrecta")
print(f"Acceso con clave incorrecta: {acceso}")

# Acceder a los miembros (no requiere clave)
miembros = circulo.obtener_miembros()
print(f"Miembros del Círculo: {miembros}")

# Pero la clave privada no es accesible directamente
try:
    print(circulo.__clave_acceso)  # Esto fallará
except AttributeError as e:
    print(f"No puedo acceder a la clave privada: {e}")

# Nota: En Python, los atributos que empiezan con __ tienen
# name mangling y no son directamente accesibles desde fuera
```

## `if __name__ == "__main__"`: El hilo principal

Cada módulo en Python tiene una variable especial `__name__`. Cuando ejecutas un archivo directamente, `__name__` vale `"__main__"`. Cuando lo importas, `__name__` vale el nombre del módulo.

```python
# --- Creando un módulo con ejecución condicional ---

contenido_analisis = '''
"""Módulo de análisis forense digital."""

import sys

def analizar_quipu(quipu):
    """Analiza un quipu y devuelve estadísticas."""
    partes = quipu.split(":")
    tipo = partes[0]
    nudos = [int(p) for p in partes[1:]]
    
    return {
        "tipo": tipo,
        "total_nudos": len(nudos),
        "suma": sum(nudos),
        "promedio": sum(nudos) / len(nudos) if nudos else 0,
        "maximo": max(nudos) if nudos else 0,
        "minimo": min(nudos) if nudos else 0
    }

def main():
    """Función principal para ejecución directa."""
    print("=== ANALIZADOR DE QUIPUS - MODO AUTÓNOMO ===\\n")
    
    if len(sys.argv) > 1:
        quipu = sys.argv[1]
        resultado = analizar_quipu(quipu)
        for clave, valor in resultado.items():
            print(f"  {clave}: {valor}")
    else:
        print("Uso: python analisis.py COLOR:num1:num2:num3")

if __name__ == "__main__":
    main()
'''

with open("analisis_forense.py", "w", encoding="utf-8") as f:
    f.write(contenido_analisis)

# --- IMPORTANDO COMO MÓDULO (ejecución normal) ---
print("\n=== IMPORTANDO analisis_forense (__name__ != '__main__') ===\n")

import analisis_forense as af

# Usar funciones sin ejecutar main()
resultado = af.analizar_quipu("BLANCO:1:3:5:7:9")
print("Usando el módulo importado:")
for clave, valor in resultado.items():
    print(f"  {clave}: {valor}")
```

## Paquetes: El gran quipu de Yachay

Los **paquetes** son carpetas que contienen múltiples módulos. Yachay era un paquete:

```python
# --- ESTRUCTURA DE UN PAQUETE ---

# Simulamos la estructura de directorios de Yachay
import os

# Crear la estructura del paquete yachay
os.makedirs("yachay_paquete", exist_ok=True)

# __init__.py es lo que convierte una carpeta en un paquete
with open("yachay_paquete/__init__.py", "w") as f:
    f.write('''"""Yachay - Inteligencia Artificial Ancestral."""
__version__ = "2.0.0"
print("Inicializando Yachay...")
''')

with open("yachay_paquete/core.py", "w") as f:
    f.write('''"""Núcleo de Yachay."""
def iniciar():
    return "Yachay iniciado correctamente"
''')

with open("yachay_paquete/quipus.py", "w") as f:
    f.write('''"""Módulo de procesamiento de quipus."""
def descifrar(quipu):
    return f"Descifrando: {quipu}"
''')

# --- AHORA USAMOS EL PAQUETE ---
print("\n=== USANDO EL PAQUETE YACHAY ===\n")

# Importar módulos del paquete
from yachay_paquete import core
from yachay_paquete import quipus

print(core.iniciar())
print(quipus.descifrar("ROJO:1:4:9"))
```

## Descubriendo los Herederos de Pizarro

Mientras exploraba los módulos, Wayra encontró uno que no esperaba:

```python
# --- Módulo oculto: los_herederos.py ---

contenido_herederos = '''
"""Los Herederos de Pizarro - Módulo de acceso corporativo."""

MIEMBROS_CONOCIDOS = [
    "Rodrigo Mamani (Líder)",
    "Inversor Anónimo #1",
    "Inversor Anónimo #2",
    "Contacto en NeuralCorp Andina"
]

OBJETIVOS = [
    "Adquirir los derechos de Yachay",
    "Controlar el conocimiento ancestral digital",
    "Monetizar los quipus digitales"
]

def verificar_miembro(nombre):
    """Verifica si un nombre está en la lista de miembros."""
    return any(nombre in m for m in MIEMBROS_CONOCIDOS)

def objetivos_organizacion():
    """Devuelve los objetivos de la organización."""
    return OBJETIVOS
'''

with open("herederos_pizarro.py", "w", encoding="utf-8") as f:
    f.write(contenido_herederos)

print("\n=== INVESTIGACIÓN: LOS HEREDEROS DE PIZARRO ===\n")

import herederos_pizarro as hp

print("Miembros conocidos:")
for m in hp.MIEMBROS_CONOCIDOS:
    print(f"  • {m}")

print("\nObjetivos:")
for o in hp.OBJETIVOS:
    print(f"  • {o}")

# Verificar si Rodrigo Mamani es miembro
es_miembro = hp.verificar_miembro("Rodrigo Mamani")
print(f"\n¿Rodrigo Mamani es miembro de Los Herederos? {es_miembro}")

# ¿Lara está en la lista?
lara_en_herederos = hp.verificar_miembro("Lara")
print(f"¿Lara Mamani es miembro? {lara_en_herederos}")
```

—Rodrigo Mamani —dijo Wayra—. Es el líder de "Los Herederos de Pizarro". Y es el padre secreto de Lara. Si Lara está trabajando para su padre... entonces todo lo que hemos visto hasta ahora podría ser una puesta en escena.

—¿Lara estaría infiltrada? —preguntó Raúl.

—No lo sé. Pero el módulo de los Herederos no menciona a Lara. Y eso es sospechoso.

## Enigmas

### Enigma 10.1: Crea tu propio módulo

Crea un archivo llamado `mis_herramientas.py` que contenga:
- Una función `saludar_investigador(nombre)` que salude
- Una constante `VERSION = "1.0"`
- Una variable `casos_resueltos = 0`

Luego, desde otro script, importa el módulo y úsalo.

### Enigma 10.2: __name__ == "__main__"

Agrega a `mis_herramientas.py` un bloque `if __name__ == "__main__":` que muestre "Módulo de herramientas forenses - Modo autónomo" cuando se ejecute directamente.

### Enigma 10.3: Import selectivo

Del módulo `analisis_forense.py`, importa solo la función `analizar_quipu` con un alias `aq`. Úsala para analizar el quipu "YACHAY:1:2:3:4:5".

### Enigma 10.4: Busca en el paquete

Crea un paquete llamado `investigacion/` con los módulos:
- `evidencias.py` (función: `agregar_evidencia`)
- `sospechosos.py` (función: `listar_sospechosos`)
- `__init__.py` (que importe ambos)

Luego úsalos desde otro archivo.

---

## Lo que aprendiste

- Los **módulos** son archivos `.py` que contienen funciones y variables reutilizables
- `import modulo` importa todo el módulo
- `from modulo import funcion` importa solo lo necesario
- `as` permite crear alias (`import modulo as m`)
- `__name__` vale `"__main__"` cuando se ejecuta directamente
- `if __name__ == "__main__":` permite que un archivo sea módulo y script a la vez
- Los **paquetes** son carpetas con `__init__.py` que contienen módulos
- Python "oculta" atributos que empiezan con `__` (name mangling)

El descubrimiento del módulo de Los Herederos de Pizarro cambió todo. Rodrigo Mamani no solo era un empresario ambicioso: era el líder de una organización que quería controlar Yachay. Y si su hija Lara estaba trabajando con él...

—Wayra —dijo Raúl—. Si Rodrigo está detrás de esto, y Lara es su hija... ¿ella sabe que su padre es el líder de Los Herederos?

—Esa es la pregunta. Y la respuesta está en cómo Inti modeló a las personas en su código. Porque Inti no solo programaba algoritmos: programaba la realidad. Usaba **clases** para representar a las personas, sus relaciones, sus secretos.

Wayra abrió el archivo `yachay_core.py` que había encontrado antes. Dentro, vio algo que le heló la sangre:

```python
class Persona:
    def __init__(self, nombre, rol, secreto=None):
        self.nombre = nombre
        self.rol = rol
        self.secreto = secreto  # Todos tienen secretos
```

—Inti modeló a todos en Yachay —dijo—. Incluido al asesino. Y si encuentro la instancia correcta de la clase Persona... encontraré el nombre del culpable.

—¿Y cómo encuentras esa instancia?

—Aprendiendo **Programación Orientada a Objetos**. Porque Yachay no es solo un programa: es un mundo modelado en objetos.

---
