from django import forms
from .models import *

class clienteI(forms.ModelForm):

    class Meta:
        model = Clienteindividual
        fields=("codigo", "cui","nit","primer_nombre","primer_apellido","nacimiento","nacimiento","email","telefono")

class clienteIndividual2(forms.Form):
    codigo=forms.IntegerField(required=True, help_text="Solo puedes ingresar números")
    cui=forms.IntegerField(required=True, help_text="Solo puedes ingresar números")
    nit=forms.IntegerField(required=True, help_text="Solo puedes ingresar números")
    primer_nombre = forms.CharField(max_length=50, help_text='Nombre del solicitante', required=True)
    primer_apellido=forms.CharField(max_length=50, help_text='Apellido del solicitante', required=True)
    nacimiento = forms.DateField(help_text='Fecha de nacimiento', required=True)
    email = forms.EmailField(help_text='Correo electrónico', required=True)
    usuario = forms.CharField(max_length=50, help_text='Nombre de usuario', required=True)
    contrasenia = forms.CharField(max_length=50, help_text='Contraseña de usuario', required=True)
    telefono = forms.CharField(max_length=50, help_text='Teléfono de contacto', required=True)

    class Meta:

        fields = ("codigo", "cui", "nit", "primer_nombre","primer_apellido", "nacimiento", "email", "usuario", "contrasenia", "telefono")

class clienteE(forms.ModelForm):
    class Meta:
        model=Clienteempresarial
        fields=("codigo","tipo", "nombre_comercial", "nombre_empresa", "nombre_representante", "direccion","telefono")

class clienteE2(forms.Form):
    codigo = forms.IntegerField(required=True, help_text="Solo puedes ingresar números")
    tipo = forms.TypedChoiceField(help_text='Tipo de empresa', required=True)
    nombre_comercial=forms.CharField(max_length=50, help_text='Nombre comercial', required=True)
    nombre_empresa=forms.CharField(max_length=50, help_text='Contraseña de usuario', required=True)
    nombre_representante=forms.CharField(max_length=50, help_text='Nombre de representante', required=True)
    direccion=forms.CharField(max_length=50, help_text='Dirección', required=True)
    telefono = forms.IntegerField(required=True, help_text="Solo puedes ingresar números")


    class Meta:
        fields=("codigo","tipo", "nombre_comercial", "nombre_empresa", "nombre_representante", "direccion","telefono")







