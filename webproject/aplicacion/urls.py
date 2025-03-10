from django.urls import path
from aplicacion import views

urlpatterns = [
  
    path('', views.index, name='index'),
    path('viernes/', views.metodoviernes, name='viernes'),
    path('listas/', views.metodolistas, name='listas'),
    path('peliculas/', views.metodopeliculas, name='peliculas'),
    ]