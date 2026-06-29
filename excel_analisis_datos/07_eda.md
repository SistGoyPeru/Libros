# Capítulo 3: Análisis Exploratorio de Datos (EDA)

## Conocer los datos antes de analizarlos

—El EDA —dijo Valeria— es como conocer a una persona antes de trabajar con ella. Le preguntas cosas básicas: quién eres, qué haces, cómo te comportas.

### La Historia

—Ya tenemos los datos limpios —dijo Andrés—. 45,000 filas de ventas de todo el año. ¿Ahora qué?

—Ahora —dijo Valeria— vamos a conocerlos.

### Estadísticas descriptivas

—Lo primero —dijo Valeria— son las medidas básicas.

**Usa las funciones de Excel:**
```
PROMEDIO(rango)        'Media'
MEDIANA(rango)          'Mediana (50 percentil)'
MODA(rango)             'Moda (valor más frecuente)'
DESVEST.M(rango)        'Desviación estándar'
VAR.M(rango)            'Varianza'
MIN(rango)              'Mínimo'
MAX(rango)              'Máximo'
PERCENTIL(rango, 0.25)  'Q1 (25 percentil)'
PERCENTIL(rango, 0.75)  'Q3 (75 percentil)'
```

—O mejor —dijo Valeria—, usa **Análisis de datos**:

```
Datos > Análisis de datos > Estadística descriptiva
[ ] Resumen de estadísticas
[ ] Nivel de confianza para la media
```

### La función UNICOS

—Para ver valores únicos en una columna:

```
=UNICOS(rango)
```

—Esto te da de inmediato todas las categorías, productos o regiones sin duplicados.

### Análisis de frecuencias

—¿Cómo se distribuyen las ventas?

**Tabla de frecuencias con COUNTIF:**
```
=CONTAR.SI(rango, criterio)
```

**O con tabla dinámica para variables categóricas:**
```
Insertar > Tabla dinámica
Filas: Categoría
Valores: Conteo de Transacciones
Valores: Suma de Monto
```

### La función FILTRAR para segmentar

—Para explorar subconjuntos de datos:

```
=FILTRAR(tabla, condición)
```

**Ejemplos:**
```
=FILTRAR(Ventas, Ventas[Monto]>1000)
=FILTRAR(Ventas, (Ventas[Region]="Lima") * (Ventas[Mes]="Enero"))
```

### Matrices dinámicas para EDA

—Las nuevas funciones de Excel 365 hacen el EDA mucho más fácil:

**Ordenar y filtrar:**
```
=ORDENAR(UNICOS(Ventas[Producto]))
=ORDENAR(FILTRAR(Ventas, Ventas[Monto]>PROMEDIO(Ventas[Monto])))
```

**Top 10 productos por venta:**
```
=TOMA(ORDENAR(Ventas, 3, -1), 10)
```

**Resumen estadístico dinámico:**
```
=PORCOL(rango, PROMEDIO)
=PORCOL(rango, DESVEST)
```

### Análisis de correlación

—Para ver relaciones entre variables:

**Coeficiente de correlación:**
```
=COEFICIENTE.R2(ventas, publicidad)
```

**Matriz de correlación con Análisis de datos:**
```
Datos > Análisis de datos > Correlación
Rango de entrada: Seleccionar columnas numéricas
```

—El valor va de -1 a 1. Cerca de 1 = correlación positiva fuerte. Cerca de 0 = sin correlación.

### La checklist de EDA

—Cuando tengas datos nuevos —dijo Valeria—, sigue esta checklist:

```
[ ] ¿Cuántas filas y columnas? (FILAS, COLUMNAS)
[ ] ¿Qué tipos de datos tengo? (texto, número, fecha)
[ ] ¿Hay valores faltantes? (CONTAR.BLANCO)
[ ] ¿Valores únicos por columna? (UNICOS)
[ ] Estadísticas descriptivas (Media, Mediana, Desvest)
[ ] Distribución de variables numéricas (histograma)
[ ] Frecuencia de variables categóricas
[ ] Correlaciones entre variables
[ ] Top N y Bottom N
[ ] ¿Hay outliers? (IQR, formato condicional)
```

### Enigma #3

En `codigos/c03_eda/ventas_anuales_limpias.xlsx` tienes datos de ventas ya limpios.

**Tu misión:**
1. Calcula las estadísticas descriptivas de todas las columnas numéricas
2. Identifica los 5 productos más vendidos y los 5 menos vendidos
3. Calcula la correlación entre gasto en publicidad y ventas
4. Crea una tabla de frecuencias por región y mes
5. Responde: ¿Hay una región que consistentemente vende más? ¿Hay productos que deberían descontinuarse?