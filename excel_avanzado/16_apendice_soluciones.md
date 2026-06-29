
# Apéndice: Soluciones a los Enigmas

---

## Capítulo 1: Power Query

### Enigma 1.1 — Limpieza de datos bancarios

Proceso paso a paso en Power Query:

1. **Origen**: Conectar al archivo CSV
2. **Quitar filas superiores**: `Inicio > Quitar filas > Quitar filas superiores > 4`
   - Esto elimina las filas 1-4 de basura
3. **Usar primera fila como encabezados**: La fila 5 se convierte en nombres de columna
4. **Cambiar tipo de fecha**:
   - Para fechas en número (serial): `Agregar columna > Columna personalizada`
   - Fórmula M: `=Date.From(Text.From([Fecha]))`
   - O usar: `Table.TransformColumnTypes` con tipo `type date`
5. **Reemplazar valores en Monto**:
   - Reemplazar `"S/ "` por `""` (vacío)
   - Reemplazar `","` por `""` (quitar comas de miles)
   - Cambiar tipo de dato a `Número decimal`
6. **Agregar columna Tipo**:
   - `Agregar columna > Columna condicional`
   - Si `Monto < 0` entonces `"Retiro"` sino `"Depósito"`

Código M generado:

```m
let
    Origen = Csv.Document(File.Contents("C:\Datos\Banco.csv"),[Delimiter=",", Encoding=65001]),
    #"Filas superiores quitadas" = Table.Skip(Origen,4),
    #"Encabezados promovidos" = Table.PromoteHeaders(#"Filas superiores quitadas", [PromoteAllScalars=true]),
    #"Tipo de Fecha cambiado" = Table.TransformColumnTypes(#"Encabezados promovidos",{{"Fecha", type date}}),
    #"Valor S/ reemplazado" = Table.ReplaceValue(#"Tipo de Fecha cambiado","S/ ","",Replacer.ReplaceText,{"Monto"}),
    #"Valor coma reemplazado" = Table.ReplaceValue(#"Valor S/ reemplazado",",","",Replacer.ReplaceText,{"Monto"}),
    #"Tipo de Monto cambiado" = Table.TransformColumnTypes(#"Valor coma reemplazado",{{"Monto", type number}}),
    #"Columna condicional agregada" = Table.AddColumn(#"Tipo de Monto cambiado", "Tipo", each if [Monto] < 0 then "Retiro" else "Depósito"),
    #"Valor absoluto Monto" = Table.TransformColumns(#"Columna condicional agregada",{{"Monto", Number.Abs, type number}})
in
    #"Valor absoluto Monto"
```

### Enigma 1.2 — Detectar estructuración

1. **Filtrar por rango de monto**:
   - En Power Query: Filtrar columna Monto entre 20000 y 24999
   - O usar: `Table.SelectRows(#"Paso anterior", each [Monto] >= 20000 and [Monto] < 25000)`

2. **Agrupar por emisor**:
   - `Inicio > Agrupar por`
   - Agrupar por columna `Emisor`
   - Nueva columna: `Cantidad Transacciones` = Conteo de filas
   - Nueva columna: `Total Monto` = Suma de Monto

3. **Determinar si superan 100,000**:
   - Agregar columna condicional: Si `Total Monto` > 100000 entonces "Sospechoso" sino "Normal"

Código M:

```m
let
    Origen = ...,
    #"Filtro rango" = Table.SelectRows(Origen, each [Monto] >= 20000 and [Monto] < 25000),
    #"Agrupado" = Table.Group(#"Filtro rango", {"Emisor"}, {
        {"Cantidad", each Table.RowCount(_), type number},
        {"Total", each List.Sum([Monto]), type number}
    }),
    #"Clasificación" = Table.AddColumn(#"Agrupado", "Clasificación", each if [Total] > 100000 then "Sospechoso" else "Normal")
in
    #"Clasificación"
```

### Enigma 1.3 — Combinar tres fuentes

1. **Importar cada archivo**:
   - `Ventas_2024.xlsx`: Power Query > Desde Excel > Seleccionar tabla
   - `Clientes_Nova.csv`: Power Query > Desde CSV
   - `Transacciones_2024.pdf`: Power Query > Desde PDF > Seleccionar tabla

2. **Limpiar datos**:
   - Para cada tabla: promocionar encabezados, cambiar tipos, quitar filas vacías, estandarizar formatos

3. **Combinar usando RUC**:
   - Primero combinar `Ventas` con `Clientes` por RUC (Merge)
   - Luego combinar resultado con `Transacciones` por RUC
   - Expandir columnas necesarias

```m
let
    Ventas = Excel.Workbook(File.Contents("Ventas_2024.xlsx"), null, true),
    Clientes = Csv.Document(File.Contents("Clientes_Nova.csv")),
    TransaccionesPDF = Pdf.Tables(File.Contents("Transacciones_2024.pdf")),
    
    VentasLimpio = Table.PromoteHeaders(...),
    ClientesLimpio = Table.PromoteHeaders(...),
    TransaccionesLimpio = Table.PromoteHeaders(...),
    
    MergeVentasClientes = Table.NestedJoin(VentasLimpio, {"RUC"}, ClientesLimpio, {"RUC"}, "Cliente", JoinKind.LeftOuter),
    Expandido = Table.ExpandTableColumn(MergeVentasClientes, "Cliente", {"Razon_Social", "Direccion"}),
    
    MergeFinal = Table.NestedJoin(Expandido, {"RUC"}, TransaccionesLimpio, {"RUC_Emisor"}, "Transacciones", JoinKind.LeftOuter)
in
    MergeFinal
```

---

## Capítulo 2: Power Pivot

### Enigma 2.1 — Modelo de datos

**Tablas y relaciones:**

```
[Pedidos]           --ID_Cliente-->  [Clientes]
[Pedidos]           --ID_Producto--> [Productos]
[Productos]         --ID_Categoría--> [Categorías]
```

**Diagrama del modelo:**

```
┌─────────┐         ┌──────────┐
│ Pedidos │────────>│ Clientes │
│         │         │          │
│ ID_Pedido│         │ ID_Cliente│
│ Fecha   │         │ Nombre   │
│ ID_Cliente│        │ Ciudad   │
│ ID_Producto│       │ Segmento │
│ Cantidad│         └──────────┘
│ Precio  │
└────┬────┘         ┌──────────┐
     └──────────────>│Productos │
                     │          │
                     │ ID_Producto│
                     │ Nombre   │
                     │ Categoría│
                     │ Precio   │
                     └────┬─────┘
                          │
                     ┌────┴─────┐
                     │Categorías│
                     │          │
                     │ ID_Cat   │
                     │ Nombre   │
                     │ Dpto     │
                     └──────────┘
```

**Cardinalidad:**
- Pedidos:Clientes — Muchos a uno (un cliente tiene muchos pedidos)
- Pedidos:Productos — Muchos a uno (un producto está en muchos pedidos)
- Productos:Categorías — Muchos a uno (una categoría tiene muchos productos)

### Enigma 2.2 — Medidas exploratorias

```dax
Total Ventas:=SUMX(Pedidos, Pedidos[Cantidad] * Pedidos[Precio_Unitario])

Cantidad Pedidos:=COUNTROWS(Pedidos)

Ticket Promedio:=DIVIDE([Total Ventas], [Cantidad Pedidos], 0)

Productos Vendidos:=SUM(Pedidos[Cantidad])

Precio Promedio:=DIVIDE([Total Ventas], [Productos Vendidos], 0)
```

### Enigma 2.3 — Análisis de relación

**1. Cliente con más ingresos:**
   - En tabla dinámica: Clientes[Nombre] en filas, [Total Ventas] en valores
   - Ordenar descendente por Total Ventas
   - El primer cliente de la lista es el que más ingresos genera

**2. Categoría con ticket promedio más alto:**
   - En tabla dinámica: Categorías[Nombre_Categoría] en filas, [Ticket Promedio] en valores
   - La categoría con el ticket más alto es la que tiene el promedio por pedido más elevado
   - Nota: La relación va de Pedidos → Productos → Categorías (relación de dos saltos, soportada por Power Pivot)

**3. Correlación segmento y frecuencia:**
   - En tabla dinámica: Clientes[Segmento] en filas, Clientes[ID_Cliente] (DistinctCount) como "Clientes", [Cantidad Pedidos] como "Total Pedidos"
   - Agregar medida: `Frecuencia:=DIVIDE([Cantidad Pedidos], DISTINCTCOUNT(Clientes[ID_Cliente]))`
   - Comparar la frecuencia entre segmentos para ver diferencias

---

## Capítulo 3: DAX

### Enigma 3.1 — CALCULATE en acción

```dax
Ventas Región Norte:=CALCULATE(SUM(Ventas[Monto]), Ventas[Región] = "Norte")

Ventas Canal Online:=CALCULATE(SUM(Ventas[Monto]), Ventas[Canal] = "Online")

Ventas Sin Región Sur:=CALCULATE(SUM(Ventas[Monto]), Ventas[Región] <> "Sur")

% Ventas Online:=DIVIDE(
    [Ventas Canal Online],
    CALCULATE(SUM(Ventas[Monto]), ALL(Ventas[Canal])),
    0
)
```

### Enigma 3.2 — Iteradores y FILTER

```dax
Ventas con Descuento:=SUMX(Ventas, Ventas[Monto] * 0.95)

Ventas Premium:=CALCULATE(
    SUM(Ventas[Monto]),
    Clientes[Categoría] = "Premium"
)

Productos Estrella:=COUNTROWS(
    FILTER(
        VALUES(Ventas[ID_Producto]),
        CALCULATE(SUM(Ventas[Monto])) > 50000
    )
)

Transacciones Grandes:=SUMX(
    FILTER(Ventas, Ventas[Monto] > 10000),
    Ventas[Monto]
)
```

### Enigma 3.3 — Análisis forense

```dax
-- 1. Estructuración: transacciones justo debajo de S/25,000 agrupadas
Transacciones Fraccionadas:=COUNTROWS(
    FILTER(
        Transacciones,
        Transacciones[Monto] >= 20000 &&
        Transacciones[Monto] < 25000
    )
)

-- 2. Clientes que aparecen en múltiples empresas del mismo grupo
Clientes Multiempresa:=COUNTROWS(
    FILTER(
        VALUES(Transacciones[ID_Cliente]),
        CALCULATE(
            DISTINCTCOUNT(Empresas[ID]),
            Empresas[Grupo] = "Nova"
        ) > 1
    )
)

-- 3. % de transacciones con personas naturales vs jurídicas
% Personas Naturales:=DIVIDE(
    CALCULATE(COUNTROWS(Transacciones), Clientes[Tipo] = "Persona Natural"),
    CALCULATE(COUNTROWS(Transacciones), ALL(Clientes[Tipo])),
    0
)

% Personas Jurídicas:=DIVIDE(
    CALCULATE(COUNTROWS(Transacciones), Clientes[Tipo] = "Jurídica"),
    CALCULATE(COUNTROWS(Transacciones), ALL(Clientes[Tipo])),
    0
)
```

---

## Capítulo 4: VBA

### Enigma 4.1 — Macro de limpieza automática

```vba
Option Explicit

Sub LimpiarFilasVacias()
    Dim ws As Worksheet
    Dim i As Long
    Dim ultimaFila As Long
    Dim totalEliminadas As Long
    
    totalEliminadas = 0
    
    For Each ws In ThisWorkbook.Worksheets
        ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
        
        ' Recorrer de abajo hacia arriba para no alterar índices
        For i = ultimaFila To 1 Step -1
            If ws.Cells(i, 1).Value = "" Or IsEmpty(ws.Cells(i, 1)) Then
                ws.Rows(i).Delete
                totalEliminadas = totalEliminadas + 1
            End If
        Next i
    Next ws
    
    MsgBox "Proceso completado." & vbCrLf & _
           "Filas eliminadas: " & totalEliminadas, _
           vbInformation, "Limpieza automática"
End Sub
```

### Enigma 4.2 — Función personalizada de riesgo

```vba
Option Explicit

Function NivelRiesgo(monto As Double, frecuencia As Integer, origen As String) As String
    ' Determina nivel de riesgo de una transacción
    ' Alto: monto > 20000 Y frecuencia > 3 Y origen = "Delta"
    ' Medio: monto > 10000 O frecuencia > 5
    ' Bajo: cualquier otro caso
    
    If monto > 20000 And frecuencia > 3 And UCase(origen) = "DELTA" Then
        NivelRiesgo = "Alto"
    ElseIf monto > 10000 Or frecuencia > 5 Then
        NivelRiesgo = "Medio"
    Else
        NivelRiesgo = "Bajo"
    End If
End Function
```

### Enigma 4.3 — Generador de informes

```vba
Option Explicit

Sub GenerarReporteSemanal()
    Dim semana As String
    Dim wsDatos As Worksheet
    Dim wsReporte As Worksheet
    Dim rangoDatos As Range
    Dim nombreArchivo As String
    Dim rutaGuardado As String
    
    ' 1. Preguntar semana
    semana = InputBox("Ingrese la semana a reportar (ej: 2026-04):", _
                      "Generar Reporte Semanal")
    If semana = "" Then Exit Sub
    
    ' 2. Referenciar hoja de datos
    Set wsDatos = ThisWorkbook.Sheets("Transacciones")
    
    ' 3. Aplicar filtro
    If wsDatos.AutoFilterMode Then wsDatos.AutoFilterMode = False
    wsDatos.Range("A1").AutoFilter Field:=1, Criteria1:=semana
    
    ' 4. Copiar datos filtrados
    Set rangoDatos = wsDatos.AutoFilter.Range
    rangoDatos.Copy
    
    ' 5. Crear nueva hoja
    On Error Resume Next
    Set wsReporte = ThisWorkbook.Sheets("Reporte")
    If wsReporte Is Nothing Then
        Set wsReporte = ThisWorkbook.Sheets.Add(After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count))
        wsReporte.Name = "Reporte"
    Else
        wsReporte.Cells.Clear
    End If
    On Error GoTo 0
    
    ' 6. Pegar datos
    wsReporte.Range("A1").PasteSpecial Paste:=xlPasteValues
    Application.CutCopyMode = False
    
    ' 7. Agregar encabezado con fecha del sistema
    wsReporte.Range("A1").EntireRow.Insert
    wsReporte.Range("A1").Value = "Reporte Semanal - Semana: " & semana
    wsReporte.Range("B1").Value = "Generado: " & Now
    wsReporte.Range("A1:B1").Font.Bold = True
    wsReporte.Range("A1:B1").Font.Size = 14
    
    ' 8. Configurar impresión
    With wsReporte.PageSetup
        .Orientation = xlLandscape
        .FitToPagesWide = 1
        .FitToPagesTall = 1
    End With
    
    ' 9. Guardar libro
    nombreArchivo = "Reporte_Semana_" & semana & ".xlsx"
    rutaGuardado = ThisWorkbook.Path & "\" & nombreArchivo
    ThisWorkbook.SaveCopyAs rutaGuardado
    
    ' 10. Quitar filtro
    wsDatos.AutoFilterMode = False
    
    MsgBox "Reporte generado exitosamente:" & vbCrLf & rutaGuardado, _
           vbInformation, "Completado"
End Sub
```

---

## Capítulo 5: Matrices Dinámicas y LAMBDA

### Enigma 5.1 — Filtro de transacciones sospechosas

```excel
=LET(
    datos, Ventas,
    filtrados, FILTER(datos, CHOOSECOLS(datos, 4) > 1000),  // Monto > 1000
    ordenados, SORT(filtrados, 4, -1),  // Ordenar por Monto desc
    seleccion, CHOOSECOLS(ordenados, 2, 3, 4),  // Cliente, Producto, Monto
    top10, TAKE(seleccion, 10),
    top10
)
```

### Enigma 5.2 — Función LAMBDA de análisis

Crear en el Administrador de nombres:

```
Nombre: ANALIZAR_CLIENTE
Ámbito: Libro
Se refiere a: =LAMBDA(nombre_cliente, rango,
    LET(
        filtro, FILTER(rango, CHOOSECOLS(rango, 2) = nombre_cliente),
        montos, CHOOSECOLS(filtro, 4),
        HSTACK(
            nombre_cliente,
            SUM(montos),
            ROWS(filtro),
            MAX(montos)
        )
    )
)
```

Uso: `=ANALIZAR_CLIENTE("Sofía Mendoza", A1:E100)`

### Enigma 5.3 — Detección de anomalías con LET y MAP

```excel
=LET(
    montos, Ventas[Monto],
    promedio, AVERAGE(montos),
    umbral, promedio * 3,
    clasificacion, MAP(montos, LAMBDA(m, IF(m > umbral, "ANÓMALA", "NORMAL"))),
    HSTACK(montos, clasificacion)
)
```

---

## Capítulo 6: Solver y Escenarios

### Enigma 6.1 — Optimización de producción

Configuración de Solver:

- **Celda objetivo**: $F$1 (Utilidad Total)
- **Valor**: Máximo
- **Celdas variables**: $B$1:$B$2 (Cantidad A, Cantidad B)
- **Restricciones**:
  - $B$1 >= 0 (Entero opcional)
  - $B$2 >= 0 (Entero opcional)
  - $B$1 <= 60 (Demanda máxima A)
  - $B$2 <= 40 (Demanda máxima B)
  - 2*$B$1 + 3*$B$2 <= 200 (Horas máquina)
  - 1*$B$1 + 2*$B$2 <= 160 (Horas mano de obra)

**Resultado esperado**: A=60, B=26.67 → pero como enteros: A=60, B=26 → Utilidad = 50*60 + 80*26 = S/ 5,080

### Enigma 6.2 — Análisis de escenarios

Crear escenarios en Administrador de escenarios:

**Escenario Pesimista**: Ventas=800000, CostoFijo=400000, MargenVariable=0.3
**Escenario Moderado**: Ventas=1200000, CostoFijo=350000, MargenVariable=0.4
**Escenario Optimista**: Ventas=1800000, CostoFijo=300000, MargenVariable=0.5

Fórmula de utilidad: `= Ventas * MargenVariable - CostoFijo`

Informe de resumen mostrará:
- Pesimista: 800000*0.3 - 400000 = -160,000 (pérdida)
- Moderado: 1200000*0.4 - 350000 = 130,000
- Optimista: 1800000*0.5 - 300000 = 600,000

### Enigma 6.3 — Tabla de sensibilidad

1. Celda B1: fórmula de Valor Futuro
   - `=VA * (1 + Tasa)^Plazo` donde VA=100000, Tasa y Plazo son celdas de entrada
2. Columna A (A2:A12): tasas de 5% a 15%
3. Fila 1 (B1:F1): plazos de 1 a 5 años
4. Celda B2: `=TABLE(B1, A2)` donde B1=celda de tasa, A2=celda de plazo
5. Seleccionar rango B2:F12 y completar la tabla de datos

Resultados (aproximados):

| Tasa \ Años | 1 año | 2 años | 3 años | 4 años | 5 años |
|-------------|-------|--------|--------|--------|--------|
| 5% | 105,000 | 110,250 | 115,763 | 121,551 | 127,628 |
| 10% | 110,000 | 121,000 | 133,100 | 146,410 | 161,051 |
| 15% | 115,000 | 132,250 | 152,088 | 174,901 | 201,136 |

---

## Capítulo 7: Dashboard

### Enigma 7.1 — Dashboard de ventas

**Layout propuesto:**

```
+----------------------------------------------------------+
| LOGO  DASHBOARD DE VENTAS - 2026                          |
+--------+-------------------------------------------------+
| [Año ▾] | GRÁFICO PRINCIPAL                               |
| [Mes ▾] | Ventas por Región (Barras apiladas)             |
|         |                                                  |
| [Radio] |                                                  |
| ○ Mensual                                                  |
| ○ Trimestral                                              |
+---------+-------------------------------------------------+
| KPI 1      | KPI 2           | KPI 3           |
| S/ 2.5M    | 15.3%           | 342             |
| Total Ventas| % Crecimiento  | Clientes Nuevos |
|            | vs Año Ant.     |                 |
+------------+-----------------+-----------------+
| TOP 5 PRODUCTOS                                          |
| 1. Producto A  S/ 450,230                                 |
| 2. Producto B  S/ 380,100                                 |
| ...                                                       |
+----------------------------------------------------------+
```

**Conexiones:**
- Segmentaciones de año y mes conectadas a tabla Calendario
- Gráfico de barras conectado a modelo Power Pivot
- KPIs con medidas DAX desde Power Pivot
- Botón de opción vinculado a celda que cambia campo en tabla dinámica

### Enigma 7.2 — Conectar controles

```excel
' Fórmula para filtrar por monto mínimo (F3 = barra de desplazamiento)
=FILTER(Transacciones, Transacciones[Monto] >= F3)

' Fórmula para seleccionar mes (F4 = cuadro combinado, 1-12)
=FILTER(Transacciones, MES(Transacciones[Fecha]) = F4)

' Fórmula para cambiar tipo de gráfico (F5 = botón de opción, 1/2/3)
' Usar función SWITCH:
=SWITCH(F5,
    1, "Gráfico de barras",
    2, "Gráfico de líneas",
    3, "Gráfico circular",
    "Seleccione un tipo"
)
```

### Enigma 7.3 — KPIs con formato condicional

```dax
Crecimiento Mensual:=DIVIDE(
    [Total Ventas],
    CALCULATE([Total Ventas], PREVIOUSMONTH(Calendario[Fecha])),
    0
) - 1

Alertas Críticas:=CALCULATE(
    COUNTROWS(Transacciones),
    Transacciones[Monto] > 100000
)

Concentración:=DIVIDE(
    CALCULATE([Total Ventas],
        TOPN(3, VALUES(Clientes[Nombre]), [Total Ventas])
    ),
    CALCULATE([Total Ventas], ALL(Clientes)),
    0
)

Tendencia:=
VAR VentasMesActual = [Total Ventas]
VAR VentasMesAnterior = CALCULATE([Total Ventas], PREVIOUSMONTH(Calendario[Fecha]))
RETURN
    IF(VentasMesActual > VentasMesAnterior, "▲ Aumentó",
    IF(VentasMesActual < VentasMesAnterior, "▼ Disminuyó",
    "→ Sin cambios"))
```

**Formato condicional:**

| KPI | Regla | Color/Icono |
|-----|-------|-------------|
| Crecimiento Mensual | > 5% | Verde |
| | 0% a 5% | Amarillo |
| | < 0% | Rojo |
| Alertas Críticas | > 10 | Rojo (fondo) |
| | 5 a 10 | Amarillo |
| | < 5 | Verde |
| Concentración | > 50% | Rojo (alta dependencia) |
| | 25% a 50% | Amarillo |
| | < 25% | Verde (diversificado) |
| Tendencia | Aumentó | ▲ Verde |
| | Disminuyó | ▼ Rojo |
| | Sin cambios | → Gris |

---

## Capítulo 8: Power BI

### Enigma 8.1 — Migrar modelo a Power BI

**Pasos:**
1. Abrir Power BI Desktop
2. Inicio > Obtener datos > Excel
3. Seleccionar el archivo .xlsx con el modelo Power Pivot
4. En el navegador, seleccionar la opción "Seleccionar elementos relacionados" o elegir manualmente las tablas
5. Hacer clic en "Cargar"

**Elementos que se conservan:**
- Tablas y sus datos
- Relaciones entre tablas
- Medidas DAX
- Columnas calculadas
- Jerarquías

**Elementos que se pierden:**
- Formato de hojas de Excel (irrelevante en Power BI)
- Tablas dinámicas (se reemplazan por visualizaciones)
- Macros VBA (Power BI no ejecuta VBA)
- Gráficos de Excel (se reemplazan por visuales de Power BI)
- Controles de formulario (se reemplazan por segmentaciones)

### Enigma 8.2 — Visualizaciones

1. Evolución de ventas en 12 meses → **Gráfico de líneas**
2. Comparación de ventas por región → **Gráfico de barras** (o mapa)
3. Proporción del presupuesto por departamento → **Gráfico circular** o **Treemap**
4. Relación entre precio y cantidad vendida → **Gráfico de dispersión (Scatter)**
5. Progreso hacia un objetivo de ventas → **Medidor (Gauge)**
6. Cambio acumulado mes a mes → **Gráfico de cascada (Waterfall)**

### Enigma 8.3 — RLS para el caso forense

```dax
-- Rol: Fiscal Jefe
-- (sin filtro) - Ve todos los datos

-- Rol: Investigador
[Transacciones Restringidas] = 
FILTER(
    Transacciones,
    Transacciones[Monto] > 20000
)

-- Rol: Auditor Externo
[Empresas Restringidas] = 
FILTER(
    Empresas_Nova,
    Empresas_Nova[Tipo] <> "Fantasma"
)
```

---

## Capítulo 9: Auditoría y Seguridad

### Enigma 9.1 — Auditoría de fórmulas

1. **Rastrear precedentes**: La fórmula depende de B2, C2, y del rango Precios!$A$2:$B$100
2. **Qué pasa si B2 está vacío**: SI(B2>0) → es FALSO → muestra "SIN DATOS"
3. **Verificar duplicados en Precios**: Usar formato condicional o =CONTAR.SI(Precios!$A$2:$A$100, A2) > 1
4. **Evaluar paso a paso**: Con B2=5, C2=10:
   - Paso 1: SI(5>0, ...) → VERDADERO
   - Paso 2: BUSCARV(5, Precios!$A$2:$B$100, 2, FALSO) → busca 5 en A, devuelve valor de B
   - Paso 3: resultado_buscarv * 10 → resultado final

### Enigma 9.2 — Protección del modelo

**Esquema de protección:**

1. **Tres niveles de acceso**:
   - Nivel 1 (Analistas): Solo ven dashboard y tablas de reporte. Sin acceso a fórmulas, datos crudos ni VBA
   - Nivel 2 (Administradores): Acceso completo a fórmulas y medidas. Pueden modificar el modelo
   - Nivel 3 (Auditoría): Solo lectura, con capacidad de verificar integridad

2. **Implementación**:
   - Separar en 4 hojas: DatosCrudos, Modelo, Dashboard, Configuración
   - Proteger DatosCrudos: solo administradores
   - Proteger Modelo (Power Pivot): contraseña separada
   - Dashboard: celdas desbloqueadas solo para filtros/controles
   - Configuración: oculta y protegida

3. **Log de cambios**: Macro VBA que registra en hoja AuditLog protegida

4. **Integridad**: Firma digital + backup versionado diario

### Enigma 9.3 — Log de auditoría mejorado

```vba
Option Explicit

Private Sub Workbook_SheetChange(ByVal Sh As Object, ByVal Target As Range)
    Dim wsLog As Worksheet
    Dim ultimaFila As Long
    
    ' Ignorar hoja de log
    If Sh.Name = "AuditLog" Then Exit Sub
    
    ' Solo cambios en una celda
    If Target.Count > 1 Then Exit Sub
    
    ' Ignorar si el valor no cambió realmente
    Dim oldValue As Variant
    oldValue = Application.Undo ' No siempre funciona, alternativa: almacenar en variable estática
    
    ' Crear o referenciar log
    On Error Resume Next
    Set wsLog = ThisWorkbook.Sheets("AuditLog")
    If wsLog Is Nothing Then
        Set wsLog = ThisWorkbook.Sheets.Add
        wsLog.Name = "AuditLog"
        wsLog.Range("A1:F1").Value = Array("Timestamp (UTC-5)", "Usuario", "Hoja", "Celda", "Valor Anterior", "Valor Nuevo")
        wsLog.Range("A1:F1").Font.Bold = True
        wsLog.Range("A1:F1").Interior.Color = RGB(220, 220, 220)
        wsLog.Protect Password:="LogPass2026"
    End If
    On Error GoTo 0
    
    ' Registrar
    ultimaFila = wsLog.Cells(wsLog.Rows.Count, 1).End(xlUp).Row + 1
    
    wsLog.Unprotect Password:="LogPass2026"
    
    wsLog.Cells(ultimaFila, 1).Value = Format(Now, "yyyy-mm-dd hh:mm:ss") & " UTC-5"
    wsLog.Cells(ultimaFila, 2).Value = Environ("UserName")
    wsLog.Cells(ultimaFila, 3).Value = Sh.Name
    wsLog.Cells(ultimaFila, 4).Value = Target.Address
    ' Intentar obtener valor anterior (limitación: no siempre funciona)
    On Error Resume Next
    wsLog.Cells(ultimaFila, 5).Value = Application.Undo
    On Error GoTo 0
    wsLog.Cells(ultimaFila, 6).Value = Target.Value
    
    wsLog.Protect Password:="LogPass2026"
    
    ' Mensaje de confirmación
    Application.StatusBar = "Cambio registrado en AuditLog: " & Target.Address
End Sub
```

---

## Capítulo 10: Proyecto Integrador

Los ejercicios del capítulo 10 son de diseño abierto. Aquí hay guías:

### Enigma 10.1 — Proyecto integrador

**Ejemplo de estructura:**

| Componente | Descripción |
|------------|-------------|
| Problema | Analizar rentabilidad de 3 sucursales |
| Fuentes | 4 archivos CSV de ventas, 1 Excel de gastos, 1 BD Access de inventario |
| Modelo | 5 tablas: Ventas, Gastos, Sucursales, Productos, Calendario |
| Medidas DAX | Rentabilidad, Margen, Crecimiento, Participación |
| Automatización | Macro que importa datos, actualiza modelo y envía correo |
| Dashboard | Power BI con KPIs, mapas, gráficos de tendencia |
| Seguridad | RLS: cada sucursal ve solo sus datos |

### Enigma 10.2 — Continuidad del caso Nova

**Plan de implementación:**

1. **Detección automática**:
   - Power Query programado para importar datos de Delta cada lunes 8am
   - Medida DAX que compara nuevas transacciones con patrones históricos
   - Alerta: si hay 3+ transacciones entre 20K-25K del mismo emisor en una semana

2. **Alertas automáticas**:
   - VBA que envía correo con Outlook si se detecta patrón
   - Power BI con alertas por correo (suscripciones condicionales)

3. **Informe semanal**:
   - Power BI publicado con actualización programada
   - Suscripción: cada lunes a las 9am enviar PDF por correo al fiscal

4. **Histórico de alertas**:
   - Tabla en Power Pivot: Alertas(ID, Fecha, Tipo, Descripción, Estado)
   - VBA: cada alerta se registra automáticamente en la tabla
   - Dashboard con histórico y estadísticas de alertas

### Enigma 10.3 — Proyección de carrera

**Plan de 6 meses:**

| Mes | Objetivo | Recursos |
|-----|----------|----------|
| 1-2 | Dominar Power Query y Power Pivot | Documentación Microsoft, curso Udemy |
| 3 | DAX avanzado (time intelligence, variables) | SQLBI.com, daxpatterns.com |
| 4 | Power BI Desktop + RLS | PL-300 path de Microsoft Learn |
| 5 | Proyecto real en trabajo o voluntariado | ONG local, negocio familiar |
| 6 | Certificación PL-300 o MO-201 | Examen de certificación |

**Proyecto real para el portafolio:** Dashboard de finanzas personales o análisis de ventas de un negocio local.
