
from django.http import HttpResponse
from django.template import loader

from pokedex.forms import PokemonFor
from .models import Pokemon
from django.shortcuts import get_object_or_404, redirect, render

#importacion de librearia de autenticacion 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    #pokemons = Pokemon.objects.all() ## SELECT * FROM pokedex_pokemon
    pokemons = Pokemon.objects.order_by('type') ## SELECT * FROM pokedex_pokemon ORD
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

 
def pokemon(request, pokemon_id):
    #SELECT * FROM pokedex_pokemon WHERE id='pokemon_id'
    pokemon = get_object_or_404(Pokemon,id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

@login_required    
def add_pokemon(request):
    if request.method=='POST':
        form= PokemonFor(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
    
        form = PokemonFor()
        
    return render(request,"pokemon_form.html",{'form': form }) 

def edit_pokemon(request, id):
    pokemon= get_object_or_404(Pokemon, pk =id)
    if request.method=='POST':
        form= PokemonFor(request.POST ,request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
    
        form = PokemonFor()
        
    return render(request,"pokemon_form.html",{'form': form }) 

@login_required
def delete_pokemon(request,id):
    pokemon=get_object_or_404(Pokemon,pk=id)
    pokemon.delete()
    return redirect('pokdex:index')

class CustomLoginView(LoginView):
    template_name="login.html"
       
