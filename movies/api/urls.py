from django.urls import path, include  # new
from movies.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path("list/", MovieListAV.as_view(), name="movie-list"),
    path("detail/<int:pk>/", MovieDetailAV.as_view(), name="movie-detail"),
]
