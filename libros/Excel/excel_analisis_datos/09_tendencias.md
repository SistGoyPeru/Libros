# Capítulo 5: Análisis de Tendencias y Patrones

## Ver el futuro en los datos

—El análisis de tendencias —dijo Valeria— es lo que separa a un analista de un reporteador. No solo miras lo que pasó, sino hacia dónde vas.

### Cálculo de variaciones

—Lo básico pero fundamental:

```
Variación absoluta = Valor Actual - Valor Anterior
Variación % = (Valor Actual - Valor Anterior) / Valor Anterior
```

**En Excel:**
```
Variación Mes = C2 - B2
Variación % = (C2 - B2) / B2   'Formato: 0.00%'
```

### Promedios móviles

—El promedio móvil suaviza las fluctuaciones y revela tendencias:

```
Promedio móvil 3 meses:
=PROMEDIO(B2:D2)

Promedio móvil 12 meses (anual móvil):
=PROMEDIO(B2:M2)
```

**Con gráfico:**
```
Insertar > Gráfico de líneas
Agregar serie: Promedio móvil
```

### Pronóstico con Excel

—Excel tiene herramientas de pronóstico integradas:

```
Datos > Previsión > Pronóstico
Rango de historial: Ventas por mes
Rango de fechas: Meses
Opciones: Estacionalidad automática
Intervalo de confianza: 95%
```

**FUNCIÓN PRONOSTICO:**
```
=PRONOSTICO(nuevo_x, ventas_conocidas, meses_conocidos)
```

**FUNCIÓN PRONOSTICO.ETS (estacional):**
```
=PRONOSTICO.ETS(fecha_objetivo, valores, línea_tiempo, estacionalidad, confianza)
```

### Análisis de estacionalidad

—Muchos negocios tienen patrones que se repiten:

```
Índice estacional = Ventas del mes / Promedio anual
```

**Tabla de estacionalidad:**

| Mes | Ventas 2024 | Ventas 2025 | Índice Promedio |
|-----|-------------|-------------|----------------|
| Ene | 100,000 | 110,000 | 0.85 |
| Feb | 95,000 | 105,000 | 0.80 |
| ... | ... | ... | ... |

—Si el índice es > 1, ese mes vende más que el promedio.

### Formato condicional para patrones

—Para detectar patrones visualmente:

**Barras de datos (data bars):**
```
Formato condicional > Barra de datos
Visualiza la magnitud relativa
```

**Conjunto de íconos para tendencias:**
```
Formato condicional > Conjunto de íconos > Flechas
Verde = subió, Amarillo = estable, Rojo = bajó
```

**Reglas para detección de patrones:**
```
=TASA_CRECIMIENTO() > 0.1  → Fondo verde
=TASA_CRECIMIENTO() < -0.1 → Fondo rojo
```

### Análisis de Pareto (80/20)

—El principio de Pareto: el 80% de los resultados vienen del 20% de las causas.

```
1. Ordenar productos por ventas descendente
2. Calcular % acumulado
3. Identificar el punto donde se llega al 80%
```

**En Excel:**
```
% del Total = Venta Producto / Total Ventas
% Acumulado = SUMAR.SI con rango expandido
=SI(%Acumulado <= 0.8, "A", SI(%Acumulado <= 0.95, "B", "C"))
```

### Análisis de segmentación

—Para encontrar patrones en segmentos:

```
Promedio por segmento:
=PROMEDIO.SI.CONJUNTO(Ventas[Monto], Ventas[Region], A2)

Comparación año vs año:
=SUMAR.SI.CONJUNTO(Ventas[Monto], Ventas[Año], 2025) /
 SUMAR.SI.CONJUNTO(Ventas[Monto], Ventas[Año], 2024) - 1
```

### Resumen del capítulo

| Técnica | Fórmula/Herramienta |
|---------|-------------------|
| Variación % | (Actual - Anterior) / Anterior |
| Promedio móvil | PROMEDIO de últimos N períodos |
| Pronóstico | PRONOSTICO.ETS |
| Estacionalidad | Índice estacional |
| Pareto | % acumulado + clasificación ABC |
| Segmentación | SUMAR.SI.CONJUNTO + comparación |

### Enigma #5

En `codigos/c05_tendencias/ventas_historicas.xlsx` tienes 36 meses de datos de ventas (2023-2025).

**Tu misión:**
1. Calcula la variación % mensual y anual
2. Crea un promedio móvil de 3 meses
3. Identifica los meses con mayor y menor estacionalidad
4. Genera un pronóstico para los próximos 3 meses usando PRONOSTICO.ETS
5. Aplica Pareto: ¿Qué productos generan el 80% de las ventas?
6. Crea un gráfico combinado: ventas reales + promedio móvil + pronóstico