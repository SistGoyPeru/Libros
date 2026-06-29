# Apéndice: Soluciones a los Enigmas

### Capítulo 1

**Enigma 1.1:**
```python
nombre_sospechoso = "Lara Mamani"
edad_sospechoso = 32
rol_sospechoso = "Asistente de laboratorio"
coartada = "Estaba en mi departamento"
acceso = True

print("=== FICHA DE SOSPECHOSO ===")
print(f"Nombre: {nombre_sospechoso}")
print(f"Edad: {edad_sospechoso}")
print(f"Rol: {rol_sospechoso}")
print(f"Coartada: {coartada}")
print(f"Acceso: {acceso}")
```

**Enigma 1.2:**
```python
quipu_digital_002 = "Yachay:2:4:6:8:10"
elementos = quipu_digital_002.split(":")
tipo = elementos[0]
numeros = elementos[1:]
print(f"Tipo: {tipo}")
print(f"Números: {numeros}")
# Son números pares (respuestas). Yachay: 2,4,6,8,10
```

**Enigma 1.3:**
```python
mi_teoria = "Creo que el asesino conocía a Inti y tenía acceso al laboratorio"
print(f"Mi teoría inicial: {mi_teoria}")
```

### Capítulo 2

**Enigma 2.1:**
```python
mensaje = "ÑAN*QHAPAQ*TAMBO*WAYRA*INTI"
minusculas = mensaje.lower()
reemplazado = mensaje.replace("*", " -> ")
posicion = mensaje.find("WAYRA")
conteo_a = mensaje.count("A")
longitud = len(mensaje)

print(f"Minúsculas: {minusculas}")
print(f"Reemplazado: {reemplazado}")
print(f"Posición de WAYRA: {posicion}")
print(f"Veces que aparece A: {conteo_a}")
print(f"Longitud: {longitud}")
```

**Enigma 2.2:**
```python
mensaje = "ÑAN*QHAPAQ*TAMBO*WAYRA*INTI"
pos = mensaje.find("WAYRA")
nombre = mensaje[pos:pos+5]  # "WAYRA"
print(nombre)
```

**Enigma 2.3:**
```python
quipu_invertido = "ATAM-ATAK-AP"
inverso = quipu_invertido[::-1]
print(inverso)  # "PA-KATA-MATA"
```

### Capítulo 3

**Enigma 3.1:**
```python
coartadas = [
    "Lara: Estaba en mi departamento, viendo series.",
    "Carlos: Trabajaba en mi oficina de la universidad.",
    "Sarah: Tenía una videollamada con el MIT.",
    "Rodrigo: Estaba en una cena de negocios.",
    "Killa: Dormía. A mi edad, no salgo de noche."
]
coartadas.append("Wayra: Estaba durmiendo en mi departamento.")
coartadas.sort()
print(coartadas)
print(f"Total: {len(coartadas)}")
print(f"Primera: {coartadas[0]}")
print(f"Última: {coartadas[-1]}")
```

**Enigma 3.2:**
```python
matriz_acceso = [
    ["Lara", True, True, True, True],
    ["Carlos", True, False, True, False],
    ["Sarah", True, True, False, False],
    ["Rodrigo", False, False, False, False],
    ["Killa", True, False, True, True],
]
print(matriz_acceso)
# ¿Quién tiene acceso al Servidor (columna 2)?
print([fila[0] for fila in matriz_acceso if fila[2]])
```

**Enigma 3.3:**
```python
coordenadas = [
    (-13.5167, -71.9781),
    (-13.1631, -72.5450),
    (-13.3333, -72.0833),
    (-13.3167, -72.1167),
]
coordenadas.append((-13.5090, -71.9820))
print(coordenadas)
```

### Capítulo 4

**Enigma 4.1:**
```python
nuevo_sospechoso = {
    "nombre": "Raúl Cusi",
    "edad": 35,
    "rol": "Periodista",
    "acceso": False,
    "sospecha": 2,
    "coartada": "Llamó a Wayra a las 06:30"
}
sospechosos["Raúl Cusi"] = nuevo_sospechoso
print(sospechosos)
```

**Enigma 4.2:**
```python
for nombre, info in sospechosos.items():
    print(f"{nombre}: {info['evidencias']}")
```

**Enigma 4.3:**
```python
acceso_lab = {"Lara", "Carlos", "Sarah", "Killa"}
coartada_debil = {"Lara", "Carlos", "Rodrigo"}
print(f"Intersección: {acceso_lab & coartada_debil}")
print(f"Unión: {acceso_lab | coartada_debil}")
print(f"Diferencia (acceso - debil): {acceso_lab - coartada_debil}")
print(f"Diferencia (debil - acceso): {coartada_debil - acceso_lab}")
```

### Capítulo 5

**Enigma 5.1:**
```python
nombre = input("Nombre del sospechoso: ")
hora_coartada = float(input("Hora de la coartada: "))
hora_crimen = 2.34

if hora_coartada < 2.00:
    print("Coartada sólida")
elif hora_coartada <= 2.34:
    print("Coartada débil")
else:
    print("Coartada falsa")
```

**Enigma 5.2:**
```python
for s in sospechosos:
    if s["motivo"] >= 7:
        print(f"{s['nombre']}: motivo >= 7")
    if s["acceso"] and s["motivo"] >= 6:
        print(f"{s['nombre']}: acceso Y motivo >= 6")
    if not s["coartada"] or s["huellas"]:
        print(f"{s['nombre']}: sin coartada O con huellas")
```

**Enigma 5.3:**
```python
t1 = "Vi a alguien salir"
t2 = "Estaba oscuro"
t3 = "Escuché discusión"

if t1 and t2:
    print("POSIBLE CONTRADICCIÓN: vio a alguien pero estaba oscuro")
elif t1 and t3:
    print("COMPATIBLE: alguien salió mientras discutían")
else:
    print("VERSIONES COMPATIBLES")
```

### Capítulo 6

**Enigma 6.1:**
```python
evidencias = [
    "Quipus digital en escritorio",
    "Registro de acceso manipulado",
    "Código en la pantalla OLED",
    "Mensaje cifrado en las estaciones",
    "Pasaje secreto del Qhapaq Ñan"
]
for i, ev in enumerate(evidencias, 1):
    print(f"{i}. {ev}")
```

**Enigma 6.2:**
```python
archivos = ["a.py", "b.docx", "c.py", "d.csv", "e.md", "f.py"]
for a in archivos:
    if not a.endswith(".py"):
        continue
    print(a)
```

**Enigma 6.3:**
```python
lista = ["Lara", "Carlos", "Sarah", "Rodrigo Mamani", "Killa"]
for nombre in lista:
    if nombre == "Rodrigo Mamani":
        print("SOSPECHOSO ENCONTRADO")
        break
    print(f"Buscando... {nombre} no es")
```

**Enigma 6.4:**
```python
num = 1
for fila in range(1, 5):
    for col in range(fila):
        print(num, end=" ")
        num += 1
    print()
```

### Capítulo 7

**Enigma 7.1:**
```python
def presentar_sospechoso(nombre, rol):
    print(f"SOSPECHOSO: {nombre}")
    print(f"ROL: {rol}")
```

**Enigma 7.2:**
```python
def verificar_coartada(hora_coartada, hora_crimen="02:34"):
    hc, mc = map(int, hora_coartada.split(":"))
    hcr, mcr = map(int, hora_crimen.split(":"))
    minutos_c = hc * 60 + mc
    minutos_cr = hcr * 60 + mcr
    return abs(minutos_c - minutos_cr) >= 60
```

**Enigma 7.3:**
```python
def mensaje_secreto(mensaje, cifrado=True):
    if cifrado:
        return mensaje[::-1]
    return mensaje
```

### Capítulo 8

**Enigma 8.2:**
```python
hora_crimen = 2 * 60 + 34
with open("coartadas.txt", "r") as f:
    for linea in f:
        nombre, hi, hf = linea.strip().split(":")
        inicio = int(hi[:2]) * 60 + int(hi[2:])
        fin = int(hf[:2]) * 60 + int(hf[2:])
        if inicio <= hora_crimen <= fin:
            print(f"{nombre}: COARTADA VÁLIDA")
        else:
            print(f"{nombre}: SIN COARTADA")
```

### Capítulo 9

**Enigma 9.1:**
```python
def dividir_evidencias(a, b):
    try:
        resultado = a / b
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir una evidencia en cero partes")
```

**Enigma 9.3:**
```python
class EvidenciaFaltanteError(Exception):
    pass

def verificar_evidencia(lista_ev, buscada):
    if buscada not in lista_ev:
        raise EvidenciaFaltanteError(f"Evidencia '{buscada}' no encontrada")
    return True
```

### Capítulo 10

**Enigma 10.1:**
```python
# mis_herramientas.py
def saludar_investigador(nombre):
    return f"Hola, investigador {nombre}"

VERSION = "1.0"
casos_resueltos = 0
```

**Enigma 10.2:**
```python
if __name__ == "__main__":
    print("Módulo de herramientas forenses - Modo autónomo")
```

### Capítulo 11

**Enigma 11.1:**
```python
class Evidencia:
    def __init__(self, tipo, descripcion, fecha, es_clave=False):
        self.tipo = tipo
        self.descripcion = descripcion
        self.fecha = fecha
        self.es_clave = es_clave
    
    def mostrar(self):
        print(f"{self.tipo}: {self.descripcion} ({self.fecha})")
    
    def marcar_como_clave(self):
        self.es_clave = True
```

### Capítulo 12

**Enigma 12.1:**
```python
class Caso:
    def __init__(self, nombre):
        self.nombre_caso = nombre

class CasoHomicidio(Caso):
    def __init__(self, nombre, victima):
        super().__init__(nombre)
        self.victima = victima

class CasoHomicidioCerrado(CasoHomicidio):
    def __init__(self, nombre, victima, culpable):
        super().__init__(nombre, victima)
        self.culpable = culpable
```

---

**Nota:** Estas soluciones son una guía. No hay una única forma correcta de resolver los enigmas. Si tu solución funciona y tiene sentido, ¡es válida!
