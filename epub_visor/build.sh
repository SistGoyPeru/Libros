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
# Escanear proyectos de libros
python manage.py shell -c "
import os
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epub_visor.settings')
import django; django.setup()
from visor.models import Book
from visor.views import _scan_opencode_projects, _check_opencode_diagnostics
projects = _scan_opencode_projects()
new_count = 0
for proj in projects:
    slug = proj['slug']
    if not Book.objects.filter(slug=slug).exists():
        book = Book(
            title=proj['title'], slug=slug,
            author='Alex Goyzueta Delgado',
            is_opencode_project=True,
            opencode_path=proj['path'],
            status='en_progreso',
        )
        book.save()
        _check_opencode_diagnostics(book)
        book.is_public = True
        book.save()
        new_count += 1
# Actualizar portadas de libros existentes
for book in Book.objects.filter(is_opencode_project=True):
    _check_opencode_diagnostics(book)
    book.is_public = True
    book.save()
print(f'Libros: {len(projects)}, nuevos: {new_count}')
"
