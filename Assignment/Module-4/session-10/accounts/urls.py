from django.urls import path
from . import views

urlpatterns = [
    path('', views.forgot_password_view, name='forgot_password'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password_alt'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
]
