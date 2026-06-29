"""Capitulo 13: El Proyecto Integrador
Conceptos: Proyecto completo - Analizador de Olas LOCUENTO
"""

import json
from datetime import datetime

# --- MODULOS ---

class Ola:
    """Representa una ola registrada."""

    total_olas = 0

    def __init__(self, altura, frecuencia, direccion, timestamp=None):
        self.altura = altura
        self.frecuencia = frecuencia
        self.direccion = direccion
        self.timestamp = timestamp or datetime.now().isoformat()
        self._es_artificial = False
        Ola.total_olas += 1

    def es_surfeable(self):
        return 0.8 <= self.altura <= 3.0

    def marcar_artificial(self):
        self._es_artificial = True

    def es_artificial(self):
        return self._es_artificial

    def info(self):
        tipo = "Bot Artificial" if self._es_artificial else "~ Natural"
        return (f"Ola #{Ola.total_olas}: {self.altura}m, "
                f"{self.frecuencia}s, {self.direccion} | {tipo}")

class OlaArtificial(Ola):
    def __init__(self, altura, frecuencia, direccion, mensaje_codificado):
        super().__init__(altura, frecuencia, direccion)
        self.mensaje_codificado = mensaje_codificado
        self.marcar_artificial()

    def descifrar_mensaje(self):
        return ''.join(chr(c + 64) for c in self.mensaje_codificado if 1 <= c <= 26)

# --- FUNCIONES ---

def filtrar_por_altura(olas, min_alt, max_alt):
    return [o for o in olas if min_alt <= o.altura <= max_alt]

def detectar_artificiales(olas):
    """Detecta olas artificiales por patron de frecuencia exacta."""
    paises = {"15", "18", "20", "25", "30"}  # frecuencias non-naturales
    return [o for o in olas if str(o.frecuencia) in paises]

def registrar_ola(archivo, ola):
    with open(archivo, "a", encoding="utf-8") as f:
        json.dump({
            "altura": ola.altura,
            "frecuencia": ola.frecuencia,
            "direccion": ola.direccion,
            "timestamp": ola.timestamp,
            "artificial": ola.es_artificial()
        }, f)
        f.write("\n")

def cargar_registros(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [json.loads(linea) for linea in f if linea.strip()]
    except FileNotFoundError:
        print(f"! Archivo {archivo} no encontrado. Creando nuevo.")
        return []

def main():
    print("=" * 60)
    print("  ANALIZADOR DE OLAS - PROYECTO LOCUENTO")
    print("=" * 60)

    # Datos de ejemplo - registros del puerto
    registros_raw = [
        (1.2, 12, "SO", None), (2.4, 15, "O", [1, 14, 3, 15, 14]),
        (0.8, 8, "NO", None), (1.8, 18, "SO", [16, 18, 9, 22, 1, 20, 15]),
        (2.0, 20, "O", [3, 15, 19, 20, 1, 26, 21, 12]),
        (0.5, 25, "NO", [16, 12, 1, 14]), (1.5, 10, "SO", None),
        (2.2, 30, "O", [15, 12, 1, 19, 4, 5, 3, 15, 4, 9, 6, 9, 3, 1, 4, 15])
    ]

    olas = []
    for alt, freq, dir, msg in registros_raw:
        if msg:
            ola = OlaArtificial(alt, freq, dir, msg)
        else:
            ola = Ola(alt, freq, dir)
        olas.append(ola)

    print(f"\nChart Total olas registradas: {len(olas)}")

    artificiales = [o for o in olas if o.es_artificial()]
    print(f"Bot Olas artificiales detectadas: {len(artificiales)}")

    print("\n=== MENSAJES DESCIFRADOS ===")
    mensaje_completo = []
    for ola in artificiales:
        if ola.mensaje_codificado:
            msg = ola.descifrar_mensaje()
            print(f"  {msg}")
            mensaje_completo.append(msg)

    print(f"\nKey Mensaje completo: {' '.join(mensaje_completo)}")

    print(f"\n~ Olas surfeables: {len([o for o in olas if o.es_surfeable()])}")

    # Persistencia
    archivo = "registros_olas.json"
    for ola in olas:
        registrar_ola(archivo, ola)
    print(f"\nSave Registros guardados en {archivo}")

    print("\n" + "=" * 60)
    print("  INVESTIGACION COMPLETA")
    print("=" * 60)
    print("  El proyecto LOCUENTO usaba olas artificiales")
    print("  para transmitir mensajes cifrados y manipular")
    print("  las condiciones del mar en Ancon.")
    print("=" * 60)

if __name__ == "__main__":
    main()
