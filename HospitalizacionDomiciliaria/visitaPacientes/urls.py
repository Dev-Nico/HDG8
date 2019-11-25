from django.contrib import admin
from django.urls import path, include
from .views import VisitaPacientePageView


urlpatterns = [
    path('', VisitaPacientePageView.as_view() ,name='visitaPacientes'),
]