# Capítulo 2: La Condición del Sospechoso

—No entiendo —dijo el inspector Rovira, frotándose la barbilla—. El forense insiste en que fue un infarto. Sin signos de violencia.

Elisa estaba frente al ordenador del profesor, revisando los archivos del sistema.

—Mira esto —señaló la pantalla—. Héctor tenía un proyecto secreto. Lo llamó "Proyecto Cerbero".

—¿Qué es?

—No lo sé. Pero hay experimentos que no aparecen en la base de datos principal. Héctor los escondió.

Elisa abrió una terminal y escribió:

```sql
SELECT * FROM experimentos WHERE proyecto = 'Cerbero';
```

La consulta devolvió cero resultados.

—No hay nada —dijo Rovira.

—O no estamos buscando bien. Déjame pensar.

Elisa sabía que su mentor era meticuloso. Si había creado algo llamado Cerbero, los datos tenían que estar en alguna parte. Quizás no era una tabla independiente, sino registros filtrados por alguna condición.

Recordó una conversación con Héctor semanas atrás: *"Elisa, la condición WHERE es la diferencia entre encontrar la verdad y perderte en el ruido."*

---

## Concepto SQL: WHERE y condiciones

La cláusula **WHERE** filtra filas según una condición. Solo las filas que cumplen la condición aparecen en el resultado.

```sql
-- Filtrar por un valor exacto
SELECT * FROM experimentos WHERE proyecto = 'Cerbero';

-- Filtrar por número
SELECT * FROM experimentos WHERE id > 10;

-- Múltiples condiciones con AND
SELECT * FROM experimentos 
WHERE proyecto = 'Cerbero' AND resultado = 'éxito';

-- Múltiples condiciones con OR
SELECT * FROM experimentos 
WHERE proyecto = 'Cerbero' OR proyecto = 'Fénix';

-- Negar una condición
SELECT * FROM experimentos 
WHERE NOT resultado = 'fallo';
```

### Operadores de comparación

| Operador | Significado | Ejemplo |
|----------|------------|---------|
| `=` | Igual a | `WHERE nombre = 'Blasco'` |
| `<>` o `!=` | Distinto de | `WHERE resultado != 'fallo'` |
| `>` | Mayor que | `WHERE id > 100` |
| `<` | Menor que | `WHERE fecha < '2026-07-01'` |
| `>=` | Mayor o igual | `WHERE version >= 2.0` |
| `<=` | Menor o igual | `WHERE intentos <= 3` |

### Operadores especiales

```sql
-- BETWEEN: valores en un rango
SELECT * FROM experimentos 
WHERE fecha BETWEEN '2026-01-01' AND '2026-06-30';

-- IN: valores dentro de una lista
SELECT * FROM experimentos 
WHERE investigador IN ('Blasco', 'Riera', 'Valls');

-- LIKE: búsqueda con patrones
SELECT * FROM experimentos 
WHERE nombre LIKE 'Proyecto%';  -- Empieza con "Proyecto"

-- IS NULL: valores nulos
SELECT * FROM experimentos 
WHERE fecha_fin IS NULL;
```

---

### El Descubrimiento

Elisa probó otra consulta:

```sql
SELECT * FROM logs_acceso 
WHERE usuario = 'hblasco' AND accion LIKE 'CREATE TABLE%';
```

La base de datos devolvió un registro: el profesor había creado una tabla llamada `cerbero_config` hacía tres meses, a las 2:47 de la madrugada.

—Trabajaba de noche —murmuró Elisa—. ¿Qué escondía, Héctor?

---

### Enigma SQL #2: El Rastro del Profesor

Usando la base de datos del ICB:

1. Encuentra todos los accesos al laboratorio realizados por el Dr. Blasco después de las 22:00 (10 PM).
2. ¿Cuántos experimentos tienen resultado NULL (inconcluso)?
3. Lista los proyectos que contienen la palabra "Cerbero" en su nombre.

```sql
-- Tus consultas aquí
```
