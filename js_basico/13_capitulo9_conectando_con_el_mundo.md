# Capítulo 9: Conectando con el Mundo

## Fetch y APIs

---

—Los cursos de la plataforma están hardcodeados —dijo Diego—. Están escritos directamente en el código. En una aplicación real, los cursos vendrían de un servidor.

—¿Cómo los traemos? —preguntó Camila.

—Con **fetch**. Es la forma moderna de hacer peticiones HTTP desde JavaScript.

---

## ¿Qué es una API?

—**API** significa **Application Programming Interface**. Es un intermediario que permite que dos aplicaciones se comuniquen.

En el contexto web, una **API REST** expone datos a través de URLs. Por ejemplo:

```
https://api.aprendeya.com/cursos
https://api.aprendeya.com/cursos/1
https://api.aprendeya.com/usuarios
```

—El backend expone estas URLs, y el frontend las consume con JavaScript.

---

## Fetch: Peticiones GET

—La forma más común es obtener datos con una petición **GET**.

```javascript
fetch("https://jsonplaceholder.typicode.com/posts")
  .then(function(respuesta) {
    return respuesta.json();
  })
  .then(function(datos) {
    console.log(datos);
  })
  .catch(function(error) {
    console.error("Error:", error);
  });
```

—`fetch` devuelve una **Promise**. Las promesas representan operaciones asíncronas: operaciones que no se completan inmediatamente.

---

## Promesas: then y catch

—JavaScript es **asíncrono**. Cuando pides datos a un servidor, no sabes cuánto tardará la respuesta. Las promesas manejan esta incertidumbre.

```javascript
// Una promesa puede estar en 3 estados:
// pending (pendiente), fulfilled (resuelta), rejected (rechazada)

const promesa = fetch("https://api.aprendeya.com/cursos");

promesa
  .then(function(respuesta) {
    // La promesa se resolvió exitosamente
    if (!respuesta.ok) {
      throw new Error("Error HTTP: " + respuesta.status);
    }
    return respuesta.json(); // También devuelve una promesa
  })
  .then(function(cursos) {
    // Aquí tienes los datos listos para usar
    console.log("Cursos obtenidos:", cursos);
    mostrarCursos(cursos);
  })
  .catch(function(error) {
    // La promesa fue rechazada (error de red, servidor caído, etc.)
    console.error("Error al obtener cursos:", error);
    mostrarError("No se pudieron cargar los cursos");
  });
```

### Encadenamiento de promesas

```javascript
fetch("https://jsonplaceholder.typicode.com/users/1")
  .then(respuesta => respuesta.json())
  .then(usuario => {
    console.log("Usuario:", usuario.name);
    return fetch(`https://jsonplaceholder.typicode.com/posts?userId=${usuario.id}`);
  })
  .then(respuesta => respuesta.json())
  .then(posts => {
    console.log("Posts del usuario:", posts);
  })
  .catch(error => console.error("Error:", error));
```

---

## Async / Await

—Si las promesas te parecen confusas —dijo Diego—, JavaScript moderno ofrece una sintaxis más limpia: **async/await**.

```javascript
// Función async: siempre devuelve una promesa
async function obtenerCursos() {
  try {
    const respuesta = await fetch("https://api.aprendeya.com/cursos");
    
    if (!respuesta.ok) {
      throw new Error(`Error HTTP: ${respuesta.status}`);
    }
    
    const cursos = await respuesta.json();
    console.log("Cursos:", cursos);
    return cursos;
    
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}

// Uso
obtenerCursos().then(cursos => {
  console.log(`Se obtuvieron ${cursos.length} cursos`);
});
```

—`await` pausa la ejecución hasta que la promesa se resuelva. Solo funciona dentro de funciones `async`.

| Enfoque | Sintaxis | Ideal para |
|---------|----------|------------|
| then/catch | `.then().catch()` | Cadenas cortas |
| async/await | `async function() { await }` | Flujo lineal, múltiples await |

---

## Manejo de errores

—Las peticiones a servidores pueden fallar por muchas razones. Siempre debes manejar los errores.

```javascript
async function cargarCursos() {
  const contenedor = document.querySelector("#lista-cursos");
  const loader = document.querySelector("#loader");
  
  try {
    // Mostrar loader
    loader.style.display = "block";
    contenedor.innerHTML = "";
    
    const respuesta = await fetch("https://jsonplaceholder.typicode.com/posts");
    
    if (!respuesta.ok) {
      throw new Error(`Error del servidor: ${respuesta.status}`);
    }
    
    const cursos = await respuesta.json();
    mostrarCursos(cursos);
    
  } catch (error) {
    contenedor.innerHTML = `
      <div class="error">
        <p>😕 No pudimos cargar los cursos.</p>
        <p>${error.message}</p>
        <button onclick="cargarCursos()">Reintentar</button>
      </div>
    `;
  } finally {
    loader.style.display = "none";
  }
}

function mostrarCursos(cursos) {
  const contenedor = document.querySelector("#lista-cursos");
  
  cursos.slice(0, 10).forEach(curso => {
    const tarjeta = document.createElement("div");
    tarjeta.classList.add("tarjeta-curso");
    tarjeta.innerHTML = `
      <h3>${curso.title}</h3>
      <p>${curso.body}</p>
    `;
    contenedor.appendChild(tarjeta);
  });
}
```

---

## Mostrando datos en la UI

Camila conectó su plataforma con una API simulada:

```javascript
// API pública de ejemplo (JSONPlaceholder)
const API_URL = "https://jsonplaceholder.typicode.com";

const AprendeYaAPI = {
  async obtenerCursos() {
    const res = await fetch(`${API_URL}/posts`);
    return res.json();
  },

  async obtenerCurso(id) {
    const res = await fetch(`${API_URL}/posts/${id}`);
    return res.json();
  },

  async obtenerComentarios(cursoId) {
    const res = await fetch(`${API_URL}/comments?postId=${cursoId}`);
    return res.json();
  }
};

// Cargar cursos y mostrarlos en tarjetas
async function inicializarPlataforma() {
  try {
    const cursos = await AprendeYaAPI.obtenerCursos();
    const contenedor = document.querySelector("#cursos-container");
    
    contenedor.innerHTML = cursos.slice(0, 8).map(curso => `
      <div class="curso-card" data-id="${curso.id}">
        <h3>${curso.title}</h3>
        <p>${curso.body.substring(0, 100)}...</p>
        <button class="btn-ver-curso">Ver curso</button>
      </div>
    `).join("");

    // Event delegation para los botones
    contenedor.addEventListener("click", async (event) => {
      if (event.target.classList.contains("btn-ver-curso")) {
        const card = event.target.closest(".curso-card");
        const id = card.dataset.id;
        await verDetalleCurso(id);
      }
    });

  } catch (error) {
    document.querySelector("#cursos-container").innerHTML = `
      <div class="alerta alerta-error">
        No se pudieron cargar los cursos. 
        <button onclick="inicializarPlataforma()">Reintentar</button>
      </div>
    `;
  }
}

async function verDetalleCurso(id) {
  try {
    const curso = await AprendeYaAPI.obtenerCurso(id);
    const comentarios = await AprendeYaAPI.obtenerComentarios(id);
    
    const detalle = document.querySelector("#detalle-curso");
    detalle.innerHTML = `
      <h2>${curso.title}</h2>
      <p>${curso.body}</p>
      <h4>Comentarios (${comentarios.length})</h4>
      ${comentarios.map(c => `
        <div class="comentario">
          <strong>${c.name}</strong>
          <p>${c.body}</p>
        </div>
      `).join("")}
    `;

  } catch (error) {
    console.error("Error al cargar detalle:", error);
  }
}

// Iniciar
inicializarPlataforma();
```

---

## Enviando datos con POST

—No solo obtenemos datos. También podemos enviarlos.

```javascript
async function registrarUsuario(nuevoUsuario) {
  try {
    const respuesta = await fetch("https://jsonplaceholder.typicode.com/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(nuevoUsuario)
    });

    if (!respuesta.ok) {
      throw new Error("Error al registrar usuario");
    }

    const usuarioCreado = await respuesta.json();
    console.log("Usuario creado:", usuarioCreado);
    return usuarioCreado;

  } catch (error) {
    console.error("Error:", error);
    return null;
  }
}

// Uso
registrarUsuario({
  name: "Camila Ríos",
  email: "camila@aprendeya.com"
});
```

---

## Enigmas del Capítulo 9

### Enigma 9.1: Tu primera API

Usando `https://jsonplaceholder.typicode.com/users`, obtén la lista de usuarios y muestra en consola solo los nombres y emails.

### Enigma 9.2: Galería de fotos

Usando `https://jsonplaceholder.typicode.com/photos`, obtén las primeras 10 fotos y muéstralas en una galería HTML. Cada foto debe mostrar la miniatura (thumbnailUrl) y el título.

### Enigma 9.3: Carga con indicador

Modifica el enigma 9.2 para mostrar un mensaje "Cargando..." mientras se obtienen los datos, y reemplazarlo con la galería cuando lleguen los datos. Maneja el caso de error.

### Enigma 9.4: Buscador de usuarios

Crea un input de búsqueda que filtre usuarios de la API `https://jsonplaceholder.typicode.com/users` en tiempo real. Muestra solo los usuarios cuyo nombre coincida con lo que el usuario escribe.

---

## Lo que aprendiste

- **API**: interfaz para comunicar aplicaciones
- **fetch**: API nativa para peticiones HTTP
- **GET**: obtener datos del servidor
- **POST**: enviar datos al servidor
- **Promesas**: operaciones asíncronas con `.then()` y `.catch()`
- **async/await**: sintaxis más legible para código asíncrono
- Manejo de **errores** con try/catch
- Mostrar **loader** y estados de carga en la UI

---

—Ahora la plataforma ya no está aislada —dijo Camila, viendo cómo los cursos aparecían desde la API—. Se conecta con el mundo.

Diego asintió.

—Mañana es el gran día. La demo con los inversores. Vamos a integrar todo lo que has aprendido.

Camila miró su código. Variables, condicionales, funciones, arrays, objetos, DOM, eventos, formularios, localStorage, fetch. Había recorrido un largo camino en solo dos semanas.
