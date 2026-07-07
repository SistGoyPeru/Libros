# Capítulo 4: Listas y Colecciones

## Arrays y Objetos

---

La plataforma "AprendeYa" tenía un catálogo de cursos. Camila los había diseñado en Figma, pero en el código eran solo texto estático en HTML.

—Necesitamos manejar listas de cursos, estudiantes y progreso —dijo Diego—. Para eso existen los **arrays** y los **objetos**.

---

## Arrays

—Un **array** es una lista ordenada de elementos. Piensa en una caja con compartimentos numerados.

```javascript
// Crear un array
const cursos = ["HTML Básico", "CSS Avanzado", "JavaScript Básico"];
const numeros = [1, 2, 3, 4, 5];
const mixto = ["Texto", 42, true, null, [1, 2, 3]];
const vacio = [];
```

### Acceder a elementos

Los arrays usan **índices** que empiezan desde 0.

```javascript
const frutas = ["manzana", "banana", "naranja"];

console.log(frutas[0]);  // "manzana"
console.log(frutas[1]);  // "banana"
console.log(frutas[2]);  // "naranja"
console.log(frutas[3]);  // undefined (no existe)
```

### Propiedad length

```javascript
console.log(frutas.length); // 3

const ultimoElemento = frutas[frutas.length - 1];
console.log(ultimoElemento); // "naranja"
```

### Métodos básicos

```javascript
const cursos = ["HTML", "CSS"];

// push: agrega al final
cursos.push("JavaScript");
console.log(cursos); // ["HTML", "CSS", "JavaScript"]

// pop: elimina el último
const ultimo = cursos.pop();
console.log(ultimo); // "JavaScript"
console.log(cursos); // ["HTML", "CSS"]

// unshift: agrega al inicio
cursos.unshift("Python");
console.log(cursos); // ["Python", "HTML", "CSS"]

// shift: elimina el primero
const primero = cursos.shift();
console.log(primero); // "Python"
console.log(cursos); // ["HTML", "CSS"]
```

### Métodos de iteración

—Estos son los más poderosos —dijo Diego—. Te permiten recorrer arrays sin usar bucles tradicionales.

**forEach**: ejecuta una función para cada elemento

```javascript
const cursos = ["HTML", "CSS", "JavaScript"];

cursos.forEach(function(curso, indice) {
  console.log(`${indice + 1}. ${curso}`);
});
// "1. HTML"
// "2. CSS"
// "3. JavaScript"
```

**map**: crea un nuevo array transformando cada elemento

```javascript
const numeros = [1, 2, 3, 4, 5];
const cuadrados = numeros.map(function(num) {
  return num * num;
});
console.log(cuadrados); // [1, 4, 9, 16, 25]

// Con arrow function:
const dobles = numeros.map(n => n * 2);
console.log(dobles); // [2, 4, 6, 8, 10]
```

**filter**: crea un nuevo array con los elementos que cumplen una condición

```javascript
const edades = [15, 22, 18, 30, 12, 17, 25];
const mayoresDeEdad = edades.filter(edad => edad >= 18);
console.log(mayoresDeEdad); // [22, 18, 30, 25]
```

**find**: encuentra el primer elemento que cumple una condición

```javascript
const usuarios = ["Ana", "Carlos", "María", "Pedro"];
const encontrado = usuarios.find(nombre => nombre.startsWith("M"));
console.log(encontrado); // "María"
```

---

## Objetos

—Si los arrays son listas ordenadas, los **objetos** son colecciones de propiedades con nombre.

```javascript
// Crear un objeto
const curso = {
  titulo: "JavaScript Básico",
  duracion: "10 horas",
  nivel: "Principiante",
  gratuito: false
};

// Acceder a propiedades (notación de punto)
console.log(curso.titulo);  // "JavaScript Básico"
console.log(curso.nivel);   // "Principiante"

// Acceder con corchetes
console.log(curso["titulo"]); // "JavaScript Básico"

// Modificar propiedades
curso.gratuito = true;
console.log(curso.gratuito); // true

// Agregar nuevas propiedades
curso.rating = 4.5;
console.log(curso.rating); // 4.5
```

### Objetos anidados

—Los objetos pueden contener otros objetos y arrays.

```javascript
const estudiante = {
  nombre: "Camila Ríos",
  edad: 27,
  cursos: ["HTML Básico", "CSS Avanzado"],
  direccion: {
    ciudad: "Lima",
    pais: "Perú"
  },
  progreso: {
    "HTML Básico": 100,
    "CSS Avanzado": 70
  }
};

console.log(estudiante.nombre);                // "Camila Ríos"
console.log(estudiante.cursos[0]);             // "HTML Básico"
console.log(estudiante.direccion.ciudad);      // "Lima"
console.log(estudiante.progreso["HTML Básico"]); // 100
```

### Métodos en objetos

—Los objetos también pueden tener funciones como propiedades. Se llaman **métodos**.

```javascript
const usuario = {
  nombre: "Camila",
  edad: 27,
  saludar: function() {
    return `Hola, soy ${this.nombre}`;
  },
  // Método con arrow function
  mostrarEdad: () => {
    return `Tengo ${usuario.edad} años`;
  }
};

console.log(usuario.saludar());    // "Hola, soy Camila"
console.log(usuario.mostrarEdad()); // "Tengo 27 años"
```

—La palabra clave `this` dentro de un método se refiere al objeto que contiene el método.

---

## JSON

—Hay un formato muy usado para intercambiar datos: **JSON** (JavaScript Object Notation). Es básicamente texto con la misma estructura que los objetos de JavaScript.

```javascript
// Objeto JavaScript
const cursoJS = {
  titulo: "JavaScript Básico",
  precio: 0,
  lecciones: 15
};

// Convertir a JSON (string)
const cursoJSON = JSON.stringify(cursoJS);
console.log(cursoJSON);
// '{"titulo":"JavaScript Básico","precio":0,"lecciones":15}'

// Convertir de JSON a objeto
const cursoObjeto = JSON.parse(cursoJSON);
console.log(cursoObjeto.titulo); // "JavaScript Básico"
```

—JSON es el lenguaje universal de intercambio de datos en la web. Lo usaremos en el capítulo 9 con APIs.

---

## Catálogo de cursos de AprendeYa

Camila organizó todo el catálogo de la plataforma:

```javascript
const catalogo = [
  {
    id: 1,
    titulo: "HTML para Principiantes",
    duracion: "5 horas",
    nivel: "principiante",
    gratuito: true,
    rating: 4.8
  },
  {
    id: 2,
    titulo: "CSS Avanzado",
    duracion: "8 horas",
    nivel: "intermedio",
    gratuito: false,
    rating: 4.5
  },
  {
    id: 3,
    titulo: "JavaScript Básico",
    duracion: "10 horas",
    nivel: "principiante",
    gratuito: true,
    rating: 4.9
  },
  {
    id: 4,
    titulo: "React: Tu primera app",
    duracion: "12 horas",
    nivel: "avanzado",
    gratuito: false,
    rating: 4.2
  }
];

// Filtrar cursos gratuitos
const cursosGratis = catalogo.filter(curso => curso.gratuito);
console.log(cursosGratis);
// Devuelve los cursos con gratuito: true

// Obtener solo los títulos
const titulos = catalogo.map(curso => curso.titulo);
console.log(titulos);
// ["HTML para Principiantes", "CSS Avanzado", "JavaScript Básico", "React: Tu primera app"]

// Encontrar un curso por ID
const cursoJS = catalogo.find(curso => curso.id === 3);
console.log(cursoJS.titulo); // "JavaScript Básico"

// Calcular rating promedio
const promedio = catalogo
  .map(curso => curso.rating)
  .reduce((total, rating) => total + rating, 0) / catalogo.length;
console.log(promedio.toFixed(2)); // "4.60"
```

—`reduce` es otro método poderoso —dijo Diego—. Reduce un array a un solo valor. Aprenderás a usarlo con la práctica.

---

## Enigmas del Capítulo 4

### Enigma 4.1: Tu lista de compras

Crea un array llamado `listaCompras` con 5 productos. Agrega un producto al final con `push`, elimina el primero con `shift`, y muestra el array final y su longitud.

### Enigma 4.2: Catálogo de cursos

Crea un array de objetos con 3 cursos (cada uno con `titulo`, `duracion`, `precio`). Usa `map` para obtener un array solo con los títulos. Usa `filter` para encontrar los cursos gratis (precio === 0).

### Enigma 4.3: Objeto estudiante

Crea un objeto `estudiante` con: `nombre`, `edad`, `cursos` (array), `direccion` (objeto con `ciudad`, `pais`). Agrega un método `presentarse()` que devuelva "Hola, soy [nombre] de [ciudad], [pais]".

### Enigma 4.4: Transformando datos

Dado el array `const nums = [5, 12, 8, 21, 3, 15]`:
1. Usa `filter` para obtener los números mayores a 10
2. Usa `map` para obtener el doble de cada número
3. Usa `find` para encontrar el primer número mayor a 10

---

## Lo que aprendiste

- **Arrays**: listas ordenadas `[elemento1, elemento2]`
- Índices empiezan en **0**
- **Métodos**: `push`, `pop`, `shift`, `unshift`, `length`
- **Iteración**: `forEach`, `map`, `filter`, `find`
- **Objetos**: colecciones clave-valor `{ clave: valor }`
- **Propiedades** y **métodos** en objetos
- `this` se refiere al objeto contenedor
- **JSON**: formato de intercambio de datos

---

Camila miró el catálogo de cursos funcionando como un array de objetos. La plataforma comenzaba a tener datos reales, no solo maquetas.

—Mañana —dijo Diego— vamos a conectar estos datos con la página. Vas a ver cómo el DOM cobra vida.

Camila sonrió. Por primera vez, sentía que estaba construyendo algo real.
