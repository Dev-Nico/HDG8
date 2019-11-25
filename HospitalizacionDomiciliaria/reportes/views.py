from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from core.views import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms

from .forms import DatosPersonalesForm, RegistroUsuarioForm, ReporteFuncionarioForm
from core.models import Datos_Personales, Usuario 
from .models import ReporteFuncionario

# Create your views here.
class ReportesPageView(staff_member_required,TemplateView):
    template_name = "reportes/reportes.html"
    

class RegistroPageView(staff_member_required,CreateView):
    model = Datos_Personales
    form_class = DatosPersonalesForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('usuarios')

class RegistroUsuarioView(staff_member_required,CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'registration/registroPaciente.html'
    success_url = reverse_lazy('usuarios')

class ReportePageView(staff_member_required,CreateView):
	model = ReporteFuncionario
	form_class = ReporteFuncionarioForm
	template_name = 'reportes/reporte.html'
	success_url = reverse_lazy('reportes')