from rest_framework import serializers
from .models import Product, Review, Director


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars']


class ProductSerializer(serializers.ModelSerializer):
    all_reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'all_reviews', 'rating']

    def get_rating(self, obj):
        reviews = obj.all_reviews.all()
        if reviews.exists():
            return round(reviews.aggregate(models.Avg('stars'))['stars__avg'], 2)
        return 0


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField()

    class Meta:
        model = Director
        fields = ['name', 'movies_count']
