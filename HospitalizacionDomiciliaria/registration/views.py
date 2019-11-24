from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from core.views import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms

from .forms import DatosPersonalesForm, RegistroUsuarioForm
from core.models import Datos_Personales, Usuario 

# Create your views here.
class UsuariosPageView(staff_member_required,TemplateView):
    template_name = "registration/usuarios.html"
    

class DatosPersonalesView(staff_member_required,CreateView):
    model = Datos_Personales
    form_class = DatosPersonalesForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('usuarios')

class RegistroUsuarioView(staff_member_required,CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'registration/registroPaciente.html'
    success_url = reverse_lazy('usuarios')


        
    