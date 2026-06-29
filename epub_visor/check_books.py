import os, django
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epub_visor.settings')
django.setup()

from visor.models import Book
for b in Book.objects.all():
    d = b.get_diagnostics()
    print(f'{b.title}: status={b.status} progress={b.progress_percentage}% pages={b.page_count} words={b.word_count}')
    print(f'  missing: {d.get("missing_items", [])}')
    print()
