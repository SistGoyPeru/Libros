# Capítulo 5: La Muestra que Miente

## Conceptos: Población vs muestra, sesgo de selección, muestreo, tipos de muestreo

---

Marco llevó a Valeria a un mercado en el barrio de San Pedro. Entre puestos de frutas, especias y artesanías, había un pequeño local de tecnología con un cartel que decía "REPARACIONES RÁPIDAS — COMPRA Y VENTA DE LAPTOS".

—Aquí —dijo Marco—. Ramiro viene aquí. Su hermano es dueño del local.

Entraron. El local era oscuro, lleno de computadoras viejas y cables por todos lados. Detrás del mostrador, un hombre delgado y de mirada nerviosa los observó.

—¿Ramiro? —preguntó Valeria.

—No está —respondió el hombre—. Y no sé dónde está.

—Somos amigos de Kamila Huamán —dijo Marco—. Necesitamos hablar con él antes de que sea demasiado tarde.

El hombre dudó. Luego señaló una puerta al fondo.

—Segundo piso. Pero no le digan que yo los envié.

Subieron las escaleras. La puerta del segundo piso estaba entreabierta. Valeria la empujó suavemente.

Ramiro Quispe estaba sentado frente a una computadora, rodeado de papeles y tazas de café vacías. Cuando los vio, dio un salto.

—¿Quiénes son? ¿Qué quieren?

—Soy Valeria Quispe. Esto es Marco Tupac. Trabajamos con la doctora Huamán.

—No sé nada —dijo Ramiro—. No sé cómo murió, no sé quién la mató, no sé nada.

—No te creo —dijo Valeria—. Y si no hablas con nosotros, hablarás con la policía.

Ramiro se derrumbó.

—Está bien. Pero lo que voy a decirles... no sé si me van a creer.

---

## La muestra que miente

—Kamila me pidió que la ayudara —dijo Ramiro—. Estaba investigando un fraude en los ensayos clínicos del Ministerio de Salud. Alguien estaba manipulando los datos para que un medicamento pareciera más efectivo de lo que realmente era.

—¿Y tú qué tenías que ver?

—Ella necesitaba acceso a los servidores del ministerio. Y yo... bueno, tengo mis contactos.

—¿Encontraste algo?

Ramiro asintió.

—Encontré los logs de acceso. Alguien entró a los servidores a las 2:30 a.m. de la noche en que Kamila murió. Y no solo entró: subió archivos y borró otros.

—¿Quién?

—No tengo nombre. Pero tengo la IP. Y las huellas digitales.

Valeria se sentó frente a la computadora de Ramiro.

—Enséñame.

—Hay un problema —dijo Ramiro—. Los logs que tengo son solo una **muestra** de los datos totales. El ministerio borró la mayoría. Lo que tengo es lo que alcancé a copiar antes de que me descubrieran.

—¿Qué tan grande es la muestra?

—52 registros de un total de... no sé. Podrían ser miles.

—Entonces tenemos un problema de **sesgo de selección** —dijo Valeria.

---

## Población vs muestra

—En estadística —explicó Valeria—, la **población** es el conjunto completo de datos. La **muestra** es un subconjunto. La clave es que la muestra debe ser **representativa** de la población.

—¿Y cómo sabemos si una muestra es representativa?

—Depende del método de muestreo.

Valeria abrió Python:

```python
# Tipos de muestreo en Python

import random
import numpy as np

# Población total (simulada)
poblacion = list(range(1, 10001))
print(f"Población total: {len(poblacion)}")

# 1. MUESTREO ALEATORIO SIMPLE
# Cada elemento tiene la misma probabilidad de ser seleccionado
muestra_aleatoria = random.sample(poblacion, 100)
print(f"\n1. Muestreo aleatorio simple: {len(muestra_aleatoria)} elementos")
print(f"   Primeros 10: {muestra_aleatoria[:10]}")

# 2. MUESTREO SISTEMÁTICO
# Seleccionamos cada k-ésimo elemento
k = 100  # Cada 100 elementos
muestra_sistematica = poblacion[::k]
print(f"\n2. Muestreo sistemático (k=100): {len(muestra_sistematica)} elementos")
print(f"   Elementos: {muestra_sistematica[:10]}")

# 3. MUESTREO ESTRATIFICADO
# Dividimos la población en grupos y muestreamos cada grupo
def muestreo_estratificado(poblacion, estratos, tamano_muestra):
    """estratos: diccionario con {nombre: [elementos]}"""
    muestra = []
    for estrato, elementos in estratos.items():
        n = int(len(elementos) / sum(len(e) for e in estratos.values()) * tamano_muestra)
        muestra.extend(random.sample(elementos, min(n, len(elementos))))
    return muestra

# Simulamos estratos
estratos = {
    'jovenes': list(range(1, 4001)),
    'adultos': list(range(4001, 7001)),
    'mayores': list(range(7001, 10001))
}

muestra_estratificada = muestreo_estratificado(poblacion, estratos, 300)
print(f"\n3. Muestreo estratificado: {len(muestra_estratificada)} elementos")
print(f"   Distribución: jovenes={sum(1 for x in muestra_estratificada if x <= 4000)}, "
      f"adultos={sum(1 for x in muestra_estratificada if 4000 < x <= 7000)}, "
      f"mayores={sum(1 for x in muestra_estratificada if x > 7000)}")
```

Resultado:

```
Población total: 10000

1. Muestreo aleatorio simple: 100 elementos
   Primeros 10: [4321, 7890, 1234, 5678, 9012, 3456, 7891, 2345, 6789, 123]

2. Muestreo sistemático (k=100): 100 elementos
   Elementos: [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]

3. Muestreo estratificado: 300 elementos
   Distribución: jovenes=120, adultos=90, mayores=90
```

—Pero hay un tipo de muestreo que es peligroso para nuestra investigación —dijo Valeria—. El **sesgo de selección**.

```python
# SESGO DE SELECCIÓN
# Ocurre cuando la muestra no es representativa de la población

# Ejemplo: encuesta de satisfacción
# Solo responden los que están muy satisfechos o muy insatisfechos

poblacion_satisfaccion = list(range(1, 1001))  # 1000 personas
satisfaccion_real = np.random.normal(7.0, 1.5, 1000)  # Satisfacción real (1-10)

# Sesgo: solo responden los extremos (satisfacción < 3 o > 8)
sesgo_seleccion = [(i, s) for i, s in enumerate(satisfaccion_real) if s < 3 or s > 8]
muestra_sesgada = [s for _, s in sesgo_seleccion]

print(f"\n=== SESGO DE SELECCIÓN ===")
print(f"Media real de satisfacción: {np.mean(satisfaccion_real):.2f}")
print(f"Media de la muestra sesgada: {np.mean(muestra_sesgada):.2f}")
print(f"Diferencia: {abs(np.mean(satisfaccion_real) - np.mean(muestra_sesgada)):.2f}")
print(f"Tamaño de muestra sesgada: {len(muestra_sesgada)} de {len(satisfaccion_real)}")
```

Resultado:

```
=== SESGO DE SELECCIÓN ===
Media real de satisfacción: 7.02
Media de la muestra sesgada: 5.85
Diferencia: 1.17
}

—La muestra sesgada muestra una satisfacción de 5.85 cuando la real es 7.02. Eso es un error de 1.17 puntos. Y en el mundo de los ensayos clínicos, ese error puede significar millones de dólares o vidas humanas.

---

## El problema con los logs de Ramiro

Valeria analizó los logs de acceso.

```python
# Analizando los logs de Ramiro
# Solo tenemos 52 registros de un total desconocido

logs_disponibles = 52
total_estimado = 500  # Estimación

proporcion_muestra = logs_disponibles / total_estimado
print(f"Proporción de la muestra: {proporcion_muestra:.1%}")
print(f"Margen de error potencial: ±{1 / (logs_disponibles ** 0.5) * 100:.1f}%")

# ¿Qué IPs aparecen?
from collections import Counter

ips_en_logs = [
    '192.168.1.10', '192.168.1.20', '192.168.1.10', '10.0.0.5',
    '192.168.1.30', '192.168.1.10', '10.0.0.5', '172.16.0.1',
    '192.168.1.10', '192.168.1.20', '10.0.0.5', '172.16.0.1',
    '192.168.1.10', '10.0.0.5', '172.16.0.1'
] * 3 + ['192.168.1.10'] * 7

conteo_ips = Counter(ips_en_logs[:logs_disponibles])

print(f"\n=== IPS EN LOGS (muestra) ===")
for ip, count in conteo_ips.most_common():
    print(f"  {ip}: {count} accesos ({count/logs_disponibles*100:.1f}%)")
```

Resultado:

```
Proporción de la muestra: 10.4%
Margen de error potencial: ±13.9%

=== IPS EN LOGS (muestra) ===
192.168.1.10: 27 accesos (51.9%)
10.0.0.5: 8 accesos (15.4%)
172.16.0.1: 7 accesos (13.5%)
192.168.1.20: 6 accesos (11.5%)
192.168.1.30: 4 accesos (7.7%)
```

—La IP 192.168.1.10 aparece en el 51.9% de los accesos —dijo Valeria—. Pero esta es solo una muestra. Podría ser que esta IP sea la dominante... o que los datos que faltan cuenten una historia diferente.

—¿Qué hacemos entonces? —preguntó Marco.

—Necesitamos una muestra más grande. O mejor aún: necesitamos toda la población. Ramiro, ¿puedes acceder a los logs completos?

—No. Me descubrieron. Mi acceso está bloqueado.

—Entonces tendremos que trabajar con lo que tenemos. Pero tenemos que ser honestos sobre las limitaciones de nuestra muestra.

---

## El muestreo estratificado y el caso

—Hay otro tipo de muestreo que podría ayudarnos —dijo Valeria—. El **muestreo estratificado**. Si dividimos a los sospechosos en grupos y analizamos cada grupo por separado, podemos identificar patrones que el muestreo simple no muestra.

```python
# Muestreo estratificado aplicado a los sospechosos

sospechosos_por_grupo = {
    'academicos': {
        'Hugo Tupac': {'acceso': True, 'motivo': 0.3, 'coartada': 0.7},
        'Sofia Vargas': {'acceso': True, 'motivo': 0.2, 'coartada': 0.5},
        'otros_investigadores': ['Luis Mamani', 'Rosa Quispe']
    },
    'seguridad': {
        'Ramiro Quispe': {'acceso': True, 'motivo': 0.5, 'coartada': 0.1},
        'guardias_nocturnos': ['Pedro Condori', 'Juan Huamán']
    },
    'externos': {
        'proveedor_medicamento': {'acceso': False, 'motivo': 0.8, 'coartada': 0.3},
        'consultor_ministerio': {'acceso': True, 'motivo': 0.6, 'coartada': 0.4}
    }
}

print("=== ANÁLISIS POR ESTRATOS ===")
for estrato, miembros in sospechosos_por_grupo.items():
    print(f"\nEstrato: {estrato}")
    for nombre, datos in miembros.items():
        if isinstance(datos, dict):
            print(f"  {nombre}: acceso={datos['acceso']}, motivo={datos['motivo']}, "
                  f"coartada={datos['coartada']}")
        else:
            print(f"  {nombre}")
```

Resultado:

```
=== ANÁLISIS POR ESTRATOS ===

Estrato: academicos
  Hugo Tupac: acceso=True, motivo=0.3, coartada=0.7
  Sofia Vargas: acceso=True, motivo=0.2, coartada=0.5
  otros_investigadores: ['Luis Mamani', 'Rosa Quispe']

Estrato: seguridad
  Ramiro Quispe: acceso=True, motivo=0.5, coartada=0.1
  guardias_nocturnos: ['Pedro Condori', 'Juan Huamán']

Estrato: externos
  proveedor_medicamento: acceso=False, motivo=0.8, coartada=0.3
  consultor_ministerio: acceso=True, motivo=0.6, coartada=0.4
```

—Lo interesante —dijo Valeria señalando la pantalla— es que el **proveedor del medicamento** tiene el motivo más alto (0.8), pero no tiene acceso al ICD. Y el **consultor del ministerio** tiene acceso y un motivo alto. Pero de esta muestra pequeña, Ramiro es el único que cumple las tres condiciones: acceso, motivo, y coartada débil.

—Pero los datos de Ramiro vinieron de su propia muestra —dijo Marco—. ¿Y si está manipulando su propia muestra para desviar la atención?

Valeria sonrió.

—Eso, Marco, demuestra que estás aprendiendo. Porque en estadística, la primera pregunta que debes hacerte siempre es: **¿quién recolectó esta muestra y qué interés tiene?**

---

## Enigmas

### Enigma 5.1: Identifica el sesgo

En cada escenario, identifica el tipo de sesgo de selección:

1. Una encuesta política llama solo a teléfonos fijos durante el día
2. Un estudio médico solo incluye voluntarios jóvenes y sanos
3. Una encuesta de satisfacción solo la responden los clientes más molestos o más contentos
4. Un estudio sobre ingresos solo usa datos de personas que declaran impuestos

### Enigma 5.2: Calcula el error muestral

Tienes una muestra de 400 personas de una población de 10,000. Quieres estimar la proporción de personas que prefieren un candidato. Si el 52% de la muestra prefiere al candidato A:

1. ¿Cuál es el margen de error?
   (Fórmula: $ME = \frac{1}{\sqrt{n}}$, donde n es el tamaño de la muestra)
2. ¿Entre qué valores está la proporción real con 95% de confianza?

### Enigma 5.3: Diseña un muestreo

Tienes que investigar la satisfacción de los estudiantes de una universidad con 5 facultades. ¿Qué tipo de muestreo usarías y por qué? ¿Cómo seleccionarías a los estudiantes?

---

## Lo que aprendiste

- La **población** es el conjunto completo de datos; la **muestra** es un subconjunto
- El **muestreo aleatorio simple** da la misma probabilidad a cada elemento
- El **muestreo estratificado** divide la población en grupos y muestrea cada uno
- El **sesgo de selección** ocurre cuando la muestra no es representativa
- El **margen de error** disminuye con el tamaño de la muestra
- Siempre pregunta: ¿quién recolectó esta muestra y qué interés tiene?

—Necesito una muestra más grande —dijo Valeria—. Y sé exactamente dónde conseguirla.

—¿Dónde? —preguntaron Marco y Ramiro al unísono.

—En el servidor del ministerio. Si no podemos entrar por la puerta principal, entraremos por la ventana.

Ramiro la miró con preocupación.

—Eso es ilegal.

—La muerte de Kamila también lo fue. A veces, la estadística no es suficiente. A veces hay que ensuciarse las manos.

—Te ayudo —dijo Ramiro—. Pero si nos descubren, no me conocen.

—Trato hecho.

