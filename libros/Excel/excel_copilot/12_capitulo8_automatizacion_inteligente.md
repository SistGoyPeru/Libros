# Capítulo 8: Automatización Inteligente

El nuevo año trajo nuevos desafíos. Andrea ahora lideraba oficialmente el equipo de adopción de Copilot, y su siguiente misión era automatizar los reportes semanales que consumían horas del equipo.

—Cada lunes, alguien pasa dos horas generando el reporte de ventas —le explicó a Diego—. Es siempre el mismo formato, los mismos cálculos, las mismas tablas. Es un desperdicio de talento.

—¿Puede Copilot ayudar? —preguntó Diego.

—Sí, pero mejor aún: podemos enseñarle a Excel a hacerlo solo.

Andrea se sentó con Ricardo y diseñaron un plan de automatización.

### El Proceso Manual

Cada lunes, el proceso era:

1. Descargar datos del sistema contable (formato CSV)
2. Limpiar y transformar los datos (30 minutos)
3. Calcular KPIs con fórmulas (20 minutos)
4. Generar tablas dinámicas (15 minutos)
5. Crear gráficos (15 minutos)
6. Formatear y dar presentación (20 minutos)
7. Enviar por correo (5 minutos)

Total: ~1 hora 45 minutos por semana.

### La Solución con Copilot

Andrea abrió el archivo y escribió:

*"Copilot, necesito automatizar este reporte semanal de ventas. El proceso incluye:*
1. *Importar datos CSV de la carpeta 'Reportes_Semanales'*
2. *Limpiar: eliminar filas con ventas = 0, estandarizar fechas*
3. *Calcular: Ventas Totales, Margen Bruto, % Crecimiento vs semana anterior*
4. *Generar tabla dinámica: Ventas por Categoría y por Sucursal*
5. *Crear gráfico: barras de ventas por sucursal + línea de margen*

*¿Puedes generar un script de VBA o una consulta Power Query que automatice todo esto?"*

Copilot respondió:

*"Te recomiendo una combinación de Power Query (para importación y limpieza) y VBA (para generar reporte final).*

*SCRIPT VBA SUGERIDO:*

```vba
Sub GenerarReporteSemanal()
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim rng As Range
    
    ' Crear nuevo libro para el reporte
    Set wb = Workbooks.Add
    Set ws = wb.Sheets(1)
    ws.Name = "Reporte Semanal"
    
    ' Configurar encabezados
    ws.Range("A1:E1").Value = Array("Sucursal", "Ventas", "Margen", "% Crecimiento", "Categoría")
    ws.Range("A1:E1").Font.Bold = True
    
    ' Importar datos desde Power Query (asumiendo consulta existente)
    With ws.ListObjects.Add(SourceType:=xlSrcExternal, _
        Source:=Array("OLEDB;Provider=Microsoft.Mashup.OleDb.1;Location=ReporteSemanal"), _
        Destination:=ws.Range("A2"))
        .Name = "DatosReporte"
        .Refresh
    End With
    
    ' Dar formato
    ws.Range("A:E").Columns.AutoFit
    ws.Range("A:E").HorizontalAlignment = xlCenter
    
    ' Generar tabla dinámica
    ' ... (código para tabla dinámica)
    
    MsgBox "Reporte generado exitosamente"
End Sub
```

*¿Te gustaría que refine el script o que explique cada parte?"*

Andrea decidió empezar con Power Query para la parte de datos y dejar el VBA para después. Lo importante era que el proceso estaba documentado y listo para implementarse gradualmente.

---

### Conceptos Clave: Automatización con Copilot

Copilot puede ayudarte a automatizar tareas repetitivas de varias formas:

#### Niveles de Automatización

| Nivel | Herramienta | Cuándo Usarla |
|-------|------------|--------------|
| Básico | Fórmulas + Copilot | Tareas únicas o poco frecuentes |
| Medio | Power Query | Transformaciones recurrentes de datos |
| Avanzado | VBA + Copilot | Procesos complejos y repetitivos |
| Experto | Office Scripts (Excel Web) | Automatización en la nube |

#### Macros con Copilot

Copilot puede generar código VBA a partir de descripciones en lenguaje natural:

- *"Crea una macro que limpie la hoja activa: elimine filas vacías, borre formatos innecesarios, y ajuste el ancho de columnas"*
- *"Genera un script VBA que copie la hoja 'Ventas' a un nuevo libro y lo guarde con la fecha actual como nombre"*
- *"Escribe una macro que envíe por correo electrónico el reporte semanal a la lista de destinatarios en la columna A"*

#### Office Scripts (Excel para Web)

Si usas Excel en el navegador, Copilot puede generar Office Scripts (TypeScript):

- *"Crea un script que sume los valores de la columna B y muestre el resultado en una celda"*
- *"Genera un script que filtre la tabla por fecha y exporte los resultados a un archivo CSV"*

#### Mejores Prácticas de Automatización

1. **Empieza pequeño**: Automatiza un paso a la vez
2. **Documenta**: Pídele a Copilot que agregue comentarios al código
3. **Prueba en copia**: Nunca ejecutes macros en el archivo original
4. **Valida resultados**: Compara la salida automatizada con el proceso manual
5. **Itera**: Mejora gradualmente la automatización

---

### Ejercicio 8.1: Tu Primera Macro

Pídele a Copilot:

*"Genera una macro en VBA que:*
1. *Seleccione la hoja activa*
2. *Encuentre la última fila con datos*
3. *Agregue una fila de totales al final con SUM en cada columna numérica*
4. *Dé formato de negrita y color azul a la fila de totales*
5. *Muestre un mensaje de confirmación"*

Guarda el código en un módulo de VBA y pruébalo.

### Ejercicio 8.2: Plan de Automatización

Identifica un proceso repetitivo que hagas semanalmente en Excel. Pídele a Copilot:

*"Ayúdame a diseñar un plan de automatización para este proceso:*
[Describe el proceso paso a paso]

*¿Qué partes se pueden automatizar con Power Query? ¿Qué partes con VBA? ¿Qué partes deben seguir siendo manuales?"*
