# Capítulo 6: Limpieza de Datos Automatizada

Dos semanas después de la presentación, Andrea se había convertido en la "experta en Copilot" de la oficina. Sus compañeros la buscaban para pedirle ayuda con sus archivos.

—Andrea, ¿puedes revisar esto? —preguntó Mariana, del equipo de logística—. Tengo un archivo con datos de proveedores que está... bueno, mira tú misma.

Andrea abrió el archivo y entendió el problema inmediatamente.

La hoja de cálculo tenía:

- Nombres de proveedores escritos de formas diferentes: "Proveedor A", "proveedor a", "PROVEEDOR A", "Prov. A"
- Fechas en formatos mezclados: "15/01/2026", "01/15/2026", "2026-01-15"
- Celdas vacías en columnas críticas como RUC y Teléfono
- Texto y números en la misma columna
- Espacios al inicio y final de los textos
- Caracteres especiales: tildes, ñ, símbolos extraños

—Esto parece el diario de un Excel con personalidad múltiple —bromeó Andrea.

—¿Puedes arreglarlo? —preguntó Mariana con esperanza.

—Voy a intentarlo.

Andrea abrió Copilot y escribió:

*"Copilot, necesito limpiar esta tabla de proveedores. Problemas detectados:*
1. *Estandarizar nombres de proveedores (eliminar variaciones, mayúsculas consistentes)*
2. *Unificar formato de fecha a DD/MM/AAAA*
3. *Identificar y marcar celdas vacías en columnas críticas: RUC, Teléfono, Correo*
4. *Eliminar espacios extra al inicio y final de todas las celdas de texto*
5. *Separar columna 'Dirección' en tres: Calle, Distrito, Ciudad*
6. *Detectar y marcar duplicados basados en RUC*

*Genera las fórmulas o pasos necesarios para cada limpieza."*

Copilot respondió con un plan detallado:

*"Plan de Limpieza:*

1. **Estandarizar nombres:***
   `=MAYUSC.INICIA(ESPACIOS(A2))`

2. **Unificar fechas:***
   Selecciona la columna de fechas > Datos > Texto en Columnas > Fecha DMY

3. **Celdas vacías críticas:***
   `=SI(O(B2="",C2=""),"REVISAR","OK")`

4. **Eliminar espacios:***
   `=ESPACIOS(A2)` — aplicar a todas las columnas de texto

5. **Separar dirección:***
   Selecciona columna > Datos > Texto en Columnas > Delimitado > Coma

6. **Duplicados:***
   `=CONTAR.SI(B:B,B2)>1` en columna auxiliar

*¿Empiezo con el paso 1?"*

Andrea aceptó y Copilot fue aplicando cada transformación paso a paso. En 30 minutos, el archivo de proveedores pasó de ser un caos a una base de datos limpia y profesional.

—¿Ya terminaste? —preguntó Mariana, incrédula.

—Sí. Aquí tienes. El archivo limpio, con una hoja de diagnóstico que muestra los problemas que encontré y cómo los resolví.

Mariana abrió el archivo y sus ojos se abrieron como platos.

—Andrea, esto es increíble. ¿Me enseñas?

Andrea sonrió.

—Claro. Pero primero, deja que te muestre algo...

---

### Conceptos Clave: Limpieza de Datos con Copilot

La limpieza de datos es donde Copilot realmente brilla. Los datos del mundo real son desordenados, y la IA puede acelerar drásticamente el proceso.

#### Problemas Comunes que Copilot Puede Detectar

| Problema | Prompt |
|----------|--------|
| Duplicados | "Detecta y marca filas duplicadas basadas en el ID" |
| Valores faltantes | "Identifica celdas vacías en columnas críticas" |
| Formatos inconsistentes | "Unifica el formato de fecha en toda la columna" |
| Errores tipográficos | "Encuentra nombres similares con probable error" |
| Espacios extra | "Elimina espacios al inicio y final de todas las celdas" |
| Mayúsculas/minúsculas | "Estandariza textos a mayúscula inicial" |
| Valores atípicos | "Detecta valores fuera del rango esperado" |
| Datos mezclados | "Separa la columna Nombre Completo en Nombre y Apellido" |

#### Pasos de Limpieza Recomendados

1. **Diagnóstico**: Pídele a Copilot que evalúe la calidad de tus datos
2. **Priorización**: Identifica los problemas más críticos primero
3. **Limpieza en copia**: Trabaja siempre sobre una copia del archivo original
4. **Documentación**: Pídele a Copilot que registre los cambios realizados
5. **Validación**: Verifica que los datos limpios tengan sentido

#### Comandos Avanzados de Limpieza

- *"Estandariza los nombres de clientes: elimina abreviaturas, corrige ortografía común"*
- *"Convierte todas las columnas de texto a mayúscula inicial (MAYUSC.INICIA)"*
- *"Separa la columna 'Dirección Completa' usando comas como delimitador"*
- *"Combina las columnas Nombre y Apellido en una sola columna 'Nombre Completo'"*
- *"Reemplaza los valores 'N/A', '-' y vacíos por un valor estándar 'No Disponible'"*
- *"Valida que los RUC tengan exactamente 11 dígitos y marca los incorrectos"*

#### Power Query como Alternativa

Para limpiezas muy grandes o recurrentes, Copilot puede sugerir Power Query:

- *"Crea una consulta en Power Query que limpie automáticamente este archivo cada vez que se actualice"*
- *"Agrega un paso en Power Query para eliminar columnas innecesarias"*
- *"Configura Power Query para combinar todos los archivos de una carpeta"*

---

### Ejercicio 6.1: Diagnóstico de Calidad

Abre un archivo que sepas que tiene problemas de datos. Pídele a Copilot:

*"Realiza un diagnóstico completo de calidad de datos. Identifica:*
1. *Columnas con valores faltantes*
2. *Filas duplicadas*
3. *Formatos inconsistentes*
4. *Valores atípicos*
5. *Errores de ortografía o tipografía*

*Genera un reporte con los hallazgos y sugiere acciones correctivas."*

### Ejercicio 6.2: Pipeline de Limpieza Automatizado

Pídele a Copilot:

*"Diseña un flujo de limpieza automatizada para este archivo usando Power Query. Los pasos deben incluir:*
1. *Promover encabezados*
2. *Cambiar tipos de datos*
3. *Eliminar filas duplicadas*
4. *Reemplazar valores nulos*
5. *Agregar columna de fecha estandarizada*

*Genera el código M necesario."*
