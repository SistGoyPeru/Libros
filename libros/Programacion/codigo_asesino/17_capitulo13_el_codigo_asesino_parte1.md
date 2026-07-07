# Capítulo 13: El Código Asesino — Primera Parte

## Proyecto Integrador: Reconstrucción forense digital con Python

---

La luz del amanecer teñía de dorado las piedras del Coricancha cuando Wayra tomó una decisión. Había aprendido lo suficiente. Tenía las herramientas. Ahora era el momento de construir el programa que resolvería el caso.

—Voy a escribir el Código Asesino —dijo—. Un programa completo que integre todo lo que hemos aprendido. Que procese los datos del caso, analice a los sospechosos, descifre los quipus y... identifique al culpable.

—¿Y si el programa se equivoca? —preguntó Raúl.

—Los programas no se equivocan. Nosotros nos equivocamos al programarlos. Pero siInti dejó las pistas correctas, y si yo las interpreté bien, el programa mostrará la verdad.

Wayra abrió su editor. Era el momento de escribir el proyecto final.

---

## Estructura del proyecto

El Código Asesino tendrá varios módulos, cada uno construido sobre lo aprendido en los capítulos anteriores:

```
codigo_asesino/
├── __init__.py
├── datos_caso.py        # Datos del caso (variables, listas, dicts)
├── quipus.py            # Procesamiento de quipus (strings, slicing)
├── sospechosos.py       # Análisis de sospechosos (POO, herencia)
├── evidencias.py        # Gestión de evidencias (archivos, errores)
├── analisis.py          # Motor de análisis (condicionales, bucles, funciones)
└── main.py              # Punto de entrada principal
```

### Módulo 1: `datos_caso.py` — La información del caso

```python
# ============================================
# MÓDULO: datos_caso.py
# CONTIENE: Datos estructurados del caso
# CONCEPTOS: variables, listas, diccionarios
# ============================================

# --- DATOS GENERALES DEL CASO ---

nombre_caso = "El Asesinato del Dr. Inti Quispe"
fecha_crimen = "27 de junio, 2026"
lugar_crimen = "Templo del Sol (Coricancha), Neo-Cusco"
hora_crimen = "02:34"
investigadora = "Wayra Condori"

# --- QUIPUS DIGITALES ENCONTRADOS ---

quipus_del_caso = [
    {"id": "Q001", "color": "rojo", "nudos": [1, 4, 9], 
     "significado": "conflicto/guerra"},
    {"id": "Q002", "color": "verde", "nudos": [2, 5, 10], 
     "significado": "crecimiento/conocimiento"},
    {"id": "Q003", "color": "azul", "nudos": [1, 5, 9], 
     "significado": "espiritualidad/religión"},
    {"id": "Q004", "color": "amarillo", "nudos": [3, 7, 11], 
     "significado": "poder/riqueza"},
    {"id": "Q005", "color": "blanco", "nudos": [1, 3, 5, 7, 9, 11], 
     "significado": "verdad/conexión espiritual"}
]

# --- SOSPECHOSOS CON DATOS COMPLETOS ---

sospechosos_data = {
    "Lara Mamani": {
        "edad": 32, "rol": "Asistente de laboratorio",
        "acceso_lab": True, "nivel_acceso": 7,
        "coartada": "Departamento propio",
        "coartada_valida": False,
        "motivo": "Económico/Emocional (hija de Rodrigo)",
        "intensidad_motivo": 8,
        "huellas_escena": True,
        "evidencias": [
            "Registro de acceso a las 02:34",
            "Huellas en el teclado de Inti",
            "Hija secreta de Rodrigo Mamani",
            "Llamada perdida de Inti a las 02:30"
        ]
    },
    "Dr. Carlos Huamán": {
        "edad": 55, "rol": "Colega universitario",
        "acceso_lab": True, "nivel_acceso": 5,
        "coartada": "Oficina universitaria (no verificada)",
        "coartada_valida": False,
        "motivo": "Envidia profesional",
        "intensidad_motivo": 7,
        "huellas_escena": False,
        "evidencias": [
            "Discusión pública con Inti días antes",
            "Publicación bloqueada por Inti en 2024",
            "Correos amenazantes (no probados)"
        ]
    },
    "Dra. Sarah Chen": {
        "edad": 40, "rol": "Colaboradora del MIT",
        "acceso_lab": True, "nivel_acceso": 6,
        "coartada": "Videollamada con MIT (02:00-03:30)",
        "coartada_valida": True,
        "motivo": "Presión académica",
        "intensidad_motivo": 5,
        "huellas_escena": False,
        "evidencias": [
            "Presión del MIT por obtener resultados",
            "Visa académica próxima a vencer",
            "Oferta de NeuralCorp por Yachay"
        ]
    },
    "Rodrigo Mamani": {
        "edad": 60, "rol": "Empresario tecnológico",
        "acceso_lab": False, "nivel_acceso": 3,
        "coartada": "Cena de negocios (Hotel Monasterio)",
        "coartada_valida": True,
        "motivo": "Control de Yachay",
        "intensidad_motivo": 10,
        "huellas_escena": False,
        "evidencias": [
            "Líder de Los Herederos de Pizarro",
            "Padre secreto de Lara Mamani",
            "Ofertas de compra rechazadas por Inti",
            "Conexiones con NeuralCorp Andina"
        ]
    },
    "Mama Killa": {
        "edad": 70, "rol": "Hermana de Inti",
        "acceso_lab": True, "nivel_acceso": 9,
        "coartada": "Su casa en San Blas",
        "coartada_valida": False,
        "motivo": "Protección del legado familiar",
        "intensidad_motivo": 6,
        "huellas_escena": True,
        "evidencias": [
            "Miembro del Círculo del Sol",
            "Conocía el pasaje secreto",
            "Mensaje de Inti: 'Mama Killa sabe la verdad'",
            "Depositó algo en el banco el 26/06"
        ]
    }
}

# --- REGISTRO DE ACCESOS ---

registro_accesos = [
    {"persona": "Lara", "hora": "08:15", "tipo": "entrada"},
    {"persona": "Inti", "hora": "08:30", "tipo": "entrada"},
    {"persona": "Carlos", "hora": "09:00", "tipo": "entrada"},
    {"persona": "Lara", "hora": "12:30", "tipo": "salida"},
    {"persona": "Lara", "hora": "13:30", "tipo": "entrada"},
    {"persona": "Carlos", "hora": "14:00", "tipo": "salida"},
    {"persona": "Sarah", "hora": "14:30", "tipo": "entrada"},
    {"persona": "Sarah", "hora": "16:00", "tipo": "salida"},
    {"persona": "Inti", "hora": "18:00", "tipo": "salida"},
    {"persona": "Inti", "hora": "22:00", "tipo": "entrada"},
    {"persona": "Lara", "hora": "02:34", "tipo": "entrada"},  # ¿Fraudulento?
    {"persona": "Lara", "hora": "02:45", "tipo": "salida"},   # ¿Fraudulento?
]
```

Wayra guardó el módulo. —Los datos están listos. Ahora necesito las herramientas para procesarlos.

### Módulo 2: `quipus.py` — Decodificando los mensajes

```python
# ============================================
# MÓDULO: quipus.py
# CONTIENE: Funciones para procesar quipus digitales
# CONCEPTOS: strings, slicing, listas, funciones
# ============================================

def decodificar_quipu(quipu):
    """Decodifica un quipu digital y devuelve su mensaje."""
    color = quipu["color"]
    nudos = quipu["nudos"]
    significado = quipu["significado"]
    
    # Analizar patrón de nudos
    if all(n % 2 == 1 for n in nudos):
        tipo = "PREGUNTA"
    elif all(n % 2 == 0 for n in nudos):
        tipo = "RESPUESTA"
    else:
        tipo = "MENSAJE MIXTO"
    
    # Calcular la diferencia entre nudos
    if len(nudos) >= 2:
        diferencias = [nudos[i+1] - nudos[i] for i in range(len(nudos)-1)]
        patron = diferencias[0] if len(set(diferencias)) == 1 else "variable"
    else:
        patron = "único"
    
    return {
        "color": color,
        "significado": significado,
        "tipo": tipo,
        "total_nudos": len(nudos),
        "posiciones": nudos,
        "patron": patron,
        "mensaje_decodificado": f"{color.upper()}: {significado} ({tipo})"
    }

def decodificar_todos_los_quipus(lista_quipus):
    """Decodifica todos los quipus de una lista."""
    resultados = []
    for quipu in lista_quipus:
        resultado = decodificar_quipu(quipu)
        resultados.append(resultado)
    return resultados

def buscar_quipu_por_color(lista_quipus, color):
    """Busca quipus por color."""
    return [q for q in lista_quipus if q["color"] == color]

def quipu_a_string(quipu):
    """Convierte un quipu decodificado a string formateado."""
    return (f"  [{quipu['color'].upper():8}] {quipu['significado']:30} "
            f"| {quipu['tipo']:15} | {quipu['total_nudos']} nudos")
```

### Módulo 3: `sospechosos.py` — Modelando a los implicados

```python
# ============================================
# MÓDULO: sospechosos.py
# CONTIENE: Clases para modelar a los implicados
# CONCEPTOS: POO, clases, herencia, encapsulación
# ============================================

class Persona:
    """Clase base para todas las personas del caso."""
    
    def __init__(self, nombre, edad, rol):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
    
    def presentarse(self):
        return f"{self.nombre} ({self.edad}), {self.rol}"


class Sospechoso(Persona):
    """Modela un sospechoso con todas sus características."""
    
    def __init__(self, nombre, edad, rol, datos):
        super().__init__(nombre, edad, rol)
        self.acceso_lab = datos.get("acceso_lab", False)
        self.nivel_acceso = datos.get("nivel_acceso", 0)
        self.coartada = datos.get("coartada", "")
        self.coartada_valida = datos.get("coartada_valida", False)
        self.motivo = datos.get("motivo", "")
        self.intensidad_motivo = datos.get("intensidad_motivo", 0)
        self.huellas_escena = datos.get("huellas_escena", False)
        self.evidencias = datos.get("evidencias", [])
        self._puntaje_sospecha = 0  # Encapsulado
    
    def calcular_puntaje(self):
        """Calcula el puntaje de sospecha basado en múltiples factores."""
        puntaje = 0
        
        # Factor 1: Acceso al laboratorio
        if self.acceso_lab:
            puntaje += 3 * (self.nivel_acceso / 10)
        
        # Factor 2: Coartada
        if not self.coartada_valida:
            puntaje += 4
        
        # Factor 3: Intensidad del motivo
        puntaje += self.intensidad_motivo * 0.5
        
        # Factor 4: Huellas en la escena
        if self.huellas_escena:
            puntaje += 2
        
        # Factor 5: Evidencias
        puntaje += len(self.evidencias) * 0.5
        
        self._puntaje_sospecha = min(puntaje, 10)
        return self._puntaje_sospecha
    
    def obtener_categoria(self):
        """Devuelve la categoría según el puntaje."""
        if self._puntaje_sospecha >= 8:
            return "CRÍTICO"
        elif self._puntaje_sospecha >= 6:
            return "ALTO"
        elif self._puntaje_sospecha >= 4:
            return "MODERADO"
        else:
            return "BAJO"
    
    def reporte(self):
        """Genera un reporte completo del sospechoso."""
        self.calcular_puntaje()
        categoria = self.obtener_categoria()
        
        return {
            "nombre": self.nombre,
            "puntaje": self._puntaje_sospecha,
            "categoria": categoria,
            "evidencias": self.evidencias,
            "motivo": self.motivo
        }
```

---

Wayra había construido los cimientos. Pero aún necesitaba el motor de análisis que conectara todo.

—Raúl —dijo—. Dame una hora más. El Código Asesino está tomando forma. Pero la parte más importante aún viene: el análisis que conecta todos los datos y revela la verdad.

—¿Y mientras tanto?

—Mientras tanto, revisa estos quipus descifrados. Busca patrones. Busca algo que no encaje.

Raúl tomó la lista de quipus decodificados y comenzó a estudiarlos. Wayra, por su parte, siguió escribiendo.

## Enigmas

### Enigma 13.1: Extiende el módulo datos_caso.py

Agrega un nuevo quipus al caso: uno de color "negro" con nudos en posiciones [2, 4, 8] y significado "muerte/desconocido". Luego actualiza la lista `quipus_del_caso`.

### Enigma 13.2: Prueba la decodificación

Usa el módulo `quipus.py` para decodificar todos los quipus del caso. ¿Qué patrón encuentras en el quipu blanco?

### Enigma 13.3: Crea un Sospechoso desde datos

Usando la clase `Sospechoso` y los datos de `sospechosos_data`, crea el objeto para "Lara Mamani", calcula su puntaje y muestra su reporte.

### Enigma 13.4: El quipu blanco

Ejecuta `decodificar_quipu` en el quipu blanco (Q005). ¿Qué tipo de mensaje es? ¿Por qué Inti le dio 6 nudos?

---

## Lo que aprendiste (hasta ahora en el proyecto)

- Cómo **estructurar** un proyecto Python en múltiples módulos
- Cómo separar **datos** de **lógica** en archivos distintos
- Cómo usar **diccionarios anidados** para modelar datos complejos
- Cómo crear **funciones reutilizables** para procesamiento
- Cómo usar **POO** para modelar entidades del mundo real
- Cómo aplicar **herencia** para crear jerarquías de clases

Wayra guardó los módulos y tomó un respiro profundo. La primera parte del Código Asesino estaba completa. Pero la parte más importante —el análisis que determinaría al culpable— aún estaba por escribir.

—Raúl —llamó—. ¿Encontraste algo en los quipus?

—Sí —respondió Raúl, con el ceño fruncido—. El quipu blanco tiene 6 nudos. Pero los otros tienen 3. ¿Por qué el blanco tiene el doble?

—Porque el blanco es la clave. Los 6 nudos representan las 6 personas involucradas. Y las posiciones... las posiciones son edades. O niveles de acceso. O algo que aún no hemos visto.

Wayra miró el código que había escrito. Faltaba el módulo de análisis. El que usaría condicionales, bucles y funciones para procesar todos los datos y señalar al culpable.

—Voy a escribir el motor de análisis —dijo—. Y cuando termine, ejecutaremos el programa. Y sabremos la verdad.

---
