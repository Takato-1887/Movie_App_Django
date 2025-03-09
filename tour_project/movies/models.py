# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField(default="No overview available.")
    poster_path = models.CharField(max_length=255)
    backdrop_path = models.CharField(max_length=255, blank=True, null=True)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genre = models.CharField(max_length=50, default="all")

    def __str__(self):
        return self.title