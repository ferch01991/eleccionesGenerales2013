# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('candidato_codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('candidato_orden', models.IntegerField(null=True, blank=True)),
                ('circunscripcion_codigo', models.IntegerField(null=True, blank=True)),
                ('candidato_nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('candidato_sexo', models.IntegerField(null=True, blank=True)),
                ('candidato_edad_exacta', models.FloatField(null=True, blank=True)),
                ('candidatos_grupos_de_edad', models.IntegerField(null=True, blank=True)),
                ('suplente_nombre1', models.CharField(max_length=50, null=True, blank=True)),
                ('suplente_sexo1', models.IntegerField(null=True, blank=True)),
                ('suplente_edad_exacta1', models.FloatField(null=True, blank=True)),
                ('suplente_grupos_de_edad1', models.IntegerField(null=True, blank=True)),
                ('suplente_nombre2', models.CharField(max_length=50, null=True, blank=True)),
                ('suplente_sexo2', models.IntegerField(null=True, blank=True)),
                ('suplente_edad_exacta2', models.FloatField(null=True, blank=True)),
                ('suplente_grupos_de_edad2', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'candidatos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cantones',
            fields=[
                ('canton_codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('canton_nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('provincia_nombre', models.CharField(max_length=40, null=True, blank=True)),
            ],
            options={
                'db_table': 'cantones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dignidades',
            fields=[
                ('dignidad_codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('dignidad_nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('dignidad_ambito', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'dignidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orgpoliticas',
            fields=[
                ('op_codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('provincia_codigo', models.IntegerField(null=True, blank=True)),
                ('canton_codigo', models.IntegerField(null=True, blank=True)),
                ('parroquia_codigo', models.IntegerField(null=True, blank=True)),
                ('op_tipo', models.CharField(max_length=25, null=True, blank=True)),
                ('op_ambito', models.CharField(max_length=10, null=True, blank=True)),
                ('op_nombre', models.CharField(max_length=130, null=True, blank=True)),
                ('op_siglas', models.CharField(max_length=50, null=True, blank=True)),
                ('op_lista', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'orgpoliticas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parroquias',
            fields=[
                ('provincia_nombre', models.CharField(max_length=40, null=True, blank=True)),
                ('canton_nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('parroquia_codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('parroquia_nombre', models.CharField(max_length=40, null=True, blank=True)),
                ('parroquia_estado', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'parroquias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('provincia_codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('provincia_nombre', models.CharField(max_length=40, null=True, blank=True)),
                ('provincia_latitud', models.CharField(max_length=20, null=True, blank=True)),
                ('provincia_longitud', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regelectorales',
            fields=[
                ('sexo', models.IntegerField(null=True, blank=True)),
                ('grandes_grupos_de_edad', models.IntegerField(null=True, blank=True)),
                ('electores', models.IntegerField(null=True, blank=True)),
                ('regelectoral_codigo', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'regelectorales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('circunscripcion_codigo', models.IntegerField(null=True, blank=True)),
                ('sexo', models.IntegerField(null=True, blank=True)),
                ('numero_de_actas', models.IntegerField(null=True, blank=True)),
                ('votos_en_blanco', models.IntegerField(null=True, blank=True)),
                ('votos_nulos', models.IntegerField(null=True, blank=True)),
                ('candidato_votos', models.IntegerField(null=True, blank=True)),
                ('candidato_estado', models.IntegerField(null=True, blank=True)),
                ('resultado_codigo', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'resultados',
                'managed': False,
            },
        ),
    ]
