# Capítulo 11: La Clase del Misterio

## Conceptos: POO, clases, objetos, atributos, métodos, `__init__`, `self`

---

La madrugada envolvía Neo-Cusco en un silencio de piedra. En el laboratorio, Wayra había encontrado el núcleo de Yachay. No era un algoritmo de inteligencia artificial convencional. Era un modelo del mundo construido con **clases** de Python.

—Inti no construyó una IA —dijo Wayra, maravillada—. Construyó un universo de objetos. Cada persona, cada quipu, cada secreto en este caso... está representado como un objeto en Yachay.

—¿Un objeto? —preguntó Raúl.

—En Python, un **objeto** es una representación de algo del mundo real dentro del código. Y una **clase** es como un molde para crear objetos. Como un telar: el telar (la clase) define la estructura, pero cada tejido (el objeto) es único.

## Clases: El telar del quipucamayoc

```python
# ============================================
# MODELANDO EL MISTERIO CON CLASES
# ============================================

class QuipuDigital:
    """Representa un quipu digital."""
    
    def __init__(self, color, posiciones, significado=""):
        """Inicializa un nuevo quipu digital.
        
        Args:
            color: El color de la cuerda principal
            posiciones: Lista de posiciones de los nudos
            significado: El significado del quipu
        """
        self.color = color
        self.posiciones = posiciones
        self.significado = significado
        self.descifrado = False
    
    def descifrar(self):
        """Descifra el quipu y revela su mensaje."""
        mensaje = f"Quipu {self.color}: {len(self.posiciones)} nudos en posiciones {self.posiciones}"
        self.descifrado = True
        return mensaje
    
    def agregar_nudo(self, posicion):
        """Agrega un nudo en la posición especificada."""
        if posicion not in self.posiciones:
            self.posiciones.append(posicion)
            self.posiciones.sort()
            print(f"  ✓ Nudo agregado en posición {posicion}")
        else:
            print(f"  ✗ Ya existe un nudo en posición {posicion}")

# Crear objetos (instancias) de la clase QuipuDigital
quipu_rojo = QuipuDigital("rojo", [1, 4, 9], "conflicto")
quipu_blanco = QuipuDigital("blanco", [1, 3, 5, 7, 9], "verdad")

print("=== QUIPUS DIGITALES CREADOS ===\n")
print(f"Quipu rojo: {quipu_rojo.color} - {quipu_rojo.significado}")
print(f"Quipu blanco: {quipu_blanco.color} - {quipu_blanco.significado}")

# Usar métodos de los objetos
print("\n=== DESCIFRANDO QUIPUS ===\n")
print(quipu_rojo.descifrar())
print(quipu_blanco.descifrar())

# Modificar atributos
quipu_blanco.agregar_nudo(11)
quipu_blanco.agregar_nudo(5)  # Ya existe
```

### La clase Sospechoso

Wayra decidió modelar a los sospechosos como objetos. Cada uno con sus atributos y métodos:

```python
class Sospechoso:
    """Representa un sospechoso en el caso."""
    
    def __init__(self, nombre, edad, rol, acceso=False):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
        self.acceso = acceso
        self.nivel_sospecha = 0
        self.coartada = ""
        self.evidencias = []
        self.interrogado = False
    
    def agregar_evidencia(self, evidencia):
        """Agrega una evidencia en contra del sospechoso."""
        self.evidencias.append(evidencia)
        self.nivel_sospecha += 2
        print(f"  ⚠ Evidencia contra {self.nombre}: {evidencia}")
    
    def establecer_coartada(self, coartada):
        """Establece la coartada del sospechoso."""
        self.coartada = coartada
        print(f"  ✓ Coartada registrada: {coartada}")
    
    def interrogar(self):
        """Simula un interrogatorio."""
        self.interrogado = True
        print(f"\n  === INTERROGANDO A {self.nombre.upper()} ===")
        print(f"  Edad: {self.edad}")
        print(f"  Rol: {self.rol}")
        print(f"  Acceso: {self.acceso}")
        print(f"  Coartada: {self.coartada or 'No proporcionada'}")
        print(f"  Evidencias: {len(self.evidencias)}")
        
        if self.nivel_sospecha >= 6:
            return f"  → {self.nombre} es ALTAMENTE SOSPECHOSO"
        elif self.nivel_sospecha >= 3:
            return f"  → {self.nombre} es MODERADAMENTE SOSPECHOSO"
        else:
            return f"  → {self.nombre} es POCO SOSPECHOSO"

# Crear sospechosos como objetos
lara = Sospechoso("Lara Mamani", 32, "Asistente", acceso=True)
carlos = Sospechoso("Dr. Carlos Huamán", 55, "Colega universitario", acceso=True)
sarah = Sospechoso("Dra. Sarah Chen", 40, "Colaboradora MIT", acceso=True)
rodrigo = Sospechoso("Rodrigo Mamani", 60, "Empresario", acceso=False)
killa = Sospechoso("Mama Killa", 70, "Hermana", acceso=True)

print("\n=== SOSPECHOSOS CREADOS COMO OBJETOS ===\n")

# Agregar evidencias
lara.agregar_evidencia("Registro de acceso a las 2:34")
lara.agregar_evidencia("Huellas en el teclado")
lara.establecer_coartada("Estaba en su departamento (sin verificar)")

carlos.agregar_evidencia("Discusión con Inti días antes")
carlos.establecer_coartada("Oficina universitaria")
```

## El valor de `self`

Wayra notó que Raúl estaba confundido con `self`.

—`self` es la forma en que un objeto se refiere a sí mismo —explicó—. Cuando creas `lara = Sospechoso(...)`, y luego llamas `lara.interrogar()`, Python pasa automáticamente el objeto `lara` como `self` al método. Así el método sabe **qué** sospechoso está interrogando.

### Atributos de clase vs. de instancia

Algunos atributos pertenecen a la clase (son iguales para todos los objetos) y otros a cada instancia:

```python
class Investigacion:
    """Clase que modela toda la investigación."""
    
    # Atributo de clase (compartido por todas las instancias)
    nombre_del_caso = "El Asesinato del Dr. Inti Quispe"
    total_investigadores = 0
    
    def __init__(self, investigador_principal):
        # Atributos de instancia (únicos para cada objeto)
        self.investigador = investigador_principal
        self.sospechosos = []
        self.evidencias_encontradas = []
        self.estado = "abierta"
        
        Investigacion.total_investigadores += 1
    
    def agregar_sospechoso(self, sospechoso):
        self.sospechosos.append(sospechoso)
    
    def agregar_evidencia(self, evidencia):
        self.evidencias_encontradas.append(evidencia)
    
    def resumen(self):
        print(f"\n=== {self.nombre_del_caso} ===")
        print(f"Investigador: {self.investigador}")
        print(f"Estado: {self.estado}")
        print(f"Sospechosos: {len(self.sospechosos)}")
        print(f"Evidencias: {len(self.evidencias_encontradas)}")
        print(f"Total investigadores activos: {Investigacion.total_investigadores}")

# Crear la investigación
caso = Investigacion("Wayra Condori")
caso.agregar_sospechoso(lara)
caso.agregar_sospechoso(carlos)
caso.agregar_evidencia("Quipu digital modificado")
caso.agregar_evidencia("Registro de acceso fraudulento")
caso.resumen()
```

## La clase que reveló el secreto

Wayra encontró en el código de Yachay una clase especial:

```python
class PersonaYachay:
    """Modela una persona en el sistema Yachay."""
    
    def __init__(self, id_persona, nombre_real, rol_en_sistema, secreto=None, 
                 lealtad="desconocida", nivel_acceso=0):
        self.id = id_persona
        self.nombre = nombre_real
        self.rol = rol_en_sistema
        self.secreto = secreto  # Atributo oculto
        self.lealtad = lealtad
        self.nivel_acceso = nivel_acceso
        self._conexiones = []  # Privado por convención
    
    def revelar_secreto(self, clave_acceso):
        """Revela el secreto si la clave es correcta."""
        if clave_acceso == "YACHAY_ADMIN":
            return f"Secreto de {self.nombre}: {self.secreto}"
        return "Acceso denegado"
    
    def conectar_con(self, otra_persona):
        """Establece una conexión entre dos personas en el sistema."""
        self._conexiones.append(otra_persona.id)
        print(f"  🔗 {self.nombre} → {otra_persona.nombre}")

# Las personas en el sistema Yachay
print("\n=== PERSONAS EN EL SISTEMA YACHAY ===\n")

personas_yachay = [
    PersonaYachay("P001", "Inti Quispe", "Creador", 
                  "Yac... llave... quipu blanco...", "Círculo del Sol", 10),
    PersonaYachay("P002", "Lara Mamani", "Asistente", 
                  "Hija de Rodrigo Mamani", "Dividida", 7),
    PersonaYachay("P003", "Carlos Huamán", "Colega", 
                  "Saboteó publicación de Inti en 2024", "Universidad", 5),
    PersonaYachay("P004", "Sarah Chen", "Colaboradora", 
                  "Presionada por MIT para obtener Yachay", "MIT/Círculo", 6),
    PersonaYachay("P005", "Rodrigo Mamani", "Empresario", 
                  "Líder de Los Herederos de Pizarro", "Herederos", 3),
    PersonaYachay("P006", "Mama Killa", "Guardiana", 
                  "Sabe quién mató a Inti pero no puede hablar", "Círculo del Sol", 9),
    PersonaYachay("P007", "Wayra Condori", "Investigadora", 
                  "Nieta de Teodora - heredera del conocimiento", "En desarrollo", 1)
]

for p in personas_yachay:
    print(f"  [{p.id}] {p.nombre:25} | Rol: {p.rol:20} | Lealtad: {p.lealtad}")
```

Wayra se detuvo en la última entrada. La suya propia.

—Inti me conocía —susurró—. Me tenía registrada en su sistema. Como "investigadora". Con nivel de acceso 1, el más bajo. Pero estoy aquí.

—¿Y qué dice tu secreto? —preguntó Raúl.

—"Nieta de Teodora - heredera del conocimiento". Mi abuela Teodora... ella tejía con la hermana de Inti. Inti sabía que yo terminaría aquí.

Wayra continuó explorando las conexiones entre las personas en el sistema:

```python
# Establecer conexiones conocidas
inti = personas_yachay[0]
lara = personas_yachay[1]
rodrigo = personas_yachay[4]
killa = personas_yachay[5]

# Conexiones conocidas
inti.conectar_con(lara)     # Jefe-asistente
inti.conectar_con(killa)    # Hermano-hermana
lara.conectar_con(rodrigo)  # Padre-hija (secreto)

# Ver los secretos con la clave
print("\n=== REVELANDO SECRETOS ===\n")
for p in personas_yachay:
    secreto = p.revelar_secreto("YACHAY_ADMIN")
    print(f"  {p.nombre}: {secreto}")
```

## Enigmas

### Enigma 11.1: Crea la clase Evidencia

Define una clase `Evidencia` con:
- Atributos: `tipo` (str), `descripcion` (str), `fecha` (str), `es_clave` (bool)
- Método `mostrar()` que imprima toda la información
- Método `marcar_como_clave()` que cambie `es_clave` a True

Crea dos objetos Evidencia y usa sus métodos.

### Enigma 11.2: Agrega un método a Sospechoso

Agrega un método `liberar_sospechas()` a la clase `Sospechoso` que:
- Ponga `nivel_sospecha` a 0
- Muestre "Sospechas liberadas para [nombre]"

### Enigma 11.3: Contador de objetos

Modifica la clase `QuipuDigital` para que lleve la cuenta de cuántos quipus se han creado en total (usa un atributo de clase).

### Enigma 11.4: Tu propia investigación

Crea una clase `Pista` con:
- Atributos: `id`, `descripcion`, `ubicacion`, `resuelta`
- Método `resolver()` que marque la pista como resuelta
- Método `info()` que muestre los detalles

Luego crea 3 pistas del caso y muéstralas.

---

## Lo que aprendiste

- Una **clase** es un molde para crear objetos
- Un **objeto** es una instancia concreta de una clase
- `__init__()` es el constructor que inicializa los objetos
- `self` es la referencia al propio objeto dentro de sus métodos
- **Atributos de clase** son compartidos por todas las instancias
- **Atributos de instancia** son únicos para cada objeto
- Los **métodos** son funciones que pertenecen a un objeto
- La POO permite modelar el mundo real en código

Wayra miró la lista de personas en Yachay. Todos tenían secretos. Todos tenían conexiones. Pero había algo que no cuadraba.

—Raúl —dijo—. Mama Killa tiene nivel de acceso 9. Solo superada por Inti. Ella sabe quién mató a su hermano. ¿Por qué no habla?

—Quizás tiene miedo.

—O quizás está protegida por el Círculo del Sol. O quizás... es la siguiente.

Wayra revisó los niveles de acceso. Rodrigo Mamani tenía nivel 3, el más bajo después de ella misma. Pero era el líder de Los Herederos de Pizarro. ¿Cómo podía tener acceso tan bajo si era el principal sospechoso?

—A menos que... —murmuró—. A menos que no necesitara acceso porque alguien con más acceso trabajaba para él.

Lara. Nivel de acceso 7. Hija de Rodrigo.

—Lara le dio acceso a su padre —dijo Wayra—. O Rodrigo usó a Lara para obtener lo que necesitaba. Pero si eso es cierto... ¿Lara sabía que su padre iba a matar a Inti?

La respuesta estaba en el código. En las **relaciones** entre las clases. En la **herencia**.

---
