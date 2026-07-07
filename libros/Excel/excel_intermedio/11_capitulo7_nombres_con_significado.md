# Capítulo 7: Nombres con Significado

## Tema: Rangos con nombre, administrador de nombres

---

—¿Te has dado cuenta de que tus fórmulas se están volviendo ilegibles? —preguntó Carlos mientras miraba la pantalla de Sofía.

—¿Ilegibles? Funcionan bien.

—Funcionan, sí. Pero mira esta fórmula:

```
=SI.ERROR(BUSCARV(A2; $G$2:$H$156; 2; FALSO); "No encontrado")
```

—¿Qué es `$G$2:$H$156`?

—Es el rango de la tabla maestra —respondió Sofía—. Columna G y H, filas 2 a 156.

—¿Y si dentro de un mes agregas más filas? Tendrías que cambiar todas las fórmulas. ¿Y si alguien más tiene que mantener este archivo? Tendría que descifrar qué significa cada rango.

—Ya veo el problema. No es muy... amigable.

—Por eso existen los **rangos con nombre**. En lugar de escribir `$G$2:$H$156`, puedes escribir `TablaMaestraProductos`. La fórmula se lee sola:

```
=SI.ERROR(BUSCARV(A2; TablaMaestraProductos; 2; FALSO); "No encontrado")
```

—Es como darle nombre a las direcciones —dijo Sofía—. Como ponerle "Casa de la Abuela" en lugar de "Av. Los Pinos 123".

—Exactamente. Y además, el rango se ajusta automáticamente si agregas o quitas datos.

---

## Creando rangos con nombre

—Hay varias formas de crear rangos con nombre:

**Método 1: Cuadro de nombres**
—A la izquierda de la barra de fórmulas está el **cuadro de nombres**. Selecciona el rango y escribe el nombre allí.

Sofía seleccionó el rango de la tabla maestra (G1:H156) y escribió `TablaMaestra` en el cuadro de nombres. Presionó Enter.

—Listo. Ahora `TablaMaestra` se refiere a ese rango.

**Método 2: Administrador de nombres**
—Para más control, usa **Fórmulas > Administrador de nombres** (o Ctrl+F3).

Se abrió un cuadro de diálogo mostrando todos los nombres definidos en el libro.

—**Nuevo...** —dijo Carlos—. Aquí puedes:
1. Escribir el **Nombre** (sin espacios, sin caracteres especiales)
2. Seleccionar el **Ámbito** (solo esta hoja o todo el libro)
3. Escribir un **Comentario** explicativo
4. Definir el **rango** al que se refiere

—Crea un nombre para la columna Valor_A del archivo secreto.

Sofía creó: `Ingresos` = `Hoja1!$B$2:$B$1001`

—Ahora puedo hacer `=SUMA(Ingresos)` en lugar de `=SUMA(Hoja1!$B$2:$B$1001)`.

—Exacto. Y la fórmula es mucho más clara.

**Método 3: Crear desde selección**
—Si tu tabla tiene encabezados, puedes crear nombres automáticamente.

Selecciona la tabla incluyendo los encabezados. Ve a **Fórmulas > Crear desde selección**. Marca "Fila superior". Excel creará nombres usando los encabezados.

—Así, si tu columna se llama "Valor_A", se creará automáticamente un nombre `Valor_A` para todo el rango de datos.

---

## Reglas para nombres válidos

—Los nombres tienen reglas —advirtió Carlos—:

| Regla | Correcto | Incorrecto |
|-------|----------|------------|
| Sin espacios | TotalIngresos | Total Ingresos |
| No empieza con número | Ingreso2024 | 2024Ingreso |
| Sin caracteres especiales | Ventas_Q1 | Ventas-Q1 |
| No es una dirección de celda | Total1 | A1 |
| Máximo 255 caracteres | — | (más de 255) |

—Puedes usar mayúsculas, minúsculas, números (no al inicio), guión bajo (\_), punto (.) —aunque el punto puede confundirse con el operador de rango, así que mejor evitarlo.

—¿Los nombres distinguen entre mayúsculas y minúsculas? —preguntó Sofía.

—No. `TotalIngresos` y `totalingresos` son el mismo nombre. Excel los trata como iguales.

---

## Beneficios de los rangos con nombre

—Más allá de la legibilidad, los rangos con nombre tienen ventajas prácticas:

**1. Fórmulas auto-documentadas:**
```
=SUMA(Ingresos) - SUMA(Gastos)
```
vs
```
=SUMA(Hoja1!B:B) - SUMA(Hoja1!C:C)
```

**2. Navegación rápida:**
—En el cuadro de nombres, escribe `Ingresos` y presiona Enter. Excel te lleva directamente a ese rango.

**3. Rangos dinámicos (avanzado):**
—Un rango con nombre puede crecer automáticamente usando la función DESREF:

```
=DESREF(Hoja1!$B$2;0;0;CONTARA(Hoja1!$B:$B);1)
```

—Este rango se expande automáticamente al agregar nuevos datos. Pero eso es nivel avanzado.

**4. Listas desplegables dinámicas:**
—Recuerdas las listas desplegables que aprendiste? Puedes referenciar un rango con nombre en la validación: `=ListaMaderas`.

---

## Usando nombres en fórmulas

—Ahora reescribamos algunas fórmulas del archivo con nombres —propuso Carlos.

Sofía había estado usando:

```
=SUMA(Hoja1!$B$2:$B$1001)
=SI.ERROR(BUSCARV(A2; Hoja1!$G$2:$H$156; 2; FALSO); "No encontrado")
=PROMEDIO(Hoja1!$C$2:$C$1001)
```

Después de crear los nombres:

```
=SUMA(Ingresos)
=SI.ERROR(BUSCARV(A2; TablaMaestra; 2; FALSO); "No encontrado")
=PROMEDIO(Egresos)
```

—¿Ves la diferencia? —dijo Carlos—. Ahora cualquiera que abra el archivo puede entender qué hace cada fórmula sin tener que rastrear referencias.

—Es hermoso —dijo Sofía—. ¿Por qué no me enseñaste esto antes?

—Porque primero necesitabas entender las referencias absolutas y relativas. Los rangos con nombre son como referencias absolutas con esteroides.

---

## Administrador de nombres

—Cuando tu archivo crece, puedes tener docenas de nombres —dijo Carlos—. El **Administrador de nombres** (Ctrl+F3) te permite:

1. **Ver todos los nombres** definidos en el libro
2. **Editar** la referencia de un nombre
3. **Eliminar** nombres que ya no usas
4. **Filtrar** por ámbito (hoja o libro)
5. **Buscar** nombres específicos

—También puedes ver el **uso de nombres** en las fórmulas: si un nombre está en uso, no deberías eliminarlo sin antes actualizar las fórmulas que lo referencian.

---

### Enigma 7.1: Nombra las columnas del archivo secreto

Crea rangos con nombre para cada columna del archivo secreto:
- `Codigos` = columna A
- `Ingresos` = columna B (Valor_A)
- `Egresos` = columna C (Valor_B)
- `Indicador` = columna D (Valor_C)
- `Fechas` = columna E

Luego escribe una fórmula que calcule el total de ingresos menos egresos usando estos nombres.

---

### Enigma 7.2: Crea un nombre para el rango dinámico de la tabla maestra

Usando DESREF, crea un nombre `Productos` que se expanda automáticamente al agregar productos a la tabla maestra. Pista:

```
=DESREF(Hoja2!$A$2;0;0;CONTARA(Hoja2!$A:$A)-1;2)
```

---

### Enigma 7.3: Documenta tu archivo

En el Administrador de nombres, agrega comentarios a cada nombre explicando qué representa. Por ejemplo, para `Ingresos`: "Valores de ingreso del archivo secreto de Don Rafael (2005-2015)".

---

## Lo que aprendiste

- Los **rangos con nombre** reemplazan direcciones de celda por nombres descriptivos
- Se crean desde el **cuadro de nombres**, el **Administrador de nombres** o **Crear desde selección**
- Tienen **reglas** (sin espacios, no empiezan con número, sin caracteres especiales)
- Hacen las **fórmulas más legibles** y auto-documentadas
- El **Administrador de nombres** permite gestionar, editar y eliminar nombres
- Los **rangos dinámicos** (con DESREF) se expanden automáticamente al agregar datos

---

—Con los rangos con nombre, el archivo está mucho más organizado —dijo Sofía—. Pero todavía no sé qué representan los números.

—Tal vez sea momento de dejar de mirar el pasado y empezar a planear el futuro —dijo Carlos—. Mañana te enseño **análisis de hipótesis**.

—¿Para qué?

—Para responder preguntas como: "¿Cuánto tengo que vender para alcanzar una meta?" o "¿Qué pasa si los costos suben un 20%?".

—¿Y eso cómo me ayuda con el misterio del abuelo?

—Tal vez no te ayude con el pasado. Pero te ayudará a decidir qué hacer con lo que descubras. El abuelo no solo quería que encontraras el archivo. Quería que hicieras algo con él.

Sofía asintió lentamente. Tenía la sensación de que se acercaba a algo grande. Algo que cambiaría no solo su comprensión del pasado, sino también el futuro del taller.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
