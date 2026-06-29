# Capítulo 1: SELECT y los Datos Perdidos

Eran las 6:47 de la mañana cuando el teléfono de Elisa Riera vibró sobre la mesa de noche. El sonido era diferente al de una llamada normal: más grave, más insistente. Era el tono de emergencia del ICB.

Veinte minutos después estaba frente a la puerta del laboratorio 7, en el sótano del instituto. El lugar olía a café quemado y a plástico caliente. Un cuerpo yacía en el suelo, junto a una silla volcada. El Dr. Héctor Blasco, su mentor, tenía los ojos abiertos mirando el techo.

—Elisa, lo siento —dijo el inspector Rovira, acercándose—. Lo encontró el guardia de seguridad a las 5:30.

—¿Qué dice la autopsia?

—Ataque al corazón. Pero hay algo raro. Héctor estaba sano. Corría maratones.

Elisa se arrodilló junto al cuerpo. Sus dedos tocaron el brazo frío del profesor. Luego miró la pantalla de su ordenador. Estaba encendida, mostrando una ventana de terminal con una línea de texto:

```
SELECT * FROM experimentos;
```

—No ha ejecutado la consulta —murmuró Elisa—. Es una instrucción incompleta. Héctor nunca dejaba consultas a medias.

---

## Concepto SQL: SELECT y FROM

La consulta `SELECT * FROM experimentos;` es la instrucción más fundamental en SQL. Vamos a desglosarla:

- **SELECT**: Indica qué columnas queremos obtener.
- `*` : Significa "todas las columnas" (es un comodín).
- **FROM experimentos**: Especifica la tabla de donde extraer los datos.

Una tabla SQL es como una hoja de cálculo: filas (registros) y columnas (campos). Por ejemplo, una tabla `experimentos` podría verse así:

| id | nombre | fecha | investigador | resultado |
|----|--------|-------|-------------|-----------|
| 1 | Proyecto Fénix | 2026-06-01 | Blasco | éxito |
| 2 | Proyecto Ícaro | 2026-06-15 | Blasco | fallo |
| 3 | Delta-7 | 2026-07-01 | Blasco | éxito |

### Sintaxis básica

```sql
-- Obtener todas las columnas de una tabla
SELECT * FROM experimentos;

-- Obtener columnas específicas
SELECT nombre, fecha FROM experimentos;

-- Obtener las primeras 5 filas
SELECT * FROM experimentos LIMIT 5;

-- Ordenar resultados
SELECT * FROM experimentos ORDER BY fecha DESC;
```

### ¿Por qué es importante?

El `SELECT` es la puerta de entrada a los datos. Sin él, no puedes ver nada. Como detective, tu primera tarea siempre será observar los datos disponibles.

Cuando Elisa vea `SELECT * FROM experimentos;` incompleto, sabrá que alguien interrumpió al profesor mientras buscaba algo específico.

---

### Enigma SQL #1: Los Registros Perdidos

La policía ha incautado la base de datos del ICB y te ha dado acceso. Usa SQL para responder:

1. ¿Cuántos experimentos hay registrados?
2. Muestra todos los experimentos ordenados por fecha del más reciente al más antiguo.
3. ¿Qué columnas tiene la tabla `experimentos`?

```sql
-- Escribe tus consultas aquí
```

*(Solución en el Apéndice, página 1)*
