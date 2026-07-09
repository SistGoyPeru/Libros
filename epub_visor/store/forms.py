from django import forms
from .models import (
    AboutMe, BlogArticle, BlogComment, ContactInfo, Course, Libro,
    Project, Service, SocialLink, Testimonial, Tool,
)


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'descripcion',
            'excerpt',
            'categoria',
            'portada_url',
            'portada_archivo',
            'pdf_url',
            'pdf_archivo',
            'epub_archivo',
            'precio',
            'payhip_url',
            'publicado',
            'folder_name',
            'epub_filename',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5}),
            'excerpt': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Agrega aquí la parte importante o un extracto breve del libro.'}),
        }


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 6}),
            'hero_title': forms.TextInput(attrs={'placeholder': 'Ej: Transforma datos en poder'}),
            'hero_subtitle': forms.TextInput(attrs={'placeholder': 'Ej: Dashboards, automatización y análisis para tu negocio'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {'descripcion': forms.Textarea(attrs={'rows': 4})}


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {'descripcion': forms.Textarea(attrs={'rows': 4})}


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'


class BlogArticleForm(forms.ModelForm):
    class Meta:
        model = BlogArticle
        fields = '__all__'
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 8}),
            'resumen': forms.Textarea(attrs={'rows': 3}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {'descripcion': forms.Textarea(attrs={'rows': 4})}


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {'texto': forms.Textarea(attrs={'rows': 4})}


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['nombre', 'texto']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
        }


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = '__all__'


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'
        widgets = {'mensaje_bienvenida': forms.Textarea(attrs={'rows': 4})}
