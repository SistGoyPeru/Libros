# Capítulo 3: Libro Diario y Libro Mayor

## El ADN de la contabilidad

—El libro diario y el libro mayor —dijo Don Alberto— son el ADN de la contabilidad. Sin ellos, no hay estados financieros, no hay auditoría, no hay nada.

María observaba la pantalla. Don Alberto había abierto un archivo con cientos de filas de transacciones.

### La Historia

—¡María, urgente! —gritó Don Ricardo desde la puerta de su oficina—. La SUNAT nos ha solicitado el libro diario y el libro mayor de "Importaciones del Sur" de los últimos 4 años. ¡Tenemos que entregarlos en una semana!

María sintió que el estómago se le encogía. Cuatro años de transacciones. Miles de asientos contables.

Don Alberto, que estaba cerca, le sonrió.

—No te preocupes. Excel puede hacer esto en cuestión de horas si lo configuras bien.

### Libro Diario en Excel

—El libro diario registra cada transacción en orden cronológico. En Excel, lo modelamos así:

| Fecha | Comprobante | Glosa | Cuenta Debe | Cuenta Haber | Debe S/ | Haber S/ |
|-------|------------|-------|-------------|--------------|---------|----------|
| 01/01 | CP-001 | Apertura | 1.1.1.1 | 5.1.1.1 | 50,000 | 50,000 |
| 01/01 | CP-001 | Apertura | 1.1.1.1 | 4.1.1.1 | 30,000 | 30,000 |

Don Alberto explicó:

—Cada fila es una transacción. Pero cuidado: una transacción puede tener múltiples líneas (debe y haber). La clave está en que la suma del debe debe ser igual a la suma del haber.

**Validación de partida doble:**

```
=D5+E5+F5+G5
```

—No —dijo Don Alberto—. Así no. La validación debe ser:

```
Celda H5 (total debe) = SUMAR.SI(rango, "Debe", rango_monto)
Celda I5 (total haber) = SUMAR.SI(rango, "Haber", rango_monto)
```

—Y la validación general:

```
=SI(SUMA(debe_rango)=SUMA(haber_rango), "CUADRA", "NO CUADRA")
```

### Tabla de Excel para el libro diario

—Convierte tu rango en **Tabla de Excel** (Ctrl + T) —dijo Don Alberto—. Esto te dará:

1. Filtros automáticos por fecha y comprobante
2. Referencias estructuradas (Tabla[Columna])
3. Expansión automática al agregar filas
4. Fórmulas que se copian solas

```
Seleccionar datos > Ctrl + T > Aceptar
Nombre de tabla: tblDiario
```

### Cálculos automáticos en el libro diario

—Ahora, los totales mensuales:

```
Total Debe Enero = SUMAR.SI.CONJUNTO(
    tblDiario[Debe],
    tblDiario[Fecha], ">=01/01/2025",
    tblDiario[Fecha], "<=31/01/2025"
)
```

—O mejor, con tabla dinámica.

### Libro Mayor en Excel

—El libro mayor agrupa las transacciones por cuenta. Es como un resumen de todo lo que ha pasado en cada cuenta.

Don Alberto mostró cómo construirlo:

**Paso 1: Extraer cuentas únicas**
```
=UNICOS(tblDiario[Cuenta])
```
—Esta función de Excel 365 extrae automáticamente todas las cuentas sin duplicados.

**Paso 2: Saldo inicial de cada cuenta**
```
=SUMAR.SI(tblDiario[Cuenta], A2, tblDiario[Debe]) -
 SUMAR.SI(tblDiario[Cuenta], A2, tblDiario[Haber])
```

**Paso 3: Movimientos del período**
```
=SUMAR.SI(tblDiario[Cuenta], A2, tblDiario[Monto])
```

**Paso 4: Saldo final**
```
=SaldoInicial + SUMAR.SI.CONJUNTO(
    tblDiario[Debe], tblDiario[Cuenta], A2
) - SUMAR.SI.CONJUNTO(
    tblDiario[Haber], tblDiario[Cuenta], A2
)
```

### Asientos de ajuste automáticos

—Algo que los contadores hacen constantemente —dijo Don Alberto— son los asientos de ajuste. Podemos automatizar algunos:

**Depreciación lineal mensual:**
```
=MontoActivo / (VidaUtil * 12)
```

**Devengado de alquileres:**
```
=SI(DíaActual>=InicioContrato, AlquilerMensual, 0)
```

**Provisiones mensuales:**
```
=Ingresos * PorcentajeProvision
```

### Conteo rápido con funciones contables

Don Alberto mostró algunas funciones clave:

**CONTAR.SI para tipos de comprobantes:**
```
=CONTAR.SI(tblDiario[Comprobante], "CP-*")
=CONTAR.SI(tblDiario[Comprobante], "FAC-*")
```

**SUMAR.SI.CONJUNTO para análisis detallado:**
```
=SUMAR.SI.CONJUNTO(
    tblDiario[Monto],
    tblDiario[Cuenta], "1.1.1.*",
    tblDiario[Fecha], ">=01/01/2025",
    tblDiario[Fecha], "<=31/03/2025"
)
```

### Resumen del capítulo

| Concepto | Fórmula / Herramienta |
|----------|----------------------|
| Tabla Excel | Ctrl + T, nombres estructurados |
| Validación partida doble | SUMAR.SI(debe) = SUMAR.SI(haber) |
| Cuentas únicas | =UNICOS(rango) |
| Saldo por cuenta | SUMAR.SI(debe) - SUMAR.SI(haber) |
| Análisis temporal | SUMAR.SI.CONJUNTO con fechas |
| Agrupación | Tabla dinámica por cuenta |

### Enigma contable #3

Don Ricardo te ha pasado el archivo `codigos/03_diario_mayor/transacciones_anuales.xlsx` con 3,000 transacciones del año 2025 de "Importaciones del Sur S.A.C."

**Tu misión:**
1. Convierte los datos en una Tabla de Excel (Ctrl + T)
2. Verifica que todas las transacciones cumplan la partida doble (Total Debe = Total Haber)
3. Crea el Libro Mayor con saldos por cuenta usando SUMAR.SI.CONJUNTO
4. Identifica qué cuentas tuvieron más movimiento (mayor cantidad de transacciones)
5. Genera un asiento de ajuste automático para la depreciación mensual

*Entregable: un libro con 3 hojas (Diario, Mayor, Ajustes) listo para presentar a la SUNAT.*