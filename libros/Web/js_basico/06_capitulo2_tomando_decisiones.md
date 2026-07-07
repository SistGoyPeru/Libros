# Capítulo 2: Tomando Decisiones

## Operadores y Condicionales

---

—Buenos días —dijo Diego, dejando una taza de café en el escritorio de Camila—. Hoy vamos a hacer que la plataforma piense.

—¿Piense? —Camila levantó una ceja.

—Sí. Hasta ahora solo guardamos datos. Pero un programa sin decisiones es como un semáforo que siempre muestra verde: inútil. Necesitamos **condicionales** para que el código reaccione según el contexto.

Camila abrió su editor. Tenía lista la estructura de la plataforma: un menú, una sección de cursos, un área de perfil. Pero todo se mostraba igual para todos los usuarios.

—El primer problema —dijo Diego—: necesitamos saber si el usuario está logueado para mostrar contenido personalizado.

---

## Operadores aritméticos

—Antes de las decisiones, necesitamos las herramientas para comparar y calcular —Diego escribió en la consola:

```javascript
// Operadores aritméticos básicos
let suma = 10 + 5;       // 15
let resta = 10 - 5;      // 5
let multiplicacion = 10 * 5;  // 50
let division = 10 / 5;   // 2
let modulo = 10 % 3;     // 1 (resto de la división)
```

—El operador `%` (módulo) es útil para saber si un número es par o impar, o para ciclos —explicó Diego.

---

## Operadores de comparación

—Para tomar decisiones, necesitamos comparar valores.

```javascript
// Comparación
console.log(5 == "5");   // true (compara solo valor)
console.log(5 === "5");  // false (compara valor y tipo)
console.log(5 != "5");   // false
console.log(5 !== "5");  // true
console.log(10 > 5);     // true
console.log(10 < 5);     // false
console.log(10 >= 10);   // true
console.log(10 <= 5);    // false
```

—La regla de oro —dijo Diego—: **siempre usa `===` y `!==`**. El `==` y `!=` hacen conversiones automáticas que pueden causar bugs sutiles.

| Operador | Significado | Ejemplo true |
|----------|-------------|--------------|
| `===` | Estrictamente igual | `5 === 5` |
| `!==` | Estrictamente diferente | `5 !== "5"` |
| `>` | Mayor que | `10 > 5` |
| `<` | Menor que | `3 < 7` |
| `>=` | Mayor o igual | `5 >= 5` |
| `<=` | Menor o igual | `3 <= 5` |

---

## Operadores lógicos

—Ahora —continuó Diego—, ¿qué pasa si necesitamos verificar varias condiciones a la vez?

```javascript
let edad = 18;
let tienePermiso = true;

// AND (&&): ambas deben ser true
console.log(edad >= 18 && tienePermiso);  // true

// OR (||): al menos una debe ser true
console.log(edad >= 18 || tienePermiso);  // true

// NOT (!): invierte el valor
console.log(!true);   // false
console.log(!false);  // true
```

Diego dibujó una tabla en su cuaderno:

```javascript
// Tabla de verdad de AND (&&)
console.log(true && true);   // true
console.log(true && false);  // false
console.log(false && true);  // false
console.log(false && false); // false

// Tabla de verdad de OR (||)
console.log(true || true);   // true
console.log(true || false);  // true
console.log(false || true);  // true
console.log(false || false); // false
```

---

## If / Else if / Else

—Ahora sí —dijo Diego—. Vamos a tomar decisiones.

La primera función que Camila necesitaba: verificar si un usuario está logueado y mostrar contenido diferente.

```javascript
const usuarioLogueado = true;
const nombreUsuario = "Camila";

if (usuarioLogueado) {
  console.log(`Bienvenida de nuevo, ${nombreUsuario}!`);
} else {
  console.log("Bienvenido. Por favor, inicia sesión.");
}
```

—¿Y si necesito más opciones? —preguntó Camila.

—Usas `else if`:

```javascript
const rol = "admin";

if (rol === "admin") {
  console.log("Acceso total a la plataforma");
} else if (rol === "instructor") {
  console.log("Acceso para crear y editar cursos");
} else if (rol === "estudiante") {
  console.log("Acceso para ver cursos y progreso");
} else {
  console.log("Rol no reconocido");
}
```

Camila aplicó esto a su plataforma:

```javascript
const usuario = {
  nombre: "Camila Ríos",
  logueado: true,
  rol: "admin"
};

if (usuario.logueado) {
  console.log(`Hola, ${usuario.nombre}`);
  if (usuario.rol === "admin") {
    console.log("Tienes permisos de administrador");
  }
} else {
  console.log("Por favor, inicia sesión");
}
```

—¡Un `if` dentro de otro `if`! —exclamó Camila.

—Se llama **anidamiento**. Úsalo con moderación; demasiados niveles hacen el código difícil de leer.

---

## Switch

—Cuando tienes muchas condiciones basadas en un mismo valor, `switch` puede ser más limpio:

```javascript
const dia = "lunes";

switch (dia) {
  case "lunes":
    console.log("Inicio de semana. Nuevo curso disponible.");
    break;
  case "martes":
  case "miercoles":
  case "jueves":
    console.log("Día de estudio. Sigue tu progreso.");
    break;
  case "viernes":
    console.log("Viernes de repaso. Prepara tus dudas.");
    break;
  case "sabado":
  case "domingo":
    console.log("Fin de semana. Disfruta y aprende algo nuevo.");
    break;
  default:
    console.log("Día no válido");
}
```

—El `break` es importante —explicó Diego—. Sin él, el código sigue ejecutando los casos siguientes aunque ya haya encontrado una coincidencia. Eso se llama **fall-through**.

---

## Operador ternario

—Hay un atajo para condicionales simples —dijo Diego—. El **operador ternario**:

```javascript
// Sintaxis: condición ? valorSiTrue : valorSiFalse

const edad = 20;
const mensaje = edad >= 18 ? "Eres mayor de edad" : "Eres menor de edad";
console.log(mensaje);

// Es equivalente a:
let mensajeLargo;
if (edad >= 18) {
  mensajeLargo = "Eres mayor de edad";
} else {
  mensajeLargo = "Eres menor de edad";
}
```

—Úsalo para condicionales simples de una línea. Para lógica más compleja, usa `if/else`.

---

## El problema real de Camila

La plataforma necesitaba mostrar el progreso del usuario con un mensaje personalizado según el porcentaje:

```javascript
const progreso = 65;
let mensajeProgreso;

if (progreso === 0) {
  mensajeProgreso = "Aún no has empezado el curso. ¡Anímate!";
} else if (progreso < 25) {
  mensajeProgreso = "Has comenzado. ¡Sigue así!";
} else if (progreso < 50) {
  mensajeProgreso = "Ya llevas menos de la mitad. ¡No te rindas!";
} else if (progreso < 75) {
  mensajeProgreso = "Más de la mitad. ¡Estás avanzando!";
} else if (progreso < 100) {
  mensajeProgreso = "Casi llegas. ¡Finaliza el curso!";
} else {
  mensajeProgreso = "¡Felicidades! Has completado el curso.";
}

console.log(mensajeProgreso);
```

—¿Y si el progreso es negativo o mayor a 100? —preguntó Camila.

—Buena observación. Validar los datos antes de usarlos es una buena práctica:

```javascript
function obtenerMensajeProgreso(progreso) {
  if (progreso < 0 || progreso > 100) {
    return "Progreso inválido";
  }
  
  if (progreso === 0) return "Aún no has empezado";
  if (progreso < 25) return "Has comenzado. ¡Sigue así!";
  if (progreso < 50) return "Ya llevas menos de la mitad";
  if (progreso < 75) return "Más de la mitad. ¡Estás avanzando!";
  if (progreso < 100) return "Casi llegas";
  return "¡Felicidades! Has completado el curso.";
}

console.log(obtenerMensajeProgreso(65));
```

—Las funciones las veremos pronto —dijo Diego—. Pero mira cómo el código se vuelve más legible cuando validas primero.

---

## Enigmas del Capítulo 2

### Enigma 2.1: Calculadora de notas

Crea una variable `let nota = 85`. Usando condicionales, muestra en consola:
- "Excelente" si la nota es >= 90
- "Bien" si la nota es >= 70 y < 90
- "Regular" si la nota es >= 50 y < 70
- "Necesitas mejorar" si la nota es < 50

### Enigma 2.2: Acceso a la plataforma

Tres variables: `logueado` (boolean), `tieneSuscripcion` (boolean), `esAdmin` (boolean). Escribe un condicional que:
- Si está logueado Y (tiene suscripción O es admin): "Acceso concedido"
- Si está logueado pero no tiene suscripción ni es admin: "Debes adquirir una suscripción"
- Si no está logueado: "Por favor, inicia sesión"

### Enigma 2.3: Día laboral o finde

Usa `switch` con una variable `const dia = "sabado"`. Muestra si es "Día laboral" (lunes a viernes) o "Fin de semana" (sábado, domingo).

### Enigma 2.4: ¿Par o impar?

Usa el operador módulo `%` para determinar si un número es par o impar. Prueba con: `15`, `22`, `7`, `100`. Muestra en consola: "El número X es par" o "El número X es impar".

---

## Lo que aprendiste

- **Operadores aritméticos**: `+`, `-`, `*`, `/`, `%`
- **Operadores de comparación**: `===`, `!==`, `>`, `<`, `>=`, `<=`
- **Operadores lógicos**: `&&` (AND), `||` (OR), `!` (NOT)
- **`if/else if/else`**: Para decisiones con múltiples caminos
- **`switch`**: Alternativa limpia para múltiples casos
- **Operador ternario**: `condición ? valorTrue : valorFalse`
- La importancia de **validar datos** antes de procesarlos

---

—Buen trabajo —dijo Diego—. Ahora la plataforma ya puede distinguir entre un usuario logueado y uno que no lo está. Mañana veremos cómo organizar todo este código para no repetirnos.

Camila guardó su archivo. Por primera vez, sintió que el código no era solo instrucciones, sino una conversación: si esto, entonces aquello. Como la vida misma.
