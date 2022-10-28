# Personalizacion de los Formularios en Django, el app HOME
from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
            )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                        'placeholder': 'Ingrese un texto aqui'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un texto aqui'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese un numero aqui'
                }
            )
        }
            
    # Metodo que valida el valor del campo "cantidad"
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 1:
            raise forms.ValidationError('Ingrese un numero mayor a 0')
        return cantidad
        
