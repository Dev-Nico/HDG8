from django.views.generic.base import TemplateView
#mixin de identificacion
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.shortcuts import redirect

#mixin de identificaicon
class staff_member_required(object):

    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        return super(staff_member_required,self).dispatch(request,*args,**kwargs)
            

# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"