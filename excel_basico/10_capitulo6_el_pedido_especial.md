# Capítulo 6: El Pedido Especial

## Funciones Básicas: SUM, AVERAGE, COUNT, MAX, MIN

---

El teléfono del taller sonó un martes por la mañana. Don Manuel lo contestó, y su expresión cambió de concentración a sorpresa, y de sorpresa a alegría.

—Sofía —dijo, tapando el auricular—, es el Hotel Miraflores. Quieren hacer un pedido grande.

Sofía dejó el café y tomó el teléfono.

—¿Aló? —dijo, tratando de sonar profesional.

—Señorita Mendoza —dijo una voz femenina al otro lado—, soy Carolina Ramírez, gerente de operaciones del Hotel Miraflores. Necesitamos renovar el mobiliario de diez habitaciones y dos suites. ¿Podría darnos un presupuesto?

—Por supuesto —respondió Sofía, mientras su corazón latía rápido—. ¿Qué tipo de muebles necesita?

—Para cada habitación: una cama queen, dos mesas de noche, un escritorio y una silla. Para las suites: una cama king, dos mesas de noche, un escritorio, un sillón y un ropero.

Sofía anotó todo, tratando de mantener la calma.

—¿Qué plazo tienen?

—Idealmente, tres semanas. Necesito el presupuesto antes del viernes.

Sofía colgó y miró a Don Manuel con los ojos brillantes.

—Don Manuel, esto es enorme. Necesito calcular cuánta madera vamos a necesitar, cuánto va a costar, cuánto vamos a ganar... ¡es un montón de cálculos!

—Entonces —dijo Don Manuel—, mejor que le preguntes a ese programa que tanto te gusta.

Sofía encendió la computadora. Era hora de usar las funciones de Excel.

---

## Las funciones: herramientas especializadas

Las **funciones** en Excel son fórmulas predefinidas que realizan cálculos específicos. Son como las herramientas especializadas en un taller: para cada tarea hay una herramienta adecuada.

### SUM (SUMA)

La función más básica y útil. Suma todos los valores de un rango.

Sintaxis: `=SUM(rango)` o en español `=SUMA(rango)`

Sofía creó una hoja nueva llamada "Pedido Hotel" y empezó a organizar:

| A | B | C | D | E |
|---|---|---|---|---|
| **Producto** | **Cant. x Hab.** | **Total (10 hab.)** | **Precio Unit.** | **Total x Producto** |
| Cama queen | 1 | 10 | 450 | =D2*C2 |
| Mesa de noche | 2 | 20 | 120 | =D3*C3 |
| Escritorio | 1 | 10 | 280 | =D4*C4 |
| Silla de escritorio | 1 | 10 | 150 | =D5*C5 |

Para calcular el costo total de todas las habitaciones, Sofía necesitaba sumar la columna E:

=SUM(E2:E5)

El resultado: S/ 11,000.00

Luego agregó los muebles de las suites:

| A | B | C | D | E |
|---|---|---|---|---|
| **Producto** | **Cant. x Suite** | **Total (2 suites)** | **Precio Unit.** | **Total x Producto** |
| Cama king | 1 | 2 | 680 | 1360 |
| Mesa de noche | 2 | 4 | 120 | 480 |
| Escritorio | 1 | 2 | 280 | 560 |
| Sillón | 1 | 2 | 520 | 1040 |
| Ropero | 1 | 2 | 890 | 1780 |

Suma de suites: =SUM(E8:E12) = S/ 5,220.00

Total del pedido: =SUM(E2:E5) + SUM(E8:E12) = S/ 16,220.00

—Esto es solo el costo de producción —murmuró Sofía—. Necesito calcular el precio de venta.

---

### AVERAGE (PROMEDIO)

Calcula el promedio (media aritmética) de un rango.

Sintaxis: `=AVERAGE(rango)` o en español `=PROMEDIO(rango)`

Don Rafael había registrado los precios de venta de sus productos en los últimos meses. Sofía encontró una hoja llamada "Ventas_Históricas":

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| **Mes** | **Ene** | **Feb** | **Mar** | **Abr** | **May** | **Jun** |
| Silla | 1200 | 1350 | 1100 | 1400 | 1300 | 1450 |
| Mesa | 800 | 750 | 900 | 850 | 780 | 920 |
| Estante | 450 | 500 | 480 | 520 | 490 | 510 |
| Ropero | 600 | 580 | 620 | 640 | 590 | 610 |

Sofía quería saber cuánto vendía en promedio cada producto:

=Silla: =AVERAGE(B2:G2) → 1300
Mesa: =AVERAGE(B3:G3) → 833.33
Estante: =AVERAGE(B4:G4) → 491.67
Ropero: =AVERAGE(B5:G5) → 606.67

—Interesante —dijo Sofía—. Las sillas son lo que más se vende, con un promedio de 1300 soles al mes.

---

### COUNT (CONTAR)

Cuenta cuántas celdas en un rango contienen números.

Sintaxis: `=COUNT(rango)` o en español `=CONTAR(rango)`

Sofía quería saber cuántos meses tenía registrados en su hoja de ventas:

=COUNT(B1:G1) → 6 meses

También usó **COUNTA** (CONTARA) para contar celdas no vacías (incluye texto):

=COUNTA(A2:A5) → 4 productos

Y **COUNTBLANK** (CONTAR.BLANCO) para contar celdas vacías:

=COUNTBLANK(B2:G5) → 0 (todas las celdas tienen datos)

---

### MAX y MIN

Encuentran el valor máximo y mínimo de un rango.

Sintaxis: `=MAX(rango)` y `=MIN(rango)`

Sofía quería saber cuál era la madera más cara y la más barata en el inventario:

=MAX(D2:D7) → 62.00 (Roble)
=MIN(D2:D7) → 22.00 (Pino)

También verificó las ventas máximas y mínimas de sillas:

=MAX(B2:G2) → 1450 (Junio)
=MIN(B2:G2) → 1100 (Marzo)

—Marzo fue un mes bajo para las sillas —notó Sofía—. Y junio fue el mejor mes.

---

## Combinando funciones

Sofía combinó funciones para obtener información más rica:

**¿Cuál es el producto más vendido en total?**

=MAX(SUM(B2:G2), SUM(B3:G3), SUM(B4:G4), SUM(B5:G5))

Pero esto era complicado. Encontró una mejor manera: una tabla de totales.

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Mes** | **Ene** | **Feb** | **Mar** | **Abr** | **May** | **Jun** | **Total** |
| Silla | 1200 | 1350 | 1100 | 1400 | 1300 | 1450 | =SUM(B2:G2) |
| Mesa | 800 | 750 | 900 | 850 | 780 | 920 | =SUM(B3:G3) |
| Estante | 450 | 500 | 480 | 520 | 490 | 510 | =SUM(B4:G4) |
| Ropero | 600 | 580 | 620 | 640 | 590 | 610 | =SUM(B5:G5) |

Luego usó MAX en la columna H:

=MAX(H2:H5) → 7800 (Sillas)
=MIN(H2:H5) → 2950 (Estante)

—Las sillas son nuestro producto estrella —concluyó Sofía.

---

## El presupuesto final para el hotel

Sofía armó el presupuesto combinando todo lo aprendido:

| A | B | C | D |
|---|---|---|---|
| **Concepto** | **Cálculo** | **Valor** |  |
| Costo materiales habitaciones | =SUM(E2:E5) | S/ 11,000.00 |  |
| Costo materiales suites | =SUM(E8:E12) | S/ 5,220.00 |  |
| **Total costo materiales** | =B2+B3 | S/ 16,220.00 |  |
| Margen de ganancia (40%) | =B4*0.40 | S/ 6,488.00 |  |
| **Precio de venta** | =B4+B5 | S/ 22,708.00 |  |
| IGV (18%) | =B6*0.18 | S/ 4,087.44 |  |
| **Precio final con IGV** | =B6+B7 | S/ 26,795.44 |  |

—Ya está —dijo Sofía, sonriendo—. El presupuesto está listo.

Pero mientras revisaba los números, algo le llamó la atención. El promedio de ventas mensuales de sillas era 1300. El hotel pedía 10 sillas a 150 cada una = 1500 soles. Eso era más del promedio mensual.

—Don Manuel —dijo—, este pedido del hotel representa más de un mes de ventas normales. Es grande.

—Por eso —respondió Don Manuel—, tu abuelo siempre decía que los números no mienten. Pero hay que saber interpretarlos.

---

## Enigmas del Capítulo 6

### Enigma 6.1: Totales del taller

Usando el inventario del Capítulo 1, calcula:

1. **SUMA** del Precio Unitario de todos los productos (¿cuánto vale todo el inventario por unidad?)
2. **PROMEDIO** del Precio Unitario (¿cuál es el precio promedio de los materiales?)
3. **MAX** del Precio Unitario (¿cuál es el material más caro?)
4. **MIN** del Precio Unitario (¿cuál es el material más barato?)
5. **CONTAR** cuántos productos tienen precio mayor a 30 soles

Crea una sección "Resumen" en tu hoja con estas funciones.

### Enigma 6.2: Análisis de ventas

Usando los datos de ventas históricas del capítulo (o creando tus propios datos):

1. ¿Cuál es el total de ventas de cada producto en el semestre?
2. ¿Cuál es el promedio mensual de ventas totales (suma de todos los productos)?
3. ¿Qué mes tuvo las ventas más altas?
4. ¿Qué mes tuvo las ventas más bajas?
5. ¿Cuántos valores de venta superan los 1000 soles?

Pista: usa SUM, AVERAGE, MAX, MIN y COUNTIF (CONTAR.SI) para la última.

### Enigma 6.3: Control de stock mínimo

Don Rafael estableció que ningún material puede bajar de 15 unidades. Usa la función MIN para verificar si algún producto está por debajo del mínimo.

Si el inventario actual tiene:
- Cedro: 50
- Roble: 30
- Pino: 100
- Triplay: 40
- Barniz: 10 → Está en riesgo
- Tornillos #10: 500
- Lija fina: 200

¿Qué función usarías para encontrar el valor mínimo de stock? ¿Qué productos están por debajo de 15?

### Enigma 6.4: Presupuesto de herramientas

Don Manuel necesita herramientas nuevas. Calcula el presupuesto:

| Herramienta | Cantidad | Precio Unit. |
|-------------|----------|-------------|
| Taladro | 2 | S/ 280.00 |
| Sierra circular | 1 | S/ 350.00 |
| Lijadora | 2 | S/ 180.00 |
| Juego de brocas | 3 | S/ 45.00 |

Usa:
1. SUMA para calcular el total general
2. PROMEDIO para el precio promedio de las herramientas
3. MAX y MIN para la herramienta más cara y más barata

---

## Lo que aprendiste

- **SUM** suma todos los valores de un rango
- **AVERAGE** calcula el promedio (media aritmética)
- **COUNT** cuenta celdas con números
- **MAX** encuentra el valor máximo
- **MIN** encuentra el valor mínimo
- Puedes **combinar funciones** para análisis más complejos
- Las funciones ahorran tiempo y reducen errores
- **Interpretar** los resultados es tan importante como calcularlos

---

Sofía envió el presupuesto al Hotel Miraflores a las 4:30 de la tarde. A las 5:15, recibió la respuesta de Carolina Ramírez:

*"Señorita Mendoza, el presupuesto está aprobado. Adjunto la orden de compra. Esperamos comenzar la próxima semana."*

Sofía saltó de la silla con un grito de alegría. Don Manuel la miró, riendo.

—¿Ves, mija? Los números no mienten. Y tú empezaste a entenderlos.

Esa noche, Sofía abrió el cuaderno de su abuelo y escribió al final:

*"Querido abuelo: Hoy conseguí mi primer pedido grande. Usé tus números. Tus fórmulas. Tu sistema. Gracias por dejarme el camino marcado."*

Luego apagó la luz, pero no pudo dormir. Estaba demasiado emocionada pensando en todo lo que aún le quedaba por aprender.
