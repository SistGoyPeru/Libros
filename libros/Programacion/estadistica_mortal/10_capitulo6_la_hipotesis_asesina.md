# Capítulo 6: La Hipótesis Asesina

## Conceptos: Prueba de hipótesis, hipótesis nula y alternativa, valor p, significancia estadística

---

Ramiro trabajó toda la noche. Cuando Valeria y Marco llegaron al local de reparaciones a la mañana siguiente, lo encontraron dormido sobre el teclado, con una taza de café volcada a su lado.

—¿Lo lograste? —preguntó Valeria.

Ramiro levantó la cabeza lentamente, con los ojos rojos.

—Sí. Pero no me gusta lo que encontré.

—¿Qué es?

—Los logs completos del ministerio. 5,000 registros. Y una IP que aparece repetidamente en los momentos clave.

—¿Cuál IP?

—172.16.0.1. Es la IP del ICD. Del servidor interno.

—¿Del ICD? —preguntó Marco—. ¿Alguien dentro del ICD accedió a los datos del ministerio?

—No solo accedió —dijo Ramiro—. Modificó archivos. Borró registros. Y todo ocurrió entre las 2 y las 4 a.m. de la noche en que Kamila murió.

—¿Puedes identificar al usuario?

—No. La conexión usaba credenciales genéricas. Pero hay algo más.

—¿Qué?

—La IP 172.16.0.1 es la del despacho del director.

El silencio se instaló en la habitación. Marco palideció.

—Mi padre —dijo en voz baja.

—O alguien que usó su computadora —corrigió Valeria—. Aún no tenemos pruebas suficientes.

—¿Cómo vamos a obtenerlas?

—Con una **prueba de hipótesis**.

---

## La hipótesis nula y la alternativa

—En estadística —explicó Valeria—, cuando queremos probar algo, formulamos dos hipótesis:

1. **Hipótesis nula (H₀)**: lo que asumimos que es verdad por defecto. "No hay efecto", "no hay diferencia", "todo es normal".
2. **Hipótesis alternativa (H₁)**: lo que queremos demostrar. "Hay un efecto", "hay una diferencia", "algo está mal".

—En nuestro caso:

- **H₀**: El Dr. Hugo Tupac no accedió a los datos del ministerio esa noche
- **H₁**: El Dr. Hugo Tupac accedió a los datos del ministerio esa noche

—Pero no podemos probar H₁ directamente. Lo que hacemos es tratar de **rechazar H₀**. Si los datos son suficientemente inconsistentes con H₀, la rechazamos y aceptamos H₁.

—¿Y cómo sabemos si los datos son "suficientemente inconsistentes"?

—Con el **valor p** (p-value).

---

## El valor p

Valeria abrió Python:

```python
# Prueba de hipótesis aplicada al caso

import numpy as np
import random

# DATOS DEL CASO
# Queremos saber si Hugo Tupac es responsable de los accesos nocturnos

# Paso 1: Definir las hipótesis
print("=== PRUEBA DE HIPÓTESIS ===")
print("H₀: Hugo Tupac NO accedió a los datos")
print("H₁: Hugo Tupac SÍ accedió a los datos")
print()

# Paso 2: Recopilar evidencia
# Logs de acceso: 5000 registros
# Accesos desde la IP del despacho de Hugo: 78 (de 5000)
# Accesos nocturnos (2-4 a.m.) desde cualquier IP: 12
# Accesos nocturnos desde la IP de Hugo: 5

total_accesos = 5000
accesos_ip_hugo = 78
accesos_nocturnos = 12
accesos_nocturnos_hugo = 5

print(f"Total de accesos en logs: {total_accesos}")
print(f"Accesos desde IP de Hugo: {accesos_ip_hugo}")
print(f"Accesos nocturnos (2-4 a.m.): {accesos_nocturnos}")
print(f"Accesos nocturnos desde IP de Hugo: {accesos_nocturnos_hugo}")
print()

# Paso 3: Calcular la probabilidad esperada bajo H₀
# Si Hugo es inocente, los accesos nocturnos desde su IP deberían seguir
# la misma distribución que el resto de accesos

proporcion_ip_hugo = accesos_ip_hugo / total_accesos
print(f"Proporción de accesos desde IP de Hugo: {proporcion_ip_hugo:.4f}")
print(f"Esperados (si H₀ es cierta): {proporcion_ip_hugo * accesos_nocturnos:.2f} accesos nocturnos")
print(f"Observados: {accesos_nocturnos_hugo}")
print()

# Paso 4: Simular para obtener el valor p
# Bajo H₀, simulamos 10000 escenarios y vemos con qué frecuencia
# obtenemos 5 o más accesos nocturnos desde la IP de Hugo

random.seed(42)
simulaciones = 100000
resultados_extremos = 0

for _ in range(simulaciones):
    # Simulamos los 12 accesos nocturnos
    accesos_simulados = []
    for _ in range(accesos_nocturnos):
        if random.random() < proporcion_ip_hugo:
            accesos_simulados.append('hugo')
        else:
            accesos_simulados.append('otro')
    
    conteo_hugo = sum(1 for a in accesos_simulados if a == 'hugo')
    if conteo_hugo >= accesos_nocturnos_hugo:
        resultados_extremos += 1

p_valor = resultados_extremos / simulaciones
print(f"=== VALOR P ===")
print(f"Simulaciones: {simulaciones}")
print(f"Resultados extremos (>= {accesos_nocturnos_hugo}): {resultados_extremos}")
print(f"Valor p: {p_valor:.6f}")
print(f"Interpretación: {'RECHAZAMOS H₀' if p_valor < 0.05 else 'NO RECHAZAMOS H₀'}")
```

Resultado:

```
=== PRUEBA DE HIPÓTESIS ===
H₀: Hugo Tupac NO accedió a los datos
H₁: Hugo Tupac SÍ accedió a los datos

Total de accesos en logs: 5000
Accesos desde IP de Hugo: 78
Accesos nocturnos (2-4 a.m.): 12
Accesos nocturnos desde IP de Hugo: 5

Proporción de accesos desde IP de Hugo: 0.0156
Esperados (si H₀ es cierta): 0.19 accesos nocturnos
Observados: 5

=== VALOR P ===
Simulaciones: 100000
Resultados extremos (>= 5): 0
Valor p: 0.000000
Interpretación: RECHAZAMOS H₀
```

—El valor p es esencialmente 0 —dijo Valeria—. La probabilidad de haber observado 5 accesos nocturnos desde la IP de Hugo, si él fuera inocente, es prácticamente nula. Rechazamos la hipótesis nula.

—Eso significa... —Marco no podía terminar la frase.

—Significa que los datos apuntan a tu padre. Pero estadísticamente, esto no es una condena. Es una **evidencia**. Necesitamos más.

---

## La significancia estadística y los errores

—En las pruebas de hipótesis, hay dos errores posibles:

```python
print("=== ERRORES EN PRUEBAS DE HIPÓTESIS ===")
print()
print("ERROR TIPO I (Falso Positivo): Rechazar H₀ cuando es verdadera")
print("  → Decir que Hugo es culpable cuando es inocente")
print("  → Probabilidad = α (nivel de significancia, típicamente 0.05)")
print()
print("ERROR TIPO II (Falso Negativo): No rechazar H₀ cuando es falsa")
print("  → Decir que Hugo es inocente cuando es culpable")
print("  → Probabilidad = β")
print()
print(f"Nuestro valor p ({p_valor:.6f}) es menor que α (0.05)")
print(f"→ Rechazamos H₀ con 95% de confianza")
print(f"→ Pero hay 5% de probabilidad de que esto sea un falso positivo")
```

—Entonces, ¿hay un 5% de probabilidad de que mi padre sea inocente? —preguntó Marco.

—Si solo nos basáramos en esta prueba, sí. Pero la evidencia no termina aquí. Cuantas más pruebas independientes tengamos, más seguros podemos estar.

---

## La fuerza de la evidencia

Valeria continuó:

—En estadística, una prueba sola rara vez es concluyente. Pero cuando múltiples pruebas apuntan en la misma dirección, la evidencia se vuelve abrumadora.

```python
# Múltiples pruebas de hipótesis

print("=== MÚLTIPLES EVIDENCIAS ===")
print()

# Evidencia 1: Accesos nocturnos
p1 = 0.00001
print(f"Evidencia 1 (accesos nocturnos): valor p = {p1}")

# Evidencia 2: Manipulación de datos
# Los datos manipulados tienen una firma estadística
# Z-score de 11.5 es esencialmente imposible bajo H₀
p2 = 1e-30  # Aproximadamente 0
print(f"Evidencia 2 (manipulación datos): valor p ≈ {p2}")

# Evidencia 3: Desaparición de Ramiro
# Si Ramiro huyó porque tenía miedo de Hugo...
p3 = 0.15  # Débil, pero consistente
print(f"Evidencia 3 (desaparición Ramiro): valor p = {p3}")

# Evidencia 4: IP del despacho de Hugo
# La IP 172.16.0.1 está física en su despacho
p4 = 0.01  # Alguien más podría haber usado su computadora
print(f"Evidencia 4 (IP física en despacho): valor p = {p4}")

# Combinación: el producto de los valores p
# (Esto es una simplificación, el método correcto es Fisher)
import math
chi_cuadrado = -2 * sum(math.log(p) for p in [p1, p2, p3, p4])
print(f"\nEstadístico combinado (Fisher): {chi_cuadrado:.2f}")
print("Con 8 grados de libertad, valor p combinado < 0.00001")
print("→ La evidencia conjunta es abrumadora")
```

—Cuanto más evidencia reunimos, más se inclina la balanza —dijo Valeria—. Pero aún tenemos un problema.

—¿Cuál?

—No tenemos **prueba directa**. Tenemos correlación, tenemos probabilidades, tenemos valores p. Pero en un tribunal, necesitas más que estadísticas.

—¿Qué necesitamos?

—Algo que vincule directamente a Hugo con la manipulación. Un archivo. Un email. Una confesión.

—O un testigo —dijo Marco.

—O un testigo —repitió Valeria.

---

## Enigmas

### Enigma 6.1: Calcula el valor p

Lanzas una moneda 20 veces y obtienes 15 caras. ¿Es una moneda cargada?

1. H₀: la moneda es justa (P(cara) = 0.5)
2. H₁: la moneda está cargada hacia caras
3. Simula 10000 lanzamientos de 20 monedas justas
4. ¿Cuántas veces obtienes 15 o más caras?
5. ¿Cuál es el valor p?

### Enigma 6.2: Error tipo I y tipo II

Un test médico para detectar una enfermedad rara (0.1% de la población) tiene 99% de precisión:

1. Si el test da positivo, ¿cuál es la probabilidad de que sea un falso positivo (Error Tipo I)?
2. Si el test da negativo pero la persona tiene la enfermedad, ¿qué tipo de error es?
3. ¿Qué es más peligroso en este contexto?

### Enigma 6.3: Diseña tu propia prueba

Tienes datos de tiempos de respuesta (en segundos) de dos sitios web:

```python
sitio_A = [2.3, 2.1, 2.5, 2.2, 2.4, 2.0, 2.6, 2.3, 2.2, 2.5]
sitio_B = [3.1, 2.9, 3.3, 2.8, 3.0, 3.2, 2.7, 3.1, 2.9, 3.0]
```

1. Formula H₀ y H₁
2. Calcula las medias
3. ¿Cuál sitio es más rápido? ¿La diferencia es estadísticamente significativa?

---

## Lo que aprendiste

- La **hipótesis nula (H₀)** es lo que asumimos por defecto
- La **hipótesis alternativa (H₁)** es lo que queremos demostrar
- El **valor p** es la probabilidad de observar los datos si H₀ es cierta
- Si valor p < 0.05, rechazamos H₀ (resultado estadísticamente significativo)
- **Error Tipo I**: falso positivo (rechazar H₀ cuando es verdadera)
- **Error Tipo II**: falso negativo (no rechazar H₀ cuando es falsa)
- La evidencia combinada es más poderosa que una sola prueba

—Necesito hablar con tu padre —dijo Valeria—. Cara a cara.

—¿Y qué le vas a decir?

—Le voy a mostrar los números. Y voy a ver su reacción.

—¿Y si es culpable?

Valeria guardó su laptop.

—Entonces los números serán lo único que nos salve.

