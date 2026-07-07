
# Capítulo 4: Automatización Necesaria

## Macros y VBA Básico

—No podemos estar haciendo esto manualmente cada semana —dijo Valeria, frotándose los ojos—. Los datos de Delta se actualizan cada viernes. Necesito generar los informes de inmediato.

—¿Cuánto tiempo toma hacerlo manual? —preguntó Sofía.

—Tres horas. Entre importar los nuevos datos, actualizar las consultas, refrescar las tablas dinámicas, formatear los informes y exportar a PDF.

—¿Y si lo automatizamos?

—Con VBA —dijo Valeria—, podemos hacerlo en cinco minutos.

### Grabando la primera macro

Valeria abrió la pestaña **Programador** en Excel. (Si no está visible: **Archivo > Opciones > Personalizar cinta de opciones > Marcar "Programador"**).

—VBA significa Visual Basic for Applications. Es el lenguaje de programación integrado en Excel. Con él, podemos decirle a Excel que haga exactamente lo que queremos.

—Pero no sé programar —dijo Carlos.

—No importa. Vamos a empezar con la **grabadora de macros**. Haz todo manualmente una vez, y Excel escribe el código por ti.

Valeria hizo clic en **Grabar macro**, nombró la macro `ActualizarInformes` y comenzó a realizar la secuencia:

1. **Datos > Actualizar todo** (para refrescar Power Query)
2. **Power Pivot > Actualizar todo** (para refrescar el modelo)
3. **Seleccionar hoja "Resumen"**
4. **Seleccionar tabla dinámica > Actualizar**
5. **Dar formato a celdas** (negritas, bordes, colores)
6. **Exportar hoja a PDF**

Cuando terminó, hizo clic en **Detener grabación**.

—Ahora veamos qué escribió Excel.

Abrió el editor de VBA con **Alt + F11**.

```vba
Sub ActualizarInformes()
' ActualizarInformes Macro
'
    ActiveWorkbook.RefreshAll
    Sheets("Resumen").Select
    ActiveSheet.PivotTables("TablaDinámica1").PivotCache.Refresh
    Range("A1:F20").Select
    Selection.Font.Bold = True
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
    ActiveSheet.ExportAsFixedFormat Type:=xlTypePDF, _
        Filename:="C:\Informes\Resumen_Semanal.pdf"
End Sub
```

—El código tiene errores —dijo Valeria—. Usa `.Select` y `.Activate`, que son lentos y propensos a errores. Vamos a mejorarlo.

### Escribiendo VBA limpio

Valeria borró el código grabado y escribió desde cero:

```vba
Sub ActualizarInformes()
    ' Propósito: Actualizar datos, formatear y exportar informe semanal
    ' Autor: Valeria Rivas
    ' Fecha: Enero 2026
    
    Dim rptPath As String
    Dim ws As Worksheet
    
    ' 1. Configurar ruta de exportación
    rptPath = "C:\Informes\Resumen_" & Format(Date, "yyyymmdd") & ".pdf"
    
    ' 2. Actualizar todas las conexiones de datos
    ActiveWorkbook.RefreshAll
    Application.CalculateUntilAsyncQueriesDone
    
    ' 3. Referenciar la hoja de resumen
    Set ws = ThisWorkbook.Sheets("Resumen")
    
    ' 4. Actualizar tabla dinámica
    ws.PivotTables("TablaDinámica1").PivotCache.Refresh
    
    ' 5. Formatear rango
    With ws.Range("A1:F20")
        .Font.Bold = True
        .Font.Size = 11
        .HorizontalAlignment = xlCenter
        With .Borders(xlEdgeBottom)
            .LineStyle = xlContinuous
            .Weight = xlMedium
            .Color = RGB(0, 51, 102)
        End With
    End With
    
    ' 6. Exportar a PDF
    ws.ExportAsFixedFormat _
        Type:=xlTypePDF, _
        Filename:=rptPath, _
        Quality:=xlQualityStandard, _
        IncludeDocProperties:=True
        
    ' 7. Mensaje de confirmación
    MsgBox "Informe generado exitosamente: " & rptPath, vbInformation, "Completado"
    
    ' 8. Limpiar objetos
    Set ws = Nothing
End Sub
```

—Esto es más profesional —dijo Valeria—. Usa variables, evita Select, maneja objetos correctamente y da retroalimentación al usuario.

—¿Qué son esas líneas con `Dim`? —preguntó Carlos.

—`Dim` declara variables. En VBA, las variables pueden ser de varios tipos: String (texto), Integer (número entero), Long (entero grande), Double (decimal), Date (fecha), Boolean (verdadero/falso), Worksheet (hoja), Range (rango de celdas), etc.

### Variables y tipos de datos

—En VBA, declarar variables es opcional pero muy recomendable —dijo Valeria—. Si usas `Option Explicit` al inicio del módulo, VBA te obligará a declarar todas las variables. Esto evita errores tontos.

```vba
Option Explicit

Sub VariablesEjemplo()
    Dim nombre As String
    Dim edad As Integer
    Dim salario As Double
    Dim activo As Boolean
    Dim fechaIngreso As Date
    Dim rangoDatos As Range
    
    nombre = "Sofía Mendoza"
    edad = 35
    salario = 48500.50
    activo = True
    fechaIngreso = #1/15/2024#
    
    ' Asignar rango
    Set rangoDatos = ThisWorkbook.Sheets("Datos").Range("A1:A100")
    
    ' Mostrar valores
    MsgBox "Nombre: " & nombre & vbCrLf & _
           "Edad: " & edad & vbCrLf & _
           "Salario: S/ " & salario
End Sub
```

### Estructuras de control

—Para procesar datos, necesitas loops y condicionales.

**If...Then...Else:**

```vba
Sub ClasificarMontos()
    Dim monto As Double
    Dim categoria As String
    
    ' Leer valor de celda A1
    monto = ThisWorkbook.Sheets("Datos").Range("A1").Value
    
    If monto > 25000 Then
        categoria = "Reportable"
    ElseIf monto >= 20000 Then
        categoria = "Sospechoso"
    Else
        categoria = "Normal"
    End If
    
    ' Escribir resultado en B1
    ThisWorkbook.Sheets("Datos").Range("B1").Value = categoria
End Sub
```

**For...Next:**

```vba
Sub AnalizarTransacciones()
    Dim i As Long
    Dim ultimaFila As Long
    Dim ws As Worksheet
    Dim monto As Double
    Dim contSospechosas As Long
    
    Set ws = ThisWorkbook.Sheets("Transacciones")
    contSospechosas = 0
    
    ' Encontrar última fila con datos
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    
    ' Loop de fila 2 a la última (asumiendo fila 1 = encabezados)
    For i = 2 To ultimaFila
        monto = ws.Cells(i, 3).Value  ' Columna C = Monto
        
        If monto >= 20000 And monto < 25000 Then
            contSospechosas = contSospechosas + 1
            ws.Cells(i, 5).Value = "SOSPECHOSA"  ' Columna E = Marca
        End If
    Next i
    
    MsgBox "Se encontraron " & contSospechosas & " transacciones sospechosas.", _
           vbInformation, "Análisis completado"
End Sub
```

**For Each...Next (para recorrer objetos):**

```vba
Sub FormatearTodasLasHojas()
    Dim ws As Worksheet
    
    For Each ws In ThisWorkbook.Worksheets
        With ws.Range("A1:Z1")
            .Font.Bold = True
            .Font.Color = RGB(255, 255, 255)
            .Interior.Color = RGB(0, 51, 102)
            .HorizontalAlignment = xlCenter
        End With
    Next ws
    
    MsgBox "Formato aplicado a todas las hojas."
End Sub
```

### Trabajando con rangos

Valeria mostró las diferentes formas de referenciar celdas:

```vba
Sub RangosEjemplo()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Datos")
    
    ' Diferentes formas de referenciar celdas
    ws.Range("A1").Value = "Texto"              ' Una celda
    ws.Range("A1:B10").Value = "Texto"          ' Rango
    ws.Range("A:A").Font.Bold = True            ' Columna completa
    ws.Rows(1).Font.Bold = True                 ' Fila completa
    ws.Cells(1, 1).Value = "Celda A1"           ' Fila, Columna
    ws.Cells(1, "A").Value = "Celda A1"         ' Fila, Letra
    
    ' Rango dinámico (desde A1 hasta última fila con datos)
    Dim ultimaFila As Long
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    ws.Range("A1:A" & ultimaFila).Select
    
    ' Limpiar objetos
    Set ws = Nothing
End Sub
```

### Creando funciones personalizadas (UDF)

—También podemos crear funciones que se usen como fórmulas de Excel —dijo Valeria.

```vba
Function EsSospechosa(monto As Double) As String
    ' Función personalizada que clasifica montos
    ' Uso en Excel: =EsSospechosa(A2)
    
    If monto >= 20000 And monto < 25000 Then
        EsSospechosa = "SOSPECHOSA"
    ElseIf monto >= 25000 Then
        EsSospechosa = "REPORTABLE"
    Else
        EsSospechosa = "NORMAL"
    End If
End Function

Function FormatearRUC(ruc As String) As String
    ' Formatea RUC peruano: 12345678901 -> 12-34567890-1
    
    If Len(ruc) = 11 Then
        FormatearRUC = Left(ruc, 2) & "-" & Mid(ruc, 3, 8) & "-" & Right(ruc, 1)
    Else
        FormatearRUC = ruc ' Devuelve original si no tiene 11 dígitos
    End If
End Function
```

### Eventos: código que se ejecuta automáticamente

—Los eventos son subrutinas que se ejecutan cuando ocurre algo: abrir el libro, cambiar una celda, hacer clic, etc.

```vba
' Este código va en el módulo de ThisWorkbook
Private Sub Workbook_Open()
    ' Se ejecuta al abrir el archivo
    MsgBox "Bienvenido al Sistema de Análisis Forense v2.0", vbInformation
    ActualizarInformes ' Llama a la macro que creamos antes
End Sub

' Este código va en el módulo de una hoja específica
Private Sub Worksheet_Change(ByVal Target As Range)
    ' Se ejecuta cuando cambia cualquier celda
    If Target.Column = 3 Then ' Columna C (Monto)
        If Target.Value >= 20000 Then
            MsgBox "Transacción de alto valor detectada: S/ " & Target.Value, _
                   vbExclamation, "Alerta"
        End If
    End If
End Sub
```

### La automatización que cambió todo

Con el código de Valeria, el proceso que antes tomaba tres horas ahora tomaba tres minutos. Cada viernes, Sofía ejecutaba la macro y recibía un PDF completo con:

- Resumen ejecutivo de la semana
- Tabla de transacciones sospechosas nuevas
- Gráfico de tendencias
- Alertas de estructuración

—Es hermoso —dijo Sofía—. Poderoso. Pero todavía hay algo que me preocupa.

—¿Qué? —preguntó Carlos.

—Nova está moviendo dinero constantemente. Cada semana aparecen nuevas transacciones. Necesito una forma de crear mis propias funciones de análisis sin depender de VBA.

—Ah, quieres funciones personalizadas en las celdas —dijo Valeria—. LAMBDA.

—¿LAMBDA? —preguntó Carlos.

—La función que permite crear tus propias funciones directamente en Excel, sin una línea de VBA. Eso, combinado con matrices dinámicas, es el siguiente nivel.

---

## Explicación técnica: Macros y VBA

### ¿Qué es VBA?

**Visual Basic for Applications (VBA)** es el lenguaje de programación de Microsoft Office. Permite automatizar tareas repetitivas, crear funciones personalizadas, interactuar con bases de datos y controlar completamente el entorno de Excel.

### Cómo acceder al Editor de VBA

| Método | Acción |
|--------|--------|
| Alt + F11 | Abre el editor VBA |
| Programador > Visual Basic | Desde la cinta de opciones |
| Programador > Grabar macro | Graba acciones como código VBA |

### Componentes del Editor VBA

1. **Explorador de proyectos**: Muestra todos los libros abiertos y sus componentes
2. **Ventana de código**: Donde se escribe el código
3. **Ventana de propiedades**: Propiedades del objeto seleccionado
4. **Ventana inmediato**: Para pruebas rápidas (Ctrl + G)

### Estructura de un módulo VBA

```vba
Option Explicit  ' Obliga a declarar variables

Declaraciones a nivel de módulo

Sub NombreMacro()
    ' Cuerpo de la macro
End Sub

Function NombreFuncion(param1 As Tipo) As Tipo
    ' Cuerpo de la función
End Function
```

### Tipos de datos principales

| Tipo | Descripción | Rango |
|------|-------------|-------|
| String | Texto | Hasta ~2 mil millones caracteres |
| Integer | Número entero | -32,768 a 32,767 |
| Long | Entero grande | -2,147,483,648 a 2,147,483,647 |
| Single | Decimal (precisión simple) | ±1.5E-45 a ±3.4E38 |
| Double | Decimal (precisión doble) | ±5.0E-324 a ±1.7E308 |
| Currency | Monetario | -922,337,203,685,477 a 922,337,203,685,477 |
| Date | Fecha y hora | 1/1/100 a 12/31/9999 |
| Boolean | Verdadero/Falso | True o False |
| Variant | Cualquier tipo | Flexible pero lento |

### Buenas prácticas en VBA

1. **Usar Option Explicit** al inicio de cada módulo
2. **Evitar Select y Activate** — referenciar objetos directamente
3. **Declarar todas las variables** con tipos explícitos
4. **Usar nombres descriptivos** para macros y variables
5. **Comentar el código** (especialmente la lógica compleja)
6. **Manejar errores** con `On Error GoTo`
7. **Liberar objetos** (Set objeto = Nothing)
8. **Respaldar el archivo** antes de ejecutar macros no probadas

---

### Enigma 4.1: Macro de limpieza automática

Escribe una macro VBA que:

1. Recorra todas las hojas del libro activo
2. En cada hoja, busque en la columna A las celdas vacías
3. Cuando encuentre una celda vacía, elimine toda la fila (shift up)
4. Al final, muestre un mensaje con el total de filas eliminadas

### Enigma 4.2: Función personalizada de riesgo

Crea una función VBA llamada `NivelRiesgo` que:

- Reciba tres parámetros: monto (Double), frecuencia (Integer), origen (String)
- Devuelva "Alto" si: monto > 20,000 Y frecuencia > 3 Y origen = "Delta"
- Devuelva "Medio" si: monto > 10,000 O frecuencia > 5
- Devuelva "Bajo" en cualquier otro caso
- Prueba la función en Excel: `=NivelRiesgo(A2, B2, C2)`

### Enigma 4.3: Generador de informes

Escribe una macro que:

1. Pregunte al usuario la semana a reportar (InputBox)
2. Filtre la tabla de transacciones por esa semana
3. Copie los datos filtrados a una nueva hoja llamada "Reporte"
4. En la nueva hoja, agregue un encabezado con la fecha del sistema
5. Configure la impresión para que quepa en una página
6. Guarde el libro con el nombre "Reporte_Semana_[semana].xlsx"

*(Soluciones en el Apéndice)*
