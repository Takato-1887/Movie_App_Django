from django.core.management.base import BaseCommand
from movies.utils import fetch_popular_movies
from movies.models import Movie

class Command(BaseCommand):
    help = 'Populate the database with popular movies from TMDB'

    def handle(self, *args, **kwargs):
        movies = fetch_popular_movies()
        if movies:
            for movie_data in movies:
                Movie.objects.create(
                    title=movie_data['title'],
                    overview=movie_data['overview'],
                    poster_path=movie_data['poster_path'],
                    backdrop_path=movie_data['backdrop_path'],
                    vote_average=movie_data['vote_average'],
                    vote_count=movie_data['vote_count'],
                    genre=movie_data.get('genre', 'all'),  # Add genre field
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully added {movie_data["title"]}'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from TMDB'))