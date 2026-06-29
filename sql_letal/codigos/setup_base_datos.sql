-- Database setup script for "SQL Letal: El Misterio de la Base de Datos"
-- Este script crea las tablas y datos de ejemplo para seguir la novela

-- ============================================================
-- TABLAS PRINCIPALES (diseño normalizado)
-- ============================================================

CREATE TABLE IF NOT EXISTS departamentos (
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS personal (
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT,
    email TEXT,
    cargo TEXT,
    departamento_codigo TEXT REFERENCES departamentos(codigo),
    jefe_codigo TEXT REFERENCES personal(codigo),
    autorizado BOOLEAN DEFAULT 0,
    fecha_muerte TIMESTAMP NULL
);

CREATE TABLE IF NOT EXISTS proyectos (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    presupuesto REAL,
    fecha_inicio DATE,
    responsable_codigo TEXT REFERENCES personal(codigo)
);

CREATE TABLE IF NOT EXISTS proyecto_investigadores (
    proyecto_id TEXT REFERENCES proyectos(id),
    investigador_codigo TEXT REFERENCES personal(codigo),
    PRIMARY KEY (proyecto_id, investigador_codigo)
);

CREATE TABLE IF NOT EXISTS laboratorios (
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    ubicacion TEXT
);

CREATE TABLE IF NOT EXISTS accesos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    puerta TEXT,
    laboratorio TEXT,
    acceso_concedido BOOLEAN DEFAULT 1,
    ip_origen TEXT,
    duracion REAL
);

CREATE TABLE IF NOT EXISTS experimentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    fecha DATE,
    investigador TEXT,
    resultado TEXT,
    proyecto TEXT,
    fecha_fin DATE
);

CREATE TABLE IF NOT EXISTS logs_acceso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    accion TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS logs_modificaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    tabla TEXT,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_origen TEXT
);

CREATE TABLE IF NOT EXISTS transacciones_ocultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monto REAL,
    fecha TIMESTAMP,
    concepto TEXT,
    beneficiario TEXT,
    usuario_creacion TEXT,
    proyecto_asociado TEXT,
    notas TEXT,
    ip_creacion TEXT,
    estado TEXT DEFAULT 'PENDIENTE'
);

CREATE TABLE IF NOT EXISTS proveedores_autorizados (
    codigo TEXT PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE IF NOT EXISTS conexiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    ip_origen TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auditoria_oculta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaccion_id INTEGER,
    usuario TEXT,
    monto REAL,
    ip_origen TEXT,
    fecha TIMESTAMP,
    hash TEXT
);

-- ============================================================
-- DATOS DE EJEMPLO
-- ============================================================

INSERT OR IGNORE INTO departamentos VALUES ('DIR', 'Dirección');
INSERT OR IGNORE INTO departamentos VALUES ('SIS', 'Sistemas');
INSERT OR IGNORE INTO departamentos VALUES ('INV', 'Investigación');
INSERT OR IGNORE INTO departamentos VALUES ('ADM', 'Administración');
INSERT OR IGNORE INTO departamentos VALUES ('QCA', 'Química');

INSERT OR IGNORE INTO personal VALUES ('director', 'Carlos', 'Mendoza', 'cmendoza@icb.cat', 'Director General', 'DIR', NULL, 1, NULL);
INSERT OR IGNORE INTO personal VALUES ('vilaro', 'Albert', 'Vilaró', 'avilaro@icb.cat', 'Subdirector', 'SIS', 'director', 1, NULL);
INSERT OR IGNORE INTO personal VALUES ('hblasco', 'Héctor', 'Blasco', 'hblasco@icb.cat', 'Investigador Senior', 'INV', 'vilaro', 1, '2026-07-15 05:30');
INSERT OR IGNORE INTO personal VALUES ('mrobles', 'Marta', 'Robles', 'mrobles@icb.cat', 'Asistente de Investigación', 'INV', 'hblasco', 1, NULL);
INSERT OR IGNORE INTO personal VALUES ('eriera', 'Elisa', 'Riera', 'eriera@icb.cat', 'Analista de Datos', 'INV', 'hblasco', 1, NULL);

INSERT OR IGNORE INTO proyectos VALUES ('CERBERO', 'Cerbero', 'Sistema de control biométrico avanzado', 500000, '2025-01-01', 'hblasco');
INSERT OR IGNORE INTO proyectos VALUES ('FENIX', 'Fénix', 'Recuperación de datos cifrados', 300000, '2025-06-01', 'hblasco');
INSERT OR IGNORE INTO proyectos VALUES ('ICARO', 'Ícaro', 'Sistema de detección de intrusiones', 400000, '2025-03-01', 'vilaro');

INSERT OR IGNORE INTO proyecto_investigadores VALUES ('CERBERO', 'hblasco');
INSERT OR IGNORE INTO proyecto_investigadores VALUES ('CERBERO', 'mrobles');
INSERT OR IGNORE INTO proyecto_investigadores VALUES ('CERBERO', 'eriera');
INSERT OR IGNORE INTO proyecto_investigadores VALUES ('FENIX', 'hblasco');
INSERT OR IGNORE INTO proyecto_investigadores VALUES ('ICARO', 'vilaro');

INSERT OR IGNORE INTO experimentos VALUES (1, 'Proyecto Fénix', '2026-06-01', 'Blasco', 'éxito', 'Fénix', NULL);
INSERT OR IGNORE INTO experimentos VALUES (2, 'Proyecto Ícaro', '2026-06-15', 'Blasco', 'fallo', 'Ícaro', NULL);
INSERT OR IGNORE INTO experimentos VALUES (3, 'Delta-7', '2026-07-01', 'Blasco', 'éxito', 'Cerbero', NULL);
INSERT OR IGNORE INTO experimentos VALUES (4, 'Prueba Alfa', '2026-05-10', 'Riera', 'éxito', 'Fénix', NULL);
INSERT OR IGNORE INTO experimentos VALUES (5, 'Sigma-9', '2026-06-20', 'Blasco', NULL, 'Cerbero', NULL);

INSERT OR IGNORE INTO proveedores_autorizados VALUES ('ICB', 'Instituto de Ciberseguridad de Barcelona');
INSERT OR IGNORE INTO proveedores_autorizados VALUES ('UPC', 'Universitat Politècnica de Catalunya');

-- Nota: los datos de accesos, transacciones y logs se generan dinámicamente en la historia
-- Este script proporciona la estructura base para seguir los ejemplos del libro.

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

SELECT 'Base de datos SQL Letal inicializada correctamente.' as mensaje;
