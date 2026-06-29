# Capítulo 15: Epílogo — Ola Libre

## Conceptos: Reflexión final — Python como herramienta de cambio

---

Pasaron tres meses.

Ancón había cambiado. La "Reserva de Olas" era ahora un modelo para otras caletas del Perú. La Municipalidad había instalado sensores —manejados por la comunidad— para monitorear la calidad de las olas y detectar cualquier intento de manipulación.

Mateo abrió su laptop una mañana, frente al mar. El sol salía sobre el puerto. Las olas rompían con un ritmo perfecto.

—Hora de la lectura de olas —dijo.

```python
# ============================================
# EPÍLOGO: OLA LIBRE - MONITOREO COMUNITARIO
# ============================================

from datetime import datetime
import json

class MonitorOlas:
    """Sistema de monitoreo comunitario de Ancón."""
    
    def __init__(self, archivo="monitoreo_ancon.json"):
        self.archivo = archivo
        self.lecturas = []
        self.cargar_historial()
    
    def cargar_historial(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.lecturas = [json.loads(l) for l in f if l.strip()]
            print(f"📂 Historial cargado: {len(self.lecturas)} registros")
        except FileNotFoundError:
            print("📂 Nuevo archivo de monitoreo")
    
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
        
        estado = "🌊 Natural" if lectura["natural"] else "⚠️ ¡Sospechosa!"
        print(f"{estado} | {altura}m | {frecuencia}s | {direccion}")
    
    def _es_sospechosa(self, frecuencia):
        return frecuencia in (15, 18, 20, 25, 30)
    
    def reporte(self):
        total = len(self.lecturas)
        sospechosas = [l for l in self.lecturas if not l["natural"]]
        print(f"\n=== REPORTE DE MONITOREO ===")
        print(f"Total registros: {total}")
        print(f"Olas sospechosas: {len(sospechosas)}")
        print(f"Playas protegidas: Ancón, Tuquillo, Hermosa")
        print(f"Estado: ✅ Libre" if len(sospechosas) == 0 else f"⚠️ Alerta")
        return total

# Iniciar monitoreo del día
monitor = MonitorOlas()

print("\n=== LECTURA MATINAL DE OLAS ===")
print("Ancón, 06:00 AM\n")

monitor.registrar_ola(1.5, 10, "SO")
monitor.registrar_ola(0.8, 12, "O")
monitor.registrar_ola(2.0, 8, "NO")
monitor.registrar_ola(1.2, 20, "SO")  # ¡Frecuencia sospechosa!

print(f"\nTotal olas hoy: {len(monitor.lecturas)}")
```

Mateo sonrió. La última lectura mostraba una frecuencia de 20 —la misma que usaba el generador. Pero esta vez no era el generador. Era el mar, recuperando su ritmo natural. O tal vez... alguien probando los límites del sistema.

—El código de las olas sigue vivo —dijo—. Pero ahora todos pueden leerlo.

Cerró la laptop, agarró su tabla, y corrió hacia el mar. La primera ola lo recibió como un viejo amigo.

---

### Python es tu tabla de surf

En este libro aprendiste que Python no es solo un lenguaje de programación. Es una herramienta para entender el mundo, para resolver misterios, para proteger lo que amas.

Así como una tabla de surf te permite cabalgar las olas, Python te permite cabalgar los datos. Así como el surfista lee el mar, el programador lee el código. Así como una ola puede esconder un mensaje, un programa puede revelar una verdad.

Sigue aprendiendo. Sigue preguntando. Y recuerda:

> **El océano tiene su propio código. Y ahora tú sabes cómo leerlo.**

---

## Proyecto Final (Opcional)

### Construye tu propio sistema de monitoreo

Usando todo lo aprendido, crea un sistema que:

1. **Registre** olas desde un archivo o entrada del usuario
2. **Analice** patrones sospechosos (frecuencias, alturas anómalas)
3. **Descifre** mensajes ocultos en las olas
4. **Almacene** los datos en archivos JSON
5. **Genere** reportes en texto
6. **Use clases** para modelar olas, playas, y monitoreo
7. **Maneje errores** con try/except

```python
# ESQUELETO DEL PROYECTO FINAL
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
```

---

¡Felicitaciones! Has completado **Código de Olas: El Misterio del Puerto de Ancón**.

Ahora eres un programador Python... y un lector del mar.

---

### Código fuente

Si este libro te fue útil y quieres apoyar más proyectos como este, puedes adquirir el código completo en
➡ **[payhip.com/b/cx87Y](https://payhip.com/b/cx87Y)** ⬅

¿Comentarios, sugerencias, o encontraste un error? Escríbeme a:

📧 **alexgoyzueta2018@gmail.com**

---
