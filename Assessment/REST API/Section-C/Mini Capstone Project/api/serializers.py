from rest_framework import serializers
from .models import Category, MenuItem, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Category name cannot be empty.")
        return value.strip()


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'category', 'is_available']

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Menu item name cannot be empty.")
        return value.strip()

    def validate_price(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'item', 'quantity', 'status', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate_quantity(self, value):
        if value is None or value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value
