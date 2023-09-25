from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from myApp.forms import *

# Create your views here.

# Vistas
def home_page(request):
    return render(request, 'myApp/home.html')

def views_pokemon(request):
    all_pokemons = Pokemon.objects.all()
    if request.method == 'POST':
        
        pokeform = PokemonForm(request.POST)
        
        if pokeform.is_valid():
            info = pokeform.cleaned_data
            print(f'This is form info {info}')
            pokemon = Pokemon(name=info["name"], type=info["type"], attack=info["attack"])
            pokemon.save()
            return render(request, 'myApp/pokemon.html', {'all_pokemons': all_pokemons, 'pokeform': pokeform })
    else:
        pokeform = PokemonForm()
    return render(request, 'myApp/pokemon.html', {'all_pokemons': all_pokemons, 'pokeform': pokeform })

def views_master(request):
    all_masters = Master.objects.all()
    if request.method == 'POST':
        
        masterform = MasterForm(request.POST)
        if masterform.is_valid():
            info = masterform.cleaned_data
            master = Master(name=info['name'], lastname=info['lastname'], favorite_type=info['favorite_type'])
            master.save()
            return render(request, 'myApp/master.html', {'all_masters': all_masters, 'masterform': masterform})
    else:
        masterform = MasterForm()
    return render(request, 'myApp/master.html', {'all_masters': all_masters, 'masterform': masterform})

def views_gym(request):
    all_gyms = Gym.objects.all()
    if request.method == 'POST':
        gymform = GymForm(request.POST)
        if gymform.is_valid():
            info = gymform.cleaned_data
            gym = Gym(name=info['name'], type=info['type'], master=info['master'])
            gym.save()
            return render(request, 'myApp/gym.html', {'all_gyms': all_gyms, 'gymform': gymform })
    else:
        gymform = GymForm()
    return render(request, 'myApp/gym.html', {'all_gyms': all_gyms, 'gymform': gymform })

# Vista de Busquedas
def pokemon_search_result(request):
    if request.GET['pokemon']:
        name = request.GET['pokemon']
        pokemon = Pokemon.objects.filter(name__icontains=name)
        return render(request, 'myApp/search_pokemon.html', { 'name': name, 'pokemon': pokemon})
    else:
        advice = f'No se enviaron datos!'
        
    return HttpResponse(advice)

# Vistas de Delete
def delete_pokemon(request, pokemon):
    result = f'You Click me to delete {pokemon}'
    # if request.method == 'DELETE':
    
    return HttpResponse(result)

def delete_master(request):
    pass

def delete_gym(request):
    pass


