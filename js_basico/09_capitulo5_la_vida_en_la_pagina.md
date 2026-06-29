# Capítulo 5: La Vida en la Página

## DOM y Eventos

---

—Hasta ahora hemos trabajado en la consola —dijo Diego, cerrando la pestaña de herramientas de desarrollador—. Pero la magia real ocurre cuando JavaScript interactúa con la página web.

Camila abrió su archivo HTML de la plataforma. Había una estructura limpia con `<header>`, `<main>`, `<section>` y `<footer>`. Todo se veía hermoso pero inmóvil.

—Vamos a darle vida —dijo Diego.

---

## ¿Qué es el DOM?

—**DOM** significa **Document Object Model**. Es una representación de tu página HTML como un árbol de objetos que JavaScript puede manipular.

Cuando el navegador carga tu HTML, crea el DOM. Cada etiqueta HTML se convierte en un **nodo** que puedes modificar, eliminar o crear.

```html
<!DOCTYPE html>
<html>
<head>
  <title>AprendeYa</title>
</head>
<body>
  <h1 id="titulo">Bienvenido a AprendeYa</h1>
  <p class="descripcion">Tu plataforma de cursos online</p>
</body>
</html>
```

—Cada elemento del HTML se convierte en un objeto JavaScript con propiedades y métodos.

---

## Seleccionando elementos del DOM

Para manipular un elemento, primero debes seleccionarlo.

### document.getElementById()

```javascript
const titulo = document.getElementById("titulo");
console.log(titulo); // <h1 id="titulo">Bienvenido a AprendeYa</h1>
console.log(titulo.textContent); // "Bienvenido a AprendeYa"
```

### document.querySelector()

—Este es el más versátil —dijo Diego—. Usa selectores CSS.

```javascript
// Selecciona por ID (usa #)
const titulo = document.querySelector("#titulo");

// Selecciona por clase (usa .)
const descripcion = document.querySelector(".descripcion");

// Selecciona por etiqueta
const primerParrafo = document.querySelector("p");

// Selecciona el primer elemento que coincida
const primerBoton = document.querySelector("button");
```

### document.querySelectorAll()

```javascript
// Selecciona TODOS los elementos que coincidan
const todosLosParrafos = document.querySelectorAll("p");
const botones = document.querySelectorAll(".btn");

console.log(todosLosParrafos.length); // Número de párrafos
todosLosParrafos.forEach(p => console.log(p.textContent));
```

| Método | Devuelve | Usa |
|--------|----------|-----|
| `getElementById("id")` | Un elemento | IDs únicos |
| `querySelector("selector")` | Primer elemento | Cualquier selector CSS |
| `querySelectorAll("selector")` | NodeList (como array) | Múltiples elementos |

---

## Eventos: la página reacciona

—Un **evento** es algo que ocurre en la página: un clic, una tecla presionada, el mouse moviéndose. JavaScript puede "escuchar" esos eventos y reaccionar.

### addEventListener

```javascript
const boton = document.querySelector("#btn-iniciar-sesion");

boton.addEventListener("click", function() {
  alert("Has hecho clic en Iniciar Sesión");
});
```

—El primer argumento es el tipo de evento (`"click"`). El segundo es la función que se ejecuta cuando ocurre.

### Tipos de eventos comunes

```javascript
const boton = document.querySelector("#miBoton");
const input = document.querySelector("#miInput");
const parrafo = document.querySelector("#miParrafo");

// Click
boton.addEventListener("click", () => {
  console.log("¡Click!");
});

// Mouse over (mouse encima)
boton.addEventListener("mouseover", () => {
  console.log("Mouse está sobre el botón");
});

// Keydown (tecla presionada)
input.addEventListener("keydown", (event) => {
  console.log(`Tecla presionada: ${event.key}`);
});

// Submit (formulario enviado)
const formulario = document.querySelector("#miFormulario");
formulario.addEventListener("submit", (event) => {
  event.preventDefault(); // Evita que la página se recargue
  console.log("Formulario enviado");
});
```

### El objeto event

—Cuando ocurre un evento, JavaScript pasa automáticamente un objeto `event` a la función manejadora. Este objeto contiene información sobre el evento.

```javascript
const boton = document.querySelector("#miBoton");

boton.addEventListener("click", function(event) {
  console.log(event.type);     // "click"
  console.log(event.target);   // El elemento que recibió el click
  console.log(event.clientX);  // Posición X del mouse
  console.log(event.clientY);  // Posición Y del mouse
});
```

---

## this en eventos

—Dentro de un manejador de eventos con función normal, `this` se refiere al elemento que recibió el evento.

```javascript
const botones = document.querySelectorAll(".btn");

botones.forEach(function(boton) {
  boton.addEventListener("click", function() {
    console.log(this.textContent); // El texto del botón clickeado
    this.style.backgroundColor = "blue";
  });
});
```

—Con arrow functions, `this` no se refiere al elemento, sino al contexto exterior. Si necesitas acceder al elemento, usa `event.target`.

```javascript
botones.forEach(boton => {
  boton.addEventListener("click", (event) => {
    console.log(event.target.textContent);
    event.target.style.backgroundColor = "blue";
  });
});
```

---

## El primer botón interactivo de Camila

Camila creó su primera funcionalidad interactiva: un botón que muestra el mensaje de bienvenida personalizado.

**HTML:**
```html
<header>
  <h1 id="titulo">Bienvenido a AprendeYa</h1>
  <button id="btn-saludo">Saludar</button>
  <p id="mensaje"></p>
</header>
```

**JavaScript:**
```javascript
const btnSaludo = document.querySelector("#btn-saludo");
const mensaje = document.querySelector("#mensaje");
const titulo = document.querySelector("#titulo");

btnSaludo.addEventListener("click", function() {
  const nombre = "Camila";
  mensaje.textContent = `¡Hola, ${nombre}! Gracias por usar AprendeYa.`;
  titulo.style.color = "#2ecc71";
});
```

—¡Funcionó! —exclamó Camila—. La página cambió cuando hice clic.

—Eso es el DOM en acción —dijo Diego—. JavaScript modificó el contenido y el estilo de la página en tiempo real.

---

## Enigmas del Capítulo 5

### Enigma 5.1: Botón que cambia de color

Crea un botón en HTML que, al hacerle clic, cambie su propio color de fondo a un color aleatorio. Pista: usa `Math.floor(Math.random() * 16777215).toString(16)` para generar un color hexadecimal.

### Enigma 5.2: Contador de clics

Crea un botón y un párrafo que muestre un número. Cada clic al botón incrementa el número. Llega al 10 y reinicia.

### Enigma 5.3: Mouseover en tarjetas

Crea tres divs con clase "tarjeta". Cuando el mouse pase sobre una, cambia su borde a verde. Cuando salga, vuelve al borde original.

### Enigma 5.4: Input en vivo

Crea un input de texto y un párrafo. Cada vez que el usuario escriba en el input, el párrafo muestra en tiempo real lo que se está escribiendo. Usa el evento `input`.

---

## Lo que aprendiste

- El **DOM** es la representación HTML como objetos JavaScript
- **`querySelector`** y **`querySelectorAll`** seleccionan elementos
- **`addEventListener`** escucha eventos
- Tipos de eventos: `click`, `mouseover`, `keydown`, `submit`, `input`
- El objeto **`event`** contiene información del evento
- `this` en eventos se refiere al elemento (con funciones normales)
- **`event.target`** es el elemento que desencadenó el evento

---

—Ahora la página ya responde —dijo Diego, guardando los cambios—. Mañana vamos a aprender a transformar la interfaz por completo: crear elementos, eliminarlos, cambiar clases y estilos dinámicamente.

Camila hizo clic en su botón de saludo una vez más. Cada clic cambiaba el color del título. Era un detalle pequeño, pero para ella era enorme: había hecho que la página le respondiera.
