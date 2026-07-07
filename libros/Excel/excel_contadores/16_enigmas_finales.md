# Anexo: Enigmas Contables

## Pon a prueba lo aprendido

Los siguientes enigmas combinan conceptos de varios capítulos. Resuélvelos usando los archivos en `codigos/enigmas/`.

### Enigma Final 1: El Balance que no cuadra

El archivo `enigmas/balance_no_cuadra.xlsx` contiene un balance general que no cuadra por S/ 15,432.00.

**Pistas:**
- Revisa las fórmulas de totales (Capítulo 1)
- Busca referencias circulares (Capítulo 8)
- Verifica que todas las cuentas estén clasificadas correctamente (Capítulo 2)
- Usa auditoría de fórmulas para rastrear el error (Capítulo 8)

**Entrega:** El balance corregido y un informe de una página explicando qué encontraste.

### Enigma Final 2: Automatización de cierre mensual

Crea un sistema de cierre mensual automatizado que:

1. Tome los datos del libro diario del mes (`enigmas/diario_mensual.xlsx`)
2. Calcule automáticamente: depreciación, provisiones, y devengados
3. Genere los asientos de ajuste
4. Actualice el libro mayor
5. Genere el estado de resultados y balance
6. Exporte todo a PDF (Capítulo 10)

**Requisitos:** Todo debe ejecutarse con UNA sola macro. El usuario solo debe hacer clic en "Cierre Mensual".

**Bonus:** Agrega un mensaje de confirmación que muestre: Utilidad del mes, Total de asientos generados, y Estado de cuadratura.

### Enigma Final 3: Dashboard de auditoría

Crea un dashboard que consolide la información de auditoría de 12 meses.

**Datos:** `enigmas/auditoria_anual.xlsx` (12 hojas, una por mes)

**Indicadores:**
- Total de errores encontrados por mes
- Top 5 tipos de errores más comunes
- Porcentaje de transacciones auditadas vs total
- Evolución mensual de la calidad de datos
- Tiempo estimado ahorrado por automatización

**Formato:** Dashboard interactivo con segmentadores por trimestre.

### Enigma Final 4: El modelo financiero

Construye un modelo financiero a 5 años para una startup:

**Supuestos:**
- Inversión inicial: S/ 500,000
- Ventas año 1: S/ 200,000 (crecimiento 30% anual)
- Costo de ventas: 60% de ventas
- Gastos operativos: S/ 50,000 (crecimiento 5% anual)
- Tasa de descuento: 12%

**Entregables:**
1. Estado de resultados proyectado (5 años)
2. Flujo de caja libre
3. VAN y TIR del proyecto
4. Análisis de sensibilidad (variar crecimiento de ventas entre 20% y 50%)
5. Gráfico de punto de equilibrio
6. Recomendación: invertir o no invertir

### Enigma Final 5: Consolidación interplanetaria

La empresa "CosmoContadores S.A.C." tiene sucursales en 4 países: Perú (S/), USA ($), Europa (€), y Japón (¥).

El archivo `enigmas/cosmo_contadores.xlsx` contiene los estados financieros de cada sucursal en su moneda local. La tabla de tipos de cambio está en la hoja "TC".

**Tu misión:**
1. Convierte todas las monedas a S/ (soles peruanos)
2. Consolida los 4 estados financieros
3. Elimina las transacciones intercompañía (hoja "InterCo")
4. Calcula la participación de la matriz (80% de cada sucursal)
5. Genera el balance consolidado final
6. Calcula los KPIs consolidados: ROE, ROA, Liquidez, Endeudamiento

**¿Cuál es la utilidad neta consolidada del grupo CosmoContadores?**