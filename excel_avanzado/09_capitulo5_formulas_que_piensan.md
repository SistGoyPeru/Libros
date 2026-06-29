
# Capítulo 5: Fórmulas que Piensan

## Matrices Dinámicas, LET, LAMBDA, BYROW, BYCOL

Una semana después, el taller era un centro de operaciones de inteligencia financiera. Tres computadoras. Cuatro monitores. Datos fluyendo desde Power Query hacia Power Pivot, analizados con DAX, automatizados con VBA.

Pero Sofía sentía que faltaba algo.

—Valeria, todo lo que hacemos está en Power Pivot o en VBA. Pero hay análisis que necesito hacer rápido, en la hoja de cálculo, sin esperar a que el modelo se actualice.

—¿Como qué? —preguntó Valeria.

—Necesito extraer clientes únicos de una lista de transacciones. Ordenarlos por monto total. Filtrar solo los que superan S/ 50,000. Y hacerlo con una sola fórmula, no con múltiples pasos.

Valeria sonrió. —Estás describiendo las **matrices dinámicas** de Excel.

### FILTER: la navaja suiza

—FILTER es una función que devuelve un rango dinámico de celdas que cumplen una condición —dijo Valeria—. No necesitas arrastrar fórmulas, no necesitas Ctrl+Shift+Enter. Solo escribes la fórmula y Excel "derrama" los resultados automáticamente.

Valeria seleccionó una celda vacía en una hoja con 50,000 transacciones y escribió:

```
=FILTER(Transacciones, Transacciones[Monto] > 50000, "Sin resultados")
```

Instantáneamente, todas las transacciones mayores a S/ 50,000 aparecieron, ocupando tantas filas como fueran necesarias.

—El resultado se "derrama" o "spills" —explicó Valeria—. Las celdas circundantes se oscurecen ligeramente para indicar que están ocupadas por el resultado de la fórmula. Si algo bloquea el derrame, Excel muestra `#SPILL!`.

—No necesito saber cuántas filas voy a obtener —dijo Sofía, maravillada—. Excel lo hace solo.

—Exactamente. Las matrices dinámicas cambiaron la forma de trabajar en Excel. Antes necesitabas fórmulas matriciales con Ctrl+Shift+Enter. Ahora, cualquier fórmula que devuelva múltiples valores se derrama automáticamente.

### SORT y SORTBY: ordenando la verdad

—Ahora combinemos FILTER con SORT:

```
=SORT(FILTER(Transacciones, Transacciones[Monto] > 50000), 3, -1)
```

—Esto filtra las transacciones mayores a S/ 50,000 y las ordena por la tercera columna (Monto) en orden descendente (-1).

—¿Y si quiero ordenar por una columna que no está en el resultado? —preguntó Carlos.

—Ahí usas SORTBY:

```
=SORTBY(
    FILTER(Transacciones, Transacciones[Monto] > 50000),
    Transacciones[Cliente],
    1
)
```

—SORTBY ordena según una columna externa, no necesariamente incluida en el resultado.

### UNIQUE: encontrando lo único

—Nova está usando los mismos clientes en diferentes empresas —dijo Valeria—. Necesito una lista de clientes únicos que aparecen en transacciones de múltiples empresas.

```
=UNIQUE(Transacciones[Cliente])
```

—Esto devuelve una lista sin duplicados de todos los clientes.

—Ahora combinemos: clientes que aparecen en transacciones sospechosas.

```
=UNIQUE(FILTER(Transacciones[Cliente], Transacciones[Monto] >= 20000))
```

—Clientes únicos con transacciones de 20,000 o más —dijo Sofía—. Perfecto para detectar reincidentes.

### SEQUENCE: secuencias dinámicas

—SEQUENCE genera secuencias de números. Útil para crear índices, calendarios, simulaciones.

```
=SEQUENCE(10, 1, 1, 1)  ' 10 filas, 1 columna, desde 1, incremento 1
=SEQUENCE(1, 12, 1, 1)  ' 1 fila, 12 columnas (meses)
=SEQUENCE(365, 1, DATE(2026,1,1), 1)  ' Todos los días del año
```

—Podemos crear un calendario completo para nuestro modelo de datos.

### LET: nombrando resultados intermedios

—Las fórmulas se están volviendo largas —dijo Sofía, mirando una línea de 200 caracteres—. Hay repeticiones. Es difícil de leer.

—LET al rescate —dijo Valeria—. LET te permite nombrar cálculos intermedios dentro de una fórmula. Es como declarar variables en una función.

```
=LET(
    datos_filtrados, FILTER(Transacciones, Transacciones[Monto] > 20000),
    clientes_unicos, UNIQUE(CHOOSECOLS(datos_filtrados, 2)),
    total_clientes, COUNTA(clientes_unicos),
    "Clientes con transacciones >20K: " & total_clientes
)
```

—Cada argumento en LET es un par nombre/valor. El último argumento es el resultado final. Es más legible y más eficiente porque los cálculos intermedios solo se evalúan una vez.

—¿Más eficiente? —preguntó Carlos.

—Sí. Si usas FILTER dos veces en una fórmula normal, Excel filtra dos veces. Con LET, filtras una vez y reutilizas el resultado.

### LAMBDA: tus propias funciones

—Ahora viene lo mejor —dijo Valeria—. LAMBDA permite crear funciones personalizadas sin VBA. Directamente en las celdas.

—¿Como crear una función en Excel? —preguntó Sofía, incrédula.

—Sí. Y puedes reutilizarla en todo el libro.

Valeria abrió el **Administrador de nombres** (Fórmulas > Administrador de nombres) y creó una nueva función:

```
Nombre: SOSPECHOSA
Ámbito: Libro
Se refiere a: =LAMBDA(monto, IF(AND(monto >= 20000, monto < 25000), "SOSPECHOSA", "NORMAL"))
```

—Ahora puedes usar `=SOSPECHOSA(A2)` en cualquier celda.

—Es como crear mi propio idioma dentro de Excel —dijo Sofía.

—Exactamente. Y lo mejor es que LAMBDA puede usar todas las funciones de Excel, incluyendo otras LAMBDA.

### BYROW y BYCOL: iterando sobre filas y columnas

—BYROW aplica una función lambda a cada fila de un rango. BYCOL a cada columna.

```
=BYROW(Transacciones, LAMBDA(fila, SOSPECHOSA(INDEX(fila, 3))))
```

—Esto aplica la función SOSPECHOSA a la tercera columna de cada fila de la tabla Transacciones.

—¿Es como un SUMX pero en la hoja? —preguntó Carlos.

—Exactamente. BYROW y BYCOL son los equivalentes en hoja de cálculo de las funciones iteradoras X de DAX.

### MAP, REDUCE y SCAN

—Si BYROW y BYCOL son los básicos, MAP, REDUCE y SCAN son los avanzados.

- **MAP**: Aplica una función a cada elemento y devuelve un array del mismo tamaño
- **REDUCE**: Acumula valores aplicando una función, devolviendo un solo valor
- **SCAN**: Como REDUCE, pero devuelve todos los valores intermedios

```
' MAP: Convertir montos a texto
=MAP(Transacciones[Monto], LAMBDA(m, "S/ " & TEXT(m, "#,##0.00")))

' REDUCE: Sumar montos de clientes específicos
=REDUCE(0, Transacciones[Monto], LAMBDA(acumulado, monto, 
    IF(monto > 20000, acumulado + monto, acumulado)))

' SCAN: Acumulado por fila
=SCAN(0, Transacciones[Monto], LAMBDA(acumulado, monto, acumulado + monto))
```

### El descubrimiento con matrices dinámicas

Sofía combinó todas estas funciones en una sola fórmula que cambió el curso de la investigación:

```
=LET(
    t, Transacciones,
    filtradas, FILTER(t, t[Monto] >= 20000),
    agrupadas, GROUPBY(
        CHOOSECOLS(filtradas, 2),  // Columna cliente
        CHOOSECOLS(filtradas, 3),  // Columna monto
        LAMBDA(v, SUM(v)),
        0,  // Sin encabezados
        ,   // Sin orden
        ,   // Sin agregación adicional
        ,   // Sin filtro adicional
        ,   // Sin subtotales
        ,   // Sin totales
    ),
    ordenadas, SORT(agrupadas, 2, -1),
    top10, TAKE(ordenadas, 10),
    top10
)
```

Los resultados aparecieron en la pantalla:

| Cliente | Total Monto |
|---------|-------------|
| Inversiones Delta S.A.C. | S/ 8,432,000 |
| Constructora del Sur | S/ 2,100,000 |
| Transportes Rápidos | S/ 1,850,000 |
| ... | ... |

—Inversiones Delta aparece como cliente —dijo Sofía—. Pero también como inversor. Están siendo cliente de sí mismos en diferentes empresas fantasma.

—Es el patrón que necesitábamos —dijo Valeria—. Auto-lavado. Mueven dinero de Delta a las empresas, y luego de vuelta a Delta a través de transacciones falsas.

—¿Podemos rastrear todas las transacciones circulares? —preguntó Sofía.

—Con LAMBDA y matrices dinámicas, podemos crear una función que detecte cualquier transacción donde emisor y receptor estén vinculados al mismo grupo empresarial.

Valeria escribió:

```
=LET(
    tr, Transacciones,
    detectar_circular, LAMBDA(fila,
        LET(
            emisor, INDEX(fila, 4),
            receptor, INDEX(fila, 5),
            grupo_emisor, XLOOKUP(emisor, Empresas[ID], Empresas[Grupo]),
            grupo_receptor, XLOOKUP(receptor, Empresas[ID], Empresas[Grupo]),
            IF(AND(grupo_emisor <> "", grupo_receptor <> "", grupo_emisor = grupo_receptor),
                "CIRCULAR", 
                "NORMAL")
        )
    ),
    BYROW(tr, detectar_circular)
)
```

—Esto marcará cada transacción como "CIRCULAR" o "NORMAL". Las circulares son evidencia de lavado de dinero.

—Es hermoso —susurró Sofía—. Todo en una sola fórmula.

—Ese es el poder del análisis —dijo Valeria.

---

## Explicación técnica: Matrices Dinámicas, LET, LAMBDA

### Matrices dinámicas

Las funciones de matrices dinámicas (disponibles en Excel 365 y Excel 2021) devuelven múltiples valores que se "derraman" automáticamente en las celdas adyacentes.

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| FILTER | Filtra un rango según condición | `=FILTER(A1:C100, B1:B100>50)` |
| SORT | Ordena un rango por columna | `=SORT(A1:C100, 2, -1)` |
| SORTBY | Ordena por columna externa | `=SORTBY(A1:C100, D1:D100, 1)` |
| UNIQUE | Valores únicos | `=UNIQUE(A1:A100)` |
| SEQUENCE | Secuencia de números | `=SEQUENCE(10,1,1,1)` |
| RANDARRAY | Array aleatorio | `=RANDARRAY(10,1)` |
| CHOOSECOLS | Selecciona columnas | `=CHOOSECOLS(A1:C100, 1, 3)` |
| CHOOSEROWS | Selecciona filas | `=CHOOSEROWS(A1:C100, 1, 5, 10)` |
| TAKE | Primeras N filas/columnas | `=TAKE(A1:C100, 10)` |
| DROP | Elimina primeras N filas | `=DROP(A1:C100, 5)` |
| VSTACK | Apila verticalmente | `=VSTACK(A1:A10, B1:B10)` |
| HSTACK | Apila horizontalmente | `=HSTACK(A1:A10, B1:B10)` |
| EXPAND | Expande un array | `=EXPAND(A1:A10, 20)` |
| TOCOL | Convierte a columna | `=TOCOL(A1:C10)` |
| TOROW | Convierte a fila | `=TOROW(A1:C10)` |
| WRAPROWS | Agrupa en filas | `=WRAPROWS(A1:A20, 5)` |
| GROUPBY | Agrupa y agrega | `=GROUPBY(rango_col1, rango_valor, LAMBDA(s,SUM(s)))` |
| PIVOTBY | Tabla dinámica con fórmula | `=PIVOTBY(rango_fila, rango_col, rango_valor, LAMBDA(s,SUM(s)))` |

### LET: Variables en fórmulas

**Sintaxis:** `=LET(nombre1, valor1, nombre2, valor2, ..., resultado)`

```
=LET(
    ventas, SUM(Ventas[Monto]),
    costo, SUM(Ventas[Costo]),
    ganancia, ventas - costo,
    ganancia / ventas  -- Margen porcentual
)
```

Beneficios:
1. **Legibilidad**: Nombres descriptivos para cálculos intermedios
2. **Rendimiento**: Los valores se calculan una vez y se reutilizan
3. **Depuración**: Más fácil identificar errores

### LAMBDA: Funciones personalizadas

**Sintaxis:** `=LAMBDA(parámetro1, parámetro2, ..., expresión)`

Crear una LAMBDA reutilizable:
1. Fórmulas > Administrador de nombres
2. Nuevo nombre
3. En "Se refiere a": `=LAMBDA(x, x * 1.18)`
4. Usar: `=IGV(A2)`

**LAMBDA auxiliares** (sin nombre, usadas dentro de otras funciones):

```
=BYROW(A1:A100, LAMBDA(x, x * 1.18))
=MAP(A1:A100, LAMBDA(x, "S/ " & TEXT(x, "#,##0.00")))
=SCAN(0, A1:A100, LAMBDA(acc, x, acc + x))
```

### BYROW, BYCOL, MAP, REDUCE, SCAN

| Función | Entrada | Salida | Descripción |
|---------|---------|--------|-------------|
| BYROW | Array | Array | Aplica lambda a cada fila; resultado una fila por elemento original |
| BYCOL | Array | Array | Aplica lambda a cada columna |
| MAP | Array(s) | Array | Aplica lambda a cada elemento individual |
| REDUCE | Array + valor inicial | Valor único | Acumula usando lambda |
| SCAN | Array + valor inicial | Array | Acumula pero devuelve todos los pasos |

---

### Enigma 5.1: Filtro de transacciones sospechosas

Tienes una tabla `Ventas` con columnas: Fecha, Cliente, Producto, Monto, Cantidad.

Crea una fórmula con matrices dinámicas que:
1. Filtre las ventas donde Monto > 1000
2. Ordene por Monto descendente
3. Seleccione solo las columnas Cliente, Producto, Monto
4. Muestre solo los primeros 10 resultados

### Enigma 5.2: Función LAMBDA de análisis

Crea una función LAMBDA llamada `AnalizarCliente` que:
- Reciba: nombre del cliente, rango de datos
- Devuelva: nombre del cliente, total de compras, cantidad de compras, compra máxima
- Pista: usa FILTER, SUM, COUNT, MAX

### Enigma 5.3: Detección de anomalías con LET y MAP

Usando LET y MAP, crea una fórmula que:
1. Calcule el promedio general de montos
2. Por cada transacción, determine si es "ANÓMALA" (monto > 3 * promedio) o "NORMAL"
3. Devuelva la lista completa con la clasificación

*(Soluciones en el Apéndice)*
