# Capítulo 1: El Ecosistema del Analista de Datos

## TechStore: tu primer caso real

TechStore es una cadena de tiendas de electrónica con presencia en toda España. Venden portátiles, smartphones, tablets y accesorios tanto en tiendas físicas como online. Como analista de datos, tu misión será ayudar al equipo a responder preguntas de negocio usando datos reales.

A lo largo de este libro trabajarás con tres herramientas:

- **SQL** para extraer datos de la base de datos TechStore
- **Excel** para analizar y visualizar datos
- **Python** para automatizar y escalar tus análisis

## Configuración del entorno

### Instalar DB Browser for SQLite

SQLite es una base de datos ligera y autónoma. No necesita servidor. Todo está en un solo archivo.

1. Ve a https://sqlitebrowser.org
2. Descarga e instala DB Browser for SQLite
3. Abre el archivo `codigos/techstore.db` que viene con este libro

### Instalar Python

1. Ve a https://python.org/downloads
2. Descarga Python 3.12 o superior
3. Durante la instalación, marca "Add Python to PATH"
4. Verifica la instalación abriendo una terminal y escribiendo:

```
python --version
```

### Instalar VS Code

1. Ve a https://code.visualstudio.com
2. Descarga e instala Visual Studio Code
3. Instala las siguientes extensiones:
   - Python (Microsoft)
   - SQLite Viewer
   - Excel Viewer

### Archivos del libro

Todos los archivos están en la carpeta `codigos/`:

| Archivo | Descripción |
|---------|-------------|
| `techstore.db` | Base de datos SQLite completa |
| `datos_ventas.csv` | 6000 pedidos en formato CSV |
| `datos_clientes.csv` | 250 clientes |
| `datos_productos.csv` | 509 productos con categorías |
| `datos_detalles_ventas.csv` | 21,118 líneas de detalle |

## Estructura de la base de datos TechStore

La base de datos tiene 5 tablas principales:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  customers   │     │    orders    │     │  employees  │
│─────────────│     │──────────────│     │─────────────│
│ id          │────>│ customer_id  │     │ id          │
│ first_name  │     │ employee_id  │<────│ first_name  │
│ last_name   │     │ order_date   │     │ last_name   │
│ email       │     │ status       │     │ position    │
│ city        │     │ total        │     │ hire_date   │
│ region      │     └──────┬───────┘     └─────────────┘
└─────────────┘            │
                           │
                    ┌──────┴───────┐     ┌─────────────┐
                    │  order_items  │     │  products   │
                    │──────────────│     │─────────────│
                    │ order_id     │     │ id          │
                    │ product_id   │────>│ name        │
                    │ quantity     │     │ category_id │
                    │ unit_price   │     │ price       │
                    └──────────────┘     │ cost        │
                                         │ stock       │
                                         └─────────────┘
```

## Primeros pasos con DB Browser

1. Abre DB Browser for SQLite
2. Haz clic en "Open Database" y selecciona `techstore.db`
3. Ve a la pestaña "Browse Data"
4. Selecciona cada tabla para explorar sus datos

Tómate 5 minutos para explorar las tablas. Mira qué columnas tiene cada una. Familiarízate con los datos.

## Ejercicios del Capítulo 1

1. Abre la base de datos TechStore en DB Browser. ¿Cuántas tablas ves?
2. ¿Cuántos registros tiene la tabla `products`?
3. ¿Cuántos clientes hay en la tabla `customers`?
4. ¿Qué columnas tiene la tabla `orders`?
5. ¿Cuál es el rango de fechas de los pedidos? (mira la columna `order_date`)
6. ¿Cuántos empleados trabajan en TechStore?
7. ¿Cuántas categorías de productos hay?
8. Abre `datos_ventas.csv` en Excel. ¿Cuántas filas tiene?
9. ¿Cuál es la diferencia entre un archivo `.db` y un archivo `.csv`?
10. ¿Por qué crees que SQLite es más adecuado que Excel para consultar millones de filas?

## Checklist de autoevaluación

- [ ] Instalé DB Browser for SQLite y abrí techstore.db
- [ ] Instalé Python 3.12+
- [ ] Instalé VS Code con las extensiones recomendadas
- [ ] Exploraé las 5 tablas de la base de datos
- [ ] Abrí los archivos CSV en Excel
- [ ] Entiendo la diferencia entre tablas relacionadas
