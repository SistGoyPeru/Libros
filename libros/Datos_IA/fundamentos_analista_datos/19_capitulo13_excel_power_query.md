# Capítulo 13: Excel — Power Query

## ¿Qué es Power Query?

Power Query es la herramienta de transformación de datos de Excel. Te permite conectar, combinar, limpiar y transformar datos de múltiples orígenes sin escribir código.

Los analistas pasan el 80% de su tiempo limpiando datos. Power Query reduce drásticamente ese tiempo.

## Acceder a Power Query

- Excel: "Datos" > "Obtener y transformar datos" > "Power Query Editor"
- Atajo: Alt + A + P + Q

## Conectar datos desde CSV

1. "Datos" > "Desde archivo" > "Desde CSV"
2. Selecciona `datos_detalles_ventas.csv`
3. Se abre Power Query Editor con una vista previa

## Transformaciones básicas

### Promover encabezados

Cuando los encabezados están en la primera fila:
"Inicio" > "Usar la primera fila como encabezados"

### Cambiar tipo de datos

Power Query detecta tipos automáticamente, pero a veces falla:
- Haz clic en el icono junto al nombre de la columna
- Selecciona el tipo correcto: texto, número entero, decimal, fecha

### Eliminar filas y columnas

- Selecciona columnas > "Inicio" > "Quitar columnas"
- "Inicio" > "Quitar filas" > "Quitar filas superiores" / "Quitar filas en blanco"

### Reemplazar valores

- Selecciona una columna
- "Transformar" > "Reemplazar valores"
- Busca "Madrid" y reemplaza con "Madrid (Capital)"

### Dividir columnas

- Selecciona la columna a dividir
- "Transformar" > "Dividir columna"
- Opciones: por delimitador, por número de caracteres, por mayúsculas/minúsculas

Ejemplo: dividir `customer_name` en nombre y apellido.

## Combinar consultas (Merge)

Equivalente a los JOINs de SQL:

1. "Inicio" > "Combinar" > "Combinar consultas"
2. Selecciona las dos tablas
3. Elige las columnas clave
4. Selecciona el tipo de combinación:
   - Combinación interna (INNER JOIN)
   - Combinación externa izquierda (LEFT JOIN)
   - Combinación externa completa (FULL JOIN)

### Ejemplo: combinar ventas con productos

1. Carga `datos_ventas.csv` y `datos_productos.csv`
2. En la tabla ventas, "Combinar consultas"
3. Selecciona `productos` como segunda tabla
4. Empareja `product_id` con `id`
5. Expande la columna para incluir `product_name` y `category`

## Agregar columnas personalizadas

"Agregar columna" > "Columna personalizada"

```
= [quantity] * [unit_price]
```

Esto crea una columna `line_total` calculada.

También puedes crear columnas condicionales:

```
if [quantity] > 2 then "Alta" else if [quantity] > 1 then "Media" else "Baja"
```

## Agrupar y agregar

Equivalente a GROUP BY de SQL:

1. "Transformar" > "Agrupar por"
2. Agrupa por: `region`
3. Nueva columna: "Ingresos" con operación Suma sobre `total`

## Power Query vs Excel tradicional

| Operación | Excel tradicional | Power Query |
|-----------|------------------|-------------|
| Importar CSV | Archivo > Abrir | Datos > Desde CSV |
| Filtrar filas | Autofiltro | Quitar filas / Filtro |
| Combinar tablas | BUSCARV | Combinar consultas |
| Agrupar datos | Tabla dinámica | Agrupar por |
| Transformar datos | Fórmulas manuales | Editor visual |
| Repetir proceso | Manual cada vez | Actualizar consulta |

## Actualizar consultas

La gran ventaja de Power Query: cuando los datos fuente cambian:

1. "Datos" > "Actualizar todo"
2. Power Query re-ejecuta todas las transformaciones
3. El resultado se actualiza automáticamente

## M: el lenguaje de Power Query

Power Query tiene su propio lenguaje llamado M. Cada operación que haces visualmente genera código M:

```
let
    Origen = Csv.Document(File.Contents("datos.csv"),...),
    #"Encabezados promovidos" = Table.PromoteHeaders(Origen, [PromoteAllScalars=true]),
    #"Tipo cambiado" = Table.TransformColumnTypes(#"Encabezados promovidos",...)
in
    #"Tipo cambiado"
```

No necesitas aprender M para usar Power Query, pero entenderlo te da superpoderes.

## Ejercicios del Capítulo 13

1. Carga `datos_detalles_ventas.csv` en Power Query.
2. Promueve la primera fila como encabezados si no lo está.
3. Cambia el tipo de `order_date` a fecha y `total` a decimal.
4. Filtra solo los pedidos con status "Completado".
5. Divide `customer_name` en nombre y apellido.
6. Carga `datos_productos.csv` y combínala con la tabla de ventas por `product_id`.
7. Agrupa por región y calcula el total de ingresos.
8. Añade una columna personalizada que calcule el margen estimado (ingresos * 0.3).
9. Una vez terminado, carga el resultado a Excel.
10. Modifica el archivo CSV original, añade 3 filas, y actualiza la consulta. ¿Se actualiza todo automáticamente?

## Checklist de autoevaluación

- [ ] Sé acceder a Power Query Editor
- [ ] Sé importar datos desde CSV
- [ ] Sé realizar transformaciones básicas (cambiar tipo, reemplazar, dividir)
- [ ] Sé combinar consultas (equivalente a JOIN)
- [ ] Sé agregar columnas personalizadas
- [ ] Sé agrupar y agregar datos
- [ ] Sé actualizar consultas cuando los datos cambian
- [ ] Entiendo el valor de Power Query vs Excel tradicional
