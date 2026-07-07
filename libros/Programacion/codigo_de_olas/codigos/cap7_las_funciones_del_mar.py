"""Capitulo 7: Las Funciones del Mar
Conceptos: Funciones, parametros, return, alcance de variables
"""

# ============================================
# FUNCIONES DEL GENERADOR
# ============================================

# Funcion basica sin parametros
def mostrar_bienvenida():
    print("=" * 40)
    print("GENERADOR DE OLAS - SISTEMA LOCUENTO")
    print("=" * 40)

mostrar_bienvenida()

# Parametros: Las variables de la ola
def generar_ola(altura, frecuencia):
    """Genera una ola con los parametros especificados."""
    print(f"\n  ~ OLA GENERADA:")
    print(f"     Altura: {altura} metros")
    print(f"     Frecuencia: {frecuencia} segundos")
    print(f"     Tipo: {'Anomala' if altura > 2.0 else 'Normal'}")

generar_ola(1.8, 12)
generar_ola(2.4, 8)
generar_ola(0.5, 20)

# Parametros por defecto
def crear_parte_olas(playa="Ancon", altura_promedio=1.5, temperatura=18.0):
    """Crea un parte de olas con valores por defecto."""
    print(f"\n=== PARTE DE OLAS: {playa.upper()} ===")
    print(f"Altura promedio: {altura_promedio}m")
    print(f"Temperatura: {temperatura}C")
    print(f"Recomendacion: {'Ideal para surf' if altura_promedio >= 1.0 and altura_promedio <= 2.5 else 'Precaucion'}")

crear_parte_olas()
crear_parte_olas("Miraflores", 2.0, 19.5)
crear_parte_olas("Punta Hermosa", altura_promedio=2.8)

# Return: El resultado del mar
def analizar_ola(altura, frecuencia, direccion):
    """Analiza una ola y devuelve su clasificacion."""

    if altura > 2.0 and frecuencia < 10:
        return "OLA ANOMALA - Generada artificialmente"
    elif altura > 1.5:
        return "OLA GRANDE - Condicion natural"
    elif altura > 0.8:
        return "OLA MODERADA - Buena para surf"
    else:
        return "OLA PEQUENA - No recomendada"

# Usar la funcion
resultado_1 = analizar_ola(2.4, 8, "SO")
resultado_2 = analizar_ola(1.2, 15, "SO")

print(f"\nOla 1: {resultado_1}")
print(f"Ola 2: {resultado_2}")

# Multiples valores de retorno
def estadisticas_olas(alturas):
    """Calcula estadisticas de una lista de alturas de olas."""
    total = len(alturas)
    promedio = sum(alturas) / total if total > 0 else 0
    maxima = max(alturas) if alturas else 0
    minima = min(alturas) if alturas else 0

    return total, promedio, maxima, minima

# Desempaquetar el resultado
alturas_semana = [1.2, 1.8, 2.4, 1.5, 0.9, 2.1, 1.6]
total, prom, maxi, mini = estadisticas_olas(alturas_semana)

print(f"\n=== ESTADISTICAS SEMANALES ===")
print(f"Total de olas: {total}")
print(f"Altura promedio: {prom:.1f}m")
print(f"Ola mas alta: {maxi}m")
print(f"Ola mas baja: {mini}m")

# --- FIRMWARE DEL GENERADOR LOCUENTO ---

def generar_ola_anomala(altura, frecuencia, codigo):
    """Genera una ola anomala que codifica un mensaje."""
    ola = {
        "altura": altura,
        "frecuencia": frecuencia,
        "codigo": codigo,
        "tipo": "anomala"
    }
    print(f"  Antenna Transmitiendo codigo '{codigo}' en ola de {altura}m")
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
    """Transmite un mensaje completo usando olas anomalas."""
    print(f"\n=== TRANSMITIENDO: '{mensaje}' ===\n")
    frecuencias = codificar_mensaje(mensaje)

    olas_transmitidas = []
    for i, codigo in enumerate(frecuencias):
        altura = altura_base + (i * 0.1)
        ola = generar_ola_anomala(altura, codigo, codigo)
        olas_transmitidas.append(ola)

    return olas_transmitidas

# Probar la transmision
mensaje_secreto = "LOCUENTO"
olas = transmitir_mensaje(mensaje_secreto)
print(f"\nTotal de olas transmitidas: {len(olas)}")

# Alcance de variables: El mundo de cada funcion
# Variable global
playa_principal = "Ancon"

def cambiar_playa():
    # Variable local
    playa_temporal = "Miraflores"
    print(f"Dentro de la funcion: playa temporal = {playa_temporal}")

    # Para modificar la global, necesitamos 'global'
    global playa_principal
    playa_principal = "Punta Hermosa"
    print(f"Dentro de la funcion: global cambiada a {playa_principal}")

cambiar_playa()
print(f"Fuera de la funcion: playa principal = {playa_principal}")

# print(playa_temporal)  # !Error! No existe fuera

# --- ENIGMAS ---

print("\n=== ENIGMA 7.1: Tu primera funcion ===")
def recomendar_traje(temp):
    if temp < 16:
        return "Traje de neopreno 5/4mm"
    elif temp <= 20:
        return "Traje corto"
    else:
        return "Solo shorts"

print(f"Temp 14C: {recomendar_traje(14)}")
print(f"Temp 18C: {recomendar_traje(18)}")
print(f"Temp 22C: {recomendar_traje(22)}")

print("\n=== ENIGMA 7.2: Calculadora de distancia ===")
def distancia_buceo(minutos, ritmo=10):
    return minutos * ritmo

print(f"10 min a ritmo 10: {distancia_buceo(10)}m")
print(f"30 min a ritmo 15: {distancia_buceo(30, 15)}m")

print("\n=== ENIGMA 7.3: Valores por defecto ===")
def alerta_ola(altura=1.5, peligro=False):
    if peligro:
        print(f"! ALERTA! Ola de {altura}m - PELIGROSA")
    else:
        print(f"Ola de {altura}m - Sin peligro")

alerta_ola()
alerta_ola(2.5, True)

print("\n=== ENIGMA 7.4: Multiples retornos ===")
def info_playa(nombre, tiene_muelle, tiene_estacionamiento):
    puntuacion = sum([tiene_muelle, tiene_estacionamiento])
    recomendacion = "Recomendada" if puntuacion >= 2 else "Basica"
    return puntuacion, recomendacion

p, r = info_playa("Ancon", True, True)
print(f"Playa Ancon - Puntuacion: {p}, Recomendacion: {r}")
