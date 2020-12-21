from django.shortcuts import render
from .forms import *
import MySQLdb
from datetime import datetime
host='localhost'
db_name='django'
user='neidy'
contra='Auntyflores12031206'
puerto=3306
# Create your views here.
def registroCliente(request):
    form= clienteI()
    nombre="Registro de clientes"
    variables={
        "form":form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form= clienteI(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            codigo=datos.get("codigo")
            cui=datos.get("cui")
            nit=datos.get("nit")
            nombre=datos.get("nombre")
            nacimiento=datos.get("nacimiento")

            email=datos.get("email")
            usuario=datos.get("usuario")
            contrasenia=datos.get("contrasenia")
            telefono=datos.get("telefono")

            db= MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c=db.cursor()
            consulta="INSERT INTO clienteIndividual VALUES("+str(codigo)+","+str(cui)+","+str(nit)+",'"+str(nombre)+"','"+str(nacimiento)+"','"+email+"',"+str(telefono)+")"
            c.execute(consulta)
            db.commit()
            c.close()
            nombre="Nuevo cliente registrado"
            form=clienteI()
            variables = {
                "form":form,
                "mensaje":nombre
            }
        else:
            nombre="Ya existe un cliente con los mismos datos"
            variables= {
                "form":form,
                "mensaje":nombre

            }
    return render(request,'registroCliente.html',variables)


