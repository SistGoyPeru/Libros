# Apéndice: Soluciones a los Enigmas

### Enigma 1: Los Registros Perdidos

```sql
-- 1. ¿Cuántos experimentos hay registrados?
SELECT COUNT(*) FROM experimentos;

-- 2. Muestra todos ordenados por fecha descendente
SELECT * FROM experimentos ORDER BY fecha DESC;

-- 3. ¿Qué columnas tiene la tabla?
-- id, nombre, fecha, investigador, resultado, proyecto
-- Puedes obtenerlas con:
PRAGMA table_info(experimentos);
```

### Enigma 2: El Rastro del Profesor

```sql
-- 1. Accesos nocturnos del Dr. Blasco
SELECT * FROM accesos 
WHERE usuario = 'hblasco' 
  AND strftime('%H', fecha) >= '22';

-- 2. Experimentos con resultado NULL
SELECT COUNT(*) FROM experimentos 
WHERE resultado IS NULL;

-- 3. Proyectos con "Cerbero"
SELECT * FROM experimentos 
WHERE proyecto LIKE '%Cerbero%';
```

### Enigma 3: ¿Quién más sabía?

```sql
-- 1. Investigadores con acceso a Cerbero
SELECT DISTINCT p.nombre, p.codigo
FROM personal p
JOIN proyecto_investigadores pi ON p.codigo = pi.investigador_codigo
WHERE pi.proyecto_id = 'Cerbero';

-- 2. Accesos al laboratorio 7 en junio
SELECT a.fecha, a.usuario, p.nombre, a.puerta
FROM accesos a
JOIN personal p ON a.usuario = p.codigo
WHERE a.laboratorio = 7
  AND a.fecha BETWEEN '2026-06-01' AND '2026-06-30';

-- 3. Accedieron pero no son investigadores de Cerbero
SELECT DISTINCT a.usuario
FROM accesos a
WHERE a.laboratorio = 7
  AND a.usuario NOT IN (
      SELECT investigador_codigo 
      FROM proyecto_investigadores
      WHERE proyecto_id = 'Cerbero'
  );
```

### Enigma 4: La Agenda Oculta

```sql
-- 1. Accesos por empleado en junio (orden descendente)
SELECT a.usuario, p.nombre, COUNT(*) as total
FROM accesos a
JOIN personal p ON a.usuario = p.codigo
WHERE a.fecha BETWEEN '2026-06-01' AND '2026-06-30'
GROUP BY a.usuario
ORDER BY total DESC;

-- 2. Días con más de 5 accesos fallidos
SELECT DATE(fecha) as dia, COUNT(*) as fallos
FROM accesos
WHERE acceso_concedido = 0
GROUP BY DATE(fecha)
HAVING COUNT(*) > 5;

-- 3. Promedio de accesos por hora
SELECT strftime('%H', fecha) as hora, COUNT(*) as total
FROM accesos
GROUP BY strftime('%H', fecha)
ORDER BY hora;
```

### Enigma 5: La Línea de Tiempo

```sql
-- 1. Modificaciones del 15 de julio
SELECT * FROM logs_modificaciones
WHERE DATE(fecha_modificacion) = '2026-07-15'
ORDER BY fecha_modificacion;

-- 2. Modificaciones nocturnas (22:00-06:00)
SELECT * FROM logs_modificaciones
WHERE fecha_modificacion BETWEEN '2026-07-14 22:00' AND '2026-07-15 06:00';

-- 3. Diferencia entre última modif de hblasco y primera de mrobles
SELECT 
    (SELECT MAX(fecha_modificacion) FROM logs_modificaciones WHERE usuario = 'hblasco') as ultima_hblasco,
    (SELECT MIN(fecha_modificacion) FROM logs_modificaciones WHERE usuario = 'mrobles') as primera_mrobles,
    ROUND(julianday(
        (SELECT MIN(fecha_modificacion) FROM logs_modificaciones WHERE usuario = 'mrobles')
    ) - julianday(
        (SELECT MAX(fecha_modificacion) FROM logs_modificaciones WHERE usuario = 'hblasco')
    ) * 24 * 60, 2) as minutos_diferencia;
```

### Enigma 6: La Red Oculta

```sql
-- 1. Conexiones externas después del crimen
SELECT * FROM conexiones
WHERE ip_origen NOT LIKE '10.0.%'
  AND fecha > '2026-07-15 05:30';

-- 2. IPs usadas por Marta
SELECT DISTINCT ip_origen FROM conexiones
WHERE usuario = 'mrobles'
  AND fecha > DATE('now', '-30 days');

-- 3. Usuarios con accesos nocturnos sobre el promedio
WITH nocturnos AS (
    SELECT usuario, COUNT(*) as accesos_nocturnos
    FROM accesos
    WHERE strftime('%H', fecha) BETWEEN '22' AND '06'
    GROUP BY usuario
)
SELECT n.* FROM nocturnos n
WHERE n.accesos_nocturnos > (
    SELECT AVG(accesos_nocturnos) FROM nocturnos
);
```

### Enigma 7: El Rastro del Dinero

```sql
-- 1. Transacciones por año
SELECT strftime('%Y', fecha) as anio, COUNT(*) as total, SUM(monto) as suma
FROM transacciones_ocultas
GROUP BY strftime('%Y', fecha)
ORDER BY anio;

-- 2. Crear índice y verificar
CREATE INDEX idx_beneficiario_ocultas ON transacciones_ocultas(beneficiario);
EXPLAIN QUERY PLAN
SELECT * FROM transacciones_ocultas WHERE beneficiario = 'ICB';

-- 3. Transacción de mayor monto
SELECT * FROM transacciones_ocultas
ORDER BY monto DESC
LIMIT 1;
```

### Enigma 8: La Investigación Simplificada

```sql
-- 1. Vista de accesos al laboratorio 7 de Sistemas
CREATE VIEW v_accesos_lab7_sistemas AS
SELECT a.*, p.nombre, p.departamento
FROM accesos a
JOIN personal p ON a.usuario = p.codigo
WHERE a.laboratorio = 7
  AND p.departamento = 'Sistemas'
  AND a.fecha BETWEEN '2026-06-01' AND '2026-07-31';

-- 2. Empleados que accedieron a lab7 y almacén el mismo día
SELECT a.usuario, DATE(a.fecha) as dia
FROM accesos a
WHERE a.laboratorio = 7
INTERSECT
SELECT a2.usuario, DATE(a2.fecha)
FROM accesos a2
WHERE a2.laboratorio = 'AlmacenQCA';

-- 3. Accesos por departamento al lab7
CREATE VIEW v_accesos_por_depto AS
SELECT p.departamento, COUNT(*) as total_accesos
FROM accesos a
JOIN personal p ON a.usuario = p.codigo
WHERE a.laboratorio = 7
GROUP BY p.departamento;
```

### Enigma 9: La Cadena de Transacciones

```sql
-- 1. Transferencia de 500,000 EUR
BEGIN TRANSACTION;
SELECT saldo FROM cuentas WHERE id = 1;
-- Asumiendo saldo suficiente
UPDATE cuentas SET saldo = saldo - 500000 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 500000 WHERE id = 2;
INSERT INTO registro_transferencias (origen, destino, monto, fecha)
VALUES (1, 2, 500000, datetime('now'));
COMMIT;

-- 2. Transacciones con confirmación < 5 min
SELECT id, fecha_inicio, fecha_confirmacion,
       ROUND((julianday(fecha_confirmacion) - julianday(fecha_inicio)) * 24 * 60, 1) as minutos
FROM transacciones
WHERE fecha_confirmacion IS NOT NULL
  AND (julianday(fecha_confirmacion) - julianday(fecha_inicio)) * 24 * 60 < 5;

-- 3. Transacciones con cuenta de fallecido
SELECT t.* FROM transacciones t
JOIN personal p ON t.usuario_ejecutor = p.codigo
WHERE t.fecha > p.fecha_muerte;
```

### Enigma 10: Decodificando el Mensaje

```sql
-- 1. Primeros 4 caracteres de concepto
SELECT id, monto, SUBSTR(concepto, 1, 4) as prefijo,
       COUNT(*) OVER (PARTITION BY SUBSTR(concepto, 1, 4)) as frecuencia
FROM transacciones_ocultas;

-- 2. Clasificación por monto
SELECT monto,
  CASE 
    WHEN monto < 1000 THEN 'Bajo'
    WHEN monto BETWEEN 1000 AND 50000 THEN 'Medio'
    ELSE 'Alto'
  END as categoria,
  COUNT(*) as cantidad
FROM transacciones_ocultas
GROUP BY categoria;

-- 3. Nombre completo y total de transacciones
SELECT p.nombre || ' ' || p.apellido as nombre_completo,
       COUNT(t.id) as total_transacciones
FROM personal p
LEFT JOIN transacciones_ocultas t ON p.codigo = t.usuario_creacion
GROUP BY p.codigo;
```

### Enigma 11: El Guardián Silencioso

```sql
-- 1. Trigger que registra eliminaciones
CREATE TABLE IF NOT EXISTS log_eliminaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tabla TEXT,
    registro_id INTEGER,
    usuario TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER trg_log_eliminaciones
AFTER DELETE ON transacciones
FOR EACH ROW
BEGIN
    INSERT INTO log_eliminaciones (tabla, registro_id, usuario)
    VALUES ('transacciones', OLD.id, 
            (SELECT usuario FROM conexiones ORDER BY fecha DESC LIMIT 1));
END;

-- 2. Auditoría del 14 de julio
SELECT * FROM auditoria_oculta
WHERE DATE(fecha) = '2026-07-14';

-- 3. Trigger que impide modificar monto de transacciones confirmadas
CREATE TRIGGER trg_proteger_monto
BEFORE UPDATE OF monto ON transacciones
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN OLD.estado = 'CONFIRMADA' 
        THEN RAISE(ABORT, 'No se puede modificar el monto de una transacción confirmada')
    END;
END;
```

### Enigma 12: Diseñando la Verdad

```sql
-- 1. Anomalías en tabla accesos
-- Si acceso tiene nombre_completo:
-- - Redundancia (el nombre se repite en cada acceso)
-- - Anomalía de actualización (si alguien cambia de nombre, hay que actualizar N filas)

-- Estructura normalizada:
CREATE TABLE accesos_normalizado (
    id INTEGER PRIMARY KEY,
    usuario_codigo TEXT REFERENCES personal(codigo),
    fecha TIMESTAMP,
    puerta TEXT,
    laboratorio TEXT,
    acceso_concedido BOOLEAN
);

-- 2. Proyectos con transacciones pero sin registro oficial
SELECT DISTINCT t.proyecto_asociado
FROM transacciones_ocultas t
WHERE t.proyecto_asociado NOT IN (
    SELECT nombre FROM proyectos
);

-- 3. Esquema óptimo
CREATE TABLE departamentos (
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL
);
CREATE TABLE personal (
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT,
    email TEXT,
    cargo TEXT,
    departamento_codigo TEXT REFERENCES departamentos(codigo),
    jefe_codigo TEXT REFERENCES personal(codigo)
);
CREATE TABLE proyectos (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    presupuesto REAL,
    fecha_inicio DATE,
    responsable_codigo TEXT REFERENCES personal(codigo)
);
CREATE TABLE proyecto_investigadores (
    proyecto_id TEXT REFERENCES proyectos(id),
    investigador_codigo TEXT REFERENCES personal(codigo),
    PRIMARY KEY (proyecto_id, investigador_codigo)
);
CREATE TABLE accesos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_codigo TEXT REFERENCES personal(codigo),
    fecha TIMESTAMP,
    puerta TEXT,
    laboratorio TEXT,
    acceso_concedido BOOLEAN
);
CREATE TABLE transacciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monto REAL NOT NULL,
    fecha TIMESTAMP,
    concepto TEXT,
    beneficiario TEXT,
    proyecto_id TEXT REFERENCES proyectos(id),
    usuario_creacion TEXT REFERENCES personal(codigo),
    estado TEXT DEFAULT 'PENDIENTE'
);
```

### Enigma 13: Reconstruyendo la Verdad

```sql
-- 1. Eventos del 14 de julio
WITH eventos AS (
    SELECT fecha, 'acceso' as tipo, usuario, CAST(puerta AS TEXT) as detalle
    FROM accesos
    WHERE DATE(fecha) = '2026-07-14'
    UNION ALL
    SELECT fecha, 'transaccion', usuario_creacion, CAST(monto AS TEXT)
    FROM transacciones_ocultas
    WHERE DATE(fecha) = '2026-07-14'
    UNION ALL
    SELECT fecha_modificacion, 'modificacion', usuario, tabla
    FROM logs_modificaciones
    WHERE DATE(fecha_modificacion) = '2026-07-14'
)
SELECT * FROM eventos ORDER BY fecha;

-- 2. Organigrama recursivo
WITH RECURSIVE organigrama AS (
    SELECT codigo, nombre, jefe_codigo, 0 as nivel
    FROM personal
    WHERE jefe_codigo IS NULL
    UNION ALL
    SELECT p.codigo, p.nombre, p.jefe_codigo, o.nivel + 1
    FROM personal p
    JOIN organigrama o ON p.jefe_codigo = o.codigo
)
SELECT * FROM organigrama WHERE nombre LIKE '%Vilaró%' OR nombre LIKE '%Director%';

-- 3. Total transferido a Talos
WITH talos_transacciones AS (
    SELECT * FROM transacciones_ocultas
    WHERE proyecto_asociado = 'Talos'
)
SELECT COUNT(*) as num_transacciones, SUM(monto) as total
FROM talos_transacciones;
```

### Enigma 14: Siguiendo el Dinero

```sql
-- 1. Transacciones con monto >= 3x la anterior (mismo usuario)
WITH con_lag AS (
    SELECT id, usuario_creacion, fecha, monto,
           LAG(monto) OVER (PARTITION BY usuario_creacion ORDER BY fecha) as monto_anterior
    FROM transacciones_ocultas
)
SELECT * FROM con_lag
WHERE monto_anterior IS NOT NULL
  AND CAST(monto AS REAL) / monto_anterior >= 3;

-- 2. Acumulado por beneficiario
SELECT beneficiario, fecha, monto,
       SUM(monto) OVER (PARTITION BY beneficiario ORDER BY fecha) as acumulado
FROM transacciones_ocultas
ORDER BY beneficiario, fecha;

-- 3. Transacciones por orden dentro de cada día
SELECT id, fecha, monto,
       ROW_NUMBER() OVER (PARTITION BY DATE(fecha) ORDER BY fecha) as orden_dia
FROM transacciones_ocultas
WHERE DATE(fecha) = '2026-07-14';
```

### Enigma 15: El Caso Cerrado

```sql
-- 1. Resumen del caso
SELECT 
    'Talos' as proyecto,
    COUNT(*) as total_transacciones,
    SUM(monto) as total_desviado,
    COUNT(DISTINCT usuario_creacion) as implicados,
    MIN(fecha) as primer_transaccion,
    MAX(fecha) as ultima_transaccion
FROM transacciones_ocultas
WHERE proyecto_asociado = 'Talos';

-- 2. Vista para el fiscal
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

-- Uso: SELECT * FROM v_resumen_caso_blasco;

-- 3. Índices preventivos
CREATE INDEX idx_transacciones_fecha ON transacciones(fecha);
CREATE INDEX idx_transacciones_beneficiario ON transacciones(beneficiario);
CREATE INDEX idx_transacciones_usuario ON transacciones(usuario_creacion);
CREATE INDEX idx_transacciones_proyecto ON transacciones(proyecto_asociado);
-- Índice compuesto para consultas frecuentes de investigación
CREATE INDEX idx_transacciones_investigacion 
ON transacciones(fecha, usuario_creacion, beneficiario, monto);
```
