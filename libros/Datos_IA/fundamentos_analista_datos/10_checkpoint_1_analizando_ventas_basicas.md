# Checkpoint 1: Analizando Ventas Básicas

## Proyecto integrador del Proyecto 1

En este checkpoint vas a combinar todo lo aprendido en los capítulos 1-5 para realizar un análisis completo de las ventas de TechStore usando las tres herramientas.

## Parte 1: SQL — Explora los datos

Abre DB Browser, conecta `techstore.db` y responde:

```sql
-- 1.1 ¿Cuántos pedidos hay en total?
SELECT COUNT(*) FROM orders;

-- 1.2 ¿Cuánto es el total de ventas?
SELECT ROUND(SUM(total), 2) FROM orders;

-- 1.3 ¿Cuál es el ticket promedio?
SELECT ROUND(AVG(total), 2) FROM orders;

-- 1.4 ¿Cuántos pedidos por estado?
SELECT status, COUNT(*) AS cantidad
FROM orders
GROUP BY status;

-- 1.5 ¿Cuál es el pedido más caro y el más barato?
SELECT MAX(total) AS maximo, MIN(total) AS minimo FROM orders;

-- 1.6 ¿Cuántos productos hay por categoría?
SELECT category_id, COUNT(*) AS cantidad
FROM products
GROUP BY category_id
ORDER BY cantidad DESC;

-- 1.7 ¿Cuáles son los 5 productos más caros?
SELECT name, price FROM products ORDER BY price DESC LIMIT 5;

-- 1.8 ¿Cuántos clientes hay por región?
SELECT region, COUNT(*) AS cantidad
FROM customers
GROUP BY region
ORDER BY cantidad DESC;
```

## Parte 2: Excel — Analiza las ventas

1. Importa `datos_ventas.csv` a Excel y conviértelo en tabla
2. Calcula:
   - Total de ventas: `=SUMA(tabla[total])`
   - Promedio por pedido: `=PROMEDIO(tabla[total])`
   - Pedido máximo: `=MAX(tabla[total])`
   - Pedido mínimo: `=MIN(tabla[total])`
   - Conteo de pedidos: `=CONTAR(tabla[total])`
3. Filtra por región "Madrid" y calcula el total de ventas de Madrid
4. Filtra por estado "Completado" y calcula el total
5. ¿Qué porcentaje representan los pedidos completados sobre el total?

## Parte 3: Python — Calcula métricas

Crea un archivo `analisis_ventas.py`:

```python
# Análisis básico de ventas TechStore

print("=== MÉTRICAS DE TECHSTORE ===\n")

# Datos del negocio
ingresos = 1250000.50
gastos = 875000.00
clientes = 250
productos = 509
empleados = 25
pedidos = 6000
cancelados = 450
devueltos = 120

# Cálculos
beneficio = ingresos - gastos
margen = (beneficio / ingresos) * 100
pedidos_completados = pedidos - cancelados - devueltos
tasa_completados = (pedidos_completados / pedidos) * 100
ingreso_por_cliente = ingresos / clientes
ingreso_por_pedido = ingresos / pedidos
productos_por_empleado = productos / empleados

# Resultados
print(f"Ingresos:              {ingresos:>12,.2f}€")
print(f"Gastos:                {gastos:>12,.2f}€")
print(f"Beneficio:             {beneficio:>12,.2f}€")
print(f"Margen:                {margen:>11.1f}%")
print(f"Clientes:              {clientes:>12}")
print(f"Pedidos totales:       {pedidos:>12}")
print(f"Pedidos completados:   {pedidos_completados:>12}")
print(f"Tasa de completados:   {tasa_completados:>11.1f}%")
print(f"Ingreso por cliente:   {ingreso_por_cliente:>12.2f}€")
print(f"Ingreso por pedido:    {ingreso_por_pedido:>12.2f}€")
```

## Parte 4: Preguntas de negocio

Basándote en tu análisis, responde:

1. ¿Cuántos pedidos se completan vs se cancelan? ¿Es buena la tasa?
2. ¿Cuál es el ticket promedio? ¿Te parece alto o bajo para una tienda de electrónica?
3. ¿Qué región tiene más clientes? ¿Por qué crees?
4. ¿Cuál es la categoría con más productos?
5. ¿Qué métrica crees que es más importante para el negocio?

## Entregable

Guarda tu análisis en una carpeta `proyecto_1` con:
- `consultas.sql` — Tus consultas SQL
- `analisis_ventas.xlsx` — Tu archivo Excel con fórmulas
- `analisis_ventas.py` — Tu script Python

## Checklist de autoevaluación del Proyecto 1

- [ ] Sé consultar datos con SELECT, WHERE, ORDER BY, LIMIT
- [ ] Sé filtrar con operadores de comparación, IN, BETWEEN, LIKE
- [ ] Sé importar CSV a Excel y formatear datos
- [ ] Sé usar tablas de Excel (Ctrl+T) y fórmulas básicas
- [ ] Sé crear variables y usar tipos de datos en Python
- [ ] Sé usar f-strings y operadores aritméticos
- [ ] Completé el análisis integrado en las 3 herramientas
- [ ] Guardé mi proyecto en una carpeta organizada
