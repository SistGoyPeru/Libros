-- Capítulo 8: La Vista del Pasado
-- Conceptos: CREATE VIEW, DROP VIEW

-- Vista simple
CREATE VIEW v_accesos_recientes AS
SELECT usuario, fecha, puerta, acceso_concedido
FROM accesos
WHERE fecha > DATE('now', '-30 days')
ORDER BY fecha DESC;

-- Usar la vista
SELECT * FROM v_accesos_recientes;
SELECT usuario, COUNT(*) FROM v_accesos_recientes
WHERE acceso_concedido = 0
GROUP BY usuario;

-- Vista con JOIN
CREATE VIEW v_investigacion_completa AS
SELECT a.id, a.fecha, a.usuario, p.nombre as nombre_personal,
       p.departamento, a.puerta, a.acceso_concedido
FROM accesos a
JOIN personal p ON a.usuario = p.codigo;

-- Vista con agregaciones
CREATE VIEW v_estadisticas_accesos AS
SELECT usuario, 
       COUNT(*) as total_accesos,
       SUM(CASE WHEN acceso_concedido = 0 THEN 1 ELSE 0 END) as fallos,
       ROUND(AVG(CAST(strftime('%H', fecha) AS REAL)), 1) as hora_promedio
FROM accesos
GROUP BY usuario;

-- Vista detectivesca: el caso Blasco
CREATE VIEW v_caso_blasco AS
SELECT a.fecha as fecha_acceso, a.usuario, a.puerta,
       p.nombre, p.departamento, p.cargo,
       t.monto, t.beneficiario, t.fecha as fecha_transaccion
FROM accesos a
JOIN personal p ON a.usuario = p.codigo
LEFT JOIN transacciones_ocultas t ON t.fecha BETWEEN 
    datetime(a.fecha, '-1 hour') AND datetime(a.fecha, '+1 hour')
WHERE a.laboratorio = 7
  AND a.fecha > '2026-06-01';

-- Eliminar vista
DROP VIEW IF EXISTS v_investigacion_completa;
