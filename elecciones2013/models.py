# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Candidatos(models.Model):
    dignidad_codigo = models.ForeignKey('Dignidades', db_column='dignidad_codigo', blank=True, null=True)
    op_codigo = models.ForeignKey('Orgpoliticas', db_column='op_codigo', blank=True, null=True)
    candidato_codigo = models.IntegerField(primary_key=True)
    candidato_orden = models.IntegerField(blank=True, null=True)
    provincia_codigo = models.ForeignKey('Provincias', db_column='provincia_codigo', blank=True, null=True)
    circunscripcion_codigo = models.IntegerField(blank=True, null=True)
    canton_codigo = models.ForeignKey('Cantones', db_column='canton_codigo', blank=True, null=True)
    parroquia_codigo = models.ForeignKey('Parroquias', db_column='parroquia_codigo', blank=True, null=True)
    candidato_nombre = models.CharField(max_length=50, blank=True, null=True)
    candidato_sexo = models.IntegerField(blank=True, null=True)
    candidato_edad_exacta = models.FloatField(blank=True, null=True)
    candidatos_grupos_de_edad = models.IntegerField(blank=True, null=True)
    suplente_nombre1 = models.CharField(max_length=50, blank=True, null=True)
    suplente_sexo1 = models.IntegerField(blank=True, null=True)
    suplente_edad_exacta1 = models.FloatField(blank=True, null=True)
    suplente_grupos_de_edad1 = models.IntegerField(blank=True, null=True)
    suplente_nombre2 = models.CharField(max_length=50, blank=True, null=True)
    suplente_sexo2 = models.IntegerField(blank=True, null=True)
    suplente_edad_exacta2 = models.FloatField(blank=True, null=True)
    suplente_grupos_de_edad2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidatos'


class Cantones(models.Model):
    canton_codigo = models.IntegerField(primary_key=True)
    canton_nombre = models.CharField(max_length=50, blank=True, null=True)
    provincia_codigo = models.ForeignKey('Provincias', db_column='provincia_codigo', blank=True, null=True)
    provincia_nombre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantones'


class Dignidades(models.Model):
    dignidad_codigo = models.IntegerField(primary_key=True)
    dignidad_nombre = models.CharField(max_length=50, blank=True, null=True)
    dignidad_ambito = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dignidades'


class Orgpoliticas(models.Model):
    op_codigo = models.IntegerField(primary_key=True)
    provincia_codigo = models.IntegerField(blank=True, null=True)
    canton_codigo = models.IntegerField(blank=True, null=True)
    parroquia_codigo = models.IntegerField(blank=True, null=True)
    op_tipo = models.CharField(max_length=25, blank=True, null=True)
    op_ambito = models.CharField(max_length=10, blank=True, null=True)
    op_nombre = models.CharField(max_length=130, blank=True, null=True)
    op_siglas = models.CharField(max_length=50, blank=True, null=True)
    op_lista = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgpoliticas'


class Parroquias(models.Model):
    provincia_codigo = models.ForeignKey('Provincias', db_column='provincia_codigo', blank=True, null=True)
    provincia_nombre = models.CharField(max_length=40, blank=True, null=True)
    canton_codigo = models.ForeignKey(Cantones, db_column='canton_codigo', blank=True, null=True)
    canton_nombre = models.CharField(max_length=50, blank=True, null=True)
    parroquia_codigo = models.IntegerField(primary_key=True)
    parroquia_nombre = models.CharField(max_length=40, blank=True, null=True)
    parroquia_estado = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parroquias'


class Provincias(models.Model):
    provincia_codigo = models.IntegerField(primary_key=True)
    provincia_nombre = models.CharField(max_length=40, blank=True, null=True)
    provincia_latitud = models.CharField(max_length=20, blank=True, null=True)
    provincia_longitud = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincias'


class Regelectorales(models.Model):
    provincia_codigo = models.ForeignKey(Provincias, db_column='provincia_codigo', blank=True, null=True)
    canton_codigo = models.ForeignKey(Cantones, db_column='canton_codigo', blank=True, null=True)
    parroquia_codigo = models.ForeignKey(Parroquias, db_column='parroquia_codigo', blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    grandes_grupos_de_edad = models.IntegerField(blank=True, null=True)
    electores = models.IntegerField(blank=True, null=True)
    regelectoral_codigo = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'regelectorales'


class Resultados(models.Model):
    dignidad_codigo = models.ForeignKey(Dignidades, db_column='dignidad_codigo', blank=True, null=True)
    provincia_codigo = models.ForeignKey(Provincias, db_column='provincia_codigo', blank=True, null=True)
    circunscripcion_codigo = models.IntegerField(blank=True, null=True)
    canton_codigo = models.ForeignKey(Cantones, db_column='canton_codigo', blank=True, null=True)
    parroquia_codigo = models.ForeignKey(Parroquias, db_column='parroquia_codigo', blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    numero_de_actas = models.IntegerField(blank=True, null=True)
    votos_en_blanco = models.IntegerField(blank=True, null=True)
    votos_nulos = models.IntegerField(blank=True, null=True)
    op_codigo = models.ForeignKey(Orgpoliticas, db_column='op_codigo', blank=True, null=True)
    candidato_codigo = models.ForeignKey(Candidatos, db_column='candidato_codigo', blank=True, null=True)
    candidato_votos = models.IntegerField(blank=True, null=True)
    candidato_estado = models.IntegerField(blank=True, null=True)
    resultado_codigo = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'resultados'
