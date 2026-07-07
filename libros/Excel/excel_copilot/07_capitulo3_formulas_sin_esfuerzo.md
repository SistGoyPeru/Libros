# Capítulo 3: Fórmulas sin Esfuerzo

Andrea había logrado limpiar los datos básicos. Pero el verdadero desafío estaba por venir.

—Necesito calcular el costo de inventario promedio ponderado —le dijo a Ricardo una tarde—. El archivo tiene precios de compra históricos con diferentes fechas y cantidades. Es un dolor de cabeza.

—Suena a trabajo para Copilot —respondió Ricardo sin levantar la vista de su pantalla.

Andrea dudó. Las fórmulas complejas eran su especialidad. Había pasado años aprendiendo BUSCARV, SUMAR.SI.CONJUNTO, INDICE, COINCIDIR. ¿Estaba dispuesta a delegar eso en una IA?

Decidió probar.

*"Copilot, necesito calcular el costo de inventario promedio ponderado para cada producto. Tengo las columnas: Producto, Fecha de Compra, Cantidad Comprada, Precio Unitario. El cálculo debe considerar el costo promedio ponderado por lote. ¿Puedes generar la fórmula?"*

La respuesta llegó en segundos:

*"Puedes usar la siguiente fórmula para calcular el costo promedio ponderado por producto:*

*=SUMAPRODUCTO((A:A=A2)*(C:C)*(D:D))/SUMAPRODUCTO((A:A=A2)*(C:C))*

*Donde:*
- *A:A = Columna de Producto*
- *C:C = Columna de Cantidad Comprada*
- *D:D = Columna de Precio Unitario*

*Esta fórmula suma (cantidad × precio) para cada producto y lo divide entre la suma total de cantidades de ese producto.*

*¿Te gustaría que agregue una columna con este cálculo en tu tabla?"*

Andrea examinó la fórmula. Era correcta. Elegante, incluso. Copilot no solo había entendido lo que necesitaba, sino que había generado una fórmula más limpia de lo que ella misma habría escrito.

—Está bien, Copilot —dijo en voz baja—. Me has impresionado.

---

### Conceptos Clave: Fórmulas con Copilot

Copilot puede generar desde fórmulas simples hasta las más complejas. Pero hay reglas que debes conocer.

#### Cómo Pedir una Fórmula

Sé específico sobre:

1. **Qué quieres calcular**: "La comisión del 5% sobre ventas que superen los $10,000"
2. **Columnas involucradas**: "Tengo Ventas en columna B, Vendedor en columna A"
3. **Condiciones**: "Solo para el mes de enero"
4. **Formato del resultado**: "Con dos decimales y símbolo de moneda"

#### Ejemplos de Fórmulas con Copilot

**BÚSQUEDA:**
*Prompt:* "Necesito buscar el precio del producto 'Laptop ProBook' en la tabla de precios que está en la hoja 'Precios'. Usar BUSCARV o XLOOKUP."

*Resultado:* `=XLOOKUP("Laptop ProBook", Precios!A:A, Precios!B:B)`

**CONDICIONALES:**
*Prompt:* "Quiero clasificar las ventas en tres categorías: 'Alta' si > $10,000, 'Media' si entre $5,000 y $10,000, 'Baja' si < $5,000."

*Resultado:* `=SI(B2>10000,"Alta",SI(B2>=5000,"Media","Baja"))`

**ANIDADAS:**
*Prompt:* "Calcula el bono anual: si el vendedor cumplió meta (>$100K) y tiene más de 2 años de antigüedad, bono del 10%; si cumplió meta pero tiene menos de 2 años, bono del 5%; si no cumplió meta, 0."

*Resultado:*
`=SI(Y(B2>100000,C2>2),B2*0.1,SI(B2>100000,B2*0.05,0))`

#### Validación de Fórmulas

Siempre verifica las fórmulas que Copilot genera:

1. **Pruébala con datos conocidos**: ¿El resultado es el esperado?
2. **Revisa las referencias**: ¿Apuntan a las columnas correctas?
3. **Comprueba casos borde**: ¿Qué pasa si hay celdas vacías?
4. **Pide explicación**: Si no entiendes la fórmula, pídele a Copilot que te la explique.

---

### Ejercicio 3.1: Traductor de Fórmulas

Escribe una fórmula que ya conozcas en lenguaje natural y pídele a Copilot que la genere. Por ejemplo:

*"En la columna E, quiero calcular el IVA (18%) del subtotal que está en la columna D, pero solo si la celda de la columna A dice 'Facturable'. Si dice 'No Facturable', el IVA debe ser 0."*

Compara la fórmula de Copilot con la que tú habrías escrito.

### Ejercicio 3.2: Explicación de Fórmulas

Pega una fórmula compleja que hayas heredado de un compañero y pídele a Copilot:

*"Explica qué hace esta fórmula paso a paso: [pegar fórmula]"*

¿La explicación de Copilot te ayudó a entenderla?
