from django.http import JsonResponse

# Create your views here.
from .models import Movie

def MovieListView(request):
    movies = Movie.objects.all()
    print(movies.values())
    
    return JsonResponse({"movies": list(movies.values())})

def MovieDetailView(request, pk):
    movie = Movie.objects.get(pk=pk)
    return JsonResponse({"movie": {
        "title": movie.title,
        "description": movie.description,
        "year": movie.year,
        "active": movie.active,
    }})