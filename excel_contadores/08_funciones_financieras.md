# Capítulo 4: Funciones Financieras Esenciales

## Cuando el dinero habla en Excel

—Las funciones financieras —dijo Don Alberto— son la diferencia entre un contador que aprieta botones y un contador que entiende el dinero.

### La Historia

—Don Alberto —dijo María—, el gerente de "Importaciones del Sur" quiere saber si conviene comprar una máquina nueva. Dice que cuesta S/ 200,000 y generará ingresos de S/ 50,000 al año durante 5 años. ¿Cómo le respondo?

Don Alberto sonrió.

—Esa es una pregunta de valor actual neto y tasa interna de retorno. Vamos a resolverla con Excel.

### VA — Valor Actual

—El valor actual —explicó Don Alberto— te dice cuánto vale hoy un pago futuro.

```
=VA(tasa, nper, pago, [vf], [tipo])
```

**Ejemplo contable:** ¿Cuánto vale hoy S/ 100,000 que recibirás en 3 años si la tasa de descuento es 8%?

```
=VA(8%, 3, 0, -100000, 0)
Resultado: S/ 79,383.25
```

—Es decir —dijo Don Alberto—, si alguien te ofreciera S/ 79,383 hoy en lugar de S/ 100,000 en 3 años, sería equivalente.

### VF — Valor Futuro

—El valor futuro es lo contrario: cuánto valdrá en el futuro una inversión de hoy.

```
=VF(tasa, nper, pago, [va], [tipo])
```

**Ejemplo contable:** Si inviertes S/ 50,000 hoy al 6% anual, ¿cuánto tendrás en 5 años?

```
=VF(6%, 5, 0, -50000, 0)
Resultado: S/ 66,911.28
```

### PAGO — Cuota de préstamo

—Esta —dijo Don Alberto— es quizás la función financiera más usada. Calcula la cuota de un préstamo.

```
=PAGO(tasa, nper, va, [vf], [tipo])
```

**Ejemplo contable:** Préstamo de S/ 150,000 al 12% anual a 36 meses. ¿Cuánto se paga cada mes?

```
=PAGO(12%/12, 36, 150000, 0, 0)
Resultado: -S/ 4,982.14 (cuota mensual)
```

—Pero el contador necesita más que la cuota —dijo Don Alberto—. Necesita desglosar cuánto es interés y cuánto es amortización.

### PAGOINT y PAGOPRIN — Interés y amortización

**Interés del período 1:**
```
=PAGOINT(12%/12, 1, 36, 150000)
Resultado: -S/ 1,500.00
```

**Amortización del período 1:**
```
=PAGOPRIN(12%/12, 1, 36, 150000)
Resultado: -S/ 3,482.14
```

**Tabla de amortización completa:**
Don Alberto mostró cómo construir una tabla:

```
Período 1:
  Saldo inicial: S/ 150,000
  Interés: =SALDOINICIAL * (12%/12) = S/ 1,500
  Cuota: =PAGO(...) = S/ 4,982.14
  Amortización: =Cuota - Interés = S/ 3,482.14
  Saldo final: =SaldoInicial - Amortización = S/ 146,517.86

Período 2:
  Saldo inicial: =Saldo final período anterior
  ... y así sucesivamente
```

### TIR — Tasa Interna de Retorno

—La TIR —dijo Don Alberto— es la rentabilidad real de un proyecto o inversión.

```
=TIR(rango_flujos, [estimar])
```

**Ejemplo:** Inversión inicial de S/ 200,000 y flujos de S/ 50,000 anuales por 5 años. ¿Cuál es la TIR?

| Año | Flujo |
|-----|-------|
| 0 | -200,000 |
| 1 | 50,000 |
| 2 | 50,000 |
| 3 | 50,000 |
| 4 | 50,000 |
| 5 | 50,000 |

```
=TIR(B2:B7) → 7.93%
```

—Esto significa —explicó— que el proyecto rinde 7.93% anual. Si la tasa de descuento de la empresa es menor (ej. 5%), el proyecto es rentable.

### VAN — Valor Actual Neto

—El VAN complementa la TIR —dijo Don Alberto—. Mientras la TIR te da el porcentaje, el VAN te da el valor absoluto.

```
=VNA(tasa, rango_flujos)
```
—Pero cuidado —advirtió—: VNA descuenta desde el período 1. Para incluir la inversión inicial, debes sumarla aparte.

**Ejemplo correcto:**
```
Inversión inicial (año 0): -200,000
Flujos (año 1 a 5): 50,000 cada uno
Tasa de descuento: 10%

= -200000 + VNA(10%, B3:B7)
Resultado: -S/ 10,460.78
```

—El VAN es negativo —dijo Don Alberto—. Significa que a una tasa de descuento del 10%, el proyecto no es rentable. Pero recuerda que la TIR era 7.93%. Tiene sentido: si la tasa de descuento (10%) es mayor que la TIR (7.93%), el VAN es negativo.

### TIRM — TIR Modificada

—La TIR tiene un problema —explicó Don Alberto—: asume que los flujos intermedios se reinvierten a la misma TIR. La TIRM corrige esto:

```
=TIRM(rango_flujos, tasa_financiamiento, tasa_reinversion)
```

**Ejemplo:**
```
=TIRM(B2:B7, 8%, 6%)
```

—Aquí asumimos que pedimos dinero al 8% y reinvertimos los flujos al 6%. La TIRM suele ser más realista que la TIR.

### Análisis de escenarios financieros

—Ahora —dijo Don Alberto—, combinemos todo. Vamos a crear un modelo con tres escenarios:

| Escenario | Inversión | Flujo anual | Tasa descuento | VAN | TIR |
|-----------|-----------|-------------|----------------|-----|-----|
| Optimista | 180,000 | 55,000 | 8% | | |
| Realista | 200,000 | 50,000 | 10% | | |
| Pesimista | 220,000 | 42,000 | 12% | | |

**Herramienta Análisis Y Si:**
—Podemos usar la tabla de datos de Excel:

```
Datos > Análisis Y Si > Tabla de datos
Fila: diferentes tasas
Columna: diferentes inversiones
```

### Resumen del capítulo

| Función | Qué calcula | Ejemplo contable |
|---------|-------------|------------------|
| VA | Valor actual de flujos futuros | Valor hoy de una cobranza futura |
| VF | Valor futuro de una inversión | Proyección de ahorros |
| PAGO | Cuota de préstamo | Cálculo de cuota mensual |
| PAGOINT | Interés de un período | Gastos financieros mensuales |
| PAGOPRIN | Amortización de un período | Reducción de deuda |
| TIR | Rentabilidad del proyecto | Decisión de inversión |
| VAN | Valor agregado del proyecto | Viabilidad del proyecto |
| TIRM | TIR corregida | Comparación realista |

### Enigma contable #4

El gerente de "Importaciones del Sur" te ha enviado 3 proyectos de inversión en `codigos/04_financieras/proyectos.xlsx`.

**Tu misión:**
1. Calcula la cuota mensual de cada proyecto si se financia al 15% anual
2. Calcula el VAN de cada proyecto con tasa de descuento del 10%
3. Calcula la TIR de cada proyecto
4. Crea una tabla de amortización completa para el proyecto ganador
5. Recomienda qué proyecto conviene más y por qué (basado en VAN y TIR)

*El gerente quiere una respuesta clara: ¿Sí o no a cada proyecto?*