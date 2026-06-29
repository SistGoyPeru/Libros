# Capítulo 10: Los Módulos del Puerto

## Conceptos: Módulos, paquetes, `import`, `__name__`

---

Mateo había logrado acceder al repositorio de código del proyecto LOCUENTO. No era un solo archivo: era un **paquete** completo de Python, con múltiples módulos.

```
locuento/
├── __init__.py
├── generador.py        # Control del generador de olas
├── comunicaciones.py   # Transmisión de mensajes
├── monitoreo.py        # Lectura de sensores
├── config.py           # Configuración del sistema
└── secreto.py          # ¿Módulo oculto?
```

—El módulo `secreto.py` no debería estar ahí —dijo Mateo—. No aparece en la documentación oficial.

## Import: Conectando módulos como redes de pesca

```python
# ============================================
# EXPLORANDO LOS MÓDULOS DE LOCUENTO
# ============================================

# Crear módulos simulados

with open("locuento_generador.py", "w", encoding="utf-8") as f:
    f.write('''"""Control del generador de olas."""
def activar(altura, frecuencia):
    return f"Generando ola: {altura}m cada {frecuencia}s"

def desactivar():
    return "Generador detenido"

VERSION = "2.0"
''')

with open("locuento_comunicaciones.py", "w", encoding="utf-8") as f:
    f.write('''"""Transmisión de mensajes por olas."""
def transmitir(mensaje):
    return f"Transmitiendo: {mensaje}"

def codificar(texto):
    return [ord(c) - 64 for c in texto.upper() if c.isalpha()]
''')

with open("locuento_secreto.py", "w", encoding="utf-8") as f:
    f.write('''"""Módulo secreto - Solo personal autorizado."""
__clave = "ANC0N2026"
def revelar_plan():
    return "Plan: Privatizar playas de Ancón mediante olas artificiales"
def verificar_clave(clave):
    return clave == __clave
''')

# Importar y usar
import locuento_generador as gen
import locuento_comunicaciones as com
import locuento_secreto as sec

print("=== MÓDULOS DEL PROYECTO LOCUENTO ===\n")

print(gen.activar(2.4, 8))
print(com.transmitir("PRUEBA"))
print(f"Versión del generador: {gen.VERSION}")
```

### Import selectivo

```python
from locuento_generador import activar, VERSION
print(f"\n{activar(1.8, 12)}")
print(f"Versión: {VERSION}")
```

### El módulo secreto

```python
print("\n=== MÓDULO SECRETO ===")
print(sec.revelar_plan())

clave = input("\nIngresa la clave de acceso: ")
if sec.verificar_clave(clave):
    print("✓ Acceso concedido al módulo secreto")
else:
    print("✗ Acceso denegado")
```

## `if __name__ == "__main__"`: Puerto principal

```python
# --- Crear módulo con ejecución condicional ---
with open("analisis_olas.py", "w", encoding="utf-8") as f:
    f.write('''"""Módulo de análisis de olas."""
def analizar(alturas):
    return {
        "promedio": sum(alturas) / len(alturas) if alturas else 0,
        "maxima": max(alturas) if alturas else 0,
        "total": len(alturas)
    }

def main():
    print("=== ANALIZADOR DE OLAS ===\\n")
    alturas = [float(x) for x in input("Alturas (separadas por coma): ").split(",")]
    resultado = analizar(alturas)
    for k, v in resultado.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
''')

print("\n=== IMPORTANDO COMO MÓDULO ===")
import analisis_olas
resultado = analisis_olas.analizar([1.2, 1.8, 2.4, 1.5])
print(f"Promedio: {resultado['promedio']}")
```

## Enigmas

### Enigma 10.1: Crea un módulo de playas

Crea `playas_peru.py` con funciones `lista_playas()` y `mejor_playa()`. Luego impórtalo.

### Enigma 10.2: if __name__

Agrega a tu módulo un bloque que muestre "Módulo de playas - Modo autónomo" si se ejecuta directamente.

### Enigma 10.3: Import selectivo

Del módulo `locuento_generador`, importa solo `desactivar`. Úsalo.

---

## Lo que aprendiste

- Los **módulos** son archivos `.py` reutilizables
- `import modulo` / `from modulo import funcion`
- `as` crea alias
- `__name__ == "__main__"` para ejecución directa

Mateo ejecutó el módulo secreto. Lo que encontró lo dejó helado: el plan no era solo privatizar Ancón. El proyecto LOCUENTO era una prueba para un sistema mayor que abarcaría toda la Costa Verde.

Pero alguien más estaba involucrado. Alguien que había dejado su firma en el código. Una firma en forma de **clase**.

---
