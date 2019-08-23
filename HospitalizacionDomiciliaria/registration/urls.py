from .views import UsuariosPageView, RegistroView


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', UsuariosPageView.as_view(),name='usuarios'),
    path('registro/', RegistroView.as_view(),name='registro'),
]
