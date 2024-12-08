from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_registros, name='lista_registros'),
    path('agregar/', views.agregar_registro, name='agregar_registro'),
    path('editar/<int:id>/', views.editar_registro, name='editar_registro'),
    path('eliminar/<int:id>/', views.eliminar_registro, name='eliminar_registro'),
]
