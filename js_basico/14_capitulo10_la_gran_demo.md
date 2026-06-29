# Capítulo 10: La Gran Demo

## Proyecto Final

---

Era el día de la demo. El sol entraba por las ventanas del piso 14, iluminando la sala de reuniones donde los inversores esperaban. Camila había dormido apenas cuatro horas. Pero su código estaba listo.

—¿Preparada? —preguntó Diego.

Camila asintió. Abrió su laptop y mostró la pantalla: la plataforma "AprendeYa" versión interactiva.

—Señores inversores —comenzó—, les presento el futuro de la educación online.

---

## Proyecto: Mini Plataforma Educativa

Vamos a construir lo mismo que Camila presentó: una mini plataforma educativa con:

1. Login simulado
2. Catálogo de cursos dinámico
3. Seguimiento de progreso
4. Persistencia de datos

### Estructura HTML

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AprendeYa - Plataforma Educativa</title>
  <link rel="stylesheet" href="estilo.css">
</head>
<body>
  <header>
    <div class="logo">AprendeYa</div>
    <nav id="nav-principal">
      <a href="#" data-seccion="cursos">Cursos</a>
      <a href="#" data-seccion="progreso">Mi Progreso</a>
      <a href="#" data-seccion="perfil">Perfil</a>
    </nav>
    <button id="btn-login" class="btn">Iniciar Sesión</button>
    <button id="btn-logout" class="btn oculto">Cerrar Sesión</button>
  </header>

  <main>
    <!-- Sección de Login -->
    <section id="seccion-login" class="seccion">
      <div class="login-card">
        <h2>Iniciar Sesión</h2>
        <form id="form-login">
          <input type="text" id="login-nombre" placeholder="Nombre" required>
          <input type="email" id="login-email" placeholder="Email" required>
          <button type="submit" class="btn btn-primary">Entrar</button>
        </form>
        <p id="login-error" class="error-mensaje"></p>
      </div>
    </section>

    <!-- Sección de Cursos -->
    <section id="seccion-cursos" class="seccion">
      <h2>Cursos Disponibles</h2>
      <div id="loader" class="loader oculto">Cargando cursos...</div>
      <div id="cursos-container" class="grid-cursos"></div>
    </section>

    <!-- Sección de Progreso -->
    <section id="seccion-progreso" class="seccion oculto">
      <h2>Mi Progreso</h2>
      <div id="progreso-container"></div>
    </section>

    <!-- Sección de Perfil -->
    <section id="seccion-perfil" class="seccion oculto">
      <h2>Perfil de Usuario</h2>
      <div id="perfil-container"></div>
    </section>
  </main>

  <script src="app.js"></script>
</body>
</html>
```

### JavaScript completo

```javascript
// ==========================================
// MÓDULO DE AUTENTICACIÓN
// ==========================================
const Auth = {
  usuarioActual: null,

  init() {
    this.usuarioActual = JSON.parse(localStorage.getItem("usuarioActual"));
    if (this.usuarioActual) {
      UI.mostrarDashboard();
    }
    this.configurarEventos();
  },

  configurarEventos() {
    const form = document.querySelector("#form-login");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      this.iniciarSesion();
    });

    document.querySelector("#btn-logout").addEventListener("click", () => {
      this.cerrarSesion();
    });
  },

  iniciarSesion() {
    const nombre = document.querySelector("#login-nombre").value.trim();
    const email = document.querySelector("#login-email").value.trim();
    const errorDiv = document.querySelector("#login-error");

    if (!nombre || !email) {
      errorDiv.textContent = "Todos los campos son obligatorios";
      return;
    }

    if (!email.includes("@")) {
      errorDiv.textContent = "Email inválido";
      return;
    }

    this.usuarioActual = {
      id: Date.now(),
      nombre: nombre,
      email: email,
      fechaIngreso: new Date().toISOString()
    };

    localStorage.setItem("usuarioActual", JSON.stringify(this.usuarioActual));
    errorDiv.textContent = "";
    UI.mostrarDashboard();
  },

  cerrarSesion() {
    this.usuarioActual = null;
    localStorage.removeItem("usuarioActual");
    UI.mostrarLogin();
  },

  estaLogueado() {
    return this.usuarioActual !== null;
  }
};

// ==========================================
// MÓDULO DE CURSOS
// ==========================================
const Cursos = {
  datos: [],
  API_URL: "https://jsonplaceholder.typicode.com/posts",

  async cargarCursos() {
    const loader = document.querySelector("#loader");
    const container = document.querySelector("#cursos-container");

    loader.classList.remove("oculto");
    container.innerHTML = "";

    try {
      const respuesta = await fetch(this.API_URL);
      
      if (!respuesta.ok) {
        throw new Error("Error al cargar cursos");
      }

      const datos = await respuesta.json();
      
      // Transformar datos a nuestro formato
      this.datos = datos.slice(0, 12).map((item, index) => ({
        id: index + 1,
        titulo: item.title,
        descripcion: item.body,
        lecciones: Math.floor(Math.random() * 20) + 5,
        nivel: ["Principiante", "Intermedio", "Avanzado"][Math.floor(Math.random() * 3)]
      }));

      this.renderizar(container);

    } catch (error) {
      container.innerHTML = `
        <div class="alerta-error">
          <p>No pudimos cargar los cursos.</p>
          <button onclick="Cursos.cargarCursos()" class="btn">Reintentar</button>
        </div>
      `;
    } finally {
      loader.classList.add("oculto");
    }
  },

  renderizar(container) {
    container.innerHTML = this.datos.map(curso => `
      <div class="curso-card" data-id="${curso.id}">
        <div class="curso-nivel nivel-${curso.nivel.toLowerCase()}">${curso.nivel}</div>
        <h3>${curso.titulo}</h3>
        <p>${curso.descripcion.substring(0, 120)}...</p>
        <div class="curso-info">
          <span>📚 ${curso.lecciones} lecciones</span>
        </div>
        <button class="btn btn-inscribirse ${Progreso.estaInscrito(curso.id) ? 'btn-completado' : ''}">
          ${Progreso.estaInscrito(curso.id) ? '✅ Inscrito' : 'Inscribirse'}
        </button>
      </div>
    `).join("");

    // Event delegation para botones de inscripción
    container.addEventListener("click", (e) => {
      const btn = e.target.closest(".btn-inscribirse");
      if (btn) {
        const card = btn.closest(".curso-card");
        const cursoId = parseInt(card.dataset.id);
        this.toggleInscripcion(cursoId, btn);
      }
    });
  },

  toggleInscripcion(cursoId, btn) {
    if (!Auth.estaLogueado()) {
      alert("Debes iniciar sesión para inscribirte");
      return;
    }

    if (Progreso.estaInscrito(cursoId)) {
      Progreso.desinscribir(cursoId);
      btn.textContent = "Inscribirse";
      btn.classList.remove("btn-completado");
    } else {
      Progreso.inscribir(cursoId);
      btn.textContent = "✅ Inscrito";
      btn.classList.add("btn-completado");
    }
  }
};

// ==========================================
// MÓDULO DE PROGRESO
// ==========================================
const Progreso = {
  datos: {},

  init() {
    const guardado = localStorage.getItem("progreso");
    this.datos = guardado ? JSON.parse(guardado) : {};
  },

  inscribir(cursoId) {
    if (!this.datos[cursoId]) {
      this.datos[cursoId] = {
        inscrito: true,
        leccionesCompletadas: 0,
        fechaInscripcion: new Date().toISOString()
      };
      this.guardar();
    }
  },

  desinscribir(cursoId) {
    delete this.datos[cursoId];
    this.guardar();
  },

  estaInscrito(cursoId) {
    return this.datos[cursoId] && this.datos[cursoId].inscrito;
  },

  completarLeccion(cursoId) {
    if (!this.datos[cursoId]) return;
    this.datos[cursoId].leccionesCompletadas++;
    this.guardar();
  },

  obtenerProgreso(cursoId, totalLecciones) {
    if (!this.datos[cursoId]) return 0;
    return Math.round((this.datos[cursoId].leccionesCompletadas / totalLecciones) * 100);
  },

  guardar() {
    localStorage.setItem("progreso", JSON.stringify(this.datos));
  },

  renderizarProgreso() {
    const container = document.querySelector("#progreso-container");
    const cursosInscritos = Object.keys(this.datos);

    if (cursosInscritos.length === 0) {
      container.innerHTML = "<p>Aún no te has inscrito en ningún curso.</p>";
      return;
    }

    container.innerHTML = cursosInscritos.map(cursoId => {
      const curso = Cursos.datos.find(c => c.id === parseInt(cursoId));
      if (!curso) return "";
      const progreso = this.obtenerProgreso(cursoId, curso.lecciones);
      
      return `
        <div class="progreso-card">
          <h4>${curso.titulo}</h4>
          <div class="barra-progreso">
            <div class="barra-llenado" style="width: ${progreso}%"></div>
          </div>
          <p>${progreso}% completado</p>
          <button class="btn btn-small" onclick="Progreso.completarLeccion(${cursoId}); Progreso.renderizarProgreso();">
            +1 Lección
          </button>
        </div>
      `;
    }).join("");
  }
};

// ==========================================
// MÓDULO DE INTERFAZ
// ==========================================
const UI = {
  mostrarLogin() {
    document.querySelector("#seccion-login").classList.remove("oculto");
    document.querySelector("#seccion-cursos").classList.add("oculto");
    document.querySelector("#seccion-progreso").classList.add("oculto");
    document.querySelector("#seccion-perfil").classList.add("oculto");
    document.querySelector("#btn-login").classList.remove("oculto");
    document.querySelector("#btn-logout").classList.add("oculto");
  },

  mostrarDashboard() {
    document.querySelector("#seccion-login").classList.add("oculto");
    document.querySelector("#seccion-cursos").classList.remove("oculto");
    document.querySelector("#seccion-progreso").classList.remove("oculto");
    document.querySelector("#seccion-perfil").classList.remove("oculto");
    document.querySelector("#btn-login").classList.add("oculto");
    document.querySelector("#btn-logout").classList.remove("oculto");
    
    this.mostrarBienvenida();
    this.configurarNavegacion();
    Cursos.cargarCursos();
    Progreso.renderizarProgreso();
  },

  mostrarBienvenida() {
    const perfilContainer = document.querySelector("#perfil-container");
    perfilContainer.innerHTML = `
      <div class="perfil-info">
        <p><strong>Nombre:</strong> ${Auth.usuarioActual.nombre}</p>
        <p><strong>Email:</strong> ${Auth.usuarioActual.email}</p>
        <p><strong>Miembro desde:</strong> ${new Date(Auth.usuarioActual.fechaIngreso).toLocaleDateString()}</p>
      </div>
    `;
  },

  configurarNavegacion() {
    document.querySelectorAll("[data-seccion]").forEach(enlace => {
      enlace.addEventListener("click", (e) => {
        e.preventDefault();
        const seccion = e.target.dataset.seccion;
        document.querySelectorAll("section.seccion").forEach(s => {
          if (s.id === `seccion-${seccion}`) {
            s.classList.remove("oculto");
          } else if (s.id !== "seccion-login") {
            s.classList.add("oculto");
          }
        });
        if (seccion === "progreso") Progreso.renderizarProgreso();
      });
    });
  }
};

// ==========================================
// INICIALIZACIÓN
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  Progreso.init();
  Auth.init();
});
```

---

## La demo en acción

Camila hizo una demostración en vivo:

1. **Login**: Ingresó su nombre y email. La plataforma la reconoció.
2. **Cursos**: Los cursos aparecieron desde la API con un elegante loader.
3. **Inscripción**: Se inscribió en tres cursos. Los botones cambiaron a "Inscrito".
4. **Progreso**: Marcó lecciones completadas. Las barras de progreso se llenaron.
5. **Persistencia**: Cerró sesión, volvió a iniciar, y su progreso seguía intacto.

Los inversores asintieron, impresionados. La plataforma ya no era un prototipo estático. Era una aplicación interactiva.

—Esto es solo el comienzo —dijo Camila—. Lo que han visto hoy es JavaScript puro. Imagínense lo que podemos hacer con frameworks modernos.

---

## Enigmas del Capítulo 10

### Enigma 10.1: Mejora el diseño

Agrega estilos CSS para que la plataforma se vea profesional. Incluye: colores corporativos, animaciones suaves en las tarjetas, hover effects en botones, diseño responsive.

### Enigma 10.2: Buscador de cursos

Agrega un input de búsqueda que filtre los cursos en tiempo real mientras el usuario escribe.

### Enigma 10.3: Modo oscuro

Implementa un botón de modo oscuro que sea persistente (localStorage). Cambia los colores de toda la plataforma.

### Enigma 10.4: Estadísticas de progreso

Agrega una sección de estadísticas que muestre: cursos totales, cursos inscritos, lecciones completadas, promedio de progreso. Calcula estos datos desde el módulo Progreso.

---

## Lo que aprendiste en este libro

- **Variables**: `const`, `let`, tipos de datos
- **Condicionales**: `if/else`, `switch`, ternario
- **Funciones**: declaradas, expresadas, arrow functions
- **Arrays y objetos**: métodos de iteración (`map`, `filter`, `find`)
- **DOM**: seleccionar, modificar, crear elementos
- **Eventos**: click, submit, input, mouseover
- **Formularios**: validación, expresiones regulares
- **localStorage**: persistencia de datos
- **Fetch**: consumo de APIs, async/await
- **Modularización**: separar el código en módulos

---

Los inversores aplaudieron. Marco, el CEO, sonreía de oreja a oreja.

—Camila —dijo uno de los inversores—, ¿cómo aprendiste todo esto en tres semanas?

Camila miró a Diego, que levantó su taza de café en un brindis silencioso.

—Con un buen mentor y muchas ganas de aprender —respondió.

Mientras guardaba su laptop, Camila sintió algo que no había sentido antes: confianza en sí misma como desarrolladora. No solo era diseñadora. Ahora también era alguien que podía darle vida a la web.

Y ese, pensó, era el verdadero poder de la interactividad.
