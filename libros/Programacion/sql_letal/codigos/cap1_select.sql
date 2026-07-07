-- Capítulo 1: SELECT y los Datos Perdidos
-- Conceptos: SELECT, FROM, LIMIT, ORDER BY

-- Ver todas las columnas de la tabla experimentos
SELECT * FROM experimentos;

-- Columnas específicas
SELECT nombre, fecha FROM experimentos;

-- Limitar resultados
SELECT * FROM experimentos LIMIT 5;

-- Ordenar por fecha descendente
SELECT * FROM experimentos ORDER BY fecha DESC;

-- Contar registros
SELECT COUNT(*) FROM experimentos;
