from django.http import JsonResponse

# Create your views here.
from .models import Movie

def MovieListView(request):
    movies = Movie.objects.all()
    print(movies.values())
    
    return JsonResponse({"movies": list(movies.values())})