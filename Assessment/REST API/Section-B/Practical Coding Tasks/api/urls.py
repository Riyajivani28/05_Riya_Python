from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListView,
    MenuItemListCreateView,
    MenuItemDetailView,
    OrderViewSet,
    MyOrdersView
)

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('menu-items/', MenuItemListCreateView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('my-orders/', MyOrdersView.as_view(), name='my-orders'),
    path('', include(router.urls)),
]
