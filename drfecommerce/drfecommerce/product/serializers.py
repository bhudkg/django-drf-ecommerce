from rest_framework import serializers
from .models import Category, Brand, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        exclude = ("id", "lft", "rght", "tree_id", "level", "parent")


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductLine
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        # fields = ["name", "description", "is_digital", "brand", "category", "is_active"]
        fields = "__all__"
