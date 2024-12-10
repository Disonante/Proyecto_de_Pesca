from django.shortcuts import render, redirect, get_object_or_404
from .models import RegistroPesca
from .forms import RegistroPescaForm

def lista_registros(request):
    registros = RegistroPesca.objects.all().order_by('-creado_el')
    return render(request, 'pesca/lista_registros.html', {'registros': registros})

def agregar_registro(request):
    if request.method == 'POST':
        form = RegistroPescaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroPescaForm()
    return render(request, 'pesca/agregar_registro.html', {'form': form})

def editar_registro(request, id):
    registro = get_object_or_404(RegistroPesca, id=id)
    if request.method == 'POST':
        form = RegistroPescaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroPescaForm(instance=registro)
    return render(request, 'pesca/editar_registro.html', {'form': form})

def eliminar_registro(request, id):
    registro = get_object_or_404(RegistroPesca, id=id)
    if request.method == 'POST':
        registro.delete()
        return redirect('lista_registros')
    return render(request, 'pesca/eliminar_registro.html', {'registro': registro})
