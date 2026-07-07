# Capítulo 9: Dashboard Inteligente

—Andrea, quiero un dashboard ejecutivo —dijo Diego una mañana de febrero—. Algo que pueda ver en mi teléfono desde cualquier lugar. Los KPIs principales de la empresa en tiempo real.

Andrea asintió. Ya había estado planeando esto.

—Lo tengo, Diego. Pero necesito tu ayuda para definir los KPIs críticos.

—Los de siempre —respondió Diego—. Ventas, márgenes, inventario, cuentas por cobrar. Pero quiero que sea visual, interactivo, y que se actualice solo.

Andrea sabía que Copilot podía ayudarla, pero un dashboard de nivel ejecutivo requería más que solo gráficos bonitos. Necesitaba pensar en la experiencia del usuario, la actualización de datos y la claridad de la información.

Se sentó con su laptop y comenzó.

*"Copilot, necesito diseñar un dashboard ejecutivo de ventas. Requisitos:*

1. *Indicadores principales (tarjetas KPI):*
   - *Ventas Totales (mes actual vs mes anterior)*
   - *Margen Bruto %*
   - *Crecimiento Interanual*
   - *Top Producto Más Vendido*

2. *Gráficos:*
   - *Ventas por mes (línea, últimos 12 meses)*
   - *Ventas por sucursal (barra horizontal)*
   - *Composición de ventas por categoría (anillo)*
   - *Top 10 productos (barra)*

3. *Interactividad:*
   - *Segmentadores de datos por: Mes, Sucursal, Categoría*
   - *Los gráficos deben actualizarse al cambiar los filtros*

4. *Formato:*
   - *Fondo blanco, texto oscuro*
   - *Colores: azul corporativo #1A3A5C, verde #2ECC71, rojo #E74C3C*
   - *Fuente limpia y profesional*
   - *Formato condicional en KPIs: verde si meta cumplida, rojo si no"*

Copilot comenzó a trabajar. En pocos minutos, tenía la estructura básica del dashboard.

—Buen inicio —murmuró Andrea—, pero quiero más.

Continuó refinando:

*"Copilot, agrega:*
- *Una línea de meta en el gráfico de ventas mensuales*
- *Indicadores de tendencia (flechas arriba/abajo) en cada KPI*
- *Un tooltip que muestre el detalle al pasar el mouse sobre cada gráfico"*

Tras varias iteraciones, el dashboard estaba listo. Andrea lo presentó a Diego, quien quedó impresionado.

—Esto es exactamente lo que necesitaba —dijo, desplazándose por los paneles en su tableta—. ¿Puedo compartirlo con la junta?

—Por supuesto. Y se actualiza automáticamente cada semana.

---

### Conceptos Clave: Dashboards con Copilot

Copilot puede acelerar significativamente la creación de dashboards, pero el diseño y la estructura conceptual siguen siendo responsabilidad tuya.

#### Elementos de un Buen Dashboard

1. **Claridad**: Un vistazo debe comunicar el mensaje principal
2. **Jerarquía**: KPIs principales arriba, detalle abajo
3. **Contexto**: Los números solo tienen significado en comparación
4. **Interactividad**: El usuario debe poder explorar los datos
5. **Actualización**: Los datos deben estar frescos

#### KPIs que Copilot Puede Calcular

- *"Calcula el crecimiento mes a mes de las ventas"*
- *"Muestra el margen bruto como porcentaje"*
- *"Calcula el ticket promedio por cliente"*
- *"Muestra la rotación de inventario en días"*
- *"Calcula el ratio de cobranza (DSO)"*
- *"Muestra el cumplimiento de meta por sucursal"*

#### Interactividad con Segmentadores

Los segmentadores permiten filtrar datos en tablas dinámicas y gráficos:

- *"Agrega un segmentador de datos para la columna 'Sucursal'"*
- *"Conecta el segmentador de 'Mes' a todos los gráficos del dashboard"*
- *"Crea una línea de tiempo para filtrar por fechas"*
- *"Agrega un menú desplegable que cambie la métrica mostrada"*

#### Formato Condicional en Dashboards

- *"Aplica formato condicional a los KPIs: verde si se cumple la meta, rojo si no"*
- *"Usa iconos de flechas para mostrar la tendencia: ↑ si crece, ↓ si decrece, → si estable"*
- *"Resalta la barra del producto más vendido en color dorado"*
- *"Aplica escala de colores a la tabla de sucursales"*

#### Actualización Automática

Para que el dashboard se actualice solo:

1. Conecta los datos a Power Query (origen de datos dinámico)
2. Configura actualización programada (Excel 365)
3. O usa Power BI para dashboards en tiempo real

---

### Ejercicio 9.1: Tu Dashboard Personal

Crea un dashboard personal con tus propios datos (pueden ser finanzas personales, ventas, lo que sea). Pídele a Copilot:

*"Quiero crear un dashboard personal con:*
1. *4 tarjetas KPI con los indicadores más importantes*
2. *Un gráfico de tendencia de los últimos 6 meses*
3. *Un gráfico de distribución*
4. *Segmentadores para filtrar*

*Ayúdame a estructurarlo y generarlo paso a paso."*

### Ejercicio 9.2: Refinar un Dashboard Existente

Toma un dashboard que ya tengas o crea uno simple. Pídele a Copilot mejoras:

*"Analiza mi dashboard actual y sugiere:*
1. *3 mejoras visuales*
2. *1 indicador adicional que debería incluir*
3. *1 forma de hacerlo más interactivo*
4. *1 mejora de rendimiento o actualización"*
