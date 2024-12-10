from django import forms
from .models import RegistroPesca

class RegistroPescaForm(forms.ModelForm):
    class Meta:
        model = RegistroPesca
        fields = [
            #'fecha_jornada', 
            'altura_ola', 
            'direccion_ola', 
            'periodo_ola', 
            'direccion_viento', 
            'velocidad_viento', 
            'coeficiente_marea', 
            'situacion_geografica', 
            'capturas'
        ]
        widgets = {
            'altura_ola': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
            'velocidad_viento': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
            'coeficiente_marea': forms.NumberInput(attrs={'min': 0}),
            'capturas': forms.Textarea(attrs={'rows': 3}),
            #'fecha_de_la_jornada': forms.Textarea(attrs={'rows': 1})
        }
