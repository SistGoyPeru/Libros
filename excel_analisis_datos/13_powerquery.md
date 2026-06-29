# Capítulo 9: Power Query para Análisis de Datos

## El transformador de datos definitivo

—Power Query —dijo Valeria— no es solo para limpiar datos. Es la herramienta más poderosa de Excel para preparar datos para el análisis.

### Power Query como motor de análisis

—Power Query puede hacer análisis completos sin escribir una sola fórmula:

```
Editor Power Query:
  - Agrupar por (GROUP BY)
  - Columna condicional
  - Columna personalizada (M language)
  - Combinar consultas (JOIN)
  - Anexar consultas (UNION)
  - Tablas dinámicas directamente desde PQ
```

### Agrupar y resumir en Power Query

—Equivalente a tablas dinámicas pero dentro de Power Query:

```
Inicio > Agrupar por
Operación: Suma, Promedio, Conteo, etc.
Agrupar por: Producto, Mes, Región
```

—El resultado es una tabla resumen que se actualiza automáticamente.

### Columnas condicionales

—Para crear categorías basadas en reglas:

```
Agregar columna > Columna condicional
Si [Monto] >= 10000 entonces "Alto"
Si no, si [Monto] >= 5000 entonces "Medio"
Si no "Bajo"
```

### Combinar consultas (JOIN)

—Para unir tablas como en SQL:

```
Inicio > Combinar > Combinar consultas
Tabla 1: Ventas, columna: ID_Producto
Tabla 2: Productos, columna: ID
Tipo de combinación: (Completa, Externa, Interna, etc.)
```

### Anexar consultas (UNION)

—Para unir tablas con la misma estructura:

```
Inicio > Combinar > Anexar consultas
Seleccionar tablas a unir
```

—Ideal para consolidar datos de múltiples meses o sucursales.

### Power Query + Tablas dinámicas

—El flujo de trabajo definitivo:

```
1. Power Query: Importa, limpia, transforma, combina
2. Cargar a: Tabla dinámica
3. Informe: Tabla dinámica + gráfico dinámico + segmentadores
4. Actualizar: Cuando lleguen nuevos datos, un solo clic
```

### Lenguaje M para transformaciones avanzadas

—Cuando la interfaz no es suficiente:

```
// Ejemplo: Columna personalizada en M
if [Monto] > 100000 then "VIP" else if [Monto] > 50000 then "Premium" else "Regular"

// Ejemplo: Calcular edad desde fecha de nacimiento
Date.From(DateTime.LocalNow()) - [FechaNacimiento]

// Ejemplo: Extraer año de fecha
Date.Year([Fecha])
```

### Power Query para automatización

—La verdadera magia —dijo Valeria— es que todo es reproducible.

```
Cuando recibes datos nuevos:
  1. Reemplazas el archivo fuente
  2. Clic derecho > Actualizar
  3. Todo el proceso de limpieza y análisis se ejecuta solo
```

### Caso práctico: Pipeline de análisis completo

—Valeria mostró el pipeline que usan en Datawise:

```
Consulta 1: Importar ventas del ERP (CSV)
  - Filtrar filas, cambiar tipos, dividir columnas

Consulta 2: Importar catálogo de productos (base de datos)
  - Seleccionar columnas, eliminar duplicados

Consulta 3: Combinar ventas + productos (JOIN por ID)
  - Agregar columna de margen

Consulta 4: Tabla resumen por mes y producto
  - Agrupar por mes y producto
  - Suma de ventas y margen

Cargar a: Tabla dinámica con segmentadores
```

### Enigma #9

En `codigos/c09_powerquery/` hay 3 archivos CSV: `ventas_ene.csv`, `ventas_feb.csv`, `ventas_mar.csv` y un archivo `productos.xlsx`.

**Tu misión:**
1. Importa los 3 CSVs con Power Query y anéxalos en una sola tabla
2. Combínalos con la tabla de productos (JOIN)
3. Agrupa por categoría y mes para obtener ventas totales
4. Agrega una columna condicional que clasifique: "Alto" si venta > 10,000, sino "Bajo"
5. Carga el resultado a una tabla dinámica con segmentador por mes
6. Configura: cuando se agregue un nuevo CSV a la carpeta, con actualizar basta