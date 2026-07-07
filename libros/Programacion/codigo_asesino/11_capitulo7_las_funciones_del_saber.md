# Capítulo 7: Las Funciones del Saber Ancestral

## Conceptos: Funciones, parámetros, `return`, alcance de variables, docstrings

---

Wayra estaba dentro del laboratorio. Frente a ella, la pantalla OLED parpadeaba con el mensaje enigmático sobre "funciones". A su alrededor, el laboratorio de Inti Quispe era un santuario de la tecnología andina: estantes con quipus antiguos, monitores con gráficos de patrones textiles, y una pizarra llena de ecuaciones que mezclaban símbolos incas con notación matemática moderna.

—Inti no solo programaba —dijo Wayra, recorriendo el espacio con la mirada—. Inti **tejía** código. Cada función era como un nudo en un quipu: una unidad de conocimiento que podía combinarse con otras para crear significados complejos.

En la pizarra, alguien había escrito:

```
MAMA → hilo_principal()
TAYTA → hilo_secundario()
Wawa → hilo_terciario()

Cada hilo (función) recibe datos (parámetros)
y produce un resultado (return).
El tejido completo es el programa.
```

—Inti usaba metáforas textiles para enseñar programación —explicó Wayra—. Y voy a usar el mismo método.

## Funciones: Tejiendo código reutilizable

Una **función** es un bloque de código que realizas una tarea específica y puede reutilizarse. Como un nudo en un quipu: aprendes a hacerlo una vez y lo usas en diferentes cuerdas.

```python
# ============================================
# FUNCIONES DEL SABER ANCESTRAL
# ============================================

# Definición de una función básica
def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida del laboratorio."""
    print("=" * 50)
    print("LABORATORIO YACHAY - Conocimiento Ancestral Digital")
    print("=" * 50)

# Llamar a la función
mostrar_bienvenida()
```

### Parámetros: Los hilos de entrada

Los **parámetros** son los datos que la función recibe para trabajar. Como los hilos de diferentes colores que recibe un tejedor:

```python
print("\n=== FICHAS DE SOSPECHOSOS ===\n")

def crear_ficha(nombre, edad, rol, nivel_sospecha):
    """Crea una ficha formateada de un sospechoso."""
    print(f"■ {nombre.upper()}")
    print(f"  Edad: {edad}")
    print(f"  Rol: {rol}")
    print(f"  Nivel de sospecha: {nivel_sospecha}/10")
    print()

# Llamar a la función con diferentes argumentos
crear_ficha("Lara Mamani", 32, "Asistente", 7)
crear_ficha("Dr. Carlos Huamán", 55, "Colega", 8)
crear_ficha("Mama Killa", 70, "Hermana", 5)
```

### Parámetros por defecto

A veces, un parámetro tiene un valor que se usa la mayoría de las veces. Python permite establecer valores por defecto:

```python
def crear_ficha_avanzada(nombre, edad, rol, nivel_sospecha=5, acceso=False):
    """Crea una ficha con valores por defecto."""
    print(f"■ {nombre}")
    print(f"  Edad: {edad} | Rol: {rol}")
    print(f"  Sospecha: {nivel_sospecha}/10 | Acceso: {acceso}")
    print()

crear_ficha_avanzada("Rodrigo Mamani", 60, "Empresario", 9)
crear_ficha_avanzada("Sarah Chen", 40, "Colaboradora")
crear_ficha_avanzada("Visitante Desconocido", 0, "Desconocido")
```

—Los valores por defecto son como los nudos estándar en un quipu —dijo Wayra—. La mayoría de los quipus usan nudos simples por defecto, a menos que especifiques lo contrario.

### Return: El resultado del tejido

Las funciones no solo hacen cosas: también **devuelven** resultados con `return`. Como un quipucamayoc que "devuelve" el significado después de leer los nudos:

```python
def calcular_nivel_sospecha(acceso, coartada, motivo, huellas):
    """Calcula un nivel de sospecha basado en múltiples factores.
    
    Parámetros:
        acceso (bool): Si la persona tenía acceso al laboratorio
        coartada (bool): Si la persona tiene coartada
        motivo (int): Nivel de motivo (1-10)
        huellas (bool): Si sus huellas están en la escena
    
    Returns:
        int: Nivel de sospecha (0-10)
    """
    puntaje = 0
    
    if acceso:
        puntaje += 3
    if not coartada:
        puntaje += 4
    if motivo >= 7:
        puntaje += 3
    elif motivo >= 4:
        puntaje += 1
    if huellas:
        puntaje += 1
    
    return min(puntaje, 10)  # Máximo 10

# Usando la función
nivel_lara = calcular_nivel_sospecha(True, False, 7, True)
nivel_carlos = calcular_nivel_sospecha(True, True, 8, False)

print(f"\nNivel de sospecha de Lara: {nivel_lara}/10")
print(f"Nivel de sospecha de Carlos: {nivel_carlos}/10")
```

### Múltiples valores de retorno

Una función puede devolver varios valores como una tupla:

```python
def analizar_sospechoso_completo(nombre, acceso, coartada, motivo, huellas):
    """Analiza un sospechoso y devuelve múltiples resultados."""
    nivel = calcular_nivel_sospecha(acceso, coartada, motivo, huellas)
    
    if nivel >= 8:
        categoria = "CRÍTICO"
        accion = "Interrogar inmediatamente"
    elif nivel >= 5:
        categoria = "ALTO"
        accion = "Vigilancia continua"
    elif nivel >= 3:
        categoria = "MODERADO"
        accion = "Mantener en observación"
    else:
        categoria = "BAJO"
        accion = "Sin acción requerida"
    
    return nivel, categoria, accion

# Desempaquetando el resultado
nombre = "Lara Mamani"
nivel, categoria, accion = analizar_sospechoso_completo(
    nombre, True, False, 7, True
)

print(f"\n=== RESULTADO: {nombre} ===")
print(f"Nivel: {nivel}/10")
print(f"Categoría: {categoria}")
print(f"Acción recomendada: {accion}")
```

## Alcance de variables: El mundo de cada hilo

En Python, las variables tienen **alcance** (scope). Las variables definidas dentro de una función solo existen dentro de esa función. Como los hilos de un tejido: un hilo rojo en una parte del tejido no afecta al hilo azul en otra parte.

```python
# Variable global (fuera de cualquier función)
laboratorio = "Coricancha"
investigadora = "Wayra Condori"

def mostrar_caso():
    # Variable local (solo existe dentro de esta función)
    nombre_caso = "El Asesinato del Dr. Inti Quispe"
    
    # Podemos ACCEDER a variables globales
    print(f"Caso: {nombre_caso}")
    print(f"Lugar: {laboratorio}")
    print(f"Investigadora: {investigadora}")

mostrar_caso()

# print(nombre_caso)  # ¡Error! nombre_caso no existe aquí

def cambiar_laboratorio():
    # Para MODIFICAR una variable global, necesitamos 'global'
    global laboratorio
    laboratorio = "Laboratorio Secreto del Qhapaq Ñan"
    print(f"Laboratorio cambiado a: {laboratorio}")

cambiar_laboratorio()
print(f"Laboratorio ahora es: {laboratorio}")
```

## La función del quipu descifrador

Wayra encontró en la computadora de Inti una función incompleta. Era la que había visto antes, pero ahora tenía más contexto:

```python
# --- LA FUNCIÓN INCOMPLETA DE INTI ---

def descifrar_quipu_digital(quipu_codificado):
    """Descifra un quipu digital y devuelve el mensaje oculto.
    
    Los quipus digitales usan el formato:
    'COLOR:pos1:pos2:pos3'
    
    Donde:
    - COLOR es el tipo de información (ROJO, VERDE, AZUL, etc.)
    - posN son las posiciones de los nudos
    
    Returns:
        dict: Con las claves 'tipo', 'posiciones', 'mensaje'
    """
    # Separar el quipu en partes
    partes = quipu_codificado.split(":")
    
    tipo = partes[0]
    posiciones = [int(p) for p in partes[1:]]
    
    # Decodificar según el tipo
    # (Esta parte estaba incompleta - Wayra la completó)
    
    return {
        "tipo": tipo,
        "posiciones": posiciones,
        "mensaje": f"Decodificado: {tipo} - {posiciones}"
    }

# Probar la función
quipu1 = descifrar_quipu_digital("ROJO:1:4:9")
quipu2 = descifrar_quipu_digital("BLANCO:1:3:5:7:9")

print("\n=== QUIPUS DESCIFRADOS ===")
print(f"Quipu 1: {quipu1}")
print(f"Quipu 2: {quipu2}")
```

## Las funciones del enigma

Wayra se dio cuenta de que necesitaba construir un sistema completo de análisis usando funciones:

```python
# ============================================
# SISTEMA DE ANÁLISIS FORENSE DIGITAL
# ============================================

def verificar_coartada(hora_declarada, hora_crimen, margen=30):
    """Verifica si una coartada es plausible.
    
    Args:
        hora_declarada (str): Hora que la persona dice estar
        hora_crimen (str): Hora del crimen
        margen (int): Minutos de tolerancia
    
    Returns:
        bool: True si la coartada es válida
    """
    # Convertir horas a minutos para comparar
    h_declarada, m_declarada = map(int, hora_declarada.split(":"))
    h_crimen, m_crimen = map(int, hora_crimen.split(":"))
    
    total_declarada = h_declarada * 60 + m_declarada
    total_crimen = h_crimen * 60 + m_crimen
    
    diferencia = abs(total_declarada - total_crimen)
    
    return diferencia > margen

def buscar_patron_en_quipus(lista_quipus, color_buscar):
    """Busca quipus de un color específico en una lista."""
    resultados = []
    for quipu in lista_quipus:
        if quipu.startswith(color_buscar):
            resultados.append(quipu)
    return resultados

def generar_informe(sospechosos_analizados):
    """Genera un informe formateado con todos los análisis."""
    print("\n" + "=" * 60)
    print("INFORME FORENSE DIGITAL - CASO INTI QUISPE")
    print("=" * 60)
    
    for nombre, datos in sospechosos_analizados.items():
        print(f"\n▶ {nombre}")
        print(f"  Nivel de sospecha: {datos['nivel']}/10")
        print(f"  Categoría: {datos['categoria']}")
        print(f"  Acción: {datos['accion']}")
    
    print("\n" + "=" * 60)
    print("FIN DEL INFORME")
    print("=" * 60)

# --- EJECUTANDO EL SISTEMA ---

sospechosos_data = {
    "Lara Mamani": {"acceso": True, "coartada": False, "motivo": 7, "huellas": True},
    "Carlos Huamán": {"acceso": True, "coartada": True, "motivo": 8, "huellas": False},
    "Sarah Chen": {"acceso": True, "coartada": True, "motivo": 6, "huellas": False},
    "Rodrigo Mamani": {"acceso": False, "coartada": True, "motivo": 9, "huellas": False},
    "Mama Killa": {"acceso": True, "coartada": True, "motivo": 5, "huellas": True}
}

resultados = {}
for nombre, datos in sospechosos_data.items():
    nivel, categoria, accion = analizar_sospechoso_completo(
        nombre,
        datos["acceso"],
        datos["coartada"],
        datos["motivo"],
        datos["huellas"]
    )
    resultados[nombre] = {
        "nivel": nivel,
        "categoria": categoria,
        "accion": accion
    }

generar_informe(resultados)
```

## Enigmas

### Enigma 7.1: Tu primera función

Escribe una función llamada `presentar_sospechoso()` que reciba un nombre y un rol, y muestre:

```
SOSPECHOSO: [nombre]
ROL: [rol]
```

### Enigma 7.2: Calculadora de coartadas

Escribe una función `verificar_coartada(hora_coartada, hora_crimen)` que devuelva `True` si la coartada es al menos 1 hora antes o después del crimen (asume hora_crimen = "02:34"). Usa `return`.

### Enigma 7.3: Función con valores por defecto

Crea una función `mensaje_secreto(mensaje, cifrado=True)` que:
- Si `cifrado` es `True`, devuelve el mensaje invertido (`[::-1]`)
- Si `cifrado` es `False`, devuelve el mensaje original

### Enigma 7.4: Sistema de puntaje completo

Usando las funciones que has visto, crea un programa que pida datos de un sospechoso (input) y devuelva su nivel de sospecha.

---

## Lo que aprendiste

- **`def nombre_funcion():`** define una función
- Los **parámetros** son los datos que recibe la función
- Los **valores por defecto** hacen parámetros opcionales
- **`return`** devuelve un valor desde la función
- Las funciones pueden devolver **múltiples valores** como tupla
- El **alcance (scope)** determina qué variables son accesibles
- `global` permite modificar variables globales desde una función
- Los **docstrings** (`"""..."""`) documentan qué hace la función

Wayra terminó de escribir su sistema de análisis. Ahora tenía herramientas reutilizables para cualquier nuevo dato que apareciera. Pero cuando giró para mostrarle el resultado a Raúl, notó que algo había cambiado en el laboratorio.

La computadora de Inti estaba encendida. Pero no la había encendido ella.

—Raúl —dijo lentamente—. ¿Tocaste la computadora?

—No. Pensé que habías sido tú.

Wayra se acercó. En la pantalla, una ventana de terminal mostraba un proceso activo:

```
YACHAY_CORE.EXE - EJECUTANDO
ÚLTIMA MODIFICACIÓN: 27/06/2026 02:34
ARCHIVOS ACCEDIDOS: quipus_digitales.db, registro_accesos.log
USUARIO: root
```

—Alguien más está en el sistema —susurró Wayra—. Y está usando Yachay en este momento.

De repente, la pantalla cambió. Un nuevo mensaje apareció:

```
Wayra Condori.
Has descifrado funciones. Has recorrido caminos.
Pero el código tiene un archivo que no has abierto.
El archivo que contiene la verdadera historia.
Está en el laboratorio. Busca en los quipus.
Pero cuidado: algunos archivos guardan secretos
que no deberían ser descubiertos.

-- Inti (o quien controla su legado)
```

Wayra sintió que el tiempo se aceleraba. El asesino —o alguien— estaba interactuando con ella en tiempo real. Sabía su nombre. Sabía lo que había hecho.

Y la estaba invitando a seguir.

—Raúl —dijo—. Busca todos los archivos del laboratorio. Archivos físicos, digitales, quipus, lo que sea. Necesito encontrar ese archivo antes que el asesino.

—¿Antes? ¿No está muerto Inti?

Wayra negó con la cabeza.

—El asesino no es el que está en el sistema ahora. El asesino es quien mató a Inti. Pero quien está en el sistema ahora... es otra persona. Alguien que está usando Yachay. Y que quiere que yo encuentre algo.

—¿Qué?

—No lo sé. Pero solo hay una forma de descubrirlo. Abrir los archivos de Inti.

---
