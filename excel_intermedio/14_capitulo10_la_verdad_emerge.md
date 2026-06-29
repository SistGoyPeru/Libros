# Capítulo 10: La Verdad Emmerge

## Tema: Proyecto integrador — consolidación de todo lo aprendido

---

—Es hora de unir todas las piezas —dijo Carlos, ajustándose los lentes con determinación.

Eran las siete de la mañana. El taller aún no abría. El único sonido era el zumbido del refrigerador y el tecleo ocasional del mouse. Sobre la mesa, tres cosas: la laptop con el archivo secreto, el cuaderno azul de Don Rafael, y una taza de café humeante.

—Hagamos un repaso de lo que sabemos —propuso Sofía.

---

## Lo que sabemos

**El archivo:** Un libro de Excel con 1000 registros de transacciones entre 2005 y 2015, protegido con contraseña ("lignum").

**Las columnas:**
- Código (AX, BX, CX, DX + número correlativo)
- Valor_A, Valor_B, Valor_C (tres tipos de valores numéricos)
- Fecha

**Lo que descubrimos con cada herramienta:**

| Herramienta | Revelación |
|-------------|------------|
| Formato condicional | Los valores altos se concentran en nov-dic de cada año |
| Validación y comentarios | El abuelo mencionaba a Carlos y al abogado Montenegro |
| BUSCARV / BUSCARX / INDICE+COINCIDIR | Los códigos referencian una tabla maestra con productos |
| Tabla dinámica | Resumen de 1.8M en ingresos, 1.2M en egresos, con un patrón trimestral de transferencias |
| Gráficos avanzados | Correlación fuerte entre Valor_A y Valor_C (R²=0.89) |
| Texto en columnas | El cuaderno azul contiene instrucciones y nombres |
| Rangos con nombre | Las fórmulas ahora son legibles |
| Análisis de hipótesis | Proyección de 245,000 soles en ahorros |
| Dashboard | Vista unificada de todo el negocio |

—Falta una pieza —dijo Carlos—. El abogado Montenegro.

---

## La visita al abogado

El estudio del Dr. Montenegro estaba en el centro de Lima, en un edificio antiguo con ascensor de rejas. La oficina olía a libros viejos y papel sellado. El hombre, ya mayor, los recibió con una sonrisa que delataba que los estaba esperando.

—Sabía que vendrían —dijo Montenegro, indicándoles que se sentaran—. Don Rafael me dijo: "Mi nieta encontrará el archivo. Y cuando lo haga, necesitará esto."

Abrió un sobre lacrado y extrajo una carta.

*"Querida Sofía:*

*Si estás leyendo esto, significa que encontraste el archivo. Y significa que aprendiste lo suficiente para entenderlo.*

*Durante 10 años, aparté una parte de los ingresos del taller en un fondo especial. No era dinero que sobrara: era dinero que trabajaba para el futuro. Cada trimestre, transfería 5,000 soles a una cuenta de ahorros. A veces más, cuando el negocio iba bien.*

*¿Por qué en secreto? Porque no quería que nadie supiera que estábamos ahorrando. Los negocios tienen enemigos, Sofía. Y a veces los enemigos están más cerca de lo que creemos.*

*El archivo que encontraste no es solo un registro. Es un mapa. Cada código, cada valor, cada fecha cuenta una parte de la historia. Si lograste leerlo, significa que dominas las herramientas que necesitas para manejar no solo este taller, sino cualquier negocio.*

*Los 245,000 soles (más intereses) están en una cuenta a tu nombre en el Banco del Sur. El número de cuenta está cifrado en el archivo. Si has llegado hasta aquí, sabrás cómo encontrarlo.*

*Confío en ti, Sofía. Siempre confié.*

*Con todo mi amor,*
*Don Rafael Mendoza"*

Sofía sintió que las lágrimas le quemaban los ojos. —No sabía que el abuelo confiaba tanto en mí.

—Tu abuelo —dijo Montenegro— me pidió que te entregara esto solo cuando demostraras que podías descifrar el archivo. Y lo has hecho.

—Pero todavía falta el número de cuenta —dijo Carlos—. Dijo que está cifrado en el archivo.

---

## El descifrado final

De vuelta en el taller, Sofía abrió el archivo con nuevos ojos. Ahora sabía lo que buscaba: un número de cuenta bancaria.

—Si el abuelo cifró el número en el archivo, ¿dónde podría estar? —preguntó.

—Probablemente en los valores —dijo Carlos—. Mira, hay 10 años de datos, 40 trimestres. Si tomamos Valores_C de ciertos trimestres...

—O los códigos —interrumpió Sofía—. Los códigos tienen números: 1001, 1002, 1003... algunos podrían ser parte del número de cuenta.

—Pero hay 1000 códigos. ¿Cuáles elegir?

—Los que tienen sentido. Recordemos la correlación: Valor_A y Valor_C están relacionados. ¿Y si el número de cuenta está en Valor_C de los primeros registros de cada año?

Sofía creó una tabla dinámica filtrando solo los primeros registros de cada año (enero). Extrajo Valor_C de cada uno.

| Año | Valor_C (Enero) |
|-----|-----------------|
| 2005 | 67 |
| 2006 | 12 |
| 2007 | 89 |
| 2008 | 23 |
| 2009 | 45 |
| 2010 | 78 |
| 2011 | 34 |
| 2012 | 56 |
| 2013 | 91 |
| 2014 | 18 |

—67-12-89-23-45-78-34-56-91-18 —leyó Sofía—. No parece un número de cuenta.

—Tal vez tiene que sumar algo... o usar otro método.

—Espera —dijo Sofía—. Y si en lugar de los valores, usamos las **posiciones**? La correlación entre Valor_A y Valor_C era fuerte, pero no perfecta. ¿Y si el mensaje está en la **diferencia**?

Calculó la diferencia entre Valor_A y Valor_C para cada primer registro:

| Año | Valor_A | Valor_C | Diferencia |
|-----|---------|---------|------------|
| 2005 | 1450 | 67 | 1383 |
| 2006 | 890 | 12 | 878 |
| 2007 | 2340 | 89 | 2251 |
| ... | ... | ... | ... |

—No funcionó.

—Intenta con los **comentarios** —sugirió Carlos—. Recordemos que el abuelo usaba comentarios en algunas celdas. Tal vez los comentarios contienen pistas.

Sofía revisó los comentarios que había encontrado antes. Uno decía: *"AX-1001 a AX-1050 = lote experimental"*. 

—"Lote experimental" —repitió—. ¿Qué tal si el número de cuenta está en los códigos del lote experimental?

Filtró los códigos AX-1001 a AX-1050. En la columna Valor_B, los números formaban una secuencia:

| Código | Valor_B |
|--------|---------|
| AX-1001 | 2340 |
| AX-1002 | 4520 |
| AX-1003 | 1450 |
| AX-1004 | 6780 |
| AX-1005 | 1230 |

—2340-4520-1450-6780-1230... muy largos para un número de cuenta. Pero tal vez... solo los primeros dígitos.

—O tal vez —dijo Carlos— sea más simple. ¿Qué tal si usas **Relleno rápido** para extraer algo?

—O mejor —dijo Sofía—, usemos los **minigráficos**. Recuerda que los minigráficos muestran tendencias. ¿Y si el patrón del minigráfico de Valor_C para todo el período forma un código?

—No creo que los minigráficos guarden datos cifrados.

—Entonces volvamos a lo básico —dijo Sofía—. El abuelo sabía que yo aprendería Excel. Sabía que llegaría hasta aquí. ¿Qué me enseñó primero en todo esto? **Formato condicional**.

Sofía aplicó formato condicional agresivo a toda la tabla: barras de datos en Valor_A, escala de colores en Valor_B, conjuntos de iconos en Valor_C.

—¿Qué ves? —preguntó Carlos.

—Las barras de datos en Valor_A... algunas son muy largas, otras cortas. No hay patrón obvio.

—Ahora mira los iconos en Valor_C.

Los semáforos estaban distribuidos. Pero Sofía notó algo: en la fila 23, el icono era rojo. En la fila 54, verde. En la fila 78, amarillo.

—Rojo, verde, amarillo... como un semáforo. ¿Y si es un código?

—No creo que tu abuelo usara semáforos para cifrar datos bancarios.

—Tienes razón —suspiró Sofía—. Estoy sobrepensando esto.

—Tal vez deberías dejar de pensar y simplemente **mirar** —dijo Carlos—. El archivo completo. Sin filtros, sin tablas dinámicas. Solo los datos originales con formato condicional.

Sofía miró la hoja completa. Las barras de datos de Valor_A creaban un patrón visual de altibajos. Los colores de Valor_B formaban un degradado. Los iconos de Valor_C titilaban en verde, amarillo y rojo.

Y entonces lo vio.

—Carlos... los iconos en Valor_C no son aleatorios. Mira la primera fila de cada bloque de 50 registros.

—¿Qué tiene?

—Es una secuencia: verde, verde, rojo, amarillo, verde, rojo, rojo, amarillo... tres verdes al inicio de cada bloque. Como un código de colores.

—¿Un código de barras?

—O un **código de colores** que representa números. Verde=1, Amarillo=2, Rojo=3.

Sofía anotó la secuencia de los primeros 20 bloques:

```
1,1,2,1,3,1,1,2,3,1,2,2,1,3,1,1,1,2,3,3
```

—11213112312213111233... ¿tiene sentido?

—No parece un número de cuenta. Pero tal vez no sea decimal —dijo Carlos—. Tal vez es un código que hay que convertir.

—¿A qué?

—A letras. A=1, B=2, C=3...

Sofía escribió las letras: A, A, B, A, C, A, A, B, C, A, B, B, A, C, A, A, A, B, C, C...

—"AABACAABCABBA..." no forma palabras.

—Tal vez es un cifrado más complejo —dijo Carlos—. O tal vez estamos equivocados.

—O tal vez necesitamos **combinar** los enfoques —dijo Sofía—. Mira, la correlación entre Valor_A y Valor_C era alta. ¿Y si el código está en la **relación** entre dos columnas?

Calculó una nueva columna: `Valor_C / Valor_A * 100`.

Usando formato condicional (escala de colores) en esta nueva columna, apareció un patrón mucho más claro.

—Los porcentajes altos (verde) están en las filas 45, 120, 203, 301... —Sofía anotó—. 45, 120, 203, 301, 450...

—Números de celda —dijo Carlos—. ¿Qué hay en esas celdas?

Sofía fue a la celda A45: `AX-2045`. A la celda A120: `BX-3120`.

—No parecen formar un número de cuenta...

—Pero mira las celdas **adyacentes** —dijo Carlos—. Tal vez las celdas con mayor ratio contienen los dígitos.

En la fila 45, Valor_A era 2340. En la 120, Valor_A era 5670. En la 203, 890.

—No.

Sofía estaba a punto de rendirse cuando recordó algo.

—El abuelo siempre decía: "Lo más simple es lo más difícil de ver." La contraseña del archivo era "lignum". Madera en latín. Tal vez todo sea más simple de lo que creemos.

—¿Qué es lo más simple que hemos pasado por alto?

—Los **títulos de las columnas** —dijo Sofía—. "Valor_A", "Valor_B", "Valor_C". ¿Y si en lugar de valores, son las **iniciales de algo**?

—¿Como qué?

—No sé. Valor_A podría ser "Ahorro". Valor_B "Base". Valor_C "Cuenta".

—A, B, C... —Carlos se quedó pensando—. O tal vez: C = **Cuenta**. Valor_C es la columna que tiene información sobre la cuenta.

—Y la correlación con Valor_A... ¿y si Valor_A es el monto y Valor_C es el **dígito verificador** o parte del número?

Sofía volvió a las primeras filas. En la primera transacción de 2005:

```
Valor_A = 1450
Valor_C = 67
```

—1450 y 67... 145067... son 6 dígitos. Los números de cuenta suelen tener 14 o 20 dígitos.

—Tal vez necesitas más transacciones —dijo Carlos—. O tal vez los dígitos están en el **orden de las transacciones**, no en sus valores.

—Espera —dijo Sofía, con los ojos brillando—. ¿Y si el número está en el **cuaderno azul** pero cifrado con el archivo?

Abrió el cuaderno azul en la página donde había visto "Montenegro".

—Aquí dice: "2009-04-12: Entregado a Montenegro. Ref: 001-002-003." —Sofía leyó en voz alta—. ¿001-002-003? Eso parece una referencia a códigos del archivo.

—¿Códigos? —Carlos se inclinó—. Los códigos empiezan con AX, BX, CX, DX... pero 001, 002, 003... son números de fila.

—O números de **celda** —dijo Sofía—. En Excel, la celda A1 es la primera. A2 la segunda. Si 001 es la fila 1, 002 la fila 2...

—Pero no hay nada en las primeras filas que parezca un número de cuenta.

—Tal vez no son las primeras filas del archivo —dijo Sofía—. Tal vez son las primeras filas de **cada bloque**.

Contó las filas: había 1000 registros. Si los dividía en grupos de 10, obtenía 100 bloques. La fila 1 de cada bloque...

En el bloque 1 (filas 1-10), el primer código era AX-1001. En el bloque 2 (11-20), era AX-1011. En el bloque 3 (21-30), AX-1021.

—Los últimos dos dígitos de cada código son 01, 11, 21, 31... —contó Sofía—. 01, 11, 21, 31... eso no da un número de cuenta.

—Sofía —dijo Carlos en voz baja—, mira la **primera transacción de cada mes**. No de cada bloque. De cada mes.

Sofía creó una tabla dinámica agrupada por año y mes, mostrando el primer Valor_A de cada mes.

| Año | Mes | Primer Valor_A | Primer Valor_C |
|-----|-----|----------------|----------------|
| 2005 | Ene | 1450 | 67 |
| 2005 | Feb | 1890 | 12 |
| 2005 | Mar | 2340 | 89 |
| 2005 | Abr | 3450 | 23 |
| 2005 | May | 5670 | 45 |
| 2005 | Jun | 1230 | 78 |

—1450, 1890, 2340, 3450, 5670, 1230... no parece un número de cuenta.

—Ahora Valor_C —dijo Carlos—. 67, 12, 89, 23, 45, 78...

—67-12-89-23-45-78 —repitió Sofía—. Son solo dos dígitos cada uno. No son suficientes.

—Pero si concatenas los Valor_C de **todo el año 2005**...

Sofía usó CONCATENAR (o TEXTJOIN) para unir todos los Valor_C de 2005 en orden:

```
=TEXTJOIN(""; VERDADERO; SI(AÑO(Fechas)=2005; Indicador; ""))
```

Resultado: `6712892345783412561891...`

—Esto tiene 40+ dígitos —dijo Sofía—. Demasiado largo.

—Pero 20 dígitos es un número de cuenta típico —dijo Carlos—. Tal vez los primeros 20.

—67128923457834125618 —leyó Sofía—. Eso podría ser.

—¿Y si es el número de cuenta? —preguntó Carlos—. Marcó al banco.

Sofía dudó. —Hagamos una prueba más. Si el abuelo dejó este número cifrado, debería tener una **confirmación** en alguna parte del archivo. Una suma de verificación, un dígito de control.

Calculó la suma de todos los Valor_C: `=SUMA(Indicador)`. El resultado era 98,700.

—98,700 —dijo—. Los últimos 6 dígitos de ese número de 20 dígitos son 341,256. 98,700 no se parece.

—Pero la **suma de dígitos** —insistió Carlos—: 9+8+7+0+0 = 24. Y los dígitos de control...

—No, espera —dijo Sofía de repente—. 98,700. 98-700. 98 es el código de Perú. Y 700...

—700 es la suma de los Valor_C del año 2005 multiplicado por algo... —Carlos hizo cálculos mentales.

—No —dijo Sofía—. 98,700 dividido entre 1000 registros... da 98.7. Eso es el promedio de Valor_C.

—¿Qué promedio?

—El promedio de todos los valores de la columna C. Y si tomas solo los primeros dígitos de ese promedio... 98...

—¿No estás forzando los números? —preguntó Carlos con una sonrisa.

—Tal vez —rió Sofía—. Pero es la única pista que tenemos que tenga sentido.

---

## El momento de la verdad

—No podemos saber si es correcto sin probarlo —dijo Carlos—. Llama al banco.

Sofía marcó el número del Banco del Sur. Después de varios minutos de verificación, la voz de una ejecutiva dijo:

—Sí, señorita Mendoza. Tenemos una cuenta de ahorros a su nombre, abierta en 2005 por Don Rafael Mendoza. El saldo actual es de 287,432.65 soles.

Sofía sintió que el mundo se detenía.

—¿Está segura? —preguntó con voz temblorosa.

—Completamente. ¿Desea hacer algún movimiento?

—No... no, gracias. Solo... confirmar.

Colgó. Miró a Carlos con los ojos llenos de lágrimas.

—287,432 soles —susurró—. El abuelo ahorró todo esto para mí.

—Y aprendiste todas las herramientas de Excel necesarias para descubrirlo —dijo Carlos—. No es coincidencia. Él sabía que este viaje te prepararía para manejar ese dinero.

—Pero... ¿cómo supo que yo aprendería?

—Porque te conocía, Sofía. Sabía que eras curiosa. Sabía que encontrarías el archivo. Y sabía que no te rendirías hasta descifrarlo. Igual que él.

Sofía miró la pantalla. El dashboard, las tablas dinámicas, los gráficos, el formato condicional. Todo lo que había aprendido en las últimas semanas la había llevado hasta este momento.

El legado de su abuelo no era el dinero.

Era el conocimiento.

---

## Proyecto integrador

Ahora es tu turno. Tienes todas las herramientas que aprendió Sofía. Es momento de aplicarlas en un proyecto completo.

### Enigma 10.1: Reconstruye el viaje de Sofía

Usando los datos del archivo secreto (o creando tus propios datos similares), reproduce el análisis completo de Sofía:

1. **Formato condicional:** Aplica barras de datos, escalas de color y conjuntos de iconos para identificar patrones visuales
2. **Validación y comentarios:** Agrega validación de datos a las columnas y comenta celdas importantes
3. **Búsquedas:** Crea una tabla maestra y usa BUSCARX para enriquecer los datos
4. **Tabla dinámica:** Resuma los datos por año, trimestre y tipo de código
5. **Gráficos:** Crea un gráfico combinado y minigráficos de tendencia
6. **Rangos con nombre:** Define nombres para todos los rangos importantes
7. **Análisis de hipótesis:** Proyecta el valor futuro del ahorro con diferentes tasas de interés
8. **Dashboard:** Unifica todo en un tablero de control interactivo

---

### Enigma 10.2: El mensaje cifrado

Crea tu propio mensaje cifrado en Excel, usando las técnicas que aprendiste:
- Ocultar un mensaje en formato condicional (colores, iconos)
- Usar los comentarios como pistas
- Emplear funciones de búsqueda para decodificar
- El mensaje final debe revelarse solo después de aplicar múltiples herramientas

---

### Enigma 10.3: Dashboard del taller

Crea un dashboard completo para el taller Mendoza & Hijos que incluya:

- **KPI:** Ingresos mensuales, egresos, ganancia, productividad
- **Gráfico de tendencia:** Evolución mensual del año actual
- **Tabla de productos:** Los 5 productos más vendidos
- **Segmentadores:** Por año, mes, categoría
- **Control de formulario:** Botón de giro para cambiar entre años
- **Formato condicional:** Alertas visuales cuando la ganancia sea negativa

---

## Lo que aprendiste

- El **proyecto integrador** consolida todas las herramientas intermedias de Excel
- Cada herramienta aporta una perspectiva diferente al análisis de datos
- Los datos cuentan una historia cuando sabes cómo hacerlos hablar
- El **conocimiento técnico** combinado con la **persistencia** puede resolver los misterios más complejos
- El verdadero valor de Excel no está en las funciones individuales, sino en cómo las **combinas** para resolver problemas reales

---

—287,432 soles —repitió Sofía, todavía incrédula—. ¿Qué voy a hacer con esa cantidad de dinero?

—Tu abuelo ya decidió por ti —dijo Carlos, entregándole la carta—. Dice: "Para la expansión del taller".

—¿Expansión?

—Sí. Cuando tu mamá me contrató hace años, Don Rafael ya hablaba de expandirse. Comprar el local de al lado, más maquinaria, contratar más personal. Nunca tuvo el capital. Hasta ahora.

Sofía miró por la ventana del taller. Vio a su mamá atendiendo a un cliente, a los carpinteros trabajando la madera, al aprendiz barriendo el aserrín. El taller era pequeño, familiar, pero estaba lleno de sueños.

—Voy a hacerlo —dijo—. Voy a expandir el taller. Pero voy a hacerlo bien, con datos, con análisis, con Excel.

—Eso es exactamente lo que tu abuelo quería escuchar.

Sofía guardó el archivo, cerró la laptop, y sintió que por primera vez en mucho tiempo, el futuro estaba claro.

El legado de Don Rafael no era un archivo secreto ni una cuenta de ahorros. Era la certeza de que su nieta podía enfrentar cualquier desafío con las herramientas adecuadas y la determinación correcta.

Y estaba en lo correcto.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
