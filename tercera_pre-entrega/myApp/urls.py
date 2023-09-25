from django.urls import path
from myApp import views

urlpatterns = [
    
    # URLs de Vistas
    path('', views.home_page, name='Home'),
    path('pokemon/', views.views_pokemon, name='Pokemon'),
    path('master/', views.views_master, name='Master'),
    path('gym/', views.views_gym, name='Gym'),
        
    # URLs de Búsqueda
    path('pokemon_search/', views.pokemon_search_result),
    
    # URLs de Delete
    path('pokemon/<pokemon>', views.delete_pokemon, name='DeletePokemon'),
]