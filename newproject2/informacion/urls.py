from django.urls import path
from informacion import views

urlpatterns = [
    path('jugadores/', views.jugadores, name='jugadores'),
    path('', views.index, name='index'),
    path('pelis/', views.pelis, name='pelis'),
    path('futbol/', views.futbol, name='futbol'),
  
]