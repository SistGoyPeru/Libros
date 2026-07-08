from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'descripcion',
            'excerpt',
            'categoria',
            'portada_url',
            'pdf_url',
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
