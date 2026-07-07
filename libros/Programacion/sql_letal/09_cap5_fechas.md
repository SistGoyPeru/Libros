# Capítulo 5: La Fecha del Crimen

El forense entregó el informe definitivo: muerte por paro cardíaco inducido por una toxina llamada tetrodotoxina. Alguien la había administrado horas antes del deceso.

—Es una toxina que se encuentra en el pez globo —explicó Rovira—. Es indetectable en autopsias rutinarias. Si no la hubieran buscado específicamente...

—Alguien sabía medicina —completó Elisa.

Pero había un problema: según los registros de acceso, el Dr. Blasco estuvo solo en su laboratorio desde las 22:00 hasta que lo encontraron muerto a las 5:30. Nadie entró. Nadie salió.

—¿Cómo administraron la toxina? —preguntó Elisa en voz alta.

Revisó los logs de la base de datos con más atención. Algo llamó su atención: el profesor había recibido un paquete del almacén de químicos a las 21:45.

```sql
SELECT * FROM envios 
WHERE destinatario = 'Héctor Blasco'
  AND fecha BETWEEN '2026-07-14 20:00' AND '2026-07-14 22:00';
```

| id | remitente | destinatario | contenido | fecha_envio |
|----|-----------|-------------|-----------|-------------|
| 8932 | Almacén QCA | H. Blasco | Muestra T-47 | 2026-07-14 21:30 |

—¿Qué es la muestra T-47? —preguntó Elisa.

Hizo otra consulta:

```sql
SELECT * FROM inventario_quimico WHERE codigo LIKE 'T-%';
```

No había registros. Alguien había borrado la entrada.

—Marta —dijo Rovira.

—O alguien con acceso a la base de datos —corrigió Elisa.

Entonces recordó que la base de datos registraba fechas de modificación. Si alguien manipuló los datos después del crimen...

---

## Concepto SQL: Funciones de fecha y hora

Las fechas son cruciales en investigación forense. SQL ofrece potentes funciones para trabajar con ellas.

### Tipos de datos temporales

```sql
-- DATE: solo fecha (2026-07-14)
-- TIME: solo hora (21:45:00)
-- DATETIME / TIMESTAMP: fecha y hora (2026-07-14 21:45:00)
```

### Funciones de fecha

```sql
-- Fecha actual
SELECT DATE('now');
SELECT DATETIME('now');

-- Extraer partes
SELECT strftime('%Y', fecha) as año FROM tabla;  -- 2026
SELECT strftime('%m', fecha) as mes FROM tabla;  -- 07
SELECT strftime('%d', fecha) as dia FROM tabla;  -- 14
SELECT strftime('%H', fecha) as hora FROM tabla; -- 21
SELECT strftime('%w', fecha) as dia_sem FROM tabla; -- 0=domingo

-- Operaciones con fechas
SELECT DATE(fecha, '+1 day') as manana FROM tabla;
SELECT DATE(fecha, '-7 days') as semana_pasada FROM tabla;
SELECT DATETIME(fecha, '+2 hours') FROM tabla;
```

### WHERE con fechas

```sql
-- Rango de fechas
SELECT * FROM accesos 
WHERE fecha >= '2026-07-14 22:00' 
  AND fecha < '2026-07-15 06:00';

-- Filtrar por día de semana
SELECT * FROM accesos 
WHERE strftime('%w', fecha) = '0';  -- Domingos

-- Filtrar por hora
SELECT * FROM accesos 
WHERE strftime('%H', fecha) BETWEEN '22' AND '23';  -- 10-11 PM
```

---

### La Anomalía

Elisa ejecutó una consulta clave:

```sql
SELECT tabla, fecha_modificacion, usuario
FROM logs_modificaciones
WHERE tabla = 'inventario_quimico'
  AND fecha_modificacion > '2026-07-15 05:30'
ORDER BY fecha_modificacion DESC;
```

La consulta reveló que alguien modificó la tabla `inventario_quimico` a las **6:15 AM del 15 de julio** — 45 minutos después del hallazgo del cuerpo, cuando el laboratorio estaba sellado. El usuario era `hblasco`.

—Pero Héctor estaba muerto —susurró Elisa.

—Alguien usó su cuenta —dijo Rovira.

—O alguien sabía que iba a morir y programó la modificación.

---

### Enigma SQL #5: La Línea de Tiempo

1. Encuentra todos los registros de la tabla `logs_modificaciones` del día 15 de julio de 2026, ordenados por hora.
2. ¿Hubo modificaciones a la base de datos entre las 22:00 del 14 de julio y las 6:00 del 15 de julio, antes del hallazgo del cuerpo?
3. ¿Cuánto tiempo pasó entre la última modificación hecha por el usuario `hblasco` y la primera modificación hecha por `mrobles`?

```sql
-- Tus consultas aquí
```
