from unicodedata import category
from rest_framework import serializers
from .models import Order, Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['price', 'id', 'imageUrl', 'name', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imageUrl', 'id', ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'id', 'phone', 'time', 'product']
