from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Veterinario, Mascota, Propietario
from .forms import VeterinarioForm, MascotaForm, PropietarioForm
from .forms import BusquedaForm, LoginForm



def inicio(request):
    contexto = {
        'mensaje': ''
    }
    return render(request, 'inicio/inicio.html', contexto)


def veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'inicio/veterinarios.html', {'veterinarios': veterinarios})

def mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'inicio/mascotas.html', {'mascotas': mascotas})

def propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'inicio/propietarios.html', {'propietarios': propietarios})

def agregar_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, 'inicio/agregar_veterinario.html', {'form': form})

def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotas')
    else:
        form = MascotaForm()
    return render(request, 'inicio/agregar_mascota.html', {'form': form})

def agregar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'inicio/agregar_propietario.html', {'form': form})

from django.shortcuts import render
from .forms import BusquedaForm
from .models import Veterinario, Mascota, Propietario

def buscar(request):
    form = BusquedaForm(request.GET)
    resultados_veterinarios = []
    resultados_mascotas = []
    resultados_propietarios = []

    if form.is_valid():
        termino_busqueda = form.cleaned_data['termino_busqueda']
        resultados_veterinarios = Veterinario.objects.filter(nombre__icontains=termino_busqueda)
        resultados_mascotas = Mascota.objects.filter(nombre__icontains=termino_busqueda)
        resultados_propietarios = Propietario.objects.filter(nombre__icontains=termino_busqueda)

    return render(request, 'inicio/buscar.html', {
        'form': form,
        'resultados_veterinarios': resultados_veterinarios,
        'resultados_mascotas': resultados_mascotas,
        'resultados_propietarios': resultados_propietarios
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(request, email=email, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')  # Redirige a la página de inicio después del inicio de sesión exitoso
            else:
                form.add_error(None, 'Credenciales inválidas')  # Agrega un error al formulario si las credenciales son inválidas
    else:
        form = LoginForm()
    return render(request, 'inicio/login.html', {'form': form})