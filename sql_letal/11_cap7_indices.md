# Capítulo 7: El Índice Oculto

—Necesito mirar el disco duro del servidor —dijo Elisa.

—¿Qué esperas encontrar? —preguntó Rovira.

—Archivos residuales. Datos que alguien intentó borrar pero dejó rastros.

Elisa accedió al servidor de bases de datos del ICB. El sistema operativo mostraba un archivo sospechoso en `/tmp/datos_recuperados.sql`. Lo abrió.

Era un script SQL que creaba una tabla llamada `transacciones_ocultas`.

—Alguien volcó datos aquí y borró la tabla original —murmuró Elisa—. Pero el archivo temporal sobrevivió.

Ejecutó el script y consultó la tabla:

```sql
SELECT * FROM transacciones_ocultas;
```

La tabla tenía 10,847 registros. Transferencias bancarias. Del laboratorio Cerbero a cuentas en paraísos fiscales. La más reciente: 200,000 euros transferidos el 14 de julio a las 14:30.

—El día antes del asesinato —dijo Rovira.

—Y el beneficiario es...

Elisa ejecutó:

```sql
SELECT DISTINCT beneficiario, SUM(monto) as total
FROM transacciones_ocultas
GROUP BY beneficiario
ORDER BY total DESC;
```

El primer nombre en la lista la dejó sin aliento.

---

## Concepto SQL: Índices y optimización

Hasta ahora nos hemos enfocado en la sintaxis. Pero cuando trabajas con miles o millones de registros, la **velocidad** importa. Ahí entran los **índices**.

### ¿Qué es un índice?

Un índice es como el índice alfabético de un libro: en lugar de hojear todas las páginas para encontrar una palabra, vas directamente a la página.

```sql
-- Crear un índice en una columna
CREATE INDEX idx_accesos_usuario ON accesos(usuario);

-- Índice compuesto (múltiples columnas)
CREATE INDEX idx_accesos_fecha_usuario 
ON accesos(fecha, usuario);

-- Índice único (valores no repetidos)
CREATE UNIQUE INDEX idx_personal_email 
ON personal(email);

-- Ver los índices de una tabla
SELECT * FROM sqlite_master 
WHERE type = 'index' AND tbl_name = 'accesos';
```

### ¿Cuándo usa SQL un índice?

Las consultas con WHERE, JOIN, ORDER BY y GROUP BY se benefician de los índices:

```sql
-- Sin índice: revisa todas las filas (table scan)
SELECT * FROM transacciones WHERE beneficiario = 'X';

-- Con índice: busca directamente (index seek)
-- (crea el índice primero)
CREATE INDEX idx_beneficiario ON transacciones(beneficiario);
```

### EXPLAIN QUERY PLAN

Para ver si una consulta usa índices:

```sql
EXPLAIN QUERY PLAN
SELECT * FROM transacciones 
WHERE beneficiario = 'X' AND monto > 1000;
```

### Cuidado con los índices

```sql
-- Los índices aceleran lecturas pero ralentizan escrituras
-- No indexes todo, solo lo que consultas frecuentemente

-- Las funciones en columnas pueden hacer que los índices
-- no se usen (a menos que sean índices funcionales)
SELECT * FROM accesos WHERE strftime('%Y', fecha) = '2026';
-- Mejor:
SELECT * FROM accesos 
WHERE fecha >= '2026-01-01' AND fecha < '2027-01-01';
```

---

### La Tabla Oculta

Elisa se quedó mirando el resultado de la consulta. El nombre en la cima de la lista de beneficiarios era: **ICB - Instituto de Ciberseguridad de Barcelona**.

—El dinero iba al propio instituto —dijo—. Pero a una cuenta que no aparece en los registros oficiales.

—Una cuenta fantasma —completó Rovira.

—Héctor descubrió el desvío de fondos. Por eso lo mataron.

Pero entonces, ¿quién estaba detrás? Alguien con suficiente acceso para crear transacciones ocultas y borrar evidencias. Alguien desde dentro.

### Enigma SQL #7: El Rastro del Dinero

1. ¿Cuántas transacciones sospechosas hay por cada año?
2. Crea un índice en la columna `beneficiario` de la tabla `transacciones_ocultas` y verifica si la consulta `SELECT * FROM transacciones_ocultas WHERE beneficiario = 'ICB'` lo usa (con EXPLAIN QUERY PLAN).
3. Encuentra la transacción de mayor monto y todos sus detalles.

```sql
-- Tus consultas aquí
```
