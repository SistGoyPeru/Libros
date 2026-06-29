# Capítulo 1: Configuración de Excel para Contabilidad

## El escritorio de un contador digital

—Lo primero —dijo Don Alberto— es configurar Excel como un contador. No como un ingeniero ni como un estadístico. Como un contador.

María observaba la pantalla.

—Mira —continuó Don Alberto—. La mayoría de la gente abre Excel y empieza a escribir. Nosotros no. Nosotros preparamos el terreno.

### La Historia

Eran las 8:30 a.m. cuando Don Alberto llegó al estudio con una taza de café en una mano y un cuaderno antiguo en la otra.

—Buenos días, Don Alberto —dijo el recepcionista.

—Buenos días, joven. ¿Ya llegó María?

—Sí, está en su escritorio.

Don Alberto caminó hacia el cubículo de María. La encontró mirando una hoja de Excel con los ojos entrecerrados.

—Problemas, ¿eh?

—No entiendo por qué estos números no suman bien —dijo María—. Son dólares, pero Excel está haciendo algo raro.

Don Alberto se rió suavemente.

—Excel no hace "cosas raras". Excel hace exactamente lo que le decimos. El problema es que a veces no sabemos cómo hablarle.

### Configuración básica

Don Alberto se sentó y comenzó a navegar por los menús.

**Archivo > Opciones > Avanzadas**

—Primero —dijo—, configuramos la precisión de visualización. En contabilidad trabajamos con centavos, no con infinitos decimales.

```
Opciones > Avanzadas > Al calcular este libro:
  - [x] Establecer precisión de visualización
  - [x] Usar sistema de fechas 1904 (para compatibilidad con Mac)
```

**Archivo > Opciones > Fórmulas**

—Aquí está el corazón de todo:

```
Opciones de cálculo:
  - Libro: Automático (pero conoce F9 para recalcular manual)
  - [x] Habilitar cálculo iterativo
  - Iteraciones máximas: 100
  - Cambio máximo: 0.001
```

—El cálculo iterativo es clave en contabilidad —explicó Don Alberto—. Porque a veces tienes referencias circulares controladas, como cuando calculas intereses que dependen del saldo final, y el saldo final depende de los intereses.

### Formatos contables

—Ahora —dijo Don Alberto—, los formatos.

**Formatos de número para contabilidad**

María tomó notas mientras Don Alberto explicaba:

1. **Formato Contable**: Diferente del formato moneda. El contable alinea los símbolos monetarios a la izquierda y los números a la derecha. Los valores negativos aparecen entre paréntesis.

   ```
   Formato > Contabilidad
   Símbolo: S/ (o $)
   Decimales: 2
   ```

2. **Formato personalizado para estados financieros**:
   ```
   #,##0.00 ;(#,##0.00);"-"
   ```
   —Este formato —explicó Don Alberto— muestra los positivos normales, los negativos entre paréntesis, y los ceros como un guión. Es el estándar contable.

3. **Formato de fecha fiscal**:
   ```
   dd-mmm-aaaa
   ```
   —Para períodos contables. O también:
   ```
   "Período "mmm-aa
   ```

### Temas y colores para contadores

Don Alberto abrió **Diseño de página > Colores**.

—Los contadores necesitamos claridad. Nada de fondos oscuros o colores llamativos.

```
Tema: Office
Colores: Office (o Grises para impresión)
Fuente: Calibri 10 (estándar contable)
```

—Y algo importante —añadió—: las líneas de cuadrícula. En contabilidad, las líneas nos ayudan a leer tablas de números.

```
Ver > [x] Líneas de cuadrícula
```

### Barra de acceso rápido personalizada

—Voy a configurar una barra de acceso rápido que todo contador debería tener:

```
Personalizar barra de herramientas de acceso rápido:
  - Vista previa de impresión
  - Bordes
  - Combinar y centrar
  - Formato de números contables
  - Quitar duplicados
  - Texto en columnas
  - Inmovilizar paneles
  - Proteger hoja
```

### Plantilla de libro contable

—Y ahora, lo más importante —dijo Don Alberto—. Vamos a crear una plantilla.

**Plantilla básica para estados financieros:**

```
┌──────────────────────────────────────────┐
│   EMPRESA XYZ S.A.C.                     │
│   Estado de Resultados                   │
│   Al 31 de diciembre de 2025             │
├──────────────────────────────────────────┤
│                                           │
│   Ventas netas                    1,000   │
│   Costo de ventas                  (600)  │
│   Utilidad bruta                    400   │
│                                           │
│   Gastos operativos                (200)  │
│   Utilidad operativa                200   │
│                                           │
│   Gastos financieros                (30)  │
│   Utilidad antes de impuestos       170   │
│   Impuesto a la renta               (51)  │
│   Utilidad neta                     119   │
└──────────────────────────────────────────┘
```

—¿Ves? —dijo Don Alberto—. No es solo poner números. Es estructurarlos, formatearlos, preparar el escenario.

### Resumen del capítulo

| Concepto | Configuración recomendada |
|----------|--------------------------|
| Cálculo | Automático con iterativo habilitado |
| Decimales | Precisión de visualización activada |
| Formato contable | #,##0.00 ;(#,##0.00);"-" |
| Fechas | dd-mmm-aaaa |
| Tema | Office con Calibri 10 |
| Barra acceso rápido | Bordes, formato contable, inmovilizar |

### Enigma contable #1

María recibió un archivo de Excel del Banco de la Nación con 5,000 transacciones. El formato de los montos venía como texto con comas (ej: "1,234.56") y las fechas en formato americano (MM/DD/AAAA).

**Tu misión:** Configura Excel para que María pueda:
1. Convertir esos textos a números sin perder precisión
2. Configurar el formato contable peruano (S/)
3. Mostrar las fechas en formato dd/mm/aaaa
4. Crear una plantilla de conciliación bancaria con formato condicional que resalte diferencias mayores a 1,000 en rojo

*Abre el archivo `codigos/01_configuracion/plantilla_conciliacion.xlsx` para comenzar.*