from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.


def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superhero/index.html', context)

def detail(request, hero_id):
    try:
        selected_hero = Superhero.objects.get(pk=hero_id)
        context = {
            "selected_hero": selected_hero
        }
        return render (request, 'superhero/detail.html', context)
    except:
        return index(request)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_super_ability = request.POST.get('primary_super_ability')
        secondary_super_ability = request.POST.get('secondary_super_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego_name=alter_ego_name, primary_super_ability=primary_super_ability, secondary_super_ability=secondary_super_ability, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superhero:index'))
    else:
        return render(request, 'superhero/create.html')