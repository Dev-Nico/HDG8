# Generated by Django 2.2.1 on 2019-06-24 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20190624_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ruta',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pacientes.Ruta'),
        ),
    ]
