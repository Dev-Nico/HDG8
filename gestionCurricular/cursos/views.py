from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Curso, CursoFactory

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'index.html',context=None)

class HomeCursosView(TemplateView):
    def get(self,request,**kwargs):
        cursoFactory=CursoFactory()
        return render(request, 'cursos.html',{'cursos':cursoFactory.obtenerCursos()})
