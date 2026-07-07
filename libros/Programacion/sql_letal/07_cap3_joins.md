# Capítulo 3: Las Tablas del Engaño

Elisa pasó la mañana revisando los logs. La tabla `cerbero_config` existía, pero cuando intentó consultarla:

```sql
SELECT * FROM cerbero_config;
```

El resultado fue un error: *"table not found"*.

—La borraron —dijo Rovira.

—No —respondió Elisa—. Está en otra base de datos. Héctor usaba múltiples instancias. Necesito encontrar la conexión.

En el sistema de archivos del profesor encontró un archivo sospechoso: `conexion_secreta.db`. Lo copió y lo montó en su estación de trabajo.

```sql
SELECT * FROM cerbero_config;
```

Finalmente, datos:

| id | clave | valor | fecha_modificacion | nivel |
|----|-------|-------|-------------------|-------|
| 1 | db_host | 10.0.0.15 | 2026-06-01 | ALTO |
| 2 | db_user | admin_cerbero | 2026-06-01 | ALTO |
| 3 | db_pass | ENCRYPTED | 2026-06-01 | ALTO |
| 4 | umbral_seguridad | 0.95 | 2026-06-15 | CRÍTICO |
| 5 | umbral_seguridad_anterior | 0.50 | 2026-06-15 | ALTO |

—El umbral de seguridad se duplicó —observó Elisa—. ¿Por qué?

—¿Qué significa? —preguntó Rovira.

—Cerbero es un sistema de control de acceso biométrico. El umbral determina cuán estricta es la verificación. 0.50 es el estándar. 0.95 es... paranoico.

Rovira frunció el ceño.

—O alguien quería asegurarse de que solo cierta persona pudiera acceder.

Elisa sonrió. Ahora necesitaba cruzar esta información con los registros de acceso.

---

## Concepto SQL: JOINs

Hasta ahora hemos trabajado con una sola tabla. Pero los datos reales están dispersos en múltiples tablas relacionadas. Para combinarlos, usamos **JOIN**.

### INNER JOIN

Devuelve solo las filas que tienen correspondencia en ambas tablas:

```sql
SELECT e.nombre, e.fecha, a.usuario, a.accion
FROM experimentos e
INNER JOIN logs_acceso a ON e.investigador = a.usuario;
```

### LEFT JOIN

Devuelve todas las filas de la tabla izquierda, y las correspondientes de la derecha (NULL si no hay match):

```sql
SELECT e.nombre, c.clave, c.valor
FROM experimentos e
LEFT JOIN cerbero_config c ON e.proyecto = 'Cerbero';
```

### Tablas y alias

Usamos alias (`e`, `a`, `c`) para acortar los nombres de las tablas. El patrón es:

```sql
SELECT alias.columna
FROM tabla1 alias1
JOIN tabla2 alias2 ON alias1.id = alias2.id;
```

### Tipos de JOIN

```sql
-- INNER JOIN: solo coincidencias
SELECT * FROM A INNER JOIN B ON A.id = B.id;

-- LEFT JOIN: todo de A, lo que coincida de B
SELECT * FROM A LEFT JOIN B ON A.id = B.id;

-- RIGHT JOIN: todo de B, lo que coincida de A
SELECT * FROM A RIGHT JOIN B ON A.id = B.id;

-- FULL JOIN: todo de ambas tablas
SELECT * FROM A FULL JOIN B ON A.id = B.id;
```

---

### La Conexión

Elisa unió las tablas de acceso con la configuración de Cerbero:

```sql
SELECT a.usuario, a.fecha, a.puerta, c.valor as umbral
FROM logs_acceso a
JOIN cerbero_config c ON c.clave = 'umbral_seguridad'
WHERE a.fecha > c.fecha_modificacion
  AND a.acceso_concedido = 1
ORDER BY a.fecha DESC;
```

El resultado mostraba que solo dos personas accedieron al laboratorio después del cambio de umbral: el Dr. Blasco y una cuenta llamada `mrobles`.

—Marta Robles —leyó Rovira—. La asistente del profesor.

—Llamémosla para interrogarla —dijo Elisa.

Pero cuando marcaron su número, la llamada entró directamente al buzón de voz.

---

### Enigma SQL #3: ¿Quién más sabía?

Usando joins entre las tablas `personal`, `accesos` y `experimentos`:

1. ¿Qué otros investigadores tenían acceso al proyecto Cerbero?
2. Lista todos los accesos al laboratorio 7 ocurridos durante el mes de junio de 2026, mostrando el nombre del empleado y la puerta.
3. Encuentra a las personas que accedieron al laboratorio pero NO están registradas como investigadoras en el proyecto Cerbero.

```sql
-- Tus consultas aquí
```
