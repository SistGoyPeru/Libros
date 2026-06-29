-- Capítulo 15: El Epílogo
-- Conceptos: Repaso completo, vista de resumen, índices finales

-- Resumen del caso Talos
SELECT 
    COUNT(*) as total_transacciones,
    SUM(monto) as total_desviado,
    COUNT(DISTINCT usuario_creacion) as implicados,
    MIN(fecha) as primer_transaccion,
    MAX(fecha) as ultima_transaccion
FROM transacciones_ocultas
WHERE proyecto_asociado = 'Talos';

-- Vista para el fiscal
CREATE VIEW v_resumen_caso_blasco AS
SELECT 
    t.id as transaccion_id,
    t.fecha,
    t.monto,
    t.beneficiario,
    t.proyecto_asociado,
    p.nombre as creador_nombre,
    p.departamento,
    CASE 
        WHEN t.beneficiario NOT IN (SELECT codigo FROM proveedores_autorizados)
        THEN 'NO AUTORIZADO'
        ELSE 'AUTORIZADO'
    END as estado_beneficiario
FROM transacciones_ocultas t
JOIN personal p ON t.usuario_creacion = p.codigo
WHERE t.proyecto_asociado = 'Talos';

-- Índices preventivos contra fraudes futuros
CREATE INDEX idx_transacciones_fecha ON transacciones(fecha);
CREATE INDEX idx_transacciones_beneficiario ON transacciones(beneficiario);
CREATE INDEX idx_transacciones_usuario ON transacciones(usuario_creacion);
CREATE INDEX idx_transacciones_proyecto ON transacciones(proyecto_asociado);

-- Índice compuesto para consultas de investigación
CREATE INDEX idx_transacciones_investigacion 
ON transacciones(fecha, usuario_creacion, beneficiario, monto);

-- La consulta final de Elisa:
-- SELECT la verdad FROM los datos WHERE la justicia = true;
