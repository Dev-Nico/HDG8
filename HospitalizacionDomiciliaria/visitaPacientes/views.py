# from django.shortcuts import render
# from core.views import staff_member_required
# from django.views.generic.base import TemplateView

# from core.models import Datos_Personales

# Create your views here.
# class VisitaPacientePageView(staff_member_required,TemplateView):
#     model = Datos_Personales
#     template_name = 'visitaPaciente/visitaPaciente.html'
#     def get(self, request):
#         Datos = Datos_Personales.objects.all()
       
#         args = {
#            'Datos': Datos
#         }
#         return render(request, self.template_name, args)

#     def VisitaPacientePageView_view(request):
#         return render(request, "visitaPaciente/visitaPaciente.html")

from django.shortcuts import render
from core.views import staff_member_required
from django.views.generic.base import TemplateView

# Create your views here.
class VisitaPacientePageView(staff_member_required,TemplateView):
    template_name = "visitaPacientes/visitaPaciente.html"

#class RegistroView(staff_member_required,CreateView):
#    model = 
#    form_class = 
#    template_name = 'visitaPacientes/visitaPaciente.html'
#    success_url = reverse_lazy('usuarios')