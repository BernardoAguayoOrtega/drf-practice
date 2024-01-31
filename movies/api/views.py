from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from movies.models import Movie

from movies.api.serializers import MovieSerializer


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)


@api_view()
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)

    return Response(serializer.data)
