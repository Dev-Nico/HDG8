from django.contrib import admin
from django.urls import path, include
from .views import ReportesPageView, ReportePageView


urlpatterns = [
    path('', ReportesPageView.as_view(),name='reportes'),
    path('reporte/',ReportePageView.as_view(),name='reporte'),
]
