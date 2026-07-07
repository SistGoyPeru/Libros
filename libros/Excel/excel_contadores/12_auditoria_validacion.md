# Capítulo 8: Auditoría y Validación de Datos

## El ojo del contador

—Un buen contador —dijo Don Alberto— no solo registra transacciones. Las audita. Las cuestiona. Las verifica.

### La Historia

—Don Alberto —dijo María—, estoy revisando el archivo que nos envió el cliente y creo que hay errores. Pero son 10,000 filas. Revisarlas una por una me tomaría una semana.

—No necesitas revisarlas una por una —sonrió Don Alberto—. Necesitas que Excel revise por ti.

### Auditoría de fórmulas

Don Alberto abrió el menú de fórmulas:

```
Fórmulas > Auditoría de fórmulas
```

**Rastrear precedentes:**
—Muestra flechas hacia las celdas que alimentan una fórmula.

```
Seleccionar celda > Rastrear precedentes
```

**Rastrear dependientes:**
—Muestra qué celdas dependen de la celda seleccionada.

**Mostrar fórmulas:**
—En lugar de resultados, muestra todas las fórmulas.

```
Ctrl + ` (acento grave)
```

**Evaluar fórmula:**
—Paso a paso, muestra cómo Excel calcula la fórmula.

```
Seleccionar celda > Evaluar fórmula
```

### Detección de errores

—Los errores contables más comunes en Excel —dijo Don Alberto— son:

| Error | Causa posible |
|-------|--------------|
| #¡DIV/0! | División entre cero (falta de datos) |
| #¡N/A! | Búsqueda sin resultado |
| #¡VALOR! | Tipo de dato incorrecto |
| #¡REF! | Referencia de celda eliminada |
| ###### | Columna muy angosta (no es error real) |

**Fórmula para detectar errores en un rango:**
```
=SI.ERROR(A2, "REVISAR")
```

**Validación masiva con ESERROR:**
```
=SI(ESERROR(A2), "ERROR", A2)
```

### Validación de datos avanzada

—La validación de datos —dijo Don Alberto— es tu primera línea de defensa contra errores.

**Validación personalizada para RUC (11 dígitos):**
```
=Y(LARGO(A2)=11, ES NUMERO(A2))
```

**Validación para fechas dentro del ejercicio:**
```
=Y(A2>=FECHA(2025,1,1), A2<=FECHA(2025,12,31))
```

**Validación para montos positivos:**
```
=Y(ES NUMERO(A2), A2>0)
```

**Validación para cuentas del PCGE:**
```
=Y(LARGO(A2)>=4, IZQUIERDA(A2,1)>=1, IZQUIERDA(A2,1)<=9)
```

### Formato condicional para auditoría

—El formato condicional es tu detector visual de anomalías:

**Resaltar duplicados:**
```
Seleccionar rango > Formato condicional > Resaltar reglas de celdas > Valores duplicados
```

**Resaltar montos atípicos:**
```
Fórmula: =A2>PROMEDIO($A$2:$A$1000)*3
Formato: Fondo rojo
```

**Resaltar fechas fuera del período:**
```
Fórmula: =O(A2<FECHA(2025,1,1), A2>FECHA(2025,12,31))
Formato: Fondo amarillo
```

**Resaltar celdas con errores:**
```
Fórmula: =ESERROR(A2)
Formato: Fondo naranja, letra blanca
```

### Detección de datos atípicos (outliers)

—Para detectar montos sospechosos en contabilidad:

**Rango intercuartil (IQR):**
```
Q1 = CUARTIL(rango, 1)
Q3 = CUARTIL(rango, 3)
IQR = Q3 - Q1
Límite inferior = Q1 - 1.5 * IQR
Límite superior = Q3 + 1.5 * IQR
```

**Fórmula para marcar outliers:**
```
=SI(A2>LímiteSuperior, "ATIPICO ALTO", 
    SI(A2<LímiteInferior, "ATIPICO BAJO", "NORMAL"))
```

### Circular referencias

—Las referencias circulares —dijo Don Alberto— pueden ser errores o herramientas. Depende de cómo las uses.

**Referencia circular involuntaria:**
```
Celda C2: =A2+B2+C2  ← ERROR: C2 se referencia a sí misma
```

**Referencia circular controlada:**
```
Celda D2 (Interés): =E2 * 0.01  ← Depende del saldo final
Celda E2 (Saldo Final): =B2 - C2 + D2  ← Depende del interés
```

—Para referencias circulares controladas, habilita el cálculo iterativo:

```
Archivo > Opciones > Fórmulas > Habilitar cálculo iterativo
Iteraciones: 100  Cambio máximo: 0.001
```

### Conciliación automática

—La conciliación bancaria —dijo Don Alberto— es el pan de cada día del contador.

**Tabla de conciliación:**

| Concepto | Libros | Banco | Diferencia |
|----------|--------|-------|------------|
| Saldo inicial | 150,000 | 152,000 | -2,000 |
| Ingresos | 45,000 | 44,800 | 200 |
| Egresos | (32,000) | (32,500) | 500 |
| **Saldo final** | **163,000** | **164,300** | **-1,300** |

**Fórmula para conciliación automática:**

```
=BUSCARX(A2, tblBanco[Referencia], tblBanco[Monto], "No conciliado")
```

—Las transacciones que aparezcan en libros pero no en banco, o viceversa, son las partidas pendientes de conciliación.

### Protección de datos contables

—Finalmente —dijo Don Alberto—, la protección de la información contable.

**Proteger celdas con fórmulas:**
1. Seleccionar todas las celdas > Formato celdas > Proteger > [ ] Bloqueada
2. Seleccionar celdas con fórmulas > Formato celdas > Proteger > [x] Bloqueada
3. Revisar > Proteger hoja > Contraseña

**Permitir edición solo en celdas de entrada:**
—Las celdas de entrada (montos, fechas, cuentas) quedan desbloqueadas.
—Las celdas con fórmulas quedan bloqueadas.

### Resumen del capítulo

| Herramienta | Uso en auditoría |
|-------------|-----------------|
| Rastrear precedentes | Verificar origen de datos |
| Mostrar fórmulas | Revisar lógica contable |
| SI.ERROR | Manejar errores elegante |
| Validación de datos | Prevenir errores de ingreso |
| Formato condicional | Detectar anomalías visuales |
| Rango intercuartil | Identificar outliers |
| Conciliación automática | Comparar fuentes de datos |
| Protección | Asegurar integridad contable |

### Enigma contable #8

Has recibido el archivo `codigos/08_auditoria/auditoria_errores.xlsx`. Contiene 5,000 transacciones, pero algunas tienen errores.

**Tu misión:**
1. Encuentra todas las celdas con errores usando formato condicional
2. Identifica los outliers (montos atípicos) usando el método IQR
3. Detecta transacciones duplicadas y márcalas
4. Verifica que todas las fechas estén dentro del ejercicio 2025
5. Realiza una conciliación bancaria: compara las transacciones en `auditoria_errores.xlsx` con el extracto bancario en `extracto_bancario.xlsx`
6. Genera un informe de auditoría que muestre: cantidad de errores encontrados, montos atípicos, duplicados, y partidas no conciliadas