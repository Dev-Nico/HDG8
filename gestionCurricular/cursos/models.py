from django.db import models

# Create your models here.

class Curso:
	def __init__(self,sigla,nombre,creditos):
		self.sigla=sigla
		self.nombre=nombre
		self.creditos=creditos

class CursoFactory:
	def __init__(self):
		self.cursos=[]
		self.cursos.append(Curso("ICF232","Ingeniería de Software I",6))
		self.cursos.append(Curso("ICF121","Introducción a la Ingeniería Civil Informática",6))

	def obtenerCursos(self):
		return self.cursos
		
	def getCurso(self,sigla):
		for curso in self.cursos:
			if curso.sigla==sigla:
				return curso
		return None