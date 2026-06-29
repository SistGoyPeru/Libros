"""
Capítulo 6: La Hipótesis Asesina
Prueba de hipótesis, valor p, significancia estadística
"""
import random

print("=== PRUEBA DE HIPOTESIS ===")
print("H0: Hugo Tupac NO accedio a los datos")
print("H1: Hugo Tupac SI accedio a los datos\n")

# Datos
total_accesos = 5000
accesos_ip_hugo = 78
accesos_nocturnos = 12
accesos_nocturnos_hugo = 5

print(f"Total accesos: {total_accesos}")
print(f"Accesos IP Hugo: {accesos_ip_hugo}")
print(f"Accesos nocturnos: {accesos_nocturnos}")
print(f"Nocturnos IP Hugo: {accesos_nocturnos_hugo}\n")

proporcion_ip_hugo = accesos_ip_hugo / total_accesos
esperados = proporcion_ip_hugo * accesos_nocturnos
print(f"Proporcion IP Hugo: {proporcion_ip_hugo:.4f}")
print(f"Esperados (si H0 cierta): {esperados:.2f}")
print(f"Observados: {accesos_nocturnos_hugo}\n")

# Simulación
random.seed(42)
simulaciones = 100000
resultados_extremos = 0

for _ in range(simulaciones):
    conteo_hugo = 0
    for _ in range(accesos_nocturnos):
        if random.random() < proporcion_ip_hugo:
            conteo_hugo += 1
    if conteo_hugo >= accesos_nocturnos_hugo:
        resultados_extremos += 1

p_valor = resultados_extremos / simulaciones
print(f"=== VALOR P ===")
print(f"Simulaciones: {simulaciones}")
print(f"Resultados extremos: {resultados_extremos}")
print(f"Valor p: {p_valor:.6f}")
print(f"Interpretacion: {'RECHAZAMOS H0' if p_valor < 0.05 else 'NO RECHAZAMOS H0'}")

# Errores
print(f"\n=== ERRORES EN PRUEBAS DE HIPOTESIS ===")
print(f"Error Tipo I: Rechazar H0 cuando es verdadera (falso positivo)")
print(f"Error Tipo II: No rechazar H0 cuando es falsa (falso negativo)")
print(f"α = 0.05 → 5% de probabilidad de error tipo I")
