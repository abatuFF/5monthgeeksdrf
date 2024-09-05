from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django.db import models
from .models import Product, Review, Director
from .serializers import ProductSerializer, ReviewSerializer, DirectorSerializer


# Просмотр фильмов с отзывами и рейтингом
class MovieReviewsView(GenericAPIView):
    queryset = Product.objects.all().annotate(rating=models.Avg('all_reviews__stars'))
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


# Просмотр списка и создание режиссеров
class DirectorsView(ListCreateAPIView):
    queryset = Director.objects.all().annotate(movies_count=models.Count('movies'))
    serializer_class = DirectorSerializer


# Получение, обновление и удаление конкретного режиссера
class DirectorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


# Просмотр списка фильмов и создание новых
class MoviesView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Получение, обновление и удаление конкретного фильма
class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


# Просмотр списка отзывов и создание новых
class ReviewsView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Получение, обновление и удаление конкретного отзыва
class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
