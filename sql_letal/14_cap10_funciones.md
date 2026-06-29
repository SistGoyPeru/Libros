# Capítulo 10: La Función del Silencio

La evidencia se acumulaba, pero Elisa sentía que algo no encajaba. Marta Robles tenía acceso a las cuentas, cierto. Vilaró tenía el motivo, también. Pero ¿quién había programado la transacción? ¿Y cómo sabían que Héctor estaría muerto a las 22:15?

Decidió analizar los datos de manera más profunda. Había un campo que había ignorado: las notas de las transacciones. Algunas contenían códigos extraños.

```sql
SELECT id, monto, concepto, notas
FROM transacciones_ocultas
WHERE notas IS NOT NULL
  AND notas != '';
```

Entre las notas encontró mensajes codificados. Pero no eran al azar; seguían un patrón. Cada nota era una concatenación de iniciales y números. Como si fueran... instrucciones.

—No son notas —dijo Elisa de repente—. Son comandos. Instrucciones para alguien más.

---

## Concepto SQL: Funciones de cadena y manipulación de datos

SQL no solo sirve para consultar datos, sino para transformarlos. Las funciones de cadena son esenciales para limpiar, extraer y manipular información.

### Funciones de cadena

```sql
-- Longitud de un texto
SELECT LENGTH('Hola Mundo'); -- 10

-- Convertir a mayúsculas/minúsculas
SELECT UPPER('hola'); -- HOLA
SELECT LOWER('HOLA'); -- hola

-- Extraer parte de una cadena (SQLite)
SELECT SUBSTR('Hola Mundo', 1, 4); -- Hola
SELECT SUBSTR('Hola Mundo', 6, 5); -- Mundo

-- Buscar posición
SELECT INSTR('Hola Mundo', 'Mundo'); -- 6

-- Concatenar
SELECT 'Hola' || ' ' || 'Mundo'; -- Hola Mundo

-- Reemplazar
SELECT REPLACE('Hola Mundo', 'Mundo', 'SQL'); -- Hola SQL

-- Trim (eliminar espacios)
SELECT TRIM('  Hola  '); -- Hola
SELECT LTRIM('  Hola'); -- Hola
SELECT RTRIM('Hola  '); -- Hola
```

### Extracción de información

```sql
-- Obtener iniciales
SELECT SUBSTR(nombre, 1, 1) || SUBSTR(apellido, 1, 1) as iniciales
FROM personal;

-- Extraer dominio de email
SELECT email, SUBSTR(email, INSTR(email, '@') + 1) as dominio
FROM personal;

-- Formatear fechas
SELECT strftime('%d/%m/%Y %H:%M', fecha) as fecha_formateada
FROM accesos;
```

### CASE: Condicionales en SQL

```sql
-- Clasificar accesos
SELECT usuario, fecha,
  CASE
    WHEN strftime('%H', fecha) BETWEEN '06' AND '12' THEN 'Mañana'
    WHEN strftime('%H', fecha) BETWEEN '12' AND '18' THEN 'Tarde'
    WHEN strftime('%H', fecha) BETWEEN '18' AND '22' THEN 'Noche'
    ELSE 'Madrugada'
  END as turno
FROM accesos;

-- Categorizar montos
SELECT monto,
  CASE
    WHEN monto < 1000 THEN 'Bajo'
    WHEN monto BETWEEN 1000 AND 10000 THEN 'Medio'
    WHEN monto BETWEEN 10000 AND 100000 THEN 'Alto'
    ELSE 'Crítico'
  END as nivel
FROM transacciones_ocultas;
```

### COALESCE e IFNULL

```sql
-- Valores por defecto para NULL
SELECT nombre, COALESCE(telefono, 'No registrado') as telefono
FROM personal;

SELECT nombre, IFNULL(email, 'sin-email@instituto.com') as email
FROM personal;
```

---

### El Mensaje Oculto

Elisa aplicó funciones de cadena a las notas de las transacciones:

```sql
SELECT id, monto, 
       SUBSTR(notas, 1, 3) as codigo,
       SUBSTR(notas, INSTR(notas, ':') + 1) as instruccion
FROM transacciones_ocultas
WHERE notas LIKE 'CMD:%';
```

Los resultados mostraban códigos como `CMD:TRANSFERIR_ARCHIVOS`, `CMD:BORRAR_LOGS`, `CMD:ACTIVAR_PROTOCOLO`.

—Son órdenes —dijo Elisa—. Alguien daba instrucciones a través de las transacciones bancarias.

—¿Quién? —preguntó Rovira.

Elisa modificó la consulta:

```sql
SELECT usuario, COUNT(*) as ordenes_dadas
FROM transacciones_ocultas
WHERE notas LIKE 'CMD:%'
GROUP BY usuario
ORDER BY ordenes_dadas DESC;
```

El resultado: **M. Robles** era la única que insertaba notas con comandos.

—Marta no solo sabía —concluyó Elisa—. Marta ejecutaba las órdenes. Pero ¿de quién?

---

### Enigma SQL #10: Decodificando el Mensaje

1. Extrae los primeros 4 caracteres de cada concepto de transacción. ¿Hay un patrón visible?
2. Clasifica las transacciones en categorías según el monto (bajo < 1000, medio 1000-50000, alto > 50000). ¿Cuántas hay de cada tipo?
3. Crea una consulta que muestre el nombre completo del usuario (Nombre + Apellido) y el total de transacciones que realizó.

```sql
-- Tus consultas aquí
```
