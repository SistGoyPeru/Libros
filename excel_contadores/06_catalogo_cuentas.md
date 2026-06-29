# Capítulo 2: Catálogo de Cuentas y Estructura de Datos

## El esqueleto de la contabilidad

—El catálogo de cuentas —dijo Don Alberto— es el esqueleto de la contabilidad. Si está mal estructurado, todo lo demás se derrumba.

María asintió. En la universidad le habían enseñado la teoría del plan contable, pero nunca cómo implementarlo en Excel.

### La Historia

Sonó el teléfono. María contestó:

—Estudio "Cifras & Legados", buenos días.

—María, soy Carlos, de "Importaciones del Sur S.A.C." —la voz sonaba preocupada—. Necesito que me ayudes con algo.

—Dime, Carlos.

—Mi contador anterior manejaba todo en Excel, pero renunció y me dejó un archivo con 2,000 cuentas contables sin orden, sin códigos, sin nada. Necesito reorganizar todo. El problema es que algunos códigos tienen 4 dígitos, otros 6, y los nombres de cuentas están en distintos formatos.

María suspiró. Sabía exactamente lo que eso significaba: un caos contable.

—Te ayudo —dijo—. Pero primero vamos a estructurar bien el catálogo.

### Principios del catálogo de cuentas en Excel

Don Alberto se acercó al escritorio.

—Un catálogo de cuentas bien diseñado tiene tres propiedades:

**1. Jerarquía clara**: Cada cuenta tiene un nivel (1=elemento, 2=rubro, 3=cuenta, 4=subcuenta, 5=analítica)

**2. Códigos consistentes**: Siempre la misma longitud, con ceros a la izquierda si es necesario

**3. Clasificación por tipo**: Activo, Pasivo, Patrimonio, Ingresos, Gastos

—Mira este ejemplo —dijo, mostrando una hoja en pantalla:

| Código | Descripción | Nivel | Tipo | Grupo |
|--------|-------------|-------|------|-------|
| 1 | Activo | 1 | Activo | Balance |
| 1.1 | Activo Corriente | 2 | Activo | Balance |
| 1.1.1 | Caja | 3 | Activo | Balance |
| 1.1.1.1 | Caja General | 4 | Activo | Balance |
| 1.1.1.1.01 | Caja Soles | 5 | Activo | Balance |

### Validación de datos para el catálogo

—Ahora —dijo Don Alberto—, una de las herramientas más poderosas para el contador: la validación de datos.

**Lista desplegable para tipo de cuenta:**

```
Seleccionar rango > Datos > Validación de datos > Lista
Origen: Activo, Pasivo, Patrimonio, Ingresos, Gastos, Costos
```

**Validación de longitud de código:**

```
Validación de datos > Personalizada
Fórmula: =LARGO(A2)=10
```
—Esto asegura que todos los códigos tengan exactamente 10 caracteres.

**Validación de duplicados:**

```
Validación de datos > Personalizada
Fórmula: =CONTAR.SI($A:$A,A2)=1
```
—Evita que se registren dos cuentas con el mismo código.

### Extraer datos con funciones de texto

—¿Y cómo limpiamos un catálogo desordenado? —preguntó María.

—Con funciones de texto —respondió Don Alberto.

**LIMPIAR espacios extra:**
```
=ESPACIOS(A2)
```

**EXTRAER el nivel del código:**
```
=SI(ESNUMERO(HALLAR(".",A2)), EXTRAE(A2,1, HALLAR(".",A2)-1), A2)
```

**CONVERTIR a mayúsculas/minúsculas:**
```
=MAYUSC(B2)    'CONTABILIDAD GENERAL'
=NOMPROPIO(B2) 'Contabilidad General'
```

**BUSCAR y reemplazar con fórmulas:**
```
=SUSTITUIR(B2, "Cta.", "Cuenta")
```

### Implementación del plan contable general

—En Perú —explicó Don Alberto—, el Plan Contable General Empresarial (PCGE) tiene esta estructura:

| Elemento | Descripción |
|----------|-------------|
| 1 | Activo |
| 2 | Activo Realizable |
| 3 | Existencias |
| 4 | Pasivo |
| 5 | Patrimonio |
| 6 | Gastos por Naturaleza |
| 7 | Ingresos |
| 8 | Cuentas de Orden Deudoras |
| 9 | Cuentas de Orden Acreedoras |

—Voy a mostrarte cómo implementarlo en Excel con una tabla que tenga:

```
Fórmula para código completo:
= TEXTO(elemento,"00") & "." & 
  TEXTO(rubro,"00") & "." & 
  TEXTO(cuenta,"00") & "." & 
  TEXTO(subcuenta,"00")
```

### Función BUSCARV en el catálogo

—Ahora —dijo Don Alberto—, la función más importante para un contador que trabaja con catálogos de cuentas.

**BUSCARV para obtener el nombre de la cuenta:**
```
=BUSCARV(A2, Catalogo!$A$2:$B$1000, 2, FALSO)
```

**BUSCARV con múltiples criterios (columna auxiliar):**
—Primero creamos una columna auxiliar concatenando los criterios:
```
Código completo = A2 & "-" & B2
```
—Luego buscamos:
```
=BUSCARV(D2 & "-" & E2, Catalogo!$C$2:$D$1000, 2, FALSO)
```

**BUSCARX (la evolución):**
```
=BUSCARX(A2, Catalogo[CODIGO], Catalogo[DESCRIPCION], "No encontrado")
```

—BUSCARX es superior —dijo Don Alberto—. No requiere que la columna de búsqueda esté a la izquierda, y puedes manejar errores fácilmente.

### Formato condicional en el catálogo

—El formato condicional es tu aliado —continuó Don Alberto—. Úsalo para:

**Resaltar cuentas de un tipo específico:**
```
=IZQUIERDA(A2,1)="1"  → Fondo verde claro (Activo)
=IZQUIERDA(A2,1)="4"  → Fondo azul claro (Pasivo)
```

**Resaltar cuentas sin descripción:**
```
=ESBLANCO(B2)  → Fondo rojo
```

**Resaltar códigos incorrectos:**
```
=LARGO(A2)<>10  → Fondo amarillo
```

### Resumen del capítulo

| Función | Uso contable |
|---------|-------------|
| ESPACIOS() | Limpiar descripciones de cuentas |
| SUSTITUIR() | Estandarizar nombres |
| BUSCARV() | Buscar cuentas por código |
| BUSCARX() | Búsqueda moderna en tablas |
| Validación de datos | Controlar ingreso de cuentas |
| Formato condicional | Visualizar tipos de cuenta |

### Enigma contable #2

Carlos te ha enviado el archivo `codigos/02_catalogo/catalogo_caos.xlsx` con un catálogo de cuentas desordenado.

**Tu misión:**
1. Limpia las descripciones (elimina espacios extra, estandariza mayúsculas)
2. Crea una columna "Código Completo" con formato XX.XX.XX.XX
3. Agrega validación de datos para evitar códigos duplicados
4. Implementa BUSCARX para buscar cuentas por código
5. Aplica formato condicional: Activos en verde, Pasivos en azul, Ingresos en naranja

*¿Podrás transformar el caos en un catálogo profesional?*