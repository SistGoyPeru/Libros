# Capítulo 8: ¿Qué Pasaría Si...?

## Tema: Análisis de hipótesis — buscar objetivo, tabla de datos, escenarios

---

—¿Sabes cuál es la diferencia entre un negocio que sobrevive y uno que prospera? —preguntó Carlos, mientras ambos miraban los números del taller en la pantalla.

—¿El dinero? —aventuró Sofía.

—No exactamente. La información. Un negocio que prospera es aquel que puede responder preguntas como: "¿Qué pasa si las ventas bajan un 20%?" o "¿Cuánto necesito vender para ganar 100,000 soles al año?".

—Esas son preguntas difíciles.

—Excel tiene herramientas específicas para responderlas. Se llaman **herramientas de análisis de hipótesis** (What-If Analysis). Y hay tres tipos principales:

1. **Buscar objetivo** (Goal Seek): Para encontrar el valor necesario para alcanzar una meta
2. **Tabla de datos** (Data Table): Para ver múltiples resultados variando uno o dos valores
3. **Administrador de escenarios** (Scenario Manager): Para comparar diferentes conjuntos de valores

---

## Buscar objetivo: ¿Cuánto necesito vender?

—Empecemos con algo práctico —dijo Carlos—. Tú quieres que el taller genere 200,000 soles de ganancia este año. Actualmente tenemos estos datos:

| Concepto | Valor |
|----------|-------|
| Precio promedio por silla | 250 |
| Costo de materiales por silla | 120 |
| Costos fijos mensuales (alquiler, sueldos, etc.) | 8,000 |
| Sillas vendidas al mes (promedio) | 40 |
| Ganancia mensual actual | (250-120)*40 - 8000 = -2,800 |

—¿Estamos perdiendo dinero? —preguntó Sofía alarmada.

—Sí. 2,800 soles al mes. Pero no es porque el negocio no funcione, sino porque no estamos vendiendo suficiente volumen. Necesitamos descubrir **cuántas sillas vender para alcanzar una meta**.

**Buscar objetivo** resuelve esto:

1. Crea una celda para la ganancia mensual:
   `=(Precio - CostoMaterial) * Cantidad - CostosFijos`

2. Ve a **Datos > Análisis de hipótesis > Buscar objetivo**

3. Configura:
   - **Definir la celda:** la celda de la ganancia mensual
   - **Con el valor:** 0 (punto de equilibrio)
   - **Para cambiar la celda:** la celda de la cantidad

Excel ejecutó el cálculo:

—Para alcanzar el punto de equilibrio (ganancia = 0), necesitas vender aproximadamente **62 sillas al mes** —dijo Carlos.

—Eso es 22 sillas más de las que vendemos ahora —dijo Sofía—. Es un aumento del 55%.

—Correcto. Y para ganar 200,000 al año (16,667 al mes), necesitarías vender...

Carlos configuró otro Buscar objetivo con valor 16,667.

—... **212 sillas al mes**.

—Eso es imposible —dijo Sofía—. No tenemos capacidad para fabricar 212 sillas al mes.

—Entonces necesitas ajustar otras variables: subir el precio, reducir costos, o ambas. Buscar objetivo te ayuda a explorar esas opciones.

---

## Tabla de datos: Explorando múltiples escenarios

—Buscar objetivo cambia un solo valor. Pero si quieres ver **múltiples posibilidades a la vez**, necesitas una **tabla de datos**.

—¿Como una matriz de resultados?

—Exactamente. Puedes crear una tabla que muestre la ganancia para diferentes combinaciones de precios y cantidades.

**Paso 1:** Crea una celda con la fórmula de ganancia (la celda de resultado).

**Paso 2:** En una columna, escribe diferentes cantidades (30, 40, 50, 60, 70...). En una fila, escribe diferentes precios (200, 250, 300, 350).

**Paso 3:** Selecciona toda la matriz incluyendo la fila y columna de valores.

**Paso 4:** **Datos > Análisis de hipótesis > Tabla de datos**.

**Paso 5:** En "Celda de fila", selecciona la celda del precio. En "Celda de columna", selecciona la celda de la cantidad.

Excel llenó la tabla con los resultados:

| Precio | 30 | 40 | 50 | 60 | 70 | 80 |
|--------|-----|-----|-----|-----|-----|-----|
| **200** | -5,600 | -4,800 | -4,000 | -3,200 | -2,400 | -1,600 |
| **250** | -4,100 | -2,800 | -1,500 | -200 | 1,100 | 2,400 |
| **300** | -2,600 | -800 | 1,000 | 2,800 | 4,600 | 6,400 |
| **350** | -1,100 | 1,200 | 3,500 | 5,800 | 8,100 | 10,400 |

—Con esta tabla —dijo Carlos—, puedes ver todas las combinaciones posibles. Por ejemplo, si vendes 50 sillas a 300 soles, ganas 1,000 soles al mes. Si vendes 80 sillas a 350, ganas 10,400.

—Pero vender 80 sillas a 350 suena difícil...

—Tal vez. Pero ahora tienes **datos** para tomar decisiones, no solo corazonadas.

—¿Y si quiero variar tres variables? —preguntó Sofía.

—La tabla de datos solo maneja dos variables. Para más, necesitas el Administrador de escenarios.

---

## Administrador de escenarios: El "qué pasaría si" completo

—El **Administrador de escenarios** te permite guardar diferentes conjuntos de valores y compararlos uno al lado del otro.

**Paso 1:** Define las celdas que cambiarán (variables): Precio, CostoMaterial, CostosFijos, Cantidad.

**Paso 2:** Ve a **Datos > Análisis de hipótesis > Administrador de escenarios**.

**Paso 3:** Crea el primer escenario:
- **Nombre:** "Actual"
- **Celdas cambiantes:** selecciona las cuatro celdas
- **Valores:** los valores actuales

**Paso 4:** Agrega más escenarios:

| Escenario | Precio | CostoMaterial | CostosFijos | Cantidad |
|-----------|--------|--------------|-------------|----------|
| Actual | 250 | 120 | 8,000 | 40 |
| Optimista | 350 | 100 | 7,000 | 70 |
| Pesimista | 200 | 150 | 9,000 | 25 |
| Meta 2026 | 300 | 110 | 8,000 | 60 |

—Una vez creados los escenarios, puedes **Mostrar** cada uno para ver cómo cambia la ganancia. O puedes generar un **Resumen** que los compare todos:

**Paso 5:** Haz clic en **Resumen**. Elige "Resumen de escenarios". Excel crea una nueva hoja con todos los escenarios comparados.

| Celda | Actual | Optimista | Pesimista | Meta 2026 |
|-------|--------|-----------|-----------|-----------|
| Ganancia | -2,800 | 10,500 | -9,250 | 3,400 |

—Así puedes ver de un vistazo qué funciona y qué no —concluyó Carlos.

---

## Aplicación al misterio

—¿Y cómo me ayuda esto con el archivo del abuelo? —preguntó Sofía.

—Porque los números del archivo secreto no solo son registros del pasado —respondió Carlos—. Son también un **plan para el futuro**.

—¿Qué quieres decir?

—Mira las transferencias (tipo CX). Siguen un patrón: cada tres meses, una transferencia de una cantidad específica a una cuenta que no hemos identificado. Y el monto es consistente: 5,000 soles cada trimestre.

—5,000 al trimestre... 20,000 al año...

—Durante 10 años. Eso es 200,000 soles. ¿A dónde crees que fueron?

—No sé... ¿Una cuenta de ahorros?

—O algo más. Tal vez el abuelo estaba **ahorrando para algo grande**. Y ese archivo es el registro de esos ahorros. Las columnas Valor_A, Valor_B, Valor_C podrían ser diferentes fuentes de ingreso que alimentaban esa cuenta.

—¿Como un fondo de expansión?

—Exactamente. Y con las herramientas de análisis de hipótesis, podemos proyectar cuánto hay ahora si ese dinero se invirtió con cierto interés.

Sofía abrió una nueva hoja y escribió:

```
Ahorro trimestral: 5,000
Tasa de interés estimada: 4% anual
Período: 10 años
Fórmula: =VF(4%/4; 10*4; -5000)
```

—La función VF (Valor Futuro) nos da el total: aproximadamente 245,000 soles.

—245,000 soles —repitió Sofía—. Eso es suficiente para... no sé, ¿expandir el taller? ¿Comprar maquinaria nueva?

—O abrir una nueva sucursal. O financiar la educación de alguien. O... cualquier cosa que tu abuelo considerara importante.

---

### Enigma 8.1: Punto de equilibrio del taller

Usando Buscar objetivo, determina cuántas unidades debe vender el taller al mes para alcanzar el punto de equilibrio (ganancia = 0) si:
- Precio por silla: S/300
- Costo de material: S/130
- Costos fijos mensuales: S/9,500

---

### Enigma 8.2: Tabla de datos de rentabilidad

Crea una tabla de datos de dos variables que muestre la ganancia mensual para:
- Precios: 220, 250, 280, 310, 340 (en la fila)
- Cantidades: 30, 45, 60, 75, 90 (en la columna)

¿Cuál es la combinación que da la mayor ganancia?

---

### Enigma 8.3: Escenarios del archivo secreto

Crea tres escenarios para interpretar los datos del archivo secreto:
- **Escenario A:** Valor_A son ingresos totales, Valor_B son costos operativos (80% de A)
- **Escenario B:** Valor_A son ventas, Valor_B son compras de insumos, Valor_C es margen
- **Escenario C:** Valor_A, B, C son tres cuentas bancarias diferentes que se consolidan

¿Qué escenario parece más plausible según los datos que has analizado?

---

## Lo que aprendiste

- **Buscar objetivo** encuentra el valor necesario en una celda para alcanzar un resultado específico
- Las **tablas de datos** muestran resultados para múltiples combinaciones de una o dos variables
- El **Administrador de escenarios** guarda y compara diferentes conjuntos de valores
- **VF (Valor Futuro)** calcula el valor de una inversión con pagos periódicos
- El análisis de hipótesis convierte datos históricos en **proyecciones para la toma de decisiones**

---

—245,000 soles —repitió Sofía mientras guardaba el archivo—. Si el abuelo ahorró eso durante 10 años, debía tener un plan.

—Tal vez el plan eras tú —dijo Carlos en voz baja.

—¿Yo?

—Tu abuelo siempre dijo que querías que estudiaras administración. Que tenías talento para los números. Tal vez este archivo no es un misterio que debas resolver, sino una **herencia** que debas recibir.

Sofía sintió un nudo en la garganta. La idea de que su abuelo hubiera estado planeando algo para ella, incluso después de su partida, la llenaba de una emoción difícil de describir.

—Mañana voy a ver al señor Montenegro —dijo finalmente—. Necesito respuestas.

—Yo te acompaño —dijo Carlos—. Pero antes, hay algo más que quiero mostrarte. Cómo unir todo esto en un **dashboard** que cuente la historia completa.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
