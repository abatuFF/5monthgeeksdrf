from django.urls import path
from products.views import (
    MovieReviewsView, DirectorsView, DirectorDetailView,
    MoviesView, MovieDetailView, ReviewsView, ReviewDetailView
)
from registration.views import RegisterUserView, ConfirmUserView, LoginUserView

urlpatterns = [
    path('api/v1/movies/reviews/', MovieReviewsView.as_view(), name='movie-reviews'),
    path('api/v1/directors/', DirectorsView.as_view(), name='directors'),
    path('api/v1/directors/<int:id>/', DirectorDetailView.as_view(), name='director-detail'),
    path('api/v1/movies/', MoviesView.as_view(), name='movies'),
    path('api/v1/movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('api/v1/reviews/', ReviewsView.as_view(), name='reviews'),
    path('api/v1/reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),

    path('api/v1/users/register/', RegisterUserView.as_view(), name='register-user'),
    path('api/v1/users/confirm/', ConfirmUserView.as_view(), name='confirm-user'),
    path('api/v1/users/login/', LoginUserView.as_view(), name='login-user'),
]
