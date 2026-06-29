# Capítulo 8: La Vista del Pasado

—El dinero iba al ICB —confirmó el subdirector Vilaró, un hombre calvo de 55 años con traje impecable—. Pero no es lo que parece. Era un fondo de contingencia para operaciones de ciberseguridad. Aprobado por el consejo.

—¿Por qué estaba oculto? —preguntó Elisa.

—No estaba oculto. Estaba... protegido. Si alguien accedía a la información sin autorización, los datos se auto-borrarían.

Elisa no le creyó. Volvió a su terminal y decidió crear una estructura de consulta que simplificara su investigación: una **vista** (VIEW).

Una vista es como una consulta guardada que puedes usar como si fuera una tabla. No almacena datos, sino la definición de cómo obtenerlos.

---

## Concepto SQL: Vistas (VIEWs)

Una **vista** es una tabla virtual basada en el resultado de una consulta. Simplifica consultas complejas y añade una capa de seguridad.

### Crear una vista

```sql
-- Vista simple
CREATE VIEW v_accesos_recientes AS
SELECT usuario, fecha, puerta, acceso_concedido
FROM accesos
WHERE fecha > DATE('now', '-30 days')
ORDER BY fecha DESC;

-- Usar la vista como una tabla
SELECT * FROM v_accesos_recientes;
SELECT usuario, COUNT(*) FROM v_accesos_recientes
WHERE acceso_concedido = 0
GROUP BY usuario;
```

### Vista con JOINs

```sql
CREATE VIEW v_investigacion_completa AS
SELECT a.id, a.fecha, a.usuario, p.nombre as nombre_personal,
       p.departamento, a.puerta, a.acceso_concedido
FROM accesos a
JOIN personal p ON a.usuario = p.codigo;
```

### Vista con agregaciones

```sql
CREATE VIEW v_estadisticas_accesos AS
SELECT usuario, 
       COUNT(*) as total_accesos,
       SUM(CASE WHEN acceso_concedido = 0 THEN 1 ELSE 0 END) as fallos,
       ROUND(AVG(CAST(strftime('%H', fecha) AS REAL)), 1) as hora_promedio
FROM accesos
GROUP BY usuario;
```

### ¿Vista o tabla?

| Vista | Tabla |
|-------|-------|
| No ocupa espacio (solo la definición) | Ocupa espacio |
| Siempre datos actualizados | Datos estáticos hasta que se modifican |
| No se puede indexar directamente | Se puede indexar |
| Útil para seguridad (ocultar columnas) | Expone toda la estructura |

### Eliminar una vista

```sql
DROP VIEW IF EXISTS v_investigacion_completa;
```

---

### La Vista que lo Cambió Todo

Elisa creó una vista que reunía toda la información dispersa:

```sql
CREATE VIEW v_caso_blasco AS
SELECT a.fecha as fecha_acceso, a.usuario, a.puerta,
       p.nombre, p.departamento, p.cargo,
       t.monto, t.beneficiario, t.fecha as fecha_transaccion
FROM accesos a
JOIN personal p ON a.usuario = p.codigo
LEFT JOIN transacciones_ocultas t ON t.fecha BETWEEN 
    datetime(a.fecha, '-1 hour') AND datetime(a.fecha, '+1 hour')
WHERE a.laboratorio = 7
  AND a.fecha > '2026-06-01';
```

La vista reveló algo que las consultas individuales no mostraban: Marta Robles aparecía en el laboratorio exactamente 15 minutos antes de cada transacción grande. Y el subdirector Vilaró... nunca aparecía en los accesos, pero sus credenciales de administrador se usaban para aprobar las transferencias.

—Vilaró es el jefe de Marta —dijo Rovira—. Podría estar encubriéndola.

—O ella podría estar trabajando para él —respondió Elisa.

---

### Enigma SQL #8: La Investigación Simplificada

1. Crea una vista que muestre todos los accesos al laboratorio 7 de empleados del departamento de "Sistemas" durante junio y julio de 2026.
2. Usando la vista `v_investigacion_completa` (o creando la tuya), encuentra qué empleados accedieron tanto al laboratorio 7 como al almacén de químicos en el mismo día.
3. ¿Cuántos accesos realizó cada departamento al laboratorio 7? Usa una vista para responder.

```sql
-- Tus consultas aquí
```
