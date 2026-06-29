-- Capítulo 4: El Grupo que Miente
-- Conceptos: GROUP BY, COUNT, SUM, AVG, MAX, MIN, HAVING

-- COUNT: contar filas
SELECT COUNT(*) FROM accesos;
SELECT COUNT(DISTINCT usuario) FROM accesos;

-- SUM: sumar valores
SELECT SUM(duracion_minutos) FROM sesiones;

-- AVG: promedio
SELECT AVG(duracion_minutos) FROM sesiones;

-- MAX / MIN
SELECT MAX(intentos_fallidos) FROM accesos;
SELECT MIN(intentos_fallidos) FROM accesos;

-- GROUP BY básico
SELECT usuario, COUNT(*) as total_accesos
FROM accesos
GROUP BY usuario;

-- Promedio por día
SELECT DATE(fecha) as dia, AVG(duracion) as promedio
FROM sesiones
GROUP BY DATE(fecha);

-- HAVING: filtrar grupos
SELECT usuario, COUNT(*) as total
FROM accesos
GROUP BY usuario
HAVING COUNT(*) > 50;

-- Días con más de 10 accesos fallidos
SELECT DATE(fecha) as dia, COUNT(*) as fallos
FROM accesos
WHERE acceso_concedido = 0
GROUP BY DATE(fecha)
HAVING COUNT(*) > 10;

-- Análisis detectivesco: patrón de accesos de Marta
SELECT usuario, 
       DATE(fecha) as dia,
       COUNT(*) as accesos,
       MIN(fecha) as primero,
       MAX(fecha) as ultimo
FROM accesos
WHERE usuario = 'mrobles'
GROUP BY usuario, DATE(fecha)
HAVING COUNT(*) > 3
ORDER BY dia;
