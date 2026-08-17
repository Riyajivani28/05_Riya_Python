from django.urls import path
from .views import (
    RestaurantListCreateAPIView,
    RestaurantDetailAPIView,
    RestaurantListCreateMixinView,
    RestaurantDetailMixinView,
)

urlpatterns = [
    # Refactored CRUD API using DRF GenericAPIView and Mixins
    path('restaurants/', RestaurantListCreateMixinView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetailMixinView.as_view(), name='restaurant-detail'),

    # CRUD API using DRF APIView
    path('restaurants/apiview/', RestaurantListCreateAPIView.as_view(), name='restaurant-apiview-list-create'),
    path('restaurants/apiview/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-apiview-detail'),
]
