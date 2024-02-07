from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from movies.models import Movie

from movies.api.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    if request.method == "GET":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return JsonResponse({"message": "Movie deleted successfully!"}, status=204)
