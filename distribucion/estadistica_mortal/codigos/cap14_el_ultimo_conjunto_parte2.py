"""
Capítulo 14: El Último Conjunto (Parte 2)
Cierre del caso, simulación contrafactual
"""
import random
from collections import Counter

# Simulación contrafactual
print("=== SIMULACION CONTRAFACTUAL ===")
print("Escenario: Kamila Huaman no es asesinada\n")

resultados = []
for simulacion in range(1000):
    random.seed(simulacion)
    p_publicacion = 0.95
    p_investigacion = 0.80
    p_condena = 0.60
    p_reforma = 0.30

    if random.random() < p_publicacion:
        if random.random() < p_investigacion:
            if random.random() < p_condena:
                if random.random() < p_reforma:
                    resultados.append('Reforma del sistema')
                else:
                    resultados.append('Condena sin reforma')
            else:
                resultados.append('Investigacion sin condena')
        else:
            resultados.append('Publicacion sin investigacion')
    else:
        resultados.append('Nunca se publica')

conteo = Counter(resultados)
print("Resultados de 1000 simulaciones:")
for resultado, count in conteo.most_common():
    print(f"  {resultado}: {count} ({count/10:.1f}%)")
