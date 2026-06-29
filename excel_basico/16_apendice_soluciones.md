# Apéndice: Soluciones a los Enigmas

### Capítulo 1: El Taller Heredado

**Enigma 1.1:**
1. Un libro nuevo de Excel tiene 3 hojas por defecto.
2. La celda D7 (B + 3 columnas = E, pero partiendo de B: C, D, E — la tercera columna a la derecha de B es E. Fila: 5 + 2 = 7. Celda: E7).
3. La pestaña **Inicio** contiene los grupos Fuente, Alineación y Número, donde puedes cambiar el color de una celda.
4. La **Barra de fórmulas**.

**Enigma 1.2:**
Tabla de herramientas:

| Producto | Cantidad | Precio Unitario |
|----------|----------|-----------------|
| Cinceles | 15 | S/ 25.00 |
| Martillos | 8 | S/ 45.00 |
| Cepillos de carpintero | 6 | S/ 60.00 |
| Escuadras | 12 | S/ 18.00 |
| Niveles | 4 | S/ 35.00 |

**Enigma 1.3:**
En la pestaña Insertar, los tipos de gráficos disponibles incluyen: Columna, Línea, Circular, Barra, Área, Dispersión, entre otros. El botón **Autosuma** en la pestaña Fórmulas inserta automáticamente una fórmula SUM (SUMA) para sumar los valores del rango adyacente.

**Enigma 1.4:**
Para seleccionar un rango, haz clic en la primera celda y arrastra hasta la última. Para borrar, selecciona las celdas y presiona Suprimir (o Delete).

---

### Capítulo 2: El Primer Inventario

**Enigma 2.1:**
Tabla de herramientas de almacén:

| Producto | Cantidad | Precio Unitario | Calidad |
|----------|----------|-----------------|---------|
| Taladro inalámbrico | 2 | S/ 280.00 | A |
| Sierra circular | 3 | S/ 350.00 | A |
| Lijadora orbital | 2 | S/ 180.00 | B |
| Juego de brocas | 5 | S/ 45.00 | B |
| Extensión eléctrica 10m | 4 | S/ 25.00 | C |

**Enigma 2.2:**
Si A=1, B=2, C=3:
- Taladro: A → 1
- Sierra: A → 1
- Lijadora: B → 2
- Brocas: B → 2
- Extensión: C → 3
Suma total: 1+1+2+2+3 = 9

**Enigma 2.4:**
La lista ingresada sería:
A1: Sillón, A2: Mesa, A3: Silla, A4: Banquito, A5: Estante, A6: Cómoda, A7: Ropero

---

### Capítulo 3: Las Fórmulas del Abuelo

**Enigma 3.1:**
Costos de producción:

| Producto | Costo Total | Ganancia | % Ganancia |
|----------|-------------|----------|-------------|
| Silla de roble | 62+8+4+40 = 114 | 200-114 = 86 | 86/114 = 75.44% |
| Mesa de cedro | 135+12+6+60 = 213 | 350-213 = 137 | 137/213 = 64.32% |
| Banquito de pino | 22+4+2+18 = 46 | 75-46 = 29 | 29/46 = 63.04% |
| Estante de triplay | 70+8+5+40 = 123 | 160-123 = 37 | 37/123 = 30.08% |

Fórmulas:
- Costo Total: =B2+C2+D2+E2
- Ganancia: =G2-F2
- % Ganancia: =(G2-F2)/F2

**Enigma 3.2:**
Precio con IVA: =Precio_Venta*1.18
Precio con descuento del 10%: =Precio_con_IVA*0.90

Para la silla de roble: Precio Venta = 200
IVA: =200*1.18 = 236
10% descuento: =236*0.90 = 212.40

**Enigma 3.3:**
1. =90*5 = S/ 450
2. =(150-90)*5 = S/ 300
3. =150*5*1.18 = S/ 885

**Enigma 3.4:**
1. `=A1+B1*` → Error: operador * sin segundo argumento. Corregido: `=A1+B1`
2. `suma(A1:A10)` → Falta = al inicio. Corregido: `=SUMA(A1:A10)`
3. `=A1/0` → División entre cero. Corregido: asegúrate de que el divisor no sea cero
4. `=B2 + C2` → Funciona correctamente en Excel, los espacios no afectan

---

### Capítulo 4: El Misterio de las Referencias

**Enigma 4.1:**
En la fórmula =B2*(1-C$1), C$1 mantiene fija la fila 1 (donde están los porcentajes) pero permite que la columna se desplace al copiar a la derecha (D$1, E$1). Esto permite que cada producto se multiplique por las diferentes tasas de descuento.

Para llenar la tabla, copia =B2*(1-C$1) de C2 a E5. Las referencias se ajustan automáticamente.

**Enigma 4.2:**
=SUMA(B2:D2)*$H$1

**Enigma 4.3:**
Si copias =A1+B1 de C1 a C10, la fórmula será =A10+B10 (referencias relativas se ajustan 9 filas hacia abajo).
Si la fórmula fuera =$A$1+$B$1, seguiría siendo =$A$1+$B$1 al copiarla a C10 (referencias absolutas no cambian).

**Enigma 4.4:**
=$B2*C$1 funciona porque:
- $B2: La columna B es absoluta (siempre el mismo producto), pero la fila es relativa (cambia al copiar hacia abajo)
- C$1: La columna C es relativa (cambia al copiar hacia la derecha para usar Colombia), pero la fila 1 es absoluta (siempre los porcentajes del encabezado)

---

### Capítulo 5: Dando Forma a los Números

**Enigma 5.2:**
Productos en rojo (cantidad < 20): Barniz mate (10), Barniz brillante (8), Pegamento para madera (12).
Revisa tu inventario completo para ver todos los que estén por debajo de 20 unidades.

**Enigma 5.3:**
Clasificación por tipo:
- **Madera:** Cedro, Roble, Pino, Triplay (fondo marrón claro)
- **Herramienta:** Sin herramientas en el inventario básico
- **Insumo:** Barniz mate, Barniz brillante, Tornillos #10, Tornillos #8, Lija fina, Lija gruesa, Pegamento (fondo blanco)

**Enigma 5.4:**
Para bordes profesionales, selecciona el rango y usa Inicio > Bordes > Más bordes. Allí puedes elegir diferentes grosores para bordes exteriores e interiores.

---

### Capítulo 6: El Pedido Especial

**Enigma 6.1:**
1. SUMA del Precio Unitario: =SUM(D2:D12) (usando datos del Capítulo 1)
2. PROMEDIO: =AVERAGE(D2:D12)
3. MAX: =MAX(D2:D12) → S/ 62.00 (Roble)
4. MIN: =MIN(D2:D12) → S/ 0.40 (Tornillos #8)
5. CONTAR productos con precio > 30: =COUNTIF(D2:D12,">30")

**Enigma 6.2:**
1. Total por producto: =SUM(rango de cada producto)
2. Promedio mensual de totales: =AVERAGE(rango de totales mensuales)
3. Mes con ventas más altas: =MAX(rango de totales)
4. Mes con ventas más bajas: =MIN(rango de totales)
5. Valores > 1000: =COUNTIF(rango,">1000")

**Enigma 6.3:**
Para encontrar el stock mínimo: =MIN(B2:B8)
Si el resultado es 10 (Barniz), ese producto está por debajo de 15.
Productos por debajo de 15: Barniz (10).

**Enigma 6.4:**
1. Total general: =SUMA(C2:C5*D2:D5) — ingresa como fórmula matricial o suma los subtotales uno por uno
   Alternativa: =C2*D2 + C3*D3 + C4*D4 + C5*D5
2. Precio promedio: =PROMEDIO(D2:D5)
3. Herramienta más cara: =MAX(D2:D5) → S/ 350.00 (Sierra circular)
4. Herramienta más barata: =MIN(D2:D5) → S/ 45.00 (Juego de brocas)

---

### Capítulo 7: Un Vistazo al Progreso

**Enigma 7.1:**
Gráfico de stock. El producto con más stock es Tornillos #10 (500 unidades). El producto con menos stock (entre los materiales principales) es Barniz brillante (8 unidades).

**Enigma 7.2:**
La tendencia es irregular, con picos en abril (S/ 3,100) y valles en marzo (S/ 2,300). No hay una tendencia clara al alza o a la baja.

**Enigma 7.3:**
- Calidad A: 80 tablas (36.36%)
- Calidad B: 100 tablas (45.45%)
- Calidad C: 40 tablas (18.18%)
La calidad predominante es la B (segunda).

**Enigma 7.4:**
Agrupa los gráficos en una hoja llamada "Informe_Banco". Usa Combinar y centrar para el título general. Ajusta el tamaño de los gráficos arrastrando sus bordes.

---

### Capítulo 8: La Feria de la Madera

**Enigma 8.1:**
1. Productos ordenados alfabéticamente
2. Precio Unitario de mayor a menor: Roble (S/ 62.00), Cedro (S/ 45.00), Triplay (S/ 35.00), Barniz brillante (S/ 32.00), Barniz mate (S/ 28.00), Pino (S/ 22.00), Pegamento (S/ 15.00), Lija fina (S/ 1.20), Lija gruesa (S/ 0.80), Tornillos #10 (S/ 0.50), Tornillos #8 (S/ 0.40)
3. Orden por Proveedor (A-Z) y Cantidad (mayor a menor)
4. Producto más caro: Madera de Roble (S/ 62.00). Producto más barato: Tornillos #8 (S/ 0.40)

**Enigma 8.2:**
1. Calidad A: Cedro, Roble
2. Precio < 300: Pino (22), Triplay (35), Barniz mate (28), Barniz brillante (32), Tornillos #10 (0.50), Tornillos #8 (0.40), Lija fina (1.20), Lija gruesa (0.80), Pegamento (15)
3. Productos que contienen "cama" o "mesa": Cama king, Cama queen, Mesa de centro, Mesa de noche, Mesa comedor
4. Calidad B con precio entre 100 y 300: Escritorio (280), Mesa de centro (250), Mesa de noche (120)
5. Calidad A con precio > 500: Ropero (890), Cama king (680), Cama queen... depende de los datos

**Enigma 8.3:**
Problemas comunes a corregir:
1. Unificar nombres: decidir "Silla comedor" como nombre estándar
2. Corregir ortografía: "Mesa centro"
3. Corregir decimal: 42.0 → 420.00

**Enigma 8.4:**
Para la columna Disponibilidad, si la cantidad está en columna B de la hoja original:
=SI(B2>10,"Inmediata","Bajo pedido")
(o hazlo manualmente si aún no has visto la función SI)

---

### Capítulo 9: El Presupuesto Final

**Enigma 9.1:**
Configura la impresión paso a paso siguiendo las instrucciones del capítulo. El resultado debe ser un documento con encabezado profesional, márgenes estrechos, orientación horizontal.

**Enigma 9.2:**
Depende de tus datos. Generalmente, las tablas con más de 5 columnas funcionan mejor en orientación horizontal. Los márgenes estrechos ayudan a aprovechar más espacio.

**Enigma 9.3:**
Al configurar encabezados y pies de página, los códigos &[Página], &[Fecha] y &[Hora] se reemplazan automáticamente.

**Enigma 9.4:**
Este ejercicio integra todos los conceptos. No hay una única solución correcta. Verifica que:
- Las fórmulas den resultados correctos
- Los formatos sean consistentes
- La impresión se vea profesional

---

### Capítulo 10: La Gran Apertura

**Enigma 10.1:**
No hay una única solución para el proyecto integrador. Tu informe debe incluir:
- Mínimo 4 hojas con datos coherentes
- Fórmulas que conecten las hojas
- Formato profesional (monedas, fechas, colores)
- Al menos 3 gráficos de diferentes tipos
- Funciones SUM, AVERAGE, MAX, MIN

**Enigma 10.2:**
Para exportar a PDF: Archivo > Exportar > Crear PDF. Ajusta la configuración de página antes de exportar.

**Enigma 10.3:**
Respuesta personal. Comparte tu experiencia y tus metas.

---

**Nota:** Estas soluciones son una guía. No hay una única forma correcta de resolver los enigmas. Si tu solución funciona y tiene sentido, ¡es válida!
