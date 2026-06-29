"""Capitulo 15: Epilogo - Ola Libre
Conceptos: Reflexion final - Python como herramienta de cambio
"""

from datetime import datetime
import json

class MonitorOlas:
    """Sistema de monitoreo comunitario de Ancon."""

    def __init__(self, archivo="monitoreo_ancon.json"):
        self.archivo = archivo
        self.lecturas = []
        self.cargar_historial()

    def cargar_historial(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.lecturas = [json.loads(l) for l in f if l.strip()]
            print(f"Folder Historial cargado: {len(self.lecturas)} registros")
        except FileNotFoundError:
            print("Folder Nuevo archivo de monitoreo")

    def registrar_ola(self, altura, frecuencia, direccion):
        lectura = {
            "fecha": datetime.now().isoformat(),
            "altura": altura,
            "frecuencia": frecuencia,
            "direccion": direccion,
            "natural": not self._es_sospechosa(frecuencia)
        }
        self.lecturas.append(lectura)
        with open(self.archivo, "a", encoding="utf-8") as f:
            json.dump(lectura, f)
            f.write("\n")

        estado = "~ Natural" if lectura["natural"] else "! !Sospechosa!"
        print(f"{estado} | {altura}m | {frecuencia}s | {direccion}")

    def _es_sospechosa(self, frecuencia):
        return frecuencia in (15, 18, 20, 25, 30)

    def reporte(self):
        total = len(self.lecturas)
        sospechosas = [l for l in self.lecturas if not l["natural"]]
        print(f"\n=== REPORTE DE MONITOREO ===")
        print(f"Total registros: {total}")
        print(f"Olas sospechosas: {len(sospechosas)}")
        print(f"Playas protegidas: Ancon, Tuquillo, Hermosa")
        if len(sospechosas) == 0:
            print(f"Estado: OK Libre")
        else:
            print(f"! Alerta")
        return total

# Iniciar monitoreo del dia
monitor = MonitorOlas()

print("\n=== LECTURA MATINAL DE OLAS ===")
print("Ancon, 06:00 AM\n")

monitor.registrar_ola(1.5, 10, "SO")
monitor.registrar_ola(0.8, 12, "O")
monitor.registrar_ola(2.0, 8, "NO")
monitor.registrar_ola(1.2, 20, "SO")  # Frecuencia sospechosa!

print(f"\nTotal olas hoy: {len(monitor.lecturas)}")

# Proyecto Final (Opcional) - Esqueleto
print("\n=== ESQUELETO DEL PROYECTO FINAL ===")

class SistemaMonitoreoOlas:
    def __init__(self):
        self.olas = []
        self.playas = []

    def agregar_ola(self, ola):
        pass  # Implementa

    def analizar_patrones(self):
        pass  # Implementa

    def generar_reporte(self):
        pass  # Implementa

    def main(self):
        pass  # Implementa

if __name__ == "__main__":
    sistema = SistemaMonitoreoOlas()
    sistema.main()
