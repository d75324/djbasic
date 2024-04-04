from django.shortcuts import render, redirect
from .forms import FormularioDatos
from .models import DatosUsuario
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
