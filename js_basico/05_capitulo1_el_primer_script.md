# Capítulo 1: El Primer Script

## Introducción a JS, Variables y Tipos de Datos

---

—¿Por dónde empezamos? —preguntó Camila, con el cursor parpadeando en una pantalla en blanco del navegador.

Diego se sentó a su lado, abrió Chrome y presionó F12.

—El navegador tiene herramientas ocultas —dijo—. Esto se llama **Consola del Desarrollador**. Es como el taller del mecánico, pero para páginas web.

Camila vio cómo se abría un panel dividido: HTML en una pestaña, red en otra, y una pestaña llamada "Console" con un cursor parpadeante.

—Escribe esto —dijo Diego, pasándole una hoja con una línea escrita:

```javascript
console.log("Hola, AprendeYa!");
```

Camila tecleó la línea y presionó Enter. En la consola apareció:

```
Hola, AprendeYa!
```

—¡Funcionó! —exclamó—. ¿Qué acabo de hacer?

—Acabas de escribir tu primer **script** en **JavaScript**. El lenguaje que le da vida a las páginas web.

---

## ¿Qué es JavaScript?

**JavaScript** es un lenguaje de programación que se ejecuta en el navegador del usuario. Mientras que **HTML** define la estructura de una página y **CSS** define su apariencia, JavaScript define su **comportamiento**.

| Tecnología | Función | Analogía |
|------------|---------|----------|
| HTML | Estructura | El esqueleto de una casa |
| CSS | Apariencia | Las paredes pintadas, los muebles |
| JavaScript | Comportamiento | Las tuberías, la electricidad, la calefacción |

—¿Y por qué se llama JavaScript si no tiene nada que ver con Java? —preguntó Camila.

Diego rió.

—Buena pregunta. Fue una estrategia de marketing en los 90. Java era muy popular, así que llamaron a este nuevo lenguaje "JavaScript" para montarse en la ola. No tienen nada que ver.

### ¿Dónde se ejecuta JavaScript?

JavaScript se puede ejecutar en:

1. **El navegador** — La forma más común. Chrome, Firefox, Edge, Safari.
2. **Node.js** — Un entorno que permite ejecutar JavaScript fuera del navegador (en el servidor).
3. **Aplicaciones híbridas** — Como Electron (VS Code, Slack, Discord).

Para este libro, trabajaremos exclusivamente en el navegador.

### ¿Cómo incluir JavaScript en una página?

Hay tres formas:

**1. JavaScript en línea (inline):**

```html
<button onclick="alert('Hola!')">Haz clic</button>
```

**2. Dentro de una etiqueta `<script>`:**

```html
<script>
  console.log("Esto está dentro del HTML");
</script>
```

**3. Archivo externo (recomendado):**

```html
<script src="script.js"></script>
```

---

## La consola del navegador

La **consola** es la herramienta más importante para un desarrollador JavaScript. Permite:

- Ejecutar código en tiempo real
- Ver mensajes de error
- Inspeccionar el valor de las variables
- Depurar el comportamiento del programa

Para abrirla:

| Navegador | Atajo Windows | Atajo Mac |
|-----------|--------------|-----------|
| Chrome | F12 o Ctrl + Shift + I | Cmd + Option + I |
| Firefox | F12 o Ctrl + Shift + I | Cmd + Option + I |
| Edge | F12 o Ctrl + Shift + I | Cmd + Option + I |

### console.log()

La función `console.log()` imprime un mensaje en la consola. Es la forma más básica de ver qué está pasando en tu código.

```javascript
console.log("Mensaje de texto");
console.log(42);
console.log(true);
console.log([1, 2, 3]);
console.log({ nombre: "Camila" });
```

—Úsalo siempre que tengas dudas —dijo Diego—. Es como decirle al código "muéstrame qué tienes aquí".

---

## Variables: guardando información

—Ahora —continuó Diego—, imagina que necesitas guardar el nombre de un usuario, su edad, o el título de un curso. Para eso sirven las **variables**.

Las variables son contenedores que almacenan datos. En JavaScript hay tres formas de declararlas:

### var (la forma antigua)

```javascript
var nombre = "Camila";
var edad = 27;
```

`var` tiene un comportamiento especial con el **scope** que puede causar bugs difíciles de encontrar. Hoy en día se recomienda no usarlo.

### let (la forma moderna)

```javascript
let nombre = "Camila";
let edad = 27;
nombre = "Valeria"; // Se puede reasignar
```

`let` se usa para variables que pueden cambiar de valor.

### const (constante)

```javascript
const PI = 3.1416;
const SITE_NAME = "AprendeYa";
// PI = 3; // Error: no se puede reasignar una constante
```

`const` se usa para valores que no deben cambiar. Es inmutable (no se puede reasignar).

—La regla de oro —dijo Diego— es: usa `const` por defecto. Solo usa `let` cuando sepas que la variable va a cambiar. Nunca uses `var` en código moderno.

| Declaración | Se puede reasignar | Scope | Recomendado |
|-------------|-------------------|-------|-------------|
| `var` | Sí | Función | No |
| `let` | Sí | Bloque | Sí (cuando cambia) |
| `const` | No | Bloque | Sí (por defecto) |

---

## Tipos de datos

JavaScript tiene varios tipos de datos. Diego los fue escribiendo uno por uno en la consola mientras Camila observaba.

### String (cadena de texto)

```javascript
let nombre = "Camila";
let apellido = 'Ríos';
let mensaje = `Bienvenida, ${nombre}!`; // Template string
```

Las **template strings** (con backticks) permiten incrustar variables dentro del texto usando `${}`.

### Number (número)

```javascript
let edad = 27;
let precio = 29.99;
let temperatura = -5;
```

JavaScript no diferencia entre enteros y decimales: todo es `number`.

### Boolean (booleano)

```javascript
let estaLogueado = true;
let esMayorDeEdad = false;
```

Solo dos valores: `true` (verdadero) o `false` (falso).

### Null (nulo)

```javascript
let seleccion = null; // Intencionalmente vacío
```

Representa la ausencia intencional de un valor.

### Undefined (indefinido)

```javascript
let curso;
console.log(curso); // undefined
```

Significa que una variable ha sido declarada pero no tiene valor asignado.

### typeof

El operador `typeof` te dice el tipo de un valor:

```javascript
console.log(typeof "Hola");     // "string"
console.log(typeof 42);         // "number"
console.log(typeof true);       // "boolean"
console.log(typeof null);       // "object" (error histórico de JS)
console.log(typeof undefined);  // "undefined"
```

---

## Comentarios

—El código se escribe para las máquinas —dijo Diego—, pero se lee para los humanos. Los **comentarios** te ayudan a explicar qué hace tu código.

```javascript
// Esto es un comentario de una línea

/*
  Esto es un comentario
  de varias líneas
  muy útil para explicar
  bloques de código
*/
```

Los comentarios no se ejecutan. Son solo para quien lea el código (incluyendo tu yo del futuro).

---

## El primer problema de Camila

Camila necesitaba mostrar el nombre del usuario en la plataforma. Diego la guió:

```javascript
const usuario = "Camila";
let saludo = "Bienvenida a AprendeYa, " + usuario + "!";
console.log(saludo);

// Con template strings es más fácil:
let saludoModerno = `Bienvenida a AprendeYa, ${usuario}!`;
console.log(saludoModerno);
```

—¿Ves la diferencia? —preguntó Diego—. Las **template strings** hacen el código más legible.

—¿Y si el usuario no está logueado? —preguntó Camila.

—Buena pregunta. Eso lo veremos cuando aprendamos condicionales. Por ahora, guardemos el nombre del usuario en una variable y mostrémoslo.

Camila abrió su editor y creó su primer archivo: `app.js`. Escribió:

```javascript
// Datos del usuario
const nombreUsuario = "Camila Ríos";
let edadUsuario = 27;
const esEstudiante = true;

// Mensaje de bienvenida
console.log(`Hola, ${nombreUsuario}!`);
console.log(`Edad: ${edadUsuario}`);
console.log(`¿Es estudiante? ${esEstudiante}`);
```

—Perfecto —dijo Diego—. Acabas de crear tu primer script con variables y tipos de datos.

---

## Enigmas del Capítulo 1

### Enigma 1.1: Tu primer programa

Abre la consola del navegador y escribe un programa que:
1. Declare una variable `const` con tu nombre
2. Declare una variable `let` con tu edad
3. Declare una variable `const` con tu lenguaje favorito (por ahora, JavaScript)
4. Muestre un saludo en consola usando template strings

### Enigma 1.2: Detecta el tipo

Usa `typeof` para determinar el tipo de los siguientes valores. Escribe en consola:
```javascript
typeof "42"
typeof 42
typeof true
typeof null
typeof undefined
typeof "true"
```
¿Hay algún resultado que te sorprenda?

### Enigma 1.3: El mensaje de la plataforma

Crea una variable `const` llamada `curso` con el valor "JavaScript Básico". Crea otra variable `let` llamada `progreso` con el valor 15. Usa template strings para mostrar en consola: "Estás tomando el curso JavaScript Básico. Tu progreso es 15%."

### Enigma 1.4: Conversión de tipos

¿Qué crees que imprimen estos console.log? Escríbelos en la consola para verificarlo:
```javascript
console.log("5" + 3);
console.log("5" - 3);
console.log("5" * "3");
console.log("Hola" + 5);
```

---

## Lo que aprendiste

- **JavaScript** es el lenguaje que da interactividad a la web
- La **consola del navegador** es tu herramienta principal de depuración
- Las **variables** guardan datos: `const` (constante) y `let` (variable)
- Los **tipos de datos** principales: string, number, boolean, null, undefined
- `typeof` te dice el tipo de un valor
- **Template strings** con backticks y `${}` para interpolar variables
- Los **comentarios** hacen tu código más legible

---

Camila guardó su archivo y sonrió. Había escrito su primer código JavaScript. No era mucho, pero era el primer paso de un viaje que cambiaría la forma en que veía la web.

—Mañana —dijo Diego, levantándose—, vamos a hacer que la plataforma tome decisiones. Prepárate.
