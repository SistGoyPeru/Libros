# Capítulo 10: Power Query — ETL y Transformación

## ¿Qué es Power Query?

**Power Query** es el motor de ETL (Extracción, Transformación y Carga) de Power BI. Te permite conectar, limpiar y transformar datos antes de cargarlos al modelo.

```
Fuente → Power Query (ETL) → Modelo → Visualizaciones
```

Características:
- Interfaz gráfica (sin código) + lenguaje M
- 1000+ conectores (SQL, Excel, CSV, Web, APIs)
- Transformaciones sin modificar la fuente original
- Repetible: actualizas datos, las transformaciones se re-aplican

## El Editor de Power Query

1. En Power BI Desktop: "Transformar datos" (cinta de opciones)
2. Se abre el Editor de Power Query
3. Panel izquierdo: lista de consultas (tablas)
4. Panel central: vista previa de datos
5. Panel derecho: "Pasos aplicados" (cada transformación es un paso)

## Pasos aplicados

Cada clic en Power Query crea un paso que se guarda en secuencia:

```
Consulta: fact_orders
  ├── Origen (SQLite)
  ├── Navegación (tabla seleccionada)
  ├── Tipo cambiado (tipos de datos)
  ├── Filtros aplicados (solo 2024)
  ├── Columna renombrada
  └── Carga en modelo
```

Puedes reordenar, eliminar o modificar cualquier paso.

## Transformaciones básicas

### Limpieza de columnas

```
Eliminar filas superiores/inferiores
Eliminar duplicados
Mantener filas (rango)
Rellenar hacia abajo/arriba
```

### Columnas

```
Cambiar tipo: texto, número entero, decimal, fecha
Renombrar columnas
Duplicar columnas
Dividir columna (por delimitador, por número de caracteres)
Extraer: texto antes/después, primeros/últimos caracteres, rango
Reemplazar valores
```

### Transformación de texto

```
Mayúsculas / minúsculas / título
Quitar espacios
Reemplazar texto
Agregar prefijo/sufijo
Extraer XML/JSON
```

## Combinar consultas

### Merge (JOIN)

Equivalente a JOIN en SQL:

1. "Combinar" → "Combinar consultas"
2. Selecciona las tablas y columnas clave
3. Elige el tipo de JOIN:
   - Left Outer (izquierda)
   - Right Outer (derecha)
   - Full Outer (completo)
   - Inner (interno)
   - Anti (solo no coincidentes)

### Append (UNION)

Equivalente a UNION ALL en SQL:

1. "Combinar" → "Anexar consultas"
2. Selecciona las tablas a unir
3. Las columnas deben coincidir

## Agrupación y agregación

1. "Transformar" → "Agrupar por"
2. Columna de agrupación: `category`
3. Nueva columna: "Ingresos" → Suma de `line_total`

Equivalente M generado:

```powerquery
= Table.Group(
    fact_order_items,
    {"product_sk"},
    {{"Ingresos", each List.Sum([line_total]), type number}}
)
```

## Columnas condicionales

1. "Agregar columna" → "Columna condicional"
2. Ejemplo: clasificar pedidos por monto

```powerquery
= Table.AddColumn(
    fact_orders,
    "Categoría Pedido",
    each if [total] >= 1000 then "Premium"
       else if [total] >= 500 then "Alto"
       else if [total] >= 200 then "Medio"
       else "Bajo"
)
```

## Columnas personalizadas (fórmulas M)

```powerquery
// Descuento simulado del 10% para pedidos > $500
= Table.AddColumn(
    fact_orders,
    "Descuento",
    each if [total] > 500 then [total] * 0.1 else 0
)

// Nombre completo
= Table.AddColumn(
    dim_customer,
    "Nombre Completo",
    each [name]
)

// Edad del cliente
= Table.AddColumn(
    dim_customer,
    "Años Registrado",
    each Duration.Days(DateTime.Date(DateTime.LocalNow()) - [registration_date]) / 365
)
```

## Funciones M útiles

```powerquery
// Fecha
Date.Year([fecha])
Date.Month([fecha])
Date.Day([fecha])
Date.DayOfWeek([fecha])
Date.QuarterOfYear([fecha])

// Texto
Text.Upper([texto])
Text.Lower([texto])
Text.Trim([texto])
Text.Length([texto])
Text.Start([texto], 5)
Text.End([texto], 3)

// Lógica
if [columna] > 10 then "Alto" else "Bajo"
```

## Parámetros en Power Query

Los parámetros permiten reutilizar valores:

1. "Administrar parámetros" → "Nuevo parámetro"
2. Nombre: `AñoActual`, Tipo: Número, Valor: 2024
3. Úsalo en los pasos: `if [anio] = AñoActual then ...`

## ETL práctico para TechStore

### Paso 1: Conectar y limpiar

1. Conecta las 6 tablas del star schema
2. En fact_orders: filtra `total > 0` (eliminar valores negativos)
3. En dim_customer: reemplazar ciudades vacías con "Sin Ciudad"
4. En dim_product: categorizar productos sin categoría como "General"

### Paso 2: Crear dimensión de tiempo completa

1. Crea una nueva consulta en blanco
2. Usa la función `List.Dates` para generar el calendario

```powerquery
let
    FechaInicio = #date(2023, 1, 1),
    FechaFin = #date(2026, 12, 31),
    Fechas = List.Dates(FechaInicio, Duration.Days(FechaFin - FechaInicio) + 1, #duration(1, 0, 0, 0)),
    Tabla = Table.FromList(Fechas, Splitter.SplitByNothing(), {"full_date"}),
    #"Tipo Cambiado" = Table.TransformColumnTypes(Tabla, {{"full_date", type date}}),
    #"Año Agregado" = Table.AddColumn(#"Tipo Cambiado", "anio", each Date.Year([full_date])),
    #"Mes Agregado" = Table.AddColumn(#"Año Agregado", "mes", each Date.Month([full_date])),
    #"Nombre Mes" = Table.AddColumn(#"Mes Agregado", "mes_nombre", each Date.MonthName([full_date])),
    #"Trimestre" = Table.AddColumn(#"Nombre Mes", "trimestre", each Date.QuarterOfYear([full_date])),
    #"Día Semana" = Table.AddColumn(#"Trimestre", "dia_semana_num", each Date.DayOfWeek([full_date]) + 1),
    #"Nombre Día" = Table.AddColumn(#"Día Semana", "dia_semana_nombre", each Date.DayOfWeekName([full_date])),
    #"Fin Semana" = Table.AddColumn(#"Nombre Día", "es_fin_semana", each if Date.DayOfWeek([full_date]) >= 5 then 1 else 0)
in
    #"Fin Semana"
```

### Paso 3: Fusionar consultas para tabla completa

Crea una consulta que unifique orders + customer + employee:

1. "Combinar" → fact_orders + dim_customer (por customer_sk)
2. Expande: name, city, country
3. "Combinar" → resultado + dim_employee (por employee_sk)
4. Expande: employee name, position

## Buenas prácticas en Power Query

1. **Nombra cada paso** descriptivamente (no "Paso personalizado1")
2. **Elimina pasos innecesarios** al final
3. **Usa parámetros** para valores que cambian (año, umbral)
4. **Documenta consultas complejas** con comentarios
5. **Agrupa consultas** relacionadas en carpetas
6. **Mantén la fuente original** — nunca modifiques los datos fuente

## Ejercicios

1. Conecta las 6 tablas del star schema en Power Query
2. Aplica una transformación: filtra pedidos con total > 0
3. Crea una columna condicional "Categoría de Precio" en dim_product
4. ¿Qué es un paso aplicado y cómo se reordena?
5. Combina fact_orders + dim_customer usando Merge
6. ¿Cuál es la diferencia entre Merge y Append?
7. Crea la tabla dim_date completa en Power Query usando M
8. Agrupa fact_order_items por product_sk y suma line_total
9. Crea un parámetro "Año Actual" y úsalo en un filtro
10. Documenta cada paso de tu consulta principal con nombres descriptivos
