from django.db import models

# Create your models here.

# class Datos_Personales(models.Model):
#     Primer_Nombre = models.CharField(max_length=45)
#     Segundo_Nombre = models.CharField(max_length=45)
#     Apellido_Paterno = models.CharField(max_length=45)
#     Apellido_Materno = models.CharField(max_length=45)
#     Domicilio = models.CharField(max_length=100)
#     Telefono = models.CharField(max_length=15)
#     Rut = models.CharField(max_length=10)
#     Nacionalidad = models.CharField(max_length=20)
#     Fecha_Nacimiento = models.DateField()
#     Comuna = models.CharField(max_length=20)
#     Region = models.CharField(max_length=20)

# class Usuario(models.Model):
#     idDatos = models.ForeignKey(Datos_Personales, on_delete=models.CASCADE)
#     Username = models.CharField(max_length=20)
#     Contraseña = models.CharField(max_length=20)
#     Tipo_Usuario = models.CharField(max_length=45)
#     Mail = models.CharField(max_length=45)
#     #Cargo = models.CharField(max_length=45)
#     Tipo = (
#         (0, 'Cuidador'),
#         (1, 'Funcionario'),
#         (2, 'Admin'),
#     )

# class Cuidador(models.Model):
#     IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     Familiaridad = models.CharField(max_length=200)

# class Paciente(models.Model):
#     IdCuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
#     Estado = models.CharField(max_length=45)

# class Ruta(models.Model):
#     Hora_Inicio = models.DateField()
#     Hora_Termino = models.DateField()
#     Fecha = models.DateField()
    
# class Visita(models.Model):
#     idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#     idRuta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
#     Horario_Visita = models.DateField()
#     Presencia = models.BooleanField(default=False)
#     Dia_Visitado = models.DateField()
#     Reporte = models.CharField(max_length=800)
#     Fotos_Heridas = models.ImageField(upload_to='media/images/visita')
#     Secuencia = models.IntegerField()

# class Calendario(models.Model):
#     IdPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#     Proxima_Visita = models.DateField()

# class Biblioteca(models.Model):
#     ContactoHospital = models.IntegerField()
#     Documento_PDF = models.FileField(upload_to='media/files')

# class Equipo(models.Model):
#     IdRuta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
#     IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# class Ficha_Medica(models.Model):
#     idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#     Foto_Avance_Medico = models.ImageField(upload_to='media/images/ficha-medica')
#     Historia = models.CharField(max_length=200)
#     Insumo = models.CharField(max_length=45)
#     Cant_Insumo = models.IntegerField()



