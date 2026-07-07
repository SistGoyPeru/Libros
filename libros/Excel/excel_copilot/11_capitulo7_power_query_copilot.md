# Capítulo 7: Power Query y Copilot

Llegó diciembre y con él, la temporada de cierre fiscal. Para Andrea, eso significaba una cosa: consolidar datos de múltiples fuentes.

—Tenemos archivos de ventas de 12 sucursales —le explicó Diego—, cada una con su propio formato. Necesito un archivo consolidado para el cierre anual.

Andrea abrió el primer archivo. Luego el segundo. Luego el tercero. Cada uno tenía columnas en diferentes posiciones, nombres distintos para los mismos campos, y formatos variados.

—Consolidar 12 archivos manualmente me tomaría dos días —calculó.

Recordó que Copilot podía ayudar con Power Query.

*"Copilot, necesito consolidar 12 archivos de ventas de sucursales. Están en la carpeta C:\Ventas_2026\Sucursales\. Cada archivo tiene el mismo tipo de datos pero columnas en diferente orden y con nombres distintos. ¿Puedes ayudarme a crear una consulta en Power Query que:*
1. *Importe todos los archivos de la carpeta*
2. *Estandarice los nombres de columna*
3. *Combine los datos en una sola tabla*
4. *Agregue una columna con el nombre de la sucursal (extraído del nombre del archivo)*
5. *Elimine filas duplicadas*
6. *Cargue el resultado en una nueva hoja"*

Copilot respondió con instrucciones paso a paso:

*"Te guiaré en la creación de una consulta Power Query:*

*PASO 1: Ir a Datos > Obtener datos > Desde un archivo > Desde carpeta*
*PASO 2: Seleccionar la carpeta C:\Ventas_2026\Sucursales\*
*PASO 3: En Power Query, usa este código M para estandarizar columnas:*

```m
let
    Origen = Folder.Files("C:\Ventas_2026\Sucursales\"),
    FiltrarExcel = Table.SelectRows(Origen, each Text.EndsWith([Extension], ".xlsx")),
    Importar = Table.AddColumn(FiltrarExcel, "Datos", each 
        Excel.Workbook([Content], true)),
    ExpandirDatos = Table.ExpandTableColumn(Importar, "Datos", {"Data"}),
    ExpandirTablas = Table.ExpandTableColumn(ExpandirDatos, "Data", 
        Table.ColumnNames(ExpandirDatos[Data]{0})),
    ExtraerSucursal = Table.AddColumn(ExpandirTablas, "Sucursal", each 
        Text.BeforeDelimiter(Text.AfterDelimiter([Name], "_"), ".")),
    EstandarizarNombres = Table.RenameColumns(ExpandirDatos, 
        {{"Venta", "Ventas"}, {"Importe", "Ventas"}, {"Total", "Ventas"}}),
    QuitarDuplicados = Table.Distinct(EstandarizarNombres),
    SeleccionarColumnas = Table.SelectColumns(QuitarDuplicados, 
        {"Sucursal", "Fecha", "Producto", "Cantidad", "Ventas"})
in
    SeleccionarColumnas
```

*¿Te gustaría que te guíe paso a paso en Power Query?"*

Andrea siguió las instrucciones. En 20 minutos, tenía los 12 archivos consolidados en una sola tabla de 600 mil filas.

—Esto es magia —murmuró.

---

### Conceptos Clave: Power Query + Copilot

Power Query es la herramienta de transformación de datos de Excel. Copilot puede ayudarte a escribir el código M necesario sin que seas experto.

#### ¿Qué es Power Query?

Power Query es un motor de transformación de datos integrado en Excel. Permite:

- Importar datos de múltiples fuentes (archivos, bases de datos, web)
- Transformar y limpiar datos
- Combinar tablas
- Automatizar procesos repetitivos

#### Cómo Copilot Potencia Power Query

| Tarea | Sin Copilot | Con Copilot |
|-------|-------------|-------------|
| Escribir código M | Buscar sintaxis en foros | Pedir el código en lenguaje natural |
| Depurar errores | Probar y error | Pedir explicación del error |
| Optimizar consultas | Conocer técnicas avanzadas | Pedir sugerencias de optimización |
| Documentar | Escribir manualmente | Pedir que documente cada paso |

#### Prompts Útiles para Power Query

- *"Crea una consulta Power Query que importe todos los archivos CSV de una carpeta"*
- *"Agrega un paso que convierta la columna 'Fecha' a tipo fecha"*
- *"Combina las tablas 'Ventas' y 'Clientes' por el campo 'ID_Cliente'"*
- *"Agrupa los datos por 'Categoría' y suma las 'Ventas'"*
- *"Agrega una columna personalizada que calcule el margen: (Precio - Costo) / Precio"*
- *"Explica qué hace este código M paso a paso: [pegar código]"*

#### Cuándo Usar Power Query vs Fórmulas

| Escenario | Recomendación |
|-----------|--------------|
| Una sola transformación | Fórmula de Excel |
| Transformación recurrente | Power Query (automatizable) |
| Múltiples archivos | Power Query (consolidación) |
| Datos > 100k filas | Power Query (rendimiento) |
| Transformación simple única | Fórmula de Excel |

---

### Ejercicio 7.1: Tu Primera Consulta Power Query

Busca una carpeta con al menos 3 archivos Excel similares. Pídele a Copilot:

*"Necesito combinar todos los archivos Excel de la carpeta [ruta]. Los archivos tienen las mismas columnas pero en diferente orden. Crea una consulta Power Query que:*
1. *Importe todos los archivos*
2. *Estandarice los tipos de datos*
3. *Combine en una sola tabla*
4. *Agregue columna con el nombre del archivo de origen*
5. *Cargue los datos en una nueva hoja"*

### Ejercicio 7.2: Traductor de Fórmulas a Power Query

Toma una fórmula compleja de Excel (como un SUMAR.SI.CONJUNTO con múltiples criterios) y pídele a Copilot:

*"Traduce esta fórmula a un paso de Power Query: [pegar fórmula]. Quiero que el resultado sea un código M que pueda agregar a una consulta existente."*
