from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from core.views import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms

from .forms import FuncionarioForm, PacienteForm
from .models import RegistroFuncionarioForm, RegistroPacienteForm
from core.models import Datos_Personales, Usuario 

# Create your views here.
class UsuariosPageView(staff_member_required,TemplateView):
    template_name = "registration/usuarios.html"
    

class RegistroFuncionarioView(staff_member_required,CreateView):
    model = Datos_Personales
    form_class = FuncionarioForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('usuarios')

class RegistroPacienteView(staff_member_required,CreateView):
    model = RegistroPacienteForm
    form_class = PacienteForm
    template_name = 'registration/registroPaciente.html'
    success_url = reverse_lazy('usuarios')


        
    