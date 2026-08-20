from rest_framework import serializers
from .models import Category, MenuItem, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'category', 'is_available']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(required=False, allow_blank=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'item', 'quantity', 'status', 'user']

    def create(self, validated_data):
        # Default customer_name to username if logged in user exists, otherwise 'Guest Customer'
        if not validated_data.get('customer_name'):
            user = validated_data.get('user')
            if user:
                validated_data['customer_name'] = user.username
            else:
                validated_data['customer_name'] = 'Guest Customer'
        return super().create(validated_data)
