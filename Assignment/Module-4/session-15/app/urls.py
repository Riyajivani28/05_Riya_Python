from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_redirect, name='index'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('place-order/<int:product_id>/', views.place_order, name='place_order_product'),
    path('place-order/', views.place_order, name='place_order'),
    path('update-order-status/<int:pk>/', views.update_order_status, name='update_order_status'),
    path('post-product/', views.post_product, name='post_product'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('movie-reviews/', views.movie_reviews, name='movie_reviews'),
    path('add-review/', views.add_review, name='add_review'),
    path('edit-review/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:pk>/', views.delete_review, name='delete_review'),
    path('permission-denied/', views.custom_permission_denied_view, name='permission_denied'),
]
