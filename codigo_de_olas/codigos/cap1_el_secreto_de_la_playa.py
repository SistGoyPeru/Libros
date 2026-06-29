"""Capítulo 1: El Secreto de la Playa
Conceptos: Variables, tipos de datos, print(), f-strings
"""

# ============================================
# OLA DIGITAL: ANALISIS DE PATRONES
# Surfista: Mateo Sanchez
# Fecha: 27 de junio, 2026
# ============================================

# --- DATOS DE LA OLA ---

nombre_playa = "Ancon"
hora_observacion = "06:15"
altura_ola = 1.8  # metros
frecuencia_ola = 12  # segundos entre olas
temperatura_agua = 18.5  # grados Celsius
direccion_viento = "sur-oeste"
es_anomalia = True

print("=== INFORME DE OLA ===")
print("Playa:", nombre_playa)
print("Hora:", hora_observacion)
print("Altura:", altura_ola, "metros")
print("Frecuencia:", frecuencia_ola, "segundos")
print("Anomalia detectada:", es_anomalia)

# f-strings
print(f"\n--- Resumen ---")
print(f"Playa {nombre_playa} a las {hora_observacion}")
print(f"Ola de {altura_ola}m cada {frecuencia_ola} segundos")
print(f"Anomalia? {es_anomalia}")

# --- TIPOS DE DATOS DE LA OLA ---

nombre_ola = "Ancon_01"          # str - texto
altura_maxima = 2.4               # float - decimal
frecuencia_segundos = 12          # int - entero
es_generada_artificialmente = True # bool - booleano (True/False)

print(f"\nOla: {nombre_ola}")
print(f"Tipo de nombre_ola: {type(nombre_ola)}")
print(f"Tipo de altura_maxima: {type(altura_maxima)}")
print(f"Tipo de frecuencia_segundos: {type(frecuencia_segundos)}")
print(f"Tipo de es_generada: {type(es_generada_artificialmente)}")

# --- PARTE DE OLAS DE ANCON ---

fecha_parte = "27-06-2026"
total_olas_registradas = 147
ola_mas_alta = 2.8
ola_promedio = 1.6
direccion_olas = "SO"

print(f"\n=== PARTE DE OLAS: {fecha_parte} ===")
print(f"Total de olas: {total_olas_registradas}")
print(f"Ola mas alta: {ola_mas_alta}m")
print(f"Promedio: {ola_promedio}m")
print(f"Direccion: {direccion_olas}")

# Porcentaje de olas anomalas
total_anomalias = 23
porcentaje = (total_anomalias / total_olas_registradas) * 100
print(f"Anomalias: {total_anomalias} ({porcentaje:.1f}%)")

# --- ENIGMAS ---

print("\n=== ENIGMA 1.1: Tu parte de olas ===")
nombre_playa_n = "Ancon Norte"
temperatura_agua_n = 19.2
altura_ola_n = 2.1
es_segura_n = True
hora_medicion_n = "07:30"
print(f"Playa: {nombre_playa_n}")
print(f"Temperatura: {temperatura_agua_n}C")
print(f"Altura: {altura_ola_n}m")
print(f"Segura: {es_segura_n}")
print(f"Hora: {hora_medicion_n}")

print("\n=== ENIGMA 1.2: Calcula el promedio ===")
alturas = [1.5, 2.0, 1.8, 2.2, 1.9]
promedio = sum(alturas) / len(alturas)
print(f"Alturas: {alturas}")
print(f"Promedio: {promedio:.2f}m")

print("\n=== ENIGMA 1.3: La ola binaria ===")
patron_binario = "1.8:0.5:2.1"
partes = patron_binario.split(":")
print(f"Patron: {patron_binario}")
print(f"Altura: {partes[0]}")
print(f"Frecuencia: {partes[1]}")
print(f"Velocidad: {partes[2]}")
