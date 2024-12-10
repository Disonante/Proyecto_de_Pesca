from django import forms
from .models import RegistroPesca

class RegistroPescaForm(forms.ModelForm):
    class Meta:
        model = RegistroPesca
        fields = [
<<<<<<< HEAD
            #'fecha_jornada', 
            'altura_ola', 
            'direccion_ola', 
            'periodo_ola', 
            'direccion_viento', 
            'velocidad_viento', 
            'coeficiente_marea', 
            'situacion_geografica', 
            'capturas'
=======
            'altura_ola', 'direccion_ola', 'periodo_ola', 
            'direccion_viento', 'velocidad_viento', 
            'coeficiente_marea', 'situacion_geografica', 'capturas'
>>>>>>> e4622efc28a26aed0391c0db3ce1f5a4bdd34f5b
        ]
        widgets = {
            'altura_ola': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
            'velocidad_viento': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
            'coeficiente_marea': forms.NumberInput(attrs={'min': 0}),
            'capturas': forms.Textarea(attrs={'rows': 3}),
<<<<<<< HEAD
            #'fecha_de_la_jornada': forms.Textarea(attrs={'rows': 1})
=======
>>>>>>> e4622efc28a26aed0391c0db3ce1f5a4bdd34f5b
        }
