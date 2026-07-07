# Capítulo 6: Modelado de Datos en Power BI

## El modelo es el corazón del dashboard

En Power BI, el modelo de datos determina:
- Qué cálculos son posibles
- Qué tan rápido responden las visualizaciones
- Qué filtros afectan a qué medidas

Un modelo mal diseñado produce medidas incorrectas y dashboards lentos.

## Tipos de modelos en Power BI

### Import (Importación)

Los datos se copian a la memoria de Power BI. Rápido, pero limitado a RAM disponible.

```
Ventajas: velocidad, funcionalidad completa de Power Query y DAX
Desventajas: límite de RAM (1 GB en Power BI Desktop / Pro)
Ideal para: datos < 1 GB, dashboards interactivos
```

### DirectQuery

Power BI traduce las consultas al lenguaje de la fuente (SQL).

```
Ventajas: datos siempre actualizados, sin límite de tamaño
Desventajas: más lento, limitaciones en DAX y Power Query
Ideal para: BigQuery, SQL Server, datos grandes en tiempo real
```

### Composite Model

Mezcla tablas Import y DirectQuery en el mismo modelo.

```
Ventajas: lo mejor de ambos mundos
Desventajas: complejidad, ciertas limitaciones
Ideal para: modelos avanzados
```

Para TechStore, usaremos **Import** (los datos caben en RAM).

## Cardinalidad de relaciones

| Tipo | Símbolo | Ejemplo | Descripción |
|------|---------|---------|-------------|
| Muchos a 1 | *:1 | fact_orders → dim_date | Muchos pedidos tienen una fecha |
| 1 a Muchos | 1:* | dim_date → fact_orders | Una fecha tiene muchos pedidos |
| 1 a 1 | 1:1 | dim_customer → fact_orders (raro) | Un cliente por fila |
| Muchos a Muchos | *:* | Con tabla puente | Casos avanzados |

**Regla de oro del modelado**: todas las tablas de hechos se relacionan con las dimensiones en *:1. Las dimensiones no se relacionan entre sí (tablas huérfanas en el modelo).

## Dirección de filtro (Cross Filter Direction)

| Dirección | Efecto | Cuándo usarla |
|-----------|--------|---------------|
| **Simple** (← o →) | La dimensión filtra al hecho | Siempre por defecto |
| **Ambas** (↔) | También el hecho filtra a la dimensión | Solo cuando es necesario (cuidado) |

### Ejemplo de filtro bidireccional

Si `fact_orders` → `dim_product` y queremos filtrar `dim_product` por `dim_employee`:

```
dim_employee → fact_orders → dim_product
                (bidireccional)
```

## Tablas puente (Bridge Tables)

A veces necesitas una relación muchos a muchos. Ejemplo: un producto puede tener múltiples categorías o un cliente múltiples direcciones.

```sql
-- Tabla puente: producto-categoría
CREATE TABLE bridge_product_category (
    product_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (product_id, category_id)
);
```

En Power BI:
- `dim_product` *:* `bridge_product_category` *:* `dim_category`
- Ambas relaciones deben ser unidireccionales

## Jerarquías

Power BI permite crear jerarquías dentro de una dimensión:

```
📍 dim_date
   ├── Año
   │   ├── Trimestre
   │   │   ├── Mes
   │   │   │   └── Día
   │   │   └── ...
   │   └── ...
   └── ...

📍 dim_product
   ├── Categoría
   │   └── Producto
   └── ...
```

Para crear una jerarquía en Power BI:
1. En el panel Campos, haz clic derecho en `dim_date[anio]`
2. "Nueva jerarquía"
3. Agrega `trimestre`, `mes`, `full_date` en ese orden

## Columnas calculadas vs Medidas

| | Columna Calculada | Medida |
|---|---|---|
| **Cuándo** | Al cargar datos | Al consultar |
| **Almacenamiento** | En RAM | No almacena (calcula en consulta) |
| **Contexto** | Fila por fila | Dinámico (filtros, segmentaciones) |
| **Uso típico** | Columnas derivadas (edad, categoría) | Agregaciones (SUM, AVG, COUNT) |
| **Rendimiento** | Consume RAM | Más eficiente |

### Cuándo usar cada una

Usa **columna calculada** cuando:
- Necesitas un valor por fila (ej: nombre completo)
- La columna se usará como filtro o segmentación
- Necesitas ordenar por una columna personalizada

Usa **medida** cuando:
- Necesitas una agregación (SUM, COUNT, AVERAGE)
- El valor depende del contexto de filtro
- Quieres cálculos dinámicos (YTD, vs mes anterior)

## Ejemplo: Crear columna calculada

```dax
-- En dim_product: margen estimado (columna)
Margen Estimado = dim_product[price] * 0.4

-- En dim_customer: nombre completo (columna)
Nombre Completo = dim_customer[name]

-- En fact_orders: rango de ticket (columna)
Rango Ticket = SWITCH(
    TRUE(),
    fact_orders[total] >= 1000, "Premium",
    fact_orders[total] >= 500, "Alto",
    fact_orders[total] >= 200, "Medio",
    "Bajo"
)
```

## Ejemplo: Crear medidas básicas

```dax
-- Total ingresos (medida)
Ingresos Totales = SUM(fact_orders[total])

-- Total pedidos (medida)
Total Pedidos = COUNTROWS(fact_orders)

-- Ticket promedio (medida)
Ticket Promedio = AVERAGE(fact_orders[total])

-- Clientes únicos (medida)
Clientes Activos = DISTINCTCOUNT(fact_orders[customer_sk])
```

## Buenas prácticas de modelado

1. **Star schema siempre**: evita snowflake en Power BI
2. **Nombres claros**: usa nombres descriptivos en español
3. **Oculta columnas clave**: en el panel Campos, oculta surrogate keys (date_sk, customer_sk)
4. **Organiza carpetas**: agrupa medidas en carpetas
5. **Fecha única**: una sola tabla de calendario para todo el modelo
6. **Evita bidireccional**: salvo que sea estrictamente necesario

## Ejercicios

1. ¿Cuál es la diferencia entre Import y DirectQuery? ¿Cuál usas para TechStore?
2. Crea una jerarquía de fecha en dim_date (Año → Trimestre → Mes → Día)
3. Crea una columna calculada "Categoría de Precio" en dim_product
4. ¿Cuándo usarías una columna calculada vs una medida?
5. Define 3 medidas básicas: Total Pedidos, Ingreso Promedio, Clientes Únicos
6. Oculta las columnas date_sk, customer_sk, employee_sk en el panel Campos
7. Organiza tus medidas en una carpeta llamada "KPIs Principales"
8. ¿Qué es la cardinalidad *:* y cómo se maneja en Power BI?
9. Crea una columna en dim_date que indique "Fin de Semana" (Sí/No)
10. ¿Por qué el star schema es la recomendación estándar en Power BI?
