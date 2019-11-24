from .views import UsuariosPageView, RegistroFuncionarioView,RegistroPacienteView


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', UsuariosPageView.as_view(),name='usuarios'),
    path('registroFuncionario/', RegistroFuncionarioView.as_view(),name='registroFuncionario'),
    path('registroPaciente/', RegistroPacienteView.as_view(),name='registroPaciente'),
]
