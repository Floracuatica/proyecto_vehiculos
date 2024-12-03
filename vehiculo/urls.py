from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('list/', views.listar_vehiculos, name='listar_vehiculos'),
]
