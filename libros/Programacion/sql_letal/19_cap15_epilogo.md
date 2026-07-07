# Capítulo 15: El Epílogo

## La Verdad

—Héctor no solo descubrió Talos —dijo Elisa, de pie frente al tribunal—. Descubrió que el proyecto financiaba operaciones encubiertas del ICB. Operaciones que el gobierno había autorizado pero que nunca aparecerían en los presupuestos oficiales.

Vilaró la miraba desde el banquillo. A su lado, Marta Robles mantenía la cabeza baja.

—Pero entonces —intervino el fiscal—, ¿por qué mataron al doctor Blasco?

—Porque Héctor descubrió que una parte del dinero no iba a operaciones encubiertas. Iba a una cuenta privada. Vilaró estaba robando, usando el proyecto Talos como pantalla.

—Y cuando Blasco lo descubrió...

—Vilaró lo silenció. Pero cometió un error: usó SQL para ocultar su rastro. Y SQL, bien usado, siempre revela la verdad.

---

## Resumen SQL

A lo largo de esta investigación, has aprendido:

### Nivel Básico
- **SELECT y FROM**: Leer datos de tablas
- **WHERE**: Filtrar filas con condiciones
- **ORDER BY**: Ordenar resultados
- **LIMIT**: Limitar resultados
- **LIKE**: Búsqueda con patrones
- **IN, BETWEEN**: Rangos y listas

### Nivel Intermedio
- **JOIN** (INNER, LEFT, RIGHT, FULL): Combinar tablas
- **GROUP BY y funciones de agregación**: Resumir datos (COUNT, SUM, AVG, MAX, MIN)
- **HAVING**: Filtrar grupos
- **Funciones de fecha**: DATE, strftime, datetime
- **Subconsultas**: Consultas dentro de consultas
- **Funciones de cadena**: SUBSTR, UPPER, LOWER, REPLACE, TRIM
- **CASE**: Condicionales en SQL

### Nivel Avanzado
- **Índices**: Optimizar consultas
- **Vistas**: Simplificar consultas complejas
- **Transacciones**: Controlar cambios (BEGIN, COMMIT, ROLLBACK)
- **Triggers**: Automatizar acciones en la base de datos
- **Normalización**: Diseñar bases de datos eficientes
- **CTEs**: Consultas temporales (WITH)
- **CTEs Recursivos**: Datos jerárquicos
- **Window Functions**: ROW_NUMBER, LAG, LEAD, SUM/AVG con ventanas

---

## El Juicio

El trigger de Héctor, combinado con las window functions que Elisa aplicó, demostró que Vilaró había usado la cuenta de Blasco para ejecutar la transferencia de 750,000 EUR. La toxina T-47 fue enviada al laboratorio por orden de Vilaró, quien luego borró el registro del inventario.

Marta Robles, enfrentando cargos reducidos por cooperar, testificó que Vilaró la había amenazado para que participara en el encubrimiento.

Albert Vilaró fue condenado a 25 años de prisión por asesinato, malversación de fondos y obstrucción a la justicia.

---

## Después

Elisa Riera fue promovida a jefa del departamento de análisis forense de datos del ICB. Su primera decisión fue rediseñar la base de datos del instituto.

—Nunca más —dijo— un diseño defectuoso ocultará un crimen. Los datos deben ser claros, consistentes y auditables. Como la verdad.

En su escritorio, una placa recordaba a su mentor:

> *"SELECT la verdad FROM los datos WHERE la justicia = true;"*

—Héctor —murmuró—. Tu último query se ejecutó.

---

### Enigma SQL #15: El Caso Cerrado

1. Usando todo lo aprendido, escribe una consulta que resuma el caso: total de dinero desviado, número de transacciones, implicados y periodo de tiempo.
2. Crea una vista `v_resumen_caso_blasco` que pueda usar un fiscal para presentar la evidencia.
3. Si fueras Elisa, ¿qué índice crearías para prevenir futuros fraudes en la tabla `transacciones`?

```sql
-- Tus consultas aquí
```
