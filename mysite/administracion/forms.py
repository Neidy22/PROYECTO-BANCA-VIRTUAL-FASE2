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

class cuentaMonetaria(forms.ModelForm):
    class Meta:
        model=Cuentamonetaria
        fields=("id","codigo_usuario","fondo","monto_manejo","moneda","estado","pre_auto")

class cuentaMonetaria2(forms.Form):
    opciones=(("1","Activada"),("0","Desactivada"))
    codigo_usuario=forms.IntegerField(required=True,label="Código de usuario")
    fondo=forms.FloatField(required=True, label="Fondo")
    monto_manejo=forms.FloatField(required=True, label="Monto por manejo de cuenta:")
    moneda=forms.CharField(max_length=1, label="Tipo de moneda: ")
    estado=forms.ChoiceField(required=True, label="Estado de la cuenta",choices=opciones)
    pre_auto=forms.ChoiceField(required=True, label="Pre-autorización de cheques:",choices=opciones)

    class Meta:

        fields=("id","codigo_usuario","fondo","monto_manejo","moneda","estado","pre_auto")

class cuentaAhorro(forms.Form):
    opciones=(("1","Activada"),("0","Desactivada"))
    codigo_usuario=forms.IntegerField(required=True,label="Código de usuario:")
    fondo = forms.FloatField(required=True, label="Fondo:")
    tasa_interes = forms.FloatField(required=True, label="Tasa de Interés:")
    promocion=forms.FloatField(required=True, label="Promoción")
    moneda = forms.CharField(max_length=1, label="Tipo de moneda:")
    estado = forms.ChoiceField(required=True, label="Estado de la cuenta:", choices=opciones)
    pre_auto = forms.ChoiceField(required=True, label="Pre-autorización de cheques:", choices=opciones)

    class Meta:
        fields=("id","codigo_usuario","fondo","tasa_interes","promocion","moneda","estado","pre_auto")

class cuentaFija(forms.Form):
    opciones = (("1", "Activada"), ("0", "Desactivada"))
    opc=(("1","3"),("2","6"),("3","12"),("4","24"),("5","36"))
    codigo_usuario=forms.IntegerField(required=True,label="Código de usuario:")
    cuota=forms.FloatField(required=True, label="Cuota:")
    capitalizacion=forms.ChoiceField(required=True,label="Tiempo en meses:",choices=opc)
    tasa_interes=forms.FloatField(required=True, label="Tasa de interés:")
    fondo_total=forms.FloatField(required=True, label="Fondo Total:")
    moneda=forms.CharField(max_length=1,label="Tipo de moneda:")
    estado = forms.ChoiceField(required=True, label="Estado de la cuenta:", choices=opciones)

    class Meta:
        fields=("id","codigo_usuario","cuota","capitalizacion","tasa_interes","fondo_total","moneda","estado")






