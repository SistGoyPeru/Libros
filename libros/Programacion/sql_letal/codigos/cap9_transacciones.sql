-- Capítulo 9: La Transacción Perfecta
-- Conceptos: BEGIN TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT

-- Transacción básica
BEGIN TRANSACTION;
UPDATE cuentas SET saldo = saldo - 1000 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 1000 WHERE id = 2;
COMMIT;

-- Transacción con ROLLBACK
BEGIN TRANSACTION;
UPDATE cuentas SET saldo = saldo - 5000 WHERE id = 1;
-- Error: la cuenta 2 no existe
UPDATE cuentas SET saldo = saldo + 5000 WHERE id = 999;
ROLLBACK;

-- Transacción con verificación
BEGIN TRANSACTION;
SELECT saldo FROM cuentas WHERE id = 1;
-- Si saldo >= 2000, continuar
UPDATE cuentas SET saldo = saldo - 2000 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 2000 WHERE id = 2;
SELECT SUM(saldo) FROM cuentas;  -- debe ser el mismo valor
COMMIT;

-- SAVEPOINT
BEGIN TRANSACTION;
INSERT INTO logs VALUES ('inicio', datetime('now'));
SAVEPOINT despues_log;
UPDATE cuentas SET saldo = 0 WHERE id = 1;
-- Deshacer solo la actualización
ROLLBACK TO SAVEPOINT despues_log;
-- El log se mantiene
COMMIT;

-- Investigación: logs de transacciones
SELECT * FROM logs_transacciones
WHERE usuario = 'vilaro'
  AND fecha BETWEEN '2026-07-14 20:00' AND '2026-07-14 23:00'
ORDER BY fecha;
