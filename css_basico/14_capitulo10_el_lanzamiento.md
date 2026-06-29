# Capítulo 10: El Lanzamiento

*Tema: Proyecto final — Maquetar la portada completa*

---

Era viernes, el último día antes del lanzamiento del sitio web de "Cultura Viva". Mateo llegó a PixelLab a las 7:30 de la mañana, dos horas antes de lo habitual. El café de la oficina aún no estaba listo, así que se preparó un té y se sentó frente a su estación de trabajo.

En la pantalla tenía el diseño final que Carolina le había pasado: la **portada completa** de la revista digital. Era un layout complejo con múltiples secciones: hero, artículos destacados, galería, eventos, suscripción, y footer. Todo debía funcionar en cualquier dispositivo.

—Hoy no hay lecciones —dijo Carolina, apareciendo detrás de él con su café—. Hoy pones a prueba todo lo que aprendiste.

Mateo asintió. Abrió el archivo `index.html` de la portada y, al lado, su archivo `estilo.css`. Había llegado el momento.

## El proyecto final

El HTML de la portada tenía esta estructura:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cultura Viva — Arte y Pensamiento</title>
  <link rel="stylesheet" href="estilo.css">
</head>
<body>

  <header class="header-principal">
    <a href="#" class="logo">Cultura Viva</a>
    <nav>
      <a href="#">Inicio</a>
      <a href="#">Arte</a>
      <a href="#">Literatura</a>
      <a href="#">Música</a>
      <a href="#">Eventos</a>
    </nav>
    <a href="#" class="btn-suscripcion">Suscribirse</a>
  </header>

  <main>
    <!-- Hero principal -->
    <section class="hero">
      <div class="hero-contenido">
        <span class="hero-etiqueta">Edición Julio 2026</span>
        <h1 class="hero-titulo">El Renacimiento Digital del Arte Latinoamericano</h1>
        <p class="hero-subtitulo">Exploramos cómo los artistas contemporáneos están transformando la identidad cultural a través de la tecnología.</p>
        <a href="#" class="btn-primario">Leer artículo</a>
      </div>
      <div class="hero-imagen">
        <img src="hero.jpg" alt="Arte digital latinoamericano">
      </div>
    </section>

    <!-- Artículos destacados -->
    <section class="articulos-destacados">
      <h2 class="seccion-titulo">Artículos Destacados</h2>
      <div class="grid-articulos">
        <article class="tarjeta-articulo">
          <img src="art1.jpg" alt="Artículo 1">
          <div class="tarjeta-contenido">
            <span class="tarjeta-categoria">Literatura</span>
            <h3>La Narrativa del Siglo XXI</h3>
            <p>Autores que están redefiniendo la literatura latinoamericana desde las plataformas digitales.</p>
            <a href="#" class="enlace-articulo">Leer más →</a>
          </div>
        </article>
        <article class="tarjeta-articulo">
          <img src="art2.jpg" alt="Artículo 2">
          <div class="tarjeta-contenido">
            <span class="tarjeta-categoria">Música</span>
            <h3>Sonidos de Transformación</h3>
            <p>La fusión de ritmos tradicionales con producción digital está creando un nuevo paisaje sonoro.</p>
            <a href="#" class="enlace-articulo">Leer más →</a>
          </div>
        </article>
        <article class="tarjeta-articulo">
          <img src="art3.jpg" alt="Artículo 3">
          <div class="tarjeta-contenido">
            <span class="tarjeta-categoria">Arte</span>
            <h3>Galerías sin Paredes</h3>
            <p>El auge de las exposiciones virtuales y su impacto en la democratización del arte.</p>
            <a href="#" class="enlace-articulo">Leer más →</a>
          </div>
        </article>
      </div>
    </section>

    <!-- Galería de arte -->
    <section class="galeria-seccion">
      <h2 class="seccion-titulo">Galería Destacada</h2>
      <div class="galeria">
        <div class="galeria-item"><img src="gale1.jpg" alt="Obra 1"></div>
        <div class="galeria-item"><img src="gale2.jpg" alt="Obra 2"></div>
        <div class="galeria-item"><img src="gale3.jpg" alt="Obra 3"></div>
        <div class="galeria-item"><img src="gale4.jpg" alt="Obra 4"></div>
        <div class="galeria-item"><img src="gale5.jpg" alt="Obra 5"></div>
        <div class="galeria-item"><img src="gale6.jpg" alt="Obra 6"></div>
      </div>
    </section>

    <!-- Eventos -->
    <section class="eventos-seccion">
      <h2 class="seccion-titulo">Próximos Eventos</h2>
      <div class="lista-eventos">
        <div class="tarjeta-evento">
          <div class="evento-fecha">
            <span class="evento-dia">28</span>
            <span class="evento-mes">JUL</span>
          </div>
          <div class="evento-info">
            <h3>Exposición: Colores del Ande</h3>
            <p>Galería de Arte Contemporáneo, Miraflores</p>
          </div>
        </div>
        <div class="tarjeta-evento">
          <div class="evento-fecha">
            <span class="evento-dia">05</span>
            <span class="evento-mes">AGO</span>
          </div>
          <div class="evento-info">
            <h3>Conferencia: Literatura Digital</h3>
            <p>Centro Cultural PUCP, San Miguel</p>
          </div>
        </div>
        <div class="tarjeta-evento">
          <div class="evento-fecha">
            <span class="evento-dia">19</span>
            <span class="evento-mes">AGO</span>
          </div>
          <div class="evento-info">
            <h3>Concierto: Fusión Andina</h3>
            <p>Teatro Municipal, Lima Centro</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Suscripción -->
    <section class="suscripcion-seccion">
      <div class="suscripcion-contenido">
        <h2>No te pierdas ninguna edición</h2>
        <p>Suscríbete a Cultura Viva y recibe cada mes lo mejor del arte y el pensamiento contemporáneo.</p>
        <form class="suscripcion-form">
          <input type="email" class="campo-formulario" placeholder="Tu correo electrónico">
          <button type="submit" class="btn-suscripcion">Suscribirse</button>
        </form>
      </div>
    </section>
  </main>

  <footer class="footer-principal">
    <div class="footer-grid">
      <div>
        <h4>Cultura Viva</h4>
        <p>Arte y pensamiento desde 1998</p>
      </div>
      <div>
        <h4>Secciones</h4>
        <a href="#">Arte</a>
        <a href="#">Literatura</a>
        <a href="#">Música</a>
        <a href="#">Eventos</a>
      </div>
      <div>
        <h4>Síguenos</h4>
        <a href="#">Facebook</a>
        <a href="#">Instagram</a>
        <a href="#">Twitter</a>
      </div>
      <div>
        <h4>Contacto</h4>
        <a href="#">contacto@culturaviva.pe</a>
        <a href="#">+51 1 555 0123</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Cultura Viva. Todos los derechos reservados.</p>
    </div>
  </footer>

</body>
</html>
```

Mateo respiró hondo y comenzó a escribir el CSS completo:

```css
/* === CSS COMPLETO — CULTURA VIVA PORTADA === */

/* === RESET === */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* === TIPOGRAFÍA === */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Lato:wght@300;400;700&display=swap');

:root {
  --color-primario: #8B0000;
  --color-secundario: #1a1a2e;
  --color-fondo: #f5f0eb;
  --color-texto: #2d2d2d;
  --color-claro: #e8e0d5;
  --fuente-titulos: "Playfair Display", Georgia, serif;
  --fuente-cuerpo: "Lato", Arial, sans-serif;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: var(--fuente-cuerpo);
  color: var(--color-texto);
  background-color: var(--color-fondo);
  line-height: 1.7;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
}

/* === HEADER === */
.header-principal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 70px;
  background-color: var(--color-secundario);
  color: white;
  display: flex;
  align-items: center;
  padding: 0 30px;
  z-index: 1000;
}

.logo {
  font-family: var(--fuente-titulos);
  font-size: 24px;
  font-weight: 700;
  color: white;
}

.header-principal nav {
  display: flex;
  gap: 25px;
  margin-left: 50px;
}

.header-principal nav a {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: rgba(255, 255, 255, 0.7);
  transition: color 0.3s ease;
}

.header-principal nav a:hover {
  color: white;
}

.btn-suscripcion {
  margin-left: auto;
  background-color: var(--color-primario);
  color: white;
  padding: 10px 22px;
  border-radius: 25px;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn-suscripcion:hover {
  background-color: #a52a2a;
  transform: translateY(-2px);
}

/* === HERO === */
.hero {
  margin-top: 70px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 500px;
  background-color: var(--color-secundario);
  color: white;
  overflow: hidden;
}

.hero-contenido {
  padding: 60px 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  animation: fadeInUp 1s ease-out;
}

.hero-etiqueta {
  display: inline-block;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--color-primario);
  font-weight: 700;
  margin-bottom: 20px;
}

.hero-titulo {
  font-family: var(--fuente-titulos);
  font-size: 42px;
  font-weight: 900;
  line-height: 1.2;
  margin-bottom: 20px;
}

.hero-subtitulo {
  font-size: 18px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 30px;
}

.btn-primario {
  display: inline-block;
  background-color: var(--color-primario);
  color: white;
  padding: 14px 32px;
  border-radius: 6px;
  font-weight: 700;
  transition: all 0.3s ease;
  align-self: flex-start;
}

.btn-primario:hover {
  background-color: #a52a2a;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(139, 0, 0, 0.4);
}

.hero-imagen {
  overflow: hidden;
}

.hero-imagen img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.hero:hover .hero-imagen img {
  transform: scale(1.05);
}

/* === SECCIONES === */
.seccion-titulo {
  font-family: var(--fuente-titulos);
  font-size: 32px;
  color: var(--color-secundario);
  text-align: center;
  margin-bottom: 40px;
  position: relative;
}

.seccion-titulo::after {
  content: "";
  display: block;
  width: 60px;
  height: 3px;
  background-color: var(--color-primario);
  margin: 15px auto 0;
}

section {
  padding: 60px 30px;
  max-width: 1200px;
  margin: 0 auto;
}

/* === ARTÍCULOS DESTACADOS === */
.grid-articulos {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 25px;
}

.tarjeta-articulo {
  background: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tarjeta-articulo:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
}

.tarjeta-articulo img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.tarjeta-contenido {
  padding: 25px;
}

.tarjeta-categoria {
  display: inline-block;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--color-primario);
  font-weight: 700;
  margin-bottom: 10px;
}

.tarjeta-contenido h3 {
  font-family: var(--fuente-titulos);
  font-size: 22px;
  margin-bottom: 12px;
  color: var(--color-secundario);
}

.tarjeta-contenido p {
  font-size: 14px;
  line-height: 1.6;
  color: #666;
  margin-bottom: 15px;
}

.enlace-articulo {
  color: var(--color-primario);
  font-weight: 700;
  font-size: 14px;
  position: relative;
}

.enlace-articulo::after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--color-primario);
  transition: width 0.3s ease;
}

.enlace-articulo:hover::after {
  width: 100%;
}

/* === GALERÍA === */
.galeria {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}

.galeria-item {
  overflow: hidden;
  border-radius: 8px;
}

.galeria-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.galeria-item:hover img {
  transform: scale(1.1);
}

/* === EVENTOS === */
.lista-eventos {
  display: grid;
  gap: 15px;
}

.tarjeta-evento {
  display: flex;
  align-items: center;
  gap: 25px;
  background: white;
  padding: 20px 25px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: transform 0.3s ease;
}

.tarjeta-evento:hover {
  transform: translateX(8px);
}

.evento-fecha {
  text-align: center;
  background-color: var(--color-primario);
  color: white;
  padding: 12px 18px;
  border-radius: 8px;
  min-width: 70px;
}

.evento-dia {
  display: block;
  font-size: 28px;
  font-weight: 900;
  font-family: var(--fuente-titulos);
  line-height: 1;
}

.evento-mes {
  display: block;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 5px;
}

.evento-info h3 {
  font-family: var(--fuente-titulos);
  font-size: 18px;
  margin-bottom: 5px;
}

.evento-info p {
  font-size: 14px;
  color: #888;
}

/* === SUSCRIPCIÓN === */
.suscripcion-seccion {
  background: linear-gradient(135deg, var(--color-secundario), #16213e);
  color: white;
  border-radius: 15px;
  text-align: center;
  margin: 60px auto;
}

.suscripcion-contenido h2 {
  font-family: var(--fuente-titulos);
  font-size: 32px;
  margin-bottom: 15px;
}

.suscripcion-contenido p {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 30px;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.suscripcion-form {
  display: flex;
  gap: 10px;
  max-width: 500px;
  margin: 0 auto;
}

.campo-formulario {
  flex: 1;
  padding: 14px 20px;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  transition: box-shadow 0.3s ease;
}

.campo-formulario:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(139, 0, 0, 0.3);
}

.btn-suscripcion {
  background-color: var(--color-primario);
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 6px;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-suscripcion:hover {
  background-color: #a52a2a;
}

/* === FOOTER === */
.footer-principal {
  background-color: var(--color-secundario);
  color: white;
  padding: 60px 30px 0;
  margin-top: 60px;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.footer-grid h4 {
  font-family: var(--fuente-titulos);
  margin-bottom: 20px;
  color: var(--color-claro);
}

.footer-grid a {
  display: block;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 10px;
  transition: color 0.3s ease;
}

.footer-grid a:hover {
  color: white;
}

.footer-bottom {
  text-align: center;
  padding: 30px 0;
  margin-top: 40px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 13px;
  color: rgba(255, 255, 255, 0.4);
}

/* === ANIMACIONES === */
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

/* === RESPONSIVE === */
@media (max-width: 768px) {
  .header-principal nav {
    display: none;
  }

  .hero {
    grid-template-columns: 1fr;
  }

  .hero-contenido {
    padding: 40px 25px;
  }

  .hero-titulo {
    font-size: 28px;
  }

  .grid-articulos {
    grid-template-columns: 1fr;
  }

  .galeria {
    grid-template-columns: repeat(2, 1fr);
  }

  .footer-grid {
    grid-template-columns: 1fr 1fr;
  }

  section {
    padding: 40px 20px;
  }

  .suscripcion-form {
    flex-direction: column;
  }
}

@media (max-width: 480px) {
  .galeria {
    grid-template-columns: 1fr;
  }

  .footer-grid {
    grid-template-columns: 1fr;
  }

  .hero-titulo {
    font-size: 24px;
  }

  .seccion-titulo {
    font-size: 24px;
  }
}
```

Mateo guardó el archivo, abrió el navegador y recargó la página.

La portada apareció completa. El hero con dos columnas mostraba el título majestuoso y la imagen vibrante. Los artículos se alineaban en una cuadrícula perfecta. La galería desplegaba las obras de arte con elegancia. Los eventos se deslizaban uno tras otro. El formulario de suscripción invitaba a participar. El footer cerraba el diseño con solidez.

Redimensionó la ventana. Todo se adaptaba. Probó en el teléfono. Funcionaba.

Mateo se reclinó en su silla. Dos meses atrás no sabía ni qué era un selector. Ahora tenía un sitio web completo, responsivo, animado, diseñado profesionalmente.

—¿Listo para el lanzamiento? —preguntó Carolina, asomándose por la puerta.

—Listo —respondió Mateo.

—Entonces vamos. El sitio de "Cultura Viva" se publica hoy.

Mateo sonrió. No solo había aprendido CSS. Había descubierto que el diseño no era decoración: era la forma en que la tecnología se comunicaba con los humanos. Y él, Mateo Vargas, era ahora un puente entre ambos mundos.

---

## Enigmas del Capítulo 10

**Enigma 10.1:** Modifica el CSS de la portada para que el header se vuelva translúcido (fondo semitransparente) cuando el usuario hace scroll. Pista: necesitarás una clase adicional (que se agregaría con JavaScript) para activar este efecto.

**Enigma 10.2:** Agrega una animación de entrada para las tarjetas de artículo. Cada tarjeta debe aparecer con un retraso progresivo (la primera inmediata, la segunda 0.2s después, la tercera 0.4s después).

**Enigma 10.3:** Crea una versión del hero donde la imagen de fondo use `background-image` en lugar de un `<img>`. Ajusta el CSS para que funcione igual.

**Enigma 10.4:** Agrega un efecto de "parallax" suave al fondo de la sección de suscripción usando `background-attachment: fixed`.

**Enigma 10.5:** Piensa en tres mejoras que le harías al diseño de la portada. Descríbelas y escribe el CSS necesario para implementarlas.
