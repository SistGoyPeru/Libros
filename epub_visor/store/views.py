from datetime import timedelta
import json

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import (
    AboutMe, BlogArticle, ContactInfo, Course, Libro,
    LibroView, PayhipClick, Project, Service, SocialLink,
    Testimonial, Tool,
)
from .forms import (
    AboutMeForm, BlogArticleForm, BlogCommentForm, ContactInfoForm,
    CourseForm, LibroForm, ProjectForm, ServiceForm, SocialLinkForm,
    TestimonialForm, ToolForm,
)


def home(request):
    about = AboutMe.objects.filter(activo=True).first()
    proyectos = Project.objects.filter(publicado=True)
    cursos = Course.objects.filter(publicado=True)
    herramientas = Tool.objects.all().order_by('categoria', 'orden')
    blog = BlogArticle.objects.filter(publicado=True)
    servicios = Service.objects.filter(publicado=True)
    sociales = SocialLink.objects.all()
    testimonios = Testimonial.objects.filter(publicado=True)
    contacto = ContactInfo.objects.first()
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
        'about': about,
        'proyectos': proyectos,
        'cursos': cursos,
        'herramientas': herramientas,
        'blog': blog,
        'servicios': servicios,
        'sociales': sociales,
        'testimonios': testimonios,
        'contacto': contacto,
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

    LibroView.objects.create(
        libro=libro,
        ip_address=request.META.get('REMOTE_ADDR', ''),
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
    )
    total_views = LibroView.objects.filter(libro=libro).count()
    return render(request, 'store/detalle.html', {'libro': libro, 'total_views': total_views})


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
    total_views = LibroView.objects.count()
    total_clicks = PayhipClick.objects.count()

    days = 14
    today = timezone.localdate()
    start_date = today - timedelta(days=days - 1)
    views_by_date = (
        LibroView.objects
        .filter(timestamp__date__gte=start_date)
        .annotate(day=TruncDate('timestamp'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )
    clicks_by_date = (
        PayhipClick.objects
        .filter(timestamp__date__gte=start_date)
        .annotate(day=TruncDate('timestamp'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )

    view_counts = {item['day']: item['count'] for item in views_by_date}
    click_counts = {item['day']: item['count'] for item in clicks_by_date}
    daily_labels = [(start_date + timedelta(days=i)).strftime('%d %b') for i in range(days)]
    daily_views_data = [view_counts.get(start_date + timedelta(days=i), 0) for i in range(days)]
    daily_clicks_data = [click_counts.get(start_date + timedelta(days=i), 0) for i in range(days)]

    return render(request, 'store/dashboard.html', {
        'libros': libros,
        'total_libros': total_libros,
        'total_views': total_views,
        'total_clicks': total_clicks,
        'daily_views_labels': json.dumps(daily_labels),
        'daily_views_data': json.dumps(daily_views_data),
        'daily_clicks_data': json.dumps(daily_clicks_data),
    })


@login_required(login_url='admin_access')
def admin_profile(request):
    error = None
    success = None
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'profile':
            first_name = request.POST.get('first_name', '').strip()
            email = request.POST.get('email', '').strip()
            if first_name:
                request.user.first_name = first_name
            if email:
                request.user.email = email
            request.user.save()
            success = 'Perfil actualizado correctamente.'
        elif action == 'password':
            old_password = request.POST.get('old_password', '')
            new_password = request.POST.get('new_password', '')
            confirm_password = request.POST.get('confirm_password', '')
            if not request.user.check_password(old_password):
                error = 'La contraseña actual no es correcta.'
            elif len(new_password) < 6:
                error = 'La nueva contraseña debe tener al menos 6 caracteres.'
            elif new_password != confirm_password:
                error = 'Las contraseñas nuevas no coinciden.'
            else:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                success = 'Contraseña cambiada correctamente.'
    return render(request, 'store/admin_profile.html', {
        'error': error,
        'success': success,
    })


@login_required(login_url='admin_access')
def book_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store_dashboard')
    else:
        form = LibroForm()
    return render(request, 'store/book_form.html', {'form': form, 'action': 'Crear libro', 'is_create': True})


@login_required(login_url='admin_access')
def book_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('store_dashboard')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'store/book_form.html', {'form': form, 'libro': libro, 'action': 'Editar libro', 'is_create': False})


@login_required(login_url='admin_access')
def book_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('store_dashboard')
    return render(request, 'store/book_confirm_delete.html', {'libro': libro})


# ─── CRUD Secciones del Portafolio ─────────────────────────────

def _section_list(request, model, template, context_attr, form_class=None):
    items = model.objects.all()
    return render(request, template, {context_attr: items})


def _section_create(request, model, form_class, redirect_url, template, extra_context=None):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    ctx = {'form': form, 'action': f'Crear {model._meta.verbose_name}'}
    if extra_context:
        ctx.update(extra_context)
    return render(request, template, ctx)


def _section_update(request, model, form_class, pk, redirect_url, template, extra_context=None):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=obj)
    ctx = {'form': form, 'action': f'Editar {model._meta.verbose_name}'}
    if extra_context:
        ctx.update(extra_context)
    return render(request, template, ctx)


def _section_delete(request, model, pk, redirect_url, template, display_attr='titulo'):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)
    return render(request, template, {'obj': obj, 'display_attr': display_attr})


# AboutMe ─── solo un registro
@login_required(login_url='admin_access')
def about_edit(request):
    obj = AboutMe.objects.first()
    if request.method == 'POST':
        form = AboutMeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('about_edit')
    else:
        form = AboutMeForm(instance=obj)
    return render(request, 'store/section_form.html', {'form': form, 'action': 'Editar Sobre mí'})


# Project
@login_required(login_url='admin_access')
def project_list(request):
    return _section_list(request, Project, 'store/project_list.html', 'items')

@login_required(login_url='admin_access')
def project_create(request):
    return _section_create(request, Project, ProjectForm, 'project_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def project_update(request, pk):
    return _section_update(request, Project, ProjectForm, pk, 'project_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def project_delete(request, pk):
    return _section_delete(request, Project, pk, 'project_list', 'store/section_confirm_delete.html')


# Course
@login_required(login_url='admin_access')
def course_list(request):
    return _section_list(request, Course, 'store/course_list.html', 'items')

@login_required(login_url='admin_access')
def course_create(request):
    return _section_create(request, Course, CourseForm, 'course_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def course_update(request, pk):
    return _section_update(request, Course, CourseForm, pk, 'course_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def course_delete(request, pk):
    return _section_delete(request, Course, pk, 'course_list', 'store/section_confirm_delete.html')


def blog_detail(request, pk):
    item = get_object_or_404(BlogArticle, pk=pk)
    comentarios = item.comentarios.filter(publicado=True)
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.articulo = item
            comment.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = BlogCommentForm()
    return render(request, 'store/blog_detail.html', {
        'item': item,
        'comentarios': comentarios,
        'form': form,
    })


# Tool
@login_required(login_url='admin_access')
def tool_list(request):
    return _section_list(request, Tool, 'store/tool_list.html', 'items')

@login_required(login_url='admin_access')
def tool_create(request):
    return _section_create(request, Tool, ToolForm, 'tool_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def tool_update(request, pk):
    return _section_update(request, Tool, ToolForm, pk, 'tool_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def tool_delete(request, pk):
    return _section_delete(request, Tool, pk, 'tool_list', 'store/section_confirm_delete.html')


# BlogArticle
@login_required(login_url='admin_access')
def blog_list(request):
    return _section_list(request, BlogArticle, 'store/blog_list.html', 'items')

@login_required(login_url='admin_access')
def blog_create(request):
    return _section_create(request, BlogArticle, BlogArticleForm, 'blog_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def blog_update(request, pk):
    return _section_update(request, BlogArticle, BlogArticleForm, pk, 'blog_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def blog_delete(request, pk):
    return _section_delete(request, BlogArticle, pk, 'blog_list', 'store/section_confirm_delete.html')


# Service
@login_required(login_url='admin_access')
def service_list(request):
    return _section_list(request, Service, 'store/service_list.html', 'items')

@login_required(login_url='admin_access')
def service_create(request):
    return _section_create(request, Service, ServiceForm, 'service_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def service_update(request, pk):
    return _section_update(request, Service, ServiceForm, pk, 'service_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def service_delete(request, pk):
    return _section_delete(request, Service, pk, 'service_list', 'store/section_confirm_delete.html')


# Testimonial
@login_required(login_url='admin_access')
def testimonial_list(request):
    return _section_list(request, Testimonial, 'store/testimonial_list.html', 'items')

@login_required(login_url='admin_access')
def testimonial_create(request):
    return _section_create(request, Testimonial, TestimonialForm, 'testimonial_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def testimonial_update(request, pk):
    return _section_update(request, Testimonial, TestimonialForm, pk, 'testimonial_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def testimonial_delete(request, pk):
    return _section_delete(request, Testimonial, pk, 'testimonial_list', 'store/section_confirm_delete.html')


# SocialLink
@login_required(login_url='admin_access')
def social_list(request):
    return _section_list(request, SocialLink, 'store/social_list.html', 'items')

@login_required(login_url='admin_access')
def social_create(request):
    return _section_create(request, SocialLink, SocialLinkForm, 'social_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def social_update(request, pk):
    return _section_update(request, SocialLink, SocialLinkForm, pk, 'social_list', 'store/section_form.html')

@login_required(login_url='admin_access')
def social_delete(request, pk):
    return _section_delete(request, SocialLink, pk, 'social_list', 'store/section_confirm_delete.html')


# ContactInfo ─── solo un registro
@login_required(login_url='admin_access')
def contact_edit(request):
    obj = ContactInfo.objects.first()
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('section_contact')
    else:
        form = ContactInfoForm(instance=obj)
    return render(request, 'store/section_form.html', {'form': form, 'action': 'Editar Contacto'})


# Dashboard de secciones
@login_required(login_url='admin_access')
def sections_dashboard(request):
    ctx = {
        'total_projects': Project.objects.count(),
        'total_courses': Course.objects.count(),
        'total_tools': Tool.objects.count(),
        'total_blog': BlogArticle.objects.count(),
        'total_services': Service.objects.count(),
        'total_social': SocialLink.objects.count(),
        'total_testimonios': Testimonial.objects.count(),
        'has_about': AboutMe.objects.exists(),
        'has_contact': ContactInfo.objects.exists(),
    }
    return render(request, 'store/sections_dashboard.html', ctx)
