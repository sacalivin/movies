from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies
def movies(request):
    data = Movies.objects.all()
    return render(request, 'movies/movies.html', {'movies':data})

def home(request):
    return HttpResponse("Home page")

def details(request, id):
    data = Movies.objects.get(pk=id)
    return render(request, 'movies/details.html', {'movie':data})

def add(request):
    return render(request, "movies/add.html", )