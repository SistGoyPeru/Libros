
# Capítulo 10: Justicia y Nuevos Comienzos

## Proyecto Integrador Final

El día 30. La cita en la UIF era a las 10:00 a.m.

Sofía se levantó a las 5:00 a.m. No había dormido bien. En su mochila llevaba:
- El archivo de Excel con el modelo completo (45 MB)
- El informe de Power BI publicado en la nube
- Los PDFs impresos del dashboard
- Una carta con el resumen ejecutivo
- Una unidad USB con todo respaldado

Carlos la esperaba en la puerta del taller, con el uniforme de trabajo pero los ojos vidriosos.

—¿Estás lista, prima?

—Nunca lo estaré —respondió Sofía—. Pero vamos igual.

Valeria llegó en su auto, una laptop en el asiento del copiloto.

—Suban —dijo—. La UIF nos espera.

### La presentación

La oficina del Dr. Ricardo Paredes estaba en el piso 12 de un edificio en San Isidro. Mesas de vidrio, pantallas grandes, olor a café recién hecho.

Además del Dr. Paredes, había tres personas: dos analistas de la UIF y un fiscal especializado en lavado de activos.

—Señorita Mendoza —dijo el Dr. Paredes—, tiene 30 minutos. Le sugiero que vaya directo al grano.

Sofía tomó un respiro profundo. Recordó las palabras de su abuelo Don Rafael: "Cuando tengas los números de tu lado, no necesitas tener miedo."

—Señores —comenzó—, esto es lo que descubrimos en los últimos 30 días.

Conectó su laptop a la pantalla grande y abrió el dashboard.

### El flujo de la presentación

**Paso 1: Los datos**

—Todo empezó con los datos sin procesar. Usamos Power Query para importar y limpiar 278,431 transacciones de múltiples fuentes: bancos, SUNAT, facturación electrónica, registros contables.

En la pantalla, mostró el proceso de Power Query: las conexiones, los pasos aplicados, la limpieza de datos.

—Cada paso está documentado. Cada transformación es reproducible. Los datos originales no fueron modificados —dijo Valeria, apoyando la explicación.

**Paso 2: El modelo**

—Luego construimos un modelo de datos en Power Pivot —continuó Sofía—. Cinco tablas relacionadas: Transacciones, Clientes, Proveedores, Empresas Nova e Inversiones Delta.

Mostró el diagrama del modelo en Power Pivot.

—Las relaciones están validadas. No hay relaciones huérfanas ni inconsistencias.

**Paso 3: Las medidas DAX**

—Aquí está el corazón del análisis —dijo Sofía, mostrando la lista de medidas DAX.

Proyectó las medidas clave:

```
Total Sistema:=SUM(Transacciones[Monto])
Transacciones Sospechosas:=SUMX(Transacciones, IF(Transacciones[Monto]>=20000 && Transacciones[Origen]="Delta", Transacciones[Monto], 0))
% Estructuración:=DIVIDE([Transacciones Fraccionadas], [Cantidad Transacciones], 0)
```

—Cada medida fue probada contra datos conocidos. Los resultados coinciden.

**Paso 4: Las evidencias**

—Y esto es lo que las medidas revelaron.

Mostró la tabla con los resultados:

| Indicador | Valor |
|-----------|-------|
| Total de transacciones analizadas | 278,431 |
| Monto total en transacciones sospechosas | S/ 11,672,000 |
| Transacciones justo debajo de S/ 25,000 | 287 |
| Empresas vinculadas a la red | 23 |
| Empresas fantasma (sin ingresos reales) | 2 |
| Nuestro taller | Objetivo de adquisición |

—Las 287 transacciones fraccionadas son estructuración pura —dijo Valeria—. Cada una está diseñada para estar justo debajo del límite de reporte.

—¿Pueden demostrar que es intencional? —preguntó el fiscal.

Sofía sonrió. —Sí. Con análisis de patrones.

Mostró el gráfico de dispersión de Power BI:

—Las transacciones de Delta se acumulan sistemáticamente entre S/ 20,000 y S/ 24,999. Mientras que las transacciones legítimas tienen una distribución normal. La probabilidad de que esta concentración sea aleatoria es menor al 0.01%.

**Paso 5: El valor del taller**

—Finalmente, para demostrar que la oferta de Nova era parte del esquema, usamos Solver y análisis de escenarios.

Sofía mostró los resultados de la optimización:

—El taller vale, incluso en el escenario más pesimista, S/ 1,900,000. La oferta de Nova ($850,000) representa menos del 30% de ese valor. No es una oferta. Es un vehículo para lavar dinero a través de una empresa infravalorada.

### El momento de la verdad

El Dr. Paredes se levantó y caminó hacia la pantalla. Señaló la tabla de transacciones sospechosas.

—Esto es impresionante —dijo—. Pero necesito preguntar: ¿cuál es la garantía de que estos datos no han sido manipulados?

Valeria se adelantó. —Cada cambio en el archivo fue registrado. Tenemos un log de auditoría VBA con fecha, usuario, celda modificada y valores anterior y nuevo.

Mostró la hoja AuditLog:

| Fecha | Usuario | Hoja | Celda | Anterior | Nuevo |
|-------|---------|------|-------|----------|-------|
| 15/01 16:30 | VRIVAS | PowerPivot | Medida DAX | — | Total Sistema |
| 16/01 09:15 | SMENDOZA | Dashboard | Filtro mes | — | Enero |
| ... | ... | ... | ... | ... | ... |

—Además —continuó Valeria—, el archivo tiene firma digital. Cualquier modificación posterior invalidaría la firma.

El fiscal asintió lentamente.

—Esto es más de lo que esperábamos —dijo—. Mucho más. Con esto, podemos obtener una orden de allanamiento para las oficinas de Nova y una orden de congelamiento de cuentas para Inversiones Delta.

Sofía sintió que el aire volvía a sus pulmones.

—¿Entonces...?

—Entonces —dijo el Dr. Paredes—, usted acaba de salvar su taller y destapar una red de lavado de dinero que investigábamos desde hace un año. Todo con Excel.

—No solo Excel —corrigió Sofía—. Power Query, Power Pivot, DAX, VBA, matrices dinámicas, Solver y Power BI.

El Dr. Paredes sonrió por primera vez. —Excel avanzado, entonces.

### Dos meses después...

El taller "Mendoza & Hijos" había duplicado su producción. Nova fue desmantelada. Inversiones Delta congelada. Siete personas arrestadas.

Sofía estaba en su oficina, revisando los nuevos pedidos, cuando sonó el teléfono.

—¿Sofía Mendoza?

—Sí.

—Habla el Dr. Paredes, de la UIF. Tengo una oferta que quizá le interese. Necesitamos un analista de datos forenses. Con experiencia en lavado de dinero. Y con habilidades excepcionales en Excel.

Sofía se recostó en su silla. Miró el certificado de "Excel Avanzado" enmarcado en la pared, junto a la foto de su abuelo Don Rafael.

—¿Es tiempo completo? —preguntó.

—Podemos negociar.

—Acepto —dijo—. Con una condición: puedo seguir manejando el taller desde casa.

—Trato hecho.

Colgó y sonrió. Su abuelo siempre dijo que los números tenían poder. Pero ella había descubierto algo más importante: **el poder no está en los números, sino en quien sabe analizarlos**.

---

## Explicación técnica: Proyecto Integrador

### Arquitectura de solución completa

El caso de Sofía demuestra la arquitectura completa de una solución de análisis de datos con Excel moderno:

```
┌─────────────┐    ┌───────────────┐    ┌─────────────┐
│ ADQUISICIÓN │    │  MODELADO     │    │ ANÁLISIS    │
│             │    │               │    │             │
│ Power Query │───>│ Power Pivot   │───>│ DAX Medidas │
│   - CSV     │    │   - Tablas    │    │   - SUMX    │
│   - PDF     │    │   - Relaciones│    │   - CALC    │
│   - Web     │    │   - Columnas  │    │   - FILTER  │
│   - DB      │    │               │    │   - ALL     │
└─────────────┘    └───────────────┘    └──────┬──────┘
                                               │
                        ┌──────────────────────┼──────────┐
                        ▼                      ▼          ▼
                  ┌───────────┐          ┌──────────┐ ┌──────┐
                  │ AUTOMAT.  │          │ VISUAL.  │ │ OPT. │
                  │           │          │          │ │      │
                  │ VBA       │          │ Dashboard│ │Solver│
                  │  - Macros │          │  - KPIs  │ │Escen.│
                  │  - UDFs   │          │  - Power │ │      │
                  │  - Logs   │          │    View  │ │      │
                  └───────────┘          └──────────┘ └──────┘
                                               │
                                          ┌────┴────┐
                                          │ POWER BI│
                                          │ - Pub.  │
                                          │ - RLS   │
                                          │ - Cloud │
                                          └─────────┘
```

### Habilidades cubiertas en el viaje de Sofía

| Herramienta | Capítulo | Uso en el caso |
|-------------|----------|----------------|
| Power Query | 1 | Importar y limpiar 278K transacciones |
| Power Pivot | 2 | Modelo relacional con 5 tablas |
| DAX | 3 | Medidas de análisis forense |
| VBA | 4 | Automatización de informes semanales |
| Matrices dinámicas/LAMBDA | 5 | Análisis ad-hoc en la hoja |
| Solver/Escenarios | 6 | Valoración real del taller |
| Dashboard | 7 | Panel de control interactivo |
| Power BI | 8 | Publicación y colaboración |
| Auditoría/Seguridad | 9 | Validación y protección forense |

### Reflexión final

Excel avanzado no es solo saber muchas funciones. Es saber **cuándo** usar cada herramienta y **cómo** combinarlas para resolver problemas complejos.

El caso de Nova requería:
1. Volumen: 278,431 transacciones → Power Query + Power Pivot
2. Relaciones: 5 tablas interconectadas → Power Pivot
3. Cálculos complejos: Estructuración, patrones → DAX
4. Automatización: Informes semanales → VBA
5. Flexibilidad: Análisis rápidos → Matrices dinámicas + LAMBDA
6. Optimización: Valor del negocio → Solver
7. Visualización: Comunicar hallazgos → Dashboard + Power BI
8. Integridad: Evidencia admisible → Auditoría + Seguridad

Cada herramienta en su lugar. Cada una potenciando a las demás.

---

### Enigma 10.1: Tu propio proyecto integrador

Diseña un proyecto integrador para tu trabajo o negocio que use al menos 4 de las herramientas aprendidas. Describe:

1. El problema a resolver
2. Las fuentes de datos
3. El modelo de datos (tablas y relaciones)
4. Las medidas clave (DAX)
5. La automatización necesaria (VBA o LAMBDA)
6. Las visualizaciones (dashboard/Power BI)
7. Las medidas de seguridad y validación

### Enigma 10.2: El caso Sofía — Tú eres el analista

Eres contratado por la UIF para dar continuidad al caso Nova. Ahora necesitas:

1. Automatizar la detección de nuevas transacciones sospechosas (los datos de Delta se actualizan semanalmente)
2. Crear alertas automáticas cuando se detecte un patrón de estructuración
3. Generar un informe semanal para el fiscal
4. Mantener un histórico de todas las alertas generadas

Escribe el plan de implementación usando las herramientas aprendidas.

### Enigma 10.3: Proyección de carrera

Basado en lo aprendido en el libro, describe tu plan de aprendizaje para los próximos 6 meses:

- ¿Qué herramientas de Excel avanzado dominarás primero?
- ¿Qué recursos usarás (documentación, cursos, comunidades)?
- ¿Qué proyecto real construirás para demostrar tus habilidades?
- ¿Cómo medirás tu progreso?

*(Soluciones —o más bien, guías— en el Apéndice)*
