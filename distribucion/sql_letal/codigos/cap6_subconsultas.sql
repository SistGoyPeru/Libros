-- Capítulo 6: La Subconsulta Asesina
-- Conceptos: Subconsultas, EXISTS, NOT EXISTS

-- Subconsulta en WHERE con IN
SELECT * FROM accesos
WHERE usuario IN (
    SELECT DISTINCT usuario 
    FROM logs_modificaciones
    WHERE fecha_modificacion > '2026-07-15 05:30'
);

-- Subconsulta con comparación (> promedio)
SELECT * FROM accesos
WHERE duracion > (
    SELECT AVG(duracion) FROM accesos
);

-- Subconsulta en SELECT
SELECT a.*, (
    SELECT COUNT(*) 
    FROM accesos a2 
    WHERE a2.usuario = a.usuario
) as total_usuario
FROM accesos a;

-- EXISTS
SELECT DISTINCT usuario FROM personal p
WHERE EXISTS (
    SELECT 1 FROM accesos a
    WHERE a.usuario = p.codigo
      AND strftime('%H', a.fecha) BETWEEN '22' AND '06'
);

-- NOT EXISTS
SELECT * FROM personal p
WHERE NOT EXISTS (
    SELECT 1 FROM accesos a
    WHERE a.usuario = p.codigo
      AND a.fecha > '2026-07-15 05:30'
);

-- Subconsultas anidadas
SELECT ip, COUNT(*) as total
FROM conexiones
WHERE ip IN (
    SELECT DISTINCT ip_origen 
    FROM logs_modificaciones
    WHERE fecha > '2026-07-15 05:30'
      AND usuario NOT IN (
          SELECT codigo FROM personal WHERE autorizado = 1
      )
)
GROUP BY ip
ORDER BY total DESC
LIMIT 1;

-- Investigación: IP del intruso
SELECT ip_origen, COUNT(*) as operaciones
FROM logs_modificaciones
WHERE fecha_modificacion > '2026-07-15 05:30'
  AND usuario = 'hblasco'
GROUP BY ip_origen;
