from .models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
