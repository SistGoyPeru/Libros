from django.db import models
from django.urls import reverse


class AboutMe(models.Model):
    nombre = models.CharField(max_length=200, default='Alex Goyzueta Delgado')
    titulo = models.CharField(max_length=200, blank=True, help_text='Ej: Analista de datos freelance')
    hero_title = models.CharField(max_length=300, blank=True, help_text='Texto grande del hero (ej: "Transforma datos en poder")')
    hero_subtitle = models.CharField(max_length=500, blank=True, help_text='Texto descriptivo del hero')
    bio = models.TextField(blank=True)
    foto_url = models.CharField(max_length=500, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    ubicacion = models.CharField(max_length=200, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sobre mí'
        verbose_name_plural = 'Sobre mí'


class Project(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    imagen_url = models.CharField(max_length=500, blank=True)
    url = models.URLField(blank=True, help_text='Enlace al proyecto')
    tecnologias = models.CharField(max_length=500, blank=True, help_text='Separadas por coma')
    orden = models.IntegerField(default=0)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['orden']


class Course(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    imagen_url = models.CharField(max_length=500, blank=True)
    url = models.URLField(blank=True)
    plataforma = models.CharField(max_length=200, blank=True)
    orden = models.IntegerField(default=0)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['orden']


class Tool(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, blank=True, help_text='Ej: Python, Visualización, etc.')
    nivel = models.IntegerField(default=3, help_text='Nivel de 1 a 5')
    icono = models.CharField(max_length=200, blank=True, help_text='URL del icono o clase CSS')
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Herramienta / Skill'
        verbose_name_plural = 'Herramientas / Skills'
        ordering = ['orden']


class BlogArticle(models.Model):
    titulo = models.CharField(max_length=300)
    contenido = models.TextField(blank=True)
    resumen = models.TextField(blank=True, max_length=500)
    imagen_url = models.CharField(max_length=500, blank=True)
    url = models.URLField(blank=True)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Artículo / Blog'
        verbose_name_plural = 'Artículos / Blog'
        ordering = ['-fecha']


class Service(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=200, blank=True, help_text='Clase CSS o emoji')
    orden = models.IntegerField(default=0)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['orden']


class Testimonial(models.Model):
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200, blank=True, help_text='Ej: CEO de Empresa X')
    texto = models.TextField(help_text='El testimonio del cliente')
    foto_url = models.CharField(max_length=500, blank=True)
    orden = models.IntegerField(default=0)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
        ordering = ['orden']


class BlogComment(models.Model):
    articulo = models.ForeignKey(BlogArticle, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} en {self.articulo.titulo}'

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-fecha']


class SocialLink(models.Model):
    nombre = models.CharField(max_length=100, help_text='Ej: LinkedIn, GitHub')
    url = models.URLField()
    icono = models.CharField(max_length=200, blank=True, help_text='URL del icono o clase CSS')
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'
        ordering = ['orden']


class ContactInfo(models.Model):
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True)
    ubicacion = models.CharField(max_length=200, blank=True)
    mensaje_bienvenida = models.TextField(blank=True, help_text='Texto para la sección de contacto')

    def __str__(self):
        return 'Información de contacto'

    class Meta:
        verbose_name = 'Información de contacto'
        verbose_name_plural = 'Información de contacto'


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(
        max_length=120,
        blank=True,
        help_text='Categoría del libro para filtrar en la tienda',
    )
    portada_url = models.CharField(max_length=255, blank=True)
    portada_archivo = models.ImageField(upload_to='portadas/', blank=True, null=True)
    pdf_url = models.CharField(
        max_length=255,
        blank=True,
        help_text='URL pública del PDF para vista previa del libro',
    )
    pdf_archivo = models.FileField(upload_to='pdfs/', blank=True, null=True, help_text='Subir archivo PDF directamente')
    epub_archivo = models.FileField(upload_to='epubs/', blank=True, null=True, help_text='Subir archivo EPUB directamente')
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=1.00)
    payhip_url = models.URLField(blank=True)
    publicado = models.BooleanField(default=False)
    excerpt = models.TextField(
        blank=True,
        help_text='Parte importante del libro para destacar en el detalle',
    )
    folder_name = models.CharField(
        max_length=255,
        blank=True,
        help_text='Nombre de la carpeta en distribucion',
    )
    epub_filename = models.CharField(
        max_length=255,
        blank=True,
        help_text='Nombre del archivo EPUB original',
    )

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('libro_detalle', args=[str(self.pk)])

    def get_admin_url(self):
        return reverse('admin:store_libro_change', args=[self.pk])

    def payhip_click_count(self):
        return self.payhip_clicks.count()

    def view_count(self):
        return self.libro_views.count()


class PayhipClick(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='payhip_clicks')
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=45, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f'Click en {self.libro.titulo} @ {self.timestamp}'


class LibroView(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_views')
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=45, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f'Vista en {self.libro.titulo} @ {self.timestamp}'
