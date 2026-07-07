# Apéndice: Soluciones a los Enigmas

## Capítulo 1: El Primer Script

### Enigma 1.1: Tu primer programa

```javascript
const miNombre = "Tu nombre aquí";
let miEdad = 25;
const lenguajeFavorito = "JavaScript";

console.log(`Hola, me llamo ${miNombre}, tengo ${miEdad} años y mi lenguaje favorito es ${lenguajeFavorito}.`);
```

### Enigma 1.2: Detecta el tipo

```javascript
typeof "42"    // "string"
typeof 42      // "number"
typeof true    // "boolean"
typeof null    // "object" (error histórico de JavaScript)
typeof undefined  // "undefined"
typeof "true"  // "string"
```

El caso `typeof null === "object"` es un error conocido de JavaScript que no se corrigió por compatibilidad histórica.

### Enigma 1.3: El mensaje de la plataforma

```javascript
const curso = "JavaScript Básico";
let progreso = 15;
console.log(`Estás tomando el curso ${curso}. Tu progreso es ${progreso}%.`);
```

### Enigma 1.4: Conversión de tipos

```javascript
console.log("5" + 3);  // "53" (concatenación)
console.log("5" - 3);  // 2 (conversión a número)
console.log("5" * "3"); // 15 (ambos se convierten a números)
console.log("Hola" + 5); // "Hola5" (concatenación)
```

---

## Capítulo 2: Tomando Decisiones

### Enigma 2.1: Calculadora de notas

```javascript
let nota = 85;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 70) {
  console.log("Bien");
} else if (nota >= 50) {
  console.log("Regular");
} else {
  console.log("Necesitas mejorar");
}
```

### Enigma 2.2: Acceso a la plataforma

```javascript
let logueado = true;
let tieneSuscripcion = false;
let esAdmin = true;

if (logueado && (tieneSuscripcion || esAdmin)) {
  console.log("Acceso concedido");
} else if (logueado && !tieneSuscripcion && !esAdmin) {
  console.log("Debes adquirir una suscripción");
} else {
  console.log("Por favor, inicia sesión");
}
```

### Enigma 2.3: Día laboral o finde

```javascript
const dia = "sabado";

switch (dia) {
  case "lunes":
  case "martes":
  case "miercoles":
  case "jueves":
  case "viernes":
    console.log("Día laboral");
    break;
  case "sabado":
  case "domingo":
    console.log("Fin de semana");
    break;
  default:
    console.log("Día no válido");
}
```

### Enigma 2.4: ¿Par o impar?

```javascript
function esPar(numero) {
  return numero % 2 === 0;
}

console.log(`15: ${esPar(15) ? "par" : "impar"}`);
console.log(`22: ${esPar(22) ? "par" : "impar"}`);
console.log(`7: ${esPar(7) ? "par" : "impar"}`);
console.log(`100: ${esPar(100) ? "par" : "impar"}`);
```

---

## Capítulo 3: Las Funciones del Conocimiento

### Enigma 3.1: Tu primera función

```javascript
function esMayorDeEdad(edad) {
  return edad >= 18;
}

console.log(esMayorDeEdad(15)); // false
console.log(esMayorDeEdad(18)); // true
console.log(esMayorDeEdad(21)); // true
console.log(esMayorDeEdad(0));  // false
```

### Enigma 3.2: Calculadora básica

```javascript
const sumar = (a, b) => a + b;
const restar = (a, b) => a - b;
const multiplicar = (a, b) => a * b;

function calculadora(operacion, a, b) {
  if (operacion === "suma") return sumar(a, b);
  if (operacion === "resta") return restar(a, b);
  if (operacion === "multiplica") return multiplicar(a, b);
  return "Operación no válida";
}

console.log(calculadora("suma", 10, 5));       // 15
console.log(calculadora("resta", 10, 5));      // 5
console.log(calculadora("multiplica", 10, 5)); // 50
```

### Enigma 3.3: Validación de email

```javascript
function validarEmail(email) {
  return email.includes("@") && email.includes(".", email.indexOf("@"));
}

console.log(validarEmail("camila@email.com")); // true
console.log(validarEmail("invalido@"));         // false
console.log(validarEmail("sinarroba.com"));     // false
```

### Enigma 3.4: Conversión de temperatura

```javascript
const celsiusAFahrenheit = celsius => celsius * 9/5 + 32;

console.log(celsiusAFahrenheit(0));   // 32
console.log(celsiusAFahrenheit(100)); // 212
console.log(celsiusAFahrenheit(37));  // 98.6
```

---

## Capítulo 4: Listas y Colecciones

### Enigma 4.1: Tu lista de compras

```javascript
let listaCompras = ["pan", "leche", "huevos", "arroz", "frijoles"];
listaCompras.push("azúcar");
listaCompras.shift();
console.log(listaCompras);
console.log(`Longitud: ${listaCompras.length}`);
```

### Enigma 4.2: Catálogo de cursos

```javascript
const cursos = [
  { titulo: "HTML Básico", duracion: "5h", precio: 0 },
  { titulo: "CSS Avanzado", duracion: "8h", precio: 29.99 },
  { titulo: "JavaScript", duracion: "10h", precio: 0 }
];

const titulos = cursos.map(curso => curso.titulo);
console.log(titulos);

const cursosGratis = cursos.filter(curso => curso.precio === 0);
console.log(cursosGratis);
```

### Enigma 4.3: Objeto estudiante

```javascript
const estudiante = {
  nombre: "Camila Ríos",
  edad: 27,
  cursos: ["HTML", "CSS", "JavaScript"],
  direccion: {
    ciudad: "Lima",
    pais: "Perú"
  },
  presentarse() {
    return `Hola, soy ${this.nombre} de ${this.direccion.ciudad}, ${this.direccion.pais}.`;
  }
};

console.log(estudiante.presentarse());
```

### Enigma 4.4: Transformando datos

```javascript
const nums = [5, 12, 8, 21, 3, 15];

const mayores = nums.filter(n => n > 10);
console.log(mayores); // [12, 21, 15]

const dobles = nums.map(n => n * 2);
console.log(dobles); // [10, 24, 16, 42, 6, 30]

const primeroMayor = nums.find(n => n > 10);
console.log(primeroMayor); // 12
```

---

## Capítulo 5: La Vida en la Página

### Enigma 5.1: Botón que cambia de color

```javascript
const boton = document.querySelector("#miBoton");

boton.addEventListener("click", function() {
  const color = "#" + Math.floor(Math.random() * 16777215).toString(16);
  this.style.backgroundColor = color;
});
```

### Enigma 5.2: Contador de clics

```javascript
let contador = 0;
const btnContador = document.querySelector("#btn-contador");
const display = document.querySelector("#display");

btnContador.addEventListener("click", () => {
  contador++;
  if (contador > 10) contador = 0;
  display.textContent = contador;
});
```

### Enigma 5.3: Mouseover en tarjetas

```javascript
document.querySelectorAll(".tarjeta").forEach(tarjeta => {
  tarjeta.addEventListener("mouseover", function() {
    this.style.border = "2px solid green";
  });
  tarjeta.addEventListener("mouseout", function() {
    this.style.border = "1px solid #ccc";
  });
});
```

### Enigma 5.4: Input en vivo

```javascript
const input = document.querySelector("#miInput");
const parrafo = document.querySelector("#vista-previa");

input.addEventListener("input", function() {
  parrafo.textContent = this.value || "Escribe algo...";
});
```

---

## Capítulo 6: Transformando la Interfaz

### Enigma 6.1: Lista de tareas

```javascript
const input = document.querySelector("#nueva-tarea");
const btn = document.querySelector("#agregar");
const lista = document.querySelector("#lista-tareas");

btn.addEventListener("click", () => {
  const texto = input.value.trim();
  if (texto === "") return alert("Escribe una tarea");
  
  const li = document.createElement("li");
  li.textContent = texto;
  lista.appendChild(li);
  input.value = "";
});
```

### Enigma 6.2: Tarjetas de colores

```javascript
const btnAgregar = document.querySelector("#agregar-tarjeta");
const contenedor = document.querySelector("#contenedor-tarjetas");

btnAgregar.addEventListener("click", () => {
  const tarjeta = document.createElement("div");
  tarjeta.className = "tarjeta-color";
  tarjeta.style.backgroundColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
  tarjeta.innerHTML = '<button class="eliminar">X</button>';
  contenedor.appendChild(tarjeta);
});

contenedor.addEventListener("click", (e) => {
  if (e.target.classList.contains("eliminar")) {
    e.target.parentElement.remove();
  }
});
```

### Enigma 6.3: Modo oscuro

```javascript
const btnModo = document.querySelector("#btn-modo");
const body = document.body;

btnModo.addEventListener("click", () => {
  body.classList.toggle("modo-oscuro");
  btnModo.textContent = body.classList.contains("modo-oscuro") ? "Modo Claro" : "Modo Oscuro";
});
```

### Enigma 6.4: Galería dinámica

```javascript
const imagenes = [
  "https://via.placeholder.com/150/ff0000",
  "https://via.placeholder.com/150/00ff00",
  "https://via.placeholder.com/150/0000ff"
];

const galeria = document.querySelector("#galeria");

imagenes.forEach(url => {
  const img = document.createElement("img");
  img.src = url;
  img.addEventListener("mouseover", () => img.style.border = "3px solid gold");
  img.addEventListener("mouseout", () => img.style.border = "none");
  galeria.appendChild(img);
});
```

---

## Capítulo 7: Formularios Inteligentes

### Enigma 7.1: Validación de edad

```javascript
function validarEdad(edad) {
  const valor = parseInt(edad);
  if (isNaN(valor) || valor < 18 || valor > 120) {
    return "La edad debe ser un número entre 18 y 120";
  }
  return "";
}
```

### Enigma 7.2: Confirmación de contraseña

```javascript
function validarConfirmacion(password, confirmacion) {
  if (password !== confirmacion) {
    return "Las contraseñas no coinciden";
  }
  return "";
}
```

### Enigma 7.3: Contador de caracteres

```javascript
const textarea = document.querySelector("#biografia");
const contador = document.querySelector("#contador");
const max = 200;

textarea.addEventListener("input", function() {
  const restantes = max - this.value.length;
  contador.textContent = `${restantes} caracteres restantes`;
  contador.style.color = restantes < 0 ? "red" : "#666";
});
```

### Enigma 7.4: Validación de nombre de usuario

```javascript
function validarNombreUsuario(nombre) {
  const regex = /^[a-z][a-z0-9_]{3,14}$/;
  return regex.test(nombre);
}
```

---

## Capítulo 8: Guardando el Progreso

### Enigma 8.1: Contador de visitas

```javascript
let visitas = localStorage.getItem("contadorVisitas") || 0;
visitas = parseInt(visitas) + 1;
localStorage.setItem("contadorVisitas", visitas);
console.log(`Has visitado esta página ${visitas} veces`);
```

### Enigma 8.2: Tema persistente

```javascript
const temaGuardado = localStorage.getItem("tema");
if (temaGuardado === "oscuro") document.body.classList.add("modo-oscuro");

document.querySelector("#btn-tema").addEventListener("click", () => {
  document.body.classList.toggle("modo-oscuro");
  const tema = document.body.classList.contains("modo-oscuro") ? "oscuro" : "claro";
  localStorage.setItem("tema", tema);
});
```

### Enigma 8.3: Lista de favoritos

```javascript
function toggleFavorito(cursoId) {
  let favoritos = JSON.parse(localStorage.getItem("favoritos") || "[]");
  const index = favoritos.indexOf(cursoId);
  if (index === -1) favoritos.push(cursoId);
  else favoritos.splice(index, 1);
  localStorage.setItem("favoritos", JSON.stringify(favoritos));
  mostrarFavoritos();
}
```

### Enigma 8.4: Notas persistentes

```javascript
const notas = document.querySelector("#notas");
notas.value = localStorage.getItem("notas") || "";

notas.addEventListener("input", function() {
  localStorage.setItem("notas", this.value);
});
```

---

## Capítulo 9: Conectando con el Mundo

### Enigma 9.1: Tu primera API

```javascript
fetch("https://jsonplaceholder.typicode.com/users")
  .then(res => res.json())
  .then(usuarios => {
    usuarios.forEach(u => console.log(`${u.name}: ${u.email}`));
  });
```

### Enigma 9.2: Galería de fotos

```javascript
async function cargarGaleria() {
  const res = await fetch("https://jsonplaceholder.typicode.com/photos");
  const fotos = await res.json();
  const galeria = document.querySelector("#galeria");
  
  fotos.slice(0, 10).forEach(foto => {
    const div = document.createElement("div");
    div.innerHTML = `<img src="${foto.thumbnailUrl}" alt="${foto.title}"><p>${foto.title}</p>`;
    galeria.appendChild(div);
  });
}
```

### Enigma 9.3: Carga con indicador

```javascript
async function cargarGaleria() {
  const loader = document.querySelector("#loader");
  const galeria = document.querySelector("#galeria");
  
  loader.style.display = "block";
  
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/photos");
    if (!res.ok) throw new Error("Error");
    const fotos = await res.json();
    galeria.innerHTML = fotos.slice(0, 10).map(f =>
      `<div><img src="${f.thumbnailUrl}" alt="${f.title}"><p>${f.title}</p></div>`
    ).join("");
  } catch {
    galeria.innerHTML = "<p>Error al cargar imágenes</p>";
  } finally {
    loader.style.display = "none";
  }
}
```

### Enigma 9.4: Buscador de usuarios

```javascript
let usuarios = [];

async function init() {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  usuarios = await res.json();
}

document.querySelector("#buscador").addEventListener("input", function() {
  const filtro = this.value.toLowerCase();
  const resultados = usuarios.filter(u => u.name.toLowerCase().includes(filtro));
  console.log(resultados);
});
```

---

## Capítulo 10: La Gran Demo

Las soluciones del capítulo 10 son proyectos abiertos. No hay una única respuesta correcta. Evalúa tu solución según:

- **Enigma 10.1**: ¿La plataforma se ve profesional y responsiva?
- **Enigma 10.2**: ¿El buscador filtra correctamente en tiempo real?
- **Enigma 10.3**: ¿El modo oscuro persiste al recargar la página?
- **Enigma 10.4**: ¿Las estadísticas se calculan correctamente desde los datos reales?
