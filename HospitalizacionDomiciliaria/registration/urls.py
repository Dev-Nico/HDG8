from .views import UsuariosPageView, DatosPersonalesView,RegistroUsuarioView


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', UsuariosPageView.as_view(),name='usuarios'),
    path('registroDatosPersonales/', DatosPersonalesView.as_view(),name='registroDatosPersonales'),
    path('registroUsuario/', RegistroUsuarioView.as_view(),name='registroUsuario'),
]
