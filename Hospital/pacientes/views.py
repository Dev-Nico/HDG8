from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Paciente, Ruta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PacienteCreate(LoginRequiredMixin,CreateView):
	model= Paciente
	template_name='./paciente_form.html'
	fields='__all__'

class PacienteUpdate(LoginRequiredMixin,UpdateView):
	model=Paciente
	template_name='./paciente_form.html'
	fields=('primer_nombre','segundo_nombre','apellido_paterno','apellido_materno','rut','domicilio','fecha_nacimiento',)

class PacienteUpdate2(LoginRequiredMixin,UpdateView):
	model=Paciente
	template_name='./paciente_form2.html'
	fields=('ruta',)


class PacienteDelete(LoginRequiredMixin,DeleteView):
	model=Paciente
	template_name='./paciente_confirm_delete.html'
	success_url=reverse_lazy('pacientes')

class RutaCreate(LoginRequiredMixin,CreateView):
	model= Ruta
	template_name='./ruta_form.html'
	fields='__all__'
"""
class RutaUpdate(LoginRequiredMixin,UpdateView):
	model=Paciente
	template_name='./paciente_form.html'
	fields='__all__'
"""
class RutaDelete(LoginRequiredMixin,DeleteView):
	model=Ruta
	template_name='./ruta_confirm_delete.html'
	success_url=reverse_lazy('rutas')


class HomePageView(TemplateView):

	def get(self, request, **kwargs):
		return render(request,'index.html', context=None)

class HomePacientesView(LoginRequiredMixin,TemplateView):
	def get (self,request,**kwargs):
		return render(request,'pacientes.html',{'pacientes':Paciente.pacientes.all()})

class DetallePacienteView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		rut=kwargs["rut"]
		return render(request,'paciente.html',{'paciente':Paciente.pacientes.get(rut=rut)})

class DetallePacienteView2(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		rut=kwargs["rut"]
		return render(request,'paciente2.html',{'paciente':Paciente.pacientes.get(rut=rut)})

class HomeRutasView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'rutas.html',{'rutas':Ruta.rutas.all()})

class DetalleRutaView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		numero=kwargs["pk"]
		return render(request,'ruta.html',{'ruta':Ruta.rutas.get(pk=numero)})

class PacientesEnRuta(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		ruta=kwargs["pk"]
		return render(request,'pacientesenruta.html',{'pacientes':Paciente.pacientes.filter(ruta=ruta)})