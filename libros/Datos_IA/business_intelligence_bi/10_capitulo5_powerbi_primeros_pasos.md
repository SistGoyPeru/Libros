# Capítulo 5: Power BI Desktop — Primeros Pasos

## ¿Qué es Power BI?

Power BI es la plataforma de Business Intelligence de Microsoft. Está compuesta por:

| Componente | Qué es | Coste |
|-----------|--------|-------|
| **Power BI Desktop** | App de escritorio para crear modelos y dashboards | Gratuito |
| **Power BI Service** | Portal cloud para publicar, compartir y colaborar | Gratuito (licencia Pro / Premium de pago) |
| **Power BI Mobile** | Apps para iOS y Android | Gratuito |
| **Power BI Report Builder** | Creador de reportes paginados | Gratuito |
| **Power BI Embedded** | Integración en apps propias | Por uso |

En este proyecto nos enfocamos en **Power BI Desktop**.

## Instalación

1. Ve a https://powerbi.microsoft.com/desktop
2. Descarga e instala Power BI Desktop
3. Abre la aplicación

### Pantalla inicial

Al abrir Power BI Desktop verás:

- **Panel de navegación** (izquierda): paneles Reporte, Datos, Modelo
- **Lienzo central**: donde construyes visualizaciones
- **Panel de visualizaciones**: tipos de gráficos, campos, filtros
- **Panel de campos**: lista de tablas y columnas de tu modelo
- **Barra de herramientas**: cinta de opciones con pestañas

### Las 3 vistas de Power BI

| Vista | Icono | Para qué sirve |
|-------|-------|----------------|
| **Reporte** | 📊 | Crear y diseñar visualizaciones |
| **Datos** | 📋 | Ver y explorar datos en tabla |
| **Modelo** | 🔗 | Gestionar relaciones entre tablas |

## Conectar a TechStore

Vamos a conectar Power BI a nuestro star schema:

1. En la cinta de opciones: "Obtener datos" → "SQL Server" o "Más..."
2. Selecciona **ODBC** o **SQLite** (necesitarás el conector SQLite ODBC)
3. Alternativa más simple: importar desde CSV

### Opción recomendada: Conectar a SQLite

Power BI no tiene conector nativo a SQLite. Usaremos un archivo CSV temporal en su lugar, o mejor aún: **Datos desde Excel**.

### Opción práctica: Datos desde CSV

Exporta cada tabla del star schema a CSV:

```sql
-- En SQLite, exportar cada tabla a CSV
.headers on
.mode csv
.once dim_date.csv
SELECT * FROM dim_date;
```

O mejor, desde Python:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("techstore_bi.db")
tables = ["dim_date", "dim_customer", "dim_product", "dim_employee",
          "fact_orders", "fact_order_items"]

for table in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    df.to_csv(f"{table}.csv", index=False)
    print(f"{table}: {len(df)} filas exportadas")
conn.close()
```

En Power BI:
1. "Obtener datos" → "Texto/CSV"
2. Selecciona cada archivo CSV
3. Haz clic en "Cargar"

### Opción avanzada: Power Query + ODBC

Si tienes el driver ODBC para SQLite, puedes conectarte directamente:

1. "Obtener datos" → "ODBC"
2. Selecciona "SQLite3 Datasource"
3. Navega a `techstore_bi.db`

## Crear relaciones en el modelo

1. Ve a la **Vista Modelo** (icono de diagrama a la izquierda)
2. Arrastra para crear relaciones entre:
   - `fact_orders[date_sk]` → `dim_date[date_sk]`
   - `fact_orders[customer_sk]` → `dim_customer[customer_sk]`
   - `fact_orders[employee_sk]` → `dim_employee[employee_sk]`
   - `fact_order_items[order_sk]` → `fact_orders[order_sk]`
   - `fact_order_items[product_sk]` → `dim_product[product_sk]`

3. Configura cada relación como:
   - **Dirección**: Unidireccional (de dimensión a hecho)
   - **Cardinalidad**: Muchos a uno (*:1)
   - **Cruzada**: Aplica filtro en ambas direcciones NO (excepto si necesitas)

## Primeros gráficos

### Tarjeta de Ingresos Totales

1. Selecciona el visual "Tarjeta" (card)
2. Arrastra `fact_orders[total]` al campo "Campos"
3. Power BI automáticamente hace SUM

### Gráfico de líneas: Ingresos por mes

1. Selecciona "Gráfico de líneas"
2. Eje X: `dim_date[full_date]` (o `dim_date[anio_mes]`)
3. Eje Y: `fact_orders[total]` (SUM)

### Gráfico de barras: Ventas por categoría

1. Selecciona "Gráfico de barras"
2. Eje Y: `dim_product[category]`
3. Eje X: `fact_orders[total]` (SUM)

## Guardar el archivo

1. Archivo → Guardar como → `TechStore_BI.pbix`
2. El archivo .pbix contiene el modelo, los datos y las visualizaciones

## Ejercicios

1. Instala Power BI Desktop si no lo tienes
2. Conecta las 6 tablas del star schema de TechStore a Power BI
3. Crea las relaciones en el modelo y verifica la cardinalidad
4. Crea una tarjeta con el total de pedidos (COUNT de order_sk)
5. Crea un gráfico de líneas con ingresos por mes
6. ¿Qué diferencia ves entre la Vista Reporte, Datos y Modelo?
7. ¿Para qué sirve la dirección de filtro en las relaciones?
8. Agrega una segmentación de datos (slicer) para filtrar por año
9. Crea un gráfico de barras con ventas por categoría
10. Guarda tu archivo como .pbix
