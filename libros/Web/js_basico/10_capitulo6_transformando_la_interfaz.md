# Capítulo 6: Transformando la Interfaz

## Manipulación del DOM

---

—Ahora que sabes escuchar eventos —dijo Diego—, es hora de transformar la interfaz dinámicamente. Crear menús que se despliegan, contenido que aparece y desaparece, tarjetas que se agregan en tiempo real.

Camila tenía una lista de tareas: el menú de navegación debía colapsarse en móviles, los cursos debían mostrarse dinámicamente, y los usuarios debían poder marcar lecciones como completadas.

—Vamos por partes —dijo Diego.

---

## innerHTML vs textContent

```javascript
const contenedor = document.querySelector("#contenido");

// textContent: solo texto (más seguro, más rápido)
contenedor.textContent = "Hola, mundo!";

// innerHTML: permite HTML (cuidado con inyección)
contenedor.innerHTML = "<h2>Hola, mundo!</h2><p>Esto es HTML</p>";
```

—Usa `textContent` cuando solo necesites texto. Usa `innerHTML` cuando necesites insertar HTML, pero **nunca** con datos del usuario sin sanitizar.

---

## classList: manejando clases CSS

—Manipular clases CSS directamente es una de las operaciones más comunes.

```javascript
const menu = document.querySelector("#menu-lateral");

// Agregar una clase
menu.classList.add("visible");

// Quitar una clase
menu.classList.remove("visible");

// Alternar (agrega si no existe, quita si existe)
menu.classList.toggle("visible");

// Verificar si tiene una clase
if (menu.classList.contains("visible")) {
  console.log("El menú está visible");
}
```

Camila aplicó esto al menú de navegación:

```javascript
const btnMenu = document.querySelector("#btn-menu");
const nav = document.querySelector("#nav-principal");

btnMenu.addEventListener("click", () => {
  nav.classList.toggle("activo");
});
```

**CSS:**
```css
#nav-principal {
  display: none;
}

#nav-principal.activo {
  display: block;
}
```

---

## Creando y eliminando elementos

—A veces necesitas crear elementos desde JavaScript y agregarlos al DOM.

### createElement y appendChild

```javascript
// Crear un nuevo elemento
const nuevaTarjeta = document.createElement("div");
nuevaTarjeta.classList.add("tarjeta");
nuevaTarjeta.textContent = "Curso: JavaScript Básico";

// Agregarlo al DOM
const contenedor = document.querySelector("#lista-cursos");
contenedor.appendChild(nuevaTarjeta);
```

### Crear elementos con estructura

```javascript
function crearTarjetaCurso(titulo, nivel, duracion) {
  const tarjeta = document.createElement("div");
  tarjeta.classList.add("tarjeta-curso");
  
  const h3 = document.createElement("h3");
  h3.textContent = titulo;
  
  const pNivel = document.createElement("p");
  pNivel.textContent = `Nivel: ${nivel}`;
  
  const pDuracion = document.createElement("p");
  pDuracion.textContent = `Duración: ${duracion}`;
  
  tarjeta.appendChild(h3);
  tarjeta.appendChild(pNivel);
  tarjeta.appendChild(pDuracion);
  
  return tarjeta;
}

// Uso
const contenedor = document.querySelector("#lista-cursos");
const tarjetaJS = crearTarjetaCurso("JavaScript Básico", "Principiante", "10h");
contenedor.appendChild(tarjetaJS);
```

### removeChild y remove

```javascript
// Eliminar un elemento
const tarjeta = document.querySelector("#tarjeta-1");
tarjeta.remove(); // Método directo

// O desde el padre
const contenedor = document.querySelector("#lista-cursos");
const tarjeta2 = document.querySelector("#tarjeta-2");
contenedor.removeChild(tarjeta2);
```

---

## Manipulando estilos con style

```javascript
const elemento = document.querySelector("#destacado");

// Cambiar estilos inline
elemento.style.backgroundColor = "#3498db";
elemento.style.color = "white";
elemento.style.fontSize = "20px";
elemento.style.padding = "16px";
elemento.style.borderRadius = "8px";
```

—Las propiedades CSS se escriben en **camelCase** cuando se usan desde JavaScript:

| CSS | JavaScript |
|-----|-----------|
| `background-color` | `style.backgroundColor` |
| `font-size` | `style.fontSize` |
| `margin-top` | `style.marginTop` |
| `border-radius` | `style.borderRadius` |

---

## Trabajando con atributos

```javascript
const enlace = document.querySelector("a");

// Obtener atributo
console.log(enlace.getAttribute("href"));

// Establecer atributo
enlace.setAttribute("href", "https://aprendeya.com/cursos");
enlace.setAttribute("target", "_blank");

// Verificar si tiene atributo
if (enlace.hasAttribute("target")) {
  console.log("El enlace abre en nueva pestaña");
}

// Eliminar atributo
enlace.removeAttribute("target");
```

---

## La funcionalidad de mostrar/ocultar

Camila implementó varias funcionalidades en la plataforma:

```javascript
// Mostrar/Ocultar menú de perfil
const btnPerfil = document.querySelector("#btn-perfil");
const menuPerfil = document.querySelector("#menu-perfil");

btnPerfil.addEventListener("click", () => {
  menuPerfil.classList.toggle("oculto");
});

// Cerrar menú al hacer clic fuera
document.addEventListener("click", (event) => {
  if (!btnPerfil.contains(event.target) && !menuPerfil.contains(event.target)) {
    menuPerfil.classList.add("oculto");
  }
});
```

```javascript
// Generar lista de cursos dinámicamente
const cursos = [
  { titulo: "HTML Básico", nivel: "Principiante", duracion: "5h" },
  { titulo: "CSS Avanzado", nivel: "Intermedio", duracion: "8h" },
  { titulo: "JavaScript", nivel: "Principiante", duracion: "10h" },
  { titulo: "React", nivel: "Avanzado", duracion: "12h" }
];

const contenedorCursos = document.querySelector("#lista-cursos");

cursos.forEach(curso => {
  const tarjeta = document.createElement("div");
  tarjeta.classList.add("tarjeta-curso");
  
  tarjeta.innerHTML = `
    <h3>${curso.titulo}</h3>
    <p><strong>Nivel:</strong> ${curso.nivel}</p>
    <p><strong>Duración:</strong> ${curso.duracion}</p>
    <button class="btn-inscribirse">Inscribirse</button>
  `;
  
  contenedorCursos.appendChild(tarjeta);
});

// Agregar evento a cada botón de inscripción
document.querySelectorAll(".btn-inscribirse").forEach(btn => {
  btn.addEventListener("click", (event) => {
    const tarjeta = event.target.closest(".tarjeta-curso");
    const titulo = tarjeta.querySelector("h3").textContent;
    alert(`Te has inscrito en: ${titulo}`);
  });
});
```

—`closest()` busca el ancestro más cercano que coincida con el selector —explicó Diego—. Muy útil cuando trabajas con eventos en elementos creados dinámicamente.

---

## Enigmas del Capítulo 6

### Enigma 6.1: Lista de tareas

Crea un HTML con un input y un botón "Agregar". Cada vez que el usuario escribe y presiona el botón, se agrega un nuevo elemento `<li>` a una lista `<ul>`. Si el input está vacío, muestra un mensaje de error.

### Enigma 6.2: Tarjetas de colores

Crea un botón que, al hacer clic, agregue una tarjeta de color aleatorio al contenedor. Cada tarjeta debe tener un botón "Eliminar" que la quite del DOM.

### Enigma 6.3: Modo oscuro

Crea un botón "Modo Oscuro" que alterne las clases del body. Cuando está activo, el fondo es negro y el texto blanco. Cambia también el texto del botón a "Modo Claro".

### Enigma 6.4: Galería dinámica

Dado un array de URLs de imágenes (pueden ser placeholder como `https://via.placeholder.com/150`), genera dinámicamente una galería. Cada imagen debe tener un borde que se resalte al pasar el mouse.

---

## Lo que aprendiste

- **`textContent`**: texto plano; **`innerHTML`**: HTML (con precaución)
- **`classList`**: `add`, `remove`, `toggle`, `contains`
- **`createElement`** y **`appendChild`**: crear y agregar elementos
- **`remove`** y **`removeChild`**: eliminar elementos
- **`style`**: manipular estilos inline (en camelCase)
- **`getAttribute`** / **`setAttribute`**: trabajar con atributos HTML
- **`closest()`**: buscar ancestros de un elemento

---

—Ahora la plataforma ya no es estática —dijo Camila, viendo cómo las tarjetas de cursos aparecían en pantalla—. Los usuarios pueden ver el contenido dinámicamente.

—Y mañana —dijo Diego— van a poder registrarse. Vamos a trabajar con formularios y validación.

Camila sonrió. La plataforma comenzaba a sentirse como una aplicación de verdad.
