# Capítulo 11: El Trigger del Miedo

—Marta no es la mente maestra —dijo Elisa frente al panel—. Es una ejecutora. Alguien le daba órdenes a través de las transacciones. Pero necesito probar que no actuaba sola.

—¿Cómo? —preguntó Rovira.

—Los triggers. Héctor configuró triggers en la base de datos para auditar cambios críticos. Si alguien modificó datos sensibles, el trigger debió registrar algo.

—Pero dijiste que borraron los logs.

—Los logs de aplicación. Pero los triggers de base de datos operan a nivel interno. Son más difíciles de eliminar.

Elisa accedió al esquema de la base de datos y encontró algo:

```sql
SELECT * FROM sqlite_master WHERE type = 'trigger';
```

Había un trigger llamado `trg_auditar_transferencias`.

---

## Concepto SQL: Triggers

Un **trigger** es un procedimiento que se ejecuta automáticamente cuando ocurre un evento en una tabla (INSERT, UPDATE, DELETE). Es como un guardián silencioso.

### Sintaxis básica

```sql
CREATE TRIGGER nombre_trigger
[BEFORE | AFTER] [INSERT | UPDATE | DELETE] ON tabla
[FOR EACH ROW]
BEGIN
  -- instrucciones SQL
END;
```

### Ejemplo: Auditoría de cambios

```sql
-- Tabla de auditoría
CREATE TABLE auditoria_transferencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    accion TEXT,
    usuario TEXT,
    monto_anterior REAL,
    monto_nuevo REAL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger después de UPDATE
CREATE TRIGGER trg_auditar_transferencias
AFTER UPDATE ON transacciones
FOR EACH ROW
BEGIN
    INSERT INTO auditoria_transferencias 
        (accion, usuario, monto_anterior, monto_nuevo, fecha)
    VALUES ('UPDATE', OLD.usuario_mod, OLD.monto, NEW.monto, 
            datetime('now'));
END;
```

### BEFORE vs AFTER

```sql
-- BEFORE: validar datos antes de insertar
CREATE TRIGGER trg_validar_monto
BEFORE INSERT ON transacciones
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN NEW.monto <= 0 THEN RAISE(ABORT, 'El monto debe ser positivo')
        WHEN NEW.beneficiario IS NULL THEN RAISE(ABORT, 'Beneficiario requerido')
    END;
END;

-- AFTER: registrar después de la operación
CREATE TRIGGER trg_log_insercion
AFTER INSERT ON transacciones
FOR EACH ROW
BEGIN
    INSERT INTO logs_eventos (evento, detalle, fecha)
    VALUES ('INSERT', 'Transacción #' || NEW.id, datetime('now'));
END;
```

### OLD y NEW

Dentro del trigger, puedes referirte a los valores antes y después del cambio:

```sql
-- OLD: valores antes del cambio (UPDATE, DELETE)
-- NEW: valores después del cambio (INSERT, UPDATE)

CREATE TRIGGER trg_bitacora_cambios
AFTER UPDATE ON personal
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (tabla, campo, valor_anterior, valor_nuevo, fecha)
    VALUES ('personal', 'cargo', OLD.cargo, NEW.cargo, datetime('now'));
END;
```

### Prevenir cambios no autorizados

```sql
CREATE TRIGGER trg_prevenir_borrado_logs
BEFORE DELETE ON logs_modificaciones
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN OLD.fecha > datetime('now', '-1 day') 
        THEN RAISE(ABORT, 'No se pueden borrar logs recientes')
    END;
END;
```

---

### El Trigger de Héctor

Elisa examinó el trigger que Héctor había creado:

```sql
CREATE TRIGGER trg_auditar_transferencias
AFTER INSERT ON transacciones
FOR EACH ROW
BEGIN
    INSERT INTO auditoria_oculta 
        (transaccion_id, usuario, monto, ip_origen, fecha, hash)
    VALUES (NEW.id, 
            (SELECT usuario FROM conexiones WHERE ip = NEW.ip_creacion ORDER BY fecha DESC LIMIT 1),
            NEW.monto, NEW.ip_creacion, datetime('now'),
            hex(randomblob(16)));
END;
```

Héctor había creado una tabla `auditoria_oculta` que registraba cada transacción junto con el usuario real que la realizó, identificado por su IP. Y el trigger no se podía borrar fácilmente porque estaba protegido.

Elisa consultó la tabla:

```sql
SELECT * FROM auditoria_oculta
WHERE fecha > '2026-07-01'
ORDER BY fecha;
```

Los registros mostraban que cada transacción de Marta Robles estaba vinculada a una IP: la misma IP que aparecía en las conexiones del subdirector Vilaró. Pero había algo más: en las transacciones realizadas después de las 22:00 del 14 de julio, el usuario registrado era `hblasco`, pero la IP era la de Vilaró.

—Vilaró usó la cuenta de Héctor —dijo Elisa—. Y Marta ejecutó las órdenes. Pero el trigger lo registró todo.

—Tenemos el caso —dijo Rovira.

—Casi. Necesito saber por qué.

---

### Enigma SQL #11: El Guardián Silencioso

1. Crea un trigger que registre en una tabla `log_eliminaciones` cada vez que alguien intente borrar un registro de la tabla `transacciones`.
2. ¿Qué información registró el trigger `trg_auditar_transferencias` sobre las transacciones del 14 de julio?
3. Crea un trigger que impida que alguien modifique el campo `monto` de una transacción si esta ya fue confirmada (campo `estado = 'CONFIRMADA'`).

```sql
-- Tus consultas aquí
```
