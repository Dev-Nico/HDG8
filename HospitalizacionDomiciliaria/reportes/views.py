from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from core.views import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms

from .forms import ReporteFuncionarioForm
from core.models import Datos_Personales, Usuario, Visita

# Create your views here.
class ReportesPageView(staff_member_required,TemplateView):
    template_name = "reportes/reportes.html"


class ReportePageView(staff_member_required,CreateView):
	model = Visita
	form_class = ReporteFuncionarioForm
	template_name = 'reportes/reporte.html'
	success_url = reverse_lazy('reportes')