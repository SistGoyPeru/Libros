# Capítulo 4: El Grupo que Miente

Marta Robles apareció al día siguiente. Tenía 28 años, ojos inquietos y una respuesta preparada para todo.

—Sí, trabajaba con el doctor Blasco. Sí, sabía de Cerbero. No, no sé quién lo mató.

Elisa la observaba desde el otro lado de la mesa. Había algo en su lenguaje corporal que no encajaba. Demasiado controlada.

—¿Por qué accediste al laboratorio a las 3 de la madrugada del 15 de julio? —preguntó Elisa.

—Me olvidé el teléfono.

—Tu teléfono estaba en tu bolso, Marta. Lo vi en las imágenes de seguridad.

Marta tragó saliva.

—Está bien. Fui a revisar unos datos. El doctor me pidió que verificara los logs de Cerbero.

—¿A las 3 de la mañana?

—Era... urgente.

Después de la entrevista, Elisa volvió a su terminal. Algo no cuadraba. Decidió analizar los patrones de acceso de Marta usando agregaciones SQL.

---

## Concepto SQL: GROUP BY y funciones de agregación

Hasta ahora hemos visto filas individuales. Pero a menudo necesitamos **resumir** datos: contar, sumar, promediar. Para eso usamos **GROUP BY** junto con funciones de agregación.

### Funciones de agregación

```sql
-- COUNT: contar filas
SELECT COUNT(*) FROM accesos;
SELECT COUNT(DISTINCT usuario) FROM accesos;

-- SUM: sumar valores numéricos
SELECT SUM(duracion_minutos) FROM sesiones;

-- AVG: promedio
SELECT AVG(duracion_minutos) FROM sesiones;

-- MAX / MIN: valores máximo y mínimo
SELECT MAX(intentos_fallidos) FROM accesos;
SELECT MIN(intentos_fallidos) FROM accesos;
```

### GROUP BY: Agrupar datos

```sql
-- Contar accesos por usuario
SELECT usuario, COUNT(*) as total_accesos
FROM accesos
GROUP BY usuario;

-- Promedio de duración por día
SELECT DATE(fecha) as dia, AVG(duracion) as promedio
FROM sesiones
GROUP BY DATE(fecha);

-- Múltiples niveles de agrupación
SELECT usuario, puerta, COUNT(*) as veces
FROM accesos
GROUP BY usuario, puerta;
```

### HAVING: Filtrar grupos

WHERE filtra filas **antes** de agrupar. HAVING filtra grupos **después** de agrupar:

```sql
-- Usuarios con más de 50 accesos
SELECT usuario, COUNT(*) as total
FROM accesos
GROUP BY usuario
HAVING COUNT(*) > 50;

-- Días con más de 10 accesos fallidos
SELECT DATE(fecha) as dia, COUNT(*) as fallos
FROM accesos
WHERE acceso_concedido = 0
GROUP BY DATE(fecha)
HAVING COUNT(*) > 10;
```

---

### El Patrón

Elisa agrupó los accesos de Marta y encontró algo extraño:

```sql
SELECT usuario, 
       DATE(fecha) as dia,
       COUNT(*) as accesos,
       MIN(fecha) as primero,
       MAX(fecha) as ultimo
FROM accesos
WHERE usuario = 'mrobles'
GROUP BY usuario, DATE(fecha)
HAVING COUNT(*) > 3
ORDER BY dia;
```

El resultado mostraba que Marta accedía al laboratorio en bloques: varios accesos en pocos minutos, como si estuviera entrando y saliendo repetidamente. O como si estuviera... borrando algo.

Pero además, había un detalle más inquietante: los días que Marta tenía más accesos coincidían exactamente con los días en que el Dr. Blasco estaba fuera del instituto en conferencias.

—Marta sabía cuándo Héctor no estaría —murmuró Elisa—. Y usaba ese tiempo para... ¿qué?

---

### Enigma SQL #4: La Agenda Oculta

1. ¿Cuántos accesos al laboratorio 7 realizó cada empleado durante el mes de junio? Ordena de mayor a menor.
2. ¿Qué días hubo más de 5 accesos fallidos en total (todos los usuarios)?
3. Calcula el promedio de accesos por hora del día. ¿Hay una hora con actividad inusual?

```sql
-- Tus consultas aquí
```
