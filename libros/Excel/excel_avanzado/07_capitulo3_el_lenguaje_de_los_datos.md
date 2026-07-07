
# Capítulo 3: El Lenguaje de los Datos

## DAX Básico — CALCULATE, SUMX, FILTER, ALL, DISTINCT

—Lo que hemos hecho hasta ahora es solo el comienzo —dijo Valeria, mientras el sol se ponía sobre Barranco—. Power Query nos dio los datos limpios. Power Pivot nos dio el modelo. Pero para encontrar la verdad, necesitamos el lenguaje de los datos.

—¿DAX? —preguntó Sofía.

—Data Analysis Expressions. El lenguaje que da vida al modelo de datos.

Valeria abrió Power Pivot y navegó a la tabla Inversiones_Delta.

—DAX se escribe en la barra de fórmulas de Power Pivot o en las medidas de una tabla dinámica. Tiene tres tipos de elementos:

1. **Funciones de agregación**: SUM, COUNT, AVERAGE, MIN, MAX
2. **Funciones de iteración**: SUMX, COUNTX, AVERAGEX, FILTER
3. **Funciones de contexto**: CALCULATE, ALL, ALLEXCEPT, FILTER, VALUES

—Las primeras son fáciles —continuó Valeria—. Son como las de Excel. SUM suma, COUNT cuenta, AVERAGE promedia. Pero las verdaderamente poderosas son las de contexto.

### El primer problema: montos sospechosos

—Necesito una medida que calcule el total de transacciones de Delta, pero solo de aquellas empresas que NO son el Taller Mendoza —dijo Valeria—. Para ver el patrón completo sin que nuestros datos nos contaminen el análisis.

—¿No basta con filtrar la tabla dinámica? —preguntó Carlos.

—Podría, pero necesito que el cálculo sea dinámico y robusto. Si alguien cambia los filtros, la medida debe seguir funcionando correctamente.

Valeria escribió:

```
Ventas Sin Mendoza:=CALCULATE(
    SUM(Transacciones[Monto]),
    Empresas_Nova[Razon_Social] <> "Taller Mendoza & Hijos"
)
```

—CALCULATE es la función más importante de DAX. Toma una expresión (como SUM) y uno o más **filtros**. El filtro modifica el contexto en el que se evalúa la expresión.

—¿Qué significa "modifica el contexto"? —preguntó Sofía.

—Imagina que tienes una tabla dinámica con meses en las filas. Cuando ves el total de enero, SUM(Transacciones[Monto]) solo suma enero. Eso es el **contexto de filtro**. CALCULATE puede cambiar ese contexto.

—¿Como un SI condicional? —preguntó Carlos.

—Más potente. CALCULATE puede hacer filtros complejos con múltiples condiciones, usar funciones como ALL para ignorar filtros, y crear escenarios de análisis que serían imposibles con fórmulas de Excel tradicionales.

### Iterando sobre las transacciones

—Ahora necesito otra medida —dijo Valeria—. Quiero calcular el monto total de transacciones sospechosas. Definimos "sospechosa" como cualquier transacción de más de S/ 20,000 que venga de Delta.

—Eso suena a un SI condicional sumado muchas veces —dijo Sofía.

—Exactamente. Y para eso están las funciones **iteradoras**.

Valeria escribió:

```
Transacciones Sospechosas:=SUMX(
    Transacciones,
    IF(
        Transacciones[Monto] > 20000 && 
        Transacciones[Origen] = "Delta",
        Transacciones[Monto],
        0
    )
)
```

—SUMX itera sobre cada fila de la tabla Transacciones. Para cada fila, evalúa la expresión IF. Si la condición se cumple, suma el monto. Si no, suma 0.

—Es como una fórmula matricial —observó Sofía.

—Exactamente. SUMX, AVERAGEX, COUNTX, MINX, MAXX... todas son funciones **X** que iteran fila por fila. Son lentas si se usan en tablas enormes sin filtros, pero con Power Pivot y el motor VertiPaq, el rendimiento es sorprendente.

—¿Cuándo usar SUM y cuándo SUMX? —preguntó Carlos.

—SUM se usa cuando quieres sumar una columna directamente. SUMX se usa cuando necesitas hacer un cálculo por fila antes de sumar. Por ejemplo, si tuvieras Precio y Cantidad en columnas separadas:
  - SUM(Precio * Cantidad) NO funciona (no es una columna)
  - SUMX(Tabla, Precio * Cantidad) SÍ funciona

### Ignorando filtros con ALL

—Ahora quiero una medida que calcule el porcentaje que representa cada empresa respecto al total general, sin importar qué filtros tenga la tabla dinámica.

Valeria escribió:

```
% del Total:=DIVIDE(
    SUM(Transacciones[Monto]),
    CALCULATE(SUM(Transacciones[Monto]), ALL(Empresas_Nova))
)
```

—ALL rompe el contexto de filtro. CALCULATE(..., ALL(Tabla)) ignora cualquier filtro aplicado a esa tabla. Así, el denominador siempre es el total general, sin importar qué fila o segmentación esté activa.

—Es como un Gran Total que no cambia —dijo Sofía.

—Exactamente. Y DIVIDE es la función segura para divisiones. Si el denominador es 0, devuelve un valor predeterminado (blank) en lugar de un error.

### DESCUBRIENDO EL PATRÓN

Esa noche, con las medidas creadas, construyeron una tabla dinámica que cruzaba:

- **Filas**: Empresas_Nova[Razón Social]
- **Valores**: 
  - Transacciones[Total Ventas]
  - Inversiones[Transacciones Sospechosas]
  - Inversiones[% del Total]

Los resultados helaron la sangre de Sofía:

| Empresa | Total Ventas | Transacciones Sospechosas | % del Total |
|---------|-------------|--------------------------|-------------|
| Lavandería El Sol | S/ 340,210 | S/ 960,000 | 8.2% |
| Restaurante La Marina | S/ 520,430 | S/ 2,720,000 | 23.3% |
| Ferretería Los Andes | S/ 210,845 | S/ 712,000 | 6.1% |
| Taller Mecánico Rápido | S/ 180,320 | S/ 1,680,000 | 14.4% |
| Empresa Fantasma #1 | S/ 0 | S/ 3,400,000 | 29.1% |
| Empresa Fantasma #2 | S/ 0 | S/ 2,200,000 | 18.9% |

—¿Empresas fantasma? —preguntó Carlos.

—No tienen ventas reales —dijo Valeria—. Solo reciben transferencias de Delta. Son empresas creadas exclusivamente para mover dinero.

—¿Cuánto dinero en total? —preguntó Sofía.

Valeria agregó una medida:

```
Total Sistema:=CALCULATE(
    SUM(Inversiones_Delta[Monto_Total]),
    ALL(Empresas_Nova)
)
```

—S/ 11,672,000 —leyó—. Casi doce millones de soles en transacciones sospechosas.

—¿Y cuánto de eso está vinculado a nuestro taller? —preguntó Sofía.

—Cero. Hasta ahora. Pero tu oferta de $850,000 probablemente es el vehículo para mover dinero a través de tu empresa.

—¿Por qué nosotros? —preguntó Carlos.

—Porque no están en el radar de la UIF. Tu taller tiene historial limpio, contratos vigentes, flujo de caja saludable. Son la fachada perfecta.

### Una medida más: la prueba del 24K

Valeria sonrió. —Ahora la medida que lo cambia todo.

```
Transacciones Fraccionadas:=COUNTROWS(
    FILTER(
        Transacciones,
        Transacciones[Monto] >= 20000 && 
        Transacciones[Monto] < 25000 &&
        Transacciones[Origen] = "Delta"
    )
)
```

—FILTER crea una tabla temporal que cumple una condición. COUNTROWS cuenta las filas de esa tabla. Así sabemos cuántas transacciones de Delta están justo debajo del límite de reporte.

El resultado: 287 transacciones.

—Doscientas ochenta y siete veces que movieron dinero justo debajo del radar —dijo Valeria—. Eso no es coincidencia. Es estructuración. Es evidencia.

—¿Podemos presentar esto a la UIF? —preguntó Sofía.

—No todavía. Necesitamos más. Necesitamos automatizar el análisis, porque los datos de Delta se actualizan cada semana. Y necesitamos visualizaciones profesionales que cuenten la historia.

—Entonces —dijo Sofía, con determinación—. VBA. Macros. Automatización.

Valeria sonrió. —Exactamente. Bienvenida al siguiente nivel.

---

## Explicación técnica: DAX Básico

### ¿Qué es DAX?

**Data Analysis Expressions (DAX)** es un lenguaje de fórmulas creado por Microsoft para modelos de datos tabulares en Power Pivot, Power BI y Analysis Services. Combina conceptos de funciones de Excel con la potencia de lenguajes de bases de datos relacionales.

### Funciones de agregación básicas

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| SUM | Suma todos los valores de una columna | SUM(Ventas[Monto]) |
| COUNT | Cuenta valores numéricos en una columna | COUNT(Ventas[ID]) |
| COUNTROWS | Cuenta filas de una tabla | COUNTROWS(Ventas) |
| DISTINCTCOUNT | Cuenta valores únicos en una columna | DISTINCTCOUNT(Clientes[ID]) |
| AVERAGE | Promedio de valores en una columna | AVERAGE(Ventas[Monto]) |
| MIN | Valor mínimo | MIN(Ventas[Monto]) |
| MAX | Valor máximo | MAX(Ventas[Monto]) |

### Funciones iteradoras (X)

Evalúan una expresión para cada fila de una tabla y luego agregan los resultados:

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| SUMX | Suma de expresión por fila | SUMX(Ventas, Ventas[Cantidad] * Ventas[Precio]) |
| COUNTX | Conteo de filas que cumplen | COUNTX(Ventas, IF(Ventas[Monto]>100,1)) |
| AVERAGEX | Promedio de expresión por fila | AVERAGEX(Ventas, Ventas[Monto]) |
| MINX | Mínimo por fila | MINX(Ventas, Ventas[Monto] * 0.9) |
| MAXX | Máximo por fila | MAXX(Ventas, Ventas[Monto]) |
| FILTER | Devuelve tabla filtrada | FILTER(Ventas, Ventas[Monto] > 1000) |

### CALCULATE: La función reina

**CALCULATE** cambia el contexto de filtro en el que se evalúa una expresión.

```
CALCULATE(expresión, filtro1, filtro2, ...)
```

Ejemplos:

```dax
-- Ventas del año 2024
Ventas 2024:=CALCULATE(SUM(Ventas[Monto]), Ventas[Año] = 2024)

-- Ventas del cliente premium
Ventas Premium:=CALCULATE(
    SUM(Ventas[Monto]),
    Clientes[Categoría] = "Premium"
)

-- Ventas sin incluir una categoría
Ventas Sin Ropa:=CALCULATE(
    SUM(Ventas[Monto]),
    Productos[Categoría] <> "Ropa"
)
```

### ALL y variantes

**ALL** ignora filtros sobre una tabla o columna:

```dax
-- Total general (ignora todos los filtros)
Total General:=CALCULATE(SUM(Ventas[Monto]), ALL(Ventas))

-- Porcentaje sobre el total
% Total:=DIVIDE(SUM(Ventas[Monto]), CALCULATE(SUM(Ventas[Monto]), ALL(Productos)))
```

**ALLEXCEPT** ignora todos los filtros excepto los de una columna:

```dax
-- Total por categoría (ignora filtros de otras tablas)
Total Categoría:=CALCULATE(SUM(Ventas[Monto]), ALLEXCEPT(Productos, Productos[Categoría]))
```

### FILTER como función

FILTER devuelve una tabla filtrada, útil dentro de otras funciones:

```dax
-- Conteo de productos con ventas > 1000
Productos Top:=COUNTROWS(
    FILTER(Productos, [Total Ventas] > 1000)
)

-- Suma de ventas solo de los top 10 clientes
Ventas Top10:=SUMX(
    TOPN(10, Clientes, [Total Ventas], DESC),
    [Total Ventas]
)
```

### DISTINCT y VALUES

Devuelven valores únicos de una columna:

```dax
-- Conteo de productos distintos vendidos
Productos Vendidos:=DISTINCTCOUNT(Ventas[ID_Producto])

-- Lista de categorías (en medida)
Categorías:=CONCATENATEX(VALUES(Productos[Categoría]), Productos[Categoría], ", ")
```

### DIVIDE: División segura

Reemplaza división tradicional y evita errores #DIV/0!:

```dax
-- Margen de ganancia
Margen:=DIVIDE(
    SUM(Ventas[Ganancia]),
    SUM(Ventas[Ingreso]),
    0  -- valor alternativo si denominador es 0
)
```

### Buenas prácticas en DAX

1. **Usar nombres de medida descriptivos**: `Total Ventas FY2024` en vez de `Medida1`
2. **Prefijar medidas**: Con `_` o `M_` para identificarlas fácilmente
3. **Evitar cálculos innecesarios**: Las medidas se recalculan en cada interacción
4. **Documentar medidas**: Usar la propiedad **Descripción** en Power Pivot
5. **Probar con datos pequeños**: Verificar resultados antes de escalar
6. **Usar variables (VAR)**: Para cálculos intermedios (mejor rendimiento y legibilidad)

---

### Enigma 3.1: CALCULATE en acción

Tienes una tabla Ventas con columnas: Fecha, Monto, ID_Cliente, ID_Producto, Región, Canal.

Crea las siguientes medidas:
1. `Ventas Región Norte` — Ventas donde Región = "Norte"
2. `Ventas Canal Online` — Ventas donde Canal = "Online"
3. `Ventas Sin Región Sur` — Ventas totales excluyendo la región Sur
4. `% Ventas Online` — Porcentaje de ventas online sobre el total

### Enigma 3.2: Iteradores y FILTER

Usando la misma tabla Ventas:

1. `Ventas con Descuento` — Suma de Monto * 0.95 (tiene un 5% de descuento)
2. `Ventas Premium` — Suma de ventas de clientes que están en la tabla Clientes con Categoría = "Premium"
3. `Productos Estrella` — Cuenta cuántos productos tienen ventas totales mayores a S/ 50,000
4. `Transacciones Grandes` — Suma de ventas cuyo monto individual supera los S/ 10,000

### Enigma 3.3: Análisis forense

Eres el auditor forense. Tienes un modelo con:
- `Transacciones`: ID, Fecha, Monto, ID_Empresa, ID_Cliente, Tipo
- `Empresas`: ID, Razón_Social, Fecha_Adquisición, Grupo
- `Clientes`: ID, Nombre, Tipo (Persona Natural / Jurídica)

Necesitas crear medidas que identifiquen:
1. Transacciones que suman justo debajo de S/ 25,000 agrupadas por cliente y fecha (estructuración)
2. Clientes que aparecen en múltiples empresas de un mismo grupo
3. Porcentaje de transacciones con personas naturales vs jurídicas (con ALL para el total general)

Escribe las medidas DAX.

*(Soluciones en el Apéndice)*
