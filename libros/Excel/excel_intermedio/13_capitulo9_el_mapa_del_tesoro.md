# Capítulo 9: El Mapa del Tesoro

## Tema: Dashboard básico con controles de formulario

---

—Hasta ahora has aprendido muchas herramientas por separado —dijo Carlos la mañana siguiente—: formato condicional, validación, búsquedas, tablas dinámicas, gráficos, análisis de hipótesis. Cada una es poderosa por sí misma.

—Pero juntas deben ser imparables —completó Sofía.

—Exactamente. Y el lugar donde todas se unen es el **dashboard** o **tablero de control**. Es una hoja de resumen que muestra los indicadores más importantes del negocio en un solo vistazo.

—Como el tablero de un carro —dijo Sofía—. Velocidad, combustible, temperatura, todo en un solo lugar.

—Esa es la analogía perfecta. Y como en un carro, los controles deben ser claros, visuales y fáciles de interpretar.

---

## Diseñando el dashboard

—Lo primero es el diseño —dijo Carlos—. Un buen dashboard debe responder tres preguntas:

1. **¿Cómo vamos?** (Indicadores generales)
2. **¿Qué está pasando?** (Tendencias y patrones)
3. **¿Qué debería hacer?** (Alertas y decisiones)

—Vamos a construir el dashboard del taller Mendoza & Hijos.

Carlos abrió una hoja nueva y la llamó "Dashboard".

—Esta será la portada de nuestro análisis —dijo—. Aquí solo pondremos **resúmenes**. Los detalles estarán en otras hojas.

---

## Los elementos del dashboard

**Paso 1: Tarjetas de indicadores clave (KPI)**

En la parte superior, cuatro tarjetas con los números más importantes:

| Ingresos Totales | Egresos Totales | Ganancia Neta | Productividad |
|-----------------|----------------|---------------|---------------|
| S/ 1,856,400 | S/ 1,234,500 | S/ 621,900 | 84.5% |

—Estos son valores calculados con fórmulas que referencian los rangos con nombre que creaste:

```
=SUMA(Ingresos)
=SUMA(Egresos)
=SUMA(Ingresos) - SUMA(Egresos)
=INDICADOR_PRODUCTIVIDAD (basado en Valor_C)
```

—Usa formato condicional para que la ganancia se muestre en verde si es positiva y roja si es negativa.

**Paso 2: Gráfico de tendencia**

Debajo de las tarjetas, inserta el **gráfico combinado** que creaste en el Capítulo 5: ingresos vs egresos por año.

**Paso 3: Tabla dinámica resumida**

Al costado del gráfico, inserta una **tabla dinámica pequeña** que muestre los totales por tipo de código (AX, BX, CX).

**Paso 4: Minigráficos**

En una sección inferior, muestra minigráficos de tendencia para cada año.

**Paso 5: Segmentadores de datos**

Agrega segmentadores para filtrar por año y por tipo de código.

---

## Conectando todo

—La magia del dashboard es que todo está **conectado** —dijo Carlos—. Cuando seleccionas un año en el segmentador, la tabla dinámica, los gráficos y las tarjetas se actualizan automáticamente.

—Pero las tarjetas tienen fórmulas SUMA —objetó Sofía—. Las tablas dinámicas no afectan las fórmulas normales.

—Exacto. Por eso las tarjetas deben usar **funciones de tabla dinámica** o **tablas dinámicas con GETPIVOTDATA**.

La función **GETPIVOTDATA** extrae valores de una tabla dinámica:

```
=GETPIVOTDATA("Suma de Valor_A"; $A$3; "Año"; 2008)
```

—Esta fórmula devuelve la suma de ingresos para 2008, según lo que muestra la tabla dinámica. Si cambias el filtro del segmentador... bueno, aquí el filtro es fijo. Para hacerlo dinámico, referenciarías una celda con el año seleccionado.

—O mejor —dijo Carlos—, puedes usar **Tablas dinámicas con varias celdas de valor** y formatearlas para que parezcan tarjetas. No es elegante, pero funciona.

---

## Controles de formulario

—Para hacer el dashboard realmente interactivo, puedes agregar **controles de formulario** —dijo Carlos—. Estos son botones, barras de desplazamiento, casillas de verificación que controlan valores en tu hoja.

**Insertar controles:** **Desarrollador > Insertar > Controles de formulario**

—Si no ves la pestaña "Desarrollador", actívala: **Archivo > Opciones > Personalizar cinta > Desarrollador**.

Los controles más útiles:

| Control | Función |
|---------|---------|
| **Botón de giro** (Spin Button) | Incrementa/decrementa un valor |
| **Barra de desplazamiento** | Cambia un valor arrastrando |
| **Casilla de verificación** | Activa/desactiva algo (TRUE/FALSE) |
| **Cuadro combinado** | Lista desplegable para seleccionar |

—Agreguemos un **botón de giro** para seleccionar el año —propuso Carlos.

1. Insertar > Botón de giro
2. Haz clic derecho > **Formato de control**
3. Vincular el control a una celda (ej: $Z$1)
4. Configurar: Valor mínimo 2005, Valor máximo 2015, Incremento 1

—Ahora, cuando hagas clic en las flechas, el valor en Z1 cambia. Y puedes usar ese valor en tus fórmulas.

Por ejemplo:

```
=SUMAR.SI(Fechas; ">="&FECHA(Z1;1;1); Ingresos) - SUMAR.SI(Fechas; ">="&FECHA(Z1;1;1); Egresos)
```

—Filtra los datos para mostrar solo el año seleccionado.

Sofía experimentó con el botón de giro. Al hacer clic, los números del dashboard cambiaban.

—¡Es como tener un control remoto para los datos! —exclamó.

---

## Formato del dashboard

—Un dashboard debe ser **visualmente limpio** —dijo Carlos—. Algunas reglas:

1. **Usa una paleta de colores consistente** (2-3 colores máximo)
2. **Menos es más**: no satures el tablero
3. **Jerarquía visual**: lo más importante debe ser lo más grande
4. **Tipografía clara** y tamaños consistentes
5. **Elimina la cuadrícula** de la hoja (Ver > Cuadrícula)

—Y algo importante —agregó—: **protege el dashboard**. Si otros van a usarlo, protege las celdas con fórmulas para que no las borren accidentalmente.

**Revisar > Proteger hoja**. Puedes permitir que los usuarios seleccionen celdas pero no las modifiquen, o solo permitir cambios en celdas específicas.

---

### Enigma 9.1: Crea tu primer dashboard

Construye un dashboard para el taller con:
- Tarjetas de KPI (ingresos, egresos, ganancia)
- Gráfico combinado de ingresos vs egresos
- Tabla dinámica resumida por tipo de código
- Segmentador de datos para filtrar por año

---

### Enigma 9.2: Controles interactivos

Agrega un botón de giro que permita cambiar el año mostrado en las tarjetas KPI. Vincula el control a una celda y usa SUMAR.SI.CONJUNTO para filtrar los datos por año.

---

### Enigma 9.3: Dashboard protegido

Protege tu dashboard con contraseña ("mendoza2026") pero permite que los usuarios puedan usar los segmentadores y los controles de formulario. Pista: en **Proteger hoja**, marca "Usar tablas dinámicas" y "Editar objetos".

---

## Lo que aprendiste

- Un **dashboard** o tablero de control unifica múltiples análisis en una sola vista
- Los **KPI** (Key Performance Indicators) son los indicadores más importantes del negocio
- Los **controles de formulario** (botones de giro, barras, casillas) agregan interactividad
- **GETPIVOTDATA** extrae valores específicos de tablas dinámicas
- Un buen dashboard es **visualmente limpio**, **jerárquico** y **fácil de interpretar**
- **Proteger** el dashboard evita modificaciones accidentales

---

—Con este dashboard, cualquiera puede entender la salud del taller en segundos —dijo Sofía, admirada—. Es como haber creado un cerebro que resume todo.

—Y mañana —dijo Carlos—, vamos a unir todos estos conocimientos para descifrar el misterio completo. Es hora de saber qué escondía tu abuelo.

—¿Crees que estamos listos?

—Sofía, tienes un dashboard que integra formato condicional, validación, búsquedas, tablas dinámicas, gráficos avanzados, rangos con nombre y análisis de hipótesis. Si no estás lista con eso, nadie lo está.

Por primera vez desde que encontró el archivo secreto, Sofía sintió que el control estaba en sus manos.

Y mañana, descubriría la verdad.

---

[Facilito] → Soluciones en el Apéndice al final del libro.
