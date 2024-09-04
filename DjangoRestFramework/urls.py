from django.urls import path
from products.views import movie_reviews_view, directors_view

urlpatterns = [
    path('api/v1/movies/reviews/', movie_reviews_view, name='movie-reviews'),
    path('api/v1/directors/', directors_view, name='directors-list'),
]
