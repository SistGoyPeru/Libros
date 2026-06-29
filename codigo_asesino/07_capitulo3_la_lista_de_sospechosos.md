# Capítulo 3: La Lista de Sospechosos

## Conceptos: Listas, tuplas, indexing, métodos de listas

---

La policía había establecido un perímetro alrededor del laboratorio, pero eso no detuvo a Wayra. Con la ayuda de Raúl y su credencial de prensa, logró acceder a los archivos iniciales del caso.

El oficial a cargo, un hombre de unos 50 años con bigote gris y cara de pocos amigos, les entregó una tablet con la lista de personas relacionadas al Dr. Inti Quispe.

—Son cinco —dijo el oficial—. Todos tenían motivos. Todos tenían acceso. Pero solo uno tuvo la oportunidad.

Wayra tomó la tablet y leyó:

1. **Lara Mamani** — Asistente. 32 años. Acceso total al laboratorio. Motivo: ¿Económico?
2. **Dr. Carlos Huamán** — Colega. 55 años. Acceso restringido. Motivo: Envidia profesional.
3. **Dra. Sarah Chen** — Colaboradora. 40 años. Acceso parcial. Motivo: Presión académica.
4. **Rodrigo Mamani** — Empresario. 60 años. Sin acceso directo. Motivo: Control del proyecto.
5. **Mama Killa** — Hermana. 70 años. Acceso familiar. Motivo: ¿Secreto familiar?

—Son datos, Wayra —dijo Raúl—. Tu especialidad. ¿Qué puedes hacer con eso?

Wayra sonrió. Lo primero era estructurar esa información.

## Listas: El primer contenedor

En Python, una **lista** es una colección ordenada de elementos. Piensa en ella como una cuerda de quipu donde cada nudo es un elemento. Los elementos pueden ser de cualquier tipo: strings, números, incluso otras listas.

```python
# ============================================
# LISTA DE SOSPECHOSOS
# ============================================

# Creamos una lista con los nombres de los sospechosos
sospechosos = [
    "Lara Mamani",
    "Dr. Carlos Huamán",
    "Dra. Sarah Chen",
    "Rodrigo Mamani",
    "Mama Killa"
]

print("=== SOSPECHOSOS DEL CASO ===")
print(sospechosos)
print(f"Cantidad de sospechosos: {len(sospechosos)}")
```

—Pero solo tener nombres no basta —dijo Wayra mientras tecleaba—. Necesitamos más información.

### Accediendo a elementos

Al igual que con los strings, podemos acceder a elementos de una lista usando índices:

```python
# El primer sospechoso (índice 0)
print(f"Primer sospechoso: {sospechosos[0]}")

# El último sospechoso (índice -1)
print(f"Último sospechoso: {sospechosos[-1]}")

# Los tres primeros (slicing)
print(f"Tres primeros: {sospechosos[0:3]}")

# Los dos últimos
print(f"Dos últimos: {sospechosos[-2:]}")
```

### Listas de listas: El quipu multidimensional

Los quipus verdaderos no tenían una sola cuerda: tenían cuerdas principales, cuerdas secundarias, y cuerdas que colgaban de otras cuerdas. Wayra decidió modelar esa estructura con listas anidadas:

```python
# Cada sospechoso tiene múltiples datos
# [nombre, edad, rol, acceso_al_laboratorio, nivel_de_sospecha]

fichas_sospechosos = [
    ["Lara Mamani", 32, "Asistente", True, 7],
    ["Dr. Carlos Huamán", 55, "Colega", True, 8],
    ["Dra. Sarah Chen", 40, "Colaboradora", True, 6],
    ["Rodrigo Mamani", 60, "Empresario", False, 9],
    ["Mama Killa", 70, "Hermana", True, 5]
]

print("\n=== FICHAS COMPLETAS ===")
for ficha in fichas_sospechosos:
    print(f"Nombre: {ficha[0]} | Edad: {ficha[1]} | Rol: {ficha[2]} | Acceso: {ficha[3]} | Sospecha: {ficha[4]}/10")
```

Pero Wayra notó un problema: si modificaba una ficha, ¿cómo asegurarse de que los datos fueran consistentes? Python tiene otra estructura para eso: las **tuplas**.

## Tuplas: Datos inmutables

Una **tupla** es como una lista, pero **no se puede modificar** después de creada. Es ideal para datos que no deben cambiar:

```python
# Tuplas para datos fijos (como coordenadas o registros históricos)
escena_crimen = (-13.5167, -71.9781)  # Coordenadas del Coricancha
print(f"\nCoordenadas del crimen: {escena_crimen}")
print(f"Latitud: {escena_crimen[0]}")
print(f"Longitud: {escena_crimen[1]}")

# Intentar modificar una tupla causa error
# escena_crimen[0] = 0.0  # ¡Esto lanza TypeError!
```

—Las tuplas son como los quipus históricos —explicó Wayra—. No puedes cambiarlos. Solo puedes leerlos e interpretarlos. Las listas, en cambio, son como los quipus digitales: dinámicos, modificables, actualizables.

## Métodos de listas: Manipulando las cuerdas

Python ofrece métodos poderosos para trabajar con listas. Wayra los usó para organizar la información del caso:

```python
print("\n=== MANIPULANDO LA LISTA ===")

# .append() - Agregar un elemento al final
sospechosos.append("Oficial Paredes (policía)")
print(f"Agregamos al oficial: {sospechosos}")

# .remove() - Eliminar un elemento
sospechosos.remove("Oficial Paredes (policía)")
print(f"Quitamos al oficial: {sospechosos}")

# .sort() - Ordenar alfabéticamente
sospechosos.sort()
print(f"Ordenados alfabéticamente: {sospechosos}")

# .reverse() - Invertir el orden
sospechosos.reverse()
print(f"Orden inverso: {sospechosos}")

# .pop() - Extraer y eliminar el último elemento (o un índice específico)
ultimo = sospechosos.pop()
print(f"Extraído: {ultimo}")
print(f"Lista actualizada: {sospechosos}")

# .index() - Encontrar la posición de un elemento
posicion = sospechosos.index("Dra. Sarah Chen")
print(f"La Dra. Sarah Chen está en posición: {posicion}")

# .count() - Contar cuántas veces aparece un elemento
conteo = sospechosos.count("Lara Mamani")
print(f"Lara Mamani aparece {conteo} veces")
```

## Organizando la evidencia

Wayra decidió organizar toda la evidencia disponible en listas:

```python
# --- EVIDENCIA RECOPILADA ---

evidencias_fisicas = [
    "Quipus digital en escritorio",
    "Taza de café frío",
    "Puerta sin cerradura forzada",
    "Código en pantalla OLED"
]

evidencias_digitales = [
    "Mensaje: quipu_digital_001 = 'Ñan:1:3:5:7:9'",
    "Sistema de bienvenida personalizado",
    "Archivos del Proyecto Yachay encriptados",
    "Registro de acceso de las últimas 24 horas"
]

testigos = [
    "Raúl (periodista, descubrió el cuerpo)",
    "Guardia de seguridad (no vio nada sospechoso)",
    "Vecino del laboratorio (escuchó discusión)"
]

print("\n=== EVIDENCIA DEL CASO ===")
print(f"\nEvidencias físicas ({len(evidencias_fisicas)}):")
for evidencia in evidencias_fisicas:
    print(f"  • {evidencia}")

print(f"\nEvidencias digitales ({len(evidencias_digitales)}):")
for evidencia in evidencias_digitales:
    print(f"  • {evidencia}")

print(f"\nTestigos ({len(testigos)}):")
for testigo in testigos:
    print(f"  • {testigo}")
```

Había algo extraño en el quipus. Wayra volvió a mirarlo. Las cuerdas no solo tenían nudos en diferentes posiciones: también tenían diferentes **colores** que colgaban de la cuerda principal.

—Los colores... —murmuró—. En los quipus, los colores representan categorías. Rojo para el guerrero. Verde para la agricultura. Azul para la religión. Amarillo para el oro. Blanco para la espiritualidad.

—¿Y cómo se traduce eso a código? —preguntó Raúl.

—Con listas de tuplas. Cada cuerda es una lista de nudos, y cada nudo es una tupla de (posición, color, tipo_nudo).

## Enigmas: Construye tu propia base de datos del caso

### Enigma 3.1: La lista de coartadas

Crea una lista llamada `coartadas` con las siguientes declaraciones de los sospechosos:

1. Lara: "Estaba en mi departamento, viendo series."
2. Carlos: "Trabajaba en mi oficina de la universidad."
3. Sarah: "Tenía una videollamada con el MIT."
4. Rodrigo: "Estaba en una cena de negocios."
5. Killa: "Dormía. A mi edad, no salgo de noche."

Luego:
- Agrega una coartada para ti mismo
- Ordena la lista alfabéticamente
- Muestra cuántas coartadas hay
- Muestra la primera y la última

### Enigma 3.2: Matriz de acceso

Crea una lista de listas (matriz) que represente quién tiene acceso a qué áreas del laboratorio:

```
Áreas: "Laboratorio", "Servidor", "Archivos", "Azotea"
Sospechosos con acceso:
- Lara: todas
- Carlos: Laboratorio, Archivos
- Sarah: Laboratorio, Servidor
- Rodrigo: ninguna
- Killa: Laboratorio, Archivos, Azotea
```

Muestra la matriz y verifica quién tiene acceso al Servidor.

### Enigma 3.3: Tuplas inmutables

El Dr. Inti dejó una lista de coordenadas de lugares sagrados donde podría haber escondido información. Como son datos históricos, deben ser tuplas:

```python
coordenadas_sagradas = [
    (-13.5167, -71.9781),  # Coricancha
    (-13.1631, -72.5450),  # Machu Picchu
    (-13.3333, -72.0833),  # Ollantaytambo
    (-13.3167, -72.1167)   # Pisac
]
```

Agrega una coordenada para Sacsayhuamán (-13.5090, -71.9820) y muestra todas las coordenadas.

---

## Lo que aprendiste

- Las **listas** son colecciones ordenadas y mutables de elementos
- Se accede a los elementos con índices (empiezan en 0)
- El **slicing** también funciona con listas
- Las **tuplas** son inmutables (no se pueden modificar)
- **Métodos de listas**: `.append()`, `.remove()`, `.sort()`, `.reverse()`, `.pop()`, `.index()`, `.count()`
- Las listas pueden contener cualquier tipo, incluyendo otras listas
- `len()` funciona con listas

Wayra cerró su laptop. Tenía una lista de sospechosos, una lista de evidencias, y un montón de datos que organizar. Pero lo que más le preocupaba era algo que había notado en los registros de acceso del laboratorio.

—Raúl —dijo—. Los registros muestran que alguien accedió al sistema a las 2:34 a.m. La entrada dice "Lara Mamani". Pero a las 2:34 a.m., el sistema de seguridad de Lara en su departamento registró su huella digital... a 15 kilómetros de distancia.

—¿Entonces...?

—Alguien usó su cuenta. Alguien que conocía su contraseña. Y hay solo dos personas que conocían la contraseña de Lara: ella misma... y el Dr. Inti Quispe.

---
