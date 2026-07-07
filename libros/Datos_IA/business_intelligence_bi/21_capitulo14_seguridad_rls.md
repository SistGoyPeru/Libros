# Capítulo 14: Seguridad — RLS, Permisos y Gobernanza

## Seguridad en Power BI

La seguridad en Power BI opera en 3 capas:

```
Capa 1: Conjunto de datos (RLS)
  └── Filtros a nivel de fila según el usuario
Capa 2: Workspace y App
  └── Quién puede ver/editar/publicar
Capa 3: Fuente de datos
  └── Credenciales, gateways, cifrado
```

## RLS (Row-Level Security)

**RLS** permite restringir qué datos ve cada usuario. Ejemplo:
- Vendedor: solo ve sus propias ventas
- Gerente regional: solo ve su región
- CEO: ve todos los datos

### Paso 1: Crear roles en Power BI Desktop

1. "Modelado" → "Administrar roles"
2. "Crear"
3. Nombre: "Vendedor"
4. Agrega filtro DAX:

```dax
-- Rol: Vendedor (solo ve sus propias ventas)
[Employee Email] = USERNAME()
-- Nota: USERNAME() devuelve el email del usuario logueado
```

### Paso 2: Filtros RLS por dimensión

```dax
-- Rol: Gerente Regional (solo ve su región)
[Region] = USERPRINCIPALNAME()
-- Requiere tabla de usuarios con región asignada

-- Rol: Finanzas (ve todos los datos financieros)
TRUE  -- Sin restricción

-- Rol: Ejecutivo (ve todo)
TRUE
```

### RLS con tabla de seguridad

Para RLS avanzado, necesitas una tabla de seguridad:

```dax
-- Tabla de seguridad (no relacionada)
Seguridad =
  DATATABLE(
    "Email", STRING,
    "Rol", STRING,
    "Región", STRING,
    {
      {"ceo@techstore.com", "Ejecutivo", "Todas"},
      {"ventas.norte@techstore.com", "Vendedor", "Norte"},
      {"ventas.sur@techstore.com", "Vendedor", "Sur"},
      {"finanzas@techstore.com", "Finanzas", "Todas"}
    }
  )
```

```dax
-- Rol: Vendedor por región
VAR user_email = USERPRINCIPALNAME()
VAR user_region = 
    CALCULATE(
        VALUES(Seguridad[Región]),
        Seguridad[Email] = user_email
    )
RETURN
dim_customer[region] = user_region
```

### Probar RLS en Desktop

1. "Modelado" → "Ver como"
2. Selecciona el rol "Vendedor"
3. Verifica que solo ves datos filtrados

### Paso 3: Publicar y asignar roles

1. Publica el informe con RLS a Power BI Service
2. "Conjunto de datos" → "Seguridad a nivel de fila"
3. Agrega miembros a cada rol:
   - Rol "Vendedor": agrega emails de vendedores
   - Rol "Ejecutivo": agrega emails de directivos
4. "Guardar"

## Tabla de dimensiones de seguridad

Para RLS por región, producto o cliente:

```dax
-- Rol: Visibilidad por región
VAR usuario_actual = USERPRINCIPALNAME()
VAR regiones_permitidas = 
    CALCULATETABLE(
        VALUES(Seguridad[Región]),
        Seguridad[Email] = usuario_actual
    )
VAR resultado = 
    COUNTROWS(
        INTERSECT(
            VALUES(dim_customer[region]),
            regiones_permitidas
        )
    ) > 0
RETURN resultado
```

## Permisos de workspace

### Asignar roles en workspace

1. "Workspace" → "Acceso"
2. Agrega usuarios:
   - **Admin**: arquitectos BI
   - **Member**: analistas que crean contenido
   - **Viewer**: consumidores de dashboards

### Buenas prácticas de permisos

1. **Mínimo privilegio**: asigna solo el acceso necesario
2. **Grupos > individuos**: usa grupos de seguridad Azure AD
3. **Viewer para consumidores**: no necesitan editar
4. **App en lugar de compartir**: más control, actualización centralizada

## Gobernanza en BI

La gobernanza asegura que los datos sean confiables, seguros y bien gestionados.

### Principios de gobernanza

| Principio | Descripción | Práctica |
|-----------|-------------|----------|
| **Calidad** | Datos precisos y completos | Validaciones automáticas |
| **Linaje** | Origen y transformación de datos | Documentación de cada paso |
| **Acceso** | Solo usuarios autorizados | RLS, roles, permisos |
| **Consistencia** | Mismas definiciones en toda la org | Glosario de términos |
| **Actualidad** | Datos actualizados | Programación de refresco |

### Estándares para TechStore

```dax
-- Glosario de medidas (documentar cada una)
Medida: Ingresos Totales
Definición: Suma del campo total en fact_orders
Fórmula: SUM(fact_orders[total])
Frecuencia: Diaria
Responsable: Analista BI

Medida: Ticket Promedio
Definición: Ingreso promedio por pedido
Fórmula: AVERAGE(fact_orders[total])
Frecuencia: Diaria
Responsable: Analista BI
```

### Certificación de datasets

Power BI Service permite **certificar** datasets como oficiales:

1. "Configuración" → "Conjunto de datos" → "Certificar"
2. Solo admins pueden certificar
3. Los datasets certificados tienen un ícono de verificación

## Auditoría

Power BI Service registra actividad:

```
Consumo de informes: quién vio qué y cuándo
Actualizaciones: éxito/fallo, duración, datos cargados
Cambios en permisos: quién agregó/quitó usuarios
```

Para auditoría avanzada: **Microsoft 365 Compliance Center**.

## Ejercicios

1. Crea un rol RLS "Vendedor" que filtre por empleado
2. Prueba el rol en Power BI Desktop con "Ver como"
3. Publica el informe con RLS y asigna usuarios
4. Crea una tabla de seguridad con emails y roles
5. ¿Qué diferencia hay entre RLS y OLS (Object-Level Security)?
6. Crea un rol "Gerente Regional" que filtre por ciudad
7. ¿Qué es un workspace y qué rol asignarías a un analista?
8. Documenta 3 medidas de tu modelo con nombre, fórmula y responsable
9. Configura un dataset certificado en Power BI Service
10. ¿Cómo auditarías quién vio un informe la semana pasada?
