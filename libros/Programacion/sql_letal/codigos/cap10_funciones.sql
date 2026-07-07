-- Capítulo 10: La Función del Silencio
-- Conceptos: LENGTH, UPPER, LOWER, SUBSTR, INSTR, REPLACE, TRIM, CASE, COALESCE

-- Longitud
SELECT LENGTH('Hola Mundo');

-- Mayúsculas/minúsculas
SELECT UPPER('hola');
SELECT LOWER('HOLA');

-- Extraer subcadena
SELECT SUBSTR('Hola Mundo', 1, 4);
SELECT SUBSTR('Hola Mundo', 6);

-- Buscar posición
SELECT INSTR('Hola Mundo', 'Mundo');

-- Concatenar
SELECT 'Hola' || ' ' || 'Mundo';

-- Reemplazar
SELECT REPLACE('Hola Mundo', 'Mundo', 'SQL');

-- Eliminar espacios
SELECT TRIM('  Hola  ');

-- CASE: condicionales
SELECT usuario, fecha,
  CASE
    WHEN strftime('%H', fecha) BETWEEN '06' AND '12' THEN 'Mañana'
    WHEN strftime('%H', fecha) BETWEEN '12' AND '18' THEN 'Tarde'
    WHEN strftime('%H', fecha) BETWEEN '18' AND '22' THEN 'Noche'
    ELSE 'Madrugada'
  END as turno
FROM accesos;

-- COALESCE: valor por defecto para NULL
SELECT nombre, COALESCE(telefono, 'No registrado') as telefono
FROM personal;

-- Investigación: extraer comandos de notas
SELECT id, monto, 
       SUBSTR(notas, 1, 3) as codigo,
       SUBSTR(notas, INSTR(notas, ':') + 1) as instruccion
FROM transacciones_ocultas
WHERE notas LIKE 'CMD:%';

-- Investigación: quién daba órdenes
SELECT usuario, COUNT(*) as ordenes_dadas
FROM transacciones_ocultas
WHERE notas LIKE 'CMD:%'
GROUP BY usuario
ORDER BY ordenes_dadas DESC;
