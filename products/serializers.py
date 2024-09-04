from rest_framework import serializers
from .models import Product, Review, Director


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'product']

    def validate_stars(self, value):
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError("Stars must be between 1 and 5.")
        return value


class ProductSerializer(serializers.ModelSerializer):
    all_reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'text', 'price', 'category', 'tags', 'director', 'is_active', 'created', 'updated', 'all_reviews', 'rating']

    def get_rating(self, obj):
        reviews = obj.all_reviews.all()
        if reviews.exists():
            return round(reviews.aggregate(models.Avg('stars'))['stars__avg'], 2)
        return 0

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value
