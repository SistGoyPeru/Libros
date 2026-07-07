# Apéndice: Soluciones a los Enigmas

## Capítulo 1: El Conjunto Vacío

### Enigma 1.1
```python
edades = [29, 34, 45, 45, 45, 52, 67, 71, 34, 29, 45, 38, 52, 45, 29]

media = sum(edades) / len(edades)
# media = 43.07

edades.sort()
mediana = edades[len(edades)//2]
# mediana = 45

from collections import Counter
moda = Counter(edades).most_common(1)[0]
# moda = 45 (aparece 5 veces)

minimo = min(edades)  # 29
maximo = max(edades)  # 71
```

### Enigma 1.2
```python
edades.append(98)
media = sum(edades) / len(edades)  # 46.44 (aumentó)
edades.sort()
mediana = edades[len(edades)//2]  # 45 (igual)
```
La **media** se ve afectada por el valor extremo (outlier). La **mediana** es robusta y no cambia.

### Enigma 1.3
Porcentaje = 5/47 × 100 = 10.6%. Los valores de presión sanguínea faltantes podrían ocultar que los pacientes con presión alta fueron excluidos del estudio para sesgar los resultados.

---

## Capítulo 2: La Probabilidad del Crimen

### Enigma 2.1
Probabilidad teórica: 1/6 ≈ 0.1667 por cada cara.
Las frecuencias observadas se desvían de lo esperado (100 por cara). El 6 aparece solo 72 veces, mucho menos de lo esperado.

### Enigma 2.2
1. P(acceso) = 3/8 = 0.375
2. P(motivo) = 4/8 = 0.5
3. P(ambos) = 2/8 = 0.25

### Enigma 2.3
```python
import random
caras = sum(1 for _ in range(10000) if random.random() < 0.5)
print(f"Caras: {caras}, Prob: {caras/10000:.4f}")
# Debería obtener ~0.5
```

---

## Capítulo 3: El Teorema del Sospechoso

### Enigma 3.1
P(fraude) = 0.005, P(positivo|fraude) = 0.99, P(positivo|no fraude) = 0.01
P(positivo) = 0.99×0.005 + 0.01×0.995 = 0.0149
P(fraude|positivo) = 0.99×0.005/0.0149 = 0.332 = 33.2%

### Enigma 3.2
P(enfermedad) = 0.02, P(positivo|enfermedad) = 0.98, P(positivo|sano) = 0.02
P(positivo) = 0.98×0.02 + 0.02×0.98 = 0.0392
P(enfermedad|positivo) = 0.98×0.02/0.0392 = 0.50 = 50%
La probabilidad es baja porque la enfermedad es rara y hay muchos falsos positivos.

### Enigma 3.3
Sofía subiría significativamente porque tiene baja estatura. Hugo y Ramiro bajarían.

---

## Capítulo 4: La Distribución del Engaño

### Enigma 4.1
media = 45, σ = 10
Z(23) = (23-45)/10 = -2.2 (no outlier)
Z(81) = (81-45)/10 = 3.6 (outlier)
Z(18) = -2.7 (no outlier)
Z(78) = 3.3 (outlier)

### Enigma 4.2
1. 68% (entre μ±1σ)
2. 95% (entre μ±2σ)
3. 99.7% (entre μ±3σ)

### Enigma 4.3
Conjunto B parece manipulado: casi no tiene variabilidad (desviación estándar mucho menor que el conjunto A).

---

## Capítulo 5: La Muestra que Miente

### Enigma 5.1
1. Sesgo de disponibilidad (solo personas en casa de día)
2. Sesgo de selección (solo jóvenes sanos)
3. Sesgo de respuesta (solo extremos responden)
4. Sesgo de supervivencia (solo los que declaran impuestos)

### Enigma 5.2
ME = 1/√400 = 0.05 = 5%
IC 95%: [52% - 5%, 52% + 5%] = [47%, 57%]

### Enigma 5.3
Muestreo estratificado por facultad, con muestra proporcional al tamaño de cada facultad.

---

## Capítulo 6: La Hipótesis Asesina

### Enigma 6.1
Simular 10000 experimentos de 20 lanzamientos de moneda justa. Contar cuántas veces se obtienen 15 o más caras. Ese conteo/10000 es el valor p.

### Enigma 6.2
1. Falso positivo = Error Tipo I
2. Error Tipo II
3. Depende del contexto. En enfermedades mortales, el Error Tipo II (no detectar) puede ser más peligroso.

### Enigma 6.3
H₀: Sitio A = Sitio B; H₁: Sitio A ≠ Sitio B. Media A = 2.31s, Media B = 3.0s. La diferencia es significativa.

---

## Capítulo 7: La Correlación del Secreto

### Enigma 7.1
r ≈ 0.998. Correlación positiva casi perfecta.

### Enigma 7.2
Ejemplos:
- Ventas de helados y ahogados (variable oculta: calor)
- Número de iglesias y crímenes (población)
- Consumo de chocolate y premios Nobel (desarrollo económico)

### Enigma 7.3
Incluir a Lidia probablemente no cambia drásticamente la interpretación.

---

## Capítulo 8: La Regresión del Pasado

### Enigma 8.1
Pendiente ≈ 0.73, Intercepto ≈ 2.47. Para 7.5h: nota ≈ 7.95. R² ≈ 0.99.

### Enigma 8.2
El conjunto B parece manipulado porque los valores tienen más variabilidad pero siguen un patrón menos natural.

### Enigma 8.3
Mes 25: 2.80 × 15 + 14.20 = 56.2; Mes 26: 2.80 × 16 + 14.20 = 59.0

---

## Capítulo 9: El Intervalo de Confianza

### Enigma 9.1
EE = 800/√100 = 80. IC 95%: [2500 - 1.96×80, 2500 + 1.96×80] = [2343.2, 2656.8]

### Enigma 9.2
n = (1.96 × 800 / 100)² ≈ 246. Necesitamos al menos 246 personas.

### Enigma 9.3
Distancia desde Andahuaylas: 30-60 km/h × 6h = 180-360 km. Destinos probables: Ayacucho (130 km), Nazca (280 km).

---

## Capítulo 10: La Varianza del Silencio

### Enigma 10.1
media = 24.625, varianza = 87.98, desv_std ≈ 9.38

### Enigma 10.2
CV(A) = 1.63%, CV(B) = 42.86%. B tiene mucha mayor dispersión relativa.

### Enigma 10.3
El estudio X parece manipulado (CV muy bajo, casi sin variabilidad). El estudio Y tiene variabilidad natural.

---

## Capítulo 11: La Prueba del Chi-Cuadrado

### Enigma 11.1
Frecuencias esperadas: Hombres A=105, Mujeres A=95; Hombres B=105, Mujeres B=95.
χ² ≈ 6.12. gl = 1. Valor crítico = 3.84. χ² > 3.84 → hay relación.

### Enigma 11.2
Esperado: 20 por cara. χ² = (25-20)²/20 + ... = 3.5. gl = 5. Valor crítico = 11.07. 3.5 < 11.07 → el dado no está cargado.

### Enigma 11.3
χ² aumentaría significativamente. El Ministro (8 nocturnos, 12 diurnos) tiene una proporción nocturna del 40%, mayor incluso que el Viceministro.

---

## Capítulo 12: La Serie del Tiempo Perdido

### Enigma 12.1
Tendencia: ligeramente decreciente. Estacionalidad: 12 meses. Media móvil 3: [23.3, 25, 26.7, 27.7, 26.7, 25.3, 24, 23, 22, 21, 21, 21].

### Enigma 12.2
Predicción: 96 (sigue la tendencia lineal de +4 por mes).

### Enigma 12.3
El cambio estructural ocurre en el mes 10-11 (salto de 36 a 50).

---

## Capítulo 13: El Último Conjunto (Parte 1)

### Enigma 13.1
χ² combinado = -2(ln(0.02)+ln(0.03)+ln(0.04)) = -2(-3.91-3.51-3.22) = 21.28. gl = 6. p < 0.01 → Sí, hay un efecto combinado.

---

## Capítulo 14: El Último Conjunto (Parte 2)

### Enigma 14.2
P(cárcel) = 0.70 × 0.40 = 0.28 = 28%

