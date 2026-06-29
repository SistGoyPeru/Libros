-- Capítulo 5: La Fecha del Crimen
-- Conceptos: DATE, DATETIME, strftime, funciones de fecha

-- Fecha y hora actual
SELECT DATE('now');
SELECT DATETIME('now');

-- Extraer partes de una fecha
SELECT strftime('%Y', fecha) as año FROM tabla;  -- 2026
SELECT strftime('%m', fecha) as mes FROM tabla;  -- 07
SELECT strftime('%d', fecha) as dia FROM tabla;  -- 14
SELECT strftime('%H', fecha) as hora FROM tabla; -- 21
SELECT strftime('%w', fecha) as dia_sem FROM tabla; -- 0=domingo

-- Operaciones aritméticas con fechas
SELECT DATE(fecha, '+1 day') as manana FROM tabla;
SELECT DATE(fecha, '-7 days') as semana_pasada FROM tabla;
SELECT DATETIME(fecha, '+2 hours') FROM tabla;

-- Rango de fechas
SELECT * FROM accesos 
WHERE fecha >= '2026-07-14 22:00' 
  AND fecha < '2026-07-15 06:00';

-- Filtrar por día de semana (domingos)
SELECT * FROM accesos 
WHERE strftime('%w', fecha) = '0';

-- Filtrar por hora del día
SELECT * FROM accesos 
WHERE strftime('%H', fecha) BETWEEN '22' AND '23';

-- Búsqueda detectivesca: envíos al laboratorio
SELECT * FROM envios 
WHERE destinatario = 'Héctor Blasco'
  AND fecha BETWEEN '2026-07-14 20:00' AND '2026-07-14 22:00';

-- Modificaciones después del crimen
SELECT tabla, fecha_modificacion, usuario
FROM logs_modificaciones
WHERE tabla = 'inventario_quimico'
  AND fecha_modificacion > '2026-07-15 05:30'
ORDER BY fecha_modificacion DESC;
