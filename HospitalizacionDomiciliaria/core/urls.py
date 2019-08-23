from .views import HomePageView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
]
