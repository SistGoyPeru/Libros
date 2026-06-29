# Capítulo 10: Automatización con Macros VBA

## El contador que no se repite

—Un contador inteligente —dijo Don Alberto— no hace dos veces el mismo trabajo. Automatiza.

### La Historia

—María —dijo Don Ricardo una mañana—, todos los meses haces lo mismo: importar el extracto bancario, formatearlo, conciliarlo, y generar el informe. Son 45 minutos cada vez.

—Sí —dijo María—, y son 12 meses al año, más 3 bancos... son 27 horas al año.

—¿Y si pudieras hacerlo en 30 segundos? —preguntó Don Alberto desde la puerta.

María lo miró incrédula.

—Con macros —dijo Don Alberto—.

### Grabación de macros

—La forma más fácil de crear una macro —dijo Don Alberto— es grabarla.

```
Desarrollador > Grabar macro
Nombre: ConciliacionBancaria
Tecla método abreviado: Ctrl+Mayús+C
Guardar macro en: Libro de macros personal (Personal.xlsb)
```

—Luego —continuó—, realiza los pasos una vez mientras Excel los graba. Al terminar, detén la grabación.

**Pasos para grabar:**
1. Importar datos del banco
2. Aplicar formato contable
3. Insertar columnas de conciliación
4. Aplicar fórmulas de BUSCARX
5. Crear tabla dinámica resumen
6. Aplicar formato condicional

—¡Listo! —dijo Don Alberto—. Ahora, cada mes, solo presiona Ctrl+Mayús+C y la macro hace todo.

### Editor de VBA

—Pero —dijo Don Alberto—, la grabación tiene límites. Para macros más potentes, necesitas el Editor de VBA.

```
Desarrollador > Visual Basic (Alt + F11)
```

**Estructura de una macro:**
```vba
Sub NombreMacro()
    ' Comentario: qué hace esta macro
    
    ' Variables
    Dim wsOrigen As Worksheet
    Dim wsDestino As Worksheet
    Dim ultimaFila As Long
    
    ' Configuración
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual
    
    ' Código
    Set wsOrigen = ThisWorkbook.Sheets("Extracto")
    Set wsDestino = ThisWorkbook.Sheets("Conciliacion")
    
    ultimaFila = wsOrigen.Cells(wsOrigen.Rows.Count, 1).End(xlUp).Row
    
    ' Copiar datos
    wsOrigen.Range("A1:D" & ultimaFila).Copy wsDestino.Range("A1")
    
    ' Aplicar formato
    wsDestino.Range("D:D").NumberFormat = "#,##0.00"
    
    ' Restaurar configuración
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
    
    MsgBox "Conciliación completada: " & ultimaFila & " transacciones"
End Sub
```

### Macros contables esenciales

Don Alberto mostró varias macros que todo contador debería tener:

**1. Macro para exportar a PDF:**

```vba
Sub ExportarEstadosFinancieros()
    Dim ws As Worksheet
    Dim ruta As String
    
    ruta = ThisWorkbook.Path & "\Estados Financieros " & Format(Date, "yyyy-mm") & ".pdf"
    
    Sheets(Array("Balance", "Resultados", "Flujo")).Select
    ActiveSheet.ExportAsFixedFormat _
        Type:=xlTypePDF, _
        Filename:=ruta, _
        Quality:=xlQualityStandard
        
    MsgBox "PDF generado: " & ruta
End Sub
```

**2. Macro para generar asientos automáticos:**

```vba
Sub GenerarAsientoDepreciacion()
    Dim ws As Worksheet
    Dim activo As String
    Dim monto As Double
    Dim vidaUtil As Integer
    Dim depreciacionMensual As Double
    Dim ultimaFila As Long
    Dim i As Long
    
    Set ws = ThisWorkbook.Sheets("Activos Fijos")
    
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    
    For i = 2 To ultimaFila
        activo = ws.Cells(i, 1).Value
        monto = ws.Cells(i, 2).Value
        vidaUtil = ws.Cells(i, 3).Value
        
        depreciacionMensual = monto / (vidaUtil * 12)
        
        ' Registrar en libro diario
        Sheets("Diario").Cells(Sheets("Diario").Rows.Count, 1).End(xlUp).Offset(1, 0).Value = Date
        Sheets("Diario").Cells(Sheets("Diario").Rows.Count, 1).End(xlUp).Offset(0, 1).Value = "DEP-" & Format(Date, "yyyymm")
        Sheets("Diario").Cells(Sheets("Diario").Rows.Count, 1).End(xlUp).Offset(0, 2).Value = "Depreciación " & activo
        Sheets("Diario").Cells(Sheets("Diario").Rows.Count, 1).End(xlUp).Offset(0, 3).Value = 68 ' Cuenta gasto
        Sheets("Diario").Cells(Sheets("Diario").Rows.Count, 1).End(xlUp).Offset(0, 4).Value = depreciacionMensual
        Sheets("Diario").Cells(Sheets("Diario").Rows.Count, 1).End(xlUp).Offset(0, 5).Value = 39 ' Cuenta depreciación acumulada
        Sheets("Diario").Cells(Sheets("Diario").Rows.Count, 1).End(xlUp).Offset(0, 6).Value = depreciacionMensual
    Next i
    
    MsgBox "Asientos de depreciación generados: " & (ultimaFila - 1)
End Sub
```

**3. Macro para enviar correos desde Excel:**

```vba
Sub EnviarRecordatorioPago()
    Dim OutlookApp As Object
    Dim Mail As Object
    Dim ws As Worksheet
    Dim i As Long, ultimaFila As Long
    
    Set OutlookApp = CreateObject("Outlook.Application")
    Set ws = ThisWorkbook.Sheets("Facturas Pendientes")
    
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    
    For i = 2 To ultimaFila
        If ws.Cells(i, 5).Value > Date Then  ' Fecha vencida
            Set Mail = OutlookApp.CreateItem(0)
            Mail.To = ws.Cells(i, 4).Value  ' Email del cliente
            Mail.Subject = "Recordatorio de pago - Factura " & ws.Cells(i, 1).Value
            Mail.Body = "Estimado cliente," & vbCrLf & vbCrLf & _
                        "Le recordamos que la factura " & ws.Cells(i, 1).Value & _
                        " por S/ " & Format(ws.Cells(i, 3).Value, "#,##0.00") & _
                        " vence el " & ws.Cells(i, 5).Value & "." & vbCrLf & vbCrLf & _
                        "Saludos cordiales," & vbCrLf & "Estudio Cifras & Legados"
            Mail.Send
        End If
    Next i
    
    MsgBox "Recordatorios enviados"
End Sub
```

**4. Macro para limpiar y formatear datos:**

```vba
Sub LimpiarDatosContables()
    Dim ws As Worksheet
    Dim rng As Range
    
    Set ws = ActiveSheet
    
    ' Eliminar filas vacías
    On Error Resume Next
    ws.UsedRange.SpecialCells(xlCellTypeBlanks).EntireRow.Delete
    On Error GoTo 0
    
    ' Convertir texto a números
    With ws.UsedRange
        .NumberFormat = "General"
        .Value = .Value
    End With
    
    ' Aplicar formato contable a columnas de montos
    For Each rng In ws.Range("A1").CurrentRegion.Columns
        If Application.WorksheetFunction.IsNumber(rng.Cells(2, 1)) Then
            If rng.Cells(2, 1).Value > 100 Then
                rng.NumberFormat = "#,##0.00"
            End If
        End If
    Next rng
    
    MsgBox "Datos limpiados y formateados"
End Sub
```

### Seguridad de macros

—Las macros son poderosas —advirtió Don Alberto—, pero también riesgosas.

**Mejores prácticas de seguridad:**

1. **Firmar digitalmente** las macros antes de distribuirlas
2. **Nunca habilitar macros** de archivos desconocidos
3. **Usar contraseñas** para proteger el código VBA
4. **Respaldar** el código en un repositorio

Don Alberto mostró cómo proteger el código:

```
Editor VBA > Herramientas > Propiedades del proyecto VBA > Protección
[x] Bloquear proyecto para visualización
Contraseña: ********
```

### Asignar macros a botones

—Para que cualquiera pueda usar las macros —dijo Don Alberto—, asígnalas a botones.

```
Insertar > Formas > Botón
Asignar macro > Seleccionar la macro
```

—O mejor, crea una cinta personalizada:

```
Archivo > Opciones > Personalizar cinta
Nuevo grupo > Agregar macros desde "Macros personalizadas"
```

### Resumen del capítulo

| Macro | Función |
|-------|---------|
| Grabación | Automatizar pasos repetitivos |
| VBA | Automatización compleja |
| Exportar PDF | Generar informes automáticos |
| Asientos automáticos | Depreciación, provisiones |
| Envío de correos | Recordatorios de pago |
| Limpieza de datos | Estandarizar formatos |
| Botones | Interfaz amigable para usuarios |

### Enigma contable #10

En `codigos/10_vba/macro_conciliacion.xlsm` encontrarás un libro con datos de extracto bancario de 3 meses.

**Tu misión:**
1. Graba una macro que automatice la conciliación bancaria
2. Escribe una macro en VBA que:
   - Identifique automáticamente las transacciones no conciliadas
   - Genere un informe de conciliación en una nueva hoja
   - Formatee el informe con colores (verde = conciliado, rojo = pendiente)
   - Muestre un mensaje con el total de partidas pendientes
3. Asigna la macro a un botón llamado "Conciliar"
4. Agrega una segunda macro que exporte el informe a PDF
5. Protege el código VBA con contraseña (usa "contador2025")

*Cada mes, con un clic, la conciliación debe estar lista.*