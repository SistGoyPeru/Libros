# Capítulo 10: Proyecto Final — Pipeline de Análisis

## De datos crudos a decisión

—Llegó el momento —dijo Valeria—. Vas a construir un pipeline completo de análisis de datos desde cero. Como si fueras un analista de Datawise.

### El proyecto

La gerencia de Datawise Corp. necesita un informe mensual de rendimiento. Los datos llegan de 4 fuentes diferentes. Tu trabajo: transformarlos en un dashboard listo para presentar al directorio.

### Paso 1: Importar datos

**Fuentes de datos:**
1. `ventas_mes.csv` — Ventas del mes actual
2. `ventas_historico.xlsx` — Ventas de meses anteriores
3. `productos.xlsx` — Catálogo de productos
4. `clientes.xlsx` — Base de clientes

—Usa Power Query para importar todo desde una carpeta.

### Paso 2: Limpiar y preparar

**Tareas de limpieza:**
1. Unificar formatos de fecha
2. Eliminar duplicados
3. Estandarizar nombres de productos
4. Manejar valores faltantes
5. Verificar tipos de datos

—Crea una consulta de Power Query "LimpiezaVentas" que automatice todo.

### Paso 3: Transformar y enriquecer

**Combinar datos:**
1. Combina ventas con productos (para tener categoría y precio)
2. Combina ventas con clientes (para tener segmento y región)
3. Crea columna "Total Venta" = Cantidad * Precio
4. Crea columna "Mes" a partir de la fecha
5. Crea columna "Trimestre"

### Paso 4: Analizar

**Indicadores a calcular:**

```
KPI 1: Ventas totales del mes
KPI 2: Variación % vs mes anterior
KPI 3: Promedio de venta por transacción
KPI 4: Producto más vendido
KPI 5: Categoría con mayor crecimiento
KPI 6: % de cumplimiento de meta mensual
```

### Paso 5: Visualizar

**Dashboard de una página:**

```
┌─────────────────────────────────────────┐
│ Datawise Corp. — Informe Mensual        │
│ [Segmentador: Mes] [Segmentador: Región] │
├──────────┬──────────┬──────────┬─────────┤
│ Ventas    │ Variación │ Transac. │ Ticket  │
│ S/ 1.2M   │ +15% ▲    │ 3,450    │ S/ 348  │
├──────────┴──────────┴──────────┴─────────┤
│ [Gráfico: Ventas diarias + promedio móvil]│
├─────────────────────────────────────────┤
│ [Gráfico: Top 10 productos (barras)]     │
│ [Gráfico: Ventas por región (pastel)]    │
├─────────────────────────────────────────┤
│ [Tabla: Productos con menor rendimiento] │
│ [Minigráficos por producto]              │
└─────────────────────────────────────────┘
```

### Paso 6: Automatizar

—Configura el pipeline para que:
1. Al agregar un nuevo archivo a la carpeta "Ventas", el dashboard se actualice
2. Los segmentadores permitan filtrar por mes y región
3. El dashboard se pueda exportar a PDF con un botón

### Entregables

```
1. Pipeline de Power Query (consultas documentadas)
2. Dashboard interactivo (una hoja)
3. Informe ejecutivo (PDF exportable)
4. Documentación técnica (hoja "Metadatos")
```

### Criterios de evaluación

| Criterio | Peso |
|----------|------|
| Datos correctos (sin errores de limpieza) | 30% |
| Power Query automatizado | 20% |
| Dashboard claro y profesional | 25% |
| KPIs bien calculados | 15% |
| Documentación | 10% |

### Enigma Final

En `codigos/c10_proyecto/` encontrarás los datos de 4 fuentes para completar el proyecto.

**Tu misión:** Construye el pipeline completo de análisis. El dashboard debe responder:

1. ¿Cómo van las ventas este mes vs el mes anterior?
2. ¿Qué productos están creciendo y cuáles están cayendo?
3. ¿Qué regiones están rindiendo mejor?
4. ¿Dónde debemos enfocar nuestros esfuerzos el próximo mes?
5. ¿Cuál es el pronóstico para el cierre del trimestre?

*Cada respuesta debe estar respaldada por un número o un gráfico en el dashboard. El directorio no quiere sorpresas: quiere datos.*