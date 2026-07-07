# Capítulo 3: Las Fórmulas del Abuelo

## Fórmulas Básicas: Suma, Resta, Multiplicación y División

---

Eran las 7:30 de la mañana y Sofía ya estaba frente a la computadora. Pero en lugar de abrir Excel, hojeaba el cuaderno de su abuelo. Había encontrado una sección que la intrigaba particularmente: "Costos y Precios".

Las páginas estaban llenas de números escritos a mano:

*"Silla de cedro:*
*- Madera: 45 soles (1 tabla)*
*- Barniz: 7 soles*
*- Tornillos: 3 soles*
*- Mano de obra: 35 soles*
*- Total: ?*
*- Precio de venta: 150 soles*
*- Ganancia: ?"*

En cada página, Don Rafael había dejado los cálculos a medio hacer. Como si hubiera querido que alguien más los completara.

Sofía sonrió. Su abuelo no solo había dejado el inventario: había dejado problemas para que ella los resolviera.

—Bueno, abuelo —dijo en voz alta—. Vamos a hacer estos cálculos juntos.

---

## Las fórmulas: el corazón de Excel

En Excel, una **fórmula** es una expresión que realiza cálculos con los valores de las celdas. Todo comienza con el signo **=** (igual). Sin ese signo, Excel trata lo que escribes como texto simple.

### Operadores básicos

| Operador | Operación | Ejemplo | Resultado |
|----------|-----------|---------|-----------|
| + | Suma | =5+3 | 8 |
| - | Resta | =10-4 | 6 |
| * | Multiplicación | =6*3 | 18 |
| / | División | =15/3 | 5 |

No tienes que usar números directamente. Puedes usar **referencias a celdas**. Esto es más poderoso, porque si cambias el valor de una celda, el resultado se actualiza automáticamente.

| A | B | C |
|---|---|---|
| 45 | 7 | =A1+B1 |
| 150 | =A1+B1 | =A2-B2 |

En la celda C1, la fórmula =A1+B1 suma los valores de A1 y A2. Si cambias A1 a 50, C1 se actualizará automáticamente a 57.

---

## Sofía calcula los costos

Sofía abrió el archivo "Inventario_Taller.xlsx" y agregó una nueva hoja. La llamó "Costos". En ella, comenzó a crear una tabla para calcular los costos de producción:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| **Producto** | **Madera** | **Barniz** | **Tornillos** | **Mano Obra** | **Costo Total** |
| Silla cedro | 45 | 7 | 3 | 35 | =B2+C2+D2+E2 |
| Mesa roble | 186 | 14 | 8 | 70 | =B3+C3+D3+E3 |
| Banquito pino | 22 | 5 | 2 | 20 | =B4+C4+D4+E4 |
| Estante triplay | 70 | 10 | 5 | 45 | =B5+C5+D5+E5 |

—¡Funciona! —exclamó Sofía cuando vio los resultados aparecer en la columna F.

Pero quería ir más allá. Quería calcular la ganancia por cada producto. Agregó dos columnas más:

| G | H |
|---|---|
| **Precio Venta** | **Ganancia** |
| 150 | =G2-F2 |
| 350 | =G3-F3 |
| 80 | =G4-F4 |
| 180 | =G5-F5 |

Los resultados aparecieron:

| F | G | H |
|---|---|---|
| **Costo Total** | **Precio Venta** | **Ganancia** |
| 90 | 150 | 60 |
| 278 | 350 | 72 |
| 49 | 80 | 31 |
| 130 | 180 | 50 |

Sofía recargó la silla, impresionada. Con solo cuatro fórmulas, había calculado los costos y ganancias de todos los productos.

—Esto es increíble —murmuró—. Mi abuelo hacía estos cálculos a mano, uno por uno.

Don Manuel se asomó por encima de su hombro.

—Tu abuelo siempre decía que los números son como la madera: hay que trabajarlos con cuidado para que den su mejor forma.

---

## Orden de las operaciones

Sofía intentó una fórmula más compleja. Quería calcular el porcentaje de ganancia sobre el costo:

=G2/F2-1

En Excel, el orden de las operaciones es el mismo que en matemáticas:

1. Paréntesis ( )
2. Exponentes ^
3. Multiplicación y División * y /
4. Suma y Resta + y -

Sofía escribió = (G2 - F2) / F2 para calcular la ganancia como porcentaje del costo:

| I |
|---|
| **% Ganancia** |
| =(G2-F2)/F2 |
| =(G3-F3)/F3 |
| =(G4-F4)/F4 |
| =(G5-F5)/F5 |

El resultado mostró:

| I |
|---|
| **% Ganancia** |
| 0.6667 |
| 0.2590 |
| 0.6327 |
| 0.3846 |

Sofía frunció el ceño. Los números decimales no eran muy claros.

—Muy pronto aprenderé a darle formato —se prometió—. Por ahora, al menos los cálculos están bien.

---

## El secreto en el cuaderno

Esa noche, Sofía revisó el cuaderno de su abuelo con más atención. En una página que había pasado por alto, encontró una serie de anotaciones crípticas:

*"F1 = B1*C1 (costo de madera por cantidad)*
*"Total = SUMA de todas las F"*
*"Ganancia Neta = Total de Ventas - Total de Costos"*

Pero lo que más le llamó la atención fue una nota al margen:

*"No olvides el IVA (18%). Precio sin IVA * 1.18 = Precio final."*

—IVA —pensó Sofía—. Mi abuelo calculaba el IVA en sus precios.

Agregó una nueva columna para el precio con IVA:

| J |
|---|
| **Precio + IVA** |
| =G2*1.18 |
| =G3*1.18 |
| =G4*1.18 |
| =G5*1.18 |

—Perfecto —dijo Sofía—. Ahora todos los precios incluyen el 18% de IVA.

---

## Errores comunes al empezar

Mientras trabajaba, Sofía cometió algunos errores que la ayudaron a aprender:

### #¡DIV/0!
Intentó dividir un número entre una celda vacía:
=A1/B1 (si B1 está vacía, Excel muestra #¡DIV/0!)

### #¿NOMBRE?
Escribió mal el nombre de una función:
=SUMA(A1:A5) en lugar de =SUMA(A1:A5) — pero en inglés es =SUM(A1:A5), en español =SUMA(A1:A5)

### #¡VALOR!
Intentó sumar texto como si fuera número:
="Texto" + 5

### Referencia circular
Creó una fórmula que se refería a sí misma:
=A1+1 (escrito en la celda A1)

---

## Enigmas del Capítulo 3

### Enigma 3.1: Calcula el costo de producción

Usando los datos del inventario del Capítulo 1, crea una hoja de costos para los siguientes productos que Don Rafael tenía pendientes:

| Producto | Madera | Barniz | Tornillos | Mano de Obra | Precio Venta |
|----------|--------|--------|-----------|-------------|-------------|
| Silla de roble | 62 | 8 | 4 | 40 | 200 |
| Mesa de cedro | 135 | 12 | 6 | 60 | 350 |
| Banquito de pino | 22 | 4 | 2 | 18 | 75 |
| Estante de triplay | 70 | 8 | 5 | 40 | 160 |

Calcula:
1. Costo Total (suma de Madera, Barniz, Tornillos y Mano de Obra)
2. Ganancia (Precio Venta - Costo Total)
3. Porcentaje de ganancia ((Precio Venta - Costo Total) / Costo Total)

### Enigma 3.2: Precios con descuento

Don Rafael ofrecía 10% de descuento a clientes frecuentes. Agrega una columna "Descuento 10%" que calcule el precio con IVA menos el 10%. La fórmula sería: =Precio_con_IVA * 0.90

Usa los precios con IVA que calculaste (multiplica precio de venta por 1.18 y luego por 0.90).

### Enigma 3.3: El pedido del cliente

Un cliente quiere 5 sillas de cedro. Si cada silla cuesta S/ 90 producirla:

- ¿Cuánto cuesta producir las 5 sillas? (=90*5)
- ¿Cuánto se gana si cada silla se vende a S/ 150? (=(150-90)*5)
- ¿Cuál es el precio total con IVA para las 5 sillas? (=150*5*1.18)

Escribe las fórmulas que usarías en Excel para resolver cada pregunta.

### Enigma 3.4: Corrige los errores

Identifica qué está mal en cada una de estas fórmulas y escríbelas correctamente:

1. `=A1+B1*` (sobra un operador)
2. `suma(A1:A10)` (falta el signo =)
3. `=A1/0` (división entre cero)
4. `=B2 + C2` (tiene espacios, ¿funciona?)

Pista: en Excel, los espacios en las fórmulas generalmente no causan error, pero el resto sí.

---

## Lo que aprendiste

- Toda **fórmula** en Excel comienza con **=**
- Los **operadores básicos** son: + (suma), - (resta), * (multiplicación), / (división)
- Puedes usar **referencias a celdas** en lugar de números fijos
- El **orden de las operaciones** es: paréntesis, exponentes, multiplicación/división, suma/resta
- Los **errores comunes** incluyen #¡DIV/0!, #¿NOMBRE?, #¡VALOR!
- Puedes combinar operaciones para crear cálculos complejos

---

Sofía cerró el cuaderno de su abuelo y suspiró. Había aprendido más en una tarde que en todo un semestre de matemáticas en la universidad.

—Abuelo —dijo en voz baja—, tus fórmulas son como tus muebles: simples por fuera, pero con una estructura sólida por dentro.

Apagó la computadora. Mañana continuaría. Pero esa noche, por primera vez desde que heredó el taller, sintió que las cosas podían salir bien.

Tenía las herramientas. Tenía los datos. Y ahora, empezaba a tener las fórmulas.
