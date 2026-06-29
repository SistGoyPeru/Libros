"""
Capítulo 12: La Serie del Tiempo Perdido
Series temporales, tendencia, estacionalidad, autocorrelación
"""
import numpy as np
import random
import math

# Serie temporal de ventas (36 meses)
random.seed(42)
ventas_totales = []
for mes in range(1, 37):
    tendencia = 50 + mes * 0.8
    estacionalidad = 5 * math.sin(mes * math.pi / 6)
    if mes <= 24:
        ruido = random.gauss(0, 3)
    else:
        tendencia += (mes - 24) * 3
        ruido = random.gauss(0, 1)
    ventas_totales.append(tendencia + estacionalidad + ruido)

print("=== SERIE TEMPORAL DE VENTAS ===")
for i in range(36):
    periodo = "LEGITIMO" if i < 24 else "MANIPULADO"
    if i < 3 or i >= 33:
        print(f"  Mes {i+1:<2}: {ventas_totales[i]:6.1f}  [{periodo}]")
print("  ...")

# Descomposición
def media_movil(datos, ventana):
    resultado = []
    for i in range(len(datos)):
        inicio = max(0, i - ventana // 2)
        fin = min(len(datos), i + ventana // 2 + 1)
        resultado.append(np.mean(datos[inicio:fin]))
    return resultado

tendencia = media_movil(ventas_totales, 12)

# Residuos
residuos = [ventas_totales[i] - tendencia[i] for i in range(36)]
media_legitimo = np.mean(residuos[:24])
media_manipulado = np.mean(residuos[24:])

print(f"\nMedia de residuos (legitimo): {media_legitimo:.2f}")
print(f"Media de residuos (manipulado): {media_manipulado:.2f}")
print(f"Diferencia: {media_manipulado - media_legitimo:.2f}")

# Autocorrelación
def autocorrelacion(datos, rezago):
    n = len(datos)
    x1 = np.array(datos[:n-rezago])
    x2 = np.array(datos[rezago:])
    return np.corrcoef(x1, x2)[0, 1]

print(f"\n=== AUTOCORRELACION ===")
for r in [1, 2, 3, 6, 12]:
    print(f"  Rezago {r}: {autocorrelacion(ventas_totales[:24], r):.3f} (legitimo)  "
          f"{autocorrelacion(ventas_totales[24:], r):.3f} (manipulado)")

# Proyección vs realidad
pendiente_leg = (np.mean(ventas_totales[12:24]) - np.mean(ventas_totales[:12])) / 12
intercepto_leg = np.mean(ventas_totales[:12])

print(f"\n=== PROYECCION VS REALIDAD ===")
diff_acum = 0
for i in range(24, 36):
    proy = intercepto_leg + pendiente_leg * (i + 1)
    real = ventas_totales[i]
    diff = real - proy
    diff_acum += diff
    print(f"  Mes {i+1}: Real={real:.0f}, Proy={proy:.0f}, Diff={diff:.0f}")

print(f"\nDiferencia acumulada: ${diff_acum*1000:.0f} en ingresos 'extra'")
