# Apéndice: Soluciones a los Enigmas

### Capítulo 1

**Enigma 1.1:**
```python
nombre_playa = "Ancón Norte"
temperatura_agua = 19.2
altura_ola = 2.1
es_segura = True
hora_medicion = "07:30"

print(f"=== PARTE DE OLAS ===")
print(f"Playa: {nombre_playa}")
print(f"Temperatura: {temperatura_agua}°C")
print(f"Altura: {altura_ola}m")
print(f"Segura: {es_segura}")
print(f"Hora: {hora_medicion}")
```

**Enigma 1.2:**
```python
alturas = [1.5, 2.0, 1.8, 2.2, 1.9]
promedio = sum(alturas) / len(alturas)
print(f"Promedio de alturas: {promedio:.2f}m")
```

**Enigma 1.3:**
```python
ola_binaria = "1.8:0.5:2.1"
partes = ola_binaria.split(":")
print(f"Altura: {partes[0]}m")
print(f"Frecuencia: {partes[1]}s")
print(f"Velocidad: {partes[2]}m/s")
```

### Capítulo 2

**Enigma 2.1:**
```python
frecuencia = "03-15-12-01-19"
numeros = frecuencia.split("-")
palabra = ""
for num in numeros:
    letra = chr(int(num) + 64)
    palabra += letra
    print(f"{num} → '{letra}'")
print(f"\nPalabra: {palabra}")  # COLAS
```

**Enigma 2.2:**
```python
texto = "B/T-MARES-DE-ANCÓN-2026"
pos = texto.find("ANCÓN")
extraido = texto[pos:pos+5]
print(extraido)  # ANCÓN
```

**Enigma 2.3:**
```python
mensaje = "ODATNEMIRP SE ODAGUA"
inverso = mensaje[::-1]
print(inverso)  # "AGUA DE PRIMERMUNDO"... ¡"AGUA DE PRIMER MUNDO"!
```

**Enigma 2.4:**
```python
sensor = "  OLA: 2.4m - FREC: 12s  "
limpio = sensor.strip()
sin_etiquetas = limpio.replace("OLA: ", "").replace("- FREC: ", "")
valores = sin_etiquetas.split()
altura = valores[0].replace("m", "")
frecuencia = valores[1].replace("s", "")
print(f"Altura: {altura}m")
print(f"Frecuencia: {frecuencia}s")
```

### Capítulo 3

**Enigma 3.1:**
```python
playas_de_lima = ["Ancón", "Miraflores", "Barranco", "La Punta", "Costa Verde"]
playas_de_lima.append("Santa María")
playas_de_lima.sort()
print(f"Total: {len(playas_de_lima)}")
print(f"Primera: {playas_de_lima[0]}")
print(f"Última: {playas_de_lima[-1]}")
```

**Enigma 3.2:**
```python
accesos = [
    ["Ancón", True, True, "Estacionamiento"],
    ["Miraflores", True, False, "Parque"],
    ["Barranco", True, True, "Escaleras"],
]
print("Playas con acceso para discapacitados:")
for playa in accesos:
    if playa[2]:
        print(f"  {playa[0]}")
```

**Enigma 3.3:**
```python
coordenadas = [
    (-11.7739, -77.1529),
    (-11.7758, -77.1897),
    (-12.1200, -77.0300),
]
for lat, lon in coordenadas:
    print(f"Playa en latitud {lat}, longitud {lon}")
```

### Capítulo 4

**Enigma 4.1:**
```python
mi_playa = {
    "nombre": "Ancón",
    "ubicacion": "Lima, Perú",
    "temperatura_agua": 18.5,
    "tiene_estacionamiento": True,
    "ola_favorita": "La Derecha del Muelle"
}
for clave, valor in mi_playa.items():
    print(f"{clave}: {valor}")
```

**Enigma 4.2:**
```python
implicados = {
    "Carlos Parra": {"nivel_sospecha": 8, "evidencias": ["Diseñó el generador", "Recibió transferencia"]},
    "Miguel Soto": {"nivel_sospecha": 9, "evidencias": ["Financia proyecto"]},
    "Luisa Rivas": {"nivel_sospecha": 3, "evidencias": ["Denunció ruido"]},
}
print("Nombres:", list(implicados.keys()))
print("\nSospecha > 5:")
for n, d in implicados.items():
    if d["nivel_sospecha"] > 5:
        print(f"  {n}: {d['nivel_sospecha']}/10")
print(f"\nEvidencias de Carlos Parra: {implicados['Carlos Parra']['evidencias']}")
```

**Enigma 4.3:**
```python
surfistas = {"Mateo", "Rafa", "Lucía"}
buceadores = {"Rafa", "Pedro", "Lucía"}
kayakistas = {"Mateo", "Pedro", "Sofía"}

print(f"Surf y buceo: {surfistas & buceadores}")
print(f"Solo surf: {surfistas - buceadores - kayakistas}")
print(f"Todos: {surfistas | buceadores | kayakistas}")
```

### Capítulo 5

**Enigma 5.1:**
```python
altura = float(input("Altura de la ola (m): "))
if altura < 1.0:
    print("Ola pequeña")
elif altura <= 2.5:
    print("Ola ideal para surf")
else:
    print("Ola peligrosa")
```

**Enigma 5.2:**
```python
implicados = {
    "Carlos Parra": {"nivel_sospecha": 8, "involucrado": True, "evidencias": ["diseñó generador"]},
    "Miguel Soto": {"nivel_sospecha": 9, "involucrado": True, "evidencias": ["financia"]},
    "Luisa Rivas": {"nivel_sospecha": 3, "involucrado": False, "evidencias": []},
    "Capitán Paredes": {"nivel_sospecha": 5, "involucrado": False, "evidencias": ["no investigó"]},
}

print("Sospecha >= 7:")
for n, d in implicados.items():
    if d["nivel_sospecha"] >= 7:
        print(f"  {n}")

print("\nInvolucrados Y con evidencias:")
for n, d in implicados.items():
    if d["involucrado"] and d["evidencias"]:
        print(f"  {n}")

print("\nNo involucrados PERO sospecha > 4:")
for n, d in implicados.items():
    if not d["involucrado"] and d["nivel_sospecha"] > 4:
        print(f"  {n}")
```

**Enigma 5.3:**
```python
temp = float(input("Temperatura del agua (°C): "))
if temp < 16:
    print("Agua muy fría, usa traje de neopreno")
elif 16 <= temp <= 20:
    print("Agua templada, buenas condiciones")
else:
    print("Agua cálida, ideal para todo el día")
```

### Capítulo 6

**Enigma 6.1:**
```python
playas = ["Ancón", "Miraflores", "Barranco", "Costa Verde"]
for i, playa in enumerate(playas, 1):
    print(f"{i}. {playa}")
```

**Enigma 6.2:**
```python
distancia = 0
while distancia < 100:
    distancia += 10
    print(f"  Avanzando... {distancia}m")
print("¡GENERADOR ENCONTRADO!")
```

**Enigma 6.3:**
```python
temperaturas = [18.2, 19.0, -5, 18.5, 500, 19.1]
for t in temperaturas:
    if t < 0 or t > 50:
        continue
    print(f"Temperatura válida: {t}°C")
```

**Enigma 6.4:**
```python
for i in range(1, 5):
    print("*" * i)
```

### Capítulo 7

**Enigma 7.1:**
```python
def recomendar_traje(temp):
    if temp < 16:
        return "Traje de neopreno 5/4mm"
    elif temp <= 20:
        return "Traje corto"
    else:
        return "Solo shorts"

print(recomendar_traje(15))
print(recomendar_traje(18))
print(recomendar_traje(22))
```

**Enigma 7.2:**
```python
def distancia_buceo(minutos, ritmo=10):
    return minutos * ritmo

print(f"Distancia: {distancia_buceo(30)}m")  # 300m
print(f"Distancia: {distancia_buceo(30, 15)}m")  # 450m
```

**Enigma 7.3:**
```python
def alerta_ola(altura=1.5, peligro=False):
    if peligro:
        print(f"⚠ ¡PELIGRO! Ola de {altura}m detectada")
    else:
        print(f"Ola de {altura}m - condiciones normales")

alerta_ola()
alerta_ola(2.8, True)
```

**Enigma 7.4:**
```python
def info_playa(nombre, tiene_muelle, tiene_estacionamiento):
    puntuacion = sum([tiene_muelle, tiene_estacionamiento])
    rec = "Excelente" if puntuacion == 2 else "Regular" if puntuacion == 1 else "Básica"
    return puntuacion, rec

puntos, rec = info_playa("Ancón", True, True)
print(f"Puntuación: {puntos}/2 - {rec}")
```

### Capítulo 8

**Enigma 8.1:**
```python
with open("mi_diario_mar.txt", "w", encoding="utf-8") as f:
    f.write("Fecha: 27-06-2026\n")
    f.write("Hoy aprendí a leer y escribir archivos en Python.\n")
    f.write("El mar de Ancón guarda secretos en sus olas.\n")

with open("mi_diario_mar.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

**Enigma 8.2:**
```python
with open("temperaturas_mar.txt", "w", encoding="utf-8") as f:
    f.write("18.5\n19.0\n17.8\n18.2\n19.5\n")

with open("temperaturas_mar.txt", "r", encoding="utf-8") as f:
    temps = [float(linea.strip()) for linea in f]

promedio = sum(temps) / len(temps)
print(f"Temperaturas: {temps}")
print(f"Promedio: {promedio:.2f}°C")
```

**Enigma 8.3:**
```python
with open("mi_diario_mar.txt", "w", encoding="utf-8") as f:
    f.write("Observaciones del mar:\n")

observacion = "Vi un delfín saltando en la bahía"
with open("mi_diario_mar.txt", "a", encoding="utf-8") as f:
    f.write(f"- {observacion}\n")

with open("mi_diario_mar.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

**Enigma 8.4:**
```python
contenido = """BITÁCORA DEL PUERTO DE ANCÓN
FECHA: 27-06-2026
ACTIVIDADES SOSPECHOSAS:
- Ruido sospechoso en sector norte
- Luces sospechosas en zona de boyas
- Embarcación no identificada
NOTA: Situación normal
"""

with open("bitacora_simple.txt", "w", encoding="utf-8") as f:
    f.write(contenido)

with open("bitacora_simple.txt", "r", encoding="utf-8") as f:
    texto = f.read()

conteo = texto.lower().count("sospechosa")
print(f"La palabra 'sospechosa' aparece {conteo} veces")
```

### Capítulo 9

**Enigma 9.1:**
```python
def conectar(ip, puerto):
    try:
        print(f"Conectando a {ip}:{puerto}...")
        if ip.startswith("192."):
            raise ConnectionError("Red local no disponible")
        print("  Conexión exitosa")
        return True
    except ConnectionError:
        print("  No se pudo conectar al generador")
        return False

conectar("192.168.1.1", 8080)
conectar("10.0.0.1", 8080)
```

**Enigma 9.2:**
```python
archivo = input("Nombre del archivo: ")
try:
    with open(archivo, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Archivo '{archivo}' no encontrado. Creando uno nuevo...")
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("Datos marinos por defecto\n")
```

**Enigma 9.3:**
```python
class OlaNoDetectadaError(Exception):
    pass

def detectar_ola(altura):
    if altura == 0:
        raise OlaNoDetectadaError("No se detectó ninguna ola")
    return f"Ola detectada: {altura}m"

print(detectar_ola(1.8))
try:
    detectar_ola(0)
except OlaNoDetectadaError as e:
    print(f"Error: {e}")
```

**Enigma 9.4:**
```python
def conectar_generador():
    try:
        print("Conectando al generador submarino...")
        raise TimeoutError("Sin respuesta")
    except TimeoutError:
        print("  Error: tiempo de espera agotado")
    finally:
        print("  Cerrando conexión con el generador submarino")

conectar_generador()
```

### Capítulo 10

**Enigma 10.1:**
```python
# playas_peru.py
def lista_playas():
    return ["Ancón", "Tuquillo", "Hermosa", "Señoritas", "Grande"]

def mejor_playa():
    return "Ancón"

# Desde otro archivo: import playas_peru
# print(playas_peru.lista_playas())
```

**Enigma 10.2:**
```python
if __name__ == "__main__":
    print("Módulo de playas - Modo autónomo")
```

**Enigma 10.3:**
```python
from locuento_generador import desactivar
print(desactivar())
```

### Capítulo 11

**Enigma 11.1:**
```python
class TablaDeSurf:
    def __init__(self, marca, longitud, material):
        self.marca = marca
        self.longitud = longitud
        self.material = material

    def remar(self):
        print(f"Remando en {self.marca}")

t = TablaDeSurf("Channel Islands", 6.2, "epoxi")
t.remar()
```

**Enigma 11.2:**
```python
class Ola:
    total_olas = 0
    def __init__(self, altura, frecuencia, direccion):
        self.altura = altura
        self.frecuencia = frecuencia
        self.direccion = direccion
        Ola.total_olas += 1

o1 = Ola(1.5, 10, "SO")
o2 = Ola(2.4, 15, "O")
print(f"Total olas creadas: {Ola.total_olas}")
```

**Enigma 11.3:**
```python
class Playa:
    def __init__(self, nombre, ubicacion, tiene_muelle):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tiene_muelle = tiene_muelle

    def info(self):
        m = "con muelle" if self.tiene_muelle else "sin muelle"
        return f"{self.nombre} ({self.ubicacion}) - {m}"

p1 = Playa("Ancón", "Lima", True)
p2 = Playa("Hermosa", "Lima", False)
p3 = Playa("Tuquillo", "Ancash", False)
print(p1.info())
print(p2.info())
print(p3.info())
```

### Capítulo 12

**Enigma 12.1:**
```python
class ZonaCostera:
    def __init__(self, nombre):
        self.nombre = nombre

class PlayaPublica(ZonaCostera):
    def __init__(self, nombre, tiene_acceso_libre):
        super().__init__(nombre)
        self.tiene_acceso_libre = tiene_acceso_libre

class PlayaPrivada(ZonaCostera):
    def __init__(self, nombre, dueno):
        super().__init__(nombre)
        self.dueno = dueno

pub = PlayaPublica("Ancón", True)
priv = PlayaPrivada("Costa Azul", "Soto")
print(f"Pública: {pub.nombre}, acceso libre: {pub.tiene_acceso_libre}")
print(f"Privada: {priv.nombre}, dueño: {priv.dueno}")
```

**Enigma 12.2:**
```python
class SonidoMarino:
    def sonido(self):
        return "..."

class Ola(SonidoMarino):
    def sonido(self):
        return "Swish!"

class Barco(SonidoMarino):
    def sonido(self):
        return "Buuu!"

for s in [Ola(), Barco()]:
    print(s.sonido())
```

**Enigma 12.3:**
```python
class CuentaMaritima:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Depósito: +${monto}. Saldo: ${self.__saldo}")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro: -${monto}. Saldo: ${self.__saldo}")
            return True
        print("Saldo insuficiente")
        return False

c = CuentaMaritima("Eulogio", 500)
c.depositar(200)
c.retirar(100)
c.retirar(700)
```

### Capítulo 13

**Enigma 13.1:**
```python
def generar_reporte(olas, archivo="reporte_olas.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("=== REPORTE DE OLAS ===\n")
        f.write(f"Total: {len(olas)}\n")
        f.write(f"Surfeables: {len([o for o in olas if o.es_surfeable()])}\n")
        f.write(f"Artificiales: {len([o for o in olas if o.es_artificial()])}\n")
    print(f"Reporte generado: {archivo}")
```

**Enigma 13.2:**
```python
class OlaTormenta(Ola):
    def __init__(self, altura, frecuencia, direccion, intensidad):
        super().__init__(altura, frecuencia, direccion)
        self.intensidad = intensidad

    def info(self):
        return f"TORMENTA: {self.altura}m, intensidad {self.intensidad}"
```

**Enigma 13.3:**
```python
def mapa_calor(olas):
    horas = {}
    for o in olas:
        h = o.timestamp[11:13]
        horas[h] = horas.get(h, 0) + 1
    for h in sorted(horas):
        print(f"{h}: {'*' * horas[h]}")
```


**Nota:** Estas soluciones son una guía. No hay una única forma correcta de resolver los enigmas. Si tu solución funciona y tiene sentido, ¡es válida!
