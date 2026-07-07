# Capítulo 10: La Gran Apertura

## Repaso y Proyecto Integrador

---

Pasaron tres meses desde aquel primer día en que Sofía abrió Excel sin saber ni por dónde empezar. Ahora, el taller "Mendoza & Hijos" no solo había sobrevivido: estaba prosperando.

Los pedidos del Hotel Miraflores estaban casi terminados. La Sra. María Fernanda había aceptado el presupuesto y encargado muebles adicionales. La Feria de la Madera había generado contactos que seguían dando frutos.

Pero Sofía quería dar un paso más. Quería presentar un **Informe Mensual Completo** que mostrara la salud del taller: ingresos, gastos, ganancias, productividad, tendencias. Algo que cualquier inversor o banquero pudiera entender de un vistazo.

—Voy a crear el informe definitivo —le anunció a Don Manuel—. El informe que mi abuelo siempre quiso tener y nunca pudo hacer.

Don Manuel se sentó a su lado, y los dos aprendices —Carlos y Miguel— se acercaron también. Era el momento de poner todo junto.

---

## El proyecto integrador: Informe Mensual "Mendoza & Hijos"

Sofía abrió un nuevo libro de Excel. Lo llamó "Informe_Mensual_Completo.xlsx". Creó las siguientes hojas:

1. **Resumen Ejecutivo** — La vista general, el "panel de control"
2. **Inventario** — Datos del inventario con formato y condicional
3. **Ventas** — Registro de ventas del mes
4. **Costos** — Desglose de costos de producción
5. **Gastos** — Gastos operativos del taller
6. **Gráficos** — Visualizaciones clave

### Hoja 1: Resumen Ejecutivo

Sofía diseñó esta hoja como un tablero de control. En la parte superior, una fila con indicadores clave (KPIs):

| A | B | C | D |
|---|---|---|---|
| **Indicador** | **Valor** | **Meta** | **Estado** |
| Ventas del mes | S/ 28,450.00 | S/ 25,000.00 | ¡Meta superada! |
| Costos totales | S/ 18,200.00 | S/ 17,500.00 | Por ajustar |
| Ganancia neta | S/ 10,250.00 | S/ 7,500.00 | ¡Excelente! |
| Pedidos pendientes | 8 | 5 | Mayor capacidad necesaria |
| Días de entrega prom. | 12 | 10 | Mejorando |
| Satisfacción cliente | 4.8/5.0 | 4.5/5.0 | ¡Clientes felices! |

Las fórmulas de esta hoja tomaban datos de las otras hojas:

**Ventas del mes (B1):** =SUM(Ventas!B2:B31)
**Costos totales (B2):** =SUM(Costos!B2:B31) + SUM(Gastos!B2:B31)
**Ganancia neta (B3):** =B1-B2

### Hoja 2: Inventario

Sofía copió el inventario del Capítulo 1 y le aplicó todas las mejoras aprendidas:

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Producto** | **Cant.** | **Unidad** | **P. Unit.** | **Proveedor** | **Calidad** | **F. Ingreso** | **Ubicación** |
| Madera Cedro | 50 | tablas | S/ 45.00 | Maderas Pérez | A | 15/01/2026 | Estante 1 |
| Madera Roble | 30 | tablas | S/ 62.00 | Maderas Pérez | A | 15/01/2026 | Estante 1 |
| Madera Pino | 100 | tablas | S/ 22.00 | El Maderero | B | 20/01/2026 | Estante 2 |
| Triplay | 40 | planchas | S/ 35.00 | Maderas Pérez | C | 20/01/2026 | Estante 3 |
| Barniz mate | 10 | galones | S/ 28.00 | Pinturas Unidas | - | 10/02/2026 | Anaquel 1 |
| Barniz brillante | 8 | galones | S/ 32.00 | Pinturas Unidas | - | 10/02/2026 | Anaquel 1 |
| Tornillos #10 | 500 | unidades | S/ 0.50 | Ferretería El Tornillo | - | 05/02/2026 | Caja 1 |
| Tornillos #8 | 300 | unidades | S/ 0.40 | Ferretería El Tornillo | - | 05/02/2026 | Caja 1 |
| Lija fina | 200 | hojas | S/ 1.20 | Ferretería El Tornillo | - | 05/02/2026 | Anaquel 2 |
| Lija gruesa | 150 | hojas | S/ 0.80 | Ferretería El Tornillo | - | 05/02/2026 | Anaquel 2 |
| Pegamento | 12 | botellas | S/ 15.00 | Pinturas Unidas | - | 10/02/2026 | Anaquel 1 |

**Formato aplicado:**
- Moneda en columna D
- Fechas en formato largo en columna G
- Formato condicional en columna B (rojo < 20, amarillo 20-50, verde > 50)
- Color de fondo por tipo en columna A (si aplica)
- Bordes completos

### Hoja 3: Ventas

Sofía registró las ventas del mes con detalle:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| **Fecha** | **Producto** | **Cliente** | **Cant.** | **P. Unit.** | **Total** |
| 01/06/2026 | Silla cedro | Sr. García | 2 | S/ 150.00 | S/ 300.00 |
| 02/06/2026 | Mesa roble | Sra. López | 1 | S/ 350.00 | S/ 350.00 |
| 03/06/2026 | Estante triplay | Hotel Miraflores | 5 | S/ 180.00 | S/ 900.00 |
| ... | ... | ... | ... | ... | ... |

**Fórmula en F:** =D2*E2

**Totales al final:**
=SUM(F2:F31) → S/ 28,450.00
=AVERAGE(F2:F31) → S/ 948.33 (venta promedio por transacción)
=COUNT(F2:F31) → 30 transacciones en el mes
=MAX(F2:F31) → S/ 2,500.00 (venta más alta)
=MIN(F2:F31) → S/ 80.00 (venta más baja)

### Hoja 4: Costos

Sofía detalló los costos de cada pedido:

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| **Pedido** | **Madera** | **Barniz** | **Tornillos** | **Mano Obra** | **Otros** | **Total** |
| PED-001 | S/ 90.00 | S/ 7.00 | S/ 3.00 | S/ 35.00 | S/ 5.00 | =SUM(B2:F2) |
| PED-002 | S/ 186.00 | S/ 14.00 | S/ 8.00 | S/ 70.00 | S/ 10.00 | =SUM(B3:F3) |
| PED-003 | S/ 350.00 | S/ 35.00 | S/ 15.00 | S/ 175.00 | S/ 25.00 | =SUM(B4:F4) |
| ... | ... | ... | ... | ... | ... | ... |

### Hoja 5: Gastos

Los gastos operativos del taller:

| A | B | C | D |
|---|---|---|---|
| **Fecha** | **Concepto** | **Categoría** | **Monto** |
| 01/06/2026 | Alquiler local | Fijo | S/ 2,500.00 |
| 05/06/2026 | Electricidad | Servicio | S/ 380.00 |
| 07/06/2026 | Agua | Servicio | S/ 120.00 |
| 10/06/2026 | Compra madera cedro | Materia prima | S/ 2,250.00 |
| ... | ... | ... | ... |

### Hoja 6: Gráficos

Sofía creó cuatro gráficos para el informe:

**Gráfico 1: Ventas diarias del mes (Líneas)**
Mostraba la evolución de las ventas día a día. Se veían picos los fines de semana y una tendencia general al alza.

**Gráfico 2: Ventas por producto (Columnas)**
Las sillas dominaban, seguidas de mesas y estantes. Un gráfico de barras que confirmaba lo que Sofía ya sabía.

**Gráfico 3: Distribución de gastos (Circular)**
Mostraba qué porcentaje del presupuesto se iba en cada categoría:
- Materia prima: 45%
- Mano de obra: 30%
- Gastos fijos: 15%
- Servicios: 10%

**Gráfico 4: Comparativa mes actual vs. mes anterior (Columnas)**
Un antes y después que demostraba el crecimiento del taller bajo la gestión de Sofía.

---

## El momento de la verdad

Sofía reunió a Don Manuel, Carlos y Miguel frente a la computadora.

—Señores —dijo, con el nerviosismo de quien va a presentar algo importante—, les presento el primer Informe Mensual Completo de "Mendoza & Hijos".

Hizo clic en la hoja de Resumen Ejecutivo. Los indicadores brillaban en la pantalla.

—Este mes —continuó—, vendimos S/ 28,450. Esto es un 13.8% más que nuestra meta. Nuestra ganancia neta fue de S/ 10,250, que es un 36.7% de margen sobre ventas.

Don Manuel silbó suavemente.

—Pero lo más importante —dijo Sofía, pasando al gráfico de tendencias— es que estamos creciendo. Cada semana vendemos más que la anterior. La tendencia es positiva.

Señaló el gráfico de distribución de gastos.

—Eso sí, estamos gastando demasiado en materia prima. Necesitamos negociar mejores precios con los proveedores. Esa será mi prioridad el próximo mes.

Carlos, el aprendiz más joven, levantó la mano.

—Sofía, ¿cómo aprendiste todo esto? Hace tres meses no sabías ni encender Excel.

Sofía sonrió y miró el cuaderno de su abuelo, que descansaba junto al monitor.

—Tuve un buen maestro —dijo—. Aunque ya no esté físicamente, me dejó todo lo que necesitaba saber.

---

## El cierre del círculo

Esa noche, después de que todos se fueron, Sofía se quedó sola en el taller. La luz de la luna se filtraba por las ventanas, iluminando las herramientas colgadas en las paredes.

Abrió el cuaderno de su abuelo en la primera página. Allí, escritas con letra firme, estaban las palabras con las que Don Rafael comenzó su viaje con Excel:

*"Hoy mi nieta me regaló una computadora. Dice que tiene un programa llamado Excel. No sé para qué sirve, pero si ella dice que es importante, aprenderé. Por ella. Para dejarle algo mejor de lo que recibí."*

Sofía sintió que los ojos se le llenaban de lágrimas. Su abuelo había aprendido Excel por ella. Para dejarle un legado. Y ahora, ese legado había salvado el taller.

Tomó su laptop y creó una nueva hoja en el libro. La llamó "Legado". En la celda A1, escribió:

*"Para quien venga después de mí:*
*Este taller no es solo madera y clavos. Es sueños, esfuerzo y amor.*
*Los números no son fríos: cuentan historias de personas que trabajaron, que compraron, que confiaron.*
*Excel es solo una herramienta. Lo importante es lo que construyes con ella.*
*— Sofía Mendoza, sucesora de Don Rafael Mendoza."*

Guardó el archivo. Apagó la computadora. Y al salir del taller, miró el letrero que su abuelo había tallado cuarenta años atrás:

**MENDOZA & HIJOS**
*Carpintería Fina desde 1986*

—No voy a defraudarte, abuelo —dijo en voz baja—. El legado continúa.

---

## El proyecto final para ti

### Enigma 10.1: Crea tu propio informe mensual

Ahora es tu turno. Crea un libro de Excel con las siguientes hojas y datos (puedes inventarlos):

**Hoja: Resumen**
- 5 indicadores clave (ventas, costos, ganancias, clientes, productividad)
- Cada indicador debe usar una fórmula que tome datos de otras hojas

**Hoja: Inventario**
- Mínimo 10 productos
- Columnas: Producto, Cantidad, Precio Unitario, Proveedor, Calidad
- Formato condicional en cantidad (rojo/amarillo/verde)
- Formato de moneda en precios

**Hoja: Ventas**
- Mínimo 20 transacciones
- Columnas: Fecha, Producto, Cliente, Cantidad, Precio Unitario, Total
- Fórmula para Total (=Cantidad * Precio)
- Funciones SUM, AVERAGE, MAX, MIN al final

**Hoja: Gastos**
- Mínimo 10 gastos
- Categorías: Fijo, Variable, Materia prima
- Subtotal por categoría usando SUM con filtro

**Hoja: Gráficos**
- Gráfico de líneas: Tendencia de ventas
- Gráfico de columnas: Ventas por producto
- Gráfico circular: Distribución de gastos

### Enigma 10.2: Configuración profesional

Una vez creado el informe:

1. Configura la impresión para cada hoja (orientación, márgenes, encabezados)
2. Agrega encabezados con el nombre de tu empresa (real o ficticia)
3. Agrega pies de página con números de página
4. Ajusta la escala para que quepa en páginas legibles
5. Exporta a PDF (Archivo > Exportar > Crear PDF)

### Enigma 10.3: El mensaje final

Así como Sofía dejó un mensaje en la hoja "Legado", crea una hoja llamada "Reflexión" y escribe un párrafo sobre:

- Qué aprendiste en este libro
- Cómo crees que Excel puede ayudarte en tu vida o trabajo
- Qué meta te pones para seguir aprendiendo

---

## Lo que aprendiste en este libro

| Concepto | Capítulo | Aplicación en el taller |
|----------|----------|----------------------|
| Interfaz y navegación | Cap 1 | Conocer las herramientas disponibles |
| Tipos de datos y selección | Cap 2 | Organizar el inventario correctamente |
| Fórmulas básicas | Cap 3 | Calcular costos y ganancias |
| Referencias relativas/absolutas | Cap 4 | Calcular IVA y tipo de cambio |
| Formato de celdas | Cap 5 | Presentación profesional de datos |
| Funciones SUM, AVERAGE, etc. | Cap 6 | Análisis de ventas y promedios |
| Gráficos | Cap 7 | Visualizar tendencias y comparaciones |
| Ordenar y filtrar | Cap 8 | Organizar el catálogo de la feria |
| Configuración de impresión | Cap 9 | Presupuestos profesionales |
| Proyecto integrador | Cap 10 | Informe mensual completo |
