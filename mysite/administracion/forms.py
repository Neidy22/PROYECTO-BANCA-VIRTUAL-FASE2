from django import forms
from .models import *

class clienteI(forms.ModelForm):

    class Meta:
        model = Clienteindividual
        fields=("codigo", "cui","nit","nombre","nacimiento","email","telefono")

class clienteIndividual2(forms.Form):
    codigo=forms.IntegerField(required=True, help_text="Solo puedes ingresar números")
    cui=forms.IntegerField(required=True, help_text="Solo puedes ingresar números")
    nit=forms.IntegerField(required=True, help_text="Solo puedes ingresar números")
    nombre = forms.CharField(max_length=50, help_text='Nombre del solicitante', required=True)
    nacimiento = forms.CharField(max_length=50, help_text='Fecha de nacimiento', required=True)
    email = forms.CharField(max_length=50, help_text='Correo electrónico', required=True)
    usuario = forms.CharField(max_length=50, help_text='Nombre de usuario', required=True)
    contrasenia = forms.CharField(max_length=50, help_text='Contraseña de usuario', required=True)
    telefono = forms.CharField(max_length=50, help_text='Teléfono de contacto', required=True)

    class Meta:

        fields = ("codigo", "cui", "nit", "nombre", "nacimiento", "email", "usuario", "contrasenia", "telefono")





