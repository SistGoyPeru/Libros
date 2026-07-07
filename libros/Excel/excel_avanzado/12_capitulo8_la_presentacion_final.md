
# Capítulo 8: La Presentación Final

## Integración Power BI, Publicación y Colaboración

Faltaban 3 días. El dashboard en Excel era impresionante, pero Valeria sabía que necesitaban más.

—La UIF no va a revisar un archivo de Excel —dijo—. Necesitan algo más visual, más interactivo, más profesional. Necesitan Power BI.

—¿Power BI es diferente de Power Pivot? —preguntó Carlos.

—Power Pivot es el motor dentro de Excel. Power BI Desktop es una aplicación independiente que usa el mismo motor pero con mejores visualizaciones, capacidades de publicación en la nube y colaboración en equipo.

### Exportando el modelo a Power BI

Valeria abrió Power BI Desktop (descargable gratis desde Microsoft Store).

—Power BI Desktop puede conectarse a Excel y usar el modelo de Power Pivot directamente.

Hizo clic en **Inicio > Obtener datos > Excel** y seleccionó el archivo del taller.

—Power BI detecta automáticamente el modelo de datos: tablas, relaciones, medidas, columnas calculadas. Todo se importa tal cual.

En la pestaña **Modelo**, Valeria verificó que las relaciones estuvieran correctas:

```
[Transacciones] --ID_Cliente--> [Clientes]
[Transacciones] --ID_Proveedor--> [Proveedores]
[Transacciones] --ID_Empresa--> [Empresas_Nova]
[Inversiones_Delta] --ID_Empresa--> [Empresas_Nova]
```

—El modelo es exactamente el mismo que en Power Pivot. Power BI lo reconoce y lo usa nativamente.

### Visualizaciones impactantes

—Ahora viene la parte divertida —dijo Valeria—. Power BI tiene visualizaciones que Excel no puede igualar.

Creó las siguientes visualizaciones:

**1. Mapa de calor de transacciones por distrito:**
—Usó un mapa de árbol (Treemap) con distritos como categorías y monto total como valor. Las zonas más oscuras eran los distritos con más transacciones sospechosas.

**2. Gráfico de cascada (Waterfall):**
—Mostraba cómo se acumulaban las transacciones sospechosas mes a mes. Cada barra era un mes, y la línea de conexión mostraba el incremento o decremento.

**3. Indicador de múltiples tarjetas (Multi-row card):**
—Mostraba los KPIs principales: Total Sistema, Empresas Vinculadas, Alertas Activas.

**4. Gráfico de dispersión (Scatter):**
—Cada punto era una transacción. Eje X: fecha, Eje Y: monto, Tamaño: frecuencia. Las transacciones sospechosas aparecían como un cúmulo alrededor de los S/ 24,000.

**5. Matriz con formato condicional:**
—Tabla dinámica similar a Excel pero con barras de datos y escala de colores integradas.

—Cada visualización es interactiva —dijo Valeria—. Si selecciono un punto en el scatter, todas las demás visualizaciones se filtran para mostrar solo ese contexto.

### Power Query en Power BI vs Excel

—Power Query en Power BI es casi idéntico al de Excel —dijo Valeria—. De hecho, el lenguaje M es el mismo. La diferencia principal es que en Power BI está más integrado con el flujo de trabajo.

Valeria abrió el Editor de Power Query en Power BI:

—Aquí podemos hacer exactamente las mismas transformaciones que en Excel. Pero Power BI está diseñado para manejar volúmenes mayores y actualizaciones programadas.

—¿Actualizaciones programadas? —preguntó Sofía.

—Cuando publicamos este informe en el servicio de Power BI (nube), podemos configurar que los datos se actualicen automáticamente cada día, cada hora, o incluso cada 15 minutos. No necesitamos abrir el archivo manualmente.

### Publicación en la nube

Valeria hizo clic en **Publicar** y seleccionó el espacio de trabajo de la UIF.

—Power BI Publicar sube el informe al servicio en la nube. Desde ahí, podemos compartirlo con quien queramos.

El informe apareció en https://app.powerbi.com:

—Desde aquí, la UIF puede ver el informe desde cualquier navegador, incluso desde un iPad. No necesitan tener Power BI Desktop ni Excel instalado.

—¿Y los datos sensibles? —preguntó Carlos.

—Power BI tiene seguridad a nivel de fila (RLS). Podemos definir roles y reglas para que cada usuario solo vea los datos que debe ver.

Valeria configuró RLS:

```
-- Rol: Investigador UIF
[Transacciones] = FILTER(Transacciones, Transacciones[Monto] > 20000)

-- Rol: Administrador
-- Ve todas las transacciones sin filtro
```

—Los investigadores solo verán transacciones mayores a 20,000. El administrador ve todo.

### Compartiendo con las autoridades

—Y ahora, lo más importante —dijo Valeria—. Compartir el informe con la UIF y la Fiscalía.

En el servicio de Power BI:

1. Hizo clic en **Compartir**
2. Ingresó los correos de los fiscales
3. Activó la opción **Permitir a los destinatarios compartir este informe**
4. Agregó un mensaje: "Evidencia del caso Nova — Lavado de dinero — Urgente"

—En segundos, los fiscales tienen acceso al informe completo. Pueden explorarlo, filtrarlo, exportarlo a PDF o PowerPoint.

—¿Y si quieren hacer cambios? —preguntó Sofía.

—Power BI tiene control de versiones. Cada cambio queda registrado. Y si alguien modifica el informe, el original siempre está respaldado.

### El flujo completo

Valeria mostró el flujo completo de trabajo:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  FUENTES        │    │  POWER BI        │    │  PUBLICACIÓN    │
│  DE DATOS       │    │  DESKTOP         │    │                 │
│                 │    │                  │    │                 │
│ CSV bancarios   │───>│ Power Query      │───>│ Servicio Power  │
│ PDF facturas    │───>│ (Transformar)    │    │ BI (Nube)       │
│ Web SUNAT       │───>│                  │    │                 │
│ Base Access     │───>│ Power Pivot      │    │ Compartir con   │
│                 │    │ (Modelar)        │    │ UIF y Fiscalía  │
│ Excel local     │───>│                  │    │                 │
│                 │    │ DAX (Medidas)    │    │ Actualización   │
│                 │    │                  │    │ automática      │
│                 │    │ Power BI Vis     │    │                 │
│                 │    │ (Visualizar)     │    │ Seguridad RLS   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

—En tres semanas, construimos un sistema completo de inteligencia financiera —dijo Valeria—. Desde la extracción de datos hasta la presentación ante autoridades.

—Y todo empezó con Excel —dijo Sofía—. Power Query, Power Pivot, DAX, VBA, matrices dinámicas... y ahora Power BI.

—Excel es el punto de partida —dijo Valeria—. Power BI es la evolución natural. Pero el conocimiento es transferible. Las medidas DAX funcionan igual. Power Query es el mismo. El pensamiento analítico es el mismo.

—Mañana presentamos esto ante la UIF —dijo Sofía—. ¿Estamos listos?

Valeria sonrió. —Casi. Antes de presentar cualquier cosa como evidencia, necesitamos asegurarnos de que sea perfecta. Necesitamos auditar el modelo.

---

## Explicación técnica: Integración Power BI

### ¿Qué es Power BI?

Power BI es una suite de herramientas de business intelligence de Microsoft que permite conectar, modelar, visualizar y compartir datos. Componentes principales:

- **Power BI Desktop**: Aplicación gratuita para crear informes
- **Power BI Service**: Plataforma en la nube para compartir y colaborar
- **Power BI Mobile**: Apps para iOS, Android y Windows Phone
- **Power BI Report Builder**: Para informes paginados

### Power Query: Excel vs Power BI

| Característica | Excel | Power BI |
|---------------|-------|----------|
| Editor | Integrado en Power Pivot | Independiente |
| Límite de datos | 2GB archivo | Ilimitado (depende de plan) |
| Actualización programada | Limitada | Completa |
| Fuentes de datos | Más limitado | 150+ conectores |
| Lenguaje M | Mismo | Mismo |
| Pasos aplicados | Sí | Sí |

### DAX: Excel vs Power BI

Las medidas DAX escritas en Power Pivot se pueden copiar directamente a Power BI (y viceversa). La sintaxis y funciones son idénticas.

### Visualizaciones en Power BI

Power BI tiene visualizaciones nativas y un marketplace con cientos de visualizaciones personalizadas:

| Visualización | Uso recomendado |
|---------------|-----------------|
| Gráfico de barras | Comparar categorías |
| Gráfico de líneas | Mostrar tendencias en el tiempo |
| Mapa | Datos geográficos |
| Mapa de árbol (Treemap) | Jerarquías y proporciones |
| Cascada (Waterfall) | Cambios secuenciales |
| Embudo (Funnel) | Procesos con etapas |
| Medidor (Gauge) | KPIs con objetivos |
| Matriz | Tablas dinámicas con formato |
| Tarjeta (Card) | Valor único destacado |
| Dispersión (Scatter) | Correlaciones |
| Narrativa inteligente | Resúmenes automáticos en lenguaje natural |

### Publicación y colaboración

| Método | Descripción | Requisito |
|--------|-------------|-----------|
| Publicar en servicio | Sube informe a nube | Licencia Pro (usuario) |
| Compartir dashboard | Permite acceso a otros | Licencia Pro (creador) |
| Incrustar en web | Informe público | Licencia Premium |
| Exportar a PDF | Imagen estática | Gratuito |
| Exportar a PowerPoint | Presentación | Gratuito |
| Suscripciones por correo | Informe enviado automáticamente | Licencia Pro |

### Seguridad a nivel de fila (RLS)

Permite controlar qué datos ve cada usuario según su rol.

```dax
-- Rol: Regional
[Ventas Regional] = FILTER(Ventas, Ventas[Región] = USERPRINCIPALNAME())
```

---

### Enigma 8.1: Migrar modelo a Power BI

Describe los pasos para migrar un modelo de Power Pivot de Excel a Power BI Desktop. ¿Qué elementos se conservan? ¿Qué se pierde en la migración?

### Enigma 8.2: Visualizaciones para cada tipo de análisis

Relaciona cada tipo de análisis con la visualización de Power BI más adecuada:

1. Evolución de ventas en 12 meses → ?
2. Comparación de ventas por región → ?
3. Proporción del presupuesto por departamento → ?
4. Relación entre precio y cantidad vendida → ?
5. Progreso hacia un objetivo de ventas → ?
6. Cambio acumulado mes a mes → ?

### Enigma 8.3: RLS para el caso forense

Diseña un esquema de seguridad a nivel de fila para el informe de Nova con estos roles:

- **Fiscal Jefe**: Ve todos los datos, incluyendo fuentes confidenciales
- **Investigador**: Ve transacciones > 20,000, no ve fuentes confidenciales
- **Auditor Externo**: Solo ve datos de empresas adquiridas, no de empresas fantasma

Escribe las reglas DAX para cada rol.

*(Soluciones en el Apéndice)*
