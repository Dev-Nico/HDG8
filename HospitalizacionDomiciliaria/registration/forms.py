from django import forms
from .models import RegistroFuncionarioForm, RegistroPacienteForm

from django.contrib.auth.forms import UserCreationForm
from core.models import Datos_Personales, Usuario

class FuncionarioForm(forms.ModelForm):
    
    class Meta:
        model = Datos_Personales
        fields = ['Primer_Nombre','Segundo_Nombre','Apellido_Paterno','Apellido_Materno','Domicilio',
        'Telefono','Rut','Nacionalidad','Fecha_Nacimiento','Comuna']


class PacienteForm(forms.ModelForm):

    class Meta:
        model = RegistroPacienteForm
        fields = ['username','first_name','last_name','email','password']
