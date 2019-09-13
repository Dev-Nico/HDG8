from django.test import TestCase
from .models import ReporteFuncionario
# Create your tests here.

class ReporteFuncionarioTestCase(TestCase):
	def setUp(self):
		self.Reporte = "Este es un reporte de prueba"
		self.ReporteFuncionario = ReporteFuncionario(Reporte=self.Reporte)


	def test_ReporteFuncionarioForm(self):
		old_count =ReporteFuncionario.objects.count()
		self.ReporteFuncionario.save()
		new_count=ReporteFuncionario.objects.count()
		self.assertNotEqual(old_count,new_count)