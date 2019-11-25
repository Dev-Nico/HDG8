"""from django import forms
from .models import ReporteFuncionario

class ReporteFuncionarioForm(forms.ModelForm):
	class Meta:
		model = ReporteFuncionario
		fields = ('Reporte',)

"""
from django import forms

from django.contrib.auth.forms import UserCreationForm
from core.models import Datos_Personales, Usuario
from .models import ReporteFuncionario

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = Datos_Personales
        fields = ['Primer_Nombre','Segundo_Nombre','Apellido_Paterno','Apellido_Materno','Domicilio',
        'Telefono','Rut','Nacionalidad','Fecha_Nacimiento','Comuna']


class RegistroUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['idDatos','Username','Contraseña','Tipo_Usuario','Mail']

class ReporteFuncionarioForm(forms.ModelForm):

	class Meta:
		model = ReporteFuncionario
		fields = ['Reporte']
	Reporte = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','class':'form-control','id':'report-form'}),label='')