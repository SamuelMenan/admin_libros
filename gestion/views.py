from django.shortcuts import render

# ──────────────────────────────────────────────────
# CRUD LIBROS — Juan José Enríquez
# ──────────────────────────────────────────────────

def lista_libros(request):
    libros = Libro.objects.select_related('autor').all().order_by('titulo')
    return render(request, 'gestion/lista_libros.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion/libro_form.html', {'form': form, 'titulo': 'Agregar Libro'})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/libro_form.html', {'form': form, 'titulo': 'Editar Libro'})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'gestion/libro_confirm_delete.html', {'libro': libro})


def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'gestion/libro_detalle.html', {'libro': libro})