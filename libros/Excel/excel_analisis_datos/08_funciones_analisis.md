# Capítulo 4: Funciones de Análisis Esenciales

## El arsenal del analista

—Hay funciones que un analista de datos debe conocer como la palma de su mano —dijo Valeria—. No son muchas, pero son poderosas.

### SUMAR.SI.CONJUNTO — El taladro del analista

—La función más versátil para análisis condicional:

```
=SUMAR.SI.CONJUNTO(rango_suma, rango_crit1, crit1, rango_crit2, crit2, ...)
```

**Ejemplos de análisis:**

```
Ventas de una región en un mes específico:
=SUMAR.SI.CONJUNTO(Ventas[Monto], Ventas[Region], "Lima",
                    Ventas[Mes], "Enero")

Ventas mayores a S/1,000 en el trimestre:
=SUMAR.SI.CONJUNTO(Ventas[Monto], Ventas[Monto], ">1000",
                    Ventas[Trimestre], 1)

Gasto total por categoría y centro de costo:
=SUMAR.SI.CONJUNTO(Gastos[Monto], Gastos[Categoria], "Marketing",
                    Gastos[CentroCosto], "CC-ADM")
```

### CONTAR.SI.CONJUNTO — Conteo condicional

```
Transacciones de un cliente premium en el mes:
=CONTAR.SI.CONJUNTO(Ventas[Cliente], "VIP", Ventas[Mes], "Enero")

Productos con stock crítico:
=CONTAR.SI.CONJUNTO(Inventario[Stock], "<10", Inventario[Activo], "Sí")
```

### PROMEDIO.SI.CONJUNTO — Promedio condicional

```
=PROMEDIO.SI.CONJUNTO(Ventas[Monto], Ventas[Categoria], "Electrónicos",
                       Ventas[Mes], "Enero")
```

### BUSCARX para enriquecer datos

—El analista constantemente combina datos de diferentes tablas:

```
=BUSCARX(ID_Producto, tblProductos[ID], tblProductos[Precio])
=BUSCARX(ID_Cliente, tblClientes[ID], tblClientes[Categoria], "General")
```

### INDICE + COINCIDIR — La alternativa flexible

—Cuando BUSCARX no es suficiente:

```
=INDICE(tblProductos[Precio], COINCIDIR(ID_Producto, tblProductos[ID], 0))
```

—Ventajas: puedes buscar hacia la izquierda, derecha, arriba, abajo.

### SI.ERROR y SI.ND — Manejo elegante de errores

—Los datos reales siempre tienen sorpresas:

```
=SI.ERROR(BUSCARX(ID, tbl, tbl[Precio]), "No encontrado")
=SI.ND(BUSCARX(ID, tbl, tbl[Precio]), 0)
```

### FUNCIONES LAMBDA — Crear tus propias funciones

—Para Excel 365 —dijo Valeria—, LAMBDA te permite crear tus propias funciones reutilizables:

```
Nombre: TASA_CRECIMIENTO
Refiere a: =LAMBDA(actual, anterior, (actual - anterior) / anterior)

Uso: =TASA_CRECIMIENTO(C2, B2)
```

### Análisis de cohortes con funciones

—Para analizar grupos de clientes por período de adquisición:

```
Mes de primera compra:
=MIN.SI.CONJUNTO(Ventas[Fecha], Ventas[Cliente], A2)

Cohorte:
=TEXTO(MesPrimeraCompra, "mmm-aa")
```

### Resumen del capítulo

| Función | Para qué usarla |
|---------|----------------|
| SUMAR.SI.CONJUNTO | Totales con múltiples condiciones |
| CONTAR.SI.CONJUNTO | Conteos condicionales |
| PROMEDIO.SI.CONJUNTO | Promedios por segmento |
| BUSCARX | Combinar tablas |
| INDICE+COINCIDIR | Búsqueda flexible |
| SI.ERROR | Manejar errores |
| LAMBDA | Funciones personalizadas |
| MIN.SI.CONJUNTO | Cohortes y primera vez |

### Enigma #4

En `codigos/c04_funciones/datos_analisis.xlsx` tienes 3 tablas: Ventas, Productos, Clientes.

**Tu misión:**
1. Calcula las ventas totales por categoría de producto usando SUMAR.SI.CONJUNTO
2. Cuenta cuántos clientes VIP compraron en cada mes
3. Enriquece la tabla de ventas con el nombre del producto y la categoría del cliente usando BUSCARX
4. Calcula la tasa de crecimiento mensual usando una función LAMBDA
5. Identifica los clientes nuevos cada mes (cohorte) usando MIN.SI.CONJUNTO