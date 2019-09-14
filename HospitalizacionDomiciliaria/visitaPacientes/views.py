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
