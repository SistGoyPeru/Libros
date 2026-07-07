-- Capítulo 11: El Trigger del Miedo
-- Conceptos: CREATE TRIGGER, BEFORE/AFTER INSERT/UPDATE/DELETE, OLD/NEW

-- Tabla de auditoría
CREATE TABLE auditoria_transferencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    accion TEXT,
    usuario TEXT,
    monto_anterior REAL,
    monto_nuevo REAL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger AFTER UPDATE
CREATE TRIGGER trg_auditar_transferencias
AFTER UPDATE ON transacciones
FOR EACH ROW
BEGIN
    INSERT INTO auditoria_transferencias 
        (accion, usuario, monto_anterior, monto_nuevo, fecha)
    VALUES ('UPDATE', OLD.usuario_mod, OLD.monto, NEW.monto, 
            datetime('now'));
END;

-- Trigger BEFORE: validación
CREATE TRIGGER trg_validar_monto
BEFORE INSERT ON transacciones
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN NEW.monto <= 0 THEN RAISE(ABORT, 'El monto debe ser positivo')
        WHEN NEW.beneficiario IS NULL THEN RAISE(ABORT, 'Beneficiario requerido')
    END;
END;

-- Trigger AFTER INSERT
CREATE TRIGGER trg_log_insercion
AFTER INSERT ON transacciones
FOR EACH ROW
BEGIN
    INSERT INTO logs_eventos (evento, detalle, fecha)
    VALUES ('INSERT', 'Transacción #' || NEW.id, datetime('now'));
END;

-- Trigger de bitácora
CREATE TRIGGER trg_bitacora_cambios
AFTER UPDATE ON personal
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (tabla, campo, valor_anterior, valor_nuevo, fecha)
    VALUES ('personal', 'cargo', OLD.cargo, NEW.cargo, datetime('now'));
END;

-- Trigger para prevenir borrado
CREATE TRIGGER trg_prevenir_borrado_logs
BEFORE DELETE ON logs_modificaciones
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN OLD.fecha > datetime('now', '-1 day') 
        THEN RAISE(ABORT, 'No se pueden borrar logs recientes')
    END;
END;

-- Ver triggers existentes
SELECT * FROM sqlite_master WHERE type = 'trigger';

-- Investigación: auditoría oculta de Héctor
SELECT * FROM auditoria_oculta
WHERE fecha > '2026-07-01'
ORDER BY fecha;
