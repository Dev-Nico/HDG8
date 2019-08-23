from django import forms
from .models import RegistroFuncionarioForm

from django.contrib.auth.forms import UserCreationForm

class FuncionarioForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField()
    class Meta:
        model = RegistroFuncionarioForm
        fields = ['username','first_name','last_name','email','password']
