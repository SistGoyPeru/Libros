import sqlite3, csv, os, random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('es_ES')
random.seed(42)
fake.seed_instance(42)

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, 'techstore.db')

def generar_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            price REAL NOT NULL,
            cost REAL NOT NULL,
            stock INTEGER NOT NULL,
            supplier TEXT,
            created_at TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );

        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            city TEXT,
            region TEXT,
            registration_date TEXT
        );

        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            position TEXT,
            hire_date TEXT
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            employee_id INTEGER,
            order_date TEXT NOT NULL,
            status TEXT NOT NULL,
            total REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        );

        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    ''')

    categorias = [
        'Portátiles', 'Smartphones', 'Tablets', 'Auriculares',
        'Teclados', 'Ratones', 'Monitores', 'Impresoras',
        'Almacenamiento', 'Accesorios', 'Componentes', 'Redes',
        'Software', 'Cámaras', 'Altavoces'
    ]
    cur.executemany('INSERT OR IGNORE INTO categories (id, name) VALUES (?, ?)',
                    enumerate(categorias, 1))

    productos = []
    for cat_id in range(1, len(categorias) + 1):
        cat_name = categorias[cat_id - 1]
        for _ in range(random.randint(25, 45)):
            name = fake.unique.word().capitalize() + ' ' + fake.random_element(['Pro', 'Air', 'Max', 'Lite', 'Ultra', 'X', 'Z', 'Plus', 'Elite', 'Essential'])
            price = round(random.uniform(9.99, 1999.99), 2)
            cost = round(price * random.uniform(0.4, 0.75), 2)
            stock = random.randint(0, 500)
            supplier = fake.company()
            created = fake.date_between(start_date='-3y', end_date='-1d')
            productos.append((None, name, cat_id, price, cost, stock, supplier, created.isoformat()))
    cur.executemany('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?)', productos)

    regiones = ['Andalucía', 'Cataluña', 'Madrid', 'Comunidad Valenciana', 'Galicia',
                'País Vasco', 'Castilla y León', 'Canarias', 'Castilla-La Mancha',
                'Aragón', 'Murcia', 'Baleares', 'Asturias', 'Navarra', 'Extremadura']
    ciudades = {r: fake.city() for r in regiones}

    clientes = []
    for _ in range(250):
        region = random.choice(regiones)
        city = ciudades[region]
        reg_date = fake.date_between(start_date='-4y', end_date='-30d')
        clientes.append((None, fake.first_name(), fake.last_name(), fake.email(), fake.phone_number(),
                        city, region, reg_date.isoformat()))
    cur.executemany('INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?)', clientes)

    puestos = ['Vendedor', 'Vendedor Senior', 'Representante de Ventas', 'Key Account Manager', 'Gerente de Ventas']
    empleados = []
    for _ in range(25):
        hire = fake.date_between(start_date='-6y', end_date='-60d')
        empleados.append((None, fake.first_name(), fake.last_name(), fake.email(),
                         random.choice(puestos), hire.isoformat()))
    cur.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)', empleados)

    estados = ['Completado', 'Completado', 'Completado', 'Completado', 'Pendiente', 'Cancelado', 'Envío']
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 6, 30)

    orders_data = []
    items_data = []
    for order_id in range(1, 6001):
        customer_id = random.randint(1, 250)
        employee_id = random.randint(1, 25)
        order_date = fake.date_time_between(start_date=start_date, end_date=end_date)
        status = random.choice(estados)
        orders_data.append((order_id, customer_id, employee_id,
                           order_date.isoformat(), status, 0.0))

        num_items = random.randint(1, 6)
        order_total = 0.0
        for _ in range(num_items):
            product_id = random.randint(1, len(productos))
            qty = random.randint(1, 3)
            cur.execute('SELECT price FROM products WHERE id = ?', (product_id,))
            price = cur.fetchone()[0]
            unit_price = round(price, 2)
            order_total += unit_price * qty
            items_data.append((None, order_id, product_id, qty, unit_price))

        cur.execute('UPDATE orders SET total = ? WHERE id = ?',
                   (round(order_total, 2), order_id))

    cur.executemany('''INSERT INTO orders (id, customer_id, employee_id, order_date, status, total)
                       VALUES (?, ?, ?, ?, ?, ?)''', orders_data)
    cur.executemany('INSERT INTO order_items VALUES (?, ?, ?, ?, ?)', items_data)

    conn.commit()
    conn.close()
    print(f'Base de datos creada: {DB_PATH}')

def exportar_csvs():
    conn = sqlite3.connect(DB_PATH)
    tablas = [
        ('ventas', '''
            SELECT o.id AS order_id, o.order_date, o.status, o.total,
                   c.first_name || ' ' || c.last_name AS customer_name,
                   c.city, c.region,
                   e.first_name || ' ' || e.last_name AS employee_name
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            JOIN employees e ON o.employee_id = e.id
            ORDER BY o.order_date
        '''),
        ('clientes', 'SELECT * FROM customers'),
        ('productos', '''
            SELECT p.*, c.name AS category_name
            FROM products p
            JOIN categories c ON p.category_id = c.id
        '''),
        ('detalles_ventas', '''
            SELECT oi.id, oi.order_id, o.order_date, o.customer_id,
                   p.name AS product_name, c.name AS category_name,
                   oi.quantity, oi.unit_price, (oi.quantity * oi.unit_price) AS line_total
            FROM order_items oi
            JOIN orders o ON oi.order_id = o.id
            JOIN products p ON oi.product_id = p.id
            JOIN categories c ON p.category_id = c.id
            ORDER BY o.order_date
        '''),
    ]
    for nombre, query in tablas:
        cur = conn.execute(query)
        rows = cur.fetchall()
        cols = [desc[0] for desc in cur.description]
        path = os.path.join(BASE, f'datos_{nombre}.csv')
        with open(path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(cols)
            writer.writerows(rows)
        print(f'CSV exportado: {path} ({len(rows)} filas)')
    conn.close()

def generar_ejemplos():
    for i, sql in enumerate([
        "-- Ejemplo 1: Top 10 productos más vendidos\n"
        "SELECT p.name AS producto, SUM(oi.quantity) AS unidades_vendidas, "
        "ROUND(SUM(oi.quantity * oi.unit_price), 2) AS ingresos\n"
        "FROM order_items oi\n"
        "JOIN products p ON oi.product_id = p.id\n"
        "GROUP BY p.name\n"
        "ORDER BY unidades_vendidas DESC\n"
        "LIMIT 10;",

        "-- Ejemplo 2: Ventas por región\n"
        "SELECT c.region, COUNT(DISTINCT o.id) AS pedidos, "
        "ROUND(SUM(o.total), 2) AS ingresos_totales, "
        "ROUND(AVG(o.total), 2) AS ticket_promedio\n"
        "FROM orders o\n"
        "JOIN customers c ON o.customer_id = c.id\n"
        "GROUP BY c.region\n"
        "ORDER BY ingresos_totales DESC;",

        "-- Ejemplo 3: Clientes con mayor gasto\n"
        "SELECT c.first_name || ' ' || c.last_name AS cliente, "
        "COUNT(o.id) AS pedidos, ROUND(SUM(o.total), 2) AS gasto_total\n"
        "FROM customers c\n"
        "JOIN orders o ON c.id = o.customer_id\n"
        "GROUP BY c.id\n"
        "HAVING gasto_total > 1000\n"
        "ORDER BY gasto_total DESC;",
    ]):
        path = os.path.join(BASE, f'ejemplo_{i+1}.sql')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(sql)
        print(f'Ejemplo SQL creado: {path}')

if __name__ == '__main__':
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f'Base existente eliminada: {DB_PATH}')
    generar_db()
    exportar_csvs()
    generar_ejemplos()
    print('\n¡Todo listo! Los archivos están en la carpeta codigos/')
