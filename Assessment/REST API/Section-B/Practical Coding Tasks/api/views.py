from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Category, MenuItem, Order
from .serializers import CategorySerializer, MenuItemSerializer, OrderSerializer


# TASK 1: Food Category Listing API
class CategoryListView(generics.ListAPIView):
    """
    GET /api/categories/
    Read-only DRF endpoint returning all food categories.
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = None


# TASK 2: Menu Item CRUD API
class MenuItemListCreateView(APIView):
    """
    GET /api/menu-items/  - List all menu items
    POST /api/menu-items/ - Create a new menu item
    """
    permission_classes = [AllowAny]

    def get(self, request):
        items = MenuItem.objects.all().order_by('id')
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuItemDetailView(APIView):
    """
    GET /api/menu-items/<id>/    - Retrieve menu item detail
    PUT /api/menu-items/<id>/    - Update menu item
    DELETE /api/menu-items/<id>/ - Delete menu item
    """
    permission_classes = [AllowAny]

    def get_object(self, pk):
        return get_object_or_404(MenuItem, pk=pk)

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = MenuItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TASK 3: Order Listing with ModelViewSet, DefaultRouter, and Pagination
class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Order CRUD operations with pagination and status filtering.
    GET /api/orders/?status=pending
    """
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Order.objects.all().order_by('-id')
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset


# TASK 4: Token Authenticated Order Placement
class MyOrdersView(APIView):
    """
    GET /api/my-orders/  - Get authenticated user's orders only
    POST /api/my-orders/ - Place an order associated with authenticated user
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-id')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
