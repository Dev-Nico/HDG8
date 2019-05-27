from django.db import models

class Curso:
	def __init__(self,sigla,nombre):
		self.sigla=sigla
		self.nombre=nombre

class CursoFactory:
	def __init__(self):
		self.cursos=[]
		self.cursos.append(Curso("ICF232","Ingenieriade Software I"))
		self.cursos.append(Curso("ICF121","Introduccion a la Ingenieria Civil Informatica"))

	def obtenerCursos(self):
		return self.cursos
