-- Capítulo 14: El Último Query (Parte 2)
-- Conceptos: Window Functions, ROW_NUMBER, RANK, LAG, LEAD, SUM/AVG OVER

-- ROW_NUMBER, RANK, DENSE_RANK
SELECT id, monto, fecha,
       ROW_NUMBER() OVER (ORDER BY fecha) as num_fila,
       RANK() OVER (ORDER BY monto DESC) as ranking_monto,
       DENSE_RANK() OVER (ORDER BY monto DESC) as ranking_sin_huecos
FROM transacciones;

-- LAG y LEAD
SELECT usuario, fecha, monto,
       LAG(monto) OVER (PARTITION BY usuario ORDER BY fecha) as monto_anterior,
       monto - LAG(monto) OVER (PARTITION BY usuario ORDER BY fecha) as diferencia,
       LEAD(fecha) OVER (PARTITION BY usuario ORDER BY fecha) as siguiente_transaccion
FROM transacciones
ORDER BY usuario, fecha;

-- SUM acumulado por usuario
SELECT usuario, fecha, monto,
       SUM(monto) OVER (PARTITION BY usuario ORDER BY fecha) as acumulado
FROM transacciones;

-- Media móvil (3 transacciones)
SELECT fecha, monto,
       AVG(monto) OVER (ORDER BY fecha ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as media_movil
FROM transacciones;

-- FIRST_VALUE y LAST_VALUE
SELECT usuario, fecha, monto,
       FIRST_VALUE(monto) OVER (PARTITION BY usuario ORDER BY fecha) as primer_monto,
       LAST_VALUE(monto) OVER (PARTITION BY usuario ORDER BY fecha 
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as ultimo_monto
FROM transacciones;

-- Detectar picos sospechosos
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

-- Investigación: patrón de acumulación y consolidación
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
