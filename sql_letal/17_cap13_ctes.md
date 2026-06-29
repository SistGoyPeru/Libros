# Capítulo 13: El Último Query (Parte 1)

—Proyecto Talos —dijo Elisa, proyectando el esquema en la pantalla—. No existe en los registros oficiales, pero consumió 2.3 millones de euros en dos años.

—¿Para qué? —preguntó el inspector jefe.

—No lo sé. Pero Héctor lo descubrió. Y por eso está muerto.

Elisa necesitaba reconstruir los datos completos de Talos. Las tablas estaban fragmentadas, los logs parcialmente borrados. Era como armar un rompecabezas con piezas faltantes.

Necesitaba una consulta que uniera todo: transacciones, accesos, personal, modificaciones. Pero también necesitaba cálculos complejos y datos ordenados jerárquicamente.

—Hora de usar CTEs —dijo Elisa.

---

## Concepto SQL: CTEs (Common Table Expressions)

Un **CTE** es una tabla temporal definida dentro de una consulta. Es como una vista desechable que existe solo durante la ejecución.

### CTE simple

```sql
WITH transferencias_sospechosas AS (
    SELECT * FROM transacciones
    WHERE monto > 100000
      AND beneficiario NOT IN (
          SELECT codigo FROM proveedores_autorizados
      )
)
SELECT t.*, p.nombre as aprobador_nombre
FROM transferencias_sospechosas t
JOIN personal p ON t.aprobador = p.codigo;
```

### Múltiples CTEs

```sql
WITH
accesos_nocturnos AS (
    SELECT * FROM accesos
    WHERE strftime('%H', fecha) BETWEEN '22' AND '06'
),
transacciones_recientes AS (
    SELECT * FROM transacciones
    WHERE fecha > '2026-01-01'
)
SELECT a.usuario, a.fecha, t.id as transaccion_id, t.monto
FROM accesos_nocturnos a
JOIN transacciones_recientes t ON a.usuario = t.usuario_creacion
  AND date(a.fecha) = date(t.fecha)
ORDER BY a.fecha DESC;
```

### CTE con agregaciones

```sql
WITH
estadisticas_usuario AS (
    SELECT usuario, 
           COUNT(*) as total_accesos,
           COUNT(DISTINCT date(fecha)) as dias_activo
    FROM accesos
    GROUP BY usuario
)
SELECT p.nombre, e.total_accesos, e.dias_activo,
       ROUND(CAST(e.total_accesos AS REAL) / e.dias_activo, 1) as accesos_por_dia
FROM estadisticas_usuario e
JOIN personal p ON e.usuario = p.codigo
ORDER BY accesos_por_dia DESC;
```

### CTEs recursivos

Los CTEs recursivos se usan para datos jerárquicos (organigramas, árboles):

```sql
-- Organigrama del ICB
WITH RECURSIVE organigrama AS (
    -- Caso base: el director
    SELECT codigo, nombre, jefe_codigo, 0 as nivel
    FROM personal
    WHERE jefe_codigo IS NULL
    
    UNION ALL
    
    -- Paso recursivo: subordinados
    SELECT p.codigo, p.nombre, p.jefe_codigo, o.nivel + 1
    FROM personal p
    JOIN organigrama o ON p.jefe_codigo = o.codigo
)
SELECT * FROM organigrama ORDER BY nivel, nombre;
```

---

### La Consulta Final

Elisa construyó un CTE complejo para reunir todas las piezas:

```sql
WITH
accesos_sospechosos AS (
    SELECT usuario, fecha, ip_origen
    FROM accesos
    WHERE laboratorio = 7
      AND fecha > '2026-06-01'
),
transacciones_sospechosas AS (
    SELECT id, monto, fecha, usuario_creacion, 
           beneficiario, proyecto_asociado
    FROM transacciones_ocultas
    WHERE monto > 50000
),
modificaciones_sospechosas AS (
    SELECT usuario, tabla, fecha_modificacion, ip_origen
    FROM logs_modificaciones
    WHERE tabla IN ('transacciones', 'inventario_quimico', 'cerbero_config')
      AND fecha_modificacion > '2026-06-01'
),
linea_tiempo AS (
    SELECT fecha, 'acceso' as evento, usuario, NULL as detalle
    FROM accesos_sospechosos
    UNION ALL
    SELECT fecha, 'transaccion' as evento, usuario_creacion, 
           CAST(monto AS TEXT) as detalle
    FROM transacciones_sospechosas
    UNION ALL
    SELECT fecha_modificacion as fecha, 'modificacion' as evento, 
           usuario, tabla as detalle
    FROM modificaciones_sospechosas
)
SELECT fecha, evento, usuario, detalle
FROM linea_tiempo
ORDER BY fecha;
```

El resultado mostraba una coreografía perfecta: accesos, transacciones y modificaciones se sucedían en secuencia, como un ballet planeado. Y en el centro de todo, dos nombres: Marta Robles y Albert Vilaró.

Pero faltaba una pieza. Entre las transacciones de Talos, una se destacaba:

| Monto | Fecha | Beneficiario |
|-------|-------|-------------|
| 750,000 EUR | 2026-07-14 20:30 | SwissCredit AG |

—Esa transferencia se ejecutó antes del asesinato —dijo Elisa—. Y el beneficiario no es el ICB. Es una cuenta personal.

—¿De quién? —preguntó Rovira.

—Aún no lo sé. Pero voy a descubrirlo.

---

### Enigma SQL #13: Reconstruyendo la Verdad

1. Usando CTEs, crea una consulta que liste todos los eventos del 14 de julio de 2026 ordenados cronológicamente: accesos, transacciones y modificaciones.
2. Con un CTE recursivo, construye el organigrama del ICB y encuentra a qué nivel está Vilaró respecto al director.
3. ¿Cuánto dinero total se transfirió al proyecto Talos? Usa un CTE para calcularlo.

```sql
-- Tus consultas aquí
```
