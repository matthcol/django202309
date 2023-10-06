from django.shortcuts import render
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.filter(year__gte=2000).order_by('-year', 'title')
    return render(request, 'movies/movie_list.html', {'movies': movies, 'list_title': 'Movie collection'})

def movie_detail(request, id):
    movie = Movie.objects.get(pk=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
