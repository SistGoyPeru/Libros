# Capítulo 12: La Herencia de los Incas

## Conceptos: Herencia, polimorfismo, encapsulación, `super()`

---

El sol comenzaba a filtrarse por las rendijas de piedra del laboratorio cuando Wayra encontró el archivo más importante de Yachay: `modelo_herencia.py`. Dentro, Inti había modelado no solo a las personas, sino las **relaciones** entre ellas usando herencia de clases.

—Los incas —dijo Wayra— no veían el mundo como objetos aislados. Lo veían como una red de relaciones. El Inca era la clase padre. Los curacas (gobernantes locales) heredaban sus atributos. Y los hatun runas (pueblo) heredaban de los curacas. Todo era una cadena de herencia.

—¿Y cómo se traduce eso a Python? —preguntó Raúl.

—Con **herencia de clases**. Una clase puede heredar atributos y métodos de otra clase. Como un hijo hereda características de sus padres.

## Herencia: El árbol genealógico del código

```python
# ============================================
# HERENCIA: EL ÁRBOL DEL CONOCIMIENTO
# ============================================

# Clase padre (base)
class Persona:
    """Clase base para todas las personas en el sistema."""
    
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self._vivo = True  # Privado por convención
    
    def presentarse(self):
        return f"Soy {self.nombre}, de {self.edad} años."
    
    def esta_vivo(self):
        return self._vivo
    
    def morir(self):
        self._vivo = False
        print(f"  {self.nombre} ha fallecido.")

# Clase hija: Sospechoso
class Sospechoso(Persona):
    """Un sospechoso es una Persona con características adicionales."""
    
    def __init__(self, nombre, edad, dni, motivo=""):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, dni)
        
        # Atributos específicos del sospechoso
        self.motivo = motivo
        self.nivel_sospecha = 0
        self.coartada = ""
    
    def agregar_evidencia(self, peso):
        """Agrega peso a la sospecha."""
        self.nivel_sospecha += peso
    
    def presentarse(self):  # POLIMORFISMO: mismo método, diferente comportamiento
        presentacion_base = super().presentarse()
        return f"{presentacion_base} | SOSPECHOSO - Motivo: {self.motivo}"

# Clase hija: Investigador
class Investigador(Persona):
    """Un investigador es una Persona con credenciales."""
    
    def __init__(self, nombre, edad, dni, placa, rango):
        super().__init__(nombre, edad, dni)
        self.placa = placa
        self.rango = rango
        self.casos_asignados = []
    
    def asignar_caso(self, caso):
        self.casos_asignados.append(caso)
    
    def presentarse(self):  # POLIMORFISMO
        return f"{super().presentarse()} | INVESTIGADOR - Placa: {self.placa}"

# Crear instancias
print("=== HERENCIA EN ACCIÓN ===\n")

sospechoso1 = Sospechoso("Lara Mamani", 32, "DNI-47291", "Económico/Emocional")
investigador1 = Investigador("Wayra Condori", 28, "DNI-83921", "PI-007", "Analista Senior")

print(sospechoso1.presentarse())
print(investigador1.presentarse())
print(f"¿{sospechoso1.nombre} está vivo? {sospechoso1.esta_vivo()}")
print(f"¿{investigador1.nombre} está vivo? {investigador1.esta_vivo()}")
```

### El polimorfismo en acción

El **polimorfismo** permite que diferentes clases tengan métodos con el mismo nombre pero comportamientos diferentes:

```python
print("\n=== POLIMORFISMO: Mismo mensaje, diferente respuesta ===\n")

personas = [
    Sospechoso("Carlos Huamán", 55, "DNI-56123", "Envidia profesional"),
    Investigador("Raúl Cusi", 35, "DNI-78234", "PER-023", "Periodista"),
    Sospechoso("Mama Killa", 70, "DNI-34567", "Secreto familiar"),
    Investigador("Wayra Condori", 28, "DNI-83921", "PI-007", "Analista Senior"),
]

for persona in personas:
    # Cada objeto responde según su clase
    print(persona.presentarse())
    # También podemos verificar el tipo
    if isinstance(persona, Sospechoso):
        print(f"  → Nivel de sospecha: {persona.nivel_sospecha}")
    elif isinstance(persona, Investigador):
        print(f"  → Casos asignados: {len(persona.casos_asignados)}")
    print()
```

## Herencia múltiple: El mestizaje del código

Python permite que una clase herede de múltiples clases padre. Como el mestizaje cultural andino:

```python
# ============================================
# HERENCIA MÚLTIPLE
# ============================================

class GuardiánDeTradición:
    """Mixin: conocimientos ancestrales."""
    
    def __init__(self, tradiciones_conocidas=None):
        self.tradiciones = tradiciones_conocidas or []
    
    def enseñar_tradición(self):
        return f"Enseñando: {', '.join(self.tradiciones)}"

class ExpertoEnTecnología:
    """Mixin: conocimientos tecnológicos."""
    
    def __init__(self, tecnologias=None):
        self.tecnologias = tecnologias or []
    
    def programar(self, lenguaje):
        return f"Programando en {lenguaje}"

# Herencia múltiple
class QuipucamayocDigital(GuardiánDeTradición, ExpertoEnTecnología):
    """Un Quipucamayoc Digital combina tradición y tecnología."""
    
    def __init__(self, nombre, tradiciones, tecnologias, nivel_maestria):
        GuardiánDeTradición.__init__(self, tradiciones)
        ExpertoEnTecnología.__init__(self, tecnologias)
        self.nombre = nombre
        self.nivel_maestria = nivel_maestria
    
    def descifrar_quipu(self, quipu):
        return f"Descifrando {quipu} con sabiduría ancestral y tecnología moderna"

# Crear un Quipucamayoc Digital
inti = QuipucamayocDigital(
    "Inti Quispe",
    ["quipus", "tejido andino", "medicina ancestral", "calendario inca"],
    ["Python", "Machine Learning", "Computación Cuántica", "Blockchain"],
    10  # Máximo nivel
)

print("\n=== QUIPUCAMAYOC DIGITAL ===\n")
print(f"Nombre: {inti.nombre}")
print(f"Nivel de maestría: {inti.nivel_maestria}/10")
print(f"Tradiciones: {', '.join(inti.tradiciones)}")
print(f"Tecnologías: {', '.join(inti.tecnologias)}")
print(inti.enseñar_tradición())
print(inti.programar("Python"))
print(inti.descifrar_quipu("BLANCO:1:3:5:7:9"))
```

## Encapsulación: Secretos protegidos

La **encapsulación** protege los datos internos de un objeto. En Python, se hace con convenciones:

- `_atributo`: privado por convención (no deberías tocarlo)
- `__atributo`: name mangling (Python lo ofusca)

```python
class SecretoFamiliar:
    """Un secreto que no debe ser revelado fácilmente."""
    
    def __init__(self, contenido, nivel_clasificacion):
        self._contenido = contenido  # Privado por convención
        self.__nivel = nivel_clasificacion  # Name mangling
        self.publico = True
    
    def obtener_secreto(self, clave):
        """Solo accesible con la clave correcta."""
        if clave == "YACHAY_ACCESS":
            return f"Secreto (nivel {self.__nivel}): {self._contenido}"
        return "🔒 Acceso denegado"
    
    def _metodo_interno(self):
        """Método 'privado' para uso interno."""
        return "Este método no debería llamarse desde fuera"

# Uso de encapsulación
secreto = SecretoFamiliar("Lara es hija de Rodrigo Mamani", 7)

print("\n=== ENCAPSULACIÓN ===")
print(f"Atributo público: {secreto.publico}")
print(f"Atributo 'privado': {secreto._contenido}")  # Accesible pero no recomendado
# print(secreto.__nivel)  # Error! Name mangling lo ofusca
print(f"Name mangling: {secreto._SecretoFamiliar__nivel}")  # Forma ofuscada
print(secreto.obtener_secreto("clave_incorrecta"))
print(secreto.obtener_secreto("YACHAY_ACCESS"))
```

## El modelo completo de Yachay

Wayra reconstruyó el modelo de clases que Inti había creado para representar el caso:

```python
# ============================================
# MODELO COMPLETO DE YACHAY
# ============================================

class EntidadYachay:
    """Clase base de todo en Yachay."""
    def __init__(self, id_entidad):
        self.id = id_entidad
        self.fecha_creacion = "27/06/2026"

class Persona(EntidadYachay):
    def __init__(self, id_entidad, nombre, edad):
        super().__init__(id_entidad)
        self.nombre = nombre
        self.edad = edad
        self._secretos = []
    
    def agregar_secreto(self, secreto):
        self._secretos.append(secreto)
    
    def presentarse(self):
        return f"{self.nombre}, {self.edad} años"

class MiembroLaboratorio(Persona):
    def __init__(self, id_entidad, nombre, edad, rol, nivel_acceso):
        super().__init__(id_entidad, nombre, edad)
        self.rol = rol
        self.nivel_acceso = nivel_acceso
        self.registros_acceso = []
    
    def registrar_acceso(self, hora, tipo):
        self.registros_acceso.append({"hora": hora, "tipo": tipo})
        print(f"  🕐 {self.nombre}: {tipo} a las {hora}")

class Sospechoso(MiembroLaboratorio):
    def __init__(self, id_entidad, nombre, edad, rol, nivel_acceso, motivo):
        super().__init__(id_entidad, nombre, edad, rol, nivel_acceso)
        self.motivo = motivo
        self.coartada_verificada = False
    
    def verificar_coartada(self):
        self.coartada_verificada = True
        return f"Coartada de {self.nombre} verificada"

# Construir el modelo del caso
print("\n=== MODELO COMPLETO DEL CASO ===\n")

lara_model = Sospechoso("P002", "Lara Mamani", 32, "Asistente", 7, "Hija de Rodrigo")
lara_model.agregar_secreto("Trabaja para su padre")
lara_model.registrar_acceso("08:15", "entrada")
lara_model.registrar_acceso("02:34", "entrada (fraudulenta)")

carlos_model = Sospechoso("P003", "Carlos Huamán", 55, "Colega", 5, "Envidia")
carlos_model.agregar_secreto("Saboteó publicación de Inti")
carlos_model.registrar_acceso("09:00", "entrada")
carlos_model.registrar_acceso("14:00", "salida")

print(f"\n{lara_model.presentarse()} - Rol: {lara_model.rol}")
print(f"{carlos_model.presentarse()} - Rol: {carlos_model.rol}")
```

## El polimorfismo que reveló al asesino

Wayra escribió un método que procesaba a todos los implicados de la misma forma, pero cada uno respondía según su tipo:

```python
print("\n=== ANÁLISIS POLIMÓRFICO DE IMPLICADOS ===\n")

implicados = [
    lara_model,
    carlos_model,
    Persona("P001", "Inti Quispe", 67),
    MiembroLaboratorio("P004", "Sarah Chen", 40, "Colaboradora", 6),
]

for implicado in implicados:
    print(f"▶ {implicado.presentarse()}")
    
    # Comportamiento según el tipo real
    if hasattr(implicado, "verificar_coartada"):
        print(f"  → Sospechoso: {implicado.verificar_coartada()}")
    
    if hasattr(implicado, "registros_acceso") and implicado.registros_acceso:
        ultimo = implicado.registros_acceso[-1]
        print(f"  → Último acceso: {ultimo['tipo']} a las {ultimo['hora']}")
    
    if hasattr(implicado, "_secretos") and implicado._secretos:
        print(f"  → Tiene secretos: {len(implicado._secretos)}")
    
    print()
```

Wayra se detuvo. Había una relación que no había explorado: la herencia entre Lara y Rodrigo. Si Rodrigo era el padre de Lara, entonces Lara heredaba algo más que genes: heredaba la ambición, la conexión con Los Herederos, y posiblemente, la misión de eliminar a Inti.

—Pero eso no convierte a Lara en asesina —dijo Wayra—. La convierte en una pieza. La pregunta es: ¿quién movió la pieza?

## Enigmas

### Enigma 12.1: Jerarquía de clases

Crea una jerarquía de 3 niveles:
- `Caso` (clase base): atributo `nombre_caso`
- `CasoHomicidio` (hereda de `Caso`): atributo `victima`
- `CasoHomicidioCerrado` (hereda de `CasoHomicidio`): atributo `culpable`

Crea una instancia de cada una y muestra sus atributos.

### Enigma 12.2: Polimorfismo con animales

Crea las clases `Animal`, `Perro` y `Gato`. Todas tienen el método `hacer_sonido()`. Perro devuelve "Guau", Gato devuelve "Miau". Crea una lista de animales y llama a `hacer_sonido()` para cada uno.

### Enigma 12.3: Herencia con super()

Crea las clases:
- `EvidenciaBase` con atributo `id` y método `info()`
- `EvidenciaDigital` que hereda de `EvidenciaBase`, agrega `tipo_archivo`, y usa `super()` en `__init__`

### Enigma 12.4: Encapsulación bancaria

Crea una clase `CuentaBancaria` con:
- Atributo privado `__saldo`
- Método público `depositar(monto)`
- Método público `retirar(monto)` (solo si hay saldo suficiente)
- Método público `consultar_saldo()` (que muestra el saldo)

---

## Lo que aprendiste

- La **herencia** permite que una clase herede atributos y métodos de otra
- `class Hijo(Padre):` define herencia
- `super().__init__()` llama al constructor de la clase padre
- El **polimorfismo** permite que diferentes clases respondan al mismo método de forma distinta
- `isinstance(objeto, Clase)` verifica el tipo de un objeto
- La **herencia múltiple** permite heredar de varias clases
- La **encapsulación** protege datos: `_` (convención), `__` (name mangling)
- La POO permite modelar relaciones complejas del mundo real

Wayra cerró el archivo. El modelo de clases de Inti era hermoso y aterrador. Cada persona en el caso era un objeto con atributos y métodos. Cada relación era una herencia o una conexión.

—Necesito ejecutar el modelo completo —dijo—. Necesito que Yachay procese todos los datos y me muestre quién es el asesino según su propio análisis.

—¿Y si Yachay no quiere decírtelo? —preguntó Raúl.

—Entonces lo forzaremos. Pero no con errores esta vez. Con un proyecto completo. Con el **Código Asesino**.

Wayra abrió un nuevo archivo en su editor. Era hora de escribir el programa final. El que integraría todo lo aprendido: variables, strings, listas, diccionarios, condicionales, bucles, funciones, archivos, errores, módulos, POO y herencia.

El programa que revelaría al asesino.

---
