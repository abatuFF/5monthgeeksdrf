from django.urls import path
from products.views import (
    directors_view, director_detail_view,
    movies_view, movie_detail_view,
    reviews_view, review_detail_view
)
from registration.views import register_user, confirm_user, login_user

urlpatterns = [
    # Роуты для режиссёров
    path('api/v1/directors/', directors_view, name='directors-list'),
    path('api/v1/directors/<int:id>/', director_detail_view, name='director-detail'),

    # Роуты для фильмов
    path('api/v1/movies/', movies_view, name='movies-list'),
    path('api/v1/movies/<int:id>/', movie_detail_view, name='movie-detail'),

    # Роуты для отзывов
    path('api/v1/reviews/', reviews_view, name='reviews-list'),
    path('api/v1/reviews/<int:id>/', review_detail_view, name='review-detail'),

    # Дополнительный маршрут для отзывов о фильмах
    path('api/v1/movies/reviews/', reviews_view, name='movie-reviews'),

    path('api/v1/users/register/', register_user, name='register-user'),

    # Подтверждение пользователя
    path('api/v1/users/confirm/', confirm_user, name='confirm-user'),

    # Авторизация пользователя
    path('api/v1/users/login/', login_user, name='login-user'),
]
