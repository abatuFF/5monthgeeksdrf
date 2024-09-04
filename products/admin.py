from django.contrib import admin
from .models import Product, Category, SearchTag, Review


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SearchTag)
admin.site.register(Review)
