"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 10 - Los Módulos del Heredero
Conceptos: Módulos, paquetes, import, __name__, if __name__ == "__main__"
Autor: Alex Goyzueta Delgado

NOTA: Este archivo DEMUESTRA los conceptos de módulos. 
Para una experiencia completa, ejecute también los archivos:
  - yachay_quipus.py
  - analisis_forense.py
  - herederos_pizarro.py
creados por este script.
"""

import os
import sys

# ============================================
# CREANDO MÓDULOS DINÁMICAMENTE
# ============================================

# Crear módulo: yachay_quipus.py
with open("yachay_quipus.py", "w", encoding="utf-8") as f:
    f.write('''"""Módulo para la lectura y procesamiento de quipus digitales."""

def leer_quipu(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def contar_nudos(quipu):
    if ":" in quipu:
        partes = quipu.split(":")
        nudos = [p for p in partes[1:] if p.isdigit()]
        return len(nudos)
    return 0

def colores_del_quipu(quipu):
    if ":" in quipu:
        return quipu.split(":")[0]
    return "desconocido"

VERSION = "1.0"
AUTOR = "Inti Quispe"
''')

# Crear módulo: yachay_circulo.py
with open("yachay_circulo.py", "w", encoding="utf-8") as f:
    f.write('''"""Módulo del Círculo del Sol - Acceso restringido."""
__clave_acceso = "YACHAY_SUN_CIRCLE_2026"

def verificar_acceso(usuario, clave):
    return clave == __clave_acceso

def obtener_miembros():
    return ["Inti Quispe", "Mama Killa", "Wayra Condori (potencial)"]

class Mision:
    def __init__(self, nombre, objetivo):
        self.nombre = nombre
        self.objetivo = objetivo
        self.completada = False
''')

# Crear módulo: herederos_pizarro.py
with open("herederos_pizarro.py", "w", encoding="utf-8") as f:
    f.write('''"""Los Herederos de Pizarro - Módulo de acceso corporativo."""
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
    return any(nombre in m for m in MIEMBROS_CONOCIDOS)

def objetivos_organizacion():
    return OBJETIVOS
''')

# --- AHORA IMPORTAMOS Y USAMOS LOS MÓDULOS ---
print("=== IMPORTANDO MÓDULOS DE YACHAY ===\n")

import yachay_quipus
quipu_ejemplo = "ROJO:1:4:9"
nudos = yachay_quipus.contar_nudos(quipu_ejemplo)
color = yachay_quipus.colores_del_quipu(quipu_ejemplo)
print(f"Quipu: {quipu_ejemplo}")
print(f"Nudos encontrados: {nudos}")
print(f"Color: {color}")
print(f"Versión del módulo: {yachay_quipus.VERSION}")

# Import selectivo
from yachay_quipus import contar_nudos, colores_del_quipu
print(f"\nNudos: {contar_nudos('VERDE:2:5:10')}")
print(f"Color: {colores_del_quipu('VERDE:2:5:10')}")

# Import con alias
import yachay_quipus as yq
print(f"\nNudos (alias): {yq.contar_nudos('AZUL:1:5:9')}")

# Círculo del Sol
import yachay_circulo as circulo
acceso = circulo.verificar_acceso("Wayra", "clave_incorrecta")
print(f"\nAcceso con clave incorrecta: {acceso}")
miembros = circulo.obtener_miembros()
print(f"Miembros del Círculo: {miembros}")

# Herederos de Pizarro
import herederos_pizarro as hp
print("\n=== LOS HEREDEROS DE PIZARRO ===")
print("Miembros conocidos:")
for m in hp.MIEMBROS_CONOCIDOS:
    print(f"  • {m}")
print("\nObjetivos:")
for o in hp.OBJETIVOS:
    print(f"  • {o}")
es_miembro = hp.verificar_miembro("Rodrigo Mamani")
print(f"\n¿Rodrigo Mamani es miembro? {es_miembro}")
