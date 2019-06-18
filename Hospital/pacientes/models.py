from django.db import models

class Paciente(models.Model):
	primer_nombre=models.CharField(max_length=60)
	segundo_nombre=models.CharField(max_length=60)
	apellido_paterno=models.CharField(max_length=60)
	apellido_materno=models.CharField(max_length=60)
	rut=models.CharField(max_length=30)
	domicilio=models.CharField(max_length=100)
	fecha_nacimiento=models.DateField(auto_now=False)
	pacientes=models.Manager()

	def __str__(self):
		return "{}".format(self.rut)
