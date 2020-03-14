from django.db import models
from django.utils.timezone import now

# Create your models here.

class Datos_Personales(models.Model):
    Primer_Nombre = models.CharField(max_length=45)
    Segundo_Nombre = models.CharField(max_length=45)
    Apellido_Paterno = models.CharField(max_length=45)
    Apellido_Materno = models.CharField(max_length=45)
    Domicilio = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=15)
    Rut = models.CharField(max_length=10)
    Nacionalidad = models.CharField(max_length=20)
    Fecha_Nacimiento = models.DateField()
    Comuna = models.CharField(max_length=20)
#     Region = models.CharField(max_length=20)
# DELETE FROM hospitaldb.core_datos_personales WHERE id<100;
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (1, 'Tony', '', 'Stark', '', 'Los Sauces 12570, El Bosque, Región Metropolitana', '+56911111111', '11111111k', 'Chileno', '2000-01-01', 'El Bosque');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (2, 'Steve', '', 'Rogers', '', 'Lo Blanco 165, San Bernardo, Región Metropolitana', '+56922222222', '22222222k', 'Chileno', '2000-01-01', 'San Bernardo');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (3, 'Bruce', '', 'Banner', '', 'Yumbel 11989, 11989, El Bosque, Región Metropolitana', '+56933333333', '33333333k', 'Chileno', '2000-01-01', 'El Bosque');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (4, 'Clark', '', 'Kent', '', 'Juan de Sandoval 312, San Bernardo, Región Metropolitana', '+56944444444', '44444444k', 'Chileno', '2000-01-01', 'San Bernardo');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (5, 'Bruce', '', 'Wayne', '', 'Max Jara 378, El Bosque, Región Metropolitana', '+56955555555', '55555555k', 'Chileno', '2000-01-01', 'El Bosque');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (6, 'Peter', '', 'Parker', '', 'Las Perdices 607, El Bosque, Región Metropolitana', '+56966666666', '66666666k', 'Chileno', '2000-01-01', 'El Bosque');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (7, 'Stephen', '', 'Strange', '', 'Las Esquilas 1590, El Bosque, Región Metropolitana', '+56977777777', '77777777k', 'Chileno', '2000-01-01', 'El Bosque');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (8, 'Scot', '', 'Lang', '', 'Las Vertientes 11567, El Bosque, Región Metropolitana', '+56988888888', '88888888k', 'Chileno', '2000-01-01', 'El Bosque');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (9, 'Natasha', '', 'Romanova', '', 'Calle Todos Los Santos 1254, San Bernardo, Región Metropolitana', '+56999999999', '99999999k', 'Chileno', '2000-01-01', 'San Bernardo');
# INSERT INTO hospitaldb.core_datos_personales (id, Primer_Nombre, Segundo_Nombre, Apellido_Paterno, Apellido_Materno, Domicilio, Telefono, Rut, Nacionalidad, Fecha_Nacimiento, Comuna) VALUES (10, 'I', 'Am', 'Groot', '', 'Lago Ranco 401, San Bernardo, Región Metropolitana', '+56900000000', '00000000k', 'Chileno', '2000-01-01', 'San Bernardo');
# SELECT * FROM hospitaldb.core_datos_personales;

class Coordenada(models.Model):
    idDatos_Personales = models.ForeignKey(Datos_Personales, on_delete=models.CASCADE)
    Latitud = models.DecimalField(max_digits=9, decimal_places=6)
    Longitud = models.DecimalField(max_digits=9, decimal_places=6)
# DELETE FROM hospitaldb.core_coordenada WHERE id<100;
# SELECT * FROM hospitaldb.core_coordenada;


class Usuario(models.Model):
    idDatos = models.ForeignKey(Datos_Personales, on_delete=models.CASCADE)
    Username = models.CharField(max_length=20)
    Contraseña = models.CharField(max_length=20)
    Tipo_Usuario = models.IntegerField()
    Mail = models.CharField(max_length=45)
# DELETE FROM hospitaldb.core_usuario WHERE id<100;
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (1, 'Tony', 'Hola.1234', '1', 'Avengers@Assemble.dc', 1);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (2, 'Steve', 'Hola.1234', '1', 'Avengers@Assemble.dc', 2);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (3, 'Bruce', 'Hola.1234', '1', 'Avengers@Assemble.dc', 3);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (4, 'Clark', 'Hola.1234', '1', 'Avengers@Assemble.dc', 4);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (5, 'Bruce', 'Hola.1234', '1', 'Avengers@Assemble.dc', 5);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (6, 'Peter', 'Hola.1234', '1', 'Avengers@Assemble.dc', 6);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (7, 'Stephen', 'Hola.1234', '1', 'Avengers@Assemble.dc', 7);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (8, 'Scot', 'Hola.1234', '1', 'Avengers@Assemble.dc', 8);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (9, 'Natasha', 'Hola.1234', '1', 'Avengers@Assemble.dc', 9);
# INSERT INTO hospitaldb.core_usuario (id, Username, Contraseña, Tipo_Usuario, Mail, idDatos_id) VALUES (10, 'Groot', 'Hola.1234', '1', 'Avengers@Assemble.dc', 10);
# SELECT * FROM hospitaldb.core_usuario;


class Cuidador(models.Model):
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Parentezco = models.CharField(max_length=20)
# DELETE FROM hospitaldb.core_cuidador WHERE id<100;
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (1, 'Tatarabuelo', 1);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (2, 'Tatarabuelo', 2);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (3, 'Tatarabuelo', 3);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (4, 'Tatarabuelo', 4);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (5, 'Tatarabuelo', 5);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (6, 'Tatarabuelo', 6);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (7, 'Tatarabuelo', 7);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (8, 'Tatarabuelo', 8);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (9, 'Tatarabuelo', 9);
# INSERT INTO hospitaldb.core_cuidador (id, Parentezco, IdUsuario_id) VALUES (10, 'Tatarabuelo', 10);
# SELECT * FROM hospitaldb.core_cuidador;

class Paciente(models.Model):
    IdCuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=45)
# DELETE FROM hospitaldb.core_paciente WHERE id<100;
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (1, 'Vivo', 1);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (2, 'Vivo', 2);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (3, 'Vivo', 3);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (4, 'Vivo', 4);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (5, 'Vivo', 5);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (6, 'Vivo', 6);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (7, 'Vivo', 7);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (8, 'Vivo', 8);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (9, 'Vivo', 9);
# INSERT INTO hospitaldb.core_paciente (id, Estado, IdCuidador_id) VALUES (10, 'Vivo', 10);
# SELECT * FROM hospitaldb.core_paciente;

class Ruta(models.Model):
    Hora_Inicio = models.TimeField()
    Hora_Termino = models.TimeField()
    Fecha = models.DateField()
# DELETE FROM hospitaldb.core_ruta WHERE id<100;
# INSERT INTO hospitaldb.core_ruta (id, Hora_Inicio, Hora_Termino, Fecha) VALUES (id, Hora_Inicio, Hora_Termino, Fecha);
# SELECT * FROM hospitaldb.core_ruta;
    
class Visita(models.Model):
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idRuta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    Horario_Visita = models.TimeField()
    Presencia = models.BooleanField(default=False)
    Dia_Visitado = models.DateField(default=now)
    Reporte = models.CharField(max_length=800)
    Fotos_Heridas = models.ImageField(upload_to='media/images/visita',blank=True,null=True)
    Secuencia = models.IntegerField()
# DELETE FROM hospitaldb.core_visita WHERE id<100;
# INSERT INTO hospitaldb.core_visita (id, Horario_Visita, Presencia, Dia_Visitado, Reporte, Fotos_Heridas, Secuencia, idPaciente_id, idRuta_id) VALUES (id, Horario_Visita, Presencia, Dia_Visitado, Reporte, Fotos_Heridas, Secuencia, idPaciente_id, idRuta_id);
# SELECT * FROM hospitaldb.core_visita;

class Calendario(models.Model):
    idCuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    Proxima_Visita = models.DateField()
# DELETE FROM hospitaldb.core_calendario WHERE id<100;
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (1, '2020-01-01', 1);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (2, '2020-01-01', 2);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (3, '2020-01-01', 3);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (4, '2020-01-01', 4);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (5, '2020-01-01', 5);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (6, '2020-01-01', 6);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (7, '2020-01-01', 7);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (8, '2020-01-01', 8);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (9, '2020-01-01', 9);
# INSERT INTO hospitaldb.core_calendario (id, Proxima_Visita, idCuidador_id) VALUES (10, '2020-01-01', 10);
# SELECT * FROM hospitaldb.core_calendario;

class Biblioteca(models.Model):
    ContactoHospital = models.IntegerField()
    Documento_PDF = models.FileField(upload_to='media/files',blank=True,null=True)
# DELETE FROM hospitaldb.core_biblioteca WHERE id<100;
# INSERT INTO hospitaldb.core_biblioteca (id, ContactoHospital, Documento_PDF) VALUES (id, ContactoHospital, Documento_PDF);
# SELECT * FROM hospitaldb.core_biblioteca;

class Equipo(models.Model):
    idRuta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
# DELETE FROM hospitaldb.core_equipo WHERE id<100;
# INSERT INTO hospitaldb.core_equipo (id, idRuta_id, idUsuario_id) VALUES (id, idRuta_id, idUsuario_id);
# SELECT * FROM hospitaldb.core_equipo;

class Ficha_Medica(models.Model):
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Foto_Avance_Medico = models.ImageField(upload_to='media/images/ficha-medica',blank=True,null=True)
    Historia = models.CharField(max_length=200)
    Insumo = models.CharField(max_length=45)
    Cant_Insumo = models.IntegerField()
# DELETE FROM hospitaldb.core_ficha_medica WHERE id<100;
# INSERT INTO hospitaldb.core_ficha_medica (id, Foto_Avance_Medico, Historia, Insumo, Cant_Insumo, idPaciente_id) VALUES (id, Foto_Avance_Medico, Historia, Insumo, Cant_Insumo, idPaciente_id);
# SELECT * FROM hospitaldb.core_ficha_medica;


