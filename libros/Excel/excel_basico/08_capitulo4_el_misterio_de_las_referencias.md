# Capítulo 4: El Misterio de las Referencias

## Referencias Relativas y Absolutas

---

Tres días después de comenzar su aventura con Excel, Sofía enfrentó su primer gran desafío. Había creado una hoja de precios para todos los productos del taller, pero al copiar las fórmulas, algo extraño ocurría.

—No entiendo —murmuró, mirando la pantalla—. La primera fórmula funciona, pero cuando la copio, los resultados cambian.

Don Manuel, que estaba lijando una tabla a unos metros, alzó la vista.

—¿Problemas con los números, mija?

—Es como si Excel cambiara las fórmulas solito —respondió Sofía, frustrada—. Mire:

| A | B | C | D |
|---|---|---|---|
| **Producto** | **Precio** | **IVA (18%)** | **Precio Final** |
| Silla cedro | 150 | =B2*0.18 | =B2+C2 |
| Mesa roble | 350 | =B3*0.18 | =B3+C3 |
| Banquito pino | 80 | =B4*0.18 | =B4+C4 |
| Estante triplay | 180 | =B5*0.18 | =B5+C5 |

—Eso funciona bien —dijo Don Manuel—. ¿Cuál es el problema?

—El problema es que para poner la fórmula en cada fila, tuve que escribirla cuatro veces. Una por cada producto. Si tengo cien productos, tendría que escribirla cien veces.

Sofía había intentado copiar la fórmula de C2 a C3, pero al hacerlo, notó que la fórmula se ajustaba automáticamente. Eso era bueno... hasta que necesitó usar un valor fijo.

—Verá —explicó Sofía—, ahora quiero calcular el precio en dólares. El tipo de cambio está en la celda E1. Pero cuando copio la fórmula, la referencia a E1 también cambia.

| E |
|---|
| **Tipo de Cambio** |
| 3.75 |

Quería hacer =B2*E1, pero al copiar a la fila 3, se convertía en =B3*E2 (y E2 está vacío).

—Eso —dijo una voz desde la entrada— es el misterio de las referencias.

Ambos se giraron. Un hombre de unos sesenta años, con lentes de lectura y una camisa a cuadros, estaba en la puerta del taller.

—Don Manuel, ¿quién es? —preguntó Sofía.

—Es el contador. Don Ricardo —respondió Don Manuel—. Trabajó con tu abuelo durante veinte años.

—Tu abuelo me pidió que te ayudara si algún día venías —dijo Don Ricardo, entrando—. Y tengo algo que enseñarte que te ahorrará horas de trabajo.

---

## Referencias relativas vs. absolutas

Don Ricardo se sentó frente a la computadora y explicó:

—En Excel, cuando copias una fórmula, las referencias a celdas se ajustan automáticamente. Eso se llama **referencia relativa**. Es útil cuando quieres que la fórmula se adapte a cada fila o columna.

—Pero a veces —continuó— necesitas que una referencia **no cambie**. Que apunte siempre a la misma celda, sin importar dónde copies la fórmula. Eso se llama **referencia absoluta**.

Para hacer una referencia absoluta, usas el símbolo **$** antes de la letra de la columna y del número de la fila:

- **$A$1** — Referencia absoluta (no cambia ni columna ni fila)
- **$A1** — Fila relativa, columna absoluta
- **A$1** — Columna relativa, fila absoluta
- **A1** — Referencia relativa (cambia todo)

| Tipo | Ejemplo | Al copiar hacia abajo | Al copiar hacia la derecha |
|------|---------|----------------------|---------------------------|
| Relativa | A1 | A2, A3, A4... | B1, C1, D1... |
| Absoluta | $A$1 | $A$1, $A$1... | $A$1, $A$1... |
| Mixta (fila) | A$1 | A$1, A$1... | B$1, C$1... |
| Mixta (columna) | $A1 | $A2, $A3... | $A1, $A1... |

---

## El truco del tipo de cambio

Don Ricardo volvió al problema de Sofía.

—Quieres multiplicar el precio en soles (columna B) por el tipo de cambio (E1) para obtener el precio en dólares. El problema es que al copiar la fórmula, la referencia a E1 se desplaza. La solución es usar **$E$1**:

| F |
|---|
| **Precio USD** |
| =B2*$E$1 |
| =B3*$E$1 |
| =B4*$E$1 |

—Ahora —dijo Don Ricardo—, copia la fórmula de F2 hacia abajo.

Sofía lo hizo. La fórmula en F3 decía =B3*$E$1. La referencia a B cambió (relativa), pero $E$1 permaneció fijo (absoluto).

—¡Funciona! —exclamó Sofía—. Ahora puedo copiar la fórmula a cien filas y todas usan el mismo tipo de cambio.

### Aplicando el IVA con referencia absoluta

Sofía recordó el problema del IVA. En lugar de escribir 0.18 en cada fórmula, podía poner el valor del IVA en una celda y usar referencia absoluta:

| A | B | C | D |
|---|---|---|---|
| **Producto** | **Precio** | **IVA** | **Precio Final** |
| Silla cedro | 150 | =B2*$G$1 | =B2+C2 |
| Mesa roble | 350 | =B3*$G$1 | =B3+C3 |

**G1:** 0.18 (tasa de IVA)

—Ahora, si el gobierno cambia el IVA —dijo Don Ricardo—, solo tienes que cambiar la celda G1 y todas las fórmulas se actualizarán automáticamente.

Sofía miró la hoja con admiración. Era como magia.

---

## Referencias mixtas en acción

Don Ricardo mostró un ejemplo más avanzado. Una tabla de multiplicar donde las referencias mixtas son perfectas:

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | | 1 | 2 | 3 | 4 |
| 2 | 1 | =$A2*B$1 | | | |
| 3 | 2 | | | | |
| 4 | 3 | | | | |

La fórmula en B2 es =$A2*B$1.

- **$A2:** La columna A es absoluta (siempre columna A), pero la fila es relativa.
- **B$1:** La columna B es relativa, pero la fila 1 es absoluta.

Al copiar B2 al resto de la tabla, cada celda muestra el producto de su fila y su columna. Las referencias mixtas permiten que la fórmula se adapte correctamente en ambas direcciones.

---

## El cuaderno del abuelo revela más secretos

Esa noche, Sofía revisó el cuaderno de Don Rafael con nuevos ojos. Encontró una página que decía:

*"Fórmulas clave del taller:*
*- Precio final = Precio + (Precio * IVA)*
*- IVA está en celda B1 (siempre la misma)*
*- Ganancia = Precio Venta - (Costo Material + Costo MO)*
*- % Ganancia = Ganancia / (Costo Material + Costo MO)*
- *Dólares: precio en $B$2*$E$1 (tipo de cambio en E1)*"

Don Rafael había descubierto por su cuenta el poder de las referencias absolutas. Lo llamaba "el ancla", porque mantenía la fórmula fija en un punto.

*"Las referencias absolutas son como los clavos en la madera —decía su cuaderno—. Mantienen todo en su lugar mientras trabajas."*

Sofía sonrió. Su abuelo, sin saberlo, había entendido uno de los conceptos más importantes de Excel.

---

## Enigmas del Capítulo 4

### Enigma 4.1: Tabla de precios con múltiples descuentos

Don Rafael ofrecía descuentos según el volumen de compra:

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | | **Sin descuento** | **5% desc.** | **10% desc.** | **15% desc.** |
| 2 | Silla cedro | 150 | | | |
| 3 | Mesa roble | 350 | | | |
| 4 | Banquito | 80 | | | |
| 5 | Estante | 180 | | | |

La tasa de descuento está en la fila 1: C1=5%, D1=10%, E1=15%.
La fórmula para el precio con descuento sería: =B2*(1-C$1)

¿Por qué se usa C$1 (fila absoluta, columna relativa)? Explica con tus palabras.

Completa la tabla con las fórmulas correctas (pista: usa referencia mixta).

### Enigma 4.2: Cálculo de comisiones

En el taller, los vendedores ganan una comisión del 8% sobre las ventas. La tasa de comisión está en la celda H1.

| Producto | Vendedor 1 | Vendedor 2 | Vendedor 3 | Comisión |
|----------|-----------|-----------|-----------|----------|
| Silla | 150 | 200 | 180 | =? |
| Mesa | 350 | 310 | 400 | =? |
| Banquito | 80 | 90 | 75 | =? |

La comisión se calcula como el total de ventas por la tasa (8%).
Escribe la fórmula para calcular la comisión del primer producto (fila 2) usando $H$1.

### Enigma 4.3: El error de Sofía

Sofía copió la fórmula =A1+B1 de la celda C1 a la celda C10. ¿Qué fórmula aparecerá en C10? ¿Y si la fórmula fuera =$A$1+$B$1?

### Enigma 4.4: Tabla de IVA por país

El taller vende a tres países con diferentes tasas de IVA:

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Producto** | **Precio** | **Perú (18%)** | **Colombia (19%)** |
| 2 | Silla | 150 | =$B2*C$1 | =$B2*D$1 |
| 3 | Mesa | 350 | | |
| 4 | Banquito | 80 | | |

Explica por qué la fórmula =$B2*C$1 funciona correctamente cuando la copias al resto de la tabla.

---

## Lo que aprendiste

- Las **referencias relativas** (A1) cambian cuando copias la fórmula
- Las **referencias absolutas** ($A$1) no cambian nunca
- Las **referencias mixtas** ($A1 o A$1) fijan solo una parte
- El símbolo **$** es el "ancla" que mantiene fija una referencia
- Las referencias absolutas son ideales para valores constantes (IVA, tipo de cambio, tasas)
- Usar una celda para el valor constante te permite actualizarlo fácilmente

---

Don Ricardo se despidió, pero antes de irse, le dio un consejo a Sofía:

—Tu abuelo decía que las referencias absolutas son como los puntos de apoyo en una palanca: te permiten mover el mundo desde un punto fijo.

Sofía asintió. Miró la pantalla donde la tabla de precios en dólares brillaba con todos los cálculos correctos. Había entendido el misterio de las referencias.

Pero sabía que era solo el comienzo. El cuaderno de su abuelo tenía muchas más páginas, y cada una guardaba un nuevo secreto por descubrir.
