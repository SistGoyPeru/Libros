# Capítulo 3: Las Funciones del Conocimiento

## Funciones

---

Camila tenía un problema. Estaba copiando y pegando el mismo código en varias partes de su archivo.

—Mira esto —le dijo a Diego, señalando la pantalla:

```javascript
// Validar usuario
if (usuario.logueado) {
  console.log("Bienvenido, " + usuario.nombre);
}

// En otra parte del código...
if (otroUsuario.logueado) {
  console.log("Bienvenido, " + otroUsuario.nombre);
}

// Y otra vez...
if (admin.logueado) {
  console.log("Bienvenido, " + admin.nombre);
}
```

—Estás repitiendo la misma lógica —dijo Diego—. En programación, esto se llama **código duplicado** y es malo. ¿Por qué?

1. Si necesitas cambiar el mensaje de bienvenida, tienes que cambiarlo en tres lugares.
2. Es más fácil cometer errores.
3. El código es más largo de lo necesario.

La solución: **funciones**.

---

## Funciones declaradas

—Una función es un bloque de código reutilizable que hace una tarea específica.

```javascript
// Declarar una función
function saludar(nombre) {
  console.log(`Hola, ${nombre}! Bienvenido a AprendeYa.`);
}

// Llamar (ejecutar) la función
saludar("Camila");
saludar("Diego");
saludar("Valeria");
```

—La función `saludar` recibe un **parámetro** (`nombre`) y ejecuta el código dentro de las llaves. Cada vez que la llamas, se ejecuta con el valor que le pases.

### Parámetros y argumentos

```javascript
function sumar(a, b) {
  return a + b;
}

let resultado = sumar(5, 3);
console.log(resultado); // 8
```

- `a` y `b` son **parámetros** (los nombres que usa la función)
- `5` y `3` son **argumentos** (los valores reales que pasas)

### Return

La palabra clave `return` devuelve un valor desde la función. Sin `return`, la función devuelve `undefined`.

```javascript
function multiplicar(x, y) {
  return x * y;
  console.log("Esto nunca se ejecuta"); // Código muerto
}

let producto = multiplicar(4, 5);
console.log(producto); // 20
```

—Todo lo que esté después de `return` no se ejecuta —explicó Diego—. El `return` termina la función.

---

## Funciones expresadas

—Hay otra forma de crear funciones: asignarlas a una variable.

```javascript
// Función expresada
const saludar = function(nombre) {
  return `Hola, ${nombre}!`;
};

console.log(saludar("Camila")); // "Hola, Camila!"
```

La diferencia principal: las **funciones declaradas** pueden llamarse antes de su declaración (hoisting), las **funciones expresadas** no.

```javascript
// Esto funciona (función declarada)
console.log(despedir("Camila"));
function despedir(nombre) {
  return `Adiós, ${nombre}!`;
}

// Esto da error (función expresada)
console.log(despedir2("Camila")); // ReferenceError
const despedir2 = function(nombre) {
  return `Adiós, ${nombre}!`;
};
```

---

## Arrow functions

—JavaScript moderno introdujo las **arrow functions** —dijo Diego—. Son una forma más corta de escribir funciones.

```javascript
// Función tradicional
const sumarTradicional = function(a, b) {
  return a + b;
};

// Arrow function
const sumarFlecha = (a, b) => {
  return a + b;
};

// Arrow function aún más corta (return implícito)
const sumarCorta = (a, b) => a + b;

console.log(sumarCorta(5, 3)); // 8
```

Si la arrow function tiene un solo parámetro, se pueden omitir los paréntesis:

```javascript
const cuadrado = x => x * x;
console.log(cuadrado(4)); // 16
```

Si no tiene parámetros, se usan paréntesis vacíos:

```javascript
const saludar = () => "Hola, mundo!";
```

—Las arrow functions son muy usadas en JavaScript moderno —dijo Diego—. Las verás mucho en arrays, eventos y promesas.

---

## Scope (ámbito)

—¿Dónde vive una variable? —preguntó Diego—. Eso es el **scope**.

### Scope global

Las variables declaradas fuera de cualquier función son globales: accesibles desde cualquier parte.

```javascript
const nombreGlobal = "Soy global";

function mostrarNombre() {
  console.log(nombreGlobal); // Accesible
}

mostrarNombre();
console.log(nombreGlobal); // Accesible
```

### Scope local (de función)

Las variables declaradas dentro de una función solo existen dentro de ella.

```javascript
function crearMensaje() {
  const mensajeLocal = "Soy local";
  console.log(mensajeLocal); // Accesible aquí
}

crearMensaje();
console.log(mensajeLocal); // ReferenceError: no existe fuera
```

### Scope de bloque (let y const)

`let` y `const` tienen scope de bloque (entre llaves `{}`), a diferencia de `var`.

```javascript
if (true) {
  var vieja = "Soy var";  // Scope global
  let moderna = "Soy let"; // Scope de bloque
  const constante = "Soy const"; // Scope de bloque
}

console.log(vieja);    // "Soy var" (accesible)
console.log(moderna);  // ReferenceError
console.log(constante); // ReferenceError
```

---

## Hoisting

—JavaScript tiene un comportamiento peculiar llamado **hoisting** (elevación). Las declaraciones de funciones y `var` se "elevan" al inicio de su contexto.

```javascript
// Esto funciona por hoisting
console.log(sumar(2, 3)); // 5

function sumar(a, b) {
  return a + b;
}
```

Con `var`, la declaración se eleva pero la asignación no:

```javascript
console.log(nombre); // undefined (no error)
var nombre = "Camila";

// Es como si JS interpretara:
var nombre;
console.log(nombre); // undefined
nombre = "Camila";
```

Con `let` y `const`, el hoisting existe pero no se puede acceder a la variable antes de su declaración (Temporal Dead Zone):

```javascript
console.log(edad); // ReferenceError
let edad = 27;
```

---

## Organizando la plataforma con funciones

Camila aplicó lo aprendido para organizar su código:

```javascript
// Funciones de utilidad
function obtenerSaludo(nombre, hora) {
  if (hora < 12) return `Buenos días, ${nombre}!`;
  if (hora < 18) return `Buenas tardes, ${nombre}!`;
  return `Buenas noches, ${nombre}!`;
}

function puedeAccederAlCurso(usuario, curso) {
  if (!usuario.logueado) return false;
  if (curso.gratuito) return true;
  return usuario.suscripcionActiva;
}

function calcularProgreso(leccionesCompletadas, totalLecciones) {
  if (totalLecciones === 0) return 0;
  return Math.round((leccionesCompletadas / totalLecciones) * 100);
}

// Uso de las funciones
const camila = { nombre: "Camila Ríos", logueado: true, suscripcionActiva: true };
const cursoJS = { titulo: "JavaScript Básico", gratuito: false };

console.log(obtenerSaludo(camila.nombre, 10)); // "Buenos días, Camila Ríos!"
console.log(puedeAccederAlCurso(camila, cursoJS)); // true
console.log(calcularProgreso(3, 10)); // 30
```

—Ahora el código es más legible, reutilizable y fácil de mantener —dijo Diego—. Si necesitas cambiar el saludo, solo lo haces en un lugar.

---

## Enigmas del Capítulo 3

### Enigma 3.1: Tu primera función

Crea una función llamada `esMayorDeEdad` que reciba una edad y devuelva `true` si es mayor o igual a 18, `false` en caso contrario. Prueba con 15, 18, 21 y 0.

### Enigma 3.2: Calculadora básica

Crea tres funciones: `sumar(a, b)`, `restar(a, b)`, `multiplicar(a, b)`. Luego crea una función `calculadora(operacion, a, b)` que use las funciones anteriores según el valor de `operacion` ("suma", "resta", "multiplica").

### Enigma 3.3: Validación de formulario

Crea una función `validarEmail(email)` que:
- Devuelva `true` si el email contiene un `@` y un `.` después del `@`
- Devuelva `false` en caso contrario
Usa `includes()` para verificar. Prueba con: "camila@email.com", "invalido@", "sinarroba.com".

### Enigma 3.4: Conversión de temperatura

Escribe una función flecha `celsiusAFahrenheit(celsius)` que convierta grados Celsius a Fahrenheit usando la fórmula: `F = C * 9/5 + 32`. Prueba con 0 (debe dar 32) y 100 (debe dar 212).

---

## Lo que aprendiste

- Las **funciones** encapsulan código reutilizable
- **Parámetros** son los nombres; **argumentos** son los valores
- `return` devuelve un valor y termina la función
- **Funciones declaradas** vs **funciones expresadas**
- **Arrow functions**: sintaxis moderna y concisa `() => {}`
- **Scope global** vs **scope local** vs **scope de bloque**
- **Hoisting**: elevación de declaraciones
- Las funciones hacen el código más **modular** y **mantenible**

---

Diego se levantó y estiró los brazos.

—Mañana vamos a manejar listas de cursos y estudiantes. Arrays y objetos. Ahí las funciones se vuelven aún más poderosas.

Camila miró su código. Ahora tenía funciones limpias y reutilizables. La plataforma comenzaba a tener estructura. Y ella comenzaba a pensar como programadora.
