from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Restaurant
from .serializers import RestaurantSerializer
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Restaurant instances.
    - Uses LimitOffsetPagination as requested (Requirement 5).
    - PageNumberPagination class is also defined in pagination.py (Requirement 4).
    - Supports ordering by name and cuisine (Requirement 6).
    - Supports filtering by cuisine (Requirement 7).
    """
    queryset = Restaurant.objects.all().order_by('id')
    serializer_class = RestaurantSerializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['cuisine']
    ordering_fields = ['name', 'cuisine']
