import os, zipfile, json
from xml.etree import ElementTree as ET
from pathlib import Path
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from decimal import Decimal


def epub_cover_path(instance, filename):
    return f'covers/{instance.slug}/{filename}'


def epub_file_path(instance, filename):
    return f'epubs/{instance.slug}/{filename}'


class Book(models.Model):
    STATUS_CHOICES = [
        ('borrador', 'Borrador'),
        ('en_progreso', 'En Progreso'),
        ('completo', 'Completo'),
        ('publicado', 'Publicado'),
    ]

    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    author = models.CharField(max_length=300, blank=True, default='')
    description = models.TextField(blank=True, default='')
    language = models.CharField(max_length=10, blank=True, default='es')
    isbn = models.CharField(max_length=30, blank=True, default='')
    publisher = models.CharField(max_length=300, blank=True, default='')
    publication_date = models.CharField(max_length=50, blank=True, default='')
    rights = models.TextField(blank=True, default='')

    epub_file = models.FileField(upload_to=epub_file_path, null=True, blank=True)
    cover_image = models.ImageField(upload_to=epub_cover_path, null=True, blank=True)
    pdf_file = models.FileField(upload_to=epub_file_path, null=True, blank=True,
                                help_text='Archivo PDF del libro')

    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'),
                                help_text='Precio de venta en EUR')
    is_featured = models.BooleanField(default=False, help_text='Destacar en tienda')
    file_size = models.IntegerField(default=0, help_text='Tamaño en bytes')
    word_count = models.IntegerField(default=0, help_text='Número estimado de palabras')
    page_count = models.IntegerField(default=0, help_text='Número estimado de páginas')
    chapter_count = models.IntegerField(default=0)
    character_count = models.IntegerField(default=0)
    reading_time_minutes = models.IntegerField(default=0)

    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='uploaded_books')
    is_public = models.BooleanField(default=False, help_text='Visible para todos los usuarios')
    is_opencode_project = models.BooleanField(default=False, help_text='Creado con opencode')
    opencode_path = models.CharField(max_length=1000, blank=True, default='',
                                      help_text='Ruta al proyecto opencode')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completo')
    progress_percentage = models.IntegerField(default=100,
                                              help_text='Solo aplica si es proyecto opencode')
    diagnostics = models.TextField(blank=True, default='', help_text='JSON con diagnóstico')

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            import re
            base = re.sub(r'[^\w\s-]', '', self.title).strip().lower()
            base = re.sub(r'[-\s]+', '-', base)
            self.slug = base
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])

    def file_size_display(self):
        if self.file_size < 1024:
            return f'{self.file_size} B'
        elif self.file_size < 1024 ** 2:
            return f'{self.file_size / 1024:.1f} KB'
        else:
            return f'{self.file_size / 1024 ** 2:.1f} MB'

    def reading_time_display(self):
        h, m = divmod(self.reading_time_minutes, 60)
        if h:
            return f'{h}h {m}m'
        return f'{m} min'

    def extract_metadata(self):
        if not self.epub_file:
            return
        path = self.epub_file.path
        try:
            with zipfile.ZipFile(path, 'r') as z:
                if 'META-INF/container.xml' in z.namelist():
                    container = ET.fromstring(z.read('META-INF/container.xml'))
                    ns = {'c': 'urn:oasis:names:tc:opendocument:xmlns:container'}
                    rootfile = container.find('.//c:rootfile', ns)
                    if rootfile is not None:
                        opf_path = rootfile.get('full-path')
                        opf_data = z.read(opf_path)
                        self._parse_opf(opf_data, z, opf_path)
        except Exception as e:
            print(f'Error parsing EPUB {self.title}: {e}')

    def _parse_opf(self, opf_data, z, opf_path):
        root = ET.fromstring(opf_data)
        ns = {
            'opf': 'http://www.idpf.org/2007/opf',
            'dc': 'http://purl.org/dc/elements/1.1/',
        }

        metadata = root.find('opf:metadata', ns) or root.find('metadata')
        if metadata is not None:
            for child in metadata:
                tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                text = (child.text or '').strip()
                if tag == 'title' and not self.title:
                    self.title = text
                elif tag == 'creator' and not self.author:
                    self.author = text
                elif tag == 'language' and not self.language:
                    self.language = text
                elif tag == 'identifier' and not self.isbn:
                    if not self.isbn and text:
                        self.isbn = text
                elif tag == 'publisher' and not self.publisher:
                    self.publisher = text
                elif tag == 'date' and not self.publication_date:
                    self.publication_date = text
                elif tag == 'description' and not self.description:
                    self.description = text
                elif tag == 'rights' and not self.rights:
                    self.rights = text

        manifest = root.find('opf:manifest', ns) or root.find('manifest')
        spine = root.find('opf:spine', ns) or root.find('spine')
        if spine is not None:
            refs = spine.findall('opf:itemref', ns) or spine.findall('itemref')
            self.chapter_count = len(refs)

        cover_id = None
        if manifest is not None:
            for item in manifest:
                it_id = item.get('id', '')
                it_prop = item.get('properties', '')
                if 'cover-image' in it_prop or it_id == 'cover-image' or it_id == 'cover':
                    cover_id = it_id
                    break
            if not cover_id:
                for item in manifest:
                    href = (item.get('href', '') or '').lower()
                    if 'cover' in href and ('jpg' in href or 'png' in href or 'jpeg' in href):
                        cover_id = item.get('id')
                        break

        if cover_id and manifest is not None:
            for item in manifest:
                if item.get('id') == cover_id:
                    href = item.get('href', '')
                    base_dir = str(Path(opf_path).parent).replace('\\', '/')
                    if base_dir == '.':
                        cover_path = href
                    else:
                        cover_path = f'{base_dir}/{href}'
                    if cover_path in z.namelist():
                        img_data = z.read(cover_path)
                        img = Image.open(BytesIO(img_data))
                        img = img.convert('RGB')
                        cover_name = f'cover_{self.slug}.jpg'
                        from django.core.files.base import ContentFile
                        thumb = BytesIO()
                        img.thumbnail((600, 1000), Image.LANCZOS)
                        img.save(thumb, 'JPEG', quality=85)
                        self.cover_image.save(cover_name, ContentFile(thumb.getvalue()), save=False)

        total_text = ''
        if spine is not None and manifest is not None:
            items_map = {}
            for item in manifest:
                items_map[item.get('id')] = item.get('href', '')
            base_dir = str(Path(opf_path).parent).replace('\\', '/')
            for ref in spine:
                idref = ref.get('idref', '')
                if idref in items_map:
                    href = items_map[idref]
                    if base_dir == '.':
                        file_path = href
                    else:
                        file_path = f'{base_dir}/{href}'
                    if file_path in z.namelist():
                        try:
                            content = z.read(file_path)
                            text = content.decode('utf-8', errors='ignore')
                            import re as re_mod
                            clean = re_mod.sub(r'<[^>]+>', ' ', text)
                            clean = re_mod.sub(r'\s+', ' ', clean)
                            total_text += clean + ' '
                        except:
                            pass

        words = total_text.split()
        self.word_count = len(words)
        self.character_count = len(total_text)
        self.page_count = max(1, self.word_count // 300)
        self.reading_time_minutes = max(1, self.word_count // 250)
        self.file_size = os.path.getsize(path) if os.path.exists(path) else 0

    def get_diagnostics(self):
        if self.diagnostics:
            try:
                return json.loads(self.diagnostics)
            except:
                pass
        return {}

    def set_diagnostics(self, data):
        self.diagnostics = json.dumps(data, ensure_ascii=False)


class ReadingProgress(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='progress')
    current_chapter = models.IntegerField(default=0)
    current_percent = models.FloatField(default=0.0)
    last_position = models.TextField(blank=True, default='', help_text='CFI o identificador de posición')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Progreso de lectura'
        verbose_name_plural = 'Progresos de lectura'
