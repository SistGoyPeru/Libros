# Capítulo 14: Revelación en el Muelle

## Conceptos: Repaso final — Poniendo todo junto

---

La noche era clara en Ancón. Mateo estaba en el muelle, su laptop abierta mostrando el analizador de olas. Frente a él, el mar estaba sospechosamente tranquilo. Demasiado tranquilo.

Había citado a todos los implicados. Soto, Parra, Luisa. Y, para su sorpresa, el viejo Eulogio.

—Ustedes se preguntan por qué los reuní aquí —dijo Mateo—. Porque el mar habla. Y yo aprendí a escucharlo... con Python.

### El momento de la verdad

Mateo mostró el analizador en vivo. Cada ola artificial quedaba marcada con sus mensajes descifrados.

—El generador está ahí —señaló hacia el horizonte—. A 500 metros de la costa. Transmite datos en las olas. ¿Saben cómo lo sé? Porque las olas naturales no tienen frecuencias de 15, 18, 20, 25 y 30 segundos. Esas frecuencias son mensajes. Son coordenadas.

```python
# === REPASO FINAL: EL CÓDIGO DE LA VERDAD ===

mensajes_olas = {
    "15s": "ANCÓN",
    "18s": "PRIVATO",
    "20s": "COSTAZUL",
    "25s": "PLAN",
    "30s": "OLASDECODIFICADO"
}

print("=== DECODIFICACIÓN COMPLETA ===")
for freq, msg in mensajes_olas.items():
    print(f"  Frecuencia {freq} → {msg}")

mensaje = " ".join(mensajes_olas.values())
print(f"\n   🔑 Mensaje completo: {mensaje}")

# La evidencia final
evidencias = [
    "Firmware del generador (módulo secreto)",
    "Registros de activación (30 días)",
    "Transferencias de Costa Azul S.A.",
    "Mensajes descifrados en 9 olas artificiales",
    "Testimonio del capitán del Don Eulogio",
]

print("\n=== EVIDENCIAS RECOPILADAS ===")
for i, ev in enumerate(evidencias, 1):
    print(f"  {i}. {ev}")

# Búsqueda de cómplices
implicados = {
    "Soto (Costa Azul)": {
        "rol": "Financiamiento",
        "evidencias": 4,
        "nivel": "Alto"
    },
    "Parra (Ingeniero)": {
        "rol": "Construcción del generador",
        "evidencias": 3,
        "nivel": "Alto"
    },
    "Rivas (Bióloga)": {
        "rol": "Informes ambientales falsos",
        "evidencias": 2,
        "nivel": "Medio"
    },
}

print("\n=== NIVEL DE IMPLICACIÓN ===")
for nombre, datos in implicados.items():
    print(f"  {nombre}:")
    print(f"    Rol: {datos['rol']}")
    print(f"    Evidencias: {datos['evidencias']}")
    print(f"    Nivel: {datos['nivel']}")
```

### La confesión

Soto se levantó, pálido.

—Está bien. Es cierto. Usamos el generador para crear olas artificiales. Pero no para privatizar Ancón. Bueno... también para eso. Pero el verdadero propósito era probar un sistema de comunicación submarina. La Marina estuvo involucrada al principio.

—¿La Marina? —preguntó Luisa.

—El proyecto LOCUENTO comenzó como un proyecto de defensa. Comunicación por olas. Invisible, indetectable. Pero cuando lo cancelaron, decidí seguir adelante por mi cuenta. Para la inmobiliaria.

—Y para eso —dijo Mateo— manipularon las olas, alejaron a los surfistas, y planearon comprar toda la costa.

Don Eulogio se levantó lentamente.

—Joven Mateo —dijo—. Yo sabía todo esto desde el principio. El generador está en mi lancha. Yo ayudé a Parra a instalarlo.

Todos miraron al viejo pescador.

—Pero no para Soto —continuó—. Para la comunidad. Grabé todo. Tengo meses de evidencias. Esperaba a alguien como usted para exponerlo.

El viejo pescador sacó un USB de su bolsillo.

—Aquí está todo: el firmware original, los planos, las transferencias. Mi nieta me enseñó a usar Python. La evidencia... la guardé en un diccionario.

```python
# El USB de Don Eulogio
evidencia_final = {
    "firmware": "locuento_v2_original.bin",
    "planos": ["generador.dwg", "sistema_comunicacion.dwg"],
    "transferencias": [
        {"de": "Costa Azul S.A.", "a": "Parra Ingeniería", "monto": 150000},
        {"de": "Costa Azul S.A.", "a": "Soto Holding", "monto": 500000},
        {"de": "Soto Holding", "a": "Municipalidad de Ancón", "monto": 20000},
    ],
    "testigos": ["Eulogio Quispe", "Ana María Huerta", "Pedro Castillo"],
    "fecha_inicio": "2025-03-15",
}

print("=== EVIDENCIA FINAL (USB DON EULOGIO) ===")
for clave, valor in evidencia_final.items():
    print(f"  {clave}: {valor}")
```

### Epílogo del capítulo

La noticia estalló en todos los medios. "Costa Azul S.A. investigada por manipulación ambiental". Soto fue detenido. Parra también. Luisa fue absuelta por colaborar con la investigación.

El generador fue desmantelado. La Municipalidad de Ancón declaró la zona como "Reserva de Olas" —la primera en el Perú— protegiendo el derecho de los surfistas a las olas naturales.

Mateo volvió a surfear al día siguiente. Las olas eran perfectas. Naturales. Libres.

Pero antes de guardar su tabla, miró el horizonte. En la pantalla de su laptop, en la orilla, un nuevo mensaje parpadeaba:

```
SISTEMA_OLAS: NUEVO GENERADOR DETECTADO - CALLAO - FRECUENCIA 22
```

El código de las olas nunca dejaba de hablar.

## Enigmas

### Enigma 14.1: Sistema de alertas

Crea una función que revise un archivo de registros y detecte frecuencias sospechosas.

### Enigma 14.2: Base de datos de playas

Usando un archivo JSON, crea un sistema que almacene y consulte playas protegidas vs amenazadas.

### Enigma 14.3: Cifrado propio

Crea tu propio sistema de cifrado usando olas como metáfora. Cada letra se convierte en una frecuencia.

---

## Lo que aprendiste

- Todos los conceptos de Python pueden trabajar juntos
- La evidencia digital es poderosa
- El código puede exponer la verdad
- La comunidad puede usar la tecnología para protegerse

---
