from django.http import JsonResponse

# Create your views here.
from .models import Movie
from django.core.exceptions import ObjectDoesNotExist

def MovieListView(request):
    movies = Movie.objects.all()
    print(movies.values())
    
    return JsonResponse({"movies": list(movies.values())})

def MovieDetailView(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Movie not found"}, status=404)
    
    return JsonResponse({"movie": {
        "title": movie.title,
        "description": movie.description,
        "year": movie.year,
        "active": movie.active,
    }})