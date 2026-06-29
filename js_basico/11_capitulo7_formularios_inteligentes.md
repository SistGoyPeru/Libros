# Capítulo 7: Formularios Inteligentes

## Formularios y Validación

---

—La plataforma necesita un formulario de registro —dijo Marco, el CEO, en la reunión matutina—. Los inversores quieren ver que podemos capturar usuarios.

Camila abrió su editor. Había diseñado un formulario hermoso en Figma: campos para nombre, email, contraseña, y un botón de registro. Pero en el código, el formulario no hacía nada.

—Hoy vamos a solucionar eso —dijo Diego.

---

## El evento submit

—El evento más importante de un formulario es **submit**. Se dispara cuando el usuario intenta enviarlo.

```html
<form id="form-registro">
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre">
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  
  <label for="password">Contraseña:</label>
  <input type="password" id="password" name="password">
  
  <button type="submit">Registrarse</button>
</form>
```

```javascript
const formulario = document.querySelector("#form-registro");

formulario.addEventListener("submit", function(event) {
  event.preventDefault(); // ¡Importante! Evita recargar la página
  console.log("Formulario enviado");
});
```

—`preventDefault()` evita el comportamiento por defecto del formulario, que es recargar la página. Sin esto, perderías todos los datos en JavaScript.

---

## Eventos de formulario

### input

Se dispara cada vez que el valor del campo cambia.

```javascript
const inputNombre = document.querySelector("#nombre");

inputNombre.addEventListener("input", function() {
  console.log(`Valor actual: ${this.value}`);
});
```

### change

Se dispara cuando el campo pierde el foco y su valor ha cambiado.

```javascript
const inputEmail = document.querySelector("#email");

inputEmail.addEventListener("change", function() {
  console.log(`Email cambiado a: ${this.value}`);
});
```

### focus y blur

```javascript
inputNombre.addEventListener("focus", function() {
  this.style.borderColor = "#3498db";
});

inputNombre.addEventListener("blur", function() {
  this.style.borderColor = "#ccc";
  validarNombre(this.value);
});
```

---

## Validación básica

—Validar significa verificar que los datos ingresados cumplen ciertas reglas antes de procesarlos.

```javascript
const formulario = document.querySelector("#form-registro");
const errorNombre = document.querySelector("#error-nombre");
const errorEmail = document.querySelector("#error-email");
const errorPassword = document.querySelector("#error-password");

function validarNombre(nombre) {
  if (nombre.trim() === "") {
    errorNombre.textContent = "El nombre es obligatorio";
    return false;
  }
  if (nombre.trim().length < 3) {
    errorNombre.textContent = "El nombre debe tener al menos 3 caracteres";
    return false;
  }
  errorNombre.textContent = "";
  return true;
}

function validarEmail(email) {
  if (email.trim() === "") {
    errorEmail.textContent = "El email es obligatorio";
    return false;
  }
  if (!email.includes("@") || !email.includes(".")) {
    errorEmail.textContent = "Ingresa un email válido";
    return false;
  }
  errorEmail.textContent = "";
  return true;
}

function validarPassword(password) {
  if (password.length < 6) {
    errorPassword.textContent = "La contraseña debe tener al menos 6 caracteres";
    return false;
  }
  errorPassword.textContent = "";
  return true;
}

formulario.addEventListener("submit", function(event) {
  event.preventDefault();
  
  const nombre = document.querySelector("#nombre").value;
  const email = document.querySelector("#email").value;
  const password = document.querySelector("#password").value;
  
  const nombreValido = validarNombre(nombre);
  const emailValido = validarEmail(email);
  const passwordValida = validarPassword(password);
  
  if (nombreValido && emailValido && passwordValida) {
    console.log("Registro exitoso!", { nombre, email, password });
    // Aquí iría el código para enviar los datos al servidor
  } else {
    console.log("Corrige los errores del formulario");
  }
});
```

---

## Expresiones regulares básicas

—Para validaciones más potentes, usamos **expresiones regulares (regex)**. Son patrones que describen cadenas de texto.

```javascript
// Validar email con regex
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function validarEmailRegex(email) {
  return emailRegex.test(email);
}

console.log(validarEmailRegex("camila@email.com")); // true
console.log(validarEmailRegex("invalido@"));        // false
```

### Patrones útiles:

```javascript
// Solo letras (incluyendo espacios)
const soloLetras = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;

// Solo números
const soloNumeros = /^\d+$/;

// Teléfono (formato: 999-999-999)
const telefono = /^\d{3}-\d{3}-\d{3}$/;

// URL básica
const url = /^https?:\/\/.+/;

// Probar
console.log(soloLetras.test("Camila Ríos"));  // true
console.log(soloLetras.test("Camila123"));     // false
```

---

## Validación en tiempo real

—Lo más profesional es validar mientras el usuario escribe, no solo al enviar.

```javascript
const inputNombre = document.querySelector("#nombre");
const inputEmail = document.querySelector("#email");
const inputPassword = document.querySelector("#password");

inputNombre.addEventListener("blur", function() {
  validarNombre(this.value);
});

inputEmail.addEventListener("input", function() {
  validarEmail(this.value);
});

inputPassword.addEventListener("input", function() {
  validarPassword(this.value);
});

// También validar al escribir en el nombre
inputNombre.addEventListener("input", function() {
  if (this.value.length >= 3) {
    errorNombre.textContent = "";
  }
});
```

### Mostrar errores visualmente

```javascript
function mostrarError(input, mensaje) {
  const errorDiv = input.nextElementSibling;
  errorDiv.textContent = mensaje;
  input.classList.add("input-error");
  input.classList.remove("input-success");
}

function mostrarExito(input) {
  const errorDiv = input.nextElementSibling;
  errorDiv.textContent = "";
  input.classList.remove("input-error");
  input.classList.add("input-success");
}
```

**CSS asociado:**
```css
.input-error {
  border: 2px solid #e74c3c;
  background-color: #fdf0ef;
}

.input-success {
  border: 2px solid #2ecc71;
  background-color: #f0fdf4;
}

.error-mensaje {
  color: #e74c3c;
  font-size: 0.85em;
  margin-top: 4px;
}
```

---

## El formulario de registro de AprendeYa

Camila integró todo en un formulario completo:

```javascript
const formulario = document.querySelector("#form-registro");

// Validación en tiempo real
document.querySelectorAll("#form-registro input").forEach(input => {
  input.addEventListener("blur", function() {
    validarCampo(this);
  });
  
  input.addEventListener("input", function() {
    if (this.classList.contains("input-error")) {
      validarCampo(this);
    }
  });
});

function validarCampo(input) {
  const valor = input.value.trim();
  const errorDiv = input.nextElementSibling;
  
  if (input.required && valor === "") {
    mostrarError(input, "Este campo es obligatorio");
    return false;
  }
  
  if (input.type === "email") {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(valor)) {
      mostrarError(input, "Ingresa un email válido");
      return false;
    }
  }
  
  if (input.type === "password" && valor.length < 6) {
    mostrarError(input, "Mínimo 6 caracteres");
    return false;
  }
  
  mostrarExito(input);
  return true;
}

formulario.addEventListener("submit", function(event) {
  event.preventDefault();
  
  const inputs = this.querySelectorAll("input");
  let formularioValido = true;
  
  inputs.forEach(input => {
    if (!validarCampo(input)) {
      formularioValido = false;
    }
  });
  
  if (formularioValido) {
    const datos = {
      nombre: document.querySelector("#nombre").value,
      email: document.querySelector("#email").value
    };
    console.log("Usuario registrado:", datos);
    alert("¡Registro exitoso! Bienvenido a AprendeYa.");
    this.reset(); // Limpiar formulario
  } else {
    alert("Corrige los errores antes de continuar");
  }
});
```

---

## Enigmas del Capítulo 7

### Enigma 7.1: Validación de edad

Agrega un campo "edad" al formulario que valide que:
- Es obligatorio
- Es un número
- Está entre 18 y 120 años

### Enigma 7.2: Confirmación de contraseña

Agrega un campo "confirmar contraseña". Valida que sea igual al campo contraseña antes de enviar el formulario. Muestra error si no coinciden.

### Enigma 7.3: Contador de caracteres

Crea un textarea para "biografía" con un contador que muestre los caracteres restantes (máximo 200). El contador debe actualizarse en tiempo real y ponerse rojo cuando se exceda.

### Enigma 7.4: Validación de nombre de usuario

Crea una función que valide un nombre de usuario:
- Entre 4 y 15 caracteres
- Solo letras minúsculas, números y guión bajo
- No puede empezar con número
Usa la expresión regular: `/^[a-z][a-z0-9_]{3,14}$/`

---

## Lo que aprendiste

- **`submit`**: evento principal de formularios
- **`preventDefault()`**: evita la recarga de página
- Eventos: `input` (tiempo real), `change` (al perder foco), `focus`, `blur`
- **Validación**: verificar datos antes de procesarlos
- **Expresiones regulares (regex)**: patrones para validar texto
- Validación en **tiempo real** vs validación al enviar
- Retroalimentación visual con clases CSS

---

Camila probó el formulario una y otra vez. Ingresaba datos inválidos y veía los mensajes de error aparecer. Ingresaba datos correctos y veía los bordes verdes.

—Esto es adictivo —dijo.

—La validación es una de las cosas que más diferencia una página profesional de una amateur —respondió Diego—. Buen trabajo.

—Mañana —dijo Camila— quiero que los usuarios no pierdan su progreso al cerrar el navegador.

Diego sonrió. —Eso es justo lo que veremos mañana.
