# Capítulo 1: El Archivo Secreto

## Tema: Formato condicional — barras de datos, escalas de color, conjuntos de iconos

---

—Esto es un mar de números —dijo Sofía, desplazándose por las filas del archivo secreto—. Hay datos desde 2005 hasta 2015. Más de mil registros.

Carlos se inclinó sobre la pantalla. —El problema no es la cantidad, es que no sabemos qué representan estos números. Necesitamos encontrar **patrones**.

—¿Cómo encontramos patrones en mil números sin volvernos locas?

—Con **formato condicional**. Excel tiene una herramienta que analiza los datos y aplica formatos automáticamente según reglas que tú defines. Es como si los números se pintaran solos para revelar lo que esconden.

Carlos tomó el control del mouse.

—Mira. Selecciona toda la columna Valor_A. Luego ve a la cinta de opciones: **Inicio > Formato condicional > Barras de datos**.

Hizo clic. Instantáneamente, cada celda de la columna se llenó con una barra de color proporcional al valor. Los números grandes tenían barras casi completas; los pequeños, apenas una línea.

—¡Wow! —exclamó Sofía—. Ahora puedo ver qué valores son altos y cuáles bajos sin leer cada número.

—Eso es solo el principio —dijo Carlos, claramente disfrutando el momento.

---

## Barras de datos: el pulso de los números

Las **barras de datos** son como termómetros dentro de las celdas. La longitud de la barra es proporcional al valor de la celda en relación con el resto de los datos. Es la forma más rápida de identificar valores altos y bajos.

Hay dos estilos principales:
- **Relleno degradado:** la barra se difumina hacia el final
- **Relleno sólido:** la barra tiene color uniforme

Sofía experimentó con ambas opciones.

—Prefiero el relleno sólido —dijo—. Se ve más limpio.

—Buena elección. Ahora, apliquemos **escalas de color** a la columna Valor_B.

---

## Escalas de color: el mapa de calor de los datos

Carlos seleccionó la columna Valor_B y fue a **Formato condicional > Escalas de color**. Apareció una paleta de opciones: escalas de dos colores (blanco-rojo, blanco-azul) y de tres colores (verde-amarillo-rojo).

—Usa la escala verde-amarillo-roja —sugirió—. Es la más intuitiva: verde para valores altos, amarillo para medios, rojo para bajos.

—Parece un mapa de calor —observó Sofía—. Como los que muestran la temperatura en el noticiero.

—Exactamente. Es un **mapa de calor** para tus datos. Mira cómo los valores altos están en verde y los bajos en rojo. ¿Ves algún patrón?

Sofía recorrió la columna con la mirada. —Los valores altos en Valor_B parecen coincidir con valores altos en Valor_A...

—Exacto. Pero no podemos estar seguros solo mirando. Necesitamos más información.

| Código | Valor_A (barras) | Valor_B (escala de color) | Valor_C (iconos) |
|--------|-----------------|---------------------------|-------------------|
| AX-1001 | ████████ 1450 | ████████ (verde) | 67 |
| BX-1002 | ████ 890 | ████████████ (verde claro) | 12 |
| CX-1003 | ████████████ 2340 | ████████ (verde) | 89 |
| DX-1004 | ██████████████████ 3450 | ████████████████████ (verde) | 23 |
| AX-1005 | ████████████████████████████ 5670 | ████████████ (verde claro) | 45 |

*Nota: Las barras y colores son representaciones visuales. En tu pantalla se verán con colores reales.*

---

## Conjuntos de iconos: semáforos para tus datos

—Ahora veamos los conjuntos de iconos —Carlos seleccionó la columna Valor_C—. **Formato condicional > Conjuntos de iconos**.

Aparecieron opciones: flechas direccionales, semáforos, formas geométricas, estrellas.

—Usa los semáforos —dijo Carlos—. Excel dividirá automáticamente los datos en tres grupos: los valores más altos recibirán un círculo verde, los medios uno amarillo, los bajos uno rojo.

—¿Y cómo decide qué es "alto" o "bajo"?

—Por defecto, usa percentiles. El 33% más alto es verde, el 33% medio es amarillo, el 33% más bajo es rojo. Pero puedes personalizarlo.

Sofía aplicó los semáforos y miró la columna. —Los valores altos en Valor_C no coinciden con los altos de las otras columnas...

—Exacto. Y eso es interesante. ¿Por qué una misma transacción tendría un valor alto en A y B, pero bajo en C?

—Tal vez son tipos diferentes de datos —razonó Sofía—. Como si Valor_A fuera ingresos, Valor_B egresos, y Valor_C... no sé, ¿margen de ganancia?

—O algo completamente distinto. Pero ahora tenemos una pista: hay una relación entre las columnas, pero no es directa. Necesitamos analizar más.

---

## Reglas personalizadas

—¿Podemos crear nuestras propias reglas? —preguntó Sofía.

—Por supuesto. **Formato condicional > Nueva regla**. Puedes crear reglas basadas en valores de celda, fórmulas, o incluso basadas en el valor de otra celda.

Carlos le mostró cómo crear una regla personalizada:

1. Seleccionar el rango de datos
2. **Inicio > Formato condicional > Nueva regla**
3. Elegir "Aplicar formato únicamente a las celdas que contengan"
4. Configurar: "Valor de celda > 5000"
5. Elegir formato: relleno azul, fuente negrita

—¡Listo! Ahora cada vez que un valor supere 5000, se resaltará automáticamente.

Sofía aplicó la regla a Valor_A. Ocho celdas se iluminaron en azul.

—Ocho transacciones de alto valor —murmuró—. ¿Qué tienen de especial?

—Revisa las fechas —sugirió Carlos.

Sofía ordenó los datos por fecha (usando **Ordenar y filtrar**, que ya había aprendido). Las ocho transacciones estaban集中在 en los últimos tres meses de cada año: octubre, noviembre, diciembre.

—Compras de fin de año —dijo—. Tiene sentido. Pero el abuelo hacía compras grandes en diciembre para el inventario del año siguiente...

—Puede ser —respondió Carlos—. O puede ser otra cosa.

---

## Administrar reglas

—Con muchas reglas, el archivo puede volverse un desastre —dijo Carlos—. Por eso existe el **Administrador de reglas de formato condicional**.

**Inicio > Formato condicional > Administrar reglas**

Se abre un panel que muestra todas las reglas aplicadas, su orden de prioridad, y el rango al que afectan. Puedes:
- Editar reglas existentes
- Cambiar el orden (las reglas de arriba tienen prioridad)
- Eliminar reglas
- Ver qué celdas están afectadas

—Es como el centro de control del formato condicional —dijo Sofía.

—Exacto. Y aquí hay un truco importante: cuando tienes reglas que se superponen, la primera en la lista tiene prioridad. Puedes usar las flechas para subir o bajar reglas.

---

### Enigma 1.1: Los valores atípicos

En el archivo secreto, aplica formato condicional con barras de datos a la columna Valor_B. Luego, aplica una escala de color (blanco-rojo) a la columna Valor_A. Finalmente, aplica conjuntos de iconos (flechas) a la columna Valor_C.

¿Qué patrones observas? ¿Hay valores que destacan?

---

### Enigma 1.2: Regla personalizada para fechas

Crea una regla de formato condicional que resalte con relleno amarillo todas las filas donde la fecha sea anterior al 1 de enero de 2008. Pista: necesitarás usar una fórmula en la regla: selecciona "Utilice una fórmula que determine las celdas para aplicar formato" y usa `=$E2<FECHA(2008,1,1)` (asumiendo que la columna Fecha está en E).

¿Cuántas filas anteriores a 2008 hay?

---

### Enigma 1.3: Detectando duplicados con formato condicional

Aplica formato condicional para resaltar valores duplicados en la columna Código. Usa **Formato condicional > Reglas para resaltar celdas > Valores duplicados**.

¿Hay códigos repetidos? Si los hay, ¿qué podría significar?

---

## Lo que aprendiste

- Las **barras de datos** muestran la magnitud de los valores como barras dentro de la celda
- Las **escalas de color** crean mapas de calor para identificar patrones visualmente
- Los **conjuntos de iconos** agregan semáforos, flechas o formas según el valor
- Las **reglas personalizadas** te permiten definir condiciones específicas con fórmulas
- El **Administrador de reglas** organiza y prioriza todas las reglas aplicadas
- El formato condicional es una herramienta de **análisis visual**, no solo decorativa

---

Sofía miró la hoja ahora llena de color, barras y semáforos. Los números ya no eran una pared opaca de datos. Empezaban a contar una historia.

—El abuelo no era de hacer cosas complicadas por gusto —dijo—. Este archivo tiene un propósito. Y voy a descubrirlo.

Carlos sonrió. —Mañana te enseño otra cosa: cómo ponerle reglas a los datos para que no se puedan meter errores. Y tal vez, solo tal vez, encuentres más pistas.

—¿Qué vamos a aprender mañana?

—**Validación de datos**. Por ahora, guarda el archivo y vamos a almorzar. Tu mamá hizo lomo saltado.

Sofía guardó el archivo con un nombre nuevo: *"Investigacion_Secreta_v1.xlsx"*. El misterio apenas comenzaba, pero ya tenía colores, barras y semáforos para guiarla.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
