# Capítulo 8: Guardando el Progreso

## Almacenamiento (localStorage)

---

—Hay un problema —dijo Camila—. Los usuarios pierden su progreso cuando cierran el navegador.

—Exacto —dijo Diego—. Cada vez que recargan la página, todo vuelve a cero. Necesitamos **almacenamiento local**.

---

## ¿Qué es localStorage?

**localStorage** es una API del navegador que permite guardar datos en el equipo del usuario. Los datos persisten incluso después de cerrar el navegador.

Características principales:

- Capacidad: ~5MB por dominio
- Solo guarda **strings**
- Los datos no expiran (a menos que se borren manualmente)
- Especificidad por dominio (cada sitio web tiene su propio localStorage)

---

## Métodos de localStorage

### setItem: guardar datos

```javascript
// Guardar un valor
localStorage.setItem("nombre", "Camila Ríos");
localStorage.setItem("edad", "27");

// Los valores siempre deben ser strings
```

### getItem: recuperar datos

```javascript
const nombre = localStorage.getItem("nombre");
console.log(nombre); // "Camila Ríos"

const edad = localStorage.getItem("edad");
console.log(edad); // "27" (string)

const inexistente = localStorage.getItem("noExiste");
console.log(inexistente); // null
```

### removeItem: eliminar un dato

```javascript
localStorage.removeItem("edad");
```

### clear: limpiar todo

```javascript
localStorage.clear(); // Elimina todo el localStorage del dominio
```

---

## Guardando objetos en localStorage

—localStorage solo guarda strings. Para guardar objetos, usamos **JSON.stringify** y **JSON.parse**.

```javascript
const usuario = {
  nombre: "Camila Ríos",
  email: "camila@aprendeya.com",
  edad: 27,
  cursos: ["HTML Básico", "JavaScript Básico"]
};

// Guardar objeto (convertir a JSON string)
localStorage.setItem("usuario", JSON.stringify(usuario));

// Recuperar objeto (convertir de JSON string)
const usuarioGuardado = JSON.parse(localStorage.getItem("usuario"));
console.log(usuarioGuardado.nombre); // "Camila Ríos"
console.log(usuarioGuardado.cursos[0]); // "HTML Básico"
```

---

## Ejemplo práctico: progreso del curso

Camila implementó el seguimiento de progreso:

```javascript
// Estado inicial
let progreso = {
  leccionesCompletadas: [],
  ultimoAcceso: null,
  cursoActual: null
};

// Cargar progreso guardado
function cargarProgreso() {
  const guardado = localStorage.getItem("progreso");
  if (guardado) {
    progreso = JSON.parse(guardado);
    console.log("Progreso cargado:", progreso);
  }
}

// Guardar progreso
function guardarProgreso() {
  progreso.ultimoAcceso = new Date().toISOString();
  localStorage.setItem("progreso", JSON.stringify(progreso));
  console.log("Progreso guardado");
}

// Completar una lección
function completarLeccion(idLeccion) {
  if (!progreso.leccionesCompletadas.includes(idLeccion)) {
    progreso.leccionesCompletadas.push(idLeccion);
    guardarProgreso();
    actualizarUI();
  }
}

// Actualizar la interfaz
function actualizarUI() {
  const contador = document.querySelector("#contador-lecciones");
  contador.textContent = `Lecciones completadas: ${progreso.leccionesCompletadas.length}`;
}

// Inicializar
cargarProgreso();
actualizarUI();
```

---

## sessionStorage

—Hay un hermano de localStorage llamado **sessionStorage**. Funciona igual, pero los datos se borran cuando se cierra la pestaña.

```javascript
// Guardar en sessionStorage (temporal)
sessionStorage.setItem("carrito", JSON.stringify(["Curso JS", "Curso HTML"]));

// sessionStorage se borra al cerrar la pestaña
// localStorage persiste hasta que se borre manualmente
```

| Característica | localStorage | sessionStorage |
|---------------|--------------|----------------|
| Persistencia | Hasta borrado manual | Hasta cerrar pestaña |
| Capacidad | ~5MB | ~5MB |
| Compartido entre pestañas | Sí | No |
| Uso típico | Preferencias, progreso | Datos temporales, carrito |

---

## Cookies

—Las **cookies** son otra forma de almacenar datos, pero más antiguas y con más limitaciones. Se envían al servidor en cada petición.

```javascript
// Crear una cookie (expira en 7 días)
document.cookie = "nombre=Camila; max-age=" + (7 * 24 * 60 * 60);

// Leer cookies
console.log(document.cookie);

// Eliminar cookie (max-age negativo)
document.cookie = "nombre=; max-age=0";
```

—Para la mayoría de casos, usa `localStorage` —dijo Diego—. Es más simple y no ralentiza las peticiones al servidor.

---

## Aplicación en la plataforma

Camila integró localStorage en la plataforma:

```javascript
// ===== MÓDULO DE ALMACENAMIENTO =====

const Almacenamiento = {
  // Guardar datos del usuario al registrarse
  guardarUsuario(datos) {
    const usuarios = this.obtenerUsuarios();
    datos.id = Date.now();
    usuarios.push(datos);
    localStorage.setItem("usuarios", JSON.stringify(usuarios));
    return datos;
  },

  // Obtener todos los usuarios
  obtenerUsuarios() {
    const datos = localStorage.getItem("usuarios");
    return datos ? JSON.parse(datos) : [];
  },

  // Guardar preferencias
  guardarPreferencias(prefs) {
    localStorage.setItem("preferencias", JSON.stringify(prefs));
  },

  // Obtener preferencias
  obtenerPreferencias() {
    const datos = localStorage.getItem("preferencias");
    return datos ? JSON.parse(datos) : { modoOscuro: false, idioma: "es" };
  },

  // Guardar progreso de un curso
  guardarProgresoCurso(cursoId, leccionId, completado) {
    const progresos = this.obtenerProgresos();
    if (!progresos[cursoId]) progresos[cursoId] = {};
    progresos[cursoId][leccionId] = completado;
    localStorage.setItem("progresos", JSON.stringify(progresos));
  },

  // Obtener todos los progresos
  obtenerProgresos() {
    const datos = localStorage.getItem("progresos");
    return datos ? JSON.parse(datos) : {};
  },

  // Calcular porcentaje de un curso
  obtenerPorcentajeCurso(cursoId, totalLecciones) {
    const progresos = this.obtenerProgresos();
    const curso = progresos[cursoId];
    if (!curso) return 0;
    const completadas = Object.values(curso).filter(v => v).length;
    return Math.round((completadas / totalLecciones) * 100);
  }
};

// ===== USO =====

// Al registrarse
formulario.addEventListener("submit", function(event) {
  event.preventDefault();
  const datos = {
    nombre: document.querySelector("#nombre").value,
    email: document.querySelector("#email").value
  };
  Almacenamiento.guardarUsuario(datos);
  console.log("Usuario registrado y guardado!");
});

// Al completar una lección
function marcarCompletada(leccionId) {
  Almacenamiento.guardarProgresoCurso("js-basico", leccionId, true);
  const porcentaje = Almacenamiento.obtenerPorcentajeCurso("js-basico", 15);
  document.querySelector("#progreso").style.width = porcentaje + "%";
  document.querySelector("#porcentaje-texto").textContent = `${porcentaje}%`;
}
```

---

## Enigmas del Capítulo 8

### Enigma 8.1: Contador de visitas

Crea un script que muestre cuántas veces has visitado una página. Usa localStorage para almacenar el contador. Cada vez que cargues la página, incrementa el contador y muéstralo.

### Enigma 8.2: Tema persistente

Crea un botón que alterne entre modo claro y modo oscuro. Guarda la preferencia en localStorage. Al recargar la página, debe mantener la última selección.

### Enigma 8.3: Lista de favoritos

Crea una página con una lista de cursos y un botón "Favorito" en cada uno. Al hacer clic, guarda el curso en una lista de favoritos en localStorage. Muestra la lista en una sección separada.

### Enigma 8.4: Notas persistentes

Crea un textarea donde el usuario pueda escribir notas. Cada vez que se escriba (evento input), guarda el contenido en localStorage. Al recargar la página, el contenido debe aparecer automáticamente.

---

## Lo que aprendiste

- **localStorage**: almacenamiento persistente en el navegador
- **sessionStorage**: almacenamiento temporal (hasta cerrar pestaña)
- Métodos: `setItem`, `getItem`, `removeItem`, `clear`
- **JSON.stringify** y **JSON.parse**: convertir objetos a/desde strings
- Las **cookies** existen pero son menos recomendadas para almacenamiento local
- localStorage es ideal para preferencias, progreso y datos de sesión

---

Camila recargó la página. El progreso seguía ahí. Cerró el navegador, lo volvió a abrir, y el contador de lecciones completadas seguía intacto.

—Es como si la página tuviera memoria —dijo, maravillada.

—Eso es exactamente —respondió Diego—. Y mañana vamos a conectarla con el mundo exterior.
