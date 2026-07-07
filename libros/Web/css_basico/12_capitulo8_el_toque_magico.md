# Capítulo 8: El Toque Mágico

*Tema: Transiciones y animaciones*

---

El sitio de "Cultura Viva" funcionaba. Se veía bien en todos los dispositivos. Pero había algo que Mateo notaba que faltaba: movimiento.

—Se siente estático —dijo Mateo, moviendo el mouse por la pantalla—. Los botones están ahí, pero no reaccionan. Los elementos aparecen, pero no hay fluidez.

—Eso es porque no tienes **transiciones** ni **animaciones** —dijo Carolina—. El movimiento en la web no es decorativo: guía al usuario, le da feedback, hace la experiencia más natural.

## Transition: La transición suave

—Las **transiciones** permiten que los cambios de estilo ocurran de forma gradual en lugar de instantánea.

```css
.boton {
  background-color: #8B0000;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.boton:hover {
  background-color: #a52a2a;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(139, 0, 0, 0.3);
}
```

—Ahora, al pasar el mouse, el botón cambia de color suavemente y se eleva un poco.

### Sintaxis de transition

```css
.elemento {
  /* Propiedad específica */
  transition: background-color 0.3s ease;

  /* Múltiples propiedades */
  transition: background-color 0.3s ease, transform 0.2s ease-in;

  /* Todas las propiedades */
  transition: all 0.3s ease;

  /* Shorthand completo: propiedad duración función retardo */
  transition: background-color 0.3s ease 0.1s;
}
```

### Funciones de temporización (easing)

| Función | Comportamiento |
|---------|---------------|
| `ease` | Inicio suave, fin suave (por defecto) |
| `linear` | Velocidad constante |
| `ease-in` | Inicio lento, aceleración al final |
| `ease-out` | Inicio rápido, desaceleración al final |
| `ease-in-out` | Lento al inicio y al final |
| `cubic-bezier(n,n,n,n)` | Curva personalizada |

## Transform: Transformar elementos

—**Transform** modifica la apariencia de un elemento sin afectar el flujo del documento:

```css
/* Rotar */
.icono:hover {
  transform: rotate(45deg);
}

/* Escalar (agrandar o encoger) */
.tarjeta:hover {
  transform: scale(1.05);
}

/* Mover */
.boton:active {
  transform: translateY(2px); /* Efecto de presionar */
}

/* Inclinar */
.caja {
  transform: skew(10deg, 5deg);
}

/* Múltiples transformaciones */
.elemento:hover {
  transform: rotate(5deg) scale(1.1) translateX(10px);
}
```

## Animation y @keyframes

—Para movimientos más complejos o que se repiten automáticamente, usas **animaciones**:

```css
/* 1. Definir la animación con @keyframes */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 2. Aplicarla a un elemento */
.articulo {
  animation: fadeIn 0.8s ease-out;
}
```

### Keyframes con porcentajes

—Puedes definir múltiples puntos intermedios:

```css
@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.8;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.boton-suscribirse {
  animation: pulse 2s ease-in-out infinite;
}
```

### Propiedades de animación

```css
.elemento {
  animation-name: fadeIn;          /* Nombre del @keyframes */
  animation-duration: 0.8s;        /* Duración */
  animation-timing-function: ease-out; /* Curva de aceleración */
  animation-delay: 0.2s;           /* Retardo antes de empezar */
  animation-iteration-count: 1;    /* Número de repeticiones: 1, 2, infinite */
  animation-direction: normal;     /* normal, reverse, alternate */
  animation-fill-mode: forwards;   /* Mantiene el estado final */
  animation-play-state: running;   /* running, paused */

  /* Shorthand */
  animation: fadeIn 0.8s ease-out 0.2s 1 normal forwards;
}
```

### Animaciones que se activan con scroll

—Aunque eso normalmente requiere JavaScript, puedes hacer animaciones simples que se activen con hover:

```css
@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.tarjeta {
  animation: slideInLeft 0.5s ease-out;
  animation-fill-mode: both;
}

.tarjeta:nth-child(2) {
  animation-delay: 0.2s;
}

.tarjeta:nth-child(3) {
  animation-delay: 0.4s;
}
```

## Dale vida a "Cultura Viva"

Mateo agregó movimiento a todo el sitio:

```css
/* === Animaciones globales === */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

/* === Animaciones en elementos específicos === */
.hero-titulo {
  animation: fadeInUp 1s ease-out;
}

.hero-subtitulo {
  animation: fadeInUp 1s ease-out 0.3s both;
}

.hero-boton {
  animation: fadeInUp 1s ease-out 0.6s both;
}

/* === Transiciones en elementos interactivos === */
.boton {
  transition: all 0.3s ease;
  cursor: pointer;
}

.boton:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.boton:active {
  transform: translateY(-1px);
}

/* === Tarjetas con efecto hover === */
.tarjeta-evento {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tarjeta-evento:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
}

/* === Galería: hover con zoom === */
.galeria-item {
  overflow: hidden;
  border-radius: 8px;
}

.galeria-item img {
  transition: transform 0.4s ease;
}

.galeria-item:hover img {
  transform: scale(1.1);
}

/* === Botón de suscripción con pulso === */
.boton-suscripcion {
  background-color: #8B0000;
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 30px;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: pulse 2s ease-in-out infinite;
}

.boton-suscripcion:hover {
  animation: none; /* Detiene el pulso al hacer hover */
  background-color: #a52a2a;
  transform: scale(1.05);
}

/* === Barra de progreso al hacer scroll === */
/* (Esto se vería con JavaScript, pero el CSS está listo) */
.barra-progreso {
  height: 3px;
  background: linear-gradient(90deg, #8B0000, #cc3333);
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  transition: width 0.1s linear;
}
```

Mateo recargó el sitio. Los títulos aparecían con una animación suave. Los botones reaccionaban al mouse con elegancia. Las imágenes de la galería se agrandaban suavemente al pasar el cursor. Los artículos se deslizaban hacia arriba al cargar la página.

—Ahora el sitio respira —dijo Mateo.

—Exacto —respondió Carolina—. El movimiento hace que el sitio se sienta vivo. No es decoración: es **comunicación**. Un botón que se eleva dice "puedes hacerme clic". Una tarjeta que se agranda dice "soy importante". Las animaciones guían al usuario sin palabras.

---

## Enigmas del Capítulo 8

**Enigma 8.1:** Crea una animación llamada `bounce` que haga que un elemento rebote (suba y baje) indefinidamente. Pista: usa `translateY`.

**Enigma 8.2:** Diseña un botón con las siguientes transiciones:
- Color de fondo cambia suavemente (0.3s)
- Escala aumenta ligeramente (0.2s)
- Aparece una sombra (0.3s)
Todo debe ocurrir al hacer hover.

**Enigma 8.3:** Crea una animación de **carga** (loading spinner) usando solo CSS. Un círculo que gira 360 grados infinitamente.

**Enigma 8.4:** ¿Cuál es la diferencia entre `transition` y `animation`? ¿Cuándo usarías cada uno?

**Enigma 8.5:** Explica qué hace `animation-fill-mode: forwards` y por qué es útil.
