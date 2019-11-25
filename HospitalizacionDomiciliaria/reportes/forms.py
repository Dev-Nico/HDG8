"""from django import forms
from .models import ReporteFuncionario

class ReporteFuncionarioForm(forms.ModelForm):
	class Meta:
		model = ReporteFuncionario
		fields = ('Reporte',)

"""
from django import forms

from django.contrib.auth.forms import UserCreationForm
from core.models import Visita

class ReporteFuncionarioForm(forms.ModelForm):

	class Meta:
		model = Visita
		fields = ['idPaciente','idRuta','Horario_Visita','Presencia','Dia_Visitado','Fotos_Heridas','Secuencia','Reporte']
	Reporte = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','class':'form-control','id':'report-form'}),label='')
	Horario_Visita = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))