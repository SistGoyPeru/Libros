-- Capítulo 3: Las Tablas del Engaño
-- Conceptos: INNER JOIN, LEFT JOIN, alias, ON

-- INNER JOIN básico
SELECT e.nombre, e.fecha, a.usuario, a.accion
FROM experimentos e
INNER JOIN logs_acceso a ON e.investigador = a.usuario;

-- LEFT JOIN
SELECT e.nombre, c.clave, c.valor
FROM experimentos e
LEFT JOIN cerbero_config c ON e.proyecto = 'Cerbero';

-- JOIN con filtros
SELECT a.usuario, a.fecha, a.puerta, c.valor as umbral
FROM logs_acceso a
JOIN cerbero_config c ON c.clave = 'umbral_seguridad'
WHERE a.fecha > c.fecha_modificacion
  AND a.acceso_concedido = 1
ORDER BY a.fecha DESC;

-- FULL JOIN (no soportado en SQLite, simulado con LEFT + UNION)
SELECT * FROM A LEFT JOIN B ON A.id = B.id
UNION
SELECT * FROM B LEFT JOIN A ON B.id = A.id;
