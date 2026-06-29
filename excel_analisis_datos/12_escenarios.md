# Capítulo 8: Análisis de Escenarios y Sensibilidad

## ¿Qué pasaría si...?

—La pregunta más poderosa del análisis —dijo Valeria— es "¿qué pasaría si?".

### Tabla de datos (Data Table)

—La tabla de datos muestra cómo cambia un resultado al variar una o dos variables.

**Tabla de una variable:**
```
Datos > Análisis Y Si > Tabla de datos
Celda de columna: Variable (ej. tasa de descuento)
```

—Excel calcula automáticamente los resultados para cada valor.

**Tabla de dos variables:**
```
Celda de fila: Variable 1 (ej. precio)
Celda de columna: Variable 2 (ej. cantidad)
```

### Administrador de escenarios

—Para crear y comparar diferentes escenarios:

```
Datos > Análisis Y Si > Administrador de escenarios
Agregar:
  Escenario Optimista: Ventas +20%, Costos -5%
  Escenario Realista: Ventas +10%, Costos 0%
  Escenario Pesimista: Ventas -10%, Costos +10%
```

**Resumen de escenarios:**
```
Administrador de escenarios > Resumen
Seleccionar celdas resultado
```

—Excel genera un informe comparativo automático.

### Análisis de sensibilidad

—¿Qué variable impacta más mi resultado?

**Tabla de sensibilidad:**

| Variable | Rango | Impacto |
|----------|-------|---------|
| Precio | -10% a +10% | 50,000 |
| Volumen | -10% a +10% | 30,000 |
| Costo | -10% a +10% | -20,000 |

—El precio es la variable más sensible.

### Gráfico de sensibilidad (Tornado)

—El gráfico de tornado muestra visualmente el impacto de cada variable:

```
1. Calcula el resultado base
2. Para cada variable, calcula el resultado en escenario optimista y pesimista
3. Crea un gráfico de barras apiladas
4. Ordena por impacto (de mayor a menor)
```

### Solver para optimización

—Cuando necesitas encontrar el valor óptimo:

```
Datos > Solver
Celda objetivo: Utilidad (maximizar)
Variables: Precio, Cantidad
Restricciones: Precio >= 50, Precio <= 200, Cantidad >= 0
```

### Búsqueda de objetivo (Goal Seek)

—Para un objetivo específico:

```
Datos > Análisis Y Si > Buscar objetivo
Definir celda: Utilidad
Valor objetivo: 100,000
Para cambiar: Precio
```

—Excel encuentra automáticamente el precio necesario para alcanzar la utilidad deseada.

### Simulación Monte Carlo (con tabla de datos)

—Para modelar incertidumbre:

```
Paso 1: Crear variables aleatorias
  =ALEATORIO() para probabilidades
  =INV.NORM(ALEATORIO(), media, desvest) para distribuciones normales

Paso 2: Crear modelo con las variables aleatorias

Paso 3: Tabla de datos con 1000 iteraciones
  Columna: iteraciones (1 a 1000)
  Celda de columna: celda vacía
  Resultado: Utilidad

Paso 4: Analizar distribución de resultados
  =PROMEDIO(utilidades)
  =PERCENTIL(utilidades, 0.05) 'Peor caso al 95% de confianza'
  =PERCENTIL(utilidades, 0.95) 'Mejor caso'
```

### Enigma #8

En `codigos/c08_escenarios/modelo_negocio.xlsx` tienes un modelo de negocio con variables de precio, cantidad, costo fijo y costo variable.

**Tu misión:**
1. Crea 3 escenarios (Optimista, Realista, Pesimista) usando el Administrador de escenarios
2. Genera un informe resumen comparativo
3. Crea una tabla de sensibilidad: ¿qué variable impacta más la utilidad?
4. Usa Solver para encontrar el precio óptimo que maximiza la utilidad
5. Usa Buscar objetivo para hallar cuántas unidades vender para alcanzar S/ 200,000 de utilidad
6. Gráfico de tornado con los resultados de sensibilidad