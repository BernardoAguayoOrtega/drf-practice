from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from movies.models import Movie

from movies.api.serializers import MovieSerializer


class MovieListAV(APIView):
    def get(self, request):
        try:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movies not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(
                {"message": "Movie deleted successfully!"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )
