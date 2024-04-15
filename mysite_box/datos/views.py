from django.shortcuts import render, redirect
from .forms import FormularioDatos
from .models import DatosUsuario, Profesionales
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

# esta vista corresponde a un formulario al cual se puede acceder desde
# el template 'formulario.html'. Una vez que el formulario se completa, los
# datos se guardan en la tabla DatosUsuario.

def formulariobasico(request):
    if request.method == 'POST':
        # la instancia se llama telaviv para poder identificarla correctamente
        telaviv = FormularioDatos(request.POST)
        if telaviv.is_valid():
            telaviv.save()
            messages.success(request, "Los datos se registraron correctamente")
            return redirect('form')
    else:
        telaviv = FormularioDatos(request.POST)
    return render(request, 'formulario.html')

# esto es una vista que lista en 'beirut' todos
# los registros de la tabla 'DatosUsuario', ordenados por 'fecha_creacion'

def historico(request):
    context = {}
    beirut = DatosUsuario.objects.all().order_by('-fecha_creacion')
    context['beirut'] = beirut
    return render(request, 'historico.html', context)

# listar los profesionales por edad
def otravista(request):
    context = {}
    libano = DatosUsuario.objects.all().order_by('-edad')
    context['libano'] = libano
    return render(request, 'edad.html', context)

# crear un par de vistas sobre el modelo 'Profesionales'.
# primero, voy a crear un formulario para cargar Profesionales

def formularioprofesionales(request):
    if request.method == 'POST':
        elcairo = FormularioDatos(request.POST)
        if elcairo.is_valid():
            elcairo.save()
            #messages.success(request, "Los datos del profesional se registraron correctamente")
            return redirect('home')
    else:
        elcairo = FormularioDatos(request.POST)
    return render(request, 'profesionales.html')

def todoslosprofesionalesvista(request):
    context = {}
    aman = Profesionales.objects.all().order_by('-anio_egreso')
    context['aman'] = aman
    return render(request, 'todoslosprofesionales.html', context)