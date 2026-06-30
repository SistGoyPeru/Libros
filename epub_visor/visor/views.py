import os, json, zipfile
from xml.etree import ElementTree as ET
from pathlib import Path
from datetime import datetime
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.db.models import Q, Sum
from .models import Book, ReadingProgress


def is_admin(user):
    return user.is_authenticated and user.is_staff


# ============================================================
# AUTH
# ============================================================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('library')
        messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'visor/login.html')


def logout_view(request):
    logout(request)
    return redirect('library')


# ============================================================
# LIBRARY (vitrina pública)
# ============================================================
def library(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')

    books = Book.objects.filter(is_public=True)

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    if status_filter:
        books = books.filter(status=status_filter)

    stats = {
        'total': books.count(),
        'pages': books.aggregate(s=Sum('page_count'))['s'] or 0,
        'words': books.aggregate(s=Sum('word_count'))['s'] or 0,
        'opencode': books.filter(is_opencode_project=True).count(),
    }

    return render(request, 'visor/library.html', {
        'books': books,
        'query': query,
        'status_filter': status_filter,
        'stats': stats,
    })


# ============================================================
# BOOK DETAIL
# ============================================================
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, is_public=True)
    chapters = _get_chapters(book)
    diagnostics = book.get_diagnostics() or None
    return render(request, 'visor/book_detail.html', {
        'book': book,
        'chapters': chapters,
        'diagnostics': diagnostics,
    })


# ============================================================
# EPUB READER (seguro, anti-copia)
# ============================================================
def reader(request, slug):
    book = get_object_or_404(Book, slug=slug, is_public=True)
    chapters = _get_chapters(book)

    chapter_idx = request.GET.get('chapter', 0)
    try:
        chapter_idx = int(chapter_idx)
    except:
        chapter_idx = 0

    total = len(chapters)
    if total == 0:
        return render(request, 'visor/reader.html', {
            'book': book,
            'chapters': [],
            'total': 0,
            'chapter_idx': 0,
            'content': '<div style="text-align:center;padding:3rem;color:var(--fg2);"><p>No hay capítulos disponibles</p></div>',
            'chapter_title': '',
        })

    if chapter_idx < 0:
        chapter_idx = 0
    if chapter_idx >= total:
        chapter_idx = total - 1

    chapter = chapters[chapter_idx]
    ch_ref = chapter.get('href', '')
    ch_title = chapter.get('title', f'Capítulo {chapter_idx + 1}')

    content = ''
    epub_path = book.epub_file.path if book.epub_file else None
    opencode_path = book.opencode_path if book.is_opencode_project else None

    if epub_path and os.path.exists(epub_path):
        try:
            with zipfile.ZipFile(epub_path, 'r') as z:
                if ch_ref in z.namelist():
                    raw = z.read(ch_ref)
                    content = raw.decode('utf-8', errors='ignore')
                    content = _clean_html_for_display(content)
        except:
            pass
    elif opencode_path and os.path.isdir(opencode_path):
        content = _get_chapter_from_markdown(opencode_path, chapter_idx, total)

    if not content:
        content = '<div style="text-align:center;padding:3rem;color:var(--fg2);"><p>Contenido no disponible</p></div>'

    book.last_read_at = timezone.now()
    book.save(update_fields=['last_read_at'])

    return render(request, 'visor/reader.html', {
        'book': book,
        'chapters': chapters,
        'total': total,
        'chapter_idx': chapter_idx,
        'content': content,
        'chapter_title': ch_title,
    })


# ============================================================
# PDF READER (seguro, anti-copia con PDF.js)
# ============================================================
def pdf_reader(request, slug):
    book = get_object_or_404(Book, slug=slug, is_public=True)
    if not book.pdf_file:
        messages.error(request, 'Este libro no tiene PDF disponible')
        return redirect('book_detail', slug=slug)
    return render(request, 'visor/pdf_reader.html', {
        'book': book,
    })


# ============================================================
# SERVE PDF (protegido, no permite descarga directa)
# ============================================================
def serve_pdf(request, slug):
    book = get_object_or_404(Book, slug=slug, is_public=True)
    if not book.pdf_file:
        return HttpResponse(status=404)
    response = FileResponse(book.pdf_file.open('rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline'
    response['X-Content-Type-Options'] = 'nosniff'
    return response


# ============================================================
# EPUB DOWNLOAD (admin only)
# ============================================================
@user_passes_test(is_admin)
def download_epub(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if book.epub_file and os.path.exists(book.epub_file.path):
        return FileResponse(book.epub_file.open('rb'), as_attachment=True, filename=f'{book.slug}.epub')
    messages.error(request, 'Archivo no disponible')
    return redirect('book_detail', slug=slug)


# ============================================================
# PDF DOWNLOAD (admin only)
# ============================================================
@user_passes_test(is_admin)
def download_pdf(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if book.pdf_file and os.path.exists(book.pdf_file.path):
        return FileResponse(book.pdf_file.open('rb'), as_attachment=True, filename=f'{book.slug}.pdf')
    # Fallback: buscar PDF en opencode_path
    if book.is_opencode_project and book.opencode_path:
        for fname in os.listdir(book.opencode_path):
            if fname.lower().endswith('.pdf'):
                fpath = os.path.join(book.opencode_path, fname)
                return FileResponse(open(fpath, 'rb'), as_attachment=True, filename=fname)
    messages.error(request, 'Archivo no disponible')
    return redirect('book_detail', slug=slug)


# ============================================================
# UPLOAD BOOK (admin only)
# ============================================================
@user_passes_test(is_admin)
def upload_book(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        epub = request.FILES.get('epub_file')

        if epub:
            book = Book(
                title=title or epub.name.replace('.epub', '').replace('_', ' ').title(),
                author=author or 'Desconocido',
                uploaded_by=request.user,
                is_public=True,
            )
            book.epub_file.save(epub.name, epub, save=False)
            book.save()
            book.extract_metadata()
            book.save()
            messages.success(request, f'Libro "{book.title}" subido correctamente')
            return redirect('book_detail', slug=book.slug)
        else:
            messages.error(request, 'Selecciona un archivo EPUB')

    projects = _scan_opencode_projects()
    return render(request, 'visor/upload.html', {'projects': projects})


# ============================================================
# SCAN OPENCODE (admin only)
# ============================================================
@user_passes_test(is_admin)
def scan_opencode(request):
    projects = _scan_opencode_projects()
    count = 0
    for proj in projects:
        slug = proj['slug']
        if not Book.objects.filter(slug=slug).exists():
            book = Book(
                title=proj['title'],
                slug=slug,
                author='Alex Goyzueta Delgado',
                is_opencode_project=True,
                opencode_path=proj['path'],
                status='en_progreso',
            )
            book.save()
            _check_opencode_diagnostics(book)
            count += 1
    return redirect('library')


# ============================================================
# RUN DIAGNOSTICS (admin only)
# ============================================================
@user_passes_test(is_admin)
def run_diagnostics(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if book.is_opencode_project and book.opencode_path:
        _check_opencode_diagnostics(book)
        book.save()
    return redirect('book_detail', slug=slug)


# ============================================================
# DELETE BOOK (admin only)
# ============================================================
@require_POST
@user_passes_test(is_admin)
def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if book.epub_file and os.path.exists(book.epub_file.path):
        os.remove(book.epub_file.path)
    if book.cover_image and os.path.exists(book.cover_image.path):
        os.remove(book.cover_image.path)
    book.delete()
    return redirect('library')


# ============================================================
# HELPERS: Chapters
# ============================================================
def _get_chapters(book):
    epub_path = book.epub_file.path if book.epub_file else None
    opencode_path = book.opencode_path if book.is_opencode_project else None

    if epub_path and os.path.exists(epub_path):
        return _get_chapters_from_epub(book)
    elif opencode_path and os.path.isdir(opencode_path):
        return _get_chapters_from_markdown_list(opencode_path)
    return []


def _get_chapters_from_epub(book):
    chapters = []
    path = book.epub_file.path
    try:
        with zipfile.ZipFile(path, 'r') as z:
            if 'META-INF/container.xml' in z.namelist():
                container = ET.fromstring(z.read('META-INF/container.xml'))
                ns = {'c': 'urn:oasis:names:tc:opendocument:xmlns:container'}
                rootfile = container.find('.//c:rootfile', ns)
                if rootfile is not None:
                    opf_path = rootfile.get('full-path')
                    opf_data = z.read(opf_path)
                    root = ET.fromstring(opf_data)
                    opf_ns = {
                        'opf': 'http://www.idpf.org/2007/opf',
                        'dc': 'http://purl.org/dc/elements/1.1/',
                    }
                    manifest = root.find('opf:manifest', opf_ns) or root.find('manifest')
                    spine = root.find('opf:spine', opf_ns) or root.find('spine')

                    items_map = {}
                    if manifest is not None:
                        for item in manifest:
                            items_map[item.get('id')] = item.get('href', '')

                    base_dir = str(Path(opf_path).parent).replace('\\', '/')

                    if spine is not None:
                        refs = spine.findall('opf:itemref', opf_ns) or spine.findall('itemref')
                        for i, ref in enumerate(refs):
                            idref = ref.get('idref', '')
                            href = items_map.get(idref, '')
                            if base_dir != '.':
                                href = f'{base_dir}/{href}'
                            chapters.append({
                                'href': href,
                                'index': i,
                                'title': f'Capítulo {i + 1}',
                            })
    except:
        pass
    return chapters


def _get_chapters_from_markdown_list(path):
    chapters = []
    md_files = sorted([f for f in os.listdir(path) if f.endswith('.md') and not f.startswith('libro_completo')])
    for i, fname in enumerate(md_files):
        title = Path(fname).stem.replace('_', ' ').replace('-', ' ').title()
        chapters.append({
            'href': fname,
            'index': i,
            'title': title,
        })
    return chapters


def _get_chapter_from_markdown(path, idx, total):
    md_files = sorted([f for f in os.listdir(path) if f.endswith('.md') and not f.startswith('libro_completo')])
    if 0 <= idx < len(md_files):
        fpath = os.path.join(path, md_files[idx])
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                md = f.read()
            html = _md_to_simple_html(md)
            return html
        except:
            pass
    return ''


def _md_to_simple_html(md):
    lines = md.split('\n')
    html = []
    for line in lines:
        line = line.strip()
        if not line:
            html.append('<p><br></p>')
        elif line.startswith('### '):
            html.append(f'<h3>{_inline_md(line[4:])}</h3>')
        elif line.startswith('## '):
            html.append(f'<h2>{_inline_md(line[3:])}</h2>')
        elif line.startswith('# '):
            html.append(f'<h1>{_inline_md(line[2:])}</h1>')
        elif line.startswith('- ') or line.startswith('* '):
            html.append(f'<li>{_inline_md(line[2:])}</li>')
        elif line.startswith('> '):
            html.append(f'<blockquote>{_inline_md(line[2:])}</blockquote>')
        elif '![' in line and '](' in line:
            html.append(f'<p>{_inline_md(line)}</p>')
        else:
            html.append(f'<p>{_inline_md(line)}</p>')
    return '\n'.join(html)


def _inline_md(text):
    import re
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank">\1</a>', text)
    return text


def _clean_html_for_display(html):
    import re
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'\bon\w+\s*=\s*["\'][^"\']*["\']', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<link[^>]*>', '', html, flags=re.IGNORECASE)
    return html


# ============================================================
# HELPERS: OpenCode Scan
# ============================================================
def _scan_opencode_projects():
    base = os.environ.get('OPENCODE_BOOKS_DIR', str(Path(__file__).resolve().parent.parent.parent))
    projects = []
    for entry in os.listdir(base):
        full = os.path.join(base, entry)
        if os.path.isdir(full) and entry != 'epub_visor' and entry != 'venv_epub':
            md_files = [f for f in os.listdir(full) if f.endswith('.md')]
            if md_files:
                title = entry.replace('_', ' ').title().replace(' ', ' ')
                portada = os.path.join(full, '00_portada.md')
                if os.path.exists(portada):
                    with open(portada, 'r', encoding='utf-8', errors='ignore') as pf:
                        first = pf.readline().strip()
                        if first.startswith('# '):
                            title = first[2:]
                projects.append({
                    'name': entry,
                    'title': title,
                    'path': full,
                    'slug': entry.lower().replace('_', '-'),
                    'file_count': len(md_files),
                })
    return projects


def _check_opencode_diagnostics(book):
    path = book.opencode_path
    if not path or not os.path.isdir(path):
        return

    md_files = sorted([f for f in os.listdir(path) if f.endswith('.md')])
    has_epub = any(f.endswith('.epub') for f in os.listdir(path))
    has_pdf = any(f.endswith('.pdf') for f in os.listdir(path))
    has_cover = any(f.startswith('cover') and (f.endswith('.jpg') or f.endswith('.png'))
                    for f in os.listdir(path))

    if not book.pdf_file:
        for fname in os.listdir(path):
            if fname.lower().endswith('.pdf'):
                pdf_src = os.path.join(path, fname)
                try:
                    from django.core.files.base import ContentFile
                    book.pdf_file.save(
                        f'{book.slug}.pdf',
                        ContentFile(open(pdf_src, 'rb').read()),
                        save=False,
                    )
                except Exception as e:
                    print(f'Error copying PDF for {book.title}: {e}')
                break

    if not book.cover_image:
        for fname in os.listdir(path):
            if fname.startswith('cover') and (fname.endswith('.jpg') or fname.endswith('.png')):
                src = os.path.join(path, fname)
                try:
                    from PIL import Image
                    from io import BytesIO
                    from django.core.files.base import ContentFile
                    img = Image.open(src)
                    img = img.convert('RGB')
                    thumb = BytesIO()
                    img.thumbnail((600, 1000), Image.LANCZOS)
                    img.save(thumb, 'JPEG', quality=85)
                    book.cover_image.save(f'cover_{book.slug}.jpg', ContentFile(thumb.getvalue()), save=False)
                except Exception as e:
                    print(f'Error copying cover for {book.title}: {e}')
                break

    total_chapters = len([f for f in md_files if 'capitulo' in f.lower() or 'modulo' in f.lower()])
    if total_chapters == 0:
        total_chapters = len([f for f in md_files if f[0:2].isdigit()])

    total_words = 0
    total_chars = 0
    chapter_md_files = [f for f in md_files if not f.startswith('libro_completo')]
    for fname in chapter_md_files:
        fpath = os.path.join(path, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            total_words += len(content.split())
            total_chars += len(content)
        except:
            pass

    book.chapter_count = total_chapters
    book.word_count = total_words
    book.character_count = total_chars
    book.page_count = max(1, total_words // 300)
    book.reading_time_minutes = max(1, total_words // 250)

    total_size = 0
    for fname in md_files:
        fpath = os.path.join(path, fname)
        try:
            total_size += os.path.getsize(fpath)
        except:
            pass
    book.file_size = total_size

    has_compiled = 'libro_completo.md' in md_files or total_chapters >= 3
    has_metadata = os.path.exists(os.path.join(path, 'metadata.yaml'))
    has_toc = os.path.exists(os.path.join(path, 'toc.md'))
    has_css = any(f.endswith('.css') for f in os.listdir(path))
    if not has_css:
        parent_css = os.path.join(os.path.dirname(path), 'estilo.css')
        if os.path.exists(parent_css):
            has_css = True

    diag = {
        'project_path': path,
        'total_md_files': len(md_files),
        'total_chapters': total_chapters,
        'total_words': total_words,
        'total_chars': total_chars,
        'has_epub': has_epub,
        'has_pdf': has_pdf,
        'has_cover': has_cover,
        'has_compiled': has_compiled,
        'has_metadata': has_metadata,
        'has_toc': has_toc,
        'has_css': has_css,
        'completeness': 0,
        'missing_items': [],
        'all_ok': True,
    }

    items = [
        ('metadata.yaml', has_metadata, 15),
        ('toc.md', has_toc, 10),
        ('CSS file', has_css, 10),
        ('libro_completo.md', has_compiled, 10),
        ('Portada (cover)', has_cover, 10),
        ('EPUB generado', has_epub, 15),
        ('PDF generado', has_pdf, 10),
        ('Capítulos detectados', total_chapters > 0, 10),
        ('Archivos .md', len(md_files) > 3, 10),
    ]

    score = 0
    missing = []
    for name, present, weight in items:
        if present:
            score += weight
        else:
            missing.append(name)

    diag['completeness'] = score
    diag['missing_items'] = missing
    diag['all_ok'] = len(missing) == 0

    if score >= 90:
        book.status = 'publicado'
    elif score >= 70:
        book.status = 'completo'
    elif score >= 40:
        book.status = 'en_progreso'
    else:
        book.status = 'borrador'

    book.progress_percentage = score
    book.set_diagnostics(diag)
