from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_index, name='email_index'),
    path('test-simple-email/', views.send_simple_test_email, name='send_simple_test_email'),
    path('send-password-reset/<str:user_email>/', views.send_password_reset_email, name='send_password_reset_email'),
    path('send-password-reset/', views.send_password_reset_email, name='send_password_reset_email_default'),
    path('send-order-confirmation/<str:user_email>/', views.send_order_confirmation_email, name='send_order_confirmation_email'),
    path('send-order-confirmation/', views.send_order_confirmation_email, name='send_order_confirmation_email_default'),
    path('send-ipl-welcome/<str:user_email>/', views.send_ipl_welcome_email, name='send_ipl_welcome_email'),
    path('send-ipl-welcome/', views.send_ipl_welcome_email, name='send_ipl_welcome_email_default'),
]
