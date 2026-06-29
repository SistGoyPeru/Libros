"""
Capítulo 13: El Último Conjunto (Parte 1)
Combinación de Fisher, integración de pruebas
"""
import math

# Valores p de cada evidencia independiente
valores_p = [1e-10, 1e-8, 1e-12, 1e-6, 1e-9, 0.0001]

# Combinación de Fisher
chi2_combinado = -2 * sum(math.log(p) for p in valores_p)
grados_libertad = 2 * len(valores_p)

print("=== PROBABILIDAD COMBINADA (Fisher) ===")
print(f"Numero de pruebas: {len(valores_p)}")
print(f"Chi-cuadrado combinado: {chi2_combinado:.2f}")
print(f"Grados de libertad: {grados_libertad}")
print()
print("Interpretacion: la probabilidad de que TODAS estas")
print(f"evidencias sean coincidencias es p < 10^{-int(chi2_combinado/2)}")

# Documentación del caso (método científico)
print("\n" + "="*60)
print("INFORME FINAL: CASO KAMILA HUAMAN")
print("="*60)

print("\n1. OBSERVACION")
print("  Dra. Kamila Huaman aparece muerta en su laboratorio")
print("  Computadora muestra: datos = []")

print("\n2. PREGUNTA")
print("  ¿Los datos del ensayo clinico G-472 fueron manipulados?")

print("\n3. HIPOTESIS")
print("  H0: Los datos son legitimos")
print("  H1: Los datos fueron manipulados")

print("\n4. ANALISIS ESTADISTICO")
analisis = [
    "Z-score de 11.5 en datos clave (imposible bajo H0)",
    "Valores p < 0.00001 en todas las pruebas",
    "Bayes: P(culpable|evidencia) > 0.85",
    "Correlacion: r = 0.87 entre accesos y manipulacion",
    "Chi-cuadrado: χ² = 117.82, gl = 4",
    "Regresion: cambio de pendiente de 0.8 a 3.8",
    "Series temporales: residuos sistematicos de 11.74"
]
for a in analisis:
    print(f"  • {a}")

print("\n5. CONCLUSION")
print("  SE RECHAZA H0: los datos fueron manipulados")
print("  Responsable: Ministro de Salud")
print("  Beneficio estimado: $3.2 millones")
