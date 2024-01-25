from django.urls import path, include # new
from .views import MovieListView, MovieDetailView # new

urlpatterns = [
    path('list/', MovieListView, name="movie-list"), # new
    path("<int:pk>/", MovieDetailView, name="movie-detail"), # new
]
