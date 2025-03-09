# movies/views.py
from django.shortcuts import render
from movies.models import Movie  # Import Movie here

def index(request):
    movies = Movie.objects.all()[:20]  # Fetch the first 20 movies
    return render(request, 'movies/index.html', {'movies': movies})

def search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = []
    return render(request, 'movies/search_results.html', {'movies': movies})