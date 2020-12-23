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
def indexAdmin(request):
    return render(request,'menuAdmin.html');

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

def crearCuentaMonetaria(request):
    form=cuentaMonetaria2()
    nombre="Creación de nuevas cuentas monetarias"
    variables = {
        "form": form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form = cuentaMonetaria2(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            codigo=datos.get("codigo_usuario")
            fondo=datos.get("fondo")
            manejo=datos.get("monto_manejo")
            moneda=datos.get("moneda")
            estado=datos.get("estado")
            auto=datos.get("pre_auto")
            id=0
            ch=0


            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO cuentaMonetaria VALUES("+str(id)+"," + str(codigo) + "," + str(fondo) + "," + str(manejo) + ",'" + str(moneda) + "'," + str(estado) + "," + str(auto) + ","+str(ch)+ ")"
            c.execute(consulta)
            db.commit()
            c.close()
            nombre = "Nueva cuenta creada"
            form = cuentaMonetaria2()
            variables = {
                "form": form,
                "mensaje": nombre
            }

        else:
            nombre = "Ya existe una  con los mismos datos"
            variables = {
                "form": form,
                "mensaje": nombre

            }
    return render(request, 'registroCuentaMonetaria.html', variables)

def crearCuentaAhorro(request):
    form=cuentaAhorro()
    nombre="Creación de nuevas cuentas de ahorro"
    variables = {
        "form": form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form = cuentaAhorro(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            codigo=datos.get("codigo_usuario")
            fondo=datos.get("fondo")
            tasa=datos.get("tasa_interes")
            promo=datos.get("promocion")
            moneda=datos.get("moneda")
            estado=datos.get("estado")
            auto=datos.get("pre_auto")
            id=0
            ch=0


            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO cuentaAhorro VALUES("+str(id)+"," + str(codigo) + "," + str(fondo) + "," + str(tasa) + ","+str(promo)+",'" + str(moneda) + "'," + str(estado) + "," + str(auto) + ","+str(ch)+ ")"
            c.execute(consulta)
            db.commit()
            c.close()
            nombre = "Nueva cuenta creada"
            form = cuentaAhorro()
            variables = {
                "form": form,
                "mensaje": nombre
            }

        else:
            nombre = "Ya existe una  con los mismos datos"
            variables = {
                "form": form,
                "mensaje": nombre

            }
    return render(request, 'registroCuentaAhorro.html', variables)

def crearCuentaFija(request):
    form=cuentaFija()
    nombre="Creación de cuentas a plazo fijo"
    variables={
        "form":form,
        "mensaje":nombre
    }
    if request.method=="POST":
        form=cuentaFija(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            codigo=datos.get("codigo_usuario")
            cuota=datos.get("cuota")
            capi=datos.get("capitalizacion")
            tasa=datos.get("tasa_interes")
            fondo=datos.get("fondo_total")
            moneda=datos.get("moneda")
            estado=datos.get("estado")
            id=0
            db=MySQLdb.connect(host=host,user=user,password=contra,db=db_name,connect_timeout=5)
            c=db.cursor()
            consulta="INSERT INTO cuentaFija VALUES ("+str(id)+","+str(codigo)+","+str(cuota)+","+str(capi)+","+str(tasa)+","+str(fondo)+",'"+str(moneda)+"',"+str(estado)+")"
            c.execute(consulta)
            db.commit()
            c.close()
            nombre="Nueva cuenta creada"
            form=cuentaFija()
            variables={
                "form":form,
                "mensaje":nombre
            }

        else:
            nombre = "Ya existe una  con los mismos datos"
            variables = {
                "form": form,
                "mensaje": nombre

            }
    return render(request, 'registroCuentaFija.html', variables)

def generarChequera(request):
    form = chequera()
    nombre = "Creación de chequeras"
    variables = {
        "form": form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form = chequera(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            codigom=datos.get("codigo_monetaria")
            codigoa=datos.get("codigo_ahorro")
            fecha=datos.get("fecha_emision")
            disponibles=datos.get("cheques_disponibles")
            id = 0





            nombre="Nueva chequera registrada"
            form=chequera()
            variables={
                "form":form,
                "mensaje":nombre
            }



        else:
            nombre = "Ya existe una chequera con los mismos datos"
            variables = {
                "form": form,
                "mensaje": nombre

            }
    return render(request, 'generarChequera.html', variables)

def crearChequera(id,codigom,codigoa,fecha,disponibles):
    db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
    c = db.cursor()
    consulta = "INSERT INTO chequera VALUES (" + str(id) + "," + str(codigom) + "," + str(codigoa) + ",'" + str(fecha) + "'," + str(disponibles) + ")"
    c.execute(consulta)
    db.commit()
    c.close()




def depositar(request):
    form = deposito()
    nombre = "Depositar"
    variables = {
        "form": form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form = deposito(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            paga=datos.get("depositante")
            recibe=datos.get("receptor")
            tipo=datos.get("tipo_receptor")
            monto=datos.get("monto")
            moneda=datos.get("moneda")
            id = 0
            tp=int(tipo)

            total=tasaCambio(monto,moneda,recibe,tipo)
            if tp == 1:
                db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "UPDATE cuentaMonetaria SET fondo= '" + str(total) + "'  WHERE id=" + str(recibe)
                c.execute(consulta)
                db.commit()
                c.close()
                print(consulta)
            elif tp == 2:
                db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "UPDATE cuentaAhorro SET fondo= '" + str(total) + "' WHERE id=" + str(recibe)
                c.execute(consulta)
                db.commit()
                c.close()
                print(consulta)
            elif tp == 3:
                db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "UPDATE cuentaFija SET fondo_total= '" + str(total) + "' WHERE id=" + str(recibe)
                c.execute(consulta)
                db.commit()
                c.close()
                print(consulta)


            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO deposito VALUES (" + str(id) + ",'" + str(paga) + "'," + str(recibe) +","+str(tipo)+"," + str(monto) + ",'" + str(moneda) + "')"
            c.execute(consulta)
            db.commit()
            c.close()

            #actualizarMonto(tipo,recibe,depo)

            nombre = "Depósito realizado con éxito"
            form = deposito()
            variables = {
                "form": form,
                "mensaje": nombre
            }

        else:
            nombre = "Datos no válidos"
            variables = {
                "form": form,
                "mensaje": nombre

            }
    return render(request, 'deposito.html', variables)

def tasaCambio(monto,moneda,cuenta,tipo):
    total=0
    tp=int(tipo)
    if tp==1:
        #try:
        c=Cuentamonetaria.objects.get(id=cuenta)
        ficha=c.moneda
        mon=c.fondo
        cambio=calcularCambio(ficha,moneda,monto)
        total=cambio+mon

        #except Cuentamonetaria.DoesNotExist:
         #   return False


    elif tp==2:
        #try:
        c=Cuentaahorro.objects.get(id=cuenta)
        ficha = c.moneda
        mon=c.fondo
        cambio = calcularCambio(ficha, moneda, monto)
        total = cambio + mon
        #except Cuentaahorro.DoesNotExist:
         #   return False

    elif tp==3:
        #try:
        c=Cuentafija.objects.get(id=cuenta)
        ficha = c.moneda
        mon=c.fondo_total
        cambio = calcularCambio(ficha, moneda, monto)
        total = cambio + mon
        #except Cuentaahorro.DoesNotExist:
         #   return False
    return total

def calcularCambio(ficha,moneda,monto):
    cambio=0
    if ficha==moneda:
        cambio=monto
    elif ficha == "$" and moneda == "Q":
        cambio = monto / 7.87
    elif ficha=="Q" and moneda=="$":
        cambio=monto*7.60
    print(cambio)
    return cambio

def actualizarMonto(tipo,cuenta,total):
    if tipo==1:
        db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
        c = db.cursor()
        consulta = "UPDATE cuentaMonetaria SET fondo= '"+str(total)+"'  WHERE id="+str(cuenta)
        c.execute(consulta)
        db.commit()
        c.close()
        print(consulta)
    elif tipo==2:
        db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
        c = db.cursor()
        consulta = "UPDATE cuentaAhorro SET fondo= '" + str(total) + "' WHERE id=" + str(cuenta)
        c.execute(consulta)
        db.commit()
        c.close()
        print(consulta)
    elif tipo==3:
        db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
        c = db.cursor()
        consulta = "UPDATE cuentaFija SET fondo_total= '" + str(total) + "' WHERE id=" + str(cuenta)
        c.execute(consulta)
        db.commit()
        c.close()
        print(consulta)






