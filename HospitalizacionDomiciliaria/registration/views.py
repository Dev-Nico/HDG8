from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from core.views import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms

from .forms import FuncionarioForm
from .models import RegistroFuncionarioForm

# Create your views here.
class UsuariosPageView(staff_member_required,TemplateView):
    template_name = "registration/usuarios.html"
    

class RegistroView(staff_member_required,CreateView):
    model = RegistroFuncionarioForm
    form_class = FuncionarioForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('usuarios')


        
    