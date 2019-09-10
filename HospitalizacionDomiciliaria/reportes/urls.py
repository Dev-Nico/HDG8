from django.contrib import admin
from django.urls import path, include
from .views import ReportesPageView


urlpatterns = [
    path('', ReportesPageView.as_view(),name='reportes'),
]
