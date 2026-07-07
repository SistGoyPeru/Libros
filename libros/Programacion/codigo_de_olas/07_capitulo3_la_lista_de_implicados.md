# Capítulo 3: La Lista de Implicados

## Conceptos: Listas, tuplas, indexing, métodos de listas

---

Mateo necesitaba organizar la información. Tenía datos sueltos: nombres, lugares, frecuencias, coordenadas. Pero todo estaba desordenado.

—El mar es una lista de olas —dijo Rafa, que había llegado a ayudarlo—. Cada ola es un elemento. Tiene un orden, una posición.

—Exacto —respondió Mateo—. Y en Python, eso se llama una **lista**.

## Listas: Las olas del océano de datos

Una **lista** es una colección ordenada de elementos. Como las olas en el mar: cada una tiene su lugar, su momento, su dato.

```python
# ============================================
# LISTA DE IMPLICADOS EN EL CASO
# ============================================

# Personas relacionadas al proyecto LOCUENTO
implicados = [
    "Carlos Parra (Ingeniero Naval)",
    "Dra. Luisa Rivas (Bióloga Marina)",
    "Miguel Ángel Soto (Empresario)",
    "Capitán Paredes (Capitanía del Puerto)",
    "Rafa (testigo)"
]

print("=== IMPLICADOS EN EL CASO ===")
print(implicados)
print(f"Total de implicados: {len(implicados)}")
```

### Accediendo a elementos

Cada elemento tiene una posición (índice), igual que en los strings:

```python
print(f"\nPrimer implicado: {implicados[0]}")
print(f"Último implicado: {implicados[-1]}")
print(f"Los 3 primeros: {implicados[:3]}")
print(f"Los 2 últimos: {implicados[-2:]}")
```

### Listas de listas: Datos anidados

Cada persona tiene múltiples datos. Mateo creó una lista de listas:

```python
# [nombre, edad, rol, sabe_del_generador, nivel_confianza]
fichas_implicados = [
    ["Carlos Parra", 45, "Ingeniero Naval", True, 8],
    ["Luisa Rivas", 38, "Bióloga Marina", False, 6],
    ["Miguel Ángel Soto", 62, "Empresario", True, 9],
    ["Capitán Paredes", 55, "Capitanía del Puerto", False, 4],
    ["Rafa", 29, "Amigo / Testigo", True, 10],
]

print("\n=== FICHAS COMPLETAS ===")
for ficha in fichas_implicados:
    print(f"Nombre: {ficha[0]:30} | Edad: {ficha[1]} | Confianza: {ficha[4]}/10")
```

## Tuplas: Datos fijos del mar

Hay datos que no cambian. Las coordenadas geográficas, por ejemplo. Para eso están las **tuplas**:

```python
# --- TUPLAS: DATOS INMUTABLES ---

# Coordenadas de Ancón (no cambian)
coordenadas_ancón = (-11.7758, -77.1897)
print(f"\nCoordenadas de Ancón: {coordenadas_ancón}")
print(f"Latitud: {coordenadas_ancón[0]}")
print(f"Longitud: {coordenadas_ancón[1]}")

# Puntos de monitoreo (tuplas fijas)
puntos_monitoreo = [
    (-11.7730, -77.1880),
    (-11.7760, -77.1900),
    (-11.7780, -77.1870),
    (-11.7740, -77.1850)
]

print(f"\nPuntos de monitoreo: {len(puntos_monitoreo)}")
for i, punto in enumerate(puntos_monitoreo, 1):
    print(f"  Punto {i}: ({punto[0]}, {punto[1]})")
```

## Métodos de listas: Manipulando la red

Mateo necesitaba herramientas para gestionar su lista de implicados:

```python
# --- MÉTODOS DE LISTAS ---
print("\n=== MANIPULANDO LA LISTA ===")

# .append() - Agregar
implicados.append("Desconocido (operador del generador)")
print(f"Agregado: {implicados}")

# .remove() - Eliminar
implicados.remove("Rafa (testigo)")
print(f"Sin Rafa (es amigo, no implicado): {implicados}")

# .sort() - Ordenar
implicados.sort()
print(f"Ordenados alfabéticamente: {implicados}")

# .reverse() - Invertir
implicados.reverse()
print(f"Orden inverso: {implicados}")

# .pop() - Extraer el último
ultimo = implicados.pop()
print(f"Extraído: {ultimo}")

# .index() - Buscar posición
if "Carlos Parra (Ingeniero Naval)" in implicados:
    pos = implicados.index("Carlos Parra (Ingeniero Naval)")
    print(f"Carlos Parra está en posición: {pos}")

# .count() - Contar
print(f"Total actual: {len(implicados)}")
```

## Evidencias del caso

Mateo organizó toda la evidencia recolectada:

```python
# --- EVIDENCIAS ---

evidencias_tecnicas = [
    "Patrón de olas anómalas cada 3 horas",
    "Coordenadas del generador submarino",
    "Mensaje cifrado: 'MAR CONTAMINADO'",
    "Nombre del proyecto: LOCUENTO",
    "Frecuencias convertidas a letras"
]

testigos = [
    "Rafa (vio el generador desde su bote)",
    "Pescadores locales (oyeron ruido submarino)",
    "Capitán Paredes (recibió quejas)"
]

sospechosos_directos = [
    "Miguel Ángel Soto (financia el proyecto)",
    "Carlos Parra (diseñó el generador)",
]

print("\n=== EVIDENCIA DEL CASO ===")
print(f"\nEvidencias técnicas ({len(evidencias_tecnicas)}):")
for e in evidencias_tecnicas:
    print(f"  • {e}")

print(f"\nTestigos ({len(testigos)}):")
for t in testigos:
    print(f"  • {t}")

print(f"\nSospechosos directos ({len(sospechosos_directos)}):")
for s in sospechosos_directos:
    print(f"  • {s}")
```

## El dato que cambió todo

Al revisar los datos del parte de olas, Mateo notó una lista de frecuencias que no había procesado:

```python
# --- FRECUENCIAS DE OLAS ANÓMALAS ---

frecuencias_anomalas = [12, 15, 9, 21, 5, 14, 20, 15]

print(f"\nFrecuencias anómalas: {frecuencias_anomalas}")
print(f"Promedio: {sum(frecuencias_anomalas) / len(frecuencias_anomalas):.1f}")
print(f"Máxima: {max(frecuencias_anomalas)}")
print(f"Mínima: {min(frecuencias_anomalas)}")

# ¿Patrón en las frecuencias?
for i in range(len(frecuencias_anomalas) - 1):
    diferencia = frecuencias_anomalas[i+1] - frecuencias_anomalas[i]
    print(f"Diferencia entre {i+1} y {i+2}: {diferencia}")
```

El patrón era claro: las diferencias no eran constantes. No era una progresión aritmética. Era un mensaje codificado.

## Enigmas

### Enigma 3.1: Tu lista de playas

Crea una lista `playas_de_lima` con: "Ancón", "Miraflores", "Barranco", "La Punta", "Costa Verde". Luego:
- Agrega "Santa María"
- Ordena la lista
- Muestra el total
- Muestra la primera y la última

### Enigma 3.2: Matriz de accesos

Crea una matriz (lista de listas) con los accesos a la playa:

```
["Ancón", True, True, "Estacionamiento"]
["Miraflores", True, False, "Parque"]
["Barranco", True, True, "Escaleras"]
```

Muestra qué playas tienen acceso para discapacitados (columna 2).

### Enigma 3.3: Tuplas de coordenadas de playas

Crea una lista de tuplas con las coordenadas de 3 playas de Lima (búscalas en Google Maps o inventa). Luego itera sobre ellas mostrando: "Playa en latitud X, longitud Y".

---

## Lo que aprendiste

- Las **listas** son colecciones ordenadas y mutables de elementos
- Se accede con índices (empiezan en 0)
- Las **tuplas** son inmutables
- **Métodos**: `.append()`, `.remove()`, `.sort()`, `.reverse()`, `.pop()`, `.index()`
- `sum()`, `max()`, `min()` funcionan con listas numéricas

Mateo cerró el archivo. Tenía una lista de implicados, evidencias organizadas, y un patrón de frecuencias que mostraba un mensaje. Pero el mensaje completo necesitaba algo más: necesitaba relacionar cada frecuencia con una persona, un lugar, un motivo.

Necesitaba un **diccionario**.

---
