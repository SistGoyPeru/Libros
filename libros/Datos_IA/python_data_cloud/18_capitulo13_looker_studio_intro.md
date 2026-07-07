# Capítulo 13: Looker Studio — Conectando Datos Cloud

## ¿Qué es Looker Studio?

Looker Studio (antes Google Data Studio) es una herramienta gratuita de **business intelligence** y **visualización de datos** de Google. Te permite crear dashboards interactivos conectados a diversas fuentes de datos, incluyendo BigQuery.

Características principales:
- **Gratuito**: sin coste para el usuario (solo pagas las consultas a BigQuery)
- **Colaborativo**: edición en tiempo real como Google Docs
- **Conectores nativos**: BigQuery, Google Sheets, Cloud Storage, y 1000+ conectores
- **Interactivo**: filtros cruzados, drill-down, parámetros
- **Programático**: puedes automatizar informes con la API

## Looker Studio vs otras herramientas

| Herramienta | Precio | Curva aprendizaje | Ideal para |
|-------------|--------|------------------|------------|
| Looker Studio | Gratis | Baja | Dashboards rápidos, equipos pequeños/medianos |
| Tableau | $$$ | Media | BI corporativo, visualizaciones complejas |
| Power BI | $$ | Media | Ecosistema Microsoft |
| Metabase | Gratis (self-hosted) | Baja | Dashboards internos, equipos técnicos |
| Grafana | Gratis | Media | Series de tiempo, monitoreo |

Looker Studio es la opción ideal para empezar: cero inversión, integración directa con BigQuery, y resultados profesionales en horas.

## Conectar BigQuery a Looker Studio

### Paso 1: Crear un informe nuevo

1. Ve a https://lookerstudio.google.com
2. Haz clic en "Informe en blanco"
3. Se abre el panel de "Añadir datos al informe"

### Paso 2: Seleccionar conector BigQuery

1. En la lista de conectores, busca y selecciona **BigQuery**
2. Autoriza el acceso si es la primera vez
3. Configura la conexión:
   - **Proyecto**: `techstore-analytics` (o tu Project ID)
   - **Dataset**: `techstore`
   - **Tabla**: `orders`
4. Haz clic en "Añadir"

### Paso 3: Primer gráfico

1. En el panel derecho, selecciona "Gráfico de series temporales"
2. Configura:
   - **Dimensión**: `order_date` (eje X)
   - **Métrica**: `total` → SUM (eje Y)
3. En la barra de herramientas, ajusta el periodo a "Últimos 12 meses"
4. ¡Ya tienes tu primer gráfico conectado a BigQuery!

## Consultas personalizadas en Looker Studio

En lugar de conectar una tabla completa, puedes escribir SQL personalizado:

1. Al añadir datos, selecciona **BigQuery** → "Consulta personalizada"
2. Escribe tu SQL:

```sql
SELECT
  DATE_TRUNC(order_date, MONTH) AS mes,
  COUNT(*) AS pedidos,
  ROUND(SUM(total), 2) AS ingresos,
  ROUND(AVG(total), 2) AS ticket_promedio
FROM techstore.orders
GROUP BY mes
ORDER BY mes;
```

3. Looker Studio tratará el resultado como una tabla virtual

## Componentes básicos de Looker Studio

### Dimensiones y métricas

- **Dimensión**: campo descriptivo/categórico (fecha, nombre, ciudad)
- **Métrica**: campo numérico que se agrega (SUM, COUNT, AVG, MIN, MAX)

### Tipos de gráficos

| Gráfico | Cuándo usarlo |
|---------|---------------|
| Serie temporal | Evolución en el tiempo |
| Barra | Comparar categorías |
| Torta/Donut | Proporciones (pocas categorías) |
| Tabla | Datos detallados |
| Tabla pivotante | Resumen por 2 dimensiones |
| Mapa | Datos geográficos |
| Tarjeta de puntuación | Un número clave (KPI) |
| Medidor | Progreso vs objetivo |
| Diagrama de dispersión | Correlación entre 2 métricas |
| Gráfico de área apilada | Composición en el tiempo |

## Diseñando tu primer dashboard

Vamos a crear un dashboard de ventas para TechStore:

### Panel 1: KPIs principales

Añade 4 tarjetas de puntuación:

| Tarjeta | Métrica | Agregación |
|---------|---------|------------|
| Ingresos totales | total | SUM |
| Pedidos totales | order_id | COUNT |
| Ticket promedio | total | AVG |
| Clientes únicos | customer_id | COUNT DISTINCT |

### Panel 2: Evolución mensual

Gráfico de series temporales:
- **Dimensión**: order_date (día)
- **Métrica**: total → SUM
- **Desglose**: category (línea por categoría)

### Panel 3: Top productos

Gráfico de barras:
- **Dimensión**: product_name (requiere JOIN con products)
- **Métrica**: quantity → SUM
- **Orden**: descendente
- **Límite**: 10

### Panel 4: Mapa de clientes

Gráfico de mapa:
- **Dimensión**: city (requiere JOIN con customers)
- **Métrica**: total → SUM
- **Estilo**: burbujas proporcionales

## Filtros en Looker Studio

Los filtros permiten segmentar los datos sin modificar las consultas:

### Filtro a nivel de informe

1. En el menú, "Añadir un control" → "Selector de periodo"
2. Configura el rango de fechas
3. Todos los gráficos conectados se actualizan automáticamente

### Filtro a nivel de gráfico

1. Selecciona un gráfico
2. En propiedades → "Filtro" → "Añadir filtro"
3. Ejemplo: `category = 'Portátiles'`

### Filtro por control desplegable

1. "Añadir un control" → "Lista desplegable"
2. Dimensión: `category`
3. Los usuarios pueden seleccionar categorías para filtrar

## Compartir dashboards

1. Haz clic en "Compartir" (arriba a la derecha)
2. Opciones:
   - **Personas específicas**: invita por email (requiere edición o solo lectura)
   - **Cualquiera con el enlace**: público o privado
3. También puedes **incrustar** el informe en una web (opción "Incrustar")

## Ejercicios

1. Crea un informe en Looker Studio y conéctalo a BigQuery (tabla orders)
2. Añade un gráfico de series temporales con ventas por día
3. Crea un gráfico de barras con las 5 categorías más vendidas
4. ¿Qué diferencia hay entre una dimensión y una métrica?
5. Añade un filtro de fecha a tu dashboard y verifica que los gráficos se actualicen
6. Crea una tarjeta de puntuación que muestre el total de clientes únicos
7. Conecta una consulta personalizada (SQL) en lugar de una tabla completa
8. Añade un mapa con las ventas por ciudad
9. Comparte tu informe como "solo lectura" con un compañero
10. ¿Qué ventajas tiene Looker Studio frente a crear gráficos con matplotlib?
