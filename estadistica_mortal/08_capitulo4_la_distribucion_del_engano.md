# Capítulo 4: La Distribución del Engaño

## Conceptos: Distribución normal, desviación estándar, Z-score, regla empírica

---

El despacho del Dr. Hugo Tupac ocupaba todo el octavo piso del ICD. Paredes de vidrio, muebles de madera tallada a mano, y una vista panorámica de la cordillera de los Andes. El director era un hombre alto, de cabello cano y mirada intensa.

—Siéntense —dijo sin levantar la vista de su computadora—. Sabía que vendrían.

—¿Sabía? —preguntó Valeria.

—Marco es mi hijo. Y Kamila era mi mejor investigadora. Cuando alguien muere en tu institución, las preguntas no tardan en llegar.

El Dr. Tupac finalmente levantó la vista.

—¿Qué quieren saber?

—Todo —dijo Valeria—. ¿Qué estaba investigando Kamila?

—No lo sé con exactitud. Ella trabajaba en el proyecto Yupay, un sistema de modelos predictivos. Pero en las últimas semanas se volvió... paranoica. Decía que había encontrado una anomalía en los datos del Ministerio de Salud.

—¿Qué tipo de anomalía?

—No me dio detalles. Dijo que necesitaba verificarlo antes de hablarlo con alguien.

—¿Y usted no preguntó?

—Pregunté. Me dijo que esperara. Y luego... apareció muerta.

Valeria observó al director. Su lenguaje corporal era abierto, sus respuestas directas. Pero algo no encajaba.

—Necesito acceso a los datos del proyecto Yupay —dijo Valeria.

—Imposible. Son datos clasificados del ministerio.

—Entonces deme acceso a los servidores donde Kamila guardaba sus copias de seguridad.

El Dr. Tupac la miró largamente.

—Una hora. Marco te acompañará. Y si encuentras algo, me lo reportas directamente.

Salieron del despacho. Marco estaba pálido.

—¿Crees que dice la verdad? —preguntó.

—No lo sé —respondió Valeria—. Pero sus respuestas fueron... estadísticamente normales. Sin desviaciones. Y eso, a veces, es sospechoso.

---

## La distribución normal

En la sala de servidores, Valeria encontró los backups de Kamila. Había docenas de archivos, pero uno llamó su atención: `distribucion_original.npy`.

—Esto es un archivo NumPy —dijo—. Contiene datos numéricos puros.

Lo cargó en Python:

```python
import numpy as np
import matplotlib.pyplot as plt

# Cargamos los datos originales
datos_originales = np.load('distribucion_original.npy')
print(f"Shape: {datos_originales.shape}")
print(f"Tipo: {datos_originales.dtype}")
print(f"Primeros 20 valores: {datos_originales[:20]}")
```

Resultado:

```
Shape: (10000,)
Tipo: float64
Primeros 20 valores: [72.3 68.1 74.5 71.2 69.8 73.0 70.5 75.1 67.9 72.8
                      70.2 74.0 71.8 69.5 73.4 68.7 72.1 70.9 75.3 71.5]
}

—Son mediciones de presión arterial —dijo Valeria—. De un estudio clínico. Vamos a ver su distribución.

```python
# Visualizar la distribución
media = np.mean(datos_originales)
mediana = np.median(datos_originales)
desv_std = np.std(datos_originales)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {desv_std:.2f}")
print(f"Mínimo: {np.min(datos_originales):.2f}")
print(f"Máximo: {np.max(datos_originales):.2f}")

# Histograma
plt.hist(datos_originales, bins=50, alpha=0.7, color='blue', edgecolor='black')
plt.axvline(media, color='red', linestyle='--', label=f'Media = {media:.1f}')
plt.axvline(media - desv_std, color='green', linestyle=':', label=f'-1σ')
plt.axvline(media + desv_std, color='green', linestyle=':', label=f'+1σ')
plt.title('Distribución de Presión Arterial (Datos Originales)')
plt.xlabel('Presión Arterial')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
```

—Mira esto —dijo Valeria señalando la pantalla—. La distribución tiene forma de campana. Es una **distribución normal** (o gaussiana).

—¿Por qué es importante?

—Porque en una distribución normal, hay una **regla empírica** que se cumple siempre:

- El **68%** de los datos está a 1 desviación estándar de la media
- El **95%** está a 2 desviaciones estándar
- El **99.7%** está a 3 desviaciones estándar

```python
# Verificar la regla empírica
dentro_1sigma = np.sum(np.abs(datos_originales - media) <= desv_std)
dentro_2sigma = np.sum(np.abs(datos_originales - media) <= 2 * desv_std)
dentro_3sigma = np.sum(np.abs(datos_originales - media) <= 3 * desv_std)
total = len(datos_originales)

print(f"\n=== REGLA EMPÍRICA ===")
print(f"68% teórico: 6800")
print(f"Dentro de 1σ: {dentro_1sigma} ({100*dentro_1sigma/total:.1f}%)")
print(f"95% teórico: 9500")
print(f"Dentro de 2σ: {dentro_2sigma} ({100*dentro_2sigma/total:.1f}%)")
print(f"99.7% teórico: 9970")
print(f"Dentro de 3σ: {dentro_3sigma} ({100*dentro_3sigma/total:.1f}%)")
```

Resultado:

```
=== REGLA EMPÍRICA ===
68% teórico: 6800
Dentro de 1σ: 6832 (68.3%)
95% teórico: 9500
Dentro de 2σ: 9495 (95.0%)
99.7% teórico: 9970
Dentro de 3σ: 9973 (99.7%)
}

—Casi perfecto —dijo Valeria—. Estos datos son genuinos. Ahora comparemos con los datos manipulados que vimos en el capítulo anterior.

---

## El Z-score: midiendo la anomalía

—El **Z-score** nos dice a cuántas desviaciones estándar está un valor de la media. Es la forma estándar de identificar valores atípicos (outliers).

$$Z = \frac{x - \mu}{\sigma}$$

Valeria escribió:

```python
# Calcular Z-scores para identificar anomalías
def z_score(valor, media, desv_std):
    return (valor - media) / desv_std

# Encontremos los valores más extremos
z_scores = np.abs((datos_originales - media) / desv_std)
indices_extremos = np.argsort(z_scores)[-5:]  # 5 valores más extremos

print(f"\n=== VALORES EXTREMOS (Z-score) ===")
print(f"{'Índice':<10} {'Valor':<12} {'Z-score':<10}")
print("-" * 32)
for i in indices_extremos:
    z = z_score(datos_originales[i], media, desv_std)
    print(f"{i:<10} {datos_originales[i]:<12.2f} {z:<10.2f}")

# ¿Cuántos valores tienen Z-score > 3?
extremos = np.sum(z_scores > 3)
print(f"\nValores con Z-score > 3: {extremos}")
print(f"Esperado (0.3%): {int(0.003 * len(datos_originales))}")
```

Resultado:

```
=== VALORES EXTREMOS (Z-score) ===
Índice      Valor        Z-score   
--------------------------------
3412        65.2         -2.98      
8911        76.8          2.95      
4523        64.9         -3.12      
1023        77.1          3.05      
7845        63.8         -3.41      

Valores con Z-score > 3: 27
Esperado (0.3%): 30
}

—Ahora —dijo Valeria—, comparemos con los datos falsos del ensayo clínico.

Valeria cargó los datos del capítulo anterior.

```python
# Datos falsos: 500 pacientes, 470 mejoran (tratamiento A)
# Bajo una distribución normal, esperaríamos cierta variabilidad

# Simulamos cómo deberían verse datos genuinos
import random
random.seed(42)

datos_genuinos = []
for _ in range(500):
    if random.random() < 0.71:  # 71% de mejora general
        datos_genuinos.append(1)  # mejora
    else:
        datos_genuinos.append(0)  # no mejora

tasa_genuina = sum(datos_genuinos) / 500

# Simulamos 10000 ensayos para ver la distribución esperada
tasas_simuladas = []
for _ in range(10000):
    ensayo = []
    for _ in range(500):
        if random.random() < 0.71:
            ensayo.append(1)
        else:
            ensayo.append(0)
    tasas_simuladas.append(sum(ensayo) / 500)

media_simulada = np.mean(tasas_simuladas)
std_simulada = np.std(tasas_simuladas)

print(f"Media de tasas simuladas: {media_simulada:.3f}")
print(f"Desviación estándar: {std_simulada:.3f}")

# ¿Qué tan extrema es la tasa observada del tratamiento A (94%)?
tasa_observada = 0.94
z_tasa = (tasa_observada - media_simulada) / std_simulada
print(f"\nTasa observada (Tratamiento A): {tasa_observada}")
print(f"Z-score de la tasa observada: {z_tasa:.2f}")
print(f"Esto es {z_tasa:.0f} desviaciones estándar por encima de la media")
print(f"Probabilidad de ocurrir al azar: esencialmente 0")
```

Resultado:

```
Media de tasas simuladas: 0.710
Desviación estándar: 0.020

Tasa observada (Tratamiento A): 0.94
Z-score de la tasa observada: 11.50
Esto es 12 desviaciones estándar por encima de la media
Probabilidad de ocurrir al azar: esencialmente 0
}

—Un Z-score de 11.5 —dijo Valeria—. En el mundo real, un Z-score mayor a 3 ya es extremadamente raro. Once punto cinco es... imposible. Es como encontrar una persona de 4 metros de altura.

—Alguien manipuló estos números —dijo Marco.

—Sí. Y quien lo hizo no entiende de distribuciones normales. Porque si supiera, habría hecho que los datos falsos se vieran más realistas.

---

## La distribución del engaño

Valeria abrió otro archivo del backup de Kamila.

—Mira esto. Kamila guardó una comparación entre los datos originales y los datos manipulados.

```python
# Comparación visual
datos_manipulados = np.load('datos_manipulados.npy')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(datos_originales, bins=50, alpha=0.7, color='blue')
ax1.set_title('Datos Originales')
ax1.set_xlabel('Presión Arterial')

ax2.hist(datos_manipulados, bins=50, alpha=0.7, color='red')
ax2.set_title('Datos Manipulados')
ax2.set_xlabel('Presión Arterial')

plt.tight_layout()
plt.show()

# Estadísticas comparativas
print(f"{'Métrica':<25} {'Original':<12} {'Manipulado':<12}")
print("-" * 49)
print(f"{'Media':<25} {np.mean(datos_originales):<12.2f} {np.mean(datos_manipulados):<12.2f}")
print(f"{'Desviación Std':<25} {np.std(datos_originales):<12.2f} {np.std(datos_manipulados):<12.2f}")
print(f"{'Mediana':<25} {np.median(datos_originales):<12.2f} {np.median(datos_manipulados):<12.2f}")
print(f"{'Asimetría (skewness)':<25} {np.mean(((datos_originales - np.mean(datos_originales))/np.std(datos_originales))**3):<12.2f} {np.mean(((datos_manipulados - np.mean(datos_manipulados))/np.std(datos_manipulados))**3):<12.2f}")
```

Resultado:

```
Métrica                   Original     Manipulado  
-------------------------------------------------
Media                     71.23        74.56      
Desviación Std            2.11         0.95       
Mediana                   71.20        74.50      
Asimetría (skewness)      0.02         0.85       
}

—¿Ves la diferencia? —preguntó Valeria—. Los datos originales tienen una desviación estándar de 2.11, los manipulados de solo 0.95. La desviación estándar se redujo a la mitad. Y la asimetría pasó de casi cero (normal) a 0.85 (sesgada).

—¿Qué significa eso?

—Que alguien no solo cambió los valores, sino que alteró la **variabilidad natural** de los datos. Los datos falsos son demasiado perfectos. Demasiado centrados. En estadística, eso se llama un **sesgo de manipulación**.

---

## Enigmas

### Enigma 4.1: Identifica los outliers

Un conjunto de edades tiene media 45 y desviación estándar 10. Calcula los Z-scores de las siguientes edades e identifica cuáles son outliers (|Z| > 3):

[23, 45, 67, 72, 18, 81, 44, 46, 22, 78]

### Enigma 4.2: La regla empírica

En una distribución normal con media 100 y desviación estándar 15:

1. ¿Qué porcentaje de valores está entre 85 y 115?
2. ¿Entre 70 y 130?
3. ¿Entre 55 y 145?

### Enigma 4.3: Detecta la manipulación

Te dan dos conjuntos de datos. Uno es genuino y el otro fue manipulado. Calcula la media, desviación estándar y Z-scores de ambos. ¿Cuál parece manipulado y por qué?

```python
conjunto_A = [72, 68, 74, 71, 69, 73, 70, 75, 67, 72, 70, 74, 71, 69, 73]
conjunto_B = [72, 72, 73, 71, 72, 72, 72, 71, 73, 72, 72, 73, 71, 72, 72]
```

---

## Lo que aprendiste

- La **distribución normal** (campana de Gauss) es la distribución más común en la naturaleza
- La **regla empírica**: 68-95-99.7% de los datos dentro de 1-2-3 desviaciones estándar
- El **Z-score** mide cuán atípico es un valor: Z = (x - μ) / σ
- |Z| > 3 generalmente indica un **outlier**
- Datos manipulados suelen tener **menor variabilidad** y **mayor asimetría**

Valeria cerró su laptop.

—Tengo suficiente para demostrar que los datos del ensayo fueron manipulados. Pero aún no sé quién lo hizo ni por qué.

—¿Y ahora? —preguntó Marco.

—Ahora vamos a buscar a Ramiro. Porque si él no manipuló los datos, alguien lo está usando como chivo expiatorio. Y si él lo hizo... necesito saber por qué.

Marco asintió.

—Tengo una idea de dónde puede estar.

