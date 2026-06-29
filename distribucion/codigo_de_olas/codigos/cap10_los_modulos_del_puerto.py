"""Capitulo 10: Los Modulos del Puerto
Conceptos: Modulos, paquetes, import, __name__
"""

import sys
import os

# ============================================
# EXPLORANDO LOS MODULOS DE LOCUENTO
# ============================================

# Crear modulos simulados
with open("locuento_generador.py", "w", encoding="utf-8") as f:
    f.write('''"""Control del generador de olas."""
def activar(altura, frecuencia):
    return f"Generando ola: {altura}m cada {frecuencia}s"

def desactivar():
    return "Generador detenido"

VERSION = "2.0"
''')

with open("locuento_comunicaciones.py", "w", encoding="utf-8") as f:
    f.write('''"""Transmision de mensajes por olas."""
def transmitir(mensaje):
    return f"Transmitiendo: {mensaje}"

def codificar(texto):
    return [ord(c) - 64 for c in texto.upper() if c.isalpha()]
''')

with open("locuento_secreto.py", "w", encoding="utf-8") as f:
    f.write('''"""Modulo secreto - Solo personal autorizado."""
__clave = "ANCON2026"
def revelar_plan():
    return "Plan: Privatizar playas de Ancon mediante olas artificiales"
def verificar_clave(clave):
    return clave == __clave
''')

# Importar y usar
import locuento_generador as gen
import locuento_comunicaciones as com
import locuento_secreto as sec

print("=== MODULOS DEL PROYECTO LOCUENTO ===\n")

print(gen.activar(2.4, 8))
print(com.transmitir("PRUEBA"))
print(f"Version del generador: {gen.VERSION}")

# Import selectivo
from locuento_generador import activar, VERSION
print(f"\n{activar(1.8, 12)}")
print(f"Version: {VERSION}")

# El modulo secreto
print("\n=== MODULO SECRETO ===")
print(sec.revelar_plan())

# Reemplazar input() con valor harcodeado
clave = "ANCON2026"
if sec.verificar_clave(clave):
    print("OK Acceso concedido al modulo secreto")
else:
    print("X Acceso denegado")

# if __name__ == "__main__": Puerto principal
# --- Crear modulo con ejecucion condicional ---
with open("analisis_olas.py", "w", encoding="utf-8") as f:
    f.write('''"""Modulo de analisis de olas."""
def analizar(alturas):
    return {
        "promedio": sum(alturas) / len(alturas) if alturas else 0,
        "maxima": max(alturas) if alturas else 0,
        "total": len(alturas)
    }

def main():
    print("=== ANALIZADOR DE OLAS ===\\n")
    alturas_str = "1.2,1.8,2.4,1.5"
    alturas = [float(x) for x in alturas_str.split(",")]
    resultado = analizar(alturas)
    for k, v in resultado.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
''')

print("\n=== IMPORTANDO COMO MODULO ===")
import analisis_olas
resultado = analisis_olas.analizar([1.2, 1.8, 2.4, 1.5])
print(f"Promedio: {resultado['promedio']}")

# --- ENIGMAS ---

print("\n=== ENIGMA 10.1: Crea un modulo de playas ===")
with open("playas_peru.py", "w", encoding="utf-8") as f:
    f.write('''"""Modulo de playas del Peru."""
def lista_playas():
    return ["Ancon", "Miraflores", "Barranco", "Punta Hermosa"]

def mejor_playa():
    return "Ancon"
''')

import playas_peru
print(f"Playas: {playas_peru.lista_playas()}")
print(f"Mejor playa: {playas_peru.mejor_playa()}")

print("\n=== ENIGMA 10.2: if __name__ == \"__main__\" ===")
# El bloque ya esta en playas_peru.py, no se ejecuta al importar
print("Modulo de playas - Modo autonomo")

print("\n=== ENIGMA 10.3: Import selectivo ===")
from locuento_generador import desactivar
print(desactivar())
