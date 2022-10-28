# Personalizacion de los Formularios en Django, el app PERSONAL
# Models de Django
from django import forms
# Models de la BD Empleado
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:

        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'image',
            'habilidades',
            )
        widgets = {
            'habilidades' : forms.CheckboxSelectMultiple()
            }
