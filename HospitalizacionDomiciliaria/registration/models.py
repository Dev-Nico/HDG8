from django.db import models

# Create your models here.


class RegistroFuncionarioForm(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)