# Capítulo 6: Tablas Dinámicas para Análisis

## El poder de resumir millones de filas

—Las tablas dinámicas —dijo Valeria— son la herramienta más poderosa de Excel para análisis. Convierten datos en información en segundos.

### Tablas dinámicas como herramienta de análisis

—No uses tablas dinámicas solo para reportes. Úsalas para **explorar**.

```
Insertar > Tabla dinámica
Arrastrar:
  - Filas: Producto
  - Columnas: Mes
  - Valores: Suma de Monto
  - Filtros: Región
```

—En segundos ves qué producto vende más, en qué mes, y en qué región.

### Campos calculados en tablas dinámicas

—Para crear métricas personalizadas:

```
Tabla dinámica > Analizar > Campos, elementos y conjuntos > Campo calculado
Nombre: "Margen"
Fórmula: = Monto * 0.30
```

**Ejemplos de campos calculados:**

```
Utilidad = Ingreso - Costo
Margen % = Utilidad / Ingreso
Comisión = Ventas * 0.05
Bonificación = SI(Ventas > 100000, Ventas * 0.10, 0)
```

### Mostrar valores como

—Cambia la forma en que se muestran los valores:

| Opción | Uso en análisis |
|--------|----------------|
| % del total general | Participación de mercado |
| % del total de columna | Distribución por mes |
| % del total de fila | Composición del producto |
| Diferencia de... | Variación mes a mes |
| % de diferencia de... | Crecimiento porcentual |
| Ranking | Posición en el ranking |
| Total acumulado | Curva de Pareto |

### Agrupación inteligente

—Agrupar datos crea nuevas perspectivas:

**Agrupar fechas:**
```
Clic derecho en fecha > Agrupar
Por: Meses, Trimestres, Años
```

**Agrupar montos:**
```
Clic derecho en monto > Agrupar
Desde: 0, Hasta: 10000, Por: 1000
```

**Agrupar texto (manual):**
```
Seleccionar productos > Clic derecho > Agrupar
Nombre: "Electrónicos"
```

### Segmentadores conectados

—Para análisis interactivo:

```
Insertar segmentador: Región, Categoría, Mes
Conectar segmentador: [x] Tabla dinámica 1, [x] Tabla dinámica 2
```

—Ahora un solo clic filtra múltiples tablas dinámicas a la vez.

### GETPIVOTDATA para informes

—Para extraer valores específicos de la tabla dinámica:

```
=GETPIVOTDATA("Ventas", $A$3, "Producto", "Silla", "Mes", "Enero")
```

—Útil para crear informes con formato personalizado alimentados por la tabla dinámica.

### Minigráficos + tabla dinámica

—Combina tablas dinámicas con minigráficos para tendencias:

```
Insertar > Minigráfico > Línea
Rango de datos: Ventas mensuales por producto
```

### Análisis What-If con tablas dinámicas

—Simula escenarios:

1. Crea una tabla dinámica con Ventas por Producto
2. Agrega un campo calculado "Escenario Optimista" = Monto * 1.15
3. Agrega "Escenario Pesimista" = Monto * 0.90
4. Compara los tres escenarios lado a lado

### Resumen del capítulo

| Técnica | Para qué sirve |
|---------|---------------|
| Tabla dinámica básica | Resumir datos por categorías |
| Campos calculados | Métricas personalizadas |
| Mostrar valores como | Variación, ranking, % |
| Agrupación | Crear categorías jerárquicas |
| Segmentadores | Análisis interactivo |
| GETPIVOTDATA | Informes profesionales |
| Minigráficos | Tendencias visuales |

### Enigma #6

En `codigos/c06_tablas_dinamicas/ventas_analisis.xlsx` hay 50,000 transacciones de 2 años.

**Tu misión:**
1. Crea una tabla dinámica que muestre ventas por trimestre y categoría
2. Agrega un campo calculado "Proyección" (ventas * 1.10)
3. Muestra el % de crecimiento vs trimestre anterior
4. Agrupa los productos en segmentos (Premium, Estándar, Económico)
5. Conecta segmentadores de Región y Año a dos tablas dinámicas simultáneamente
6. Crea un informe con GETPIVOTDATA que muestre: Ventas totales del año, Top 3 productos, y % de crecimiento