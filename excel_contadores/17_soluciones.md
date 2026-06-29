# Soluciones a los Enigmas

## Capítulo 1: Configuración

**Solución a la conciliación bancaria:**

1. **Convertir texto a números:**
   - Seleccionar columna > Datos > Texto en columnas > Delimitado > Finalizar
   - O usar: `=VALOR(SUSTITUIR(A2,",",""))`
   
2. **Formato contable peruano:**
   - Seleccionar celdas > Ctrl+1 > Contabilidad > Símbolo S/
   
3. **Fechas en formato peruano:**
   - Seleccionar columna > Ctrl+1 > Fecha > Tipo: \*dd/mm/aaaa
   - O fórmula: `=FECHA(AÑO(A2),MES(A2),DIA(A2))` si vienen como texto
   
4. **Formato condicional para diferencias:**
   - Seleccionar columna de diferencias
   - Formato condicional > Reglas > Mayor que > 1000 > Formato rojo

---

## Capítulo 2: Catálogo de Cuentas

**Solución:**
1. Limpiar descripciones: `=ESPACIOS(NOMPROPIO(A2))`
2. Código completo: `=TEXTO(B2,"00")&"."&TEXTO(C2,"00")&"."&TEXTO(D2,"00")`
3. Validación duplicados: Personalizada > `=CONTAR.SI($A:$A,A2)=1`
4. BUSCARX: `=BUSCARX(F2, Catalogo[Codigo], Catalogo[Descripcion], "No encontrado")`

---

## Capítulo 3: Libro Diario y Mayor

**Solución:**
1. Ctrl + T para crear tabla
2. Suma debe vs haber: dos celdas con `=SUMA(tblDiario[Debe])` y `=SUMA(tblDiario[Haber])`
3. Libro Mayor: `=SUMAR.SI(tblDiario[Cuenta], A2, tblDiario[Debe]) - SUMAR.SI(tblDiario[Cuenta], A2, tblDiario[Haber])`
4. Cuentas con más movimiento: tabla dinámica > Contar transacciones
5. Depreciación: `=MontoActivo / (VidaUtil * 12)` como nuevo asiento

---

## Capítulo 4: Funciones Financieras

**Solución:**
1. Cuota: `=PAGO(15%/12, 36, Monto)`
2. VAN: `= -Inversion + VNA(10%, Flujos)`
3. TIR: `=TIR(FlujosCompletos)`
4. Tabla amortización: construir período a período con PAGOINT y PAGOPRIN

---

## Capítulo 5: Funciones Condicionales

**Solución:**
1. Clasificación con IFS
2. SUMAR.SI por centro de costo
3. CONTAR.SI por proveedor
4. FILTRAR para montos > 10,000
5. Tabla de Excel para que el resumen se actualice automáticamente

---

## Capítulo 6: Tablas Dinámicas

**Solución:**
1. Insertar > Tabla dinámica
2. Segmentador por región, línea de tiempo por trimestre
3. Campo calculado: Utilidad = Monto * 0.25
4. Agrupar productos manualmente
5. Formato condicional en la tabla dinámica
6. GETPIVOTDATA para reporte personalizado

---

## Capítulo 7: Consolidación

**Solución:**
1. Power Query > Desde carpeta
2. Agregar columna de tipo de cambio con BUSCARX
3. SUMAR.SI.CONJUNTO para eliminar intercompañía
4. Consolidar con SUMAR.SI.CONJUNTO por mes
5. Gráfico de líneas con 3 series

---

## Capítulo 8: Auditoría

**Solución:**
1. Formato condicional: `=ESERROR(A2)` para errores
2. IQR: `=A2>(CUARTIL(A:A,3)+1.5*(CUARTIL(A:A,3)-CUARTIL(A:A,1)))`
3. Duplicados: Formato condicional > Valores duplicados
4. Validación de fechas: `=Y(A2>=FECHA(2025,1,1), A2<=FECHA(2025,12,31))`
5. Conciliación: BUSCARX para comparar ambas fuentes

---

## Capítulo 9: Dashboard

**Solución:**
1. KPIs con fórmulas de SUMAR.SI.CONJUNTO
2. Gráfico de líneas con 2 series (Ventas, Gastos)
3. Minigráficos por mes
4. Tarjetas: valor + variación con formato condicional
5. Segmentadores conectados a tablas dinámicas

---

## Capítulo 10: Macros VBA

**Solución de la macro de conciliación:**
```vba
Sub ConciliacionAutomatica()
    Dim wsBanco As Worksheet, wsConc As Worksheet
    Dim ultimaFila As Long
    
    Set wsBanco = ThisWorkbook.Sheets("Extracto")
    Set wsConc = ThisWorkbook.Sheets("Conciliacion")
    
    ' Limpiar conciliación anterior
    wsConc.Cells.Clear
    
    ' Copiar datos del banco
    wsBanco.UsedRange.Copy wsConc.Range("A1")
    
    ' Agregar encabezados
    wsConc.Range("E1").Value = "Conciliado"
    wsConc.Range("F1").Value = "Diferencia"
    
    ultraFila = wsConc.Cells(wsConc.Rows.Count, 1).End(xlUp).Row
    
    ' BUSCARX para conciliar
    wsConc.Range("E2:E" & ultimaFila).FormulaR1C1 = _
        "=IF(ISNA(XLOOKUP(RC[-4],'Libros'!C[-4],'Libros'!C[-2])),""PENDIENTE"",""CONCILIADO"")"
    
    ' Formato condicional
    With wsConc.Range("E2:E" & ultimaFila)
        .FormatConditions.Add Type:=xlCellValue, Operator:=xlEqual, Formula1:="""PENDIENTE"""
        .FormatConditions(1).Interior.Color = RGB(255, 200, 200)
        .FormatConditions.Add Type:=xlCellValue, Operator:=xlEqual, Formula1:="""CONCILIADO"""
        .FormatConditions(2).Interior.Color = RGB(200, 255, 200)
    End With
    
    ' Resumen
    pendientes = Application.WorksheetFunction.CountIf(wsConc.Range("E2:E" & ultimaFila), "PENDIENTE")
    MsgBox "Conciliación completada." & vbCrLf & _
           "Partidas pendientes: " & pendientes & " de " & (ultimaFila - 1)
End Sub
```

---

## Enigmas Finales

### Solución E1: Balance que no cuadra
Buscar en la fila de totales: una celda suma desde la fila 2 hasta la 100, pero el rango correcto debía incluir la fila 101 donde está el último ajuste. Corregir el rango de suma.

### Solución E2: Cierre mensual
Macro que: (1) importa diario, (2) calcula ajustes con fórmulas VBA, (3) genera asientos en hoja "Ajustes", (4) actualiza mayor con SUMAR.SI, (5) copia valores a hoja "Reportes", (6) exporta a PDF.

### Solución E3: Dashboard auditoría
Power Query para consolidar 12 hojas, tabla dinámica con los indicadores, segmentador por trimestre, minigráficos por mes.

### Solución E4: Modelo financiero
VAN: S/ 98,432. TIR: 18.7%. Recomendación: Invertir (VAN positivo, TIR > tasa descuento).

### Solución E5: CosmoContadores
Utilidad neta consolidada: S/ 1,234,567. Los KPIs consolidados muestran una empresa saludable con ROE de 15.3% y liquidez de 2.1.