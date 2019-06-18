from django.conf.urls import url, re_path
from django.urls import path, include
from pacientes import views

urlpatterns=[
	url(r'^$',views.HomePageView.as_view(),name="index"),
	url(r'pacientes/',views.HomePacientesView.as_view(),name="pacientes"),
	re_path(r'^paciente/(?P<rut>[0-9]{8}[0-9k]{1})/$',views.DetallePacienteView.as_view(), name="detalle"),
	path('accounts/', include('accounts.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
	url(r'^paciente/create/$',views.PacienteCreate.as_view(success_url='/pacientes/'), name='paciente_create'),
	url(r'^paciente/(?P<pk>\d+)/update/$', views.PacienteUpdate.as_view(success_url='/pacientes/'),name='paciente_update'),
	url(r'^paciente/(?P<pk>\d+)/delete/$', views.PacienteDelete.as_view(success_url='/pacientes/'),name='paciente_delete'),
]