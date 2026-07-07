# Capítulo 4: Excel — Importar y Transformar Datos

## Excel como herramienta de análisis

Excel es la herramienta más utilizada por analistas de datos en todo el mundo. Aunque no es tan potente como SQL o Python para grandes volúmenes, es perfecta para:

- Análisis rápidos y exploratorios
- Visualización de datos
- Presentación de resultados a negocio
- Limpieza y transformación de datos pequeños

Un analista competente usa Excel a diario, combinado con SQL y Python.

## Importar datos a Excel

### Desde CSV

1. Abre Excel
2. Ve a "Datos" > "Obtener datos" > "Desde archivo" > "Desde CSV"
3. Selecciona `datos_ventas.csv` de la carpeta `codigos/`
4. Excel detectará automáticamente el separador y los tipos de datos
5. Haz clic en "Cargar"

### Desde texto con pegado especial

Otra forma común es copiar datos de un sistema y pegarlos en Excel:

1. Copia los datos (Ctrl+C)
2. En Excel, selecciona la celda A1
3. Pega con "Pegado especial" > "Texto" o simplemente Ctrl+V

## La estructura de una hoja de cálculo

Excel organiza los datos en:

- **Filas**: cada fila es un registro
- **Columnas**: cada columna es un campo
- **Celdas**: intersección de fila y columna (ej: A1, B2, C10)

En nuestro archivo `datos_ventas.csv`:

| Fila | order_id | order_date | status | total | customer_name | city | region | employee_name |
|------|----------|------------|--------|-------|---------------|------|--------|---------------|
| 1 | 1 | 2024-03-15 | Completado | 1250.50 | Ana García | Madrid | Madrid | Carlos Ruiz |
| 2 | 2 | 2024-03-15 | Pendiente | 89.99 | Luis Pérez | Barcelona | Cataluña | María López |

## Formato básico de celdas

### Números

Selecciona las celdas y usa:

- **Ctrl+Shift+1**: Número con separador de miles
- **Ctrl+Shift+4**: Moneda (€)
- **Ctrl+Shift+5**: Porcentaje
- **Ctrl+Shift+3**: Fecha

O desde la cinta: "Inicio" > "Número" > selecciona el formato.

### Texto

- **Negrita**: Ctrl+N
- **Cursiva**: Ctrl+K
- **Alinear texto**: izquierda, centro, derecha
- **Ajustar texto**: "Inicio" > "Alinear" > "Ajustar texto"

### Colores y bordes

- **Color de relleno**: "Inicio" > "Fuente" > cubo de pintura
- **Color de fuente**: "Inicio" > "Fuente" > A
- **Bordes**: "Inicio" > "Fuente" > bordes

## Filtros y ordenación

### Autofiltro

1. Selecciona cualquier celda dentro de los datos
2. Ctrl+Shift+L o "Datos" > "Filtro"
3. Aparecen flechas en cada encabezado
4. Haz clic en una flecha para filtrar por valor, color o condición

```excel
Filtro rápido: selecciona una región específica
→ Solo verás ventas de esa región
```

### Ordenar

1. Selecciona una celda en la columna a ordenar
2. "Datos" > "AZ" (ascendente) o "ZA" (descendente)
3. O: "Datos" > "Ordenar" para múltiples niveles

## Tablas de Excel (Ctrl+T)

Convertir un rango en "Tabla" da superpoderes:

1. Selecciona cualquier celda dentro de los datos
2. Ctrl+T (o "Insertar" > "Tabla")
3. Asegúrate de que "Mi tabla tiene encabezados" está marcado

**Ventajas de las tablas**:
- Filtros automáticos
- El formato se mantiene al añadir filas
- Las referencias se actualizan solas
- Las fórmulas se auto-rellenan

## Fórmulas básicas

### SUMA

```excel
=SUMA(D2:D101)  -- Suma de la columna total (D)
```

### PROMEDIO

```excel
=PROMEDIO(D2:D101)  -- Promedio de los totales
```

### CONTAR

```excel
=CONTARA(B2:B101)  -- Cuenta celdas con texto (fechas de pedido)
=CONTAR(D2:D101)   -- Cuenta celdas con números
```

### CONTAR.SI

```excel
=CONTAR.SI(C2:C101; "Completado")  -- Cuenta pedidos completados
```

### SUMAR.SI

```excel
=SUMAR.SI(C2:C101; "Completado"; D2:D101)  -- Suma total de completados
```

## Análisis rápido con tus datos de ventas

Carga `datos_ventas.csv` y practica:

1. Convierte el rango en tabla (Ctrl+T)
2. Aplica formato de moneda a la columna `total`
3. Filtra para mostrar solo pedidos "Completado"
4. Ordena por `total` descendente para ver los pedidos más grandes
5. Calcula el total de ventas en una celda: `=SUMA(tabla1[total])`
6. Calcula el promedio por pedido: `=PROMEDIO(tabla1[total])`

## Ejercicios del Capítulo 4

1. Importa `datos_ventas.csv` a Excel y conviértelo en tabla.
2. Aplica formato de moneda (€) a la columna `total`.
3. ¿Cuál es el total de ventas? Usa `=SUMA()` en una celda vacía.
4. ¿Cuántos pedidos hay? Usa `=CONTAR()` o mira el número de filas.
5. Filtra los pedidos de la región "Madrid". ¿Cuántos hay?
6. Ordena los pedidos por `total` de mayor a menor. ¿Cuál es el pedido más grande?
7. Usa `=PROMEDIO()` para calcular el ticket promedio.
8. Usa `=CONTAR.SI()` para contar cuántos pedidos están "Cancelado".
9. Usa `=SUMAR.SI()` para sumar el total de pedidos "Completado".
10. ¿Qué porcentaje de pedidos están completados?

## Checklist de autoevaluación

- [ ] Sé importar datos CSV a Excel
- [ ] Sé aplicar formato a celdas (números, moneda, texto)
- [ ] Sé usar autofiltro para filtrar datos
- [ ] Sé ordenar datos por una o más columnas
- [ ] Sé crear tablas con Ctrl+T
- [ ] Sé usar fórmulas básicas: SUMA, PROMEDIO, CONTAR, CONTAR.SI
