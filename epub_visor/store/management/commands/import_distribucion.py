from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand
from store.models import Libro


class Command(BaseCommand):
    help = 'Importar libros desde la carpeta distribucion al modelo Libro'

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            default=None,
            help='Ruta a la carpeta distribucion. Si no se especifica, usa BASE_DIR/distribucion.',
        )
        parser.add_argument(
            '--publish',
            action='store_true',
            help='Marcar publicado=True para los libros importados.',
        )

    def handle(self, *args, **options):
        base_dir = Path(settings.BASE_DIR)
        dist_path = Path(options['path']) if options['path'] else base_dir / 'distribucion'
        if not dist_path.exists() or not dist_path.is_dir():
            alternative_path = base_dir.parent / 'distribucion'
            if alternative_path.exists() and alternative_path.is_dir():
                dist_path = alternative_path

        if not dist_path.exists() or not dist_path.is_dir():
            self.stderr.write(self.style.ERROR(f'No se encontró la carpeta distribucion en: {dist_path}'))
            return

        created = 0
        updated = 0
        skipped = 0

        for category_path in sorted(dist_path.iterdir()):
            if not category_path.is_dir():
                continue

            if any(child.is_dir() for child in category_path.iterdir()):
                category_name = category_path.name
                book_folders = sorted(category_path.iterdir())
            else:
                category_name = ''
                book_folders = [category_path]

            for folder_path in book_folders:
                if not folder_path.is_dir():
                    continue

                folder_name = folder_path.name
                descripcion = self._leer_descripcion(folder_path)
                epub_filename = self._buscar_epub(folder_path)
                portada_source = self._buscar_cover(folder_path)
                titulo = self._formatear_titulo(folder_name, epub_filename)
                portada_url = self._build_cover_url(category_name, folder_name) if portada_source else ''

                if portada_source:
                    self._copy_cover(portada_source, category_name, folder_name)

                libro, created_flag = Libro.objects.get_or_create(
                    folder_name=folder_name,
                    defaults={
                        'titulo': titulo,
                        'descripcion': descripcion,
                        'categoria': category_name,
                        'portada_url': portada_url,
                        'precio': 1.00,
                        'payhip_url': '',
                        'publicado': bool(options['publish']),
                        'epub_filename': epub_filename,
                    },
                )

                changed = False
                if not created_flag:
                    if libro.titulo != titulo:
                        libro.titulo = titulo
                        changed = True
                    if descripcion and libro.descripcion != descripcion:
                        libro.descripcion = descripcion
                        changed = True
                    if epub_filename and libro.epub_filename != epub_filename:
                        libro.epub_filename = epub_filename
                        changed = True
                    if portada_url and libro.portada_url != portada_url:
                        libro.portada_url = portada_url
                        changed = True
                    if libro.categoria != category_name:
                        libro.categoria = category_name
                        changed = True
                    if options['publish'] and not libro.publicado:
                        libro.publicado = True
                        changed = True

                if created_flag:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f'Creado: {titulo}'))
                elif changed:
                    libro.save()
                    updated += 1
                    self.stdout.write(self.style.SUCCESS(f'Actualizado: {titulo}'))
                else:
                    skipped += 1
                    self.stdout.write(self.style.WARNING(f'Omitido: {titulo}'))

        self.stdout.write(
            self.style.SUCCESS(
                f'Importación completada. Creados: {created}, actualizados: {updated}, omitidos: {skipped}'
            )
        )

    def _leer_descripcion(self, folder_path: Path) -> str:
        descripcion_path = folder_path / 'descripcion.txt'
        if descripcion_path.exists():
            return descripcion_path.read_text(encoding='utf-8').strip()
        return ''

    def _buscar_epub(self, folder_path: Path) -> str:
        for candidate in folder_path.iterdir():
            if candidate.is_file() and candidate.suffix.lower() == '.epub':
                return candidate.name
        return ''

    def _buscar_cover(self, folder_path: Path) -> Path | None:
        cover_path = folder_path / 'cover.jpg'
        if cover_path.exists() and cover_path.is_file():
            return cover_path
        return None

    def _build_cover_url(self, category: str, folder_name: str) -> str:
        if category:
            return f'/static/covers/{category}/{folder_name}.jpg'
        return f'/static/covers/{folder_name}.jpg'

    def _copy_cover(self, cover_path: Path, category: str, folder_name: str) -> None:
        if category:
            static_dir = Path(settings.BASE_DIR) / 'static' / 'covers' / category
        else:
            static_dir = Path(settings.BASE_DIR) / 'static' / 'covers'
        static_dir.mkdir(parents=True, exist_ok=True)
        destination = static_dir / f'{folder_name}.jpg'
        destination.write_bytes(cover_path.read_bytes())

    def _formatear_titulo(self, folder_name: str, epub_filename: str) -> str:
        if epub_filename:
            title = Path(epub_filename).stem
        else:
            title = folder_name
        return title.replace('_', ' ')
