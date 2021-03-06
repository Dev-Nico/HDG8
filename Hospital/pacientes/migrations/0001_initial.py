# Generated by Django 2.2.1 on 2019-06-18 02:34

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=60)),
                ('segundo_nombre', models.CharField(max_length=60)),
                ('apellido_paterno', models.CharField(max_length=60)),
                ('apellido_materno', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
            managers=[
                ('pacientes', django.db.models.manager.Manager()),
            ],
        ),
    ]
