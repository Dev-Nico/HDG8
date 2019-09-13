from django.db import models

# Create your models here.


class RegistroFuncionarioForm(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    password = models.IntegerField(null=True,blank=True)


class RegistroPacienteForm(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    password = models.IntegerField(null=True,blank=True)

