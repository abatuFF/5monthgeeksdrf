from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from .models import Product, Director
from .serializers import ProductSerializer, DirectorSerializer


@api_view(['GET'])
def movie_reviews_view(request):
    products = Product.objects.filter(director__isnull=False)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all().annotate(movies_count=models.Count('movies'))
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)
