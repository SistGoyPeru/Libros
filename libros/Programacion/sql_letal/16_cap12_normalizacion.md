# Capítulo 12: La Normalización del Caos

Elisa tenía la evidencia técnica, pero aún no entendía el motivo. ¿Por qué Vilaró, un subdirector bien pagado, arriesgaría su carrera y su libertad?

Decidió analizar la estructura de datos del instituto. Necesitaba entender cómo se relacionaban todas las piezas. La base de datos del ICB era un laberinto de tablas mal diseñadas, redundancias y datos inconsistentes.

—Esto es un desastre —murmuró Elisa—. Los mismos datos en múltiples tablas, nombres inconsistentes...

—¿Importa eso? —preguntó Rovira.

—Importa más de lo que crees. Una base de datos bien diseñada revela la verdad. Una mal diseñada la oculta.

---

## Concepto SQL: Normalización

La **normalización** es el proceso de organizar datos para reducir redundancia y mejorar integridad. Se divide en "formas normales".

### Primera Forma Normal (1NF)

Cada celda debe contener un solo valor. No listas ni arreglos.

```sql
-- MAL: múltiples valores en una celda
CREATE TABLE proyectos (
    id INT,
    investigador TEXT, -- "Elisa, Marta, Héctor"
    PRIMARY KEY (id)
);

-- BIEN: cada valor en su propia fila
CREATE TABLE proyectos (
    id INT,
    investigador TEXT,
    PRIMARY KEY (id, investigador)
);

-- O mejor: tabla separada
CREATE TABLE proyecto_investigadores (
    proyecto_id INT,
    investigador_codigo TEXT,
    PRIMARY KEY (proyecto_id, investigador_codigo)
);
```

### Segunda Forma Normal (2NF)

Cada columna no clave debe depender de la clave completa, no solo de parte de ella.

```sql
-- MAL: depende solo del proyecto, no de (proyecto, investigador)
CREATE TABLE proyecto_asignaciones (
    proyecto_id INT,
    investigador_codigo TEXT,
    proyecto_nombre TEXT, -- Depende solo de proyecto_id
    PRIMARY KEY (proyecto_id, investigador_codigo)
);

-- BIEN: separar en tablas
CREATE TABLE proyectos (
    id INT PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE proyecto_asignaciones (
    proyecto_id INT REFERENCES proyectos(id),
    investigador_codigo TEXT REFERENCES personal(codigo),
    PRIMARY KEY (proyecto_id, investigador_codigo)
);
```

### Tercera Forma Normal (3NF)

Las columnas no clave no deben depender de otras columnas no clave.

```sql
-- MAL: departamento_nombre depende de departamento_codigo
CREATE TABLE personal (
    codigo TEXT PRIMARY KEY,
    nombre TEXT,
    departamento_codigo TEXT,
    departamento_nombre TEXT
);

-- BIEN: tabla separada para departamentos
CREATE TABLE departamentos (
    codigo TEXT PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE personal (
    codigo TEXT PRIMARY KEY,
    nombre TEXT,
    departamento_codigo TEXT REFERENCES departamentos(codigo)
);
```

### Normalizando el ICB

Elisa encontró múltiples problemas en la base de datos del instituto:

1. **Tabla `personal`** tenía el nombre del departamento repetido para cada empleado.
2. **Tabla `accesos`** guardaba el nombre completo del empleado, no solo su código.
3. **Tabla `proyectos`** tenía una columna con IDs separados por comas.

—Un diseño así permite inconsistencias —explicó Elisa—. Y las inconsistencias son donde se esconden los fraudes.

### Problemas comunes de diseño

| Problema | Síntoma |
|----------|---------|
| Redundancia | Mismos datos en múltiples filas |
| Anomalía de actualización | Cambiar un valor requiere múltiples UPDATEs |
| Anomalía de inserción | No puedes crear un registro sin otro relacionado |
| Anomalía de borrado | Borrar un registro elimina datos no relacionados |

---

### La Revelación

Mientras normalizaba la base de datos mentalmente, Elisa se dio cuenta de algo. La tabla `transacciones_ocultas` tenía una columna llamada `proyecto_asociado`. Consultó:

```sql
SELECT DISTINCT proyecto_asociado FROM transacciones_ocultas;
```

Los proyectos eran: Cerbero, Ícaro, Fénix... y uno más: **Talos**.

—¿Qué es Talos? —preguntó Rovira.

Elisa buscó en la base de datos:

```sql
SELECT * FROM proyectos WHERE nombre = 'Talos';
```

No había registros. El proyecto no existía en la tabla oficial. Pero las transacciones sí lo mencionaban.

—Talos es el proyecto fantasma —dijo Elisa—. Un proyecto que no existe oficialmente pero que consume fondos. Vilaró creó un proyecto falso para desviar dinero.

—¿Y Héctor lo descubrió?

—Talos es el motivo del asesinato.

---

### Enigma SQL #12: Diseñando la Verdad

1. ¿Qué anomalías de diseño encuentras en la tabla `accesos` si almacena `nombre_completo` en lugar de solo `usuario_codigo`? Propón una estructura normalizada.
2. Crea una consulta que detecte proyectos con transacciones pero sin registro en la tabla oficial `proyectos`.
3. Si tuvieras que rediseñar la base de datos del ICB desde cero, ¿qué tablas crearías y qué relaciones tendrían? Escribe el esquema SQL.

```sql
-- Tus consultas aquí
```
