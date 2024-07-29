
from django.http import HttpResponse
from django.template import loader

from pokedex.forms import PokemonFor, TrainerFor
from .models import Pokemon, Trainer
from django.shortcuts import get_object_or_404, redirect, render

#importacion de librearia de autenticacion 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    #pokemons = Pokemon.objects.all() ## SELECT * FROM pokedex_pokemon
    pokemons = Pokemon.objects.order_by('type') ## SELECT * FROM pokedex_pokemon ORD
    trainers = Trainer.objects.all
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons , 'trainers':trainers}, request))

 
def pokemon(request, pokemon_id):
    #SELECT * FROM pokedex_pokemon WHERE id='pokemon_id'
    pokemon = get_object_or_404(Pokemon,id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, trainer_id):
    #SELECT * trainer WHERE id='trainer_id'
    trainer = get_object_or_404(Trainer,id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
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

@login_required    
def add_trainer(request):
    if request.method=='POST':
        form= TrainerFor(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
    
        form = TrainerFor()
        
    return render(request,"trainer_form.html",{'form': form }) 




def edit_trainer(request, id):
    trainer= get_object_or_404(Pokemon, pk =id)
    if request.method=='POST':
        form= TrainerFor(request.POST ,request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
    
        form = TrainerFor()
        
    return render(request,"trainer_form.html",{'form': form }) 

@login_required
def delete_trainer(request,id):
    trainer=get_object_or_404(Trainer,pk=id)
    trainer.delete()
    return redirect('pokdex:index')


class CustomLoginView(LoginView):
    template_name="login.html"
       


