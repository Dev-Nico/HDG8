from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Curso,CursoFactory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CursoCreate(CreateView):
	model = Curso
	template_name='./curso_form.html'
	fields = '__all__'

class CursoUpdate(UpdateView):
	model = Curso
	template_name='./curso_form.html'
	fields=['sigla','nombre','creditos','NRC']

class CursoDelete(DeleteView):
	model=Curso
	template_name='./curso_confirm_delete.html'
	success_url=reverse_lazy('cursos')

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

class HomeCursosView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):

	permission_required='puede_buscar_cursos'
	def get(self, request, **kwargs):
		#return render(request,'cursos.html',{'cursos':cursoFactory.obtenerCursos()})
		
		return render(request, 'cursos.html',{'cursos':Curso.cursos.all()})

class HomeNRCView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
	permission_required='puede_buscar_cursos'
	def get(self,request,**kwargs):
		return render(request,'NRC.html',{'cursos':Curso.cursos.all()})

class DetalleCursoView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):

	permission_required='puede_buscar_cursos'
	def get(self, request, **kwargs):
		sigla=kwargs["sigla"]
		return render(request,'curso.html',{'curso':Curso.cursos.get(sigla=sigla)})