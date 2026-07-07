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

print(f"  {dias} dias insertados")

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
