from django.shortcuts import render
from django.views.generic.base import TemplateView
from core.views import staff_member_required

from core.models import Ruta, Equipo, Usuario, Datos_Personales

# Create your views here.
class RutasPageView(staff_member_required,TemplateView):
    model = Ruta, Equipo, Usuario, Datos_Personales
    template_name = "./ruta.html"
    def get(self, request):
        Rutas = Ruta.objects.all()
        Equipos = Equipo.objects.all()
        Usuarios = Usuario.objects.all()
        Datos = Datos_Personales.objects.all()
        args = {
           'Rutas': Rutas, 'Equipos': Equipos, 'Usuarios': Usuarios, 'Datos': Datos
        }
        return render(request, self.template_name, args)

    def RutasPageView_view(request):
        return render(request, "/ruta.html")





