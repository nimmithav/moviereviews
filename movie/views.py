from django.shortcuts import render
from .models import Movie
from django.shortcuts import get_object_or_404


def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html',
      {'searchTerm':searchTerm, 'movies': movies})


def search(request):
    return render(request, 'search.html', {'name': 'Nimmi'})


def about(request):
    return render(request, 'about.html', {'name': 'Nimmi'})


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'detail.html',
      {'movie':movie})
