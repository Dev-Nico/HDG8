from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Paciente
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class PacienteCreate(LoginRequiredMixin,CreateView):
	model= Paciente
	template_name='./paciente_form.html'
	fields='__all__'

class PacienteUpdate(LoginRequiredMixin,UpdateView):
	model=Paciente
	template_name='./paciente_form.html'
	fields='__all__'

class PacienteDelete(LoginRequiredMixin,DeleteView):
	model=Paciente
	template_name='./paciente_confirm_delete.html'
	success_url=reverse_lazy('pacientes')

class HomePageView(TemplateView):

	def get(self, request, **kwargs):
		return render(request,'index.html', context=None)

class HomePacientesView(PermissionRequiredMixin,LoginRequiredMixin,TemplateView):
	permission_required='puede_buscar_pacientes'
	def get (self,request,**kwargs):
		return render(request,'pacientes.html',{'pacientes':Paciente.pacientes.all()})

class DetallePacienteView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		rut=kwargs["rut"]
		return render(request,'paciente.html',{'paciente':Paciente.pacientes.get(rut=rut)})