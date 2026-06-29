# Apéndice: Soluciones a los Enigmas

---

## Capítulo 1: El Archivo Secreto

### Enigma 1.1: Los valores atípicos

**Solución:**
1. Selecciona la columna Valor_B. Ve a **Inicio > Formato condicional > Barras de datos** y elige el estilo de tu preferencia.
2. Selecciona la columna Valor_A. Ve a **Inicio > Formato condicional > Escalas de color > Blanco-Rojo**.
3. Selecciona la columna Valor_C. Ve a **Inicio > Formato condicional > Conjuntos de iconos > Flechas**.

**Observación:** Los valores más altos de Valor_A y Valor_B tienden a concentrarse en los meses de noviembre y diciembre de cada año, lo que sugiere compras o movimientos estacionales. Los valores de Valor_C no siguen el mismo patrón, indicando que es un tipo de dato diferente.

---

### Enigma 1.2: Regla personalizada para fechas

**Solución:**
1. Selecciona todo el rango de datos (A1:E1001).
2. **Inicio > Formato condicional > Nueva regla.**
3. Selecciona "Utilice una fórmula que determine las celdas para aplicar formato".
4. Escribe la fórmula:
   ```
   =$E2<FECHA(2008;1;1)
   ```
5. Haz clic en **Formato** > **Relleno** > elige amarillo.
6. Acepta.

**Resultado:** Las filas con fecha anterior al 1 de enero de 2008 se resaltan en amarillo. Para saber cuántas son, aplica un filtro por color: selecciona el encabezado de columna, **Ordenar y filtrar > Filtrar > Filtrar por color > Amarillo**. Excel mostrará solo las filas resaltadas. El número de filas dependerá de tus datos.

---

### Enigma 1.3: Detectando duplicados con formato condicional

**Solución:**
1. Selecciona la columna Código (A2:A1001).
2. **Inicio > Formato condicional > Reglas para resaltar celdas > Valores duplicados.**
3. Acepta los valores predeterminados.

**Interpretación:** Si hay códigos duplicados, podría significar que:
- El abuelo registró la misma transacción dos veces
- Hay dos transacciones diferentes con el mismo código (error)
- El código no es único y necesita combinarse con la fecha para serlo

Para un análisis más preciso, crea una columna auxiliar con `=A2&E2` (código + fecha) y aplica el formato condicional a esta nueva columna.

---

## Capítulo 2: Pistas Ocultas

### Enigma 2.1: Crea la lista de productos del taller

**Solución:**
1. Crea una nueva hoja con las columnas: N° Pedido, Cliente, Producto, Madera, Cantidad, Precio Unitario, Total.
2. Selecciona la columna Producto. **Datos > Validación de datos > Configuración.**
   - Permitir: Lista
   - Origen: Silla, Mesa, Ropero, Estante, Cama, Banco, Puerta
3. Selecciona la columna Madera. **Datos > Validación de datos > Configuración.**
   - Permitir: Lista
   - Origen: Caoba, Cedro, Roble, Pino, Tornillo, Nogal, Cerezo
4. Para los mensajes de entrada, ve a la pestaña **Mensaje de entrada** en cada validación y escribe un título y mensaje descriptivo.
5. En la columna Total, usa la fórmula: `=Cantidad * Precio_Unitario` (multiplicar las celdas correspondientes).

---

### Enigma 2.2: Validación personalizada

**Solución:**
1. Selecciona la columna Cantidad (asumiendo que es la columna E).
2. **Datos > Validación de datos > Configuración.**
   - Permitir: Número entero
   - Datos: entre
   - Mínimo: 1
   - Máximo: 500
3. **Mensaje de error:**
   - Título: "Cantidad no válida"
   - Mensaje: "La cantidad debe estar entre 1 y 500 unidades"

---

### Enigma 2.3: Detecta validaciones ocultas

**Solución:**
1. Selecciona toda la hoja (clic en el triángulo entre A y 1).
2. **Datos > Validación de datos > Circular celdas con validación inválida.**
3. Excel resaltará las celdas que contienen datos que no cumplen con las reglas de validación existentes.

**Resultado:** Dependerá del archivo. Si no hay validaciones definidas, Excel mostrará un mensaje indicando que no hay celdas con validación. Si las hay, las celdas inválidas se resaltarán.

---

## Capítulo 3: La Búsqueda del Tesoro

### Enigma 3.1: Completa la tabla de transacciones

**Solución con BUSCARX:**
```excel
=BUSCARX(A2; $G$2:$G$6; $H$2:$H$6; "Código no encontrado")
```

**Solución con BUSCARV:**
```excel
=SI.ERROR(BUSCARV(A2; $G$2:$J$6; 2; FALSO); "Código no encontrado")
```

**Solución con ÍNDICE + COINCIDIR:**
```excel
=SI.ERROR(INDICE($H$2:$H$6; COINCIDIR(A2; $G$2:$G$6; 0)); "Código no encontrado")
```

**Creación de tabla maestra temporal:** Crea una tabla en otra hoja con códigos AX-1001, AX-1002, etc., y descripciones inventadas (como "Silla clásica", "Mesa comedor", etc.).

---

### Enigma 3.2: Manejo de errores

**Solución:**
```excel
=SI.ERROR(BUSCARV(A2; $G$2:$J$6; 2; FALSO); "Código no registrado")
```

**Alternativa con BUSCARX:**
```excel
=BUSCARX(A2; $G$2:$G$6; $H$2:$H$6; "Código no registrado")
```

---

### Enigma 3.3: Búsqueda bidireccional

**Solución:**
Crea la tabla de descuentos en un rango (ejemplo: A17:D20 con categorías en A18:A20 y rangos en B17:D17).

Para un cliente Premium con compra de 3000 soles:
```excel
=INDICE($B$18:$D$20; COINCIDIR("Premium"; $A$18:$A$20; 0); COINCIDIR(3000; $B$17:$D$17; 1))
```

**Explicación:**
- Primer COINCIDIR: busca "Premium" en la columna A → devuelve 2 (fila 2 del rango)
- Segundo COINCIDIR: busca 3000 en [0, 1000, 5000] con tipo 1 (aproximado) → devuelve 2 (porque 3000 está entre 1000 y 5000)
- INDICE devuelve el valor en fila 2, columna 2 del rango B18:D20 → 10%

**Resultado:** 10% de descuento.

---

## Capítulo 4: El Rompecabezas Financiero

### Enigma 4.1: Crea tu primera tabla dinámica

**Solución:**
1. Selecciona el rango de datos. **Insertar > Tabla dinámica > Nueva hoja.**
2. Arrastra "Código" a **Filas**.
3. Arrastra "Valor_A" a **Valores** (se mostrará como "Suma de Valor_A").
4. Arrastra "Valor_B" a **Valores** (segunda columna).
5. Para contar registros en lugar de sumar, arrastra "Valor_A" nuevamente a **Valores**, haz clic derecho > **Configuración de campo de valor** > **Contar**.

**Respuesta:** El tipo de código con el valor total más alto dependerá de tus datos. Generalmente, AX (ingresos) suele tener el valor más alto. El tipo con más registros suele ser AX también, o BX si hay más egresos que ingresos.

---

### Enigma 4.2: Análisis temporal

**Solución:**
1. Crea la tabla dinámica con "Fecha" en **Filas**.
2. Haz clic derecho sobre cualquier fecha > **Agrupar**.
3. Selecciona "Trimestres" y "Años".
4. Arrastra "Valor_A" a **Valores**.

**Respuesta:** Dependerá de los datos. Busca el trimestre con el valor más alto en la columna "Suma de Valor_A".

---

### Enigma 4.3: Los valores sospechosos

**Solución:**
1. Calcula el promedio general de Valor_A usando `=PROMEDIO(B2:B1001)` en una celda fuera de la tabla dinámica.
2. En la tabla dinámica agrupada por mes, haz clic en la flecha de "Etiquetas de fila" > **Filtros de valor > Mayor que**.
3. Ingresa el valor del promedio calculado.

**Respuesta:** El número de meses dependerá de tus datos. Generalmente, entre 15 y 25 meses de un total de 120 (10 años) suelen estar por encima del promedio.

---

## Capítulo 5: Revelaciones

### Enigma 5.1: Crea un gráfico combinado

**Solución:**
1. Selecciona la tabla dinámica o los datos resumidos por año (año, suma Valor_A, suma Valor_B).
2. **Insertar > Gráfico combinado > Columna agrupada - Línea en eje secundario.**
3. Configura: Valor_A como columna, Valor_B como línea con eje secundario.
4. Personaliza: título "Ingresos vs Egresos (2005-2015)", colores verde para ingresos, rojo para egresos.
5. Agrega línea de tendencia: clic derecho en columna de Valor_A > **Agregar línea de tendencia**.

---

### Enigma 5.2: Minigráficos de tendencia

**Solución:**
1. Crea una tabla resumen con años en filas y meses en columnas.
2. Selecciona la celda al lado del primer año.
3. **Insertar > Minigráfico > Línea.**
4. En "Rango de datos", selecciona los valores mensuales de ese año.
5. Arrastra hacia abajo para copiar a los demás años.
6. En **Diseño de minigráfico**, marca "Punto máximo" y cambia el color a rojo.

**Respuesta:** El año más volátil suele ser 2008 (crisis económica global). Verifica los minigráficos para confirmar cuál año muestra las fluctuaciones más extremas.

---

### Enigma 5.3: Dispersión reveladora

**Solución:**
1. Selecciona las columnas Valor_A y Valor_B.
2. **Insertar > Gráfico de dispersión > Solo con marcadores.**
3. Agrega línea de tendencia lineal: clic derecho > **Agregar línea de tendencia**.
4. Marca "Presentar ecuación en el gráfico" y "Presentar el valor R cuadrado".

**Respuesta:** El R² suele ser bajo (menor a 0.3), indicando que no hay una correlación fuerte entre ingresos y egresos. Esto sugiere que Valor_A y Valor_B miden aspectos independientes del negocio, no están directamente vinculados.

---

## Capítulo 6: El Código del Abuelo

### Enigma 6.1: Limpieza de datos

**Solución:**
1. Escribe "2008/03/15_BX_1002_890_12" en la celda A1.
2. **Datos > Texto en columnas.**
3. Paso 1: Delimitados.
4. Paso 2: Marca "Otro" y escribe "/". Haz clic en "Siguiente". Luego marca "Otro" de nuevo y escribe "_".
5. Paso 3: Para la primera columna, elige "Fecha" (formato Año Mes Día).

**Resultado:** 6 columnas. La fecha se reconoce automáticamente si el formato es compatible (2008/03/15 se reconoce como AAAA/MM/DD).

**Columnas obtenidas:**
1. Fecha (15/03/2008)
2. BX
3. 1002
4. 890
5. 12
6. (vacío o siguiente dato)

---

### Enigma 6.2: Detecta y analiza duplicados

**Solución:**
1. Inserta una columna auxiliar (ej: columna F) con la fórmula: `=A2&B2` (Código & Valor_A).
2. Copia la fórmula hacia abajo.
3. Selecciona la columna F. **Inicio > Formato condicional > Reglas para resaltar celdas > Valores duplicados.**
4. Los duplicados se resaltarán. Cuenta cuántos hay.

**Alternativa:** Usa **Datos > Quitar duplicados** seleccionando las columnas Código y Valor_A. Antes de aceptar, Excel te mostrará cuántos duplicados encontrará.

---

### Enigma 6.3: Validación de integridad

**Solución:**
1. Selecciona la columna Valor_A (B2:B1001).
2. **Datos > Validación de datos > Configuración.**
   - Permitir: Personalizada
   - Fórmula: `=RESIDUO(B2;10)=0`
3. Ve a **Mensaje de error** y escribe: "El valor debe ser múltiplo de 10".
4. Luego, **Datos > Validación de datos > Circular celdas con validación inválida** para identificar los valores que no cumplen.

**Respuesta:** El número de valores que NO son múltiplos de 10 dependerá de tus datos. Si el archivo original fue creado con valores limpios, probablemente todos sean múltiplos de 10 (dando 0 valores inválidos), lo que indicaría que el abuelo era meticuloso con sus registros.

---

## Capítulo 7: Nombres con Significado

### Enigma 7.1: Nombra las columnas del archivo secreto

**Solución:**
1. **Fórmulas > Administrador de nombres > Nuevo.**
2. Crear cada nombre:

| Nombre | Referencia |
|--------|------------|
| Codigos | =Hoja1!$A$2:$A$1001 |
| Ingresos | =Hoja1!$B$2:$B$1001 |
| Egresos | =Hoja1!$C$2:$C$1001 |
| Indicador | =Hoja1!$D$2:$D$1001 |
| Fechas | =Hoja1!$E$2:$E$1001 |

3. Fórmula de ganancia neta:
```excel
=SUMA(Ingresos) - SUMA(Egresos)
```

---

### Enigma 7.2: Crea un nombre para el rango dinámico

**Solución:**
1. **Fórmulas > Administrador de nombres > Nuevo.**
2. Nombre: `Productos`
3. Refiere a:
```excel
=DESREF(Hoja2!$A$2;0;0;CONTARA(Hoja2!$A:$A)-1;2)
```

**Explicación:** DESREF comienza en A2, se desplaza 0 filas y 0 columnas, y crea un rango de alto igual al número de celdas no vacías en columna A (menos 1 por el encabezado) y ancho 2 columnas (A y B).

---

### Enigma 7.3: Documenta tu archivo

**Solución:**
1. **Fórmulas > Administrador de nombres > Ctrl+F3.**
2. Selecciona cada nombre y haz clic en **Editar**.
3. En el campo **Comentario**, escribe una descripción:
   - `Ingresos`: "Valores de ingreso del archivo secreto de Don Rafael (2005-2015). Corresponden a la columna Valor_A."
   - `Egresos`: "Valores de egreso del archivo secreto. Corresponden a la columna Valor_B."
   - etc.

---

## Capítulo 8: ¿Qué Pasaría Si...?

### Enigma 8.1: Punto de equilibrio del taller

**Solución:**
Configura las celdas:
- B1: Precio = 300
- B2: CostoMaterial = 130
- B3: CostosFijos = 9500
- B4: Cantidad = 40 (valor inicial)
- B5: Ganancia = =(B1-B2)*B4-B3

**Buscar objetivo:**
1. **Datos > Análisis de hipótesis > Buscar objetivo.**
2. Definir celda: B5
3. Con valor: 0
4. Para cambiar: B4

**Resultado:** Aproximadamente 56 unidades al mes.

---

### Enigma 8.2: Tabla de datos de rentabilidad

**Solución:**
1. Crea una celda con la fórmula de ganancia (ej: B5).
2. En una fila (ej: A7:A11) escribe las cantidades: 30, 45, 60, 75, 90.
3. En una columna (ej: B6:F6) escribe los precios: 220, 250, 280, 310, 340.
4. En A6, escribe `=B5` (referencia a la fórmula de ganancia).
5. Selecciona A6:F11.
6. **Datos > Análisis de hipótesis > Tabla de datos.**
7. Celda de fila: la celda del precio (B1)
8. Celda de columna: la celda de la cantidad (B4)

**Respuesta:** La mayor ganancia en esta tabla será con el precio más alto (340) y la cantidad más alta (90): (340-130)*90 - 9500 = 18,900 - 9500 = 9,400 soles mensuales.

---

### Enigma 8.3: Escenarios del archivo secreto

**Solución:**
1. **Datos > Análisis de hipótesis > Administrador de escenarios.**
2. Agregar escenarios (sin necesidad de cambiar valores reales, solo definirlos):

**Escenario A:** Valor_A = ingresos totales, Valor_B = costos operativos
- Celdas cambiantes: no aplica (es interpretación)
- Para validar: calcula `=SUMA(Ingresos)*0.8` y compara con `=SUMA(Egresos)`

**Escenario B:** Valor_A = ventas, Valor_B = compras, Valor_C = margen
- Para validar: `=CORREL(Ingresos;Indicador)` debe ser alta

**Escenario C:** Tres cuentas bancarias
- Para validar: las sumas deben ser independientes

**Respuesta:** El Escenario B es el más plausible porque la correlación observada entre Valor_A y Valor_C (R²=0.89) sugiere que Valor_C es un derivado de Valor_A (como un margen o comisión), y Valor_B parece independiente.

---

## Capítulo 9: El Mapa del Tesoro

### Enigma 9.1: Crea tu primer dashboard

**Solución:**
1. Crea una nueva hoja llamada "Dashboard".
2. **Tarjetas KPI:** En celdas separadas, usa fórmulas con rangos con nombre:
   - Ingresos: `=SUMA(Ingresos)`
   - Egresos: `=SUMA(Egresos)`
   - Ganancia: `=SUMA(Ingresos)-SUMA(Egresos)`
3. **Gráfico combinado:** Con los datos resumidos por año (de tu tabla dinámica).
4. **Tabla dinámica:** Inserta una tabla dinámica pequeña al costado del gráfico.
5. **Segmentador:** **Análisis de tabla dinámica > Insertar segmentador > Año**.
6. Aplica formato: colores consistentes, elimina cuadrícula, ajusta tamaños.

---

### Enigma 9.2: Controles interactivos

**Solución:**
1. **Desarrollador > Insertar > Botón de giro (Control de formulario).**
2. Dibuja el control en el dashboard.
3. Clic derecho > **Formato de control**:
   - Vincular con: $Z$1
   - Mínimo: 2005
   - Máximo: 2015
   - Incremento: 1
4. Modifica las fórmulas de las tarjetas KPI:
```excel
=SUMAR.SI.CONJUNTO(Ingresos; Fechas; ">="&FECHA(Z1;1;1); Fechas; "<="&FECHA(Z1;12;31))
=SUMAR.SI.CONJUNTO(Egresos; Fechas; ">="&FECHA(Z1;1;1); Fechas; "<="&FECHA(Z1;12;31))
```

---

### Enigma 9.3: Dashboard protegido

**Solución:**
1. Selecciona las celdas que contienen los controles y segmentadores.
2. Clic derecho > **Formato de celdas > Protección** y desmarca "Bloqueada" (para que estos elementos sigan funcionando).
3. **Revisar > Proteger hoja.**
4. Contraseña: mendoza2026
5. En la lista de opciones, marca:
   - "Usar tablas dinámicas"
   - "Editar objetos"
   - "Usar Autofiltro"
6. Desmarca "Seleccionar celdas bloqueadas" (opcional).

---

## Capítulo 10: La Verdad Emmerge

### Enigma 10.1: Reconstruye el viaje de Sofía

**Solución:**
Este es un proyecto integrador. No hay una única solución correcta. Evalúa tu trabajo contra esta lista:

- [ ] Formato condicional aplicado a todas las columnas numéricas
- [ ] Validación de datos en al menos 2 columnas
- [ ] Comentarios explicativos en celdas clave
- [ ] BUSCARX (o BUSCARV) conectando dos tablas
- [ ] Tabla dinámica con agrupación por año/mes
- [ ] Gráfico combinado con eje secundario
- [ ] Minigráficos de tendencia por año
- [ ] Rangos con nombre para todas las columnas principales
- [ ] Análisis de hipótesis (Buscar objetivo o tabla de datos)
- [ ] Dashboard con KPI y segmentadores

---

### Enigma 10.2: El mensaje cifrado

**Solución:**
No hay una solución única. Ideas para tu mensaje cifrado:
- Usa los valores de Valor_C como dígitos de un código
- Oculta pistas en comentarios que solo se entienden después de aplicar formato condicional
- Crea una tabla maestra que solo se "revela" cuando se usan las funciones de búsqueda correctas
- El mensaje final podría ser: "EL LEGADO VIVE EN TI" o similar

---

### Enigma 10.3: Dashboard del taller

**Solución:**
Verifica que tu dashboard incluya:
- [ ] 4+ tarjetas KPI visibles en la parte superior
- [ ] Gráfico de tendencia mensual
- [ ] Los 5 productos más vendidos (con BUSCARX y tabla dinámica)
- [ ] Segmentadores de año, mes y categoría
- [ ] Botón de giro para cambiar de año
- [ ] Formato condicional en las tarjetas (verde/rojo)
- [ ] Hoja protegida con funcionalidad intacta
- [ ] Rango con nombre para todos los datos fuente

---

*"No hay enigma sin solución.*
*Solo datos esperando ser descifrados."*
