
# Capítulo 6: La Estrategia Óptima

## Solver, Análisis Y si Avanzado, Escenarios

El día 18 de los 30 que tenían para responder a Nova, Sofía recibió una llamada que lo cambió todo.

—¿Señorita Mendoza? Habla el Dr. Ricardo Paredes, de la UIF. Hemos recibido su informe preliminar.

El corazón de Sofía se aceleró. —¿Y?

—Es convincente. Pero necesitamos más. Mucho más. Especialmente en una área: el valor real de su taller.

—¿El valor? —preguntó Sofía, confundida.

—Nova va a argumentar que la oferta de $850,000 es justa. Que el taller no vale más. Necesitamos que usted demuestre, con números irrefutables, que su negocio vale significativamente más. Eso fortalecería la tesis de que Nova está usando una valoración artificialmente baja para facilitar el lavado.

Sofía colgó y se quedó mirando la pantalla.

—¿Cómo demostramos cuánto vale realmente el taller? —preguntó.

Valeria ya estaba abriendo el complemento **Solver**.

### El problema de optimización

—Solver es un complemento de Excel que encuentra el valor óptimo de una celda objetivo cambiando los valores de otras celdas, sujeto a restricciones.

—¿Como un objetivo y restricciones? —preguntó Carlos.

—Exactamente. Queremos maximizar el valor del taller. Las variables de decisión son: precios de productos, cantidad de pedidos, distribución de recursos. Las restricciones: capacidad de producción, disponibilidad de materiales, demanda del mercado.

Valeria construyó el modelo en Excel:

**Celdas variables (lo que podemos cambiar):**

| Variable | Celda | Valor actual | Límite inferior | Límite superior |
|----------|-------|-------------|-----------------|-----------------|
| Precio silla estándar | B5 | S/ 150 | S/ 120 | S/ 200 |
| Precio silla ejecutiva | B6 | S/ 280 | S/ 220 | S/ 350 |
| Precio mesa familiar | B7 | S/ 450 | S/ 380 | S/ 550 |
| Precio mesa ejecutiva | B8 | S/ 780 | S/ 650 | S/ 950 |
| Prod. silla estándar/mes | C5 | 120 | 80 | 200 |
| Prod. silla ejecutiva/mes | C6 | 45 | 30 | 80 |
| Prod. mesa familiar/mes | C7 | 30 | 20 | 50 |
| Prod. mesa ejecutiva/mes | C8 | 15 | 10 | 30 |

**Celda objetivo (maximizar):** Valor del negocio (proyección a 5 años)

**Restricciones:**
- Horas de mano de obra ≤ 1,200 horas/mes
- Consumo de madera ≤ 5,000 pies tablares/mes
- Costo de materiales ≤ S/ 60,000/mes
- Capacidad de almacenamiento ≤ 200 unidades/mes
- Demanda máxima por producto (según histórico)

Sofía observó cómo Valeria ingresaba cada restricción en Solver.

—Solver usa algoritmos de optimización. Para problemas lineales usa el método simplex. Para no lineales, el método GRG (Generalized Reduced Gradient).

Valeria hizo clic en **Resolver**.

La pantalla parpadeó. Los números cambiaron.

—Miren los resultados —dijo Valeria.

**Resultados de la optimización:**

| Variable | Valor actual | Valor óptimo | Cambio |
|----------|-------------|-------------|--------|
| Precio silla estándar | S/ 150 | S/ 175 | +16.7% |
| Precio silla ejecutiva | S/ 280 | S/ 310 | +10.7% |
| Precio mesa familiar | S/ 450 | S/ 480 | +6.7% |
| Precio mesa ejecutiva | S/ 780 | S/ 850 | +9.0% |
| Prod. silla estándar/mes | 120 | 160 | +33.3% |
| Prod. silla ejecutiva/mes | 45 | 60 | +33.3% |
| Prod. mesa familiar/mes | 30 | 35 | +16.7% |
| Prod. mesa ejecutiva/mes | 15 | 20 | +33.3% |

**Valor del negocio (proyección 5 años):**

| Escenario | Valor |
|-----------|-------|
| Actual | S/ 2,450,000 |
| Óptimo | S/ 4,820,000 |
| Diferencia | +96.7% |

—El taller vale casi 5 millones de soles, no 850 mil dólares —dijo Sofía, incrédula.

—Menos de 3 millones de dólares al tipo de cambio actual —calculó Carlos.

—Exactamente. Nova te está ofreciendo menos del 30% del valor real de tu negocio —dijo Valeria—. Eso no es una oferta. Es un robo.

### Análisis Y si y escenarios

—Pero Nova va a decir que tus proyecciones son demasiado optimistas —continuó Valeria—. Necesitamos mostrar múltiples escenarios.

Valeria usó **Administrador de escenarios** (Datos > Análisis Y si > Administrador de escenarios).

Creó tres escenarios:

**1. Escenario Pesimista:**
- Crecimiento del mercado: 2% anual
- Inflación de materiales: 8% anual
- Demanda: estable

**2. Escenario Moderado:**
- Crecimiento del mercado: 5% anual
- Inflación de materiales: 4% anual
- Demanda: crecimiento moderado

**3. Escenario Optimista (Solver):**
- Crecimiento del mercado: 8% anual
- Inflación de materiales: 3% anual
- Demanda: crecimiento acelerado

—Ahora, con un clic, podemos cambiar entre escenarios y ver cómo cambia el valor.

Valeria creó un **informe de resumen de escenarios**:

| Celda de resultado | Actual | Pesimista | Moderado | Optimista |
|-------------------|--------|-----------|----------|-----------|
| Valor 1 año | S/ 520K | S/ 480K | S/ 560K | S/ 650K |
| Valor 3 años | S/ 1.8M | S/ 1.4M | S/ 2.1M | S/ 2.9M |
| Valor 5 años | S/ 2.45M | S/ 1.9M | S/ 3.2M | S/ 4.82M |
| ROI anual | 18% | 12% | 22% | 35% |

—Incluso en el escenario pesimista, el taller vale más de 1.9 millones de soles. Más del doble de lo que ofrece Nova.

### Tabla de sensibilidad

—Y para rematar —dijo Valeria—, una **tabla de sensibilidad de dos variables**.

Creó una tabla donde las filas eran diferentes tasas de crecimiento del mercado (de 0% a 15%) y las columnas diferentes niveles de eficiencia operativa (de 70% a 100%).

```
=TABLE(B20, B21)  ' B20 = crecimiento, B21 = eficiencia
```

La tabla mostraba cómo el valor del negocio cambiaba según estas dos variables.

| Eficiencia → | 70% | 75% | 80% | 85% | 90% | 95% | 100% |
|--------------|-----|-----|-----|-----|-----|-----|------|
| Crec. 0% | 1.2M | 1.3M | 1.5M | 1.6M | 1.8M | 1.9M | 2.1M |
| Crec. 3% | 1.5M | 1.7M | 1.9M | 2.1M | 2.3M | 2.5M | 2.7M |
| Crec. 5% | 1.8M | 2.0M | 2.2M | 2.5M | 2.7M | 2.9M | 3.2M |
| Crec. 8% | 2.2M | 2.5M | 2.8M | 3.1M | 3.4M | 3.7M | 4.8M |
| Crec. 10% | 2.5M | 2.8M | 3.1M | 3.5M | 3.9M | 4.3M | 5.5M |
| Crec. 15% | 3.1M | 3.5M | 4.0M | 4.5M | 5.1M | 5.7M | 7.2M |

—Incluso con el peor crecimiento y la peor eficiencia, el taller nunca baja de 1.2 millones de soles —dijo Sofía—. Nova nos está timando.

—Y esto es exactamente lo que la UIF necesita ver —dijo Valeria—. Un análisis profesional que demuestre que la oferta de Nova es sospechosamente baja. Parte del patrón de lavado.

—Pero necesito más que números —dijo Sofía—. Necesito un panel de control que le hable a cualquier persona. Un dashboard.

Valeria sonrió. —Eso es justo lo siguiente que iba a enseñarte.

---

## Explicación técnica: Solver, Análisis Y si y Escenarios

### Solver

**Solver** es un complemento de Excel que encuentra valores óptimos (máximo, mínimo o un valor específico) para una celda objetivo, cambiando los valores de otras celdas, sujeto a restricciones.

#### Cómo habilitar Solver

1. **Archivo > Opciones > Complementos**
2. En "Administrar", seleccionar **Complementos de Excel** > **Ir**
3. Marcar **Complemento Solver**
4. La pestaña **Datos** ahora tendrá el botón **Solver**

#### Componentes de Solver

| Componente | Descripción | Ejemplo |
|------------|-------------|---------|
| Celda objetivo | Celda a optimizar | $F$10 (Valor del negocio) |
| Valor de objetivo | Máximo, Mínimo o Valor específico | Máximo |
| Celdas variables | Celdas que Solver puede modificar | $B$5:$C$8 (Precios y producciones) |
| Restricciones | Condiciones que deben cumplirse | $D$5 <= 1200 (Horas) |

#### Tipos de problemas en Solver

| Método | Tipo de problema | Requisitos |
|--------|-----------------|------------|
| GRG No Lineal | Problemas suaves no lineales | Funciones continuas y derivables |
| LP Simplex | Problemas lineales | Funciones lineales en variables |
| Evolutivo | Problemas no suaves | Puede manejar funciones discontinuas |

#### Sintaxis de restricciones

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| <= | Menor o igual | Horas <= 1200 |
| >= | Mayor o igual | Producción >= 20 |
| = | Igual | Producción = Demanda |
| int | Entero | Precios deben ser enteros |
| bin | Binario (0 o 1) | Decisión de producir o no |

### Análisis Y si

Excel ofrece tres herramientas de análisis Y si:

**1. Administrador de escenarios:**
Guarda diferentes conjuntos de valores para las celdas variables y permite cambiar entre ellos.

**2. Buscar objetivo:**
Encuentra el valor de una celda que produce un resultado deseado en otra.

```
' Buscar qué precio produce utilidad de S/ 500,000
Datos > Análisis Y si > Buscar objetivo
Celda: F10 (Utilidad)
Valor: 500000
Celda cambiante: B5 (Precio)
```

**3. Tabla de datos (sensibilidad):**
Muestra cómo cambia una fórmula al modificar una o dos variables de entrada.

- **Una variable**: Tabla donde la fila/columna tiene los valores de la variable
- **Dos variables**: Tabla donde filas tienen valores de variable 1 y columnas de variable 2

### Crear una tabla de datos de dos variables

1. En una celda, escribe la fórmula que calcula el resultado (ej: valor del negocio)
2. En una columna, escribe los valores de la primera variable
3. En una fila (arriba de la columna), escribe los valores de la segunda variable
4. Selecciona toda la tabla
5. Datos > Análisis Y si > Tabla de datos
6. Celda de fila: celda de la segunda variable
7. Celda de columna: celda de la primera variable

### Interpretación de resultados de optimización

- **Solución encontrada**: Solver encontró un punto óptimo
- **Solución no mejorable**: Se alcanzó una solución óptima local
- **No se encontró solución**: Las restricciones son incompatibles (sobredeterminado)
- **Límite de iteraciones**: Solver no convergió (aumentar iteraciones)
- **Informes de Solver**: Respuesta, Sensibilidad, Límites

---

### Enigma 6.1: Optimización de producción

Una fábrica produce dos productos: A (utilidad S/ 50) y B (utilidad S/ 80).

Restricciones:
- Horas máquina: 200 horas/semana (A: 2h, B: 3h)
- Horas mano de obra: 160 horas/semana (A: 1h, B: 2h)
- Demanda máxima de A: 60 unidades/semana
- Demanda máxima de B: 40 unidades/semana

Usa Solver para maximizar la utilidad.

### Enigma 6.2: Análisis de escenarios

Una empresa tiene tres escenarios para el próximo año:

| Variable | Pesimista | Moderado | Optimista |
|----------|-----------|----------|-----------|
| Ventas | S/ 800K | S/ 1.2M | S/ 1.8M |
| Costo fijo | S/ 400K | S/ 350K | S/ 300K |
| Margen variable | 30% | 40% | 50% |

Crea los tres escenarios en el Administrador de escenarios y genera un informe de resumen.

### Enigma 6.3: Tabla de sensibilidad

Eres analista financiero. Una inversión de S/ 100,000 genera retornos variables según:

- **Tasa de interés**: 5% a 15% (variable de fila)
- **Plazo**: 1 a 5 años (variable de columna)

Crea una tabla de datos de dos variables que muestre el valor futuro para todas las combinaciones.

*(Soluciones en el Apéndice)*
