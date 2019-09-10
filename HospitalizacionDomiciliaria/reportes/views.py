from django.shortcuts import render
from django.views.generic.base import TemplateView
from core.views import staff_member_required

# Create your views here.
class ReportesPageView(staff_member_required,TemplateView):
    template_name = "reportes/reportes.html"