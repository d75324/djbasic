from django import forms
from .models import DatosUsuario, Profesionales

class FormularioDatos(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = ['nombre',
                  'apellido', 
                  'edad', 
                  'telefono'
                  ]

class FormularioDeCargaDeProfesionales(forms.ModelForm):
    class Meta:
        model = Profesionales
        fields = [
                'usuario',
                'profesion',
                'anio_egreso',
                'experiencia',
                'experiencia_docente',
                'estado'
                    ]
        
        
class Short(forms.ModelForm):
    nombre_usuario = forms.ModelChoiceField(queryset=DatosUsuario.objects.all(), label="Nombre del Usuario")

    class Meta:
        model = Profesionales
        fields = [
                'nombre_usuario',
                'profesion',
                'anio_egreso',
                'experiencia',
                'experiencia_docente',
                'estado'
                    ]
