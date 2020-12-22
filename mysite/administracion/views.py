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
            nombre=datos.get("primer_nombre")
            apellido=datos.get("primer_apellido")
            nacimiento=datos.get("nacimiento")

            email=datos.get("email")
            usuario=datos.get("usuario")
            contrasenia=datos.get("contrasenia")
            telefono=datos.get("telefono")

            db= MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c=db.cursor()
            consulta="INSERT INTO clienteIndividual VALUES("+str(codigo)+","+str(cui)+","+str(nit)+",'"+str(nombre)+"','"+str(apellido)+"','"+str(nacimiento)+"','"+email+"',"+str(telefono)+")"
            c.execute(consulta)
            db.commit()
            c.close()
            nombre="Nuevo cliente registrado"
            form=clienteI()
            variables = {
                "form":form,
                "mensaje":nombre
            }

            contrau=codigo+nit
            asignarUsuario(0,0,codigo,apellido,contrau)
        else:
            nombre="Ya existe un cliente con los mismos datos"
            variables= {
                "form":form,
                "mensaje":nombre

            }
    return render(request,'registroCliente.html',variables)


def registroClienteE(request):
    form= clienteE()

    nombre="Registro de clientes empresariales"
    variables={
        "form":form,
        "mensaje": nombre
    }

    if request.method == "POST":
        form= clienteE(data=request.POST)

        if form.is_valid() :
            datos=form.cleaned_data
            codigo=datos.get("codigo")
            tipo=datos.get("tipo")
            nombre_comercial=datos.get("nombre_comercial")
            nombre_empresa=datos.get("nombre_empresa")
            nombre_representante=datos.get("nombre_representante")
            direccion=datos.get("direccion")
            telefono=datos.get("telefono")
            db= MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c=db.cursor()
            consulta="INSERT INTO clienteEmpresarial VALUES("+str(codigo)+",'"+tipo+"','"+str(nombre_comercial)+"', '"+str(nombre_empresa)+"' , '"+str(nombre_representante)+"','"+str(direccion)+"',"+str(telefono)+")"
            c.execute(consulta)
            db.commit()
            c.close()
            contrau=codigo+telefono




            nombre="Nuevo cliente registrado"
            form=clienteE()

            variables = {
                "form":form,
                "mensaje":nombre

            }
            asignarUsuario(0, codigo, 0, nombre_comercial, contrau)
        else:
            nombre="Ya existe un cliente con los mismos datos"
            variables= {
                "form":form,

                "mensaje":nombre

            }

    return render(request,'registroClienteEm.html',variables)

def asignarUsuario(id,codigoe, codigoi,username,password):
    db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
    c = db.cursor()
    consulta = "INSERT INTO usuario VALUES("+str(id)+","+str(codigoe) +","+str(codigoi)+",'" + str(username) + "','" + str(password) + "')"
    c.execute(consulta)
    db.commit()
    c.close()




