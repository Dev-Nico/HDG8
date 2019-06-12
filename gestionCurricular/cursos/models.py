from django.db import models

# Create your models here.

class Curso(models.Model):
		sigla=models.CharField(max_length=6)
		nombre=models.CharField(max_length=60)
		creditos=models.IntegerField()
		nrc=models.IntegerField(null=True)
		cursos=models.Manager()

		def __str__(self):
			return "{}".format(self.nombre)

class CursoFactory:
	def __init__(self):
		self.cursos=[]
		self.cursos.append(Curso("ICF232","Ingeniería de Software I",6))
		self.cursos.append(Curso("ICF121","Introducción a la Ingeniería Civil Informática",6))
		#self.cursos.append(Curso("MAT021","Calculo Diferencial",6,2656))
		#self.cursos.append(Curso("MAT011","Introducción a las Matemáticas",6,2643))
		#self.cursos.append(Curso("MAT021","Calculo Diferencial",6,2554))

	def obtenerCursos(self):
		return self.cursos
		
	def getCurso(self,sigla):
		for curso in self.cursos:
			if curso.sigla==sigla:
				return curso
		return None