import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epub_visor.settings')

import django
django.setup()

from visor.models import Book
from visor.views import _check_opencode_diagnostics

for b in Book.objects.filter(is_opencode_project=True):
    print(f'Processing: {b.title}...')
    _check_opencode_diagnostics(b)
    b.save()
    if b.cover_image:
        print(f'  Cover: {b.cover_image.url}')
    else:
        print(f'  No cover found')
