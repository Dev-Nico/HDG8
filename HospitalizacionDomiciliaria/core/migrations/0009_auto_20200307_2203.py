# Generated by Django 2.2.1 on 2020-03-08 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200223_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordenada',
            name='Latitud',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='coordenada',
            name='Longitud',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
