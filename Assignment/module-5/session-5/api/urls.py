from django.urls import path
from .views import (
    MusicWeatherView,
    FoodLocationView,
    CountryInfoView,
    GitHubReposView,
)

urlpatterns = [
    path('music-weather/<str:city>/', MusicWeatherView.as_view(), name='music-weather'),
    path('food-location/', FoodLocationView.as_view(), name='food-location'),
    path('country-info/<str:country_name>/', CountryInfoView.as_view(), name='country-info'),
    path('github-repos/<str:username>/', GitHubReposView.as_view(), name='github-repos'),
]

