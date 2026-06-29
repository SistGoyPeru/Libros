-- Capítulo 13: El Último Query (Parte 1)
-- Conceptos: CTE (WITH), CTEs múltiples, CTE recursivo

-- CTE simple
WITH transferencias_sospechosas AS (
    SELECT * FROM transacciones
    WHERE monto > 100000
      AND beneficiario NOT IN (
          SELECT codigo FROM proveedores_autorizados
      )
)
SELECT t.*, p.nombre as aprobador_nombre
FROM transferencias_sospechosas t
JOIN personal p ON t.aprobador = p.codigo;

-- Múltiples CTEs
WITH
accesos_nocturnos AS (
    SELECT * FROM accesos
    WHERE strftime('%H', fecha) BETWEEN '22' AND '06'
),
transacciones_recientes AS (
    SELECT * FROM transacciones
    WHERE fecha > '2026-01-01'
)
SELECT a.usuario, a.fecha, t.id as transaccion_id, t.monto
FROM accesos_nocturnos a
JOIN transacciones_recientes t ON a.usuario = t.usuario_creacion
  AND date(a.fecha) = date(t.fecha)
ORDER BY a.fecha DESC;

-- CTE con agregaciones
WITH
estadisticas_usuario AS (
    SELECT usuario, 
           COUNT(*) as total_accesos,
           COUNT(DISTINCT date(fecha)) as dias_activo
    FROM accesos
    GROUP BY usuario
)
SELECT p.nombre, e.total_accesos, e.dias_activo,
       ROUND(CAST(e.total_accesos AS REAL) / e.dias_activo, 1) as accesos_por_dia
FROM estadisticas_usuario e
JOIN personal p ON e.usuario = p.codigo
ORDER BY accesos_por_dia DESC;

-- CTE recursivo: organigrama
WITH RECURSIVE organigrama AS (
    -- Caso base: el director
    SELECT codigo, nombre, jefe_codigo, 0 as nivel
    FROM personal
    WHERE jefe_codigo IS NULL
    
    UNION ALL
    
    -- Paso recursivo: subordinados
    SELECT p.codigo, p.nombre, p.jefe_codigo, o.nivel + 1
    FROM personal p
    JOIN organigrama o ON p.jefe_codigo = o.codigo
)
SELECT * FROM organigrama ORDER BY nivel, nombre;

-- La consulta detectivesca final (versión simplificada)
WITH
accesos_sospechosos AS (
    SELECT usuario, fecha, ip_origen
    FROM accesos
    WHERE laboratorio = 7 AND fecha > '2026-06-01'
),
transacciones_sospechosas AS (
    SELECT id, monto, fecha, usuario_creacion, beneficiario, proyecto_asociado
    FROM transacciones_ocultas
    WHERE monto > 50000
),
modificaciones_sospechosas AS (
    SELECT usuario, tabla, fecha_modificacion, ip_origen
    FROM logs_modificaciones
    WHERE tabla IN ('transacciones', 'inventario_quimico', 'cerbero_config')
      AND fecha_modificacion > '2026-06-01'
),
linea_tiempo AS (
    SELECT fecha, 'acceso' as evento, usuario, NULL as detalle
    FROM accesos_sospechosos
    UNION ALL
    SELECT fecha, 'transaccion' as evento, usuario_creacion, CAST(monto AS TEXT)
    FROM transacciones_sospechosas
    UNION ALL
    SELECT fecha_modificacion, 'modificacion' as evento, usuario, tabla
    FROM modificaciones_sospechosas
)
SELECT * FROM linea_tiempo ORDER BY fecha;
