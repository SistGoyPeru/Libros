# Capítulo 1: El Proceso del Análisis de Datos

## Pensar como analista antes de abrir Excel

Valeria reunió al equipo frente a la pizarra blanca.

—Antes de tocar una sola celda —dijo—, vamos a definir el proceso. El análisis de datos no es abrir Excel y empezar a hacer gráficos.

### La Historia

—El gerente de ventas nos preguntó: "¿Por qué cayeron las ventas en el tercer trimestre?" —dijo Valeria—. Esa es la pregunta de negocio. Nuestro trabajo es traducirla en un análisis de datos.

—Pero son 50,000 filas —dijo Andrés—. ¿Por dónde empiezo?

—Por entender el proceso —respondió Valeria. Y dibujó en la pizarra:

```
1. Pregunta de negocio
2. Obtener datos
3. Limpiar y preparar
4. Explorar (EDA)
5. Analizar y modelar
6. Comunicar resultados
```

### Las 6 etapas del análisis

**1. Pregunta de negocio**
—Todo análisis empieza con una pregunta. No "dame un reporte", sino "¿qué problema estamos resolviendo?"

```
Buena pregunta: "¿Qué productos están perdiendo ventas y por qué?"
Mala pregunta: "Hazme un Excel de ventas"
```

**2. Obtener datos**
—Las fuentes pueden ser: bases de datos, archivos CSV, sistemas contables, APIs.

**3. Limpiar y preparar**
—El 80% del tiempo de un analista se va en limpiar datos. Vale la pena hacerlo bien.

**4. Explorar (EDA)**
—Análisis Exploratorio de Datos. Mira los datos, calcula estadísticas, haz gráficos. Busca patrones, anomalías, tendencias.

**5. Analizar y modelar**
—Aquí respondes la pregunta. Tablas dinámicas, funciones, escenarios.

**6. Comunicar**
—El mejor análisis del mundo no sirve si no lo comunicas bien. Dashboard, presentación, informe ejecutivo.

### Estructura de datos ordenada

—Hay un principio fundamental —dijo Valeria—: datos ordenados.

**Reglas de datos ordenados (Tidy Data):**

1. Cada variable en una columna
2. Cada observación en una fila
3. Cada valor en una celda

| Correcto | Incorrecto |
|----------|------------|
| Fecha, Producto, Venta | Fecha, Producto Ene, Producto Feb, ... |
| 01/01, Silla, 100 | 01/01, 100, 120, ... |

### Buenas prácticas del analista

Valeria compartió su checklist:

```
Antes de empezar:
  [ ] ¿Qué pregunta estamos respondiendo?
  [ ] ¿Qué datos necesitamos?
  [ ] ¿Quién usará el resultado?

Durante el análisis:
  [ ] Datos ordenados (tidy data)
  [ ] Tablas de Excel (Ctrl+T)
  [ ] fórmulas documentadas
  [ ] Rangos con nombres

Al finalizar:
  [ ] Resultado claro y accionable
  [ ] Visualización limpia
  [ ] Recomendación concreta
```

### Power Query para importar datos

—La primera herramienta que todo analista debe dominar —dijo Valeria— es Power Query.

```
Datos > Obtener datos > Desde archivo > Desde texto/CSV
```

—O desde una carpeta completa:

```
Datos > Obtener datos > Desde archivo > Desde carpeta
```

—Power Query te permite:
- Combinar múltiples archivos
- Filtrar filas y columnas
- Cambiar tipos de datos
- Eliminar duplicados
- Todo sin modificar el origen

### Resumen del capítulo

| Etapa | Qué hacer en Excel |
|-------|------------------|
| Pregunta | Definir el problema |
| Obtener | Power Query, importar |
| Limpiar | Power Query, tabla |
| Explorar | Estadísticas, gráficos |
| Analizar | Tablas dinámicas, funciones |
| Comunicar | Dashboard, gráficos |

### Enigma #1

En `codigos/c01_proceso/pedido_gerencia.xlsx` hay un archivo con 3 hojas de datos de ventas sin procesar.

**Tu misión:**
1. Define la pregunta de negocio: ¿Qué información le darías al gerente?
2. Importa los datos con Power Query
3. Combina las 3 hojas en una sola tabla ordenada
4. Documenta cada paso (agrega una hoja "Documentación")
5. Prepara un resumen ejecutivo de 3 indicadores clave