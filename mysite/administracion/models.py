# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cheque(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo_usuario')
    codigo_monetaria = models.ForeignKey('Cuentamonetaria', models.DO_NOTHING, db_column='codigo_monetaria')
    codigo_ahorro = models.ForeignKey('Cuentaahorro', models.DO_NOTHING, db_column='codigo_ahorro')
    fecha_emision = models.DateField(blank=True, null=True)
    nombre_portador = models.CharField(max_length=100, blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheque'
        unique_together = (('id', 'codigo_usuario', 'codigo_monetaria', 'codigo_ahorro'),)


class Clienteempresarial(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)
    nombre_comercial = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=100)
    nombre_representante = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clienteempresarial'
        unique_together = (('codigo', 'tipo', 'nombre_comercial', 'nombre_empresa'),)


class Clienteindividual(models.Model):
    codigo = models.IntegerField(primary_key=True)
    cui = models.BigIntegerField()
    nit = models.IntegerField()
    primer_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clienteindividual'
        unique_together = (('codigo', 'cui', 'nit'),)


class Cuentaahorro(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo_usuario')
    fondo = models.FloatField(blank=True, null=True)
    tasa_interes = models.FloatField(blank=True, null=True)
    promocion = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentaahorro'
        unique_together = (('id', 'codigo_usuario'),)


class Cuentafija(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo_usuario')
    cuota = models.FloatField(blank=True, null=True)
    capitalizacion = models.IntegerField(blank=True, null=True)
    tasa_interes = models.FloatField(blank=True, null=True)
    fondo_total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentafija'
        unique_together = (('id', 'codigo_usuario'),)


class Cuentamonetaria(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo_usuario')
    fondo = models.FloatField(blank=True, null=True)
    monto_manejo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentamonetaria'
        unique_together = (('id', 'codigo_usuario'),)


class Prestamo(models.Model):
    codigo_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo_usuario')
    monto = models.FloatField(blank=True, null=True)
    modalidad_pago = models.IntegerField(blank=True, null=True)
    interes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo'
        unique_together = (('id', 'codigo_usuario'),)


class Tarjetadebito(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_usuario = models.IntegerField()
    fondo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjetadebito'
        unique_together = (('id', 'codigo_usuario'),)


class Usuario(models.Model):
    codigoe = models.ForeignKey(Clienteempresarial, models.DO_NOTHING, db_column='codigoE')  # Field name made lowercase.
    codigoi = models.ForeignKey(Clienteindividual, models.DO_NOTHING, db_column='codigoI')  # Field name made lowercase.
    usuario = models.CharField(max_length=150, blank=True, null=True)
    contrasenia = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('id', 'codigoe', 'codigoi'),)
