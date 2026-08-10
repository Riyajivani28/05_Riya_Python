from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('live-map/', views.live_map_search_view, name='live_map'),
    path('geocode/', views.geocode_view, name='geocode'),
    path('restaurant-location/', views.show_restaurant_location, name='restaurant_location'),
    path('nearby-cafes/', views.nearby_cafes_view, name='nearby_cafes'),
    path('pickup-points/', views.search_by_distance, name='pickup_search'),
]
