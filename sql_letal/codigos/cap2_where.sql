-- Capítulo 2: La Condición del Sospechoso
-- Conceptos: WHERE, AND, OR, NOT, IN, BETWEEN, LIKE, IS NULL

-- Filtrar por valor exacto
SELECT * FROM experimentos WHERE proyecto = 'Cerbero';

-- Filtrar por número
SELECT * FROM experimentos WHERE id > 10;

-- Múltiples condiciones con AND
SELECT * FROM experimentos 
WHERE proyecto = 'Cerbero' AND resultado = 'éxito';

-- Múltiples condiciones con OR
SELECT * FROM experimentos 
WHERE proyecto = 'Cerbero' OR proyecto = 'Fénix';

-- Negar condición
SELECT * FROM experimentos WHERE NOT resultado = 'fallo';

-- BETWEEN: rangos
SELECT * FROM experimentos 
WHERE fecha BETWEEN '2026-01-01' AND '2026-06-30';

-- IN: lista de valores
SELECT * FROM experimentos 
WHERE investigador IN ('Blasco', 'Riera', 'Valls');

-- LIKE: patrones
SELECT * FROM experimentos WHERE nombre LIKE 'Proyecto%';

-- IS NULL: valores nulos
SELECT * FROM experimentos WHERE fecha_fin IS NULL;

-- Búsqueda del detective: logs de creación de tablas
SELECT * FROM logs_acceso 
WHERE usuario = 'hblasco' AND accion LIKE 'CREATE TABLE%';
