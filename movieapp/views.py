from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Movie
from .forms import MovieSearchForm

# Create your views here.
def movie_list(request):
    movies = Movie.objects.filter(year__gte=2000).order_by('-year', 'title')
    return render(request, 'movies/movie_list.html', {'movies': movies, 'list_title': 'Movie collection'})

def movie_detail(request, id):
    # try: 
    #     movie = Movie.objects.get(pk=id)
    #     return render(request, 'movies/movie_detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404(f"No movie with id {id}")
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_search(request):
    # TODO: use a template to show form and result
    if request.method == 'GET':
        # return form as html
        form = MovieSearchForm()
    elif request.method == 'POST':
        # handle form
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            q = Q(title__icontains=form.cleaned_data['title'])
            if form.cleaned_data['year']:
                q &= Q(year=form.cleaned_data['year'])
            # return redirect("movie_by_title", title=title)
            movies = Movie.objects.filter(q)
            return render(request, 'movies/movie_list.html', 
                          {'movies': movies, 'list_title': 'Movie search result'})
    return render(request, 'movies/movie_search_form.html', {'form': form})

# https://docs.djangoproject.com/fr/4.2/ref/request-response/

def demo_http_response(request):
    return HttpResponse("My custom response")

def demo_bad_request(request):
    return HttpResponseBadRequest("My custom response")


# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/
class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'year', 'duration'] #, 'director']

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'year', 'duration'] #, 'director']
    template_name_suffix = "_form_update"

# TODO: MovieDelete + confirm template