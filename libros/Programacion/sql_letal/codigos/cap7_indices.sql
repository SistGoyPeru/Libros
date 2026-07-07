-- Capítulo 7: El Índice Oculto
-- Conceptos: CREATE INDEX, EXPLAIN QUERY PLAN, optimización

-- Consulta sin índice (table scan)
SELECT * FROM transacciones WHERE beneficiario = 'X';

-- Crear un índice simple
CREATE INDEX idx_accesos_usuario ON accesos(usuario);

-- Índice compuesto
CREATE INDEX idx_accesos_fecha_usuario 
ON accesos(fecha, usuario);

-- Índice único
CREATE UNIQUE INDEX idx_personal_email 
ON personal(email);

-- Ver los índices de una tabla
SELECT * FROM sqlite_master 
WHERE type = 'index' AND tbl_name = 'accesos';

-- Verificar plan de ejecución
EXPLAIN QUERY PLAN
SELECT * FROM transacciones 
WHERE beneficiario = 'X' AND monto > 1000;

-- Investigación: transacciones ocultas
SELECT DISTINCT beneficiario, SUM(monto) as total
FROM transacciones_ocultas
GROUP BY beneficiario
ORDER BY total DESC;

-- Crear índice en tabla descubierta
CREATE INDEX idx_beneficiario_ocultas ON transacciones_ocultas(beneficiario);
