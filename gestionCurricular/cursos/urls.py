#cursos/urls.py
from django.conf.urls import url
from cursos import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'cursos/',views.HomeCursosView.as_view(),name="cursos"),
]
