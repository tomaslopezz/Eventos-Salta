from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.listar_servicios, name='listar-servicios'),
    path('servicios/<int:id>', views.obtener_servicio, name='obtener-servicio'),
    path('clientes/', views.listar_clientes, name='listar-clientes'),
    path('coordinadores/', views.listar_coordinadores, name='listar-coordinadores'),
    path('empleados/', views.listar_empleados, name='listar-empleados')
]
