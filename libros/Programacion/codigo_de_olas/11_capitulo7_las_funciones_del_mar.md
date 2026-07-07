# Capítulo 7: Las Funciones del Mar

## Conceptos: Funciones, parámetros, `return`, alcance de variables

---

Mateo había logrado descargar el firmware del generador. Era un archivo Python. Alguien había programado todo el sistema en Python.

—Es hermoso —dijo, mientras abría el archivo—. El generador tiene funciones. Cada función controla un aspecto de las olas.

—¿Como qué? —preguntó Rafa.

—Como `generar_ola(altura, frecuencia)` o `enviar_mensaje(texto)`. El código está organizado en bloques reutilizables. Como las olas: cada una es única, pero todas siguen el mismo patrón.

## Funciones: El ritual del surfista

Una **función** es un bloque de código que realiza una tarea específica y puede reutilizarse. Como el ritual de un surfista antes de remar: siempre los mismos pasos, adaptados a cada ola.

```python
# ============================================
# FUNCIONES DEL GENERADOR
# ============================================

# Función básica sin parámetros
def mostrar_bienvenida():
    print("=" * 40)
    print("GENERADOR DE OLAS - SISTEMA LOCUENTO")
    print("=" * 40)

mostrar_bienvenida()
```

### Parámetros: Las variables de la ola

Los **parámetros** son los datos que recibe la función. Como la altura y frecuencia de una ola:

```python
def generar_ola(altura, frecuencia):
    """Genera una ola con los parámetros especificados."""
    print(f"\n  🌊 OLA GENERADA:")
    print(f"     Altura: {altura} metros")
    print(f"     Frecuencia: {frecuencia} segundos")
    print(f"     Tipo: {'Anómala' if altura > 2.0 else 'Normal'}")

generar_ola(1.8, 12)
generar_ola(2.4, 8)
generar_ola(0.5, 20)
```

### Parámetros por defecto

Algunos parámetros tienen valores que se usan la mayoría del tiempo:

```python
def crear_parte_olas(playa="Ancón", altura_promedio=1.5, temperatura=18.0):
    """Crea un parte de olas con valores por defecto."""
    print(f"\n=== PARTE DE OLAS: {playa.upper()} ===")
    print(f"Altura promedio: {altura_promedio}m")
    print(f"Temperatura: {temperatura}°C")
    print(f"Recomendación: {'Ideal para surf' if altura_promedio >= 1.0 and altura_promedio <= 2.5 else 'Precaución'}")

crear_parte_olas()
crear_parte_olas("Miraflores", 2.0, 19.5)
crear_parte_olas("Punta Hermosa", altura_promedio=2.8)
```

### Return: El resultado del mar

Las funciones no solo hacen cosas: también **devuelven** resultados:

```python
def analizar_ola(altura, frecuencia, direccion):
    """Analiza una ola y devuelve su clasificación."""
    
    if altura > 2.0 and frecuencia < 10:
        return "OLA ANÓMALA - Generada artificialmente"
    elif altura > 1.5:
        return "OLA GRANDE - Condición natural"
    elif altura > 0.8:
        return "OLA MODERADA - Buena para surf"
    else:
        return "OLA PEQUEÑA - No recomendada"

# Usar la función
resultado_1 = analizar_ola(2.4, 8, "SO")
resultado_2 = analizar_ola(1.2, 15, "SO")

print(f"\nOla 1: {resultado_1}")
print(f"Ola 2: {resultado_2}")
```

### Múltiples valores de retorno

Una función puede devolver varios valores como tupla:

```python
def estadisticas_olas(alturas):
    """Calcula estadísticas de una lista de alturas de olas."""
    total = len(alturas)
    promedio = sum(alturas) / total if total > 0 else 0
    maxima = max(alturas) if alturas else 0
    minima = min(alturas) if alturas else 0
    
    return total, promedio, maxima, minima

# Desempaquetar el resultado
alturas_semana = [1.2, 1.8, 2.4, 1.5, 0.9, 2.1, 1.6]
total, prom, maxi, mini = estadisticas_olas(alturas_semana)

print(f"\n=== ESTADÍSTICAS SEMANALES ===")
print(f"Total de olas: {total}")
print(f"Altura promedio: {prom:.1f}m")
print(f"Ola más alta: {maxi}m")
print(f"Ola más baja: {mini}m")
```

## Las funciones del generador LOCUENTO

Mateo encontró las funciones reales del generador en el firmware:

```python
# --- FIRMWARE DEL GENERADOR LOCUENTO ---

def generar_ola_anomala(altura, frecuencia, codigo):
    """Genera una ola anómala que codifica un mensaje."""
    ola = {
        "altura": altura,
        "frecuencia": frecuencia,
        "codigo": codigo,
        "tipo": "anómala"
    }
    print(f"  📡 Transmitiendo código '{codigo}' en ola de {altura}m")
    return ola

def codificar_mensaje(texto):
    """Convierte un texto en frecuencias de olas."""
    frecuencias = []
    for letra in texto.upper():
        if letra.isalpha():
            codigo = ord(letra) - 64  # A=1, B=2
            frecuencias.append(codigo)
    return frecuencias

def transmitir_mensaje(mensaje, altura_base=1.8):
    """Transmite un mensaje completo usando olas anómalas."""
    print(f"\n=== TRANSMITIENDO: '{mensaje}' ===\n")
    frecuencias = codificar_mensaje(mensaje)
    
    olas_transmitidas = []
    for i, codigo in enumerate(frecuencias):
        altura = altura_base + (i * 0.1)
        ola = generar_ola_anomala(altura, codigo, codigo)
        olas_transmitidas.append(ola)
    
    return olas_transmitidas

# Probar la transmisión
mensaje_secreto = "LOCUENTO"
olas = transmitir_mensaje(mensaje_secreto)
print(f"\nTotal de olas transmitidas: {len(olas)}")
```

## Alcance de variables: El mundo de cada función

Las variables dentro de una función no existen fuera de ella:

```python
# Variable global
playa_principal = "Ancón"

def cambiar_playa():
    # Variable local
    playa_temporal = "Miraflores"
    print(f"Dentro de la función: playa temporal = {playa_temporal}")
    
    # Para modificar la global, necesitamos 'global'
    global playa_principal
    playa_principal = "Punta Hermosa"
    print(f"Dentro de la función: global cambiada a {playa_principal}")

cambiar_playa()
print(f"Fuera de la función: playa principal = {playa_principal}")

# print(playa_temporal)  # ¡Error! No existe fuera
```

## Enigmas

### Enigma 7.1: Tu primera función

Escribe `recomendar_traje(temp)` que reciba la temperatura del agua y devuelva:
- Si temp < 16: "Traje de neopreno 5/4mm"
- Si 16 <= temp <= 20: "Traje corto"
- Si temp > 20: "Solo shorts"

### Enigma 7.2: Calculadora de distancia

Crea `distancia_buceo(minutos, ritmo=10)` donde `ritmo` es metros por minuto. Devuelve la distancia recorrida.

### Enigma 7.3: Valores por defecto

Crea una función `alerta_ola(altura=1.5, peligro=False)` que muestre un mensaje diferente si `peligro` es True.

### Enigma 7.4: Múltiples retornos

Crea una función `info_playa(nombre, tiene_muelle, tiene_estacionamiento)` que devuelva una tupla con la puntuación (suma de facilities) y la recomendación.

---

## Lo que aprendiste

- **`def nombre_funcion():`** define una función
- Los **parámetros** son los datos de entrada
- **Valores por defecto** hacen parámetros opcionales
- **`return`** devuelve uno o más valores
- **Ámbito (scope)**: variables locales vs. globales
- `global` modifica variables globales dentro de funciones

Mateo había descubierto cómo funcionaba el generador. Cada ola anómala era una función ejecutándose. Cada mensaje era un conjunto de datos transmitidos.

—Pero esto no es todo —dijo—. El generador guarda registros. Bitácoras. Archivos con datos históricos. Si puedo acceder a esos **archivos**, puedo encontrar quién programó todo esto.

---
