from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import CategoryViewSet, MenuItemViewSet, OrderViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('menu-items', MenuItemViewSet, basename='menu-item')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
