
# Capítulo 1: El Descubrimiento

## Power Query — Obtener y transformar datos

Valeria conectó el disco duro a la computadora de Sofía. El explorador mostró más de 200 archivos entre CSV, PDF, TXT y archivos de Excel.

—Esto es solo una fracción de lo que tenemos —dijo Valeria—. La UIF nos ha dado acceso a los movimientos bancarios de Nova y sus empresas vinculadas durante los últimos tres años. Tenemos aproximadamente 150,000 transacciones.

Carlos silbó bajito. —¿Quinientas mil filas de datos? ¿Excel puede manejar eso?

—Excel normal tiene un límite de 1,048,576 filas —respondió Valeria—. El problema no es el volumen, es cómo procesarlo. Si intentamos abrir estos archivos uno por uno y copiar y pegar, nos tomaría semanas.

—¿Y Power Query? —preguntó Sofía.

—Power Query puede conectarse a múltiples fuentes simultáneamente, limpiar los datos, transformarlos y cargarlos en el modelo de datos de Excel. Y todo sin escribir una sola línea de código.

Valeria abrió Excel y navegó a la pestaña **Datos**.

—Power Query está integrado en Excel desde la versión 2016. En Excel 2010 y 2013 era un add-in descargable. En Microsoft 365, es nativo.

—Nunca había usado esa pestaña —admitió Carlos.

—Ese es el problema de la mayoría de usuarios —dijo Valeria—. Excel tiene un poder oculto que pocos exploran.

### La primera conexión

Valeria hizo clic en **Obtener datos (Power Query)**.

—Power Query puede conectarse a: archivos (Excel, CSV, TXT, PDF, JSON, XML), bases de datos (SQL Server, Oracle, Access, MySQL), servicios en la nube (Azure, SharePoint, Salesforce, Google Analytics), otras fuentes (web, ODBC, OData, Active Directory).

—¿Incluso PDF? —preguntó Carlos.

—Sí. Power Query puede extraer tablas de archivos PDF. No es perfecto, pero funciona sorprendentemente bien.

Seleccionó **Desde archivo > Desde CSV** y eligió el primer archivo: `Banco_Nacional_2024.csv`.

El Editor de Power Query se abrió, mostrando una vista previa de los datos.

—Esto es el Editor de Power Query —explicó Valeria—. Es un entorno separado de Excel donde puedes transformar datos sin afectar el original. Cada transformación que aplicas se registra como un "paso aplicado".

En la pantalla, la tabla tenía 15 columnas y 12,547 filas. Pero los datos estaban sucios:

- La columna `Fecha` tenía mezcla de formatos (dd/mm/aaaa, mm/dd/aaaa, texto)
- La columna `Monto` tenía símbolos de moneda y espacios
- Había filas vacías intercaladas
- Algunas columnas tenían nombres genéricos como `Column1`, `Column2`
- La columna `Tipo de Transacción` tenía valores inconsistentes (mayúsculas, minúsculas, abreviaturas)

—Un desastre —dijo Sofía.

—Perfecto para Power Query.

Valeria comenzó a aplicar transformaciones:

1. **Promover encabezados**: Usó la opción "Usar la primera fila como encabezados" para que `Column1` se convirtiera en `Fecha`, etc.

2. **Cambiar tipo de datos**: En la columna `Fecha`, seleccionó "Tipo de datos > Fecha". Power Query transformó automáticamente todos los formatos inconsistentes.

3. **Reemplazar valores**: En `Monto`, usó "Reemplazar valores" para quitar `"S/ "` y `","`, luego cambió el tipo a "Número decimal".

—Cada transformación aparece aquí —dijo Valeria, señalando el panel "Pasos aplicados" a la derecha.

Los pasos se veían así:

| # | Paso | Descripción |
|---|------|-------------|
| 1 | Origen | Conexión al archivo CSV |
| 2 | Navegación | Selección de la tabla |
| 3 | Tipo cambiado | Excel infirió tipos iniciales |
| 4 | Encabezados promovidos | Primera fila como nombres |
| 5 | Tipo de fecha cambiado | Fecha unificada |
| 6 | Valores reemplazados | S/ y comas quitados |
| 7 | Filas vacías quitadas | Eliminación de nulls |

—Lo mejor —dijo Valeria— es que puedo guardar esta consulta y aplicarla a cualquier archivo con la misma estructura. Es completamente reproducible.

### Conectando múltiples fuentes

En las siguientes horas, conectaron cuatro fuentes:

1. **CSV bancarios** — 3 archivos de diferentes bancos (Banco Nacional, Banco Continental, Banco del Sur)
2. **PDF de transacciones** — 12 archivos PDF del portal de facturación electrónica de Nova
3. **Web scraping básico** — Datos de la SUNAT (Superintendencia Nacional de Aduanas y de Administración Tributaria) exportados como HTML
4. **Base de datos Access** — Registros contables internos de Nova (proporcionados por un informante anónimo)

—Power Query puede combinar todas estas fuentes —explicó Valeria—. Se llama **Combinar consultas**.

Creó una consulta principal haciendo clic en **Inicio > Combinar > Combinar consultas** y seleccionó como clave la columna `ID_Transacción`.

—Es como un BUSCARV, pero mucho más eficiente. Power Query usa algoritmos de combinación que son órdenes de magnitud más rápidos.

—¿Podemos ver el resultado? —preguntó Sofía.

Valeria hizo clic en **Cerrar y cargar**. Los datos fluyeron hacia el modelo de datos de Excel. En segundos, tenían una tabla con 278,431 filas y 42 columnas.

—Es hermoso —susurró Carlos.

—Es el poder del análisis —corrigió Valeria.

### El primer hallazgo

Con los datos ya en Excel, Valeria creó una tabla dinámica básica para explorar las transacciones.

—Miren esto —dijo, señalando la pantalla.

La tabla mostraba transacciones agrupadas por mes. En la columna de `Monto`, los valores de diciembre eran anormalmente altos.

—Diciembre es un mes alto para cualquier negocio —dijo Sofía—. Es navidad, la gente compra más...

—Tres veces más que noviembre —interrumpió Valeria—. Pero miren el detalle. Estas transacciones de diciembre no son ventas. Son transferencias desde una cuenta llamada "Inversiones Delta".

Valeria filtró la tabla dinámica para mostrar solo las transacciones de Delta.

—Ciento veinte mil dólares —leyó Sofía—. Transferidos en cinco transacciones de 24,000 dólares cada una.

—Exactamente debajo del límite de reporte obligatorio —dijo Valeria—. En Perú, las transacciones mayores a 25,000 dólares deben reportarse a la UIF. Cada una de estas es de 24,000.

—¿Estructuración? —preguntó Sofía.

—Exactamente. El lavado de dinero clásico: dividir grandes sumas en montos más pequeños para evitar la detección.

Carlos se inclinó hacia la pantalla. —¿Y podemos demostrar que es intencional?

—Con Power Query, podemos analizar todos los patrones de transacciones de Delta en todas las empresas que han comprado —dijo Valeria—. Si el patrón se repite, es evidencia.

—¿Cuánto tiempo tomaría?

—Con Power Query, una hora. Sin Power Query, una semana.

---

## Explicación técnica: Power Query

### ¿Qué es Power Query?

Power Query es un motor de obtención y transformación de datos integrado en Excel (y Power BI). Su propósito es conectar, combinar, limpiar y dar forma a los datos de diferentes fuentes para que estén listos para el análisis.

### Interfaz del Editor de Power Query

El Editor de Power Query tiene estos componentes principales:

1. **Cinta de opciones**: Con pestañas (Inicio, Transformar, Agregar columna, Vista, Herramientas)
2. **Panel de consultas**: Lista de todas las consultas (tablas) cargadas
3. **Vista previa de datos**: Muestra los datos de la consulta seleccionada
4. **Panel de pasos aplicados**: Cada transformación se registra como un paso
5. **Barra de fórmulas**: Muestra la fórmula M generada por cada paso

### Transformaciones más comunes en Power Query

| Transformación | Cómo se hace | Resultado |
|----------------|-------------|-----------|
| Promover encabezados | Inicio > Usar primera fila como encabezados | Convierte fila 1 en nombres de columna |
| Cambiar tipo | Inicio > Tipo de datos | Fuerza un tipo (texto, número, fecha) |
| Reemplazar valores | Inicio > Reemplazar valores | Busca y reemplaza texto específico |
| Quitar filas | Inicio > Quitar filas > Quitar filas en blanco | Elimina filas vacías |
| Dividir columna | Inicio > Dividir columna | Separa texto por delimitador |
| Agrupar por | Inicio > Agrupar por | Agrega datos (similar a tabla dinámica) |
| Combinar consultas | Inicio > Combinar > Combinar consultas | Une dos tablas por una clave común |
| Anexar consultas | Inicio > Combinar > Anexar consultas | Apila tablas una debajo de otra |
| Columna condicional | Agregar columna > Columna condicional | Crea valores basados en condiciones |
| Columna personalizada | Agregar columna > Columna personalizada | Usa fórmulas M para crear columnas |

### M, el lenguaje de Power Query

Power Query tiene su propio lenguaje llamado **M**. Cada transformación que haces en la interfaz gráfica genera código M automáticamente.

Ejemplo de código M generado al importar y limpiar un CSV:

```m
let
    Origen = Csv.Document(File.Contents("C:\Datos\Banco.csv"),[Delimiter=",", Columns=12, Encoding=65001]),
    #"Encabezados promovidos" = Table.PromoteHeaders(Origen, [PromoteAllScalars=true]),
    #"Tipo cambiado" = Table.TransformColumnTypes(#"Encabezados promovidos",{
        {"Fecha", type date},
        {"Monto", type number},
        {"Descripcion", type text}
    }),
    #"Filas filtradas" = Table.SelectRows(#"Tipo cambiado", each [Monto] > 0)
in
    #"Filas filtradas"
```

Cada paso tiene un nombre (con `#"` si tiene espacios), una función y una referencia al paso anterior.

### Combinar vs Anexar consultas

**Combinar (Merge)**: Equivalente a un JOIN en SQL. Une dos tablas basándose en una columna clave. Se puede elegir el tipo: Left Outer, Right Outer, Full Outer, Inner, etc.

**Anexar (Append)**: Equivalente a UNION en SQL. Apila filas de una tabla debajo de otra. Requiere que las columnas tengan los mismos nombres.

### Power Query vs. Fórmulas tradicionales

| Operación | Fórmula tradicional | Power Query |
|-----------|---------------------|-------------|
| Buscar en otra tabla | BUSCARV / XLOOKUP | Combinar consultas |
| Quitar duplicados | Eliminar duplicados manual | Quitar duplicados (paso reproducible) |
| Dividir texto | Texto a columnas (manual) | Dividir columna (paso reproducible) |
| Filtrar datos | Autofiltro manual | Filtrar filas (paso reproducible) |
| Actualizar datos | Repetir todo manual | Actualizar consulta (un clic) |

### Consejos prácticos

1. **Siempre trabajar sobre una copia**: Power Query nunca modifica los datos originales
2. **Usar nombres descriptivos**: Renombrar cada paso para saber qué hace
3. **Documentar las consultas**: El paso "Propiedades" permite agregar descripciones
4. **Probar con datos pequeños**: Antes de aplicar a 200,000 filas, probar con 100
5. **Actualizar datos**: Con un clic derecho > "Actualizar" se re-ejecuta toda la consulta

---

### Enigma 1.1: Limpieza de datos bancarios

Tienes un archivo CSV con transacciones bancarias. El archivo tiene estos problemas:
- Los encabezados están en la fila 5 (las filas 1-4 tienen basura)
- La columna Fecha tiene formato inconsistente (algunas en texto "Ene 15, 2024", otras en número "45325")
- La columna Monto tiene el formato "S/ 1,234.56"
- Hay filas donde Monto es negativo (son los retiros, deben marcarse como "Retiro" en una columna Tipo)

Describe el proceso en Power Query para limpiar estos datos.

### Enigma 1.2: Detectar estructuración

Usando una tabla con transacciones de un año, determina:
1. ¿Cuántas transacciones hay entre 20,000 y 24,999?
2. ¿Son de los mismos emisores?
3. ¿Suman un total que podría ser una sola transacción mayor a 100,000?

Crea una consulta en Power Query que filtre las transacciones por rango de monto y las agrupe por emisor.

### Enigma 1.3: Combinar tres fuentes

Tienes tres archivos:
- `Ventas_2024.xlsx` — Ventas del año (cliente, producto, monto, fecha)
- `Clientes_Nova.csv` — Lista de clientes de Nova (RUC, razón social, dirección)
- `Transacciones_2024.pdf` — PDF con transacciones bancarias de Nova

Describe cómo usarías Power Query para:
1. Importar cada archivo
2. Limpiar los datos (asume problemas comunes: filas vacías, formatos mixtos)
3. Combinar las tres tablas en un solo modelo usando la columna RUC como clave

*(Soluciones en el Apéndice)*
