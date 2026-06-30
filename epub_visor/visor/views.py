import os, json, zipfile
from xml.etree import ElementTree as ET
from pathlib import Path
from datetime import datetime
from django.utils import timezone
from decimal import Decimal

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.db.models import Q, Sum
from .models import Book, ReadingProgress, Cart, CartItem, Order, OrderItem

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


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


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if not username or not password:
            messages.error(request, 'Completa todos los campos')
        elif password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Cuenta creada correctamente. Ya puedes iniciar sesión.')
            return redirect('login')
    return render(request, 'visor/register.html')


def is_admin(user):
    return user.is_authenticated and user.is_staff


# ============================================================
# LIBRARY
# ============================================================
def library(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')

    # Show public books + user's own uploaded books
    if request.user.is_authenticated:
        books = Book.objects.filter(Q(is_public=True) | Q(uploaded_by=request.user))
    else:
        books = Book.objects.filter(is_public=True)

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    if status_filter:
        books = books.filter(status=status_filter)

    stats = {
        'total': books.count(),
        'opencode': Book.objects.filter(is_opencode_project=True).count(),
        'pages': Book.objects.aggregate(Sum('page_count'))['page_count__sum'] or 0,
        'words': Book.objects.aggregate(Sum('word_count'))['word_count__sum'] or 0,
    }

    return render(request, 'visor/library.html', {
        'books': books,
        'query': query,
        'status_filter': status_filter,
        'stats': stats,
    })


# ============================================================
# BOOK DETAIL / DASHBOARD
# ============================================================
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    progress, _ = ReadingProgress.objects.get_or_create(book=book)
    diag = book.get_diagnostics()
    chapters = _get_chapters(book)
    return render(request, 'visor/book_detail.html', {
        'book': book,
        'progress': progress,
        'diagnostics': diag,
        'chapters': chapters,
    })


# ============================================================
# EPUB READER (Kindle-style)
# ============================================================
def reader(request, slug):
    book = get_object_or_404(Book, slug=slug)
    chapters = _get_chapters(book)
    book.last_read_at = timezone.now()
    book.save(update_fields=['last_read_at'])

    chapter_index = int(request.GET.get('chapter', 0))
    if chapter_index < 0:
        chapter_index = 0
    if chapter_index >= len(chapters):
        chapter_index = len(chapters) - 1

    current_chapter = chapters[chapter_index] if chapters else {}
    content = current_chapter.get('content', '<p>Sin contenido</p>')
    content = _clean_html_for_display(content)

    # Update progress
    progress, _ = ReadingProgress.objects.get_or_create(book=book)
    progress.current_chapter = chapter_index
    progress.current_percent = int((chapter_index / max(len(chapters), 1)) * 100)
    progress.save()

    return render(request, 'visor/reader.html', {
        'book': book,
        'content': content,
        'chapter_index': chapter_index,
        'total_chapters': len(chapters),
        'chapter_title': current_chapter.get('title', ''),
        'progress_value': progress.current_percent,
    })


# ============================================================
# UPLOAD EPUB
# ============================================================
def upload_book(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        epub_file = request.FILES.get('epub_file')
        is_opencode = request.POST.get('is_opencode_project') == 'on'
        opencode_path = request.POST.get('opencode_path', '').strip()

        if not epub_file and not title:
            return render(request, 'visor/upload.html', {'error': 'Debes subir un archivo EPUB o ingresar un título'})

        book = Book(
            title=title or epub_file.name.replace('.epub', '').replace('.EPUB', ''),
            author=author or 'Unknown',
            is_opencode_project=is_opencode,
            opencode_path=opencode_path,
            uploaded_by=request.user if request.user.is_authenticated else None,
            is_public=False,
        )

        if epub_file:
            book.epub_file = epub_file
            book.save()
            book.extract_metadata()
            if not title:
                book.title = book.title or epub_file.name.replace('.epub', '').replace('.EPUB', '')
            book.save()
        else:
            book.save()

        return redirect('book_detail', slug=book.slug)

    projects = _scan_opencode_projects()
    return render(request, 'visor/upload.html', {'projects': projects})


# ============================================================
# DOWNLOAD EPUB
# ============================================================
def download_epub(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if not book.epub_file:
        messages.error(request, 'Este libro no tiene archivo EPUB disponible')
        return redirect('book_detail', slug=slug)
    return FileResponse(
        book.epub_file.open('rb'),
        as_attachment=True,
        filename=f'{book.slug}.epub',
        content_type='application/epub+zip',
    )


# ============================================================
# DOWNLOAD PDF
# ============================================================
def download_pdf(request, slug):
    book = get_object_or_404(Book, slug=slug)
    # If pdf_file is set in DB, serve it
    if book.pdf_file and os.path.exists(book.pdf_file.path):
        return FileResponse(
            book.pdf_file.open('rb'),
            as_attachment=True,
            filename=f'{book.slug}.pdf',
            content_type='application/pdf',
        )
    # Otherwise try to find it in opencode project path
    if book.is_opencode_project and book.opencode_path:
        for f in os.listdir(book.opencode_path):
            if f.lower().endswith('.pdf'):
                fpath = os.path.join(book.opencode_path, f)
                return FileResponse(
                    open(fpath, 'rb'),
                    as_attachment=True,
                    filename=f'{book.slug}.pdf',
                    content_type='application/pdf',
                )
    messages.error(request, 'Este libro no tiene archivo PDF disponible')
    return redirect('book_detail', slug=slug)


# ============================================================
# SCAN OPENCODE PROJECTS (admin only)
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
# RUN DIAGNOSTICS ON A BOOK (admin only)
# ============================================================
@user_passes_test(is_admin)
def run_diagnostics(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if book.is_opencode_project and book.opencode_path:
        _check_opencode_diagnostics(book)
        book.save()
    return redirect('book_detail', slug=slug)


# ============================================================
# DELETE BOOK
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
# HELPER: Get chapters from EPUB or markdown source
# ============================================================
def _get_chapters(book):
    if book.epub_file:
        chapters = _get_chapters_from_epub(book)
        if chapters:
            return chapters
    if book.is_opencode_project and book.opencode_path:
        return _get_chapters_from_markdown(book)
    return []


def _get_chapters_from_epub(book):
    path = book.epub_file.path
    if not os.path.exists(path):
        return []
    chapters = []
    try:
        with zipfile.ZipFile(path, 'r') as z:
            if 'META-INF/container.xml' not in z.namelist():
                return []
            container = ET.fromstring(z.read('META-INF/container.xml'))
            ns_c = {'c': 'urn:oasis:names:tc:opendocument:xmlns:container'}
            rootfile = container.find('.//c:rootfile', ns_c)
            if rootfile is None:
                return []
            opf_path = rootfile.get('full-path')
            opf_data = z.read(opf_path)
            root = ET.fromstring(opf_data)
            ns = {'opf': 'http://www.idpf.org/2007/opf'}
            manifest = root.find('opf:manifest', ns) or root.find('manifest')
            spine = root.find('opf:spine', ns) or root.find('spine')
            if manifest is None or spine is None:
                return []
            items = {}
            for item in manifest:
                items[item.get('id')] = item.get('href', '')
            base_dir = str(Path(opf_path).parent).replace('\\', '/')
            for ref in spine:
                idref = ref.get('idref', '')
                if idref in items:
                    href = items[idref]
                    file_path = f'{base_dir}/{href}' if base_dir != '.' else href
                    if file_path in z.namelist():
                        raw = z.read(file_path)
                        text = raw.decode('utf-8', errors='ignore')
                        title = _extract_title(text) or href
                        content_text = _extract_body(text)
                        chapters.append({
                            'id': idref,
                            'title': title,
                            'content': content_text,
                            'href': href,
                        })
    except Exception as e:
        print(f'Error reading EPUB chapters: {e}')
    return chapters


def _get_chapters_from_markdown(book):
    """Read chapters from opencode markdown project files."""
    import re as re_mod
    proj_path = book.opencode_path
    if not os.path.isdir(proj_path):
        return []
    md_files = sorted([f for f in os.listdir(proj_path)
                       if f.endswith('.md') and not f.startswith('libro_completo')])
    chapters = []
    for fname in md_files:
        fpath = os.path.join(proj_path, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            continue
        # Extract title from first # heading
        title = fname
        m = re_mod.search(r'^#\s+(.+)$', content, re_mod.MULTILINE)
        if m:
            title = m.group(1).strip()
        # Convert markdown to simple HTML for display
        html = _md_to_simple_html(content)
        chapters.append({
            'id': fname,
            'title': title,
            'content': html,
            'href': fname,
        })
    return chapters


def _md_to_simple_html(md):
    """Convert basic markdown to simple HTML for reader display."""
    import re as re_mod
    lines = md.split('\n')
    html_parts = []
    in_code = False
    code_lines = []
    in_list = False
    first_heading = True

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_code:
                html_parts.append(f'<pre><code>{"<br>".join(code_lines)}</code></pre>')
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line.rstrip())
            continue

        # Headings
        m = re_mod.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            # Skip the very first H1 (it's the chapter title shown separately)
            if first_heading and level == 1:
                first_heading = False
                continue
            first_heading = False
            html_parts.append(f'<h{level}>{text}</h{level}>')
            continue

        # Horizontal rule
        if re_mod.match(r'^---+\s*$', line) and not in_list:
            html_parts.append('<hr>')
            continue

        # Lists
        if re_mod.match(r'^[\-\*]\s+', line):
            text = re_mod.sub(r'^[\-\*]\s+', '', line)
            text = _inline_md(text)
            html_parts.append(f'<li>{text}</li>')
            in_list = True
            continue
        else:
            if in_list:
                html_parts.append('</ul>')
                in_list = False

        # Blockquote
        if line.startswith('> '):
            text = _inline_md(line[2:])
            html_parts.append(f'<blockquote>{text}</blockquote>')
            continue

        # Empty line = paragraph break
        if not line.strip():
            html_parts.append('')
            continue

        # Regular paragraph
        text = _inline_md(line)
        html_parts.append(f'<p>{text}</p>')

    if in_code:
        html_parts.append(f'<pre><code>{"<br>".join(code_lines)}</code></pre>')
    if in_list:
        html_parts.append('</ul>')

    return '\n'.join(html_parts)


def _inline_md(text):
    """Convert inline markdown formatting to HTML."""
    import re as re_mod
    # Bold italic ***text***
    text = re_mod.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold **text**
    text = re_mod.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic *text*
    text = re_mod.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code `text`
    text = re_mod.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def _extract_title(html):
    import re
    m = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r'<h[1][^>]*>(.*?)</h[1]>', html, re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return ''


def _extract_body(html):
    import re
    m = re.search(r'<body[^>]*>(.*?)</body>', html, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1)
    return html


def _clean_html_for_display(html):
    import re
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<link[^>]*>', '', html, flags=re.IGNORECASE)
    # Keep basic formatting but remove dangerous attributes
    html = re.sub(r'\s+on\w+="[^"]*"', '', html, flags=re.IGNORECASE)
    return html


# ============================================================
# HELPER: Scan opencode projects
# ============================================================
def _scan_opencode_projects():
    base = os.environ.get('OPENCODE_BOOKS_DIR', str(Path(__file__).resolve().parent.parent.parent))
    projects = []
    for entry in os.listdir(base):
        full = os.path.join(base, entry)
        if os.path.isdir(full) and entry != 'epub_visor' and entry != 'venv_epub':
            # Check if it has markdown files (looks like a book project)
            md_files = [f for f in os.listdir(full) if f.endswith('.md')]
            if md_files:
                title = entry.replace('_', ' ').title().replace(' ', ' ')
                # Read portada for real title
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


# ============================================================
# HELPER: Check opencode project completeness
# ============================================================
def _check_opencode_diagnostics(book):
    path = book.opencode_path
    if not path or not os.path.isdir(path):
        return

    md_files = sorted([f for f in os.listdir(path) if f.endswith('.md')])
    has_epub = any(f.endswith('.epub') for f in os.listdir(path))
    has_pdf = any(f.endswith('.pdf') for f in os.listdir(path))
    has_cover = any(f.startswith('cover') and (f.endswith('.jpg') or f.endswith('.png'))
                    for f in os.listdir(path))

    # Auto-copy PDF to media if found and not set
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

    # Copy cover to media if not already set
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
    # Count ALL md files except portada/credits/etc as chapters
    if total_chapters == 0:
        total_chapters = len([f for f in md_files if f[0:2].isdigit()])

    # Calculate word count, page count from markdown files
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

    # File size: sum of all md files
    total_size = 0
    for fname in md_files:
        fpath = os.path.join(path, fname)
        try:
            total_size += os.path.getsize(fpath)
        except:
            pass
    book.file_size = total_size

    # Check if libro_completo.md exists OR has individual chapters (equivalent)
    has_compiled = 'libro_completo.md' in md_files or total_chapters >= 3

    # Check metadata (project-level or shared)
    has_metadata = os.path.exists(os.path.join(path, 'metadata.yaml'))

    # Check TOC
    has_toc = os.path.exists(os.path.join(path, 'toc.md'))

    # Check CSS (project-level or shared ../estilo.css)
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


# ============================================================
# CART HELPERS
# ============================================================
def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


# ============================================================
# ADD TO CART
# ============================================================
@login_required
def add_to_cart(request, slug):
    book = get_object_or_404(Book, slug=slug, is_public=True)
    cart = get_or_create_cart(request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'"{book.title}" añadido al carrito')
    return redirect(request.META.get('HTTP_REFERER', 'library'))


# ============================================================
# REMOVE FROM CART
# ============================================================
@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, 'Item eliminado del carrito')
    return redirect('cart')


# ============================================================
# CART DETAIL
# ============================================================
@login_required
def cart_detail(request):
    cart = get_or_create_cart(request.user)
    return render(request, 'visor/cart.html', {'cart': cart})


# ============================================================
# BUY NOW
# ============================================================
@login_required
def buy_now(request, slug):
    book = get_object_or_404(Book, slug=slug, is_public=True)
    cart = get_or_create_cart(request.user)
    CartItem.objects.filter(cart=cart).delete()
    CartItem.objects.create(cart=cart, book=book, quantity=1)
    return redirect('checkout')


# ============================================================
# CHECKOUT
# ============================================================
@login_required
def checkout(request):
    cart = get_or_create_cart(request.user)
    if cart.items.count() == 0:
        messages.warning(request, 'Tu carrito está vacío')
        return redirect('library')

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        city = request.POST.get('city', '').strip()
        zip_code = request.POST.get('zip_code', '').strip()

        if not all([full_name, email, address, city, zip_code]):
            messages.error(request, 'Completa todos los campos')
            return render(request, 'visor/checkout.html', {
                'cart': cart,
                'stripe_key': settings.STRIPE_PUBLIC_KEY,
            })

        # Create Stripe Checkout Session
        line_items = []
        for item in cart.items.all():
            line_items.append({
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': item.book.title,
                        'images': [request.build_absolute_uri(item.book.cover_image.url)] if item.book.cover_image else [],
                    },
                    'unit_amount': int(item.book.price * 100),
                },
                'quantity': item.quantity,
            })

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri('/checkout/success/') + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri('/checkout/cancel/'),
                metadata={
                    'user_id': str(request.user.id),
                    'cart_id': str(cart.id),
                    'full_name': full_name,
                    'email': email,
                    'address': address,
                    'city': city,
                    'zip_code': zip_code,
                },
            )
            return redirect(session.url, code=303)
        except Exception as e:
            messages.error(request, f'Error al procesar pago: {e}')
            return render(request, 'visor/checkout.html', {
                'cart': cart,
                'stripe_key': settings.STRIPE_PUBLIC_KEY,
            })

    return render(request, 'visor/checkout.html', {
        'cart': cart,
        'stripe_key': settings.STRIPE_PUBLIC_KEY,
    })


# ============================================================
# CHECKOUT SUCCESS
# ============================================================
@login_required
def checkout_success(request):
    session_id = request.GET.get('session_id', '')
    cart = get_or_create_cart(request.user)

    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            meta = session.metadata

            # Create order
            order = Order.objects.create(
                user=request.user,
                full_name=meta.get('full_name', request.user.get_full_name() or request.user.username),
                email=meta.get('email', request.user.email),
                address=meta.get('address', ''),
                city=meta.get('city', ''),
                zip_code=meta.get('zip_code', ''),
                status='pagado',
                stripe_payment_intent=session.payment_intent,
                paid_at=timezone.now(),
            )

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    book=item.book,
                    price=item.book.price,
                    quantity=item.quantity,
                )

            # Clear cart
            cart.items.all().delete()

            messages.success(request, f'¡Pedido #{order.id} pagado con éxito!')
            return redirect('order_detail', order_id=order.id)

        except Exception as e:
            messages.error(request, f'Error verificando pago: {e}')

    return render(request, 'visor/checkout_success.html')


# ============================================================
# CHECKOUT CANCEL
# ============================================================
@login_required
def checkout_cancel(request):
    messages.warning(request, 'Pago cancelado')
    return redirect('cart')


# ============================================================
# ORDER LIST
# ============================================================
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'visor/orders.html', {'orders': orders})


# ============================================================
# ORDER DETAIL
# ============================================================
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'visor/order_detail.html', {'order': order})


# ============================================================
# STRIPE WEBHOOK
# ============================================================
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        meta = session.get('metadata', {})
        user_id = meta.get('user_id')

        if user_id and not Order.objects.filter(stripe_payment_intent=session.get('payment_intent')).exists():
            try:
                user = User.objects.get(id=user_id)
                cart_items = CartItem.objects.filter(cart__user=user)

                if cart_items.exists():
                    order = Order.objects.create(
                        user=user,
                        full_name=meta.get('full_name', user.username),
                        email=meta.get('email', user.email),
                        address=meta.get('address', ''),
                        city=meta.get('city', ''),
                        zip_code=meta.get('zip_code', ''),
                        status='pagado',
                        stripe_payment_intent=session.get('payment_intent'),
                        paid_at=timezone.now(),
                    )
                    for item in cart_items:
                        OrderItem.objects.create(order=order, book=item.book, price=item.book.price, quantity=item.quantity)
                    cart_items.delete()
            except User.DoesNotExist:
                pass

    return HttpResponse(status=200)

