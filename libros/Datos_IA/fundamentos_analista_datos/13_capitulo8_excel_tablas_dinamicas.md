# Capítulo 8: Excel — Tablas Dinámicas

## ¿Qué es una tabla dinámica?

Una tabla dinámica (pivot table) es la herramienta más potente de Excel para resumir y analizar datos. Con pocos clics puedes convertir miles de filas en un informe resumido.

En SQL escribes:
```sql
SELECT region, COUNT(*), SUM(total)
FROM ventas GROUP BY region;
```

En Excel, una tabla dinámica hace lo mismo sin escribir código.

## Crear tu primera tabla dinámica

1. Abre `datos_ventas.csv` en Excel
2. Conviértelo en tabla (Ctrl+T)
3. Ve a "Insertar" > "Tabla dinámica"
4. Confirma el rango y elige "Nueva hoja de cálculo"
5. En el panel de campos, arrastra:

   - **Filas**: `region`
   - **Valores**: `total` (arrastra 3 veces)

6. En los valores, cambia la configuración:
   - Primer `total`: Suma → "Ingresos totales"
   - Segundo `total`: Cuenta → "Pedidos"
   - Tercer `total`: Promedio → "Ticket promedio"

Resultado: una tabla que muestra ingresos, pedidos y ticket promedio por región.

## Componentes de una tabla dinámica

```
FILTROS       ──────  Filtran toda la tabla (ej: filtrar por año)
  ↓
COLUMNAS      ──────  Valores que van en columnas (ej: años)
  ↓
FILAS         ──────  Valores que van en filas (ej: regiones)
  ↓
VALORES       ──────  Métricas a calcular (ventas, conteos, etc.)
```

## Arrastrar campos: ejemplos prácticos

### Ejemplo 1: Ventas por región y estado

- **Filas**: `region`
- **Columnas**: `status`
- **Valores**: Suma de `total`

### Ejemplo 2: Clientes por ciudad (conteo)

- **Filas**: `city`
- **Valores**: Conteo de `customer_name`

### Ejemplo 3: Ventas por mes

- **Filas**: `order_date` (agrupado por meses)
- **Valores**: Suma de `total`

## Agrupar fechas en tablas dinámicas

Excel agrupa fechas automáticamente en años, trimestres, meses y días.

1. Arrastra `order_date` a Filas
2. Haz clic derecho en cualquier fecha
3. Selecciona "Agrupar"
4. Elige: Años, Trimestres, Meses
5. Aceptar

Ahora tienes ventas agrupadas por año, trimestre y mes.

## Segmentadores y líneas de tiempo

### Segmentadores: filtros visuales

1. Selecciona la tabla dinámica
2. "Analizar tabla dinámica" > "Insertar segmentador"
3. Elige: `region`, `status`
4. Aparecen botones visuales para filtrar

### Línea de tiempo: filtro temporal

1. "Analizar tabla dinámica" > "Insertar línea de tiempo"
2. Selecciona `order_date`
3. Aparece un control deslizante de tiempo

## Campos calculados

Puedes crear nuevos campos dentro de la tabla dinámica:

1. "Analizar tabla dinámica" > "Campos, elementos y conjuntos" > "Campo calculado"
2. Nombre: "Margen estimado"
3. Fórmula: `= total * 0.3` (asumiendo 30% de margen)

## Formato condicional en tablas dinámicas

1. Selecciona los valores en la tabla dinámica
2. "Inicio" > "Formato condicional"
3. Elige: "Barras de datos", "Escalas de color" o "Conjuntos de iconos"

Ejemplo: aplica barras de datos a la columna de ingresos para ver visualmente qué región vende más.

## Actualizar datos fuente

Cuando los datos cambian:

1. Haz clic derecho en la tabla dinámica
2. "Actualizar"
3. O: "Datos" > "Actualizar todo"

Si añades filas al origen, expande el rango antes de actualizar.

## Ejercicios del Capítulo 8

Carga `datos_ventas.csv` y crea una tabla dinámica para cada ejercicio.

1. Crea una tabla dinámica que muestre el total de ventas por región.
2. Añade el conteo de pedidos y el ticket promedio a la tabla anterior.
3. Crea una tabla dinámica que muestre ventas por mes (agrupa fechas).
4. Usa un segmentador para filtrar por estado (status).
5. Crea una tabla con región en filas y status en columnas. ¿Qué región tiene más pedidos completados?
6. ¿Cuántos clientes hay en cada ciudad? Usa conteo de customer_name.
7. Agrupa las ventas por año. ¿Cómo ha evolucionado el negocio?
8. Aplica formato condicional con barras de datos a los ingresos por región.
9. Crea un campo calculado que muestre el IVA (21%) de cada pedido.
10. ¿Cuál es el mes con mayores ventas en 2025?

## Checklist de autoevaluación

- [ ] Sé crear una tabla dinámica desde un rango de datos
- [ ] Sé arrastrar campos a filas, columnas y valores
- [ ] Sé cambiar el tipo de cálculo (suma, conteo, promedio)
- [ ] Sé agrupar fechas en tablas dinámicas
- [ ] Sé usar segmentadores y líneas de tiempo
- [ ] Sé crear campos calculados
- [ ] Sé aplicar formato condicional
