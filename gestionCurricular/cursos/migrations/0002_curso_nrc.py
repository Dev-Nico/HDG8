# Generated by Django 2.2.1 on 2019-06-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nrc',
            field=models.IntegerField(null=True),
        ),
    ]
