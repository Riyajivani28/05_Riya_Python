from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard_view, name='dashboard'),

    # Restaurant Management (Task 1)
    path('restaurants/', views.restaurant_list_view, name='restaurants'),
    path('restaurants/add/', views.restaurant_add_view, name='restaurant_add'),
    path('restaurants/edit/<int:pk>/', views.restaurant_edit_view, name='restaurant_edit'),
    path('restaurants/delete/<int:pk>/', views.restaurant_delete_view, name='restaurant_delete'),

    # User Management (Task 2)
    path('users/', views.user_list_view, name='users'),

    # Movie & Review Management (Task 3)
    path('movies/', views.movie_list_view, name='movies'),
    path('movies/add/', views.movie_add_view, name='movie_add'),
    path('reviews/add/', views.review_add_view, name='review_add'),

    # Category & Product Management (Task 4)
    path('products/', views.product_list_view, name='products'),
    path('categories/add/', views.category_add_view, name='category_add'),
    path('products/add/', views.product_add_view, name='product_add'),

    # Flipkart Shopping Page (Task 5)
    path('flipkart/', views.flipkart_shopping_view, name='flipkart'),
]
