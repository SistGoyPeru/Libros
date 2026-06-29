# Capítulo 4: El Diccionario del Pescador

## Conceptos: Diccionarios, sets, operaciones con sets

---

Mateo encontró a don Eulogio, un pescador de 78 años que conocía el mar de Ancón mejor que nadie. Tenía libretas llenas de anotaciones: fechas, condiciones del mar, especies que habían desaparecido.

—Don Eulogio —le dijo Mateo—. Usted ha visto todo. ¿Qué ha cambiado en el mar?

—Todo, mijito. Las olas ya no son las mismas. Los peces se fueron. Y desde hace un mes, hay un ruido. Un zumbido que viene del fondo.

Don Eulogio abrió una libreta gastada. En ella, había organizado sus observaciones como un diccionario: cada fecha tenía una entrada con múltiples datos.

—Esto es un diccionario —dijo Mateo—. Como los de Python.

## Diccionarios: La libreta del pescador

Los **diccionarios** asocian claves con valores. Como las libretas de don Eulogio: cada fecha (clave) tiene una lista de observaciones (valor).

```python
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
        "oleaje": "anómalo",
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
    print(f"  Temperatura: {datos['temperatura']}°C")
    print(f"  Anomalías: {datos['anomalias']}")
    print(f"  Especies: {datos['especies_vistas']}")
```

### Diccionario de sospechosos

Mateo creó un diccionario con todos los implicados y sus datos detallados:

```python
# --- DICCIONARIO DE IMPLICADOS ---
implicados = {
    "Carlos Parra": {
        "edad": 45,
        "rol": "Ingeniero Naval",
        "involucrado": True,
        "nivel_sospecha": 8,
        "empresa": "OceanTech Perú",
        "evidencias": ["Diseñó el generador", "Recibió transferencia de Soto"]
    },
    "Luisa Rivas": {
        "edad": 38,
        "rol": "Bióloga Marina",
        "involucrado": False,
        "nivel_sospecha": 3,
        "empresa": "IMARPE (Instituto del Mar)",
        "evidencias": ["Denunció ruido submarino", "Pidió investigación"]
    },
    "Miguel Ángel Soto": {
        "edad": 62,
        "rol": "Empresario",
        "involucrado": True,
        "nivel_sospecha": 9,
        "empresa": "Grupo Inmobiliario Costa Azul",
        "evidencias": ["Dueño del proyecto LOCUENTO", "Quiere construir en Ancón"]
    },
    "Capitán Paredes": {
        "edad": 55,
        "rol": "Capitanía del Puerto",
        "involucrado": False,
        "nivel_sospecha": 5,
        "empresa": "Gobierno del Perú",
        "evidencias": ["Recibió quejas", "No investigó"]
    }
}

print("\n=== FICHAS DE IMPLICADOS ===")
for nombre, datos in implicados.items():
    print(f"\n▶ {nombre} ({datos['edad']})")
    print(f"  Rol: {datos['rol']}")
    print(f"  Sospecha: {datos['nivel_sospecha']}/10")
    print(f"  Evidencias: {', '.join(datos['evidencias'])}")
```

### Métodos de diccionarios

```python
# --- MÉTODOS ---
print("\n=== CONSULTAS ===")

# keys()
nombres = list(implicados.keys())
print(f"Implicados: {nombres}")

# values()
print("\nRoles:")
for datos in implicados.values():
    print(f"  • {datos['rol']} - {datos['empresa']}")

# Verificar existencia
if "Carlos Parra" in implicados:
    print(f"\nCarlos Parra está fichado")

# .get() con valor por defecto
sospecha = implicados.get("Rafa", {}).get("nivel_sospecha", 0)
print(f"Nivel de sospecha de Rafa (si existiera): {sospecha}")
```

## Sets: Especies únicas del mar

Para analizar qué especies habían desaparecido, Mateo usó **sets** —colecciones de elementos únicos:

```python
# --- SETS: ESPECIES ÚNICAS ---

especies_por_fecha = {
    "01-06": {"anchoveta", "lisa", "caballa"},
    "15-06": {"lisa", "caballa"},
    "20-06": {"lisa"},
    "27-06": set()
}

print("\n=== ANÁLISIS DE ESPECIES ===")

# Especies que había al inicio
inicio = especies_por_fecha["01-06"]
print(f"Especies al inicio: {inicio}")

# Especies que había al final
final = especies_por_fecha["27-06"]
print(f"Especies al final: {final}")

# Especies desaparecidas
desaparecidas = inicio - final
print(f"Especies desaparecidas: {desaparecidas}")

# Especies que se mantuvieron (intersección de todas)
comunes = especies_por_fecha["01-06"]
for fecha in ["15-06", "20-06", "27-06"]:
    comunes = comunes & especies_por_fecha[fecha]
print(f"Especies presentes siempre: {comunes}")

# Todas las especies vistas alguna vez
todas = set()
for especies in especies_por_fecha.values():
    todas = todas | especies
print(f"Todas las especies vistas: {todas}")
```

## El proyecto LOCUENTO

Mateo encontró los papeles del proyecto LOCUENTO en la oficina del puerto. Los datos estaban en un diccionario:

```python
# --- PROYECTO LOCUENTO ---

proyecto_locuento = {
    "nombre_completo": "LOCalizador de Corrientes y Oleaje para Urbanización Nortina",
    "empresa": "Grupo Inmobiliario Costa Azul",
    "presupuesto": 2500000,
    "etapas": ["Estudio", "Instalación", "Pruebas", "Operación"],
    "ubicacion": "Ancón, 500m mar adentro",
    "equipo": {
        "ingeniero_jefe": "Carlos Parra",
        "financiista": "Miguel Ángel Soto",
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
```

## Enigmas

### Enigma 4.1: Tu diccionario de playa

Crea un diccionario `mi_playa` con: nombre, ubicación, temperatura_agua, tiene_estacionamiento, y ola_favorita. Luego muestra cada dato.

### Enigma 4.2: Consulta de implicados

Del diccionario `implicados`, muestra:
- Los nombres de todos
- Quién tiene nivel_sospecha > 5
- Las evidencias de Carlos Parra

### Enigma 4.3: Sets de deportes acuáticos

Dados estos sets:
```python
surfistas = {"Mateo", "Rafa", "Lucía"}
buceadores = {"Rafa", "Pedro", "Lucía"}
kayakistas = {"Mateo", "Pedro", "Sofía"}
```
Encuentra:
- Quiénes hacen surf y buceo (intersección)
- Quiénes hacen solo surf (diferencia)
- Todos los deportistas (unión)

---

## Lo que aprendiste

- Los **diccionarios** asocian claves con valores `{clave: valor}`
- Se accede con `diccionario[clave]`
- **Métodos**: `.keys()`, `.values()`, `.items()`, `.get()`
- Los **sets** son colecciones de elementos únicos
- **Operaciones**: `&` (intersección), `|` (unión), `-` (diferencia)
- Los diccionarios pueden anidarse

Mateo tenía el proyecto LOCUENTO mapeado. Pero había un problema: el "operador" del generador aparecía como "Desconocido". Alguien más estaba involucrado. Alguien que no aparecía en los papeles.

—Necesito saber quién opera el generador —dijo—. Y para eso, necesito tomar decisiones. Evaluar a cada implicado. Si hizo X, entonces Y.

Necesitaba **condicionales**.

---
