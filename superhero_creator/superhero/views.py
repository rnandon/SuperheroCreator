from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Superhero

# Create your views here.


def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superhero/index.html', context)