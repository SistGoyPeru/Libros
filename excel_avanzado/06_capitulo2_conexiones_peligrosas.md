
# Capítulo 2: Conexiones Peligrosas

## Power Pivot y Modelo de Datos

Pasaron tres días desde que Valeria llegó al taller. En ese tiempo, habían cargado más de 200,000 filas de datos en Excel usando Power Query. Pero algo empezaba a fallar.

—El archivo pesa 120 MB —dijo Carlos, señalando la barra de estado—. Excel se está volviendo lento.

Valeria asintió. —Es el límite de lo que puede manejar Excel tradicional con tablas en la hoja de cálculo. Para volúmenes mayores, necesitamos Power Pivot.

—¿Power Pivot? —Sofía recordaba haber visto el nombre en algún artículo, pero nunca lo había usado.

—Power Pivot es un motor de análisis de datos en memoria que está integrado en Excel. En lugar de almacenar los datos en las celdas, los comprime y los almacena en memoria RAM. Puede manejar millones de filas sin ralentizar el archivo.

—¿Millones? —repitió Carlos, incrédulo.

—Power Pivot puede manejar hasta 2 mil millones de filas por tabla —dijo Valeria—. Los datos se comprimen a aproximadamente una décima parte de su tamaño original.

Valeria abrió Power Pivot desde la pestaña **Power Pivot > Administrar**. Se abrió una ventana separada, similar a Excel pero más minimalista.

—Esto es Power Pivot. Parece Excel, pero no lo es. Es un motor tabular xVelocity (ahora llamado VertiPaq). No usa celdas. Usa columnas y tablas, como una base de datos.

### Agregando datos al modelo

—Ya tenemos los datos cargados con Power Query —dijo Valeria—. En lugar de cargarlos a una hoja de Excel, podemos cargarlos directamente al modelo de Power Pivot.

Mostró cómo, en el Editor de Power Query, se puede cambiar el destino de carga:

1. En **Archivo > Opciones y configuración > Propiedades de consulta**
2. En la sección **Cargar en**, seleccionar **Solo crear conexión** y marcar **Agregar estos datos al modelo de datos**

—Cada consulta que carguemos al modelo se convierte en una tabla dentro de Power Pivot.

En la ventana de Power Pivot, aparecieron las tablas:

- **Transacciones** (278,431 filas, 42 columnas)
- **Clientes** (1,245 filas, 15 columnas)
- **Proveedores** (342 filas, 12 columnas)
- **Inversiones_Delta** (4,320 filas, 18 columnas)
- **Empresas_Nova** (23 filas, 8 columnas)

—El modelo tiene cinco tablas —explicó Valeria—. Pero están aisladas. Para que trabajen juntas, necesitamos crear **relaciones**.

### Creando relaciones

Valeria fue a la pestaña **Diseño > Crear relaciones**.

—En Power Pivot, las relaciones conectan tablas a través de columnas comunes. Se basan en el concepto de clave primaria y clave foránea de las bases de datos relacionales.

Creó las siguientes relaciones:

| Tabla origen | Columna origen | Tabla destino | Columna destino | Cardinalidad |
|--------------|----------------|---------------|-----------------|--------------|
| Transacciones | ID_Cliente | Clientes | ID_Cliente | Muchos a uno |
| Transacciones | ID_Proveedor | Proveedores | ID_Proveedor | Muchos a uno |
| Inversiones_Delta | ID_Empresa | Empresas_Nova | ID_Empresa | Muchos a uno |
| Transacciones | ID_Empresa | Empresas_Nova | ID_Empresa | Muchos a uno |

—Las relaciones permiten que las tablas dinámicas crucen información entre tablas. Por ejemplo, puedo poner el nombre del cliente (de la tabla Clientes) en una tabla dinámica que tenga montos de transacciones (de la tabla Transacciones), y Power Pivot navegará automáticamente por la relación.

### El diagrama del modelo

Valeria cambió a la vista **Diagrama** en Power Pivot.

—Este es el modelo de datos —dijo—. Cada rectángulo es una tabla. Las líneas entre ellos son las relaciones.

Sofía observó el diagrama. Las cinco tablas conectadas por líneas con flechas. Parecía un mapa de ruta.

—Es hermoso —dijo—. Como un plano arquitectónico, pero de datos.

—Exactamente. Y ahora podemos construir sobre esta base.

### Creando columnas calculadas

—Hay dos tipos de cálculos en Power Pivot: columnas calculadas y medidas.

Valeria creó una columna calculada en la tabla Transacciones:

—Una columna calculada es como una columna normal de Excel, pero usa el lenguaje DAX (Data Analysis Expressions). Se calcula fila por fila.

En la barra de fórmulas de Power Pivot, escribió:

```
=Transacciones[Monto] * 1.18
```

—Esto crea una columna llamada `CalculatedColumn1` con el monto más 18% de IGV. Pero el nombre no es descriptivo.

Renombró la columna a `Monto_Con_IGV`.

—Las columnas calculadas se almacenan en el modelo y ocupan memoria. Por eso, solo se usan cuando es necesario. Para cálculos dinámicos (como totales, promedios, etc.), usamos medidas.

### Creando medidas básicas

—Las medidas son cálculos que se evalúan en el contexto de una tabla dinámica. No se almacenan en memoria; se calculan en el momento.

En la cuadrícula de Power Pivot, Valeria seleccionó una celda vacía en la tabla Transacciones y escribió:

```
Total Ventas:=SUM(Transacciones[Monto])
```

—Esta medida suma todos los montos de la tabla Transacciones. Pero cuando la arrastres a una tabla dinámica y la combines con fechas o categorías, se recalculará automáticamente para cada contexto.

—¿Como una función SUBTOTALES? —preguntó Carlos.

—Más potente. SUBTOTALES respeta los filtros manuales, pero las medidas DAX pueden modificar el contexto de filtro programáticamente. Eso lo veremos en el próximo capítulo.

Valeria creó más medidas:

```
Cantidad Transacciones:=COUNTROWS(Transacciones)
Monto Promedio:=AVERAGE(Transacciones[Monto])
Monto Máximo:=MAX(Transacciones[Monto])
Monto Mínimo:=MIN(Transacciones[Monto])
```

—Con estas medidas, podemos construir un primer análisis exploratorio.

### La conexión peligrosa

Con las relaciones establecidas y las medidas creadas, Valeria insertó una tabla dinámica conectada al modelo de Power Pivot.

—Normalmente, las tablas dinámicas usan datos de una hoja de Excel. Pero si activamos **Esta tabla dinámica está conectada al modelo de datos**, podemos usar todas las tablas de Power Pivot.

En la tabla dinámica, puso:
- **Filas**: Empresas_Nova[Razón Social]
- **Filas**: Clientes[Tipo] (Persona Natural / Jurídica)
- **Valores**: Transacciones[Total Ventas]

La tabla mostró algo inesperado.

—Miren —dijo Valeria—. La mayoría de las transacciones de Nova son con personas naturales, no con empresas.

—¿Y eso es raro? —preguntó Carlos.

—Nova es un grupo inversor. Deberían trabajar con otras empresas, proveedores, contratistas. Pero el 78% de sus transacciones son con personas naturales.

—Gente común —dijo Sofía—. Como las que usan para lavar dinero.

—Exactamente. Y aquí está el verdadero hallazgo.

Valeria agregó la tabla Inversiones_Delta a la mezcla, creando una relación indirecta a través de Empresas_Nova.

—Power Pivot puede navegar relaciones de múltiples pasos. Es lo que se llama "relaciones activas". Puedo ir de Transacciones a Empresas_Nova, y de ahí a Inversiones_Delta.

Creó una nueva medida:

```
Inversiones Delta Vinculadas:=SUM(Inversiones_Delta[Monto_Total])
```

La tabla dinámica ahora mostraba:

| Razón Social | Total Ventas | Inversiones Delta Vinculadas |
|-------------|-------------|------------------------------|
| Taller Mendoza & Hijos | S/ 0 | S/ 0 |
| Lavandería El Sol | S/ 340,210 | S/ 1,200,000 |
| Restaurante La Marina | S/ 520,430 | S/ 3,400,000 |
| Ferretería Los Andes | S/ 210,845 | S/ 890,000 |
| Taller Mecánico Rápido | S/ 180,320 | S/ 2,100,000 |

—¿Ven el patrón? —dijo Valeria—. Las empresas compradas por Nova tienen ingresos modestos (todos menores a S/ 600,000 al año), pero reciben inversiones de Delta que son hasta 10 veces sus ingresos reales.

—El dinero sucio entra a través de Delta como "inversión", se mezcla con las ganancias legítimas del negocio, y luego se reporta como ingreso. —Sofía sintió un nudo en el estómago.

—Y nosotros seríamos la próxima lavandería —dijo Carlos en voz baja.

—No si lo demostramos primero —respondió Valeria—. Pero necesito más medidas. Medidas más complejas. Necesito DAX avanzado.

---

## Explicación técnica: Power Pivot

### ¿Qué es Power Pivot?

Power Pivot es un motor de análisis de datos en memoria que permite manejar millones de filas de datos dentro de Excel. Utiliza el motor **VertiPaq** (xVelocity) que comprime datos y realiza cálculos a alta velocidad.

### ¿Cómo habilitar Power Pivot?

En Excel:
1. **Archivo > Opciones > Complementos**
2. En el menú **Administrar**, seleccionar **Complementos COM**
3. Marcar **Microsoft Power Pivot for Excel**

En la cinta de opciones aparecerá una pestaña **Power Pivot**.

### Tablas vs. Hojas de Excel

| Característica | Hoja de Excel | Power Pivot |
|---------------|---------------|-------------|
| Límite de filas | 1,048,576 | 2 mil millones |
| Almacenamiento | En disco (archivo) | En memoria RAM |
| Compresión | Mínima | Máxima (promedio 10:1) |
| Velocidad de cálculo | Depende de CPU | En memoria (ultrarrápido) |
| Relaciones entre tablas | Limitadas (3D) | Ilimitadas |
| Columnas calculadas | Fórmulas de Excel | Fórmulas DAX |

### Tablas y columnas

En Power Pivot:
- **Tabla**: Conjunto de datos con estructura de columnas y filas
- **Columna**: Campo individual con un tipo de datos específico
- **Fila**: Registro individual (no visible como en Excel, sino como datos)

### Relaciones en Power Pivot

Una **relación** conecta dos tablas a través de una columna común. Componentes:

| Componente | Descripción |
|------------|-------------|
| Tabla origen | Tabla del lado "muchos" (foreing key) |
| Columna origen | Columna en la tabla origen que referencia a la destino |
| Tabla destino | Tabla del lado "uno" (primary key) |
| Columna destino | Columna única en la tabla destino |
| Cardinalidad | Muchos a uno / Uno a muchos / Uno a uno / Muchos a muchos |

### Columnas calculadas vs. Medidas

| Característica | Columna calculada | Medida |
|----------------|-------------------|--------|
| Cuándo se calcula | Al cargar datos | Al consultar (en tiempo real) |
| Dónde se almacena | En memoria | No se almacena |
| Contexto | Fila por fila | Contexto de filtro actual |
| Uso en tablas dinámicas | Como fila/columna | Como valor |
| Sintaxis | =Expresión | Nombre Medida:=Expresión |

### Vistas en Power Pivot

Power Pivot tiene dos vistas principales:

1. **Vista de datos**: Muestra las tablas como cuadrículas de datos (similar a hoja Excel)
2. **Vista de diagrama**: Muestra las tablas como rectángulos conectados por líneas de relación

### Buenas prácticas

1. **Crear una tabla de calendario**: Para análisis temporales (días, meses, años)
2. **Usar nombres descriptivos**: Tablas, columnas y medidas con nombres claros
3. **Documentar medidas**: Usar la función de descripción en Power Pivot
4. **Normalizar adecuadamente**: Dividir datos en tablas relacionadas, no todo en una mega-tabla
5. **Verificar la cardinalidad**: Asegurarse de que las relaciones sean correctas (1:M vs M:M)

---

### Enigma 2.1: Construir un modelo de datos

Tienes cuatro archivos:

1. `Pedidos.xlsx` — 50,000 filas con: ID_Pedido, Fecha, ID_Cliente, ID_Producto, Cantidad, Precio_Unitario
2. `Clientes.xlsx` — 500 filas con: ID_Cliente, Nombre, Ciudad, Segmento
3. `Productos.xlsx` — 200 filas con: ID_Producto, Nombre_Producto, Categoría, Precio_Lista
4. `Categorías.xlsx` — 10 filas con: ID_Categoría, Nombre_Categoría, Departamento

¿Qué relaciones crearías? Dibuja el diagrama del modelo de datos, indicando tablas, columnas clave y cardinalidad.

### Enigma 2.2: Medidas exploratorias

Dado el modelo del ejercicio anterior, crea las siguientes medidas en DAX:

1. `Total Ventas` — Suma de (Cantidad * Precio_Unitario)
2. `Cantidad Pedidos` — Conteo de pedidos
3. `Ticket Promedio` — Total Ventas / Cantidad Pedidos
4. `Productos Vendidos` — Suma de Cantidad
5. `Precio Promedio` — Precio promedio ponderado

### Enigma 2.3: Análisis de relación

Usando el modelo de datos, determina:
1. ¿Qué cliente ha generado más ingresos?
2. ¿Qué categoría de producto tiene el ticket promedio más alto?
3. ¿Hay una correlación entre el segmento del cliente y la frecuencia de compra?

Describe qué relaciones y medidas usarías para responder cada pregunta.

*(Soluciones en el Apéndice)*
