from django.test import TestCase
from .models import RegistroFuncionarioForm,RegistroPacienteForm
# Create your tests here.

class RegistroFuncionarioFormTestCase(TestCase):
	def setUp(self):
		self.username = "falvarez"
		self.first_name = "francisco"
		self.last_name = "alvarez"
		self.email = "f.alvarezcorrea1@gmail.com"
		self.password = 1235
		self.RegistroFuncionarioForm = RegistroFuncionarioForm(username=self.username,first_name=self.first_name,last_name=self.last_name,email=self.email,password=self.password)


	def test_RegistroFuncionarioForm(self):
		old_count =RegistroFuncionarioForm.objects.count()
		self.RegistroFuncionarioForm.save()
		new_count=RegistroFuncionarioForm.objects.count()
		self.assertNotEqual(old_count,new_count)

class RegistroPacienteFormTestCase(TestCase):
	def setUp(self):
		self.username = "jperez"
		self.first_name = "Juan"
		self.last_name = "Perez"
		self.email = "Jperez@hotmail.com"
		self.password = 12345
		self.RegistroPacienteForm = RegistroPacienteForm(username=self.username,first_name=self.first_name,last_name=self.last_name,email=self.email,password=self.password)
	
	def test_RegistroPacienteForm(self):
		old_count =RegistroPacienteForm.objects.count()
		self.RegistroPacienteForm.save()
		new_count=RegistroPacienteForm.objects.count()
		self.assertNotEqual(old_count,new_count)
