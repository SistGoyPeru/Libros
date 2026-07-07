# Capítulo 9: Dashboard Contable y KPIs

## Contar la historia de los números

—Los estados financieros —dijo Don Alberto— cuentan la historia de una empresa. Pero un dashboard bien diseñado la hace visible en segundos.

### La Historia

—Don Alberto —dijo María—, el gerente quiere un "tablero de control" que muestre en una sola pantalla cómo va la empresa. Me pidió: ventas del mes, gastos, utilidad, cuentas por cobrar, cuentas por pagar, liquidez, rentabilidad... todo.

—Lo que quiere —dijo Don Alberto— es un dashboard. Y vamos a construirlo.

### Principios del dashboard contable

—Antes de abrir Excel —dijo Don Alberto—, define:

1. **Audiencia:** ¿El gerente? ¿El directorio? ¿Los accionistas?
2. **Período:** ¿Mensual? ¿Trimestral? ¿Acumulado?
3. **Métricas clave:** No más de 7 indicadores principales
4. **Acción:** ¿Qué decisión se tomará con esta información?

### KPIs financieros esenciales

—Estos son los indicadores que todo dashboard contable debe tener:

| KPI | Fórmula | Qué mide |
|-----|---------|----------|
| **Liquidez corriente** | Activo Cte / Pasivo Cte | Capacidad de pago a corto plazo |
| **Prueba ácida** | (Activo Cte - Inventarios) / Pasivo Cte | Liquidez sin inventarios |
| **ROE** | Utilidad Neta / Patrimonio | Rentabilidad del capital |
| **ROA** | Utilidad Neta / Activo Total | Rentabilidad de los activos |
| **Margen neto** | Utilidad Neta / Ventas | % de ganancia sobre ventas |
| **Endeudamiento** | Pasivo Total / Activo Total | Nivel de deuda |
| **Cobertura de intereses** | EBIT / Gastos Financieros | Capacidad de pagar intereses |

**Cálculo en Excel:**

```
Liquidez Corriente = SUMAR.SI(Balance[Categoria], "Activo Cte", Balance[Monto]) /
                     SUMAR.SI(Balance[Categoria], "Pasivo Cte", Balance[Monto])

ROE = Utilidad Neta / Patrimonio * 100
```

### Diagramas de velocímetro

—El velocímetro o gráfico de semáforo —dijo Don Alberto— es perfecto para mostrar si un indicador está en zona verde, amarilla o roja.

**Cómo crearlo:**

1. Crea una tabla con Valor Actual, Mínimo, Máximo, y Verde/Amarillo/Rojo
2. Usa un gráfico de anillo con 3 secciones
3. Superpone una aguja con un gráfico circular

—O de forma más simple —dijo Don Alberto—, usa formato condicional con íconos:

```
Formato condicional > Conjunto de íconos > Semáforos
```

**Reglas:**

| Si el indicador está... | Ícono |
|------------------------|-------|
| Por encima del objetivo | Verde |
| Entre 80% y 100% | Amarillo |
| Por debajo del 80% | Rojo |

### Gráficos de evolución

—Las tendencias son más importantes que los valores absolutos —dijo Don Alberto.

**Gráfico de ventas mensuales con línea de meta:**
```
Insertar > Gráfico de líneas
Serie 1: Ventas mensuales
Serie 2: Meta mensual (línea punteada)
Serie 3: Promedio móvil (tendencia)
```

**Agregar línea de tendencia:**
```
Clic derecho en serie > Agregar línea de tendencia
Tipo: Lineal o Media móvil (período 3)
Mostrar ecuación en el gráfico
```

### Minigráficos

—Los minigráficos —dijo Don Alberto— son gráficos en miniatura que caben en una celda. Perfectos para dashboards.

```
Insertar > Minigráficos
Tipo: Líneas, Columnas, o Ganancias/pérdidas
Rango de datos: Seleccionar serie
Ubicación: Celda para el minigráfico
```

**Ejemplo: tendencia de ventas por producto:**

| Producto | Ene | Feb | Mar | Abr | May | Jun | Tendencia |
|----------|-----|-----|-----|-----|-----|-----|-----------|
| Prod A | 100 | 120 | 115 | 130 | 145 | 140 | 📈 |
| Prod B | 80 | 75 | 70 | 60 | 55 | 50 | 📉 |

—Cada minigráfico en la última columna muestra la tendencia de 6 meses.

### Formato condicional en dashboards

**Barras de datos:**
```
Seleccionar rango > Formato condicional > Barra de datos
Color: Verde degradado
```
—Ideal para comparar magnitudes sin usar un gráfico.

**Conjuntos de íconos:**
```
Formato condicional > Conjunto de íconos > Triángulos
Criterios:
  >=105%: Triángulo verde (mejor que meta)
  >=95%: Triángulo amarillo (cerca de meta)
  <95%: Triángulo rojo (debajo de meta)
```

### Dashboard interactivo

—Para el dashboard final —dijo Don Alberto—, combina:

1. **Encabezado:** Nombre de la empresa, período, fecha de actualización
2. **KPIs principales:** 4-6 tarjetas con valor, variación, y semáforo
3. **Gráfico de evolución:** Ventas, gastos y utilidad por mes
4. **Tabla de detalle:** Las 10 cuentas más importantes
5. **Segmentadores:** Mes, Centro de Costo, Línea de Producto
6. **Formato condicional:** Alertas visuales inmediatas

### Caso práctico: Dashboard completo

María y Don Alberto construyeron juntos:

**Modelo de datos:**
```
Tabla: Ventas (Fecha, Producto, Monto, CentroCosto)
Tabla: Gastos (Fecha, Categoria, Monto, CentroCosto)
Tabla: Balances (Cuenta, Tipo, Monto)
```

**KPIs calculados:**

```
Ventas MTD (Month to Date):
=SUMAR.SI.CONJUNTO(Ventas[Monto], Ventas[Fecha], ">="&INICIO.MES(HOY(),0),
                    Ventas[Fecha], "<="&HOY())

Variación vs mes anterior:
=(VentasMTD - VentasMesAnterior) / VentasMesAnterior
```

**Dashboard final:**
—Una sola hoja con conectividad, filtros dinámicos, y alertas automáticas.

### Resumen del capítulo

| Herramienta | Uso en dashboard |
|-------------|-----------------|
| KPIs | Indicadores financieros clave |
| Velocímetros | Estado de cada indicador |
| Gráfico de líneas | Evolución temporal |
| Minigráficos | Tendencia en una celda |
| Barras de datos | Comparación visual |
| Semáforos | Alertas de cumplimiento |
| Segmentadores | Filtros interactivos |

### Enigma contable #9

En `codigos/09_dashboard/datos_contables.xlsx` encontrarás 3 tablas: Ventas 2025, Gastos 2025, y Balance General 2025.

**Tu misión:**
1. Calcula los siguientes KPIs: Liquidez Corriente, ROE, Margen Neto, Endeudamiento
2. Crea un gráfico de evolución mensual de Ventas vs Gastos
3. Agrega minigráficos de tendencia para cada mes del año
4. Diseña tarjetas de KPI con: valor actual, variación %, y semáforo
5. Agrega segmentadores por trimestre y por categoría
6. El dashboard debe ser imprimible en una sola hoja tamaño A4

*El dashboard debe ser claro, profesional y listo para presentar al gerente en 5 minutos.*