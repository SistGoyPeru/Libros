from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Libro, PayhipClick
from .forms import LibroForm


def home(request):
    categoria_seleccionada = request.GET.get('categoria', '').strip()
    libros = Libro.objects.filter(publicado=True).exclude(payhip_url='').exclude(payhip_url__isnull=True)
    categorias = (
        Libro.objects.filter(publicado=True)
        .exclude(categoria='')
        .values_list('categoria', flat=True)
        .distinct()
        .order_by('categoria')
    )
    if categoria_seleccionada:
        libros = libros.filter(categoria=categoria_seleccionada)
    return render(request, 'store/home.html', {
        'libros': libros,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
    })


def admin_access(request):
    if request.user.is_authenticated:
        return redirect('store_dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('store_dashboard')
        error = 'Usuario o contraseña incorrectos.'

    return render(request, 'store/admin_login.html', {'error': error})


def admin_logout(request):
    logout(request)
    return redirect('home')


def detalle_libro(request, pk):
    libro = get_object_or_404(
        Libro,
        pk=pk,
        publicado=True,
    )
    if not libro.payhip_url:
        raise Http404()
    return render(request, 'store/detalle.html', {'libro': libro})


def comprar_libro(request, pk):
    libro = get_object_or_404(
        Libro,
        pk=pk,
        publicado=True,
    )
    if not libro.payhip_url:
        raise Http404()

    PayhipClick.objects.create(
        libro=libro,
        ip_address=request.META.get('REMOTE_ADDR', ''),
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
    )
    return redirect(libro.payhip_url)


@login_required(login_url='admin_access')
def store_dashboard(request):
    libros = Libro.objects.all().order_by('titulo')
    total_libros = libros.count()
    total_clicks = PayhipClick.objects.count()
    return render(request, 'store/dashboard.html', {
        'libros': libros,
        'total_libros': total_libros,
        'total_clicks': total_clicks,
    })


@login_required(login_url='admin_access')
def book_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_dashboard')
    else:
        form = LibroForm()
    return render(request, 'store/book_form.html', {'form': form, 'action': 'Crear libro'})


@login_required(login_url='admin_access')
def book_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('store_dashboard')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'store/book_form.html', {'form': form, 'action': 'Editar libro'})


@login_required(login_url='admin_access')
def book_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('store_dashboard')
    return render(request, 'store/book_confirm_delete.html', {'libro': libro})
