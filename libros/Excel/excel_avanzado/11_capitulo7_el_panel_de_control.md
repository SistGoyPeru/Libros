
# Capítulo 7: El Panel de Control

## Dashboard Avanzado con Controles de Formulario y Power View

El día 23. Quedaban 7 días para responder a Nova. Los informes de Solver y los análisis de sensibilidad eran sólidos, pero faltaba algo crucial: una forma de comunicar todo el hallazgo de manera visual, impactante e interactiva.

—Si llevamos esto a la UIF —dijo Valeria—, no podemos entregarles 20 hojas de Excel con números fríos. Necesitamos un **dashboard**. Un panel de control que cuente la historia completa con un vistazo.

—¿Como un tablero de mandos? —preguntó Carlos.

—Exactamente. Un dashboard profesional combina gráficos, indicadores y controles interactivos para que el usuario pueda explorar los datos por sí mismo.

### Planificando el dashboard

Valeria abrió una hoja en blanco y dibujó el layout:

```
+--------------------------------------------------+
|  LOGO    DASHBOARD - INVESTIGACIÓN NOVA           |
|          Transacciones: 278,431 | Alertas: 47    |
+----------+---------------------------------------+
| FILTROS  |    GRÁFICO PRINCIPAL                   |
| [Mes    v]|    Transacciones por Mes               |
| [Empresa]|    [Gráfico de líneas]                 |
| [Tipo   v]|                                        |
|          +---------------------------------------+
| [Slider] |    TABLA DE DATOS                      |
| Monto    |    Top 10 Transacciones Sospechosas    |
| min-max  |    [Tabla dinámica]                    |
+----------+---------------------------------------+
| KPI 1    | KPI 2        | KPI 3       | KPI 4    |
| Total    | Trans.       | Empresas    | Alertas  |
| S/ 11.6M | Sospechosas  | Vinculadas  | Activas  |
+----------+--------------+-------------+----------+
```

—Necesitamos tres tipos de controles —dijo Valeria—:
1. **Controles de formulario**: botones, listas, barras de desplazamiento
2. **Gráficos conectados al modelo de Power Pivot**
3. **Indicadores KPI**

### Controles de formulario

Valeria activó la pestaña **Programador** y en **Insertar > Controles de formulario** seleccionó:

**1. Cuadro combinado (lista desplegable):**
—Para seleccionar el mes a analizar.

Configuró:
- Rango de entrada: `Meses!$A$1:$A$12`
- Vínculo con celda: `$F$1`
- Filas desplegables: 12

**2. Botón de opción (radio button):**
—Para alternar entre gráfico de transacciones y gráfico de montos.

Vinculó tres botones a la celda `$F$2`.

**3. Barra de desplazamiento:**
—Para filtrar por monto mínimo.

Configuró:
- Valor mínimo: 0
- Valor máximo: 50000
- Cambio incremental: 1000
- Cambio de página: 5000
- Vínculo con celda: `$F$3`

—Ahora, cualquier cambio en estos controles modifica las celdas vinculadas, y las fórmulas y gráficos que dependen de esas celdas se actualizan automáticamente.

### Conectando al modelo Power Pivot

—El dashboard obtendrá datos del modelo Power Pivot —dijo Valeria—. Las tablas dinámicas y los gráficos estarán conectados al modelo de datos.

Insertó una tabla dinámica conectada al modelo de Power Pivot:

1. **Insertar > Tabla dinámica > Usar modelo de datos de este libro**
2. **Campos**: Empresas_Nova[Razón Social] en filas, Transacciones[Monto] en valores
3. **Segmentación de datos** conectada: Mes, Tipo de Transacción

—Las **segmentaciones de datos** son filtros visuales. Mejores que los filtros tradicionales porque el usuario ve las opciones disponibles.

### Gráficos dinámicos

Valeria insertó un **gráfico dinámico** conectado al modelo:

- **Tipo**: Gráfico de líneas + columnas apiladas
- **Eje X**: Calendario[Mes] (tabla de calendario creada en Power Pivot)
- **Columnas**: Transacciones[Monto Normal] vs Transacciones[Monto Sospechoso]
- **Línea**: Medida DAX `% Transacciones Sospechosas`

—Los gráficos dinámicos conectados a Power Pivot son interactivos. Cuando el usuario filtra en la segmentación de datos, el gráfico se actualiza al instante.

### Indicadores KPI

—Los KPI (Key Performance Indicators) son medidas críticas que monitorean el estado del negocio. En nuestro caso, del caso.

Valeria creó cuatro tarjetas KPI:

**KPI 1: Total Transacciones Sospechosas**
```
=FORMAT([Transacciones Sospechosas], "$ #,##0")
```
Con formato condicional: Rojo si > 8,000,000

**KPI 2: Empresas Vinculadas**
```
=DISTINCTCOUNT(Empresas_Nova[ID])
```

**KPI 3: Alertas Activas**
```
=CALCULATE(
    COUNTROWS(Transacciones),
    Transacciones[Alerta] = "ACTIVA"
)
```

**KPI 4: Porcentaje de Estructuración**
```
=FORMAT(
    DIVIDE(
        [Transacciones Fraccionadas],
        [Cantidad Transacciones],
        0
    ),
    "0.00%"
)
```

### El informe cobra vida

Con todos los elementos en su lugar, el dashboard era impresionante:

```
+--------------------------------------------------+
|  🏪 MENDOZA & HIJOS   DASHBOARD FORENSE          |
|          Transacciones Analizadas: 278,431        |
+----------+---------------------------------------+
| MES: [▾] |  Transacciones por Mes                 |
| TIPO: [▾]|  ████████████████ Monto Normal         |
|          |  ████ Monto Sospechoso                 |
|          |  ─── % Sospechoso                      |
| MIN: ====|                                        |
| [===o===]|     Ene Feb Mar Abr May Jun Jul...    |
+----------+---------------------------------------+
| TOP 10 SOSPECHOSAS                               |
| 1. Inversiones Delta  .... S/ 8,432,000          |
| 2. Constructora Sur   .... S/ 2,100,000          |
| 3. Transportes Rápidos .... S/ 1,850,000          |
| ...                                               |
+------------------+------------------+-------------+
| $$ 11,672,000    | 23 Empresas      | 47 Alertas  |
| Total Sistema    | Vinculadas       | Activas     |
|                  |                  |             |
| 42.3%            | +18 vs mes ant   | 12 Nuevas   |
| % Estructuración | Crecimiento      | Esta Semana |
+------------------+------------------+-------------+
```

—Es interactivo —dijo Sofía, moviendo la barra de desplazamiento—. Puedo filtrar por mes, por tipo, por monto...

—Y todo se actualiza instantáneamente —dijo Valeria—. Eso es lo que hace profesional a un dashboard.

### Power View (opcional)

—Excel también tiene Power View, una herramienta de visualización interactiva —dijo Valeria—. Está disponible en Excel 2013 y 2016, pero Microsoft lo ha ido eliminando en versiones recientes en favor de Power BI.

—¿Deberíamos usarlo?

—No vale la pena. Power BI es el futuro. Pero el principio es el mismo: visualizaciones interactivas conectadas a un modelo de datos.

—Hablando de Power BI —dijo Sofía—. ¿Podemos exportar todo esto?

—Eso es exactamente lo que haremos mañana.

---

## Explicación técnica: Dashboard Avanzado

### ¿Qué es un dashboard?

Un dashboard (panel de control) es una representación visual de los indicadores clave de rendimiento (KPI), métricas y datos de un proceso o negocio. Un buen dashboard debe ser:

1. **Visual**: La información debe entenderse de un vistazo
2. **Interactivo**: El usuario debe poder explorar los datos
3. **Relevante**: Solo muestra lo importante
4. **Actualizado**: Los datos deben ser frescos

### Componentes de un dashboard en Excel

| Componente | Descripción | Cómo crearlo |
|------------|-------------|-------------|
| Segmentación de datos | Filtro visual | Insertar > Segmentación de datos |
| Línea de tiempo | Filtro de fechas | Insertar > Línea de tiempo |
| Cuadro combinado | Lista desplegable | Programador > Insertar > Control de formulario |
| Barra de desplazamiento | Control deslizante | Programador > Insertar > Control de formulario |
| Botón de opción | Selección exclusiva | Programador > Insertar > Control de formulario |
| Casilla de verificación | Sí/No | Programador > Insertar > Control de formulario |
| Tarjeta KPI | Indicador numérico | Cuadro de texto + fórmula |
| Gráfico dinámico | Gráfico interactivo | Insertar > Gráfico dinámico |
| Minigráfico | Micro-gráfico en celda | Insertar > Minigráficos |

### Controles de formulario vs Controles ActiveX

| Característica | Formulario | ActiveX |
|----------------|------------|---------|
| Compatibilidad | Máxima | Limitada (solo Windows) |
| Personalización | Básica | Avanzada |
| Eventos VBA | Limitados | Completos |
| Rendimiento | Más rápido | Más lento |
| Uso recomendado | Dashboards simples | Aplicaciones complejas |

### Crear un dashboard paso a paso

1. **Planificar**: Definir KPIs, fuentes de datos, audiencia
2. **Preparar datos**: Power Query para limpiar, Power Pivot para modelar
3. **Diseñar layout**: Boceto en papel o en una hoja de diseño
4. **Construir controles**: Segmentaciones, barras, listas
5. **Agregar gráficos**: Conectados al modelo de datos
6. **Implementar KPIs**: Medidas DAX con formato condicional
7. **Probar interactividad**: Verificar que todo se actualice
8. **Proteger**: Ocultar hojas de datos, proteger el dashboard

### Buenas prácticas de diseño

1. **Menos es más**: No saturar de información
2. **Jerarquía visual**: Lo más importante, más grande y arriba
3. **Colores consistentes**: Usar una paleta limitada (3-5 colores)
4. **Tipografía clara**: Sin fuentes decorativas
5. **Espacio en blanco**: Dejar respirar los elementos
6. **Etiquetas claras**: Texto descriptivo en todos los elementos
7. **Una sola pantalla**: El dashboard ideal cabe sin scroll

---

### Enigma 7.1: Diseñar un dashboard para ventas

Diseña el layout de un dashboard para el departamento de ventas que debe incluir:

- Filtro por año y mes (segmentaciones de datos)
- Gráfico de ventas por región (barras)
- Top 5 productos más vendidos (tabla)
- KPI: Total ventas, % crecimiento vs año anterior, clientes nuevos
- Control para cambiar entre vista mensual y trimestral

Describe cada elemento, su posición en el dashboard y las conexiones de datos.

### Enigma 7.2: Conectar controles al modelo

Tienes un dashboard con una barra de desplazamiento vinculada a la celda F3, un cuadro combinado vinculado a F4, y un botón de opción vinculado a F5.

Crea las fórmulas (usando funciones como INDIRECTO, FILTER, etc.) que:

1. Filtren una tabla dinámica según el valor de F3 (monto mínimo)
2. Seleccionen el mes según F4
3. Cambien el tipo de gráfico según F5 (1 = barras, 2 = líneas, 3 = circular)

### Enigma 7.3: KPIs con formato condicional

Crea las siguientes medidas DAX para KPIs y describe el formato condicional que aplicarías:

1. `Crecimiento Mensual` — % de cambio vs mes anterior
2. `Alertas Críticas` — Transacciones con monto > 100,000
3. `Concentración` — % que representa el top 3 de clientes sobre el total
4. `Tendencia` — Indicador de si las transacciones sospechosas aumentaron (▲), disminuyeron (▼) o se mantuvieron (→)

*(Soluciones en el Apéndice)*
