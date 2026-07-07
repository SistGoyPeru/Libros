# Capítulo 14: El Código Asesino — Segunda Parte

## Proyecto Integrador: El motor de análisis y el enfrentamiento final

---

El laboratorio estaba en silencio. Wayra había escrito los módulos de datos y modelos. Ahora venía la parte crucial: el motor de análisis que procesaría toda la información y revelaría al asesino.

—Este es el corazón del Código Asesino —dijo, con los dedos sobre el teclado—. Todo lo que hemos aprendido se reduce a esto.

### Módulo 4: `analisis.py` — El motor de razonamiento

```python
# ============================================
# MÓDULO: analisis.py
# CONTIENE: Motor de análisis forense digital
# CONCEPTOS: condicionales, bucles, funciones,
#            manejo de archivos, excepciones
# ============================================

from datos_caso import *
from quipus import *
from sospechosos import Sospechoso
import os


# --- FUNCIÓN 1: ANÁLISIS DE QUIPUS ---

def analizar_quipus_completo():
    """Analiza todos los quipus del caso y busca patrones."""
    print("=" * 65)
    print("  ANÁLISIS DE QUIPUS DIGITALES")
    print("=" * 65)
    
    quipus_decodificados = decodificar_todos_los_quipus(quipus_del_caso)
    
    for q in quipus_decodificados:
        print(quipu_a_string(q))
    
    print()
    
    # Buscar patrones especiales
    print("  ► Patrones detectados:")
    
    for q in quipus_decodificados:
        if q["patron"] != "variable":
            print(f"    • {q['color'].title()}: progresión {q['patron']}")
    
    # Analizar el quipu blanco (especial)
    blanco = buscar_quipu_por_color(quipus_del_caso, "blanco")
    if blanco:
        b = blanco[0]
        print(f"\n  ► QUIPU BLANCO (clave):")
        print(f"    • Nudos en posiciones: {b['nudos']}")
        print(f"    • Total: {len(b['nudos'])} nudos")
        print(f"    • Interpretación: las posiciones impares 1,3,5,7,9,11")
        print(f"      representan a las 6 personas clave del caso")
    
    return quipus_decodificados


# --- FUNCIÓN 2: CREAR SOSPECHOSOS ---

def crear_sospechosos():
    """Crea objetos Sospechoso a partir de los datos."""
    sospechosos_objetos = []
    
    for nombre, datos in sospechosos_data.items():
        s = Sospechoso(nombre, datos["edad"], datos["rol"], datos)
        sospechosos_objetos.append(s)
    
    return sospechosos_objetos


# --- FUNCIÓN 3: ANÁLISIS DE COARTADAS ---

def verificar_coartadas(registros, hora_crimen):
    """Verifica quién tiene coartada según los registros de acceso."""
    print("  ► Verificación de coartadas:")
    print(f"    Hora del crimen: {hora_crimen}\n")
    
    h_crimen, m_crimen = map(int, hora_crimen.split(":"))
    minutos_crimen = h_crimen * 60 + m_crimen
    
    # Personas dentro del laboratorio a la hora del crimen
    dentro = []
    estado_personas = {}
    
    for reg in registros:
        persona = reg["persona"]
        hora = reg["hora"]
        h, m = map(int, hora.split(":"))
        minutos = h * 60 + m
        
        if reg["tipo"] == "entrada":
            estado_personas[persona] = minutos
        elif reg["tipo"] == "salida":
            if persona in estado_personas:
                del estado_personas[persona]
    
    # Verificar quién estaba dentro a la hora del crimen
    print("    Personas dentro del lab a las 02:34:")
    for persona, minutos_entrada in estado_personas.items():
        if minutos_entrada <= minutos_crimen:
            print(f"      • {persona} (entró antes de las 02:34)")
            dentro.append(persona)
    
    if not dentro:
        print("      • NADIE (registro manipulado)")
    
    return dentro


# --- FUNCIÓN 4: ANÁLISIS DE EVIDENCIAS ---

def analizar_evidencias(sospechosos_objetos):
    """Analiza las evidencias de cada sospechoso."""
    print("\n  ► Resumen de evidencias por sospechoso:\n")
    
    for s in sospechosos_objetos:
        print(f"    • {s.nombre}")
        for ev in s.evidencias:
            print(f"      - {ev}")
        print()


# --- FUNCIÓN 5: CÁLCULO DE PUNTAJES ---

def calcular_puntajes(sospechosos_objetos):
    """Calcula y muestra los puntajes de todos los sospechosos."""
    print("  ► Cálculo de puntajes de sospecha:\n")
    
    resultados = []
    
    for s in sospechosos_objetos:
        reporte = s.reporte()
        resultados.append(reporte)
        
        barra = "█" * int(reporte["puntaje"]) + "░" * (10 - int(reporte["puntaje"]))
        print(f"    {reporte['nombre']:25} [{barra}] {reporte['puntaje']:.1f}/10 ({reporte['categoria']})")
    
    return resultados


# --- FUNCIÓN 6: DETERMINAR CULPABLE ---

def determinar_culpable(resultados):
    """Determina al culpable basado en los puntajes."""
    print("\n" + "=" * 65)
    print("  VEREDICTO DEL ANÁLISIS FORENSE DIGITAL")
    print("=" * 65)
    
    # Ordenar por puntaje descendente
    resultados.sort(key=lambda r: r["puntaje"], reverse=True)
    
    print(f"\n  Los sospechosos ordenados por nivel de sospecha:\n")
    
    for i, r in enumerate(resultados, 1):
        print(f"  {i}. {r['nombre']:25} - {r['puntaje']:.1f}/10")
    
    principal = resultados[0]
    segundo = resultados[1]
    
    print(f"\n  ► SOSPECHOSO PRINCIPAL: {principal['nombre']}")
    print(f"    Puntaje: {principal['puntaje']:.1f}/10")
    print(f"    Motivo: {principal['motivo']}")
    print(f"    Evidencias: {len(principal['evidencias'])}")
    
    # Coincidencia con el quipu blanco
    print(f"\n  ► Verificación con quipu blanco:")
    print(f"    Las posiciones impares (1,3,5,7,9,11) representan")
    print(f"    a las 6 personas en orden de importancia.")
    
    print(f"\n  ► Conclusión del análisis automatizado:")
    print(f"    El análisis forense digital señala a:")
    print(f"    ★ {principal['nombre'].upper()} ★")
    print(f"    Categoría: {principal['categoria']}")
    
    return principal


# --- FUNCIÓN 7: GENERAR INFORME ---

def generar_informe(resultados, culpable, quipus_decodificados):
    """Genera un informe de texto del caso."""
    
    with open("informe_final_caso.txt", "w", encoding="utf-8") as f:
        f.write("=" * 65 + "\n")
        f.write(f"INFORME FINAL: {nombre_caso}\n")
        f.write(f"Fecha: {fecha_crimen}\n")
        f.write(f"Investigadora: {investigadora}\n")
        f.write("=" * 65 + "\n\n")
        
        f.write("--- QUIPUS DIGITALES ANALIZADOS ---\n")
        for q in quipus_decodificados:
            f.write(f"  {q['color'].upper()}: {q['total_nudos']} nudos - {q['tipo']}\n")
        
        f.write("\n--- PUNTAJES DE SOSPECHA ---\n")
        for r in sorted(resultados, key=lambda r: r["puntaje"], reverse=True):
            f.write(f"  {r['nombre']:25} {r['puntaje']:.1f}/10 ({r['categoria']})\n")
        
        f.write(f"\n--- CULPABLE IDENTIFICADO ---\n")
        f.write(f"  {culpable['nombre']}\n")
        f.write(f"  Motivo: {culpable['motivo']}\n")
        f.write(f"  Evidencias:\n")
        for ev in culpable['evidencias']:
            f.write(f"    - {ev}\n")
        
        f.write("\n" + "=" * 65 + "\n")
        f.write("FIN DEL INFORME\n")
    
    print(f"\n  ► Informe generado: informe_final_caso.txt")
```

### Módulo 5: `main.py` — El punto de entrada

```python
# ============================================
# MÓDULO: main.py
# CONTIENE: Punto de entrada del Código Asesino
# CONCEPTOS: integración de todos los módulos
# ============================================

from analisis import *

def main():
    """Función principal del Código Asesino."""
    
    print("\n")
    print("  ╔═══════════════════════════════════════════════╗")
    print("  ║       CÓDIGO ASESINO - ANÁLISIS FORENSE      ║")
    print("  ║    El Enigma de Qhapaq Ñan - Motor de Datos  ║")
    print("  ╚═══════════════════════════════════════════════╝")
    print(f"\n  Caso: {nombre_caso}")
    print(f"  Investigadora: {investigadora}")
    print(f"  Fecha del crimen: {fecha_crimen}\n")
    
    # Paso 1: Analizar quipus
    quipus = analizar_quipus_completo()
    print()
    input("  Presiona Enter para continuar con el análisis de sospechosos...")
    print()
    
    # Paso 2: Crear sospechosos
    sospechosos = crear_sospechosos()
    
    # Paso 3: Verificar coartadas
    dentro = verificar_coartadas(registro_accesos, hora_crimen)
    print()
    
    # Paso 4: Analizar evidencias
    analizar_evidencias(sospechosos)
    input("  Presiona Enter para calcular puntajes...")
    print()
    
    # Paso 5: Calcular puntajes
    resultados = calcular_puntajes(sospechosos)
    print()
    
    # Paso 6: Determinar culpable
    input("  Presiona Enter para revelar el veredicto...")
    print()
    culpable = determinar_culpable(resultados)
    
    # Paso 7: Generar informe
    generar_informe(resultados, culpable, quipus)
    
    print("\n" + "=" * 65)
    print("  ANÁLISIS COMPLETADO")
    print("=" * 65)

if __name__ == "__main__":
    main()
```

Wayra guardó el último archivo y tomó un respiro profundo.

—Está listo —dijo—. El Código Asesino está completo.

—¿Y ahora? —preguntó Raúl.

—Ahora lo ejecutamos.

## La ejecución

Wayra abrió la terminal y escribió:

```bash
python main.py
```

La pantalla cobró vida. Los módulos se cargaron, los datos fluyeron, y el análisis comenzó...

```
  ╔═══════════════════════════════════════════════╗
  ║       CÓDIGO ASESINO - ANÁLISIS FORENSE      ║
  ║    El Enigma de Qhapaq Ñan - Motor de Datos  ║
  ╚═══════════════════════════════════════════════╝

  Caso: El Asesinato del Dr. Inti Quispe
  Investigadora: Wayra Condori
  Fecha del crimen: 27 de junio, 2026

=============================================================
  ANÁLISIS DE QUIPUS DIGITALES
=============================================================
  [ROJO    ] conflicto/guerra             | PREGUNTA         | 3 nudos
  [VERDE   ] crecimiento/conocimiento     | RESPUESTA        | 3 nudos
  [AZUL    ] espiritualidad/religión      | PREGUNTA         | 3 nudos
  [AMARILLO] poder/riqueza                | RESPUESTA        | 3 nudos
  [BLANCO  ] verdad/conexión espiritual   | PREGUNTA         | 6 nudos

  ► Patrones detectados:
    • Rojo: progresión 3
    • Verde: progresión 3
    • Azul: progresión 4
    • Amarillo: progresión 4

  ► QUIPU BLANCO (clave):
    • Nudos en posiciones: [1, 3, 5, 7, 9, 11]
    • Interpretación: posiciones impares = 6 personas clave

Presiona Enter para continuar con el análisis de sospechosos...
```

Wayra presionó Enter. El análisis continuó...

```
  ► Verificación de coartadas:
    Hora del crimen: 02:34

    Personas dentro del lab a las 02:34:
      • Inti (entró antes de las 02:34)
      • Lara (entró antes de las 02:34)

  ► Resumen de evidencias por sospechoso:

    • Lara Mamani
      - Registro de acceso a las 02:34
      - Huellas en el teclado de Inti
      - Hija secreta de Rodrigo Mamani
      - Llamada perdida de Inti a las 02:30

    • Dr. Carlos Huamán
      - ...

Presiona Enter para calcular puntajes...
```

Wayra sintió que el tiempo se detenía. Presionó Enter.

```
  ► Cálculo de puntajes de sospecha:

    Lara Mamani               [████████░░] 8.0/10 (CRÍTICO)
    Mama Killa                [██████░░░░] 6.5/10 (ALTO)
    Dr. Carlos Huamán         [██████░░░░] 6.0/10 (ALTO)
    Rodrigo Mamani            [█████░░░░░] 5.0/10 (MODERADO)
    Dra. Sarah Chen           [███░░░░░░░] 3.5/10 (BAJO)

Presiona Enter para revelar el veredicto...
```

El momento de la verdad.

Wayra dudó. Su mano flotaba sobre el teclado. Todo el análisis señalaba a Lara Mamani. Pero algo no cuadraba. Lara tenía el puntaje más alto, pero...

—Ejecútalo —dijo Raúl—. Descubre la verdad.

Wayra presionó Enter.

```
=============================================================
  VEREDICTO DEL ANÁLISIS FORENSE DIGITAL
=============================================================

  Los sospechosos ordenados por nivel de sospecha:

  1. Lara Mamani              - 8.0/10
  2. Mama Killa               - 6.5/10
  3. Dr. Carlos Huamán        - 6.0/10
  4. Rodrigo Mamani           - 5.0/10
  5. Dra. Sarah Chen          - 3.5/10

  ► SOSPECHOSO PRINCIPAL: Lara Mamani
    Puntaje: 8.0/10
    Motivo: Económico/Emocional (hija de Rodrigo)
    Evidencias: 4

  ► Conclusión del análisis automatizado:
    El análisis forense digital señala a:
    ★ LARA MAMANI ★
    Categoría: CRÍTICO
```

—Lara —dijo Raúl—. El programa dice que fue Lara.

—El programa dice lo que programamos —respondió Wayra lentamente—. Pero hay algo que no hemos considerado. Algo que distorsiona todos los datos.

—¿Qué?

—La cuenta de Lara se usó a las 02:34. Pero si alguien más usó su cuenta... entonces todos los datos que la señalan son falsos. Son datos plantados por el verdadero asesino.

Wayra abrió el archivo `informe_final_caso.txt` que el programa había generado. Leyó las evidencias de Lara una vez más. Y entonces lo vio.

—La llamada perdida —dijo—. Inti llamó a Lara a las 02:30. Cuatro minutos antes de morir. ¿Por qué llamaría a la persona que lo iba a matar?

—¿Para pedir ayuda?

—O para decirle algo. Algo que Lara sabe pero no ha dicho. Algo que la pone en peligro.

Wayra tomó su teléfono y marcó el número de Lara Mamani.

—¿Qué haces? —preguntó Raúl.

—Llamar a la persona que el programa dice que es la asesina. Porque a veces, la verdad no está en el código. Está en lo que el código no puede medir.

El teléfono sonó tres veces. Luego, una voz temblorosa respondió:

—¿Wayra? ¿Eres tú?

—Soy yo, Lara. Necesito que me digas la verdad. ¿Por qué te llamó Inti a las 02:30?

Hubo un largo silencio. Luego, Lara habló:

—Porque me dijo quién lo iba a matar. Y me dijo que te buscara a ti.

---

## Enigmas

### Enigma 14.1: Ejecuta el análisis completo

Copia todos los módulos del proyecto en tu editor y ejecuta `main.py`. ¿Coincide el resultado con lo que esperabas?

### Enigma 14.2: Agrega un nuevo factor

Modifica el cálculo de puntaje en la clase `Sospechoso` para incluir un factor de "conexión emocional con la víctima". ¿Cambia el resultado?

### Enigma 14.3: El sesgo del quipu blanco

El quipu blanco tiene 6 nudos (posiciones impares hasta 11). ¿Qué relación tienen esos números con los sospechosos? (Pista: piensa en edades, niveles de acceso, días del mes...)

### Enigma 14.4: Tu propio veredicto

Basado en toda la evidencia presentada en el libro, ¿quién crees que es el asesino? Escribe un pequeño programa que capture tu teoría y la compare con el resultado del análisis.

---

## Lo que aprendiste (proyecto completo)

- Cómo **estructurar** un proyecto Python completo
- Cómo integrar **múltiples módulos** en un programa cohesivo
- Cómo aplicar **todos los conceptos** de Python en un caso real
- Cómo los datos pueden **mentir** si no se interpretan correctamente
- Que la lógica del código es tan buena como los datos que recibe

Wayra colgó el teléfono. Lara había hablado. La verdad era más compleja de lo que cualquier algoritmo podía calcular. Porque la verdad involucraba secretos de familia, lealtades divididas y un amor fraternal que trascendía la muerte.

—Raúl —dijo—. El Código Asesino ha hecho su trabajo. Nos ha dado los datos. Pero la verdadera respuesta... la verdadera respuesta está en lo que el código no puede procesar: el corazón humano.

—¿Y ahora?

—Ahora vamos a encontrarnos con Lara. Y vamos a descubrir quién mató realmente a Inti Quispe.

---
