"""
Capítulo 3: El Teorema del Sospechoso
Probabilidad condicional, Teorema de Bayes
"""

# Teorema de Bayes aplicado al caso
sospechosos = ['Ramiro', 'Hugo', 'Sofia', 'Desconocido']
prob_inicial = [0.25, 0.25, 0.25, 0.25]

print("Probabilidades iniciales (previas):")
for s, p in zip(sospechosos, prob_inicial):
    print(f"  {s}: {p:.2f}")

# Evidencia 1: Acceso biométrico
prob_acceso_dado_culpable = [1.0, 1.0, 1.0, 0.1]
prob_acceso_total = sum(p * pi for p, pi in zip(prob_acceso_dado_culpable, prob_inicial))

prob_posterior_acceso = [
    (p * pi) / prob_acceso_total
    for p, pi in zip(prob_acceso_dado_culpable, prob_inicial)
]

print("\nProbabilidades actualizadas (acceso biometrico):")
for s, p in zip(sospechosos, prob_posterior_acceso):
    print(f"  {s}: {p:.3f}")

# Evidencia 2: Manipulación de datos
prob_manipula_dado_culpable = [0.3, 0.7, 0.8, 0.2]
prob_manipula_total = sum(p * pp for p, pp in zip(prob_manipula_dado_culpable, prob_posterior_acceso))
prob_posterior_manipula = [
    (p * pp) / prob_manipula_total
    for p, pp in zip(prob_manipula_dado_culpable, prob_posterior_acceso)
]

print("\nProbabilidades (acceso + manipulacion):")
for s, p in zip(sospechosos, prob_posterior_manipula):
    print(f"  {s}: {p:.3f}")

# Evidencia 3: Desaparición
prob_desaparece_dado_culpable = [0.9, 0.1, 0.1, 0.5]
prob_desaparece_total = sum(p * pp for p, pp in zip(prob_desaparece_dado_culpable, prob_posterior_manipula))
prob_final = [
    (p * pp) / prob_desaparece_total
    for p, pp in zip(prob_desaparece_dado_culpable, prob_posterior_manipula)
]

print("\n=== PROBABILIDADES FINALES (Bayes) ===")
for s, p in sorted(zip(sospechosos, prob_final), key=lambda x: -x[1]):
    print(f"  {s}: {p:.3f} ({p*100:.1f}%)")

# Paradoja de la prueba
p_culpable = 0.01
precision_prueba = 0.95
p_positivo = (0.95 * 0.01) + (0.05 * 0.99)
p_culpable_dado_positivo = (0.95 * 0.01) / p_positivo
print(f"\nParadoja de la prueba:")
print(f"P(culpable | prueba positiva) = {p_culpable_dado_positivo:.3f} ({p_culpable_dado_positivo*100:.1f}%)")
