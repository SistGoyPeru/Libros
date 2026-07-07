# Capítulo 14: El Último Query (Parte 2)

Faltaba la pieza final: ¿quién era el beneficiario real de la cuenta SwissCredit? La base de datos no tenía esa información, pero los metadatos de las transacciones sí contenían pistas.

Elisa observó el patrón de las transacciones. Cada transferencia a SwissCredit estaba precedida por una serie de transacciones más pequeñas. Como si alguien estuviera consolidando fondos.

Era un patrón conocido en lavado de dinero: muchas entradas pequeñas, una salida grande. Necesitaba una herramienta analítica más potente para detectar el patrón.

—Window functions —dijo en voz alta—. Es lo único que puede revelar este patrón.

---

## Concepto SQL: Window Functions

Las **window functions** realizan cálculos en un conjunto de filas relacionadas con la fila actual. A diferencia de GROUP BY, no colapsan filas.

### Sintaxis

```sql
SELECT columna, 
       funcion_ventana() OVER (
           PARTITION BY columna_grupo 
           ORDER BY columna_orden
           frame_clause
       ) as resultado
FROM tabla;
```

### ROW_NUMBER, RANK, DENSE_RANK

```sql
-- Numerar transacciones por fecha
SELECT id, monto, fecha,
       ROW_NUMBER() OVER (ORDER BY fecha) as num_fila,
       RANK() OVER (ORDER BY monto DESC) as ranking_monto,
       DENSE_RANK() OVER (ORDER BY monto DESC) as ranking_sin_huecos
FROM transacciones;
```

### LAG y LEAD

Acceder a filas anteriores o siguientes:

```sql
-- Comparar cada transacción con la anterior del mismo usuario
SELECT usuario, fecha, monto,
       LAG(monto) OVER (PARTITION BY usuario ORDER BY fecha) as monto_anterior,
       monto - LAG(monto) OVER (PARTITION BY usuario ORDER BY fecha) as diferencia,
       LEAD(fecha) OVER (PARTITION BY usuario ORDER BY fecha) as siguiente_transaccion
FROM transacciones
ORDER BY usuario, fecha;
```

### SUM, AVG con ventanas

```sql
-- Acumulado por usuario
SELECT usuario, fecha, monto,
       SUM(monto) OVER (PARTITION BY usuario ORDER BY fecha) as acumulado
FROM transacciones;

-- Promedio móvil de 3 transacciones
SELECT fecha, monto,
       AVG(monto) OVER (ORDER BY fecha ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as media_movil
FROM transacciones;
```

### FIRST_VALUE y LAST_VALUE

```sql
-- Primera y última transacción de cada usuario
SELECT usuario, fecha, monto,
       FIRST_VALUE(monto) OVER (PARTITION BY usuario ORDER BY fecha) as primer_monto,
       LAST_VALUE(monto) OVER (PARTITION BY usuario ORDER BY fecha 
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as ultimo_monto
FROM transacciones;
```

### Detección de patrones

```sql
-- Detectar transacciones que son > 2x la anterior (pico sospechoso)
WITH con_anterior AS (
    SELECT fecha, monto,
           LAG(monto) OVER (ORDER BY fecha) as monto_anterior
    FROM transacciones
)
SELECT fecha, monto, monto_anterior,
       ROUND(CAST(monto AS REAL) / monto_anterior, 2) as ratio
FROM con_anterior
WHERE monto_anterior IS NOT NULL
  AND CAST(monto AS REAL) / monto_anterior > 2
ORDER BY ratio DESC;
```

---

### El Patrón Revelado

Elisa aplicó window functions a las transacciones:

```sql
WITH transacciones_ordenadas AS (
    SELECT id, fecha, monto, beneficiario, usuario_creacion,
           LAG(fecha) OVER (PARTITION BY usuario_creacion ORDER BY fecha) as fecha_anterior,
           LAG(monto) OVER (PARTITION BY usuario_creacion ORDER BY fecha) as monto_anterior,
           SUM(monto) OVER (PARTITION BY usuario_creacion ORDER BY fecha) as acumulado
    FROM transacciones_ocultas
    WHERE proyecto_asociado = 'Talos'
)
SELECT *,
       CASE 
           WHEN monto_anterior IS NOT NULL 
           AND CAST(monto AS REAL) / monto_anterior > 5 
           THEN '*** PICO SOSPECHOSO ***'
           ELSE ''
       END as alerta
FROM transacciones_ordenadas
WHERE beneficiario = 'SwissCredit AG'
ORDER BY fecha;
```

El resultado mostró que las transferencias grandes a SwissCredit siempre iban precedidas de 5-7 transacciones pequeñas. El patrón era claro: acumulación y consolidación.

Pero había un detalle más: la última transacción a SwissCredit — 750,000 EUR — no tenía transacciones pequeñas precedentes. Era la única que rompía el patrón.

—Esto no es lavado de dinero —dijo Elisa—. Es un pago. Un pago único.

—¿Un soborno? —preguntó Rovira.

—O el pago por un asesinato.

---

### Enigma SQL #14: Siguiendo el Dinero

1. Usando LAG, encuentra las transacciones donde el monto es al menos 3 veces mayor que la transacción anterior del mismo usuario.
2. Calcula el acumulado de transacciones por beneficiario, ordenado por fecha. ¿Cuánto recibió SwissCredit en total?
3. Usando window functions, asigna un número de orden a cada transacción dentro de cada día. ¿Cuántas transacciones hubo el 14 de julio?

```sql
-- Tus consultas aquí
```
