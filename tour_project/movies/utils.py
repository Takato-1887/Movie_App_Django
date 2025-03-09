# movies/utils.py
import requests
from django.conf import settings

TMDB_API_KEY = settings.TMDB_API_KEY
TMDB_ACCESS_TOKEN = settings.TMDB_ACCESS_TOKEN
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

def fetch_popular_movies():
    url = f'{TMDB_BASE_URL}/movie/popular'
    headers = {
        'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}',
        'accept': 'application/json',
    }
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'page': 1,  # Fetch the first page of results
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        movies = response.json().get('results', [])[:20]  # Return the first 20 movies
        for movie in movies:
            movie['genre'] = 'all'  # Add a default genre
        return movies
    return None