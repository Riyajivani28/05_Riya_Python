from rest_framework import serializers

# AI Prompt used with ChatGPT/Copilot:
# "Write a basic Serializer class in Django REST Framework for a Zomato-style Restaurant object with fields 'name' and 'cuisine'."

class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cuisine = serializers.CharField(max_length=100)