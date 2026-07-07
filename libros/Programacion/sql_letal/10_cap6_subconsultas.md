# Capítulo 6: La Subconsulta Asesina

—La cuenta de Héctor fue usada después de su muerte —dijo Elisa frente al panel de investigadores—. Pero no fue Marta. La IP de conexión es diferente.

—¿Qué IP? —preguntó Rovira.

—Una dirección externa. Alguien se conectó desde fuera del instituto.

—¿Puedes rastrearla?

Elisa asintió. Primero necesitaba aislar todas las conexiones sospechosas de las legítimas. Decidió usar subconsultas.

---

## Concepto SQL: Subconsultas

Una **subconsulta** es una consulta dentro de otra consulta. Sirve para realizar operaciones en múltiples pasos dentro de una sola instrucción SQL.

### Subconsulta en WHERE

```sql
-- Encontrar usuarios que accedieron después del crimen
SELECT * FROM accesos
WHERE usuario IN (
    SELECT DISTINCT usuario 
    FROM logs_modificaciones
    WHERE fecha_modificacion > '2026-07-15 05:30'
);
```

### Subconsulta con comparación

```sql
-- Accesos con duración mayor al promedio
SELECT * FROM accesos
WHERE duracion > (
    SELECT AVG(duracion) FROM accesos
);
```

### Subconsulta en SELECT

```sql
-- Mostrar cada acceso junto al total de accesos del usuario
SELECT a.*, (
    SELECT COUNT(*) 
    FROM accesos a2 
    WHERE a2.usuario = a.usuario
) as total_usuario
FROM accesos a;
```

### EXISTS / NOT EXISTS

```sql
-- Usuarios que tienen al menos un acceso nocturno
SELECT DISTINCT usuario FROM personal p
WHERE EXISTS (
    SELECT 1 FROM accesos a
    WHERE a.usuario = p.codigo
      AND strftime('%H', a.fecha) BETWEEN '22' AND '06'
);

-- Usuarios sin accesos después del crimen
SELECT * FROM personal p
WHERE NOT EXISTS (
    SELECT 1 FROM accesos a
    WHERE a.usuario = p.codigo
      AND a.fecha > '2026-07-15 05:30'
);
```

### Subconsultas anidadas

```sql
-- La IP con más accesos sospechosos
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
```

---

### La IP Fantasma

Elisa ejecutó una subconsulta para encontrar la IP del intruso:

```sql
SELECT ip_origen, COUNT(*) as operaciones
FROM logs_modificaciones
WHERE fecha_modificacion > '2026-07-15 05:30'
  AND usuario = 'hblasco'
GROUP BY ip_origen;
```

Solo una IP: `185.23.47.101`.

—Está en Rusia —dijo Rovira—. O al menos usa un VPN que lo parece.

—No —dijo Elisa—. Mira más de cerca. La IP aparece antes del crimen también, pero con otro usuario.

Ejecutó:

```sql
SELECT * FROM conexiones
WHERE ip_origen = '185.23.47.101'
  AND fecha < '2026-07-15 05:30'
ORDER BY fecha DESC
LIMIT 5;
```

Las conexiones mostraban al usuario `mrobles`. Marta Robles se conectaba desde la misma IP sospechosa.

—Marta no está diciendo toda la verdad —concluyó Rovira.

—O alguien más usa la IP de Marta —dijo Elisa.

---

### Enigma SQL #6: La Red Oculta

1. Encuentra todos los usuarios que se conectaron desde IPs externas (que no son del rango 10.0.0.x) después del crimen.
2. ¿Cuántas IPs diferentes usó Marta Robles en los últimos 30 días?
3. Lista los usuarios cuyos accesos nocturnos (22:00-06:00) superan el promedio de accesos nocturnos del instituto.

```sql
-- Tus consultas aquí
```
