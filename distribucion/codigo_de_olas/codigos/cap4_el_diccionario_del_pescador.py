"""Capitulo 4: El Diccionario del Pescador
Conceptos: Diccionarios, sets, operaciones con sets
"""

# ============================================
# LIBRETA DIGITAL DE DON EULOGIO
# ============================================

# Observaciones del mar organizadas por fecha
observaciones = {
    "01-06-2026": {
        "oleaje": "moderado",
        "viento": "sur",
        "temperatura": 18.2,
        "anomalias": False,
        "especies_vistas": ["anchoveta", "lisa"]
    },
    "15-06-2026": {
        "oleaje": "fuerte",
        "viento": "sur-oeste",
        "temperatura": 17.8,
        "anomalias": True,
        "especies_vistas": ["lisa"]
    },
    "27-06-2026": {
        "oleaje": "anomalo",
        "viento": "sur",
        "temperatura": 18.5,
        "anomalias": True,
        "especies_vistas": []
    }
}

print("=== LIBRETA DE DON EULOGIO ===")
for fecha, datos in observaciones.items():
    print(f"\nFecha: {fecha}")
    print(f"  Oleaje: {datos['oleaje']}")
    print(f"  Temperatura: {datos['temperatura']}C")
    print(f"  Anomalias: {datos['anomalias']}")
    print(f"  Especies: {datos['especies_vistas']}")

# --- DICCIONARIO DE IMPLICADOS ---
implicados = {
    "Carlos Parra": {
        "edad": 45,
        "rol": "Ingeniero Naval",
        "involucrado": True,
        "nivel_sospecha": 8,
        "empresa": "OceanTech Peru",
        "evidencias": ["Diseno el generador", "Recibio transferencia de Soto"]
    },
    "Luisa Rivas": {
        "edad": 38,
        "rol": "Biologa Marina",
        "involucrado": False,
        "nivel_sospecha": 3,
        "empresa": "IMARPE (Instituto del Mar)",
        "evidencias": ["Denuncio ruido submarino", "Pidio investigacion"]
    },
    "Miguel Angel Soto": {
        "edad": 62,
        "rol": "Empresario",
        "involucrado": True,
        "nivel_sospecha": 9,
        "empresa": "Grupo Inmobiliario Costa Azul",
        "evidencias": ["Dueno del proyecto LOCUENTO", "Quiere construir en Ancon"]
    },
    "Capitan Paredes": {
        "edad": 55,
        "rol": "Capitan del Puerto",
        "involucrado": False,
        "nivel_sospecha": 5,
        "empresa": "Gobierno del Peru",
        "evidencias": ["Recibio quejas", "No investigo"]
    }
}

print("\n=== FICHAS DE IMPLICADOS ===")
for nombre, datos in implicados.items():
    print(f"\n> {nombre} ({datos['edad']})")
    print(f"  Rol: {datos['rol']}")
    print(f"  Sospecha: {datos['nivel_sospecha']}/10")
    print(f"  Evidencias: {', '.join(datos['evidencias'])}")

# --- METODOS ---
print("\n=== CONSULTAS ===")

# keys()
nombres = list(implicados.keys())
print(f"Implicados: {nombres}")

# values()
print("\nRoles:")
for datos in implicados.values():
    print(f"  * {datos['rol']} - {datos['empresa']}")

# Verificar existencia
if "Carlos Parra" in implicados:
    print(f"\nCarlos Parra esta fichado")

# .get() con valor por defecto
sospecha = implicados.get("Rafa", {}).get("nivel_sospecha", 0)
print(f"Nivel de sospecha de Rafa (si existiera): {sospecha}")

# --- SETS: ESPECIES UNICAS ---

especies_por_fecha = {
    "01-06": {"anchoveta", "lisa", "caballa"},
    "15-06": {"lisa", "caballa"},
    "20-06": {"lisa"},
    "27-06": set()
}

print("\n=== ANALISIS DE ESPECIES ===")

# Especies que habia al inicio
inicio = especies_por_fecha["01-06"]
print(f"Especies al inicio: {inicio}")

# Especies que habia al final
final = especies_por_fecha["27-06"]
print(f"Especies al final: {final}")

# Especies desaparecidas
desaparecidas = inicio - final
print(f"Especies desaparecidas: {desaparecidas}")

# Especies que se mantuvieron (interseccion de todas)
comunes = especies_por_fecha["01-06"]
for fecha in ["15-06", "20-06", "27-06"]:
    comunes = comunes & especies_por_fecha[fecha]
print(f"Especies presentes siempre: {comunes}")

# Todas las especies vistas alguna vez
todas = set()
for especies in especies_por_fecha.values():
    todas = todas | especies
print(f"Todas las especies vistas: {todas}")

# --- PROYECTO LOCUENTO ---

proyecto_locuento = {
    "nombre_completo": "LOCalizador de Corrientes y Oleaje para Urbanizacion Nortina",
    "empresa": "Grupo Inmobiliario Costa Azul",
    "presupuesto": 2500000,
    "etapas": ["Estudio", "Instalacion", "Pruebas", "Operacion"],
    "ubicacion": "Ancon, 500m mar adentro",
    "equipo": {
        "ingeniero_jefe": "Carlos Parra",
        "financiista": "Miguel Angel Soto",
        "operador": "Desconocido"
    },
    "estado": "Pruebas"
}

print("\n=== PROYECTO LOCUENTO ===")
for clave, valor in proyecto_locuento.items():
    if isinstance(valor, dict):
        print(f"\n{clave}:")
        for k, v in valor.items():
            print(f"  {k}: {v}")
    else:
        print(f"{clave}: {valor}")

# --- ENIGMAS ---

print("\n=== ENIGMA 4.1: Tu diccionario de playa ===")
mi_playa = {
    "nombre": "Ancon",
    "ubicacion": "Lima, Peru",
    "temperatura_agua": 18.5,
    "tiene_estacionamiento": True,
    "ola_favorita": "La Derecha"
}
for k, v in mi_playa.items():
    print(f"  {k}: {v}")

print("\n=== ENIGMA 4.2: Consulta de implicados ===")
print("Nombres:", list(implicados.keys()))
print("\nNivel de sospecha > 5:")
for nombre, datos in implicados.items():
    if datos["nivel_sospecha"] > 5:
        print(f"  * {nombre} ({datos['nivel_sospecha']}/10)")
print(f"\nEvidencias de Carlos Parra: {implicados['Carlos Parra']['evidencias']}")

print("\n=== ENIGMA 4.3: Sets de deportes acuaticos ===")
surfistas = {"Mateo", "Rafa", "Lucia"}
buceadores = {"Rafa", "Pedro", "Lucia"}
kayakistas = {"Mateo", "Pedro", "Sofia"}

print(f"Surf y buceo: {surfistas & buceadores}")
print(f"Solo surf: {surfistas - buceadores - kayakistas}")
print(f"Todos los deportistas: {surfistas | buceadores | kayakistas}")
