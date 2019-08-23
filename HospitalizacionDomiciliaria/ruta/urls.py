from django.contrib import admin
from django.urls import path, include
from .views import RutasPageView


urlpatterns = [
    path('', RutasPageView.as_view(),name='rutas'),
]

