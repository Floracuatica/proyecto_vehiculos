from django.shortcuts import render, redirect
from .forms import VehiculoForm
from django.http import HttpResponse
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return HttpResponse("<h1>Bienvenido al catálogo de vehículos</h1>")

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})
