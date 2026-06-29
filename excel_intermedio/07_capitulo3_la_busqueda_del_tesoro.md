# Capítulo 3: La Búsqueda del Tesoro

## Tema: BUSCARV, BUSCARX, ÍNDICE y COINCIDIR

---

—He estado mirando los códigos del archivo secreto —dijo Sofía, que había llegado temprano al taller para trabajar en el misterio antes de que comenzara el bullicio del día—. Mira esto.

En la pantalla, señaló la columna Código:

| Código |
|--------|
| AX-1001 |
| BX-1002 |
| CX-1003 |
| DX-1004 |
| AX-1005 |

—Las primeras dos letras parecen ser categorías: AX, BX, CX, DX. Y el número parece un correlativo.

—Buena observación —dijo Carlos, sirviéndose un café—. Pero el verdadero tesoro no está en los códigos, sino en lo que representan.

—¿Qué quieres decir?

—Ayer mencionaste que esto parece un libro de transacciones. Pero no hay nombres de productos, ni clientes, ni ninguna descripción. Solo códigos y números. ¿Por qué?

—Porque... los códigos se refieren a otra tabla —dijo Sofía, la idea tomando forma en su mente.

—Exacto. Tu abuelo usaba los códigos como referencia a una **tabla maestra** que contiene la información real. Para descifrar este archivo, necesitamos conectar las dos tablas.

—¿Y cómo hacemos eso?

—Con **funciones de búsqueda y referencia**. Son las herramientas más poderosas de Excel para trabajar con múltiples tablas.

---

## BUSCARV: La búsqueda vertical

—BUSCARV significa "Búsqueda Vertical" —explicó Carlos—. Busca un valor en la primera columna de una tabla y devuelve un valor de la misma fila en otra columna.

—Suena complicado.

—Es más fácil de lo que parece. Mira, voy a crear una tabla maestra hipotética. En una hoja nueva, escribe esto:

| Código | Producto | Categoría | Precio Unitario |
|--------|----------|-----------|-----------------|
| AX-1001 | Silla clásica | Silllería | 250 |
| AX-1005 | Silla ejecutiva | Silllería | 450 |
| BX-1002 | Mesa comedor 6p | Mesas | 1200 |
| CX-1003 | Ropero 3 puertas | Dormitorio | 1800 |
| DX-1004 | Estante biblioteca | Oficina | 900 |

—Ahora, en la hoja del archivo secreto, vamos a buscar el nombre del producto para cada código.

La sintaxis de BUSCARV es:

```
=BUSCARV(valor_buscado; tabla; número_columna; [ordenado])
```

- **valor_buscado:** el código que queremos buscar (ej: AX-1001)
- **tabla:** el rango de la tabla maestra (ej: $G$2:$J$6)
- **número_columna:** la columna de la tabla maestra de la que queremos el valor (1=código, 2=producto, 3=categoría, 4=precio)
- **ordenado:** FALSO para búsqueda exacta, VERDADERO para aproximada

—El cuarto parámetro es crítico —enfatizó Carlos—. Si quieres una coincidencia exacta (como buscar un código específico), usa **FALSO**. Si usas VERDADERO o lo omites, Excel asumirá que la tabla está ordenada y hará una búsqueda aproximada, lo que puede dar resultados incorrectos.

Sofía escribió en la celda F2 (junto al primer código):

```
=BUSCARV(A2; $G$2:$J$6; 2; FALSO)
```

El resultado fue "Silla clásica".

—¡Funcionó! —exclamó.

—Ahora arrastra la fórmula hacia abajo para aplicarla a todos los códigos.

Pero al arrastrarla, algunos códigos devolvieron `#N/A`.

—¿Por qué algunos no funcionan? —preguntó Sofía.

—Porque esos códigos no están en la tabla maestra que creamos. O los escribiste mal, o la tabla maestra no está completa. En el mundo real, esto pasa todo el tiempo: los datos no siempre coinciden perfectamente.

—¿Qué hacemos con los `#N/A`?

—Podemos usar **SI.ERROR** para manejarlos:

```
=SI.ERROR(BUSCARV(A2; $G$2:$J$6; 2; FALSO); "No encontrado")
```

—Así, en lugar de un error, muestra un mensaje amigable.

---

## Las limitaciones de BUSCARV

—BUSCARV es útil, pero tiene limitaciones importantes —dijo Carlos—:

1. **Solo busca en la primera columna:** El valor buscado debe estar en la primera columna de la tabla
2. **Solo busca hacia la derecha:** La columna a devolver debe estar a la derecha de la columna buscada
3. **No funciona bien si insertas o eliminas columnas:** Porque el número de columna es fijo
4. **Solo devuelve la primera coincidencia:** Si hay códigos duplicados, solo devuelve el primero

—¿Hay alternativas? —preguntó Sofía.

—Sí. Dos muy poderosas: **BUSCARX** (la evolución moderna) y la combinación **ÍNDICE + COINCIDIR**.

---

## BUSCARX: La evolución

—BUSCARX llegó con Excel 365 y Excel 2021. Es más flexible y fácil de usar.

La sintaxis es:

```
=BUSCARX(valor_buscado; rango_busqueda; rango_devolución; [si_no_encontrado]; [modo_coincidencia]; [modo_búsqueda])
```

—Lo más importante: ya no usas un número de columna, sino el **rango de devolución** directamente. Y puedes buscar en cualquier dirección.

Sofía escribió la misma búsqueda con BUSCARX:

```
=BUSCARX(A2; $G$2:$G$6; $H$2:$H$6; "No encontrado")
```

—Es más intuitiva —dijo Sofía—. Veo exactamente qué columnas estoy usando.

—Exacto. Y el parámetro "si_no_encontrado" reemplaza a SI.ERROR.

—¿Qué más tiene BUSCARX?

—Opciones adicionales:

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| modo_coincidencia | 0 | Coincidencia exacta (por defecto) |
| modo_coincidencia | -1 | Exacta o menor siguiente |
| modo_coincidencia | 1 | Exacta o mayor siguiente |
| modo_coincidencia | 2 | Coincidencia con comodines |
| modo_búsqueda | 1 | Buscar de primero a último (por defecto) |
| modo_búsqueda | -1 | Buscar de último a primero |
| modo_búsqueda | 2 | Búsqueda binaria (datos ordenados ascendente) |
| modo_búsqueda | -2 | Búsqueda binaria (datos ordenados descendente) |

—La búsqueda de último a primero es útil para encontrar la última venta de un producto, por ejemplo.

---

## ÍNDICE + COINCIDIR: La combinación clásica

—Antes de que existiera BUSCARX, los profesionales usaban la combinación de **ÍNDICE** y **COINCIDIR** para hacer búsquedas más flexibles que BUSCARV.

**COINCIDIR** encuentra la posición de un valor en un rango:

```
=COINCIDIR(valor_buscado; rango; [tipo_coincidencia])
```

Devuelve un número: la posición del valor en el rango.

**ÍNDICE** devuelve el valor en una posición específica de un rango:

```
=INDICE(rango; número_fila; [número_columna])
```

—La combinación funciona así: COINCIDIR encuentra la fila, ÍNDICE devuelve el valor:

```
=INDICE(rango_devolución; COINCIDIR(valor_buscado; rango_búsqueda; 0))
```

Sofía lo probó:

```
=INDICE($H$2:$H$6; COINCIDIR(A2; $G$2:$G$6; 0))
```

—Funciona igual que BUSCARV —dijo—. ¿Por qué es mejor?

—Porque puedes devolver valores de **cualquier columna**, incluso a la izquierda del valor buscado. Y puedes buscar en una columna y devolver de otra completamente diferente.

—Dame un ejemplo donde BUSCARV no pueda hacerlo.

—Supón que buscas un producto por su nombre y quieres saber el código. Con BUSCARV no puedes (porque el código está a la izquierda). Con ÍNDICE+COINCIDIR sí:

```
=INDICE($G$2:$G$6; COINCIDIR("Mesa comedor 6p"; $H$2:$H$6; 0))
```

—Eso busca "Mesa comedor 6p" en la columna H y devuelve el código de la columna G.

---

## Aplicación al archivo secreto

—Ahora, volvamos al archivo de tu abuelo —dijo Carlos—. Creé dos tablas adicionales basadas en lo que encontramos en los comentarios. Son hipotéticas, pero nos ayudarán a probar.

Carlos abrió una segunda hoja en el archivo:

**Hoja2: "Maestra_Productos"**

| Codigo_Real | Descripción | Tipo | Costo_Unitario |
|-------------|-------------|------|----------------|
| P-001 | Madera Caoba 1''x4m | Insumo | 45 |
| P-002 | Barniz Marino Galón | Insumo | 28 |
| P-003 | Silla Colonial Unidad | Producto | 180 |
| P-004 | Mesa Roble 8p Unidad | Producto | 350 |
| P-005 | Tornillos 2'' Caja 100 | Insumo | 12 |

—Pero los códigos en el archivo son AX-1001, no P-001... —objetó Sofía.

—Por eso necesitamos descifrar la relación. Tal vez las primeras letras (AX, BX, CX) indican el tipo de transacción, y los números son el ID del producto.

—Entonces necesitaríamos una búsqueda que tome el número después del guión...

—O usar funciones de texto para extraerlo. Pero eso es para más adelante. Por ahora, practica con las funciones de búsqueda.

---

## Búsqueda bidireccional

—Hay un caso aún más interesante —dijo Carlos—. ¿Qué pasa si necesitas buscar un valor en una tabla de doble entrada?

Creó una tabla de precios por producto y volumen:

| Producto | 1-10 uds | 11-50 uds | 51+ uds |
|----------|----------|-----------|---------|
| Silla | 250 | 220 | 180 |
| Mesa | 1200 | 1100 | 950 |
| Ropero | 1800 | 1650 | 1500 |
| Estante | 900 | 820 | 750 |

—Para buscar un precio, necesitas el producto **y** la cantidad. Eso es una **búsqueda bidireccional**. Se hace con ÍNDICE + COINCIDIR + COINCIDIR:

```
=INDICE(tabla_precios; COINCIDIR(producto; productos; 0); COINCIDIR(cantidad; rangos_cantidad; 1))
```

—El primer COINCIDIR encuentra la fila, el segundo encuentra la columna.

Sofía lo probó:

```
=INDICE($B$15:$D$18; COINCIDIR("Mesa"; $A$15:$A$18; 0); COINCIDIR(30; $B$14:$D$14; 1))
```

Resultado: 1100 (el precio de mesa para 30 unidades, que cae en el rango 11-50).

—Es como un juego de coordenadas —dijo Sofía fascinada—. Como encontrar un punto en un mapa.

—Exacto. Las hojas de cálculo son mapas, y las funciones de búsqueda son tu brújula.

---

### Enigma 3.1: Completa la tabla de transacciones

Usando el archivo secreto y la tabla maestra que creó Carlos (Hoja2), agrega una columna "Descripción" usando BUSCARX que busque el código y devuelva la descripción del producto.

**Nota:** Como los códigos no coinciden exactamente, crea una tabla maestra temporal que use los códigos AX-1001, etc., con descripciones inventadas. Practica con BUSCARV, BUSCARX e ÍNDICE+COINCIDIR.

---

### Enigma 3.2: Manejo de errores

Modifica tu fórmula de BUSCARV para que, cuando no encuentre un código, muestre "Código no registrado" en lugar de `#N/A`. Usa SI.ERROR.

---

### Enigma 3.3: Búsqueda bidireccional

Crea una tabla de descuentos por categoría de cliente y monto de compra:

| Categoría | < 1000 | 1000-5000 | > 5000 |
|-----------|--------|-----------|--------|
| Regular | 0% | 5% | 10% |
| Premium | 5% | 10% | 15% |
| VIP | 10% | 15% | 20% |

Usa ÍNDICE + COINCIDIR + COINCIDIR para encontrar el descuento de un cliente Premium que compra 3000 soles.

---

## Lo que aprendiste

- **BUSCARV** busca un valor en la primera columna de una tabla y devuelve un valor de la misma fila en otra columna (solo hacia la derecha)
- **BUSCARX** es más moderna y flexible: permite buscar en cualquier dirección, tiene manejo de errores incorporado y más opciones de coincidencia
- **ÍNDICE + COINCIDIR** es la combinación más poderosa y versátil para búsquedas complejas
- Las **búsquedas bidireccionales** (doble COINCIDIR) permiten buscar en tablas de doble entrada
- **SI.ERROR** y **SI.NOD** permiten manejar errores de búsqueda elegantemente

---

—Ya tengo una idea de lo que podría ser este archivo —dijo Sofía, mirando los resultados de las búsquedas—. Creo que los códigos AX, BX, CX no son productos, sino **tipos de movimientos**: A=Ingreso, B=Egreso, C=Transferencia, D=Ajuste.

—¿Y los números?

—Podrían ser números de factura o de lote. Si logro cruzar esto con las fechas, tal vez pueda encontrar un patrón de movimientos sospechosos.

—Eso que dices se llama **tabla dinámica** —dijo Carlos sonriendo—. Y es justo lo que vamos a aprender mañana.

—¿Hay algo que Excel no pueda hacer?

—Sí —rió Carlos—. No puede hacer café. Eso todavía lo tenemos que hacer nosotros.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
