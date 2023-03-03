from .models import Movie
from .serializer import MovieSerializer
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
