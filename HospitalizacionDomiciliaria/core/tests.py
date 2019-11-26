from django.test import TestCase

from .models import *
# Create your tests here.

class Datos_PersonalesTestCase(TestCase):
	def setUp(self):
		self.Primer_Nombre = "francisco"
		self.Segundo_Nombre = "andres"
		self.Apellido_Paterno = "alvarez"
		self.Apellido_Materno = "correa"
		self.Domicilio = "psje. prueba 2453"
		self.Telefono = "90747224"
		self.Rut = "19078222"
		self.Nacionalidad = "Chilena"
		self.Fecha_Nacimiento = "1995-04-06"
		self.Comuna = "Puente Alto"
		self.Datos_Personales = Datos_Personales(Primer_Nombre=self.Primer_Nombre,Segundo_Nombre=self.Segundo_Nombre,Apellido_Paterno=self.Apellido_Paterno,Apellido_Materno=self.Apellido_Materno,Domicilio=self.Domicilio,Telefono=self.Telefono,Rut=self.Rut,Nacionalidad=self.Nacionalidad,Fecha_Nacimiento=self.Fecha_Nacimiento,Comuna=self.Comuna)


	def test_Datos_Personales(self):
		old_count =Datos_Personales.objects.count()
		self.Datos_Personales.save()
		new_count=Datos_Personales.objects.count()
		self.assertNotEqual(old_count,new_count)

class UsuarioTestCase(TestCase):
	def setUp(self):
		self.idDatos = Datos_Personales.objects.get(Primer_Nombre=="francisco").id
		self.Username = "juanito"
		self.Contraseña = "juanito123"
		self.Tipo_Usuario = 2
		self.Mail ="juanito@gmail.com"
		self.Usuario = Usuario(idDatos=self.idDatos,Username=self.Username,Contraseña=self.Contraseña,Tipo_Usuario=self.Tipo_Usuario,Mail=self.Mail)
	
	def test_Usuario(self):
		old_count =Usuario.objects.count()
		self.Usuario.save()
		new_count=Usuario.objects.count()
		self.assertNotEqual(old_count,new_count)

class CuidadorTestCase(TestCase):
	def setUp(self):
		self.idUsuario = 1
		self.Parentezco = "Sobrino"
		self.Cuidador = Cuidador(idUsuario=self.idUsuario,Parentezco=self.Parentezco)

	def Test_Cuidador(self):
		old_count =Cuidador.objects.count()
		self.Cuidador.save()
		new_count=Cuidador.objects.count()
		self.assertNotEqual(old_count,new_count)

class PacienteTestCase(TestCase):
	def setUp(self):
		self.idCuidador = 1
		self.Estado = "Medio"
		self.Paciente=Paciente(idCuidador=self.idCuidador,Estado=self.Estado)

	def Test_Paciente(self):
		old_count =Paciente.objects.count()
		self.Paciente.save()
		new_count=Paciente.objects.count()
		self.assertNotEqual(old_count,new_count)

class RutaTestCase(TestCase):
	def setUp(self):
		self.Hora_Inicio = "10:45"
		self.Hora_Termino = "11:25"
		self.Fecha = "2019-11-25"
		self.Ruta=Ruta(Hora_Inicio=self.Hora_Inicio,Hora_Termino=self.Hora_Termino,Fecha=self.Fecha)

	def Test_Ruta(self):
		old_count =Ruta.objects.count()
		self.Ruta.save()
		new_count=Ruta.objects.count()
		self.assertNotEqual(old_count,new_count)

class VisitaTestCase(TestCase):
	def setUp(self):
		self.idPaciente = 1
		self.idRuta = 1
		self.Horario_Visita = "10:25"
		self.Presencia = True
		self.Dia_Visitado = "2019-11-25"
		self.Reporte = "Paciente presenta altos niveles de alcohol en la sangre"
		self.Secuencia = 3
		self.Visita=Visita(idPaciente=self.idPaciente,idRuta=self.idRuta,Horario_Visita=self.Horario_Visita,Presencia=self.Presencia,Dia_Visitado=self.Dia_Visitado,Reporte=self.Reporte,Secuencia=self.Secuencia)

	def Test_Visita(self):
		old_count =Visita.objects.count()
		self.Visita.save()
		new_count=Visita.objects.count()
		self.assertNotEqual(old_count,new_count)

class CalendarioTestCase(TestCase):
	def setUp(self):
		self.idCuidador = 1
		self.Proxima_Visita = "2019-11-30"
		self.Calendario=Calendario(idCuidador=self.idCuidador,Proxima_Visita=self.Proxima_Visita)

	def Test_Calendario(self):
		old_count =Calendario.objects.count()
		self.Calendario.save()
		new_count=Calendario.objects.count()
		self.assertNotEqual(old_count,new_count)

class BibliotecaTestCase(TestCase):
	def setUp(self):
		self.ContactoHospital = 2541589
		self.Biblioteca=Biblioteca(ContactoHospital=self.ContactoHospital)

	def Test_Biblioteca(self):
		old_count =Biblioteca.objects.count()
		self.Biblioteca.save()
		new_count=Biblioteca.objects.count()
		self.assertNotEqual(old_count,new_count)

class EquipoTestCase(TestCase):
	def setUp(self):
		self.idRuta = 1
		self.idUsuario = 1
		self.Equipo=Equipo(idRuta=self.idRuta,idUsuario=self.idUsuario)

	def Test_Equipo(self):
		old_count =Equipo.objects.count()
		self.Equipo.save()
		new_count=Equipo.objects.count()
		self.assertNotEqual(old_count,new_count)

class Ficha_MedicaTestCase(TestCase):
	def setUp(self):
		self.idPaciente = 1
		self.Historia = "blablabla"
		self.Insumo = "papas fritas"
		self.Cant_Insumo = 2000
		self.Ficha_Medica=Ficha_Medica(idPaciente=self.idPaciente,Historia=self.Historia,Insumo=self.Insumo,Cant_Insumo=self.Cant_Insumo)

	def Test_Ficha_Medica(self):
		old_count =Ficha_Medica.objects.count()
		self.Ficha_Medica.save()
		new_count=Ficha_Medica.objects.count()
		self.assertNotEqual(old_count,new_count)