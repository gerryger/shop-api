from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "category", "category_name", "name", "description", "price", "stock", "is_active", "created_at"]

    def get_category_name(self, obj):
        return obj.category.name
