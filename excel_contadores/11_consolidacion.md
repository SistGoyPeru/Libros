# Capítulo 7: Consolidación de Estados Financieros

## Juntando las piezas

—La consolidación —dijo Don Alberto— es el rompecabezas contable por excelencia. Tienes datos de varias empresas, sucursales o departamentos, y necesitas unirlos en un solo informe coherente.

### La Historia

—Don Alberto —dijo María—, "Importaciones del Sur" tiene 3 sucursales (Lima, Arequipa, Trujillo) y cada una manda su estado de resultados en formatos diferentes. Necesito consolidarlos para la junta de accionistas de mañana.

—Formatos diferentes —repitió Don Alberto—. El clásico problema de la consolidación.

### Consolidación por categorías

—La forma más sencilla —dijo Don Alberto— es cuando todas las sucursales usan las mismas categorías pero en diferente orden.

```
Datos > Consolidar
Función: Suma
Referencia: Seleccionar rango de cada sucursal
Usar etiquetas en: [x] Fila superior, [x] Columna izquierda
Crear vínculos con datos de origen: [x]
```

—Pero —advirtió—, esto solo funciona si las categorías se llaman exactamente igual en todas las sucursales.

### Consolidación con Power Query

—Power Query —dijo Don Alberto— es la herramienta definitiva para consolidar.

```
Datos > Obtener datos > Desde otras fuentes > Consulta en blanco
Editor Power Query > Inicio > Combinar > Combinar consultas > Anexar
```

**Pasos para consolidar múltiples archivos:**

1. Crear una carpeta con todos los archivos a consolidar
2. `Datos > Obtener datos > Desde archivo > Desde carpeta`
3. Power Query detecta automáticamente todos los archivos
4. Combinar archivos > Elegir la hoja o tabla
5. Transformar datos si es necesario
6. Cerrar y cargar

—Esto —dijo Don Alberto— consolida cualquier cantidad de archivos automáticamente. Cuando agregues un nuevo archivo a la carpeta, solo actualizas la consulta.

### Consolidación con fórmulas

—A veces —dijo Don Alberto— la consolidación es simple y las fórmulas bastan.

**Referencia 3D (misma celda en varias hojas):**
```
=SUMA(Arequipa: Trujillo!B5)
```

—Esto suma la celda B5 de todas las hojas entre Arequipa y Trujillo.

**Referencia indirecta para consolidación flexible:**
```
=INDIRECTO(A2 & "!B5")
```
—Donde A2 contiene el nombre de la hoja.

### Eliminación de transacciones intercompañía

—En contabilidad —dijo Don Alberto—, al consolidar empresas del mismo grupo, debes eliminar las transacciones entre ellas.

**Tabla de transacciones intercompañía:**

| Fecha | Empresa Origen | Empresa Destino | Monto |
|-------|---------------|-----------------|-------|
| 15/01 | Lima | Arequipa | 5,000 |
| 20/02 | Trujillo | Lima | 3,000 |

**Fórmula para eliminación:**
```
=VentasConsolidadas - SUMAR.SI.CONJUNTO(
    tblIntercompania[Monto],
    tblIntercompania[Origen], "Lima",
    tblIntercompania[Destino], "Arequipa"
)
```

### Conversión de moneda en consolidación

—¿Y si las sucursales usan diferentes monedas? —preguntó María.

—Ahí entra la conversión —dijo Don Alberto—. Creamos una tabla de tipo de cambio:

```
Tabla: tblTipoCambio
Fecha | USD | EUR
01/01 | 3.75 | 4.10
...
```

**Conversión con BUSCARX:**
```
=BUSCARX(A2, tblTipoCambio[Fecha], tblTipoCambio[USD], "No TC", -1)
```

**Columnas de moneda local y moneda funcional:**
```
Monto S/ = Monto USD * TipoCambio
```

### Consolidación de balances

—El balance general es la consolidación más delicada —dijo Don Alberto—. Debes considerar:

1. **Inversiones en subsidiarias:** la participación de la matriz se elimina
2. **Interés minoritario:** la parte que no pertenece a la matriz
3. **Plusvalía mercantil:** si se pagó más que el valor en libros

**Estructura típica para consolidación de balance:**

```
Activo Consolidado = Activo Matriz + Activo Subsidiaria - 
                     Participación Matriz + Plusvalía
Pasivo Consolidado = Pasivo Matriz + Pasivo Subsidiaria
Patrimonio Consolidado = Patrimonio Matriz + Interés Minoritario
```

### Plantilla de consolidación automática

María construyó una plantilla con Don Alberto:

1. **Hoja de entrada:** cada sucursal pega sus datos
2. **Hoja de conversión:** se aplica tipo de cambio correspondiente
3. **Hoja de eliminaciones:** se registran transacciones intercompañía
4. **Hoja de consolidación:** fórmulas SUMAR.SI.CONJUNTO agregan todo
5. **Hoja de informe:** estado de resultados y balance consolidados

### Resumen del capítulo

| Método | Cuándo usarlo |
|--------|--------------|
| Consolidar (menú) | Datos homogéneos, pocas fuentes |
| Power Query | Muchos archivos, formatos variables |
| Fórmulas 3D | Mismo libro, estructura idéntica |
| INDIRECTO | Consolidación dinámica |
| BUSCARX + TC | Conversión de moneda |
| SUMAR.SI.CONJUNTO | Eliminar intercompañía |

### Enigma contable #7

En `codigos/07_consolidacion/` encontrarás 3 archivos: `lima.xlsx`, `arequipa.xlsx` y `trujillo.xlsx`, cada uno con el estado de resultados mensual de cada sucursal.

**Tu misión:**
1. Consolida los 3 archivos en un solo estado de resultados usando Power Query
2. Convierte las sucursales que están en USD a S/ (tipo de cambio: 3.75)
3. Elimina las transacciones intercompañía registradas en `intercompania.xlsx`
4. Calcula la utilidad consolidada por mes
5. Genera un gráfico comparativo: cada sucursal como una línea, meses en el eje X

*El resultado debe ser un informe listo para presentar a la junta de accionistas.*