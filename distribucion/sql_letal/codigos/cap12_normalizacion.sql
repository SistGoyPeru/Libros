-- Capítulo 12: La Normalización del Caos
-- Conceptos: 1NF, 2NF, 3NF, diseño de esquemas

-- MAL: múltiples valores en una celda (viola 1NF)
CREATE TABLE proyectos_mal (
    id INT,
    investigador TEXT,  -- "Elisa, Marta, Héctor"
    PRIMARY KEY (id)
);

-- BIEN: tabla separada (1NF)
CREATE TABLE proyecto_investigadores (
    proyecto_id INT REFERENCES proyectos(id),
    investigador_codigo TEXT REFERENCES personal(codigo),
    PRIMARY KEY (proyecto_id, investigador_codigo)
);

-- MAL: dependencia parcial (viola 2NF)
CREATE TABLE proyecto_asignaciones_mal (
    proyecto_id INT,
    investigador_codigo TEXT,
    proyecto_nombre TEXT,  -- Depende solo de proyecto_id
    PRIMARY KEY (proyecto_id, investigador_codigo)
);

-- BIEN: separar en tablas (2NF)
CREATE TABLE proyectos (
    id INT PRIMARY KEY,
    nombre TEXT
);

-- MAL: dependencia transitiva (viola 3NF)
CREATE TABLE personal_mal (
    codigo TEXT PRIMARY KEY,
    nombre TEXT,
    departamento_codigo TEXT,
    departamento_nombre TEXT  -- Depende de departamento_codigo
);

-- BIEN: tabla separada (3NF)
CREATE TABLE departamentos (
    codigo TEXT PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE personal_bien (
    codigo TEXT PRIMARY KEY,
    nombre TEXT,
    departamento_codigo TEXT REFERENCES departamentos(codigo)
);

-- Investigación: proyectos fantasma
SELECT DISTINCT proyecto_asociado FROM transacciones_ocultas;

-- Proyectos con transacciones pero sin registro oficial
SELECT DISTINCT t.proyecto_asociado
FROM transacciones_ocultas t
WHERE t.proyecto_asociado NOT IN (
    SELECT nombre FROM proyectos
);
