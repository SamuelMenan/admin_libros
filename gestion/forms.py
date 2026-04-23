from django import forms
from .models import Autor, Libro

BASE_INPUT_CLASSES = (
    'mt-1 w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 '
    'text-slate-800 shadow-sm outline-none transition '
    'focus:border-cyan-500 focus:ring-2 focus:ring-cyan-200'
)


def apply_tailwind_styles(form):
    for field in form.fields.values():
        widget = field.widget
        classes = widget.attrs.get('class', '').strip()
        widget.attrs['class'] = f'{classes} {BASE_INPUT_CLASSES}'.strip()


class AutorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind_styles(self)

    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }


class LibroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind_styles(self)

    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }