# Capítulo 2: Limpieza y Preparación de Datos

## El 80% del trabajo del analista

—Los datos del mundo real —dijo Valeria— vienen sucios. Siempre. Aceptarlo es el primer paso.

### La Historia

Andrés abrió el archivo que el gerente de ventas había enviado.

—Esto es un desastre —murmuró.

—Déjame adivinar —dijo Valeria—. Fechas en formatos mezclados, números como texto, espacios extra, filas vacías, y algunos valores que no deberían estar ahí.

—¿Cómo lo sabes?

—Porque siempre es así.

### Técnicas de limpieza en Excel

**1. Eliminar duplicados**

```
Datos > Quitar duplicados
```
—Siempre revisa qué columnas definen un duplicado antes de eliminarlos.

**2. Texto en columnas**

```
Datos > Texto en columnas
```
—Separa nombres completos, direcciones, códigos combinados.

**3. Funciones de limpieza**

```
=ESPACIOS(texto)       'Elimina espacios extra'
=MAYUSC(texto)          'Convierte a mayúsculas'
=NOMPROPIO(texto)       'Primera letra mayúscula'
=SUSTITUIR(texto, "antiguo", "nuevo")
=HALLAR("texto", celda) 'Busca dentro de un texto'
```

**4. Limpiar con Power Query**

—Power Query tiene herramientas de limpieza integradas:

```
Editor Power Query:
  - Quitar filas en blanco
  - Quitar duplicados
  - Dividir columnas
  - Reemplazar valores
  - Cambiar tipo (texto, número, fecha)
  - Recortar (trim)
  - Limpiar (clean - caracteres no imprimibles)
```

### Detección de datos atípicos

—Antes de analizar —dijo Valeria—, debemos detectar anomalías.

**Rango intercuartil (IQR):**
```
Q1 = CUARTIL(rango, 1)
Q3 = CUARTIL(rango, 3)
IQR = Q3 - Q1
Límite inferior = Q1 - 1.5 * IQR
Límite superior = Q3 + 1.5 * IQR
```

**Formato condicional para outliers:**
```
Seleccionar columna > Formato condicional > Reglas > Mayor que
Valor: Límite superior
Formato: Fondo rojo
```

### Manejo de valores faltantes

—¿Qué hago con las celdas vacías? —preguntó Andrés.

—Depende —respondió Valeria—. Tres opciones:

**Opción 1: Eliminar fila** (si el dato faltante es crítico)
```
Filtro > (Espacios en blanco) > Eliminar fila
```

**Opción 2: Rellenar con promedio**
```
=SI.ERROR(A2, PROMEDIO(rango))
```

**Opción 3: Rellenar con valor anterior**
```
Inicio > Buscar y seleccionar > Ir a especial > Celdas vacías
Escribir =ARRIBA() y presionar Ctrl+Enter
```

### Estandarización de datos

—Los datos deben ser consistentes —dijo Valeria.

**Categorías con validación de datos:**
```
Datos > Validación de datos > Lista
Origen: Venta, Devolución, Ajuste
```

**Fechas estandarizadas:**
```
=TEXTO(fecha, "aaaa-mm-dd")
```
—El formato ISO (aaaa-mm-dd) evita confusiones regionales.

**Moneda con formato contable:**
```
Formato de número > Contabilidad
Símbolo: S/ o $
```

### Power Query para limpieza automática

—La clave —dijo Valeria— es crear una consulta de Power Query que haga toda la limpieza automáticamente.

```
Consulta: "Limpieza Ventas"
Pasos:
  1. Origen: Archivo CSV
  2. Promover encabezados
  3. Cambiar tipo de columna (fecha, número, texto)
  4. Quitar filas con errores
  5. Reemplazar valores nulos
  6. Dividir columna "Nombre Completo" por espacio
  7. Recortar espacios
  8. Cerrar y cargar en tabla
```

—Cuando lleguen nuevos datos, solo haces clic derecho > Actualizar.

### Resumen del capítulo

| Problema | Solución en Excel |
|----------|------------------|
| Duplicados | Quitar duplicados |
| Espacios extra | =ESPACIOS() |
| Formato mezclado | Texto en columnas |
| Valores faltantes | Promedio o valor anterior |
| Datos atípicos | IQR + formato condicional |
| Limpieza automática | Power Query |

### Enigma #2

El archivo `codigos/c02_limpieza/datos_sucios.xlsx` contiene 5,000 registros de clientes con todo tipo de problemas: duplicados, espacios, formatos mezclados, valores faltantes y datos inconsistentes.

**Tu misión:**
1. Identifica y cuantifica los problemas (duplicados, nulos, formatos incorrectos)
2. Limpia los datos usando Power Query (crea una consulta reproducible)
3. Estandariza nombres, fechas y montos
4. Elimina outliers usando el método IQR
5. Entrega: un archivo limpio con una hoja "Resumen" que muestre cuántos problemas se encontraron y resolvieron