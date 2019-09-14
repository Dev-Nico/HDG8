from django.db import models

# Create your models here.
class RegistroFuncionarioForm(models.Model):
    idVisit = models.IntegerField(unique = True)
    idPatient = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Visita")
    nextVisit = models.DateField(verbose_name="Proxima Visita")
