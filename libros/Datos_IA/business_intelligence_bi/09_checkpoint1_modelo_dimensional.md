# Checkpoint 1: Modelo Dimensional de TechStore

## Objetivo

Has aprendido los fundamentos de BI, arquitectura de datos, modelado dimensional y KPIs. Ahora es momento de aplicar todo: **diseñar e implementar el modelo dimensional de TechStore** como un star schema listo para Power BI.

## Requisitos

- Tener techstore.db en la carpeta `codigos/`
- Python con sqlite3 y pandas

## Paso 1: Crear la base de datos dimensional

Crea el script `codigos/crear_modelo_bi.py` que genere las tablas del star schema:

```python
"""
crear_modelo_bi.py
Construye el modelo dimensional (star schema) de TechStore.
Genera un archivo SQLite listo para Power BI.
"""

import sqlite3
import pandas as pd
from datetime import datetime, timedelta

ORIGEN = "../codigos/techstore.db"
DESTINO = "../codigos/techstore_bi.db"

conn_origen = sqlite3.connect(ORIGEN)
conn_destino = sqlite3.connect(DESTINO)

cursor = conn_destino.cursor()

# --- dim_date ---
print("Creando dim_date...")
cursor.execute("""
    CREATE TABLE dim_date (
        date_sk INTEGER PRIMARY KEY,
        full_date DATE NOT NULL,
        anio INTEGER NOT NULL,
        mes INTEGER NOT NULL,
        mes_nombre TEXT NOT NULL,
        trimestre INTEGER NOT NULL,
        semana INTEGER NOT NULL,
        dia_semana_num INTEGER NOT NULL,
        dia_semana_nombre TEXT NOT NULL,
        es_fin_semana INTEGER NOT NULL
    )
""")

fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2026, 12, 31)
dias = (fecha_fin - fecha_inicio).days + 1

for i in range(dias):
    fecha = fecha_inicio + timedelta(days=i)
    date_sk = int(fecha.strftime("%Y%m%d"))
    cursor.execute("""
        INSERT INTO dim_date VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        date_sk,
        fecha.date().isoformat(),
        fecha.year,
        fecha.month,
        fecha.strftime("%B"),
        (fecha.month - 1) // 3 + 1,
        fecha.isocalendar()[1],
        fecha.weekday() + 1,
        fecha.strftime("%A"),
        1 if fecha.weekday() >= 5 else 0
    ))

print(f"  {dias} días insertados")

# --- dim_customer ---
print("Creando dim_customer...")
df_customers = pd.read_sql_query("SELECT * FROM customers", conn_origen)
cursor.execute("""
    CREATE TABLE dim_customer (
        customer_sk INTEGER PRIMARY KEY,
        customer_id INTEGER,
        name TEXT,
        email TEXT,
        phone TEXT,
        city TEXT,
        country TEXT,
        registration_date DATE
    )
""")
for _, row in df_customers.iterrows():
    cursor.execute("""
        INSERT INTO dim_customer VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row["customer_id"],
        row["customer_id"],
        row["name"],
        row["email"],
        row.get("phone", ""),
        row["city"],
        row.get("country", "USA"),
        row.get("registration_date", "2023-01-01")
    ))

# --- dim_product ---
print("Creando dim_product...")
df_products = pd.read_sql_query("SELECT * FROM products", conn_origen)
cursor.execute("""
    CREATE TABLE dim_product (
        product_sk INTEGER PRIMARY KEY,
        product_id INTEGER,
        name TEXT,
        category TEXT,
        supplier TEXT,
        price REAL
    )
""")
for _, row in df_products.iterrows():
    cursor.execute("""
        INSERT INTO dim_product VALUES (?, ?, ?, ?, ?, ?)
    """, (
        row["product_id"],
        row["product_id"],
        row["name"],
        row["category"],
        row.get("supplier", ""),
        row.get("price", 0)
    ))

# --- dim_employee ---
print("Creando dim_employee...")
df_employees = pd.read_sql_query("SELECT * FROM employees", conn_origen)
cursor.execute("""
    CREATE TABLE dim_employee (
        employee_sk INTEGER PRIMARY KEY,
        employee_id INTEGER,
        name TEXT,
        position TEXT,
        hire_date DATE,
        salary REAL
    )
""")
for _, row in df_employees.iterrows():
    cursor.execute("""
        INSERT INTO dim_employee VALUES (?, ?, ?, ?, ?, ?)
    """, (
        row["employee_id"],
        row["employee_id"],
        row["name"],
        row["position"],
        row.get("hire_date", "2023-01-01"),
        row.get("salary", 0)
    ))

# --- fact_orders ---
print("Creando fact_orders...")
df_orders = pd.read_sql_query("SELECT * FROM orders", conn_origen)
cursor.execute("""
    CREATE TABLE fact_orders (
        order_sk INTEGER PRIMARY KEY,
        date_sk INTEGER NOT NULL,
        customer_sk INTEGER NOT NULL,
        employee_sk INTEGER NOT NULL,
        order_id INTEGER,
        total REAL,
        status TEXT,
        FOREIGN KEY (date_sk) REFERENCES dim_date(date_sk),
        FOREIGN KEY (customer_sk) REFERENCES dim_customer(customer_sk),
        FOREIGN KEY (employee_sk) REFERENCES dim_employee(employee_sk)
    )
""")
for _, row in df_orders.iterrows():
    fecha = pd.to_datetime(row["order_date"])
    date_sk = int(fecha.strftime("%Y%m%d"))
    cursor.execute("""
        INSERT INTO fact_orders (order_sk, date_sk, customer_sk, employee_sk, order_id, total, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        row["order_id"],
        date_sk,
        row["customer_id"],
        row.get("employee_id", 1),
        row["order_id"],
        row["total"],
        row["status"]
    ))

# --- fact_order_items ---
print("Creando fact_order_items...")
df_items = pd.read_sql_query("SELECT * FROM order_items", conn_origen)
cursor.execute("""
    CREATE TABLE fact_order_items (
        order_item_sk INTEGER PRIMARY KEY,
        order_sk INTEGER NOT NULL,
        product_sk INTEGER NOT NULL,
        quantity INTEGER,
        unit_price REAL,
        line_total REAL,
        FOREIGN KEY (order_sk) REFERENCES fact_orders(order_sk),
        FOREIGN KEY (product_sk) REFERENCES dim_product(product_sk)
    )
""")
for _, row in df_items.iterrows():
    cursor.execute("""
        INSERT INTO fact_order_items (order_item_sk, order_sk, product_sk, quantity, unit_price, line_total)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        row["order_item_id"],
        row["order_id"],
        row["product_id"],
        row["quantity"],
        row["unit_price"],
        row["quantity"] * row["unit_price"]
    ))

conn_destino.commit()
conn_origen.close()
conn_destino.close()
print("Modelo BI creado: techstore_bi.db")
```

Ejecútalo:

```bash
python codigos/crear_modelo_bi.py
```

## Paso 2: Validar el modelo

Crea `codigos/validar_modelo_bi.py`:

```python
"""
validar_modelo_bi.py
Valida la integridad del modelo dimensional.
"""

import sqlite3

conn = sqlite3.connect("../codigos/techstore_bi.db")
cursor = conn.cursor()

print("=== Validación del Modelo BI de TechStore ===")
print()

# Tablas y filas
tables = ["dim_date", "dim_customer", "dim_product", "dim_employee",
          "fact_orders", "fact_order_items"]
for table in tables:
    count = cursor.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"  {table}: {count} filas")

# Integridad referencial (fact_orders -> dims)
print()
print("=== Integridad Referencial ===")
checks = [
    ("fact_orders.date_sk -> dim_date", """
        SELECT COUNT(*) FROM fact_orders f
        LEFT JOIN dim_date d ON f.date_sk = d.date_sk
        WHERE d.date_sk IS NULL
    """),
    ("fact_orders.customer_sk -> dim_customer", """
        SELECT COUNT(*) FROM fact_orders f
        LEFT JOIN dim_customer c ON f.customer_sk = c.customer_sk
        WHERE c.customer_sk IS NULL
    """),
    ("fact_order_items.product_sk -> dim_product", """
        SELECT COUNT(*) FROM fact_order_items i
        LEFT JOIN dim_product p ON i.product_sk = p.product_sk
        WHERE p.product_sk IS NULL
    """),
]
for name, query in checks:
    orphans = cursor.execute(query).fetchone()[0]
    status = "OK" if orphans == 0 else f"Huerfanos: {orphans}"
    print(f"  {name}: {status}")

# KPIs básicos
print()
print("=== KPIs Básicos ===")
kpis = [
    ("Total Ingresos", "SELECT ROUND(SUM(total), 2) FROM fact_orders"),
    ("Total Pedidos", "SELECT COUNT(*) FROM fact_orders"),
    ("Ticket Promedio", "SELECT ROUND(AVG(total), 2) FROM fact_orders"),
    ("Clientes Únicos", "SELECT COUNT(DISTINCT customer_sk) FROM fact_orders"),
]
for name, query in kpis:
    value = cursor.execute(query).fetchone()[0]
    print(f"  {name}: {value}")

conn.close()
print()
print("Validación completada.")
```

## Paso 3: Diseñar el dashboard de KPIs

Basado en el modelo dimensional, diseña en papel (o con lápiz) un dashboard con:

1. **4 KPIs principales** (tarjetas): Ingresos, Pedidos, Ticket Promedio, Crecimiento %
2. **Evolución mensual** de ingresos (gráfico de líneas)
3. **Ventas por categoría** (gráfico de barras)
4. **Top 5 productos** (tabla o barras)
5. **Ventas por empleado** (gráfico de barras horizontales)
6. **Filtros**: rango de fechas, categoría de producto, vendedor

## Entregables del Checkpoint 1

- [ ] Script `crear_modelo_bi.py` funcionando y generando `techstore_bi.db`
- [ ] Script `validar_modelo_bi.py` con todas las validaciones OK
- [ ] Modelo dimensional con 4 dimensiones y 2 tablas de hechos
- [ ] Integridad referencial 100% OK
- [ ] KPIs básicos calculados y documentados
- [ ] Diseño del dashboard de KPIs (en papel o digital)

## Preguntas de reflexión

1. ¿Cuántas dimensiones creaste? ¿Crees que falta alguna?
2. ¿Qué diferencias encuentras entre el modelo original (SQLite transaccional) y el star schema?
3. ¿Por qué usamos surrogate keys en lugar de las claves naturales?
4. ¿Qué KPI crees que será más útil para la gerencia de TechStore?

¡Felicidades! Has construido tu primer modelo dimensional. En el Proyecto 2 lo conectarás a Power BI para crear dashboards profesionales.
