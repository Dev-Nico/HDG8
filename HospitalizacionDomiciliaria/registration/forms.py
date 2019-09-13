from django import forms
from .models import RegistroFuncionarioForm, RegistroPacienteForm

from django.contrib.auth.forms import UserCreationForm

class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = RegistroFuncionarioForm
        fields = ['username','first_name','last_name','email','password']


class PacienteForm(forms.ModelForm):

    class Meta:
        model = RegistroPacienteForm
        fields = ['username','first_name','last_name','email','password']
