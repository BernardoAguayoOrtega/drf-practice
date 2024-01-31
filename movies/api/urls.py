from django.urls import path, include # new
from movies.api.views import movie_list, movie_detail

urlpatterns = [
    path('list/', movie_list, name="movie-list"),
    path('detail/<int:pk>/', movie_detail, name="movie-detail")
]
