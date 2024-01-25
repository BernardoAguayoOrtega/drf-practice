from django.urls import path, include # new
from .views import MovieListView

urlpatterns = [
    path('list/', MovieListView, name="movie-list"), # new
]
