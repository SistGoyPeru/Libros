
# Capítulo 9: El Juicio

## Validación, Auditoría y Seguridad de Modelos

—Antes de enviar esto a la UIF —dijo Valeria—, tenemos que asegurarnos de que sea perfecto. Un error en una fórmula, una celda mal referenciada, y toda la evidencia podría ser desestimada.

Era el día 27. Faltaban 3 días para el plazo.

—La defensa de Nova va a contratar a sus propios auditores —continuó Valeria—. Van a revisar cada celda, cada fórmula, cada medida DAX. Si encuentran un error, por pequeño que sea, van a decir que todo el análisis es poco confiable.

—¿Qué necesitamos hacer? —preguntó Sofía.

—Una auditoría completa del modelo. Empezamos.

### Auditoría de fórmulas

Valeria abrió la pestaña **Fórmulas > Auditoría de fórmulas**.

—Excel tiene herramientas para auditar fórmulas que la mayoría de usuarios nunca usa.

**1. Rastrear precedentes:**
Seleccionó una celda con una fórmula compleja e hizo clic en **Rastrear precedentes**.

—Las flechas azules muestran qué celdas alimentan esta fórmula. Si alguna flecha está punteada (roja), significa que hay un error.

**2. Rastrear dependientes:**
—Muestra qué fórmulas dependen de esta celda. Así podemos ver el impacto de un cambio.

**3. Mostrar fórmulas:**
Valeria presionó `Ctrl + ~` (acento grave). Todas las celdas mostraron sus fórmulas en lugar de sus valores.

—Así podemos revisar visualmente que todas las fórmulas sean consistentes. Si una columna tiene 1,000 filas y 999 tienen la misma fórmula, la que es diferente salta a la vista.

**4. Evaluar fórmula:**
Seleccionó una celda con una medida DAX y abrió **Evaluar fórmula**.

—Esta herramienta ejecuta la fórmula paso a paso. Muestra el resultado intermedio de cada cálculo. Es como depurar código.

### Validación de medidas DAX

—Las medidas DAX son críticas —dijo Valeria—. Si una medida tiene un error lógico, todo el análisis se distorsiona.

**Prueba 1: Consistencia de totales**

—Creó una medida de verificación:

```
Verificación:=CALCULATE(SUM(Transacciones[Monto]), ALL(Transacciones))
```

—Luego sumó manualmente los montos en Excel. El resultado coincidió.

**Prueba 2: Filtros cruzados**

—Probó que las relaciones funcionaran correctamente:

—En una tabla dinámica, puso el nombre de una empresa y verificó que los montos correspondieran a las transacciones de esa empresa específica, no de todas.

**Prueba 3: Valores atípicos**

—Creó una medida para detectar valores extremos:

```
Promedio Móvil 3 Meses:=CALCULATE(
    AVERAGE(Transacciones[Monto]),
    DATESINPERIOD(Calendario[Fecha], LASTDATE(Calendario[Fecha]), -3, MONTH)
)

Desviación:=Transacciones[Monto] - [Promedio Móvil 3 Meses]
```

—Las transacciones con desviaciones grandes eran candidatas a revisión manual.

### Protección del modelo

—Ya verificamos que los datos son correctos —dijo Valeria—. Ahora tenemos que protegerlos para que nadie pueda manipularlos.

**1. Proteger hojas:**
—Revisión > Proteger hoja

Estableció una contraseña y seleccionó solo los permisos necesarios:
- ✅ Seleccionar celdas bloqueadas
- ❌ Seleccionar celdas desbloqueadas
- ❌ Formatear celdas
- ❌ Insertar/Eliminar
- ❌ Modificar tablas dinámicas

—Las celdas desbloqueadas son solo aquellas donde el usuario puede interactuar (controles, filtros). Todo lo demás está bloqueado.

**2. Proteger libro:**
—Archivo > Información > Proteger libro > Cifrar con contraseña

—Esto evita que alguien abra el archivo sin la contraseña.

**3. Proteger estructura del libro:**
—Revisión > Proteger libro > Proteger estructura del libro

—Esto evita que alguien mueva, elimine u oculte hojas.

**4. Firmas digitales:**
—Archivo > Información > Proteger libro > Agregar una firma digital

—Una firma digital certifica que el archivo no ha sido modificado desde que se firmó. Es la prueba forense definitiva.

### Control de cambios

—Necesitamos un registro de quién hizo qué y cuándo —dijo Valeria.

Usó **Compartir libro (heredado)** para habilitar el control de cambios:

—Cada cambio queda registrado con: usuario, fecha, qué cambió.

Pero Valeria negó con la cabeza. —El control de cambios de Excel es rudimentario. Para un caso serio, necesitamos un **log de auditoría personalizado**.

Escribió una macro que registraba cada cambio:

```vba
Option Explicit

Private Sub Workbook_SheetChange(ByVal Sh As Object, ByVal Target As Range)
    ' Registra cualquier cambio en el libro
    Dim wsLog As Worksheet
    Dim ultimaFila As Long
    Dim cambioDesc As String
    
    ' Ignorar cambios en la hoja de log
    If Sh.Name = "AuditLog" Then Exit Sub
    
    ' Crear o referenciar hoja de log
    On Error Resume Next
    Set wsLog = ThisWorkbook.Sheets("AuditLog")
    If wsLog Is Nothing Then
        Set wsLog = ThisWorkbook.Sheets.Add
        wsLog.Name = "AuditLog"
        wsLog.Range("A1:E1").Value = Array("Fecha", "Usuario", "Hoja", "Celda", "Nuevo Valor")
        wsLog.Range("A1:E1").Font.Bold = True
    End If
    On Error GoTo 0
    
    ' Registrar el cambio
    ultimaFila = wsLog.Cells(wsLog.Rows.Count, 1).End(xlUp).Row + 1
    wsLog.Cells(ultimaFila, 1).Value = Now
    wsLog.Cells(ultimaFila, 2).Value = Environ("UserName")
    wsLog.Cells(ultimaFila, 3).Value = Sh.Name
    wsLog.Cells(ultimaFila, 4).Value = Target.Address
    wsLog.Cells(ultimaFila, 5).Value = Target.Value
End Sub

Private Sub Workbook_BeforeClose(Cancel As Boolean)
    ' Al cerrar, proteger el log
    Dim wsLog As Worksheet
    Set wsLog = ThisWorkbook.Sheets("AuditLog")
    If Not wsLog Is Nothing Then
        wsLog.Protect Password:="Auditoria2026"
    End If
End Sub
```

—Cada vez que alguien modifica una celda, queda registrado: fecha, usuario, hoja, celda y nuevo valor. Es evidencia de integridad.

### La revisión final

Durante dos días enteros, revisaron cada aspecto del modelo:

1. **Power Query**: Verificaron que cada paso aplicado fuera correcto y que los datos originales no se hubieran modificado
2. **Power Pivot**: Confirmaron que las relaciones fueran correctas (1:M) y que no hubiera relaciones fantasma
3. **Medidas DAX**: Probaron cada medida con datos conocidos y verificaron los resultados manualmente
4. **VBA**: Revisaron que las macros no tuvieran errores de ejecución y que el log de auditoría funcionara
5. **Power BI**: Verificaron que las visualizaciones mostraran los datos correctos y que los filtros funcionaran
6. **Dashboard**: Probaron todos los controles interactivos
7. **Protección**: Verificaron que las hojas estuvieran protegidas y la firma digital aplicada

—¿Está todo listo? —preguntó Sofía, con los ojos rojos de tanto revisar números.

Valeria tomó un respiro profundo. —Listo. El modelo es sólido. Los datos son correctos. Las medidas están validadas. El código está limpio. El log de auditoría está funcionando.

—Entonces —dijo Sofía—, mañana presentamos ante la UIF.

—Mañana —confirmó Valeria—. Y no solo vamos a presentar datos. Vamos a presentar un caso construido con el poder del análisis.

Sofía miró la pantalla. El archivo de Excel, con sus 45 MB y cientos de miles de filas de datos, contenía la verdad que necesitaban.

—Todo este poder —dijo en voz baja—. Todo esto, dentro de Excel.

—Sí —dijo Valeria—. Y solo arañamos la superficie.

---

## Explicación técnica: Validación, Auditoría y Seguridad

### Herramientas de auditoría de fórmulas

| Herramienta | Acceso | Función |
|-------------|--------|---------|
| Rastrear precedentes | Fórmulas > Auditoría | Muestra qué celdas alimentan la fórmula |
| Rastrear dependientes | Fórmulas > Auditoría | Muestra qué fórmulas dependen de la celda |
| Quitar flechas | Fórmulas > Auditoría | Elimina las flechas de rastreo |
| Mostrar fórmulas | Fórmulas > Auditoría (Ctrl+~) | Muestra fórmulas en lugar de valores |
| Evaluar fórmula | Fórmulas > Auditoría | Ejecuta fórmula paso a paso |
| Comprobación de errores | Fórmulas > Auditoría | Busca errores comunes en el libro |
| Ventana de inspección | Fórmulas > Auditoría | Monitorea celdas específicas |

### Validación de medidas DAX

Técnicas para validar medidas DAX:

1. **Prueba de totales**: Comparar medida con suma manual
2. **Prueba de filtros**: Verificar que el contexto de filtro funcione
3. **Prueba de límites**: Probar con valores extremos (0, máximos, nulos)
4. **Prueba de consistencia**: Comparar con medidas alternativas
5. **Prueba de rendimiento**: Verificar que no haya cálculos innecesariamente lentos

### Protección de seguridad

| Método | Qué protege | Nivel |
|--------|-------------|-------|
| Proteger hoja | Celdas, formato, contenido de la hoja | Básico |
| Proteger libro | Estructura (hojas no se mueven/eliminan) | Medio |
| Cifrar con contraseña | Apertura del archivo | Alto |
| Firma digital | Integridad del archivo (no modificado) | Forense |
| Marcado como final | Lectura (no evita edición) | Bajo |
| Permisos IRM | Quién puede abrir/imprimir/copiar | Alto |

### Buenas prácticas para modelos auditables

1. **Documentar todo**: Cada paso, cada medida, cada supuesto
2. **Separar datos de presentación**: Datos crudos en una hoja, dashboard en otra
3. **Usar nombres de rango**: En lugar de referencias A1, usar nombres descriptivos
4. **Versionar el modelo**: Guardar versiones numeradas antes de cambios mayores
5. **Probar con datos de prueba**: Tener un conjunto de datos con resultados conocidos
6. **Automatizar validaciones**: Macros que verifiquen la integridad del modelo
7. **Mantener un log de cambios**: Quién, qué, cuándo y por qué

---

### Enigma 9.1: Auditoría de fórmulas

Tienes un modelo con esta fórmula:

```
=SI(B2>0, BUSCARV(B2, Precios!$A$2:$B$100, 2, FALSO) * C2, "SIN DATOS")
```

Usa las herramientas de auditoría para:
1. Rastrear los precedentes de esta fórmula
2. Identificar qué pasa si B2 está vacío
3. Verificar que la tabla en Precios!$A$2:$B$100 no tenga duplicados
4. Evaluar la fórmula paso a paso (simula B2=5, C2=10)

### Enigma 9.2: Protección del modelo

Describe el esquema de protección que implementarías para un modelo financiero que:

- Debe ser visible para 5 analistas (pueden ver y filtrar)
- Solo 2 administradores pueden modificar las fórmulas y medidas
- Debe tener un registro de cambios
- Debe mantener la integridad de los datos originales
- Será presentado como evidencia en un juicio

### Enigma 9.3: Log de auditoría VBA

Mejora la macro de log de auditoría presentada en el capítulo para que:

1. También registre el valor anterior de la celda modificada
2. Ignore cambios en celdas con formato condicional (solo cambios reales)
3. Agregue un timestamp con zona horaria
4. Proteja la hoja AuditLog con una contraseña definida al inicio
5. Muestre un mensaje de confirmación al usuario informándole que el cambio fue registrado

Escribe el código VBA completo.

*(Soluciones en el Apéndice)*
