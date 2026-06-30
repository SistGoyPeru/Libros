#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py shell -c "
import os
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
from django.contrib.auth.models import User
if not User.objects.filter(username='alex').exists():
    User.objects.create_superuser('alex', '', 'admin123')
    print('Superuser alex creado')
"
# Escanear proyectos y regenerar portadas (Render borra media/ en cada deploy)
python manage.py shell -c "
import os, shutil
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epub_visor.settings')
import django; django.setup()
from visor.models import Book
from visor.views import _scan_opencode_projects, _check_opencode_diagnostics
from django.conf import settings

# Limpiar media para regenerar desde cero
media = settings.MEDIA_ROOT
if os.path.isdir(media):
    shutil.rmtree(media)
os.makedirs(media, exist_ok=True)

projects = _scan_opencode_projects()
new_count = 0
for proj in projects:
    slug = proj['slug']
    book, created = Book.objects.get_or_create(
        slug=slug,
        defaults=dict(
            title=proj['title'], author='Alex Goyzueta Delgado',
            is_opencode_project=True, opencode_path=proj['path'],
            status='en_progreso',
        ),
    )
    # Forzar recopia de portada, pdf y epub
    book.epub_file = None
    book.pdf_file = None
    book.cover_image = None
    _check_opencode_diagnostics(book)
    book.is_public = True
    book.save()
    if created:
        new_count += 1
print(f'Libros: {len(projects)}, nuevos: {new_count}')
"
