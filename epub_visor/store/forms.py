from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'descripcion',
            'categoria',
            'portada_url',
            'precio',
            'payhip_url',
            'publicado',
            'folder_name',
            'epub_filename',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5}),
        }
