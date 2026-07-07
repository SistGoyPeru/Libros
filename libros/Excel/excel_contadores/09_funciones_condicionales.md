# Capítulo 5: Funciones Condicionales y de Búsqueda para Contabilidad

## La lógica del contador

—Las funciones condicionales —dijo Don Alberto— son el equivalente digital del juicio profesional del contador. Toman decisiones basadas en criterios que tú defines.

### La Historia

—Don Alberto —dijo María—, necesito clasificar 500 facturas por tipo de gasto y verificar si están dentro del presupuesto. Pero cada factura tiene un centro de costo, un proveedor, y una categoría diferente. Hacerlo manualmente me tomaría todo el día.

—Entonces no lo hagas manualmente —respondió Don Alberto—. Deja que Excel lo haga por ti.

### SI — La función más humana

—La función SI es la base de toda lógica en Excel:

```
=SI(prueba_logica, valor_si_verdadero, valor_si_falso)
```

**Ejemplo contable:**
```
=SI(B2>100000, "Requiere aprobación gerencial", "Aprobación automática")
```

**SI anidados para clasificación contable:**

```
=SI(C2="Ventas", "Ingreso",
  SI(C2="Alquiler", "Gasto Operativo",
    SI(C2="Sueldos", "Gasto Personal",
      "Otros")))
```

—Pero con funciones más modernas —dijo Don Alberto—, podemos evitar anidar tantos SI.

### IFS — Múltiples condiciones

—IFS es la evolución. Evalúa múltiples condiciones en orden:

```
=IFS(
  C2="Ventas", "Ingreso",
  C2="Alquiler", "Gasto Operativo",
  C2="Sueldos", "Gasto Personal",
  VERDADERO, "Otros"
)
```

—Es más limpio y menos propenso a errores que los SI anidados.

### SUMAR.SI — Suma condicional

—La reina de las funciones contables —dijo Don Alberto—.

```
=SUMAR.SI(rango_criterio, criterio, rango_suma)
```

**Ejemplos contables:**

```
Total ventas del mes:
=SUMAR.SI(C:C, "Ventas", D:D)

Total gastos de un centro de costo:
=SUMAR.SI(B:B, "CC-001", D:D)

Total facturas de un proveedor:
=SUMAR.SI(A:A, "PROV-123", D:D)
```

### SUMAR.SI.CONJUNTO — Suma con múltiples criterios

—La hermana mayor de SUMAR.SI —dijo Don Alberto—.

```
=SUMAR.SI.CONJUNTO(rango_suma, rango_criterio1, criterio1, 
                    rango_criterio2, criterio2, ...)
```

**Ejemplos contables:**

```
Ventas del mes de enero del producto A:
=SUMAR.SI.CONJUNTO(D:D, C:C, "Ventas", B:B, ">=01/01/2025", 
                    B:B, "<=31/01/2025", E:E, "Producto A")

Total compras a un proveedor en un período:
=SUMAR.SI.CONJUNTO(D:D, A:A, "PROV-123", B:B, ">=01/01/2025", 
                    B:B, "<=31/03/2025")
```

### CONTAR.SI y CONTAR.SI.CONJUNTO — Conteo de transacciones

```
Número de facturas pendientes:
=CONTAR.SI(F:F, "Pendiente")

Número de transacciones de un centro de costo en el mes:
=CONTAR.SI.CONJUNTO(B:B, "CC-001", C:C, ">=01/01/2025", C:C, "<=31/01/2025")
```

### BUSCARX en profundidad

—Ya vimos BUSCARX —dijo Don Alberto—. Pero profundicemos.

```
=BUSCARX(valor_buscado, matriz_buscar, matriz_devolver, 
         [si_no_encontrado], [modo_coincidencia], [modo_busqueda])
```

**Modos de coincidencia:**

| Modo | Comportamiento |
|------|----------------|
| 0 | Coincidencia exacta (predeterminado) |
| -1 | Coincidencia exacta o siguiente menor |
| 1 | Coincidencia exacta o siguiente mayor |
| 2 | Coincidencia de comodín (*, ?) |

**Ejemplo contable: buscar tipo de cambio:**

```
=BUSCARX(C2, tblTipoCambio[Fecha], tblTipoCambio[TC], 
         "No encontrado", -1)
```
—El modo -1 busca la fecha exacta o la anterior más cercana. Ideal para tipos de cambio cuando no hay cotización diaria exacta.

### BUSCARX con múltiples criterios

—Para buscar con dos o más criterios, concatenamos:

```
=BUSCARX(A2 & "-" & B2, 
         tblDatos[Cuenta] & "-" & tblDatos[CentroCosto], 
         tblDatos[Monto], "No encontrado")
```

—O con la función **XLOOKUP** anidada:

```
=BUSCARX(A2, tblDatos[Cuenta], 
         BUSCARX(B2, tblDatos[CentroCosto], tblDatos[Monto]))
```

—Pero esto último es más complejo. Prefiere la concatenación.

### FILTRAR — La función moderna

—Para Excel 365 —dijo Don Alberto—, FILTRAR es revolucionaria:

```
=FILTRAR(rango, condicion, [si_vacio])
```

**Ejemplo: todas las facturas vencidas:**
```
=FILTRAR(tblFacturas, tblFacturas[Estado]="Vencida", "Sin vencidas")
```

**Ejemplo: ventas de un mes específico:**
```
=FILTRAR(tblVentas, 
         (tblVentas[Mes]="Enero") * (tblVentas[Monto]>1000),
         "Sin resultados")
```
—El asterisco (*) actúa como Y lógico y el (+) como O lógico.

### Caso práctico: Clasificación automática de gastos

Don Alberto creó un sistema de clasificación automática:

```
=SI(
  ESERROR(BUSCARX(A2, tblReglas[Busqueda], tblReglas[Categoria])),
  "No clasificado",
  BUSCARX(A2, tblReglas[Busqueda], tblReglas[Categoria])
)
```

—Y luego —continuó—, un resumen por categoría:

| Categoría | Total |
|-----------|-------|
| =UNICOS(tblMovimientos[Categoria]) | =SUMAR.SI(tblMovimientos[Categoria], A2, tblMovimientos[Monto]) |

### Resumen del capítulo

| Función | Uso contable |
|---------|-------------|
| SI | Decisiones condicionales |
| IFS | Clasificación múltiple |
| SUMAR.SI | Totales por criterio |
| SUMAR.SI.CONJUNTO | Totales multicriterio |
| CONTAR.SI | Conteo de transacciones |
| BUSCARX | Búsqueda de datos contables |
| FILTRAR | Extraer transacciones específicas |

### Enigma contable #5

En `codigos/05_condicionales/gastos_mensuales.xlsx` encontrarás 1,000 transacciones de gastos de "Importaciones del Sur" con categorías, centros de costo y montos.

**Tu misión:**
1. Clasifica cada transacción como "Gasto Operativo", "Gasto Administrativo", "Costo de Venta" o "Otro" usando IFS
2. Calcula el total de gastos por centro de costo usando SUMAR.SI
3. Identifica los 5 proveedores con más transacciones usando CONTAR.SI
4. Extrae todas las transacciones mayores a S/ 10,000 usando FILTRAR
5. Crea un resumen automático: cuando se agregue una nueva transacción, el resumen debe actualizarse sin intervención manual