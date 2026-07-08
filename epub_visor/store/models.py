from django.db import models
from django.urls import reverse

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(
        max_length=120,
        blank=True,
        help_text='Categoría del libro para filtrar en la tienda',
    )
    portada_url = models.CharField(max_length=255, blank=True)
    pdf_url = models.CharField(
        max_length=255,
        blank=True,
        help_text='URL pública del PDF para vista previa del libro',
    )
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
