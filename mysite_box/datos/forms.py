from django import forms
from .models import DatosUsuario

class FormularioDatos(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = ['nombre',
                  'apellido', 
                  'edad', 
                  'telefono'
                  ]
