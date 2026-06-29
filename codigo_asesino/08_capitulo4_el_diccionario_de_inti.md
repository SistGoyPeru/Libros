# Capítulo 4: El Diccionario de Inti

## Conceptos: Diccionarios, sets, operaciones con sets

---

Wayra no podía dormir. Las 3:00 a.m. la encontraron aún frente a su laptop, con el quipus digital de Inti desplegado en la pantalla y una taza de té de coca ya fría a su lado.

Había algo que no encajaba.

Los registros de acceso mostraban que la cuenta de Lara Mamani se había usado a las 2:34 a.m., pero Lara estaba en su departamento. ¿Quién usó su cuenta? ¿Y por qué?

Wayra decidió que necesitaba más información sobre cada sospechoso. No solo nombres y edades: necesitaba datos estructurados que pudiera consultar rápidamente. Necesitaba un **diccionario**.

## Diccionarios: La memoria del quipucamayoc

Si las listas son como cuerdas de quipu ordenadas, los **diccionarios** son como el conocimiento del quipucamayoc —el guardián de los quipus—: asocian un nombre (la **clave**) con un valor (el **significado**).

En Python, los diccionarios se escriben entre `{}` con pares `clave: valor`:

```python
# ============================================
# DICCIONARIO DEL CASO
# ============================================

# Información básica del caso
caso = {
    "nombre": "El Asesinato del Dr. Inti Quispe",
    "fecha": "27 de junio, 2026",
    "lugar": "Templo del Sol (Coricancha)",
    "hora": "02:34 (acceso), 06:30 (descubrimiento)",
    "estado": "abierto",
    "analista": "Wayra Condori"
}

print("=== DATOS DEL CASO ===")
print(f"Nombre: {caso['nombre']}")
print(f"Lugar: {caso['lugar']}")
print(f"Analista: {caso['analista']}")
```

—Los diccionarios —explicó Wayra mientras tecleaba— son como los quipus temáticos. Cada cuerda principal (clave) tiene un significado (valor). Y puedes tener cuerdas que cuelgan de otras (diccionarios anidados).

```python
# Diccionario de un sospechoso con datos detallados
lara = {
    "nombre": "Lara Mamani",
    "edad": 32,
    "rol": "Asistente de laboratorio",
    "acceso": True,
    "nivel_sospecha": 7,
    "coartada": "Estaba en su departamento",
    "conexion_con_inti": "Trabajó junto a él por 3 años",
    "motivo": "Económico - ¿chantaje?"
}

print("\n=== FICHA DE LARA MAMANI ===")
for clave, valor in lara.items():
    print(f"{clave}: {valor}")
```

### Diccionarios anidados: Quipus jerárquicos

Los verdaderos quipus tenían una estructura jerárquica: cuerda principal, cuerdas secundarias, cuerdas terciarias... Wayra modeló esto con diccionarios dentro de diccionarios:

```python
# Estructura completa de sospechosos como diccionario anidado
sospechosos = {
    "Lara Mamani": {
        "edad": 32,
        "rol": "Asistente",
        "acceso": True,
        "sospecha": 7,
        "coartada": "Departamento propio",
        "evidencias": ["huella digital en teclado", "registro de acceso falso"]
    },
    "Dr. Carlos Huamán": {
        "edad": 55,
        "rol": "Colega universitario",
        "acceso": True,
        "sospecha": 8,
        "coartada": "Oficina universitaria",
        "evidencias": ["discusión con Inti días antes", "publicaciones bloqueadas"]
    },
    "Dra. Sarah Chen": {
        "edad": 40,
        "rol": "Colaboradora MIT",
        "acceso": True,
        "sospecha": 6,
        "coartada": "Videollamada con MIT",
        "evidencias": ["presión del MIT por resultados", "visa próxima a vencer"]
    },
    "Rodrigo Mamani": {
        "edad": 60,
        "rol": "Empresario tecnológico",
        "acceso": False,
        "sospecha": 9,
        "coartada": "Cena de negocios",
        "evidencias": ["interés en comprar Yachay", "conexiones políticas"]
    },
    "Mama Killa": {
        "edad": 70,
        "rol": "Hermana",
        "acceso": True,
        "sospecha": 5,
        "coartada": "Dormía en su casa",
        "evidencias": ["herencia", "secretos familiares"]
    }
}

# Accediendo a datos específicos
print(f"\n=== CONSULTAS RÁPIDAS ===")
print(f"¿Qué rol tiene Sarah? {sospechosos['Dra. Sarah Chen']['rol']}")
print(f"Evidencias contra Carlos: {sospechosos['Dr. Carlos Huamán']['evidencias']}")

# Modificando valores
sospechosos["Lara Mamani"]["sospecha"] = 9  # Nueva evidencia la hace más sospechosa
print(f"\nNivel de sospecha de Lara actualizado: {sospechosos['Lara Mamani']['sospecha']}/10")
```

### Métodos de diccionarios

Wayra necesitaba herramientas para explorar este "quipu digital" de información:

```python
# --- MÉTODOS DE DICCIONARIOS ---

# .keys() - todas las claves
print("\n=== TODOS LOS SOSPECHOSOS ===")
nombres = list(sospechosos.keys())
print(nombres)

# .values() - todos los valores
print("\n=== DATOS DE CADA SOSPECHOSO ===")
datos = list(sospechosos.values())
for dato in datos:
    print(f"  • {dato['rol']} - Sospecha: {dato['sospecha']}/10")

# .items() - pares clave-valor
print("\n=== NIVEL DE SOSPECHA ===")
for nombre, info in sospechosos.items():
    print(f"{nombre}: {info['sospecha']}/10")

# Verificar si una clave existe
if "Lara Mamani" in sospechosos:
    print("\nLara Mamani está en la base de datos")

# .get() - obtener valor con default (evita errores)
acceso = sospechosos.get("Lara Mamani", {}).get("acceso", "No especificado")
print(f"Acceso de Lara: {acceso}")

# .update() - actualizar con otro diccionario
nuevos_datos = {"Lara Mamani": {"sospecha": 10, "nota": "¡NUEVA EVIDENCIA!"}}
sospechosos.update(nuevos_datos)
print(f"\nDatos actualizados de Lara: {sospechosos['Lara Mamani']}")
```

## Sets: Los nudos únicos

Hay un tipo de dato más en Python que resultó crucial para el caso: los **sets** (conjuntos). Un set es una colección **no ordenada** de elementos **únicos**. Es como un quipu donde cada tipo de nudo solo aparece una vez.

```python
# --- SETS: ELEMENTOS ÚNICOS ---

# Roles únicos entre los sospechosos
roles = set()
for info in sospechosos.values():
    roles.add(info["rol"])

print("\n=== ROLES ÚNICOS EN EL CASO ===")
print(roles)

# Evidencias únicas (sin repetir)
evidencias_totales = set()
for info in sospechosos.values():
    for evidencia in info["evidencias"]:
        evidencias_totales.add(evidencia)

print("\n=== EVIDENCIAS ÚNICAS RECOPILADAS ===")
for e in evidencias_totales:
    print(f"  • {e}")

# --- OPERACIONES CON SETS ---

# ¿Quiénes tenían acceso al laboratorio?
tienen_acceso = {nombre for nombre, info in sospechosos.items() if info["acceso"]}
print(f"\nSospechosos con acceso: {tienen_acceso}")

# ¿Quiénes tienen sospecha mayor a 7?
alta_sospecha = {nombre for nombre, info in sospechosos.items() if info["sospecha"] > 7}
print(f"Sospechosos con alta sospecha: {alta_sospecha}")

# Intersección: ¿quién cumple AMBAS condiciones?
mas_sospechosos_con_acceso = tienen_acceso & alta_sospecha
print(f"Altamente sospechosos CON acceso: {mas_sospechosos_con_acceso}")

# Unión: todos los que tienen acceso O alta sospecha
todos_los_posibles = tienen_acceso | alta_sospecha
print(f"Todos los posibles implicados: {todos_los_posibles}")

# Diferencia: acceso pero NO alta sospecha
acceso_pero_no_sospecha = tienen_acceso - alta_sospecha
print(f"Acceso pero baja sospecha: {acceso_pero_no_sospecha}")
```

Wayra observó los resultados. La intersección mostraba los nombres de los sospechosos con alto nivel de sospecha **y** acceso al laboratorio: Lara Mamani y el Dr. Carlos Huamán.

Pero había un problema. Uno de los sospechosos no tenía acceso directo, pero aparecía consistentemente en todas las teorías.

—Rodrigo Mamani —murmuró Wayra—. No tiene acceso al laboratorio, pero es el más sospechoso. ¿Cómo mató a Inti si no podía entrar?

## El diccionario del quipu

Wayra volvió al quipus físico. Las cuerdas de colores tenían un patrón específico. Decidió modelar el quipu completo como un diccionario:

```python
# --- MODELANDO EL QUIPU FÍSICO COMO DICCIONARIO ---

quipu_inti = {
    "cuerda_roja": {
        "significado": "guerra/conflicto",
        "nudos": [1, 4, 9],
        "tipo_nudo": "simple",
    },
    "cuerda_verde": {
        "significado": "agricultura/conocimiento",
        "nudos": [2, 5, 10],
        "tipo_nudo": "compuesto",
    },
    "cuerda_azul": {
        "significado": "religión/espiritualidad",
        "nudos": [1, 5, 9],
        "tipo_nudo": "simple",
    },
    "cuerda_amarilla": {
        "significado": "riqueza/poder",
        "nudos": [3, 7, 11],
        "tipo_nudo": "compuesto largo",
    },
    "cuerda_blanca": {
        "significado": "conexión espiritual/verdad",
        "nudos": [1, 3, 5, 7, 9, 11],
        "tipo_nudo": "binario intercalado",
    }
}

# Analizando el quipu
print("\n=== ANÁLISIS DEL QUIPU DE INTI ===")
for cuerda, info in quipu_inti.items():
    print(f"\n{cuerda.replace('_', ' ').title()}:")
    print(f"  Significado: {info['significado']}")
    print(f"  Nudos en posiciones: {info['nudos']}")
    print(f"  Tipo: {info['tipo_nudo']}")
```

—La cuerda blanca —dijo Wayra, señalando la pantalla—. Tiene nudos en todas las posiciones impares hasta el 11. En la numeración inca, los impares representan preguntas. Pero si tomas los nudos de la cuerda blanca como código binario...

Se detuvo. De repente, todo cobró sentido.

—Los nudos de la cuerda blanca no son preguntas —susurró—. Son **coordenadas**. Posiciones en los otros strings. Es un índice.

## Enigmas: Construye tu propia base de datos

### Enigma 4.1: Tu diccionario de sospechoso

Crea un diccionario para un nuevo sospechoso (inventa uno) con las siguientes claves:
- `nombre`, `edad`, `rol`, `acceso`, `sospecha`, `coartada`
- Luego agrégalo al diccionario principal `sospechosos`
- Muestra el diccionario actualizado

### Enigma 4.2: Consulta de evidencias

Usando el diccionario `sospechosos`, escribe código que muestre:
1. Todos los nombres de los sospechosos
2. La evidencia de cada uno
3. Quién tiene la sospecha más alta

### Enigma 4.3: Sets en acción

Dados estos dos sets:

```python
acceso_lab = {"Lara", "Carlos", "Sarah", "Killa"}
coartada_debil = {"Lara", "Carlos", "Rodrigo"}
```

Encuentra:
- Quiénes tienen acceso Y coartada débil (intersección)
- Quiénes tienen acceso O coartada débil (unión)
- Quiénes tienen acceso pero coartada sólida (diferencia)
- Quiénes tienen coartada débil pero no acceso (diferencia)

---

## Lo que aprendiste

- Los **diccionarios** asocian claves con valores (`{clave: valor}`)
- Se accede a los valores con `diccionario[clave]`
- Los diccionarios pueden **anidarse** (valores que son diccionarios)
- **Métodos de diccionario**: `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`
- Los **sets** son colecciones no ordenadas de elementos únicos
- **Operaciones con sets**: `&` (intersección), `|` (unión), `-` (diferencia)
- Los sets se usan para eliminar duplicados y comparar grupos

Eran las 4:00 a.m. cuando Wayra encontró lo que buscaba. La cuerda blanca del quipus no señalaba lugares físicos: señalaba posiciones en el código fuente de Yachay. Inti había escondido la clave de acceso a su IA en los patrones de un tejido.

Pero cuando fue a verificar el archivo, descubrió que alguien más había estado ahí.

El archivo había sido modificado. La última modificación: 2:34 a.m. del 27 de junio. La misma hora del acceso fraudulento de la cuenta de Lara.

Wayra levantó la vista de la pantalla. La neblina matutina comenzaba a iluminarse con los primeros rayos de sol. Afuera, Neo-Cusco despertaba.

Pero ella sabía que el verdadero despertar apenas comenzaba.

---
