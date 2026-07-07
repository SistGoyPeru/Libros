# Capítulo 6: Tablas Dinámicas para Análisis Contable

## El poder de resumir

—Las tablas dinámicas —dijo Don Alberto— son el arma secreta del contador moderno. Convierten miles de filas de transacciones en informes claros en segundos.

### La Historia

—Don Alberto —dijo María—, el gerente quiere un informe por centro de costo, por mes, y por tipo de gasto. Con subtotales y totales generales. Y lo quiere para ayer.

Don Alberto se rió.

—Con una tabla dinámica, esto se hace en 30 segundos.

### Tu primera tabla dinámica

Don Alberto seleccionó los datos y presionó:

```
Insertar > Tabla dinámica > Aceptar
```

—Arrastra "Centro Costo" a Filas, "Mes" a Columnas, y "Monto" a Valores —dijo.

En segundos, la tabla apareció:

| Centro Costo | Enero | Febrero | Marzo | Total |
|-------------|-------|---------|-------|-------|
| CC-Admin | 45,000 | 48,000 | 42,000 | 135,000 |
| CC-Ventas | 32,000 | 35,000 | 38,000 | 105,000 |
| CC-Producción | 120,000 | 115,000 | 130,000 | 365,000 |
| **Total** | **197,000** | **198,000** | **210,000** | **605,000** |

—¡Increíble! —exclamó María—. Lo que me habría tomado todo el día.

### Campos calculados

—Pero podemos ir más allá —dijo Don Alberto—. Podemos crear campos calculados.

```
Tabla dinámica > Analizar > Campos, elementos y conjuntos > Campo calculado
Nombre: "Variación Mensual"
Fórmula: =SI(Monto - VALOR(EXTRAE(Mes,1,3)), ...)
```

—O mejor, calculamos indicadores fuera de la tabla dinámica usando GETPIVOTDATA.

### GETPIVOTDATA — Extraer valores de la tabla dinámica

—Esta función —dijo Don Alberto— es clave para crear informes profesionales:

```
=GETPIVOTDATA("Monto", $A$1, "CentroCosto", "CC-Admin", "Mes", "Enero")
Resultado: 45,000
```

—Con esto puedes construir reportes con formato completamente controlado, usando los valores de la tabla dinámica en celdas específicas.

### Segmentadores y líneas de tiempo

—Los segmentadores —dijo Don Alberto— son filtros visuales que hacen que tus informes sean interactivos.

```
Tabla dinámica > Analizar > Insertar segmentador
Seleccionar: Centro Costo, Tipo Gasto
```

—Y las líneas de tiempo para filtrar por fecha:

```
Tabla dinámica > Analizar > Insertar línea de tiempo
Seleccionar: Fecha
```

—Ahora el gerente puede filtrar por trimestre, por centro de costo, o por tipo de gasto con solo hacer clic.

### Agrupación en tablas dinámicas

—Una de las características más útiles para contadores —dijo Don Alberto— es la agrupación.

**Agrupar por fechas:**
```
Clic derecho sobre una fecha > Agrupar
Seleccionar: Meses, Trimestres, Años
```

—Excel agrupa automáticamente las fechas en los períodos que elijas.

**Agrupar por rangos de montos:**
```
Clic derecho sobre un monto > Agrupar
Desde: 0, Hasta: 100000, Por: 10000
```

**Agrupar cuentas contables manualmente:**
```
Seleccionar varias cuentas > Clic derecho > Agrupar
Nombre del grupo: "Activo Corriente"
```

—Esto permite crear niveles jerárquicos en el catálogo de cuentas dentro de la tabla dinámica.

### Orden personalizado

—En contabilidad —dijo Don Alberto—, el orden importa. Los activos van primero, luego pasivos, luego patrimonio.

Para orden personalizado:
```
Archivo > Opciones > Avanzadas > Editar listas personalizadas
Importar lista desde un rango de celdas
```

—Luego, en la tabla dinámica, usas ese orden.

### Formato condicional en tablas dinámicas

—Aplica formato condicional para resaltar:

```
Celdas > Reglas de formato condicional:
- Valores mayores a 100,000: fondo verde
- Valores menores a 1,000: fondo rojo
- Variaciones negativas: flecha roja
```

**Formato de número contable:**
—Asegúrate de usar el formato contable en los valores de la tabla dinámica:

```
Clic derecho en valor > Configuración de campo de valor > Formato de número
Categoría: Contabilidad
Símbolo: S/
```

### Tabla dinámica con varios campos de valor

—Podemos mostrar múltiples métricas:

```
Valores:
  Suma de Monto (con formato contable)
  Conteo de Transacciones
  Promedio de Monto
  % del total de filas
```

**Mostrar valores como:**

| Opción | Uso contable |
|--------|-------------|
| % del total general | Composición de gastos |
| % del total de columna | Distribución mensual |
| Diferencia de... | Variación mes a mes |
| % de diferencia de... | Variación porcentual |

### Caso práctico: Estado de resultados dinámico

Don Alberto construyó un estado de resultados completo con tablas dinámicas:

1. Tabla dinámica base con cuentas en filas y meses en columnas
2. Agrupación de cuentas: Ingresos, Costos, Gastos Operativos, Gastos Financieros
3. Campos calculados: Utilidad Bruta, Utilidad Operativa, Utilidad Neta
4. Segmentadores: Año, Trimestre, Centro de Costo
5. Formato condicional: utilidades en verde, pérdidas en rojo

### Resumen del capítulo

| Herramienta | Uso contable |
|-------------|-------------|
| Tabla dinámica | Resumir transacciones por período |
| Segmentadores | Filtrar por centro costo, tipo |
| Línea de tiempo | Filtrar por fechas |
| Agrupación | Crear jerarquías contables |
| GETPIVOTDATA | Extraer valores para reportes |
| Campos calculados | Indicadores financieros |
| Formato condicional | Alertas visuales |

### Enigma contable #6

En `codigos/06_tablas_dinamicas/ventas_anuales.xlsx` tienes 20,000 transacciones de ventas de todo un año.

**Tu misión:**
1. Crea una tabla dinámica que muestre ventas por mes y por categoría de producto
2. Agrega un segmentador por región y una línea de tiempo por trimestre
3. Crea un campo calculado "Utilidad" (Ventas * 0.25)
4. Agrupa los productos en categorías: Electrónicos, Ropa, Alimentos, Hogar
5. Aplica formato condicional: resalta en rojo los meses con ventas menores a 50,000 y en verde los mayores a 200,000
6. Crea un reporte GETPIVOTDATA que muestre: Ventas totales, Ventas por región, y % de crecimiento vs mes anterior