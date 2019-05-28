from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Curso,CursoFactory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class PermissionRequiredInGroupMixin(PermissionRequiredMixin):
	def has_permission(self):
		usuario=self.request.user
		permisos=self.get_permission_required()
		privilegios=[]
		for g in usuario.groups.all():
			for p in g.permissions.all():
				privilegios.append(p.codename)
		for r in permisos:
			if r not in privilegios:
				return False
		return True

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request,'index.html', context=None)

class HomeCursosView(PermissionRequiredInGroupMixin, LoginRequiredMixin, TemplateView):
	permission_required='puede_buscar_cursos'
	def get(self, request, **kwargs):
		#cursoFactory=CursoFactory()
		#return render(request,'cursos.html',{'cursos':cursoFactory.obtenerCursos()})
		return render(request, 'cursos.html',{'cursos':Curso.cursos.all()})

class DetalleCursoView(LoginRequiredMixin, TemplateView):
	def get(self, request, **kwargs):
		cursoFactory=CursoFactory()
		sigla=kwargs["sigla"]
		return render(request,'curso.html',{'curso':cursoFactory.getCurso(sigla)})