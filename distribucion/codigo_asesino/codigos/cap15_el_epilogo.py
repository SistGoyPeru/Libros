"""
Código Asesino: El Enigma de Qhapaq Ñan
Capítulo 15 - El Epílogo: La Verdad del Quipu Blanco
Proyecto Integrador: Decodificación final del quipu de Inti
Autor: Alex Goyzueta Delgado
"""

# ============================================
# EL ÚLTIMO CÓDIGO: DECODIFICANDO EL QUIPUS
# ============================================

print("=== DECODIFICANDO EL QUIPUS FINAL DE INTI ===\n")

# El quipus de Inti: nudos hacia derecha (1) e izquierda (0)
quipu_final = {
    "cuerda_1": "1011",
    "cuerda_2": "0001",
    "cuerda_3": "1110",
    "cuerda_4": "1010",
    "cuerda_5": "1101",
}

# Convertir binario a texto
for cuerda, binario in quipu_final.items():
    decimal = int(binario, 2)
    letra = chr(decimal + 64)  # A=1, B=2, etc.
    print(f"  {cuerda}: {binario} → {decimal:2} → '{letra}'")

# Mensaje completo
mensaje = ""
for cuerda, binario in quipu_final.items():
    decimal = int(binario, 2)
    mensaje += chr(decimal + 64)

print(f"\n  ► Mensaje completo: {mensaje}")

# Clave del quipu blanco original: [1,3,5,7,9,11]
clave_quipu_blanco = [1, 3, 5, 7, 9, 11]

print(f"\n  ► Aplicando clave del quipu blanco...")
mensaje_descifrado = ""
for i, letra in enumerate(mensaje):
    posicion_clave = clave_quipu_blanco[i] if i < len(clave_quipu_blanco) else 0
    nueva_pos = (ord(letra) - 65 + posicion_clave) % 26
    letra_descifrada = chr(nueva_pos + 65)
    mensaje_descifrado += letra_descifrada
    print(f"  {letra} + {posicion_clave} → {letra_descifrada}")

print(f"\n  ★ MENSAJE DESCIFRADO: {mensaje_descifrado} ★")

# --- CUERDAS SECUNDARIAS ---
quipu_secundario = {
    "sec_1": "1001",
    "sec_2": "0101",
    "sec_3": "1000",
    "sec_4": "1111",
    "sec_5": "0110",
}

print("\n=== CUERDAS SECUNDARIAS ===\n")

mensaje_completo = mensaje_descifrado
for cuerda, binario in quipu_secundario.items():
    decimal = int(binario, 2)
    letra = chr(decimal + 64)
    mensaje_completo += letra
    print(f"  {cuerda}: {binario} → {decimal:2} → '{letra}'")

print(f"\n  ► Mensaje extendido: {mensaje_completo}")

# Aplicar clave completa (impares + pares)
print(f"\n  ► Aplicando clave completa...\n")
clave_extendida = clave_quipu_blanco + [2, 4, 6, 8, 10]
resultado_final = ""
for i, letra in enumerate(mensaje_completo):
    if i < len(clave_extendida):
        nueva_pos = (ord(letra) - 65 + clave_extendida[i]) % 26
        letra_final = chr(nueva_pos + 65)
        resultado_final += letra_final
        print(f"  {letra} + {clave_extendida[i]} → {letra_final}")
    else:
        resultado_final += letra

print(f"\n  ★ {resultado_final} ★")
print(f"\n  El quipu revela el nombre de la guardiana: MAMA KILLA")
print(f"  Ella no era la asesina. Era la protectora del legado de Inti.")
