from django.conf.urls import url, re_path
from django.urls import path, include
from pacientes import views

urlpatterns=[
	url(r'^$',views.HomePageView.as_view(),name="index"),
	url(r'pacientes/',views.HomePacientesView.as_view(),name="pacientes"),
	url(r'rutas/',views.HomeRutasView.as_view(), name='rutas'),
	re_path(r'^paciente/(?P<rut>[0-9]{8}[0-9k]{1})/$',views.DetallePacienteView.as_view(), name="detalle paciente"),
	re_path(r'^ruta/(?P<numero>[0-9]{1})/$',views.DetalleRutaView.as_view(), name="detalle ruta"),
	path('accounts/', include('accounts.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
	url(r'^paciente/create/$',views.PacienteCreate.as_view(success_url='/pacientes/'), name='paciente_create'),
	url(r'^paciente/(?P<pk>\d+)/update/$', views.PacienteUpdate.as_view(success_url='/pacientes/'),name='paciente_update'),
	url(r'^paciente/(?P<pk>\d+)/update2/$', views.PacienteUpdate2.as_view(success_url='/pacientes/'),name='paciente_update2'),
	url(r'^paciente/(?P<pk>\d+)/delete/$', views.PacienteDelete.as_view(success_url='/pacientes/'),name='paciente_delete'),
	url(r'^ruta/create/$',views.RutaCreate.as_view(success_url='/rutas/'), name='ruta_create'),
	url(r'^ruta/(?P<pk>\d+)/delete/$', views.RutaDelete.as_view(success_url='/rutas/'),name='ruta_delete'),
]