# Capítulo 9: La Transacción Perfecta

Elisa tenía suficiente para un arresto, pero necesitaba la pieza final: la conexión entre Vilaró y el laboratorio. No había registros de acceso físico, pero tenía que haber alguna comunicación.

Revisó los logs de la base de datos del sistema financiero. Encontró algo: transacciones realizadas desde la cuenta de Vilaró que coincidían exactamente con accesos a la base de datos desde la IP del laboratorio.

—Hacía transferencias desde el laboratorio —dijo Elisa—. Las programaba y luego borraba los logs.

Pero faltaba algo. Las transacciones se realizaban pero no se completaban. Elisa abrió los registros de transacciones de la base de datos.

---

## Concepto SQL: Transacciones

Una **transacción** es un conjunto de operaciones que se ejecutan como una unidad. O se completan todas, o ninguna. Es la base de la integridad de los datos.

### ACID

Las bases de datos relacionales garantizan cuatro propiedades:

- **Atomicidad**: Todo se ejecuta o nada se ejecuta.
- **Consistencia**: Los datos siempre están en un estado válido.
- **Aislamiento**: Las transacciones concurrentes no interfieren.
- **Durabilidad**: Una vez confirmada, la transacción persiste.

### BEGIN, COMMIT, ROLLBACK

```sql
-- Iniciar una transacción
BEGIN TRANSACTION;

-- Operaciones
UPDATE cuentas SET saldo = saldo - 1000 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 1000 WHERE id = 2;

-- Si todo está bien, confirmar
COMMIT;

-- Si algo sale mal, deshacer
ROLLBACK;
```

### Ejemplo de aplicación bancaria

```sql
BEGIN TRANSACTION;

-- Verificar saldo suficiente
SELECT saldo FROM cuentas WHERE id = 1;
-- Resultado: 5000

-- Descontar
UPDATE cuentas SET saldo = saldo - 2000 WHERE id = 1;

-- Acreditar
UPDATE cuentas SET saldo = saldo + 2000 WHERE id = 2;

-- Verificar consistencia
SELECT SUM(saldo) FROM cuentas;
-- Debe ser el mismo valor que antes

COMMIT;
```

### Transacciones e integridad

```sql
-- Si ocurre un error, todo se deshace
BEGIN TRANSACTION;
INSERT INTO logs VALUES ('transferencia_iniciada', datetime('now'));
UPDATE cuentas SET saldo = saldo - 5000 WHERE id = 1;
-- Error: la cuenta 2 no existe
UPDATE cuentas SET saldo = saldo + 5000 WHERE id = 999;
ROLLBACK;
-- La cuenta 1 no perdió el dinero
```

### SAVEPOINT

```sql
-- Puntos de guardado dentro de una transacción
BEGIN TRANSACTION;
INSERT INTO logs VALUES ('inicio', datetime('now'));
SAVEPOINT despues_log;
UPDATE cuentas SET saldo = 0 WHERE id = 1;
-- Ups, no quería eso
ROLLBACK TO SAVEPOINT despues_log;
-- El log se mantiene, pero la actualización se deshizo
COMMIT;
```

---

### La Transacción Manipulada

Elisa encontró algo extraño en los logs de transacciones:

```sql
SELECT * FROM logs_transacciones
WHERE usuario = 'vilaro'
  AND fecha BETWEEN '2026-07-14 20:00' AND '2026-07-14 23:00'
ORDER BY fecha;
```

Una transacción llamada `PAGO_PROVEEDOR_AGO` se inició a las 22:15 y se confirmó a las 22:17. Pero no había registros intermedios.

—Dos minutos —murmuró Elisa—. Es muy rápido para una transferencia internacional.

Revisó los datos de la transferencia:

| Campo | Valor |
|-------|-------|
| Origen | ICB - Cuenta General |
| Destino | SwissCredit Bank - Cuenta 4423-XX |
| Monto | 500,000 EUR |
| Concepto | Servicios de consultoría |
| Aprobador | M. Robles |
| Ejecutor | H. Blasco (?) |

—Usaron la cuenta de Héctor para ejecutar la transacción —dijo Elisa—. Y la aprobó Marta.

—Pero si Héctor estaba muerto a las 22:15... —dijo Rovira.

—Exacto. La transacción se ejecutó después de su muerte. O alguien la programó, o... Héctor seguía vivo a las 22:17.

Elisa sintió un escalofrío.

---

### Enigma SQL #9: La Cadena de Transacciones

1. Simula una transacción que transfiera 500,000 EUR de una cuenta a otra. Escribe el SQL completo con BEGIN, COMMIT y verificaciones.
2. ¿Cuántas transacciones en el sistema tienen un tiempo entre inicio y confirmación menor a 5 minutos? Esto podría indicar automatización.
3. Encuentra todas las transacciones que se ejecutaron con la cuenta de un usuario fallecido (después de su hora de muerte registrada).

```sql
-- Tus consultas aquí
```
